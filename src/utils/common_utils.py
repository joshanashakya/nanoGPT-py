import json
from pathlib import Path


def read_jsonl(file_path):
    """Read a .jsonl file: one JSON object per line."""
    with Path(file_path).open(encoding="utf-8") as jsonl_file:
        return [json.loads(line) for line in jsonl_file if line.strip()]


