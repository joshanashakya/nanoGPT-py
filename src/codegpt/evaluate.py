import argparse
import math
from contextlib import nullcontext
from pathlib import Path

import numpy as np
import torch

from src.codegpt.sample import checkpoint_position, load_model
from src.config import Config


@torch.no_grad()
def evaluate_split(model, token_path, device, batch_size=32):
    """Mean loss over every non-overlapping window of a split."""
    context_length = model.config["context_length"]
    tokens = np.fromfile(Path(token_path), dtype=np.uint16).astype(np.int64)

    # Each window needs context_length inputs plus one shifted target.
    num_windows = (len(tokens) - 1) // context_length
    inputs = torch.from_numpy(
        tokens[:num_windows * context_length]
    ).view(num_windows, context_length)
    targets = torch.from_numpy(
        tokens[1:num_windows * context_length + 1]
    ).view(num_windows, context_length)

    if device == "cuda" and torch.cuda.is_bf16_supported():
        autocast = torch.autocast(device_type="cuda", dtype=torch.bfloat16)
    else:
        autocast = nullcontext()

    total_loss = 0.0
    for start in range(0, num_windows, batch_size):
        x = inputs[start:start + batch_size].to(device)
        y = targets[start:start + batch_size].to(device)

        with autocast:
            _, loss = model(x, y)

        # Weight each batch by its size so the last batch counts fairly.
        total_loss += loss.item() * x.size(0)

    mean_loss = total_loss / num_windows
    return mean_loss, num_windows * context_length


def parse_args():
    parser = argparse.ArgumentParser(
        description="Compute loss and perplexity over a full split."
    )
    parser.add_argument(
        "--checkpoint",
        default=f"{Config.CHECKPOINTS_DIR}/codegpt/best.pt",
    )
    parser.add_argument(
        "--data-dir",
        default=f"{Config.PROCESSED_DATA_DIR}/tokenized",
    )
    parser.add_argument(
        "--split", nargs="+", default=["val"],
        choices=["train", "val", "test"],
    )
    parser.add_argument("--batch-size", type=int, default=32)
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    device = "cuda" if torch.cuda.is_available() else "cpu"
    model, checkpoint = load_model(args.checkpoint, device)

    print(
        f"checkpoint: {args.checkpoint} "
        f"({checkpoint_position(checkpoint)})"
    )

    for split_name in args.split:
        loss, token_count = evaluate_split(
            model,
            Path(args.data_dir) / f"{split_name}.bin",
            device,
            batch_size=args.batch_size,
        )
        print(
            f"{split_name}: loss {loss:.4f}, "
            f"perplexity {math.exp(loss):.2f}, "
            f"{token_count:,} tokens"
        )
