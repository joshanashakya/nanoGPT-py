import argparse
import ast
import csv
import os
from pathlib import Path

from src.config import Config


def check_file(path):
    """Does Python accept this file? Returns (parses, message)."""
    source = Path(path).read_text(encoding="utf-8", errors="replace")
    try:
        ast.parse(source)
    except SyntaxError as error:
        return False, f"line {error.lineno}: {error.msg}"
    except (ValueError, RecursionError) as error:
        # for example a null byte in the source, or code nested too deeply
        return False, str(error)
    return True, ""


def list_files(directory):
    """Every file under a directory, in a fixed order (sub-folders included)."""
    files = []
    for folder, subfolders, names in os.walk(directory):
        subfolders.sort()
        files.extend(Path(folder) / name for name in sorted(names))
    return files


def parse_args():
    parser = argparse.ArgumentParser(description="Check whether the generated outputs are valid Python.")
    parser.add_argument(
        "directories",
        nargs="*",
        default=[f"{Config.ROOT_DIR}/phase2/outputs", f"{Config.ROOT_DIR}/phase3/outputs"],
        help="Folders with output files (default: phase2/outputs and phase3/outputs).",
    )
    parser.add_argument("--csv", help="Also write the results to this CSV file.")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    rows = []

    for directory in args.directories:
        files = list_files(directory)
        results = [(path, *check_file(path)) for path in files]

        for path, parses, message in results:
            print(f"{'yes' if parses else 'NO ':3}  {path.relative_to(directory)}  {message}")
            rows.append([str(directory), str(path.relative_to(directory)), "yes" if parses else "no", message])

        # one line per folder, and per group of probes when the folder has sub-folders
        print(f"\n{directory}: {sum(parses for _, parses, _ in results)} of {len(results)} parse")
        groups = {}
        for path, parses, _ in results:
            group = path.relative_to(directory).parent.name
            if group:
                groups.setdefault(group, []).append(parses)
        for group, flags in groups.items():
            print(f"  {group}: {sum(flags)} of {len(flags)}")
        print()

    if args.csv:
        with open(args.csv, "w", newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["directory", "file", "parses", "error"])
            writer.writerows(rows)
        print(f"Saved {args.csv}")
