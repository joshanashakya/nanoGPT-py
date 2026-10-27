import argparse
from pathlib import Path

import torch
from tokenizers import Tokenizer

from src.codegpt.sample import complete, load_model
from src.config import Config


def cut_function(prompt, completion):
    """Keep the completion only up to the end of the function being completed."""
    # indentation of the last def line in the prompt
    def_line = [line for line in prompt.splitlines() if line.lstrip().startswith("def ")][-1]
    def_indent = len(def_line) - len(def_line.lstrip())

    # the function ends at the first non-empty line indented no deeper than its def line
    kept = []
    for line in completion.split("\n"):
        if line.strip() and len(line) - len(line.lstrip()) <= def_indent:
            break
        kept.append(line)
    return "\n".join(kept).rstrip() + "\n"


def parse_args():
    parser = argparse.ArgumentParser(description="Phase 2: complete every input function with the model.")
    parser.add_argument("--checkpoint", default=f"{Config.CHECKPOINTS_DIR}/codegpt_baseline/best.pt")
    parser.add_argument("--tokenizer", default=f"{Config.PROCESSED_DATA_DIR}/tokenized/tokenizer.json")
    parser.add_argument("--inputs-dir", default=f"{Config.ROOT_DIR}/phase2/inputs")
    parser.add_argument("--outputs-dir", default=f"{Config.ROOT_DIR}/phase2/outputs")

    # Fixed generation settings, the same for every input
    # parser.add_argument("--max-new-tokens", type=int, default=150)
    # parser.add_argument("--temperature", type=float, default=0.3)
    # parser.add_argument("--top-k", type=int, default=50)
    # parser.add_argument("--seed", type=int, default=1337)
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    device = "cuda" if torch.cuda.is_available() else "cpu"
    model, _ = load_model(args.checkpoint, device)
    tokenizer = Tokenizer.from_file(args.tokenizer)

    outputs_dir = Path(args.outputs_dir)
    outputs_dir.mkdir(parents=True, exist_ok=True)

    # Sorted so the inputs run in the same order (01, 02, ...) every time.
    for input_path in sorted(Path(args.inputs_dir).iterdir()):
        prompt = input_path.read_text(encoding="utf-8")

        # Same seed for every input, so each output is reproducible on its own.
        # torch.manual_seed(args.seed)
        completion = complete(
            model,
            tokenizer,
            prompt,
            device,
            # max_new_tokens=args.max_new_tokens,
            # temperature=args.temperature,
            # top_k=args.top_k,
        )

        # Output file = prompt followed by the completed function.
        (outputs_dir / input_path.name).write_text(prompt + cut_function(prompt, completion), encoding="utf-8")
        print(f"Saved {outputs_dir / input_path.name}")
