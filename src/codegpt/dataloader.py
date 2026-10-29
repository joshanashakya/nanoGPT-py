
from pathlib import Path

import numpy as np
import torch
from torch.utils.data import Dataset, DataLoader
from src.codegpt.gptconfig import GPT_CONFIG
from src.config import Config


class CodeDataset(Dataset):
    def __init__(self, file_path, context_length=GPT_CONFIG["context_length"], random_offset=False):
        self.context_length = context_length
        self.random_offset = random_offset
        self.offset = 0

        # Load the encoded token IDs
        self.tokens = np.fromfile(
            Path(file_path), dtype=np.uint16
        ).astype(np.int64)

        if len(self.tokens) <= context_length:
            raise ValueError(
                f"Need more than {context_length} tokens, "
                f"but found {len(self.tokens)} in {file_path}"
            )

    def __len__(self):
        # Non-overlapping windows, so one epoch sees each token once.
        # The -1 leaves room for the shifted target of the last window.
        usable_tokens = len(self.tokens) - 1

        # With a random offset, reserve one window so a shifted last
        # window still fits.
        if self.random_offset:
            usable_tokens -= self.context_length

        return usable_tokens // self.context_length

    def new_random_offset(self):
        """Shift where the windows start, so each epoch cuts the code at
        different places."""
        if self.random_offset:
            self.offset = torch.randint(self.context_length, (1,)).item()

    def __getitem__(self, idx):
        start = self.offset + idx * self.context_length
        end = start + self.context_length

        # Input: one window of context_length tokens
        x = self.tokens[start:end]

        # Target: the same window shifted by one token
        y = self.tokens[start + 1:end + 1]

        return torch.from_numpy(x), torch.from_numpy(y)


class CodeDataLoader:
    def __init__(
        self,
        data_dir="tokenized",
        context_length=GPT_CONFIG["context_length"],
        batch_size=8,
        num_workers=0,
    ):
        self.data_dir = Path(data_dir)
        self.context_length = context_length
        self.batch_size = batch_size
        self.num_workers = num_workers

    def get_loader(self, split_name):
        is_train = split_name == "train"

        # Training windows start at a new random offset each epoch;
        # validation windows stay fixed so scores are comparable.
        dataset = CodeDataset(
            self.data_dir / f"{split_name}.bin",
            context_length=self.context_length,
            random_offset=is_train,
        )

        return DataLoader(
            dataset,
            batch_size=self.batch_size,
            shuffle=is_train,
            num_workers=self.num_workers,
            # Keep every validation window; drop the uneven last
            # training batch.
            drop_last=is_train,
        )

    def get_loaders(self):
        train_loader = self.get_loader("train")
        val_loader = self.get_loader("val")

        return train_loader, val_loader


if __name__ == "__main__":
    loader = CodeDataLoader(
        data_dir=f"{Config.PROCESSED_DATA_DIR}/tokenized",
        context_length=GPT_CONFIG["context_length"],
        batch_size=8,
    )

    train_loader, val_loader = loader.get_loaders()

    x, y = next(iter(train_loader))

    print("Input shape:", x.shape)
    print("Target shape:", y.shape)
    print("Training batches:", len(train_loader))
    print("Validation batches:", len(val_loader))
