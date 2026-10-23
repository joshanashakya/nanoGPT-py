import argparse
import csv
import json
import math
import time
from contextlib import nullcontext
from pathlib import Path

import torch
from loguru import logger
from tokenizers import Tokenizer

from src.codegpt.dataloader import CodeDataLoader
from src.codegpt.gptconfig import GPT_CONFIG
from src.codegpt.model import GPTLanguageModel
from src.config import Config


class Trainer:
    def __init__(
        self,
        data_dir,
        checkpoint_dir,
        context_length=512,
        batch_size=32,
        embedding_dim=384,
        num_heads=6,
        num_layers=6,
        use_position_embeddings=True,
        epochs=11,
        learning_rate=3e-4,
        seed=1337,
    ):
        self.checkpoint_dir = Path(checkpoint_dir)
        torch.manual_seed(seed)

        # Device and precision: bfloat16 on GPUs that support it.
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        if self.device == "cuda" and torch.cuda.is_bf16_supported():
            self.autocast = torch.autocast("cuda", dtype=torch.bfloat16)
        else:
            self.autocast = nullcontext()

        # Data: non-overlapping windows of context_length tokens.
        loader = CodeDataLoader(
            data_dir=data_dir,
            context_length=context_length,
            batch_size=batch_size
        )
        self.train_loader, self.val_loader = loader.get_loaders()
        self.test_loader = loader.get_loader("test")

        # Model: vocabulary size comes from the tokenizer.
        tokenizer = Tokenizer.from_file(str(Path(data_dir) / "tokenizer.json"))
        self.model_config = {
            "vocab_size": tokenizer.get_vocab_size(),
            "context_length": context_length,
            "embedding_dim": embedding_dim,
            "num_heads": num_heads,
            "num_layers": num_layers,
            "use_position_embeddings": use_position_embeddings,
        }
        self.model = GPTLanguageModel(self.model_config).to(self.device)
        parameter_count = sum(p.numel() for p in self.model.parameters())
        tokens_per_epoch = len(self.train_loader) * batch_size * context_length
        self.epochs = epochs

        logger.info(f"Device: {self.device}")
        logger.info(f"Parameters: {parameter_count:,}")
        logger.info(f"Batches per epoch: {len(self.train_loader):,}")
        logger.info(f"Tokens per epoch: {tokens_per_epoch:,}")
        logger.info(f"Epochs: {self.epochs} ({self.epochs * tokens_per_epoch:,} tokens)")

        # Optimizer with a constant learning rate.
        self.learning_rate = learning_rate
        self.optimizer = torch.optim.AdamW(self.model.parameters(), lr=learning_rate)

        self.start_epoch = 1
        self.best_val_loss = float("inf")
        self.log_path = self.checkpoint_dir / "log.csv"

        # A new run starts a new log.
        self.log_path.unlink(missing_ok=True)


    def train_one_epoch(self):
        """One pass over the training data. Returns (loss, accuracy %)."""
        total_loss, total_correct, total_tokens = 0.0, 0, 0

        # Cut the training data into windows at a new place this epoch.
        self.train_loader.dataset.new_random_offset()

        self.model.train()
        for inputs, targets in self.train_loader:
            inputs = inputs.to(self.device)
            targets = targets.to(self.device)

            with self.autocast:
                logits, loss = self.model(inputs, targets)

            total_loss += loss.item()
            total_correct += (logits.argmax(dim=-1) == targets).sum().item()
            total_tokens += targets.numel()

            # backpropagation
            self.optimizer.zero_grad()
            loss.backward()
            self.optimizer.step()

        return total_loss / len(self.train_loader), 100 * total_correct / total_tokens

    @torch.no_grad()
    def evaluate(self, loader):
        """Loss and accuracy % over every window in a loader."""
        total_loss, total_correct, total_tokens = 0.0, 0, 0

        self.model.eval()
        for inputs, targets in loader:
            inputs = inputs.to(self.device)
            targets = targets.to(self.device)

            with self.autocast:
                logits, loss = self.model(inputs, targets)

            # Weight by token count so a smaller last batch counts fairly.
            total_loss += loss.item() * targets.numel()
            total_correct += (logits.argmax(dim=-1) == targets).sum().item()
            total_tokens += targets.numel()

        return total_loss / total_tokens, 100 * total_correct / total_tokens

    def train(self):
        """Train for all epochs, evaluating on validation after each."""
        for epoch in range(self.start_epoch, self.epochs + 1):
            start_time = time.time()

            train_loss, train_acc = self.train_one_epoch()
            val_loss, val_acc = self.evaluate(self.val_loader)

            logger.info(
                f"epoch {epoch}/{self.epochs} | "
                f"train loss {train_loss:.4f}, acc {train_acc:.2f}% | "
                f"val loss {val_loss:.4f}, acc {val_acc:.2f}%, ppl {math.exp(val_loss):.2f} | "
                f"lr {self.learning_rate:.2e} | "
                f"{time.time() - start_time:.1f}s"
            )
            self.log_epoch(epoch, train_loss, train_acc, val_loss, val_acc)

            if val_loss < self.best_val_loss:
                self.best_val_loss = val_loss
                self.save_checkpoint("best.pt", epoch)
            self.save_checkpoint("last.pt", epoch)

        logger.info(f"Training done. Best val loss: {self.best_val_loss:.4f}")

        self.test()

    def test(self):
        """Score the best checkpoint on the test split, once, after training.

        The test split is never used to choose epochs or settings; validation
        does that. This gives an unbiased final number for the report.
        """
        checkpoint = torch.load(self.checkpoint_dir / "best.pt", map_location=self.device)
        self.model.load_state_dict(checkpoint["model"])

        test_loss, test_acc = self.evaluate(self.test_loader)
        logger.info(
            f"test (best.pt, epoch {checkpoint['epoch']}) | "
            f"loss {test_loss:.4f}, acc {test_acc:.2f}%, ppl {math.exp(test_loss):.2f}"
        )

        results = {
            "best_epoch": checkpoint["epoch"],
            "val_loss": checkpoint["best_val_loss"],
            "test_loss": test_loss,
            "test_acc": test_acc,
            "test_perplexity": math.exp(test_loss),
        }
        (self.checkpoint_dir / "test_results.json").write_text(json.dumps(results, indent=2))

    def log_epoch(self, epoch, train_loss, train_acc, val_loss, val_acc):
        """Append one row per epoch to log.csv (for the loss curve)."""
        is_new = not self.log_path.exists()
        self.log_path.parent.mkdir(parents=True, exist_ok=True)

        with self.log_path.open("a", newline="") as log_file:
            writer = csv.writer(log_file)
            if is_new:
                writer.writerow(["epoch", "train_loss", "train_acc", "val_loss", "val_acc"])
            writer.writerow([epoch, train_loss, train_acc, val_loss, val_acc])

    def save_checkpoint(self, file_name, epoch):
        self.checkpoint_dir.mkdir(parents=True, exist_ok=True)
        checkpoint_path = self.checkpoint_dir / file_name

        torch.save(
            {
                "model": self.model.state_dict(),
                "optimizer": self.optimizer.state_dict(),
                "model_config": self.model_config,
                "epoch": epoch,
                "best_val_loss": self.best_val_loss,
            },
            checkpoint_path,
        )
        logger.info(f"Saved checkpoint to {checkpoint_path}")

    def load_checkpoint(self, file_name="last.pt"):
        """Resume from the end of the last saved epoch."""
        checkpoint_path = self.checkpoint_dir / file_name
        if not checkpoint_path.exists():
            logger.warning(f"No checkpoint at {checkpoint_path}, starting fresh.")
            return

        checkpoint = torch.load(checkpoint_path, map_location=self.device)
        self.model.load_state_dict(checkpoint["model"])
        self.optimizer.load_state_dict(checkpoint["optimizer"])
        self.start_epoch = checkpoint["epoch"] + 1
        self.best_val_loss = checkpoint["best_val_loss"]

        logger.info(f"Resumed from {checkpoint_path} after epoch {checkpoint['epoch']}")

    def save_run_config(self, run_config):
        """Record the full configuration for reproducibility."""
        self.checkpoint_dir.mkdir(parents=True, exist_ok=True)
        run_config = {
            **run_config,
            "epochs": self.epochs,
            "device": self.device,
            "model_config": self.model_config,
        }
        config_path = self.checkpoint_dir / "run_config.json"
        config_path.write_text(json.dumps(run_config, indent=2))


