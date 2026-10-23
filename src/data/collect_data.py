import subprocess
from src.config import Config
import requests
import zipfile
from pathlib import Path
import io
import os
import shutil
import ast
from loguru import logger
import numpy as np
import hashlib

class DataCollection:
    # (download URL, folder name after extracting the zip)
    REPOS = [
        ("https://github.com/scikit-learn/scikit-learn/archive/refs/heads/main.zip", "scikit-learn-main"),
        ("https://github.com/mwaskom/seaborn/archive/refs/heads/master.zip", "seaborn-master"),
        ("https://github.com/matplotlib/matplotlib/archive/refs/heads/main.zip", "matplotlib-main"),
        ("https://github.com/numpy/numpy/archive/refs/heads/main.zip", "numpy-main"),
        ("https://github.com/pandas-dev/pandas/archive/refs/heads/main.zip", "pandas-main"),
        ("https://github.com/statsmodels/statsmodels/archive/refs/heads/main.zip", "statsmodels-main"),
        ("https://github.com/nltk/nltk/archive/refs/heads/develop.zip", "nltk-develop"),
        ("https://github.com/scipy/scipy/archive/refs/heads/main.zip", "scipy-main"),
        ("https://github.com/py-why/dowhy/archive/refs/heads/main.zip", "dowhy-main"),
        ("https://github.com/optuna/optuna/archive/refs/heads/master.zip", "optuna-master")
    ]

    def __init__(self, data_dir: str, processed_data_dir: str = None):
        self.data_dir = data_dir
        self.raw_corpus_dir = os.path.join(data_dir, "corpus")
        self.processed_corpus_dir = os.path.join(processed_data_dir, "corpus")
        self.data = []

    def download(self):
        destination = Path(self.data_dir)
        destination.mkdir(parents=True, exist_ok=True)

        for url, folder in self.REPOS:
            # skip repositories that were already downloaded
            if (destination / folder).exists():
                logger.info(f"Already downloaded: {folder}")
                continue

            logger.info(f"Downloading {url}")
            response = requests.get(url, timeout=120)
            response.raise_for_status()
            with zipfile.ZipFile(io.BytesIO(response.content)) as z:
                z.extractall(destination)

    def extract(self):
        Path(self.raw_corpus_dir).mkdir(parents=True, exist_ok=True)

        for _, folder in self.REPOS:
            folder_path = Path(os.path.join(self.data_dir, folder))
            for filepath in folder_path.rglob("*.py"):
                if filepath.is_file():
                    # get the full path relative to the source directory
                    relative_path = filepath.relative_to(folder_path)

                    # replace directory separators with hyphens
                    new_name = f"{folder}-{str(relative_path).replace("/", "-").replace("\\", "-")}"

                    # copy and rename the file
                    shutil.copy2(filepath, f"{self.raw_corpus_dir}/{new_name}")

    def check_metadata(self):
        dirs = os.listdir(self.raw_corpus_dir)
        file_count, total_lines, non_empty_lines, parsed_count = 0, 0, 0, 0
        file_sizes = {}

        for d in dirs:
            file_path = os.path.join(self.raw_corpus_dir, d)
            if not os.path.isfile(file_path):
                continue
            file_count += 1
            file_sizes[d] = os.path.getsize(file_path)
            try:
                content = Path(file_path).read_text(encoding="utf-8", errors="replace")
                source = ast.parse(content)
                parsed_count += 1
            except (OSError, SyntaxError):
                continue
            lines = content.splitlines()
            total_lines += len(lines)
            non_empty_lines += sum(1 for line in lines if line.strip())

        zero_files = [f for f, size in file_sizes.items() if size == 0]

        logger.info(f"Number of files: {file_count}")
        logger.info(f"Total size of files: {sum(file_sizes.values())} bytes")
        logger.info(f"Minimum file size: {min(file_sizes.values())} bytes")
        logger.info(f"Maximum file size: {max(file_sizes.values())} bytes")
        logger.info(f"Average file size: {sum(file_sizes.values()) / len(file_sizes)} bytes")
        logger.info(f"Median file size: {sorted(file_sizes.values())[len(file_sizes) // 2]} bytes")
        logger.info(f"Standard deviation of file sizes: {np.std(list(file_sizes.values()))} bytes")
        logger.info(f"5 percentile file size: {np.percentile(list(file_sizes.values()), 5)} bytes")
        logger.info(f"99 percentile file size: {np.percentile(list(file_sizes.values()), 99)} bytes")
        logger.info(f"Total lines of code: {total_lines}")
        logger.info(f"Total non-empty lines of code: {non_empty_lines}")
        logger.info(f"Number of parsed files: {parsed_count}")
        logger.info(f"Number of files with zero size: {len(zero_files)}")
        logger.info(f"Files with zero size: {zero_files}")

    
    def filter_files(self):
        # sorted so deduplication keeps the same copy on every machine
        files = [(path, path.stat().st_size) for path in sorted(Path(self.raw_corpus_dir).iterdir())]

        sizes = [size for path, size in files]

        # remove files that are too small or too large outlier files
        p5 = np.percentile(sizes, 5)
        p99 = np.percentile(sizes, 99)

        outliers = {path for path, size in files if size < p5 or size > p99}
        candidates = [(path, size) for path, size in files if path not in outliers]

        logger.info(f"P5 size threshold: {p5:.2f} bytes")
        logger.info(f"P99 size threshold: {p99:.2f} bytes")
        logger.info(f"Files excluded: {len(outliers)}")
        logger.info(f"Files remaining: {len(candidates)}")

        # remove duplicates using hash
        seen_hashes = set()
        unique_files = []

        for path, size in candidates:
            file_hash = hashlib.sha256(path.read_bytes()).hexdigest()

            if file_hash not in seen_hashes:
                seen_hashes.add(file_hash)
                unique_files.append((path, size))

        logger.info(f"Files before deduplication: {len(candidates)}")
        logger.info(f"Unique files remaining: {len(unique_files)}")
        logger.info(f"Duplicates removed: {len(candidates) - len(unique_files)}")

        # store candidate files in processed directory
        # start from an empty directory so no stale files remain
        processed_dir = Path(self.processed_corpus_dir)
        if processed_dir.exists():
            shutil.rmtree(processed_dir)
        processed_dir.mkdir(parents=True)

        for path, size in unique_files:
            shutil.copy2(path, processed_dir / path.name)

        logger.info(f"Saved {len(unique_files)} files to {processed_dir.resolve()}")

    def collect_data(self):
        # download repos
        self.download()

        # extract python files
        self.extract()

        # check file sizes or length of codes
        self.check_metadata()

        # throw away files that are too small or too large outlier files
        self.filter_files()

if __name__ == "__main__":
    data_collector = DataCollection(Config.RAW_DATA_DIR, Config.PROCESSED_DATA_DIR)
    data_collector.collect_data()
    