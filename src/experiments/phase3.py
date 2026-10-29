import argparse
import re
from pathlib import Path

import torch
from tokenizers import Tokenizer

from src.codegpt.sample import complete, load_model
from src.config import Config
from src.experiments.phase2 import cut_function
from src.utils import common_utils

def write_prompts(jsonl_path, txt_path, count=5):
    """Write the first `count` prompts of a .jsonl file to a text file."""
    records = common_utils.read_jsonl(jsonl_path)[:count]

    with Path(txt_path).open("w", encoding="utf-8") as txt_file:
        for number, record in enumerate(records, start=1):
            txt_file.write(f"# ---------- {number}: {record['ID']} ----------\n")
            txt_file.write(record["Prompt"] + "\n\n")


def write_prompt_files(jsonl_path, output_dir, count=4):
    """Write the first `count` prompts of a .jsonl file as separate .py files, e.g. 01_yaml_load.py."""
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    for number, record in enumerate(common_utils.read_jsonl(jsonl_path)[:count], start=1):
        # name the file after the function the prompt asks the model to write
        function_name = re.findall(r"def (\w+)\(", record["Prompt"])[-1]
        file_path = output_dir / f"{number:02d}_{function_name}.py"

        # end with a newline so the model starts the body on a fresh line
        file_path.write_text(record["Prompt"] + "\n", encoding="utf-8")
        print(f"{file_path.name}  <-  {record['ID']}")


def parse_args():
    parser = argparse.ArgumentParser(description="Phase 3: run the model on every probe.")
    parser.add_argument("--checkpoint", default=f"{Config.CHECKPOINTS_DIR}/codegpt_baseline/best.pt")
    parser.add_argument("--tokenizer", default=f"{Config.PROCESSED_DATA_DIR}/tokenized/tokenizer.json")
    parser.add_argument("--probes-dir", default=f"{Config.ROOT_DIR}/phase3/probes")
    parser.add_argument("--outputs-dir", default=f"{Config.ROOT_DIR}/phase3/outputs")
    parser.add_argument("--max-new-tokens", type=int, default=256)
    parser.add_argument("--temperature", type=float, default=1.0)
    parser.add_argument("--top-k", type=int, default=50)
    parser.add_argument("--seed", type=int, default=1337)
    return parser.parse_args()


def run_probes(args):
    """Complete every probe in phase3/probes/<group>/ and save it to phase3/outputs/<group>/."""
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model, _ = load_model(args.checkpoint, device)
    tokenizer = Tokenizer.from_file(args.tokenizer)

    for group_dir in sorted(Path(args.probes_dir).iterdir()):
        output_dir = Path(args.outputs_dir) / group_dir.name
        output_dir.mkdir(parents=True, exist_ok=True)

        for probe_path in sorted(group_dir.iterdir()):
            prompt = probe_path.read_text(encoding="utf-8")

            # Same seed for every probe, so each output is reproducible on its own.
            torch.manual_seed(args.seed)
            completion = complete(
                model,
                tokenizer,
                prompt,
                device,
                max_new_tokens=args.max_new_tokens,
                temperature=args.temperature,
                top_k=args.top_k,
            )

            # Prompts that end inside a function are cut where the function ends;
            # script-style prompts (no def line) keep the whole completion.
            if any(line.lstrip().startswith("def ") for line in prompt.splitlines()):
                completion = cut_function(prompt, completion)

            (output_dir / probe_path.name).write_text(prompt + completion, encoding="utf-8")
            print(f"Saved {output_dir / probe_path.name}")


if __name__ == "__main__":
    run_probes(parse_args())
