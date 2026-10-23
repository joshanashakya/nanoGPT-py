
from loguru import logger
from pathlib import Path

import numpy as np
from tokenizers import Tokenizer
from tokenizers import decoders, models, pre_tokenizers, trainers
from src.config import Config


class CodeTokenizer:
    def __init__(self, split_dir="dataset_split", output_dir="tokenized", vocab_size=8192):
        self.split_dir = Path(split_dir)
        self.output_dir = Path(output_dir)
        self.vocab_size = vocab_size
        self.eos_token = "<|endoftext|>"
        self.tokenizer = None

    def get_files(self, split_name):
        """Collect Python files from a dataset split."""
        split_path = self.split_dir / split_name

        # Sorted so the tokenizer and the .bin files are built in the same order on every machine.
        files = sorted(split_path.iterdir())

        return files

    def train(self):
        """Train BPE tokenizer on training files only."""
        train_files = self.get_files("train")

        self.tokenizer = Tokenizer(models.BPE())

        # With True, every file would be tokenized as if it began with a space. 
        # Code at the start of a line normally has no leading space
        self.tokenizer.pre_tokenizer = pre_tokenizers.ByteLevel(add_prefix_space=False)
        self.tokenizer.decoder = decoders.ByteLevel()

        trainer = trainers.BpeTrainer(
            vocab_size=self.vocab_size,
            special_tokens=[self.eos_token],
            initial_alphabet=pre_tokenizers.ByteLevel.alphabet(),
        )

        self.tokenizer.train(
            files=[str(path) for path in train_files],
            trainer=trainer,
        )

        self.output_dir.mkdir(parents=True, exist_ok=True)

        tokenizer_path = self.output_dir / "tokenizer.json"
        self.tokenizer.save(str(tokenizer_path))

        logger.info(f"Tokenizer trained on {len(train_files)} files.")
        logger.info(f"Vocabulary size: {self.tokenizer.get_vocab_size()}")
        logger.info(f"Saved tokenizer to {tokenizer_path}")

    def encode_split(self, split_name):
        """Encode a split and save token IDs as a binary file."""
        if self.tokenizer is None:
            raise RuntimeError("Train the tokenizer before encoding.")

        files = self.get_files(split_name)
        output_path = self.output_dir / f"{split_name}.bin"
        eos_id = self.tokenizer.token_to_id(self.eos_token)

        total_tokens = 0

        with output_path.open("wb") as output_file:
            for path in files:
                code = path.read_text(
                    encoding="utf-8",
                    errors="replace",
                )
                token_ids = self.tokenizer.encode(code).ids
                token_ids.append(eos_id)

                np.asarray(token_ids, dtype=np.uint16).tofile(
                    output_file
                )
                total_tokens += len(token_ids)

        print(
            f"{split_name}: {len(files)} files, "
            f"{total_tokens:,} tokens -> {output_path}"
        )

    def run(self):
        """Train tokenizer and encode all dataset splits."""
        self.train()

        for split_name in ("train", "val", "test"):
            self.encode_split(split_name)


if __name__ == "__main__":
    tokenizer = CodeTokenizer(
        split_dir=f"{Config.PROCESSED_DATA_DIR}/dataset_split",
        output_dir=f"{Config.PROCESSED_DATA_DIR}/tokenized",
        vocab_size=8192,
    )
    tokenizer.run()
