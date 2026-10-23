
from pathlib import Path
from collections import defaultdict
import random
import shutil
from src.config import Config
import os
from loguru import logger

class DataPipeline:
    def __init__(self, processed_dir, source_dir="corpus", output_dir="dataset_split", train_ratio=0.80, val_ratio=0.10, seed=42):
        self.source_dir = Path(os.path.join(processed_dir, source_dir))
        self.output_dir = Path(os.path.join(processed_dir, output_dir))
        self.train_ratio = train_ratio
        self.val_ratio = val_ratio
        self.seed = seed

        if not 0 <= train_ratio <= 1:
            raise ValueError("train_ratio must be between 0 and 1")
        if not 0 <= val_ratio <= 1:
            raise ValueError("val_ratio must be between 0 and 1")
        if train_ratio + val_ratio > 1:
            raise ValueError("train_ratio + val_ratio cannot exceed 1")

    def collect_files(self):
        """Group files by repository prefix."""
        repo_files = defaultdict(list)

        for path in sorted(self.source_dir.iterdir()):
            if path.is_file():
                repo_name = path.name.split("-", 1)[0]
                repo_files[repo_name].append(path)

        if not repo_files:
            raise ValueError(f"No files found in {self.source_dir.resolve()}")

        return repo_files

    def split_repo_files(self, repo_files):
        """Split files from every repository into all three sets."""
        splits = {"train": [], "val": [], "test": []}
        rng = random.Random(self.seed)

        for repo, files in sorted(repo_files.items()):
            # shuffle with a fixed seed so the split is reproducible
            files = sorted(files)
            rng.shuffle(files)

            logger.info(f"Splitting repository: {repo} with {len(files)} files")
            n = len(files)

            train_end = int(n * self.train_ratio)
            val_end = train_end + int(n * self.val_ratio)

            splits["train"].extend(files[:train_end])
            splits["val"].extend(files[train_end:val_end])
            splits["test"].extend(files[val_end:])

        return splits

    def save_splits(self, splits):
        """Copy files into their respective split directories."""
        # start from an empty directory so no stale files remain
        if self.output_dir.exists():
            shutil.rmtree(self.output_dir)
        for split_name, files in splits.items():
            split_dir = self.output_dir / split_name
            split_dir.mkdir(parents=True, exist_ok=True)

            file_count = 0

            for filepath in files:
                shutil.copy2(filepath, split_dir / filepath.name)
                file_count += 1

            logger.info(f"{split_name}: {len(files)} files, "f"{file_count} files copied")

    def run(self):
        """Execute the complete splitting pipeline."""
        repo_files = self.collect_files()
        splits = self.split_repo_files(repo_files)
        self.save_splits(splits)

        print(f"\nTotal repositories: {len(repo_files)}")
        print(f"Output directory: {self.output_dir.resolve()}")


if __name__ == "__main__":
    pipeline = DataPipeline(Config.PROCESSED_DATA_DIR)
    pipeline.run()