def parse_args():
    parser = argparse.ArgumentParser(description="Train a GPT-style model on Python code.")
    parser.add_argument("--data-dir", default=f"{Config.PROCESSED_DATA_DIR}/tokenized")
    parser.add_argument("--checkpoint-dir", default=f"{Config.CHECKPOINTS_DIR}/codegpt")

    # Model
    parser.add_argument("--context-length", type=int, default=GPT_CONFIG["context_length"])
    parser.add_argument("--embedding-dim", type=int, default=GPT_CONFIG["embedding_dim"])
    parser.add_argument("--num-heads", type=int, default=GPT_CONFIG["num_heads"])
    parser.add_argument("--num-layers", type=int, default=GPT_CONFIG["num_layers"])
    parser.add_argument("--no-pos-emb", action="store_true", help="Ablation: remove position embeddings.")

    # Training
    parser.add_argument("--batch-size", type=int, default=32)
    parser.add_argument("--epochs", type=int, default=11, help="No of epochs.")
    parser.add_argument("--learning-rate", type=float, default=3e-4)

    # Runtime
    parser.add_argument("--seed", type=int, default=1337)
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    trainer = Trainer(
        data_dir=args.data_dir,
        checkpoint_dir=args.checkpoint_dir,
        context_length=args.context_length,
        batch_size=args.batch_size,
        embedding_dim=args.embedding_dim,
        num_heads=args.num_heads,
        num_layers=args.num_layers,
        use_position_embeddings=not args.no_pos_emb,
        epochs=args.epochs,
        learning_rate=args.learning_rate,
        seed=args.seed,
    )
    trainer.save_run_config(vars(args))
    trainer.train()
