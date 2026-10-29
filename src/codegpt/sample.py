import argparse
from pathlib import Path

import torch
from tokenizers import Tokenizer

from src.codegpt.model import GPTLanguageModel
from src.config import Config


def load_model(checkpoint_path, device):
    """Rebuild the model from a checkpoint saved by train.py."""
    checkpoint = torch.load(checkpoint_path, map_location=device)

    model_config = dict(checkpoint["model_config"])
    model_config.pop("dropout", None)

    # Checkpoints saved before position-embedding ablations always had them.
    model_config.setdefault("use_position_embeddings", True)

    # Checkpoints saved before the LayerNorm ablation always had LayerNorm.
    model_config.setdefault("use_layer_norm", True)

    model = GPTLanguageModel(model_config)
    model.load_state_dict(checkpoint["model"])
    model.to(device)
    model.eval()

    return model, checkpoint


def checkpoint_position(checkpoint):
    """Where training was when the checkpoint was saved."""
    # Epoch-based checkpoints store "epoch"; older ones store "iteration".
    if "epoch" in checkpoint:
        return f"epoch {checkpoint['epoch']}"
    return f"iteration {checkpoint['iteration']}"


def complete(
    model,
    tokenizer,
    prompt,
    device,
    max_new_tokens=200,
    temperature=0.8,
    top_k=50,
    eos_token="<|endoftext|>",
):
    """Generate a completion for a prompt, stopping at end-of-text."""
    prompt_ids = tokenizer.encode(prompt).ids
    input_ids = torch.tensor([prompt_ids], dtype=torch.long, device=device)

    output_ids = model.generate(
        input_ids,
        max_new_tokens=max_new_tokens,
        temperature=temperature,
        top_k=top_k,
    )[0].tolist()

    new_ids = output_ids[len(prompt_ids):]

    # Cut the completion at the first end-of-text token.
    eos_id = tokenizer.token_to_id(eos_token)
    if eos_id in new_ids:
        new_ids = new_ids[:new_ids.index(eos_id)]

    return tokenizer.decode(new_ids)


def parse_args():
    parser = argparse.ArgumentParser(
        description="Generate code completions from a trained model."
    )
    parser.add_argument(
        "--checkpoint",
        default=f"{Config.CHECKPOINTS_DIR}/codegpt/best.pt",
    )
    parser.add_argument(
        "--tokenizer",
        default=f"{Config.PROCESSED_DATA_DIR}/tokenized/tokenizer.json",
    )
    prompt_group = parser.add_mutually_exclusive_group(required=True)
    prompt_group.add_argument("--prompt", help="Prompt text.")
    prompt_group.add_argument(
        "--prompt-file", help="Read the prompt from a file."
    )
    parser.add_argument("--num-samples", type=int, default=1)
    parser.add_argument("--max-new-tokens", type=int, default=200)
    parser.add_argument("--temperature", type=float, default=0.8)
    parser.add_argument("--top-k", type=int, default=50)
    parser.add_argument("--seed", type=int, default=1337)
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    torch.manual_seed(args.seed)

    device = "cuda" if torch.cuda.is_available() else "cpu"
    model, checkpoint = load_model(args.checkpoint, device)
    tokenizer = Tokenizer.from_file(args.tokenizer)

    if args.prompt_file:
        prompt = Path(args.prompt_file).read_text(encoding="utf-8")
    else:
        prompt = args.prompt.encode().decode("unicode_escape")

    print(
        f"# checkpoint: {args.checkpoint} "
        f"({checkpoint_position(checkpoint)}, "
        f"val loss {checkpoint['best_val_loss']:.4f})"
    )

    for index in range(args.num_samples):
        completion = complete(
            model,
            tokenizer,
            prompt,
            device,
            max_new_tokens=args.max_new_tokens,
            temperature=args.temperature,
            top_k=args.top_k,
        )
        print(f"\n# ---------- sample {index + 1} ----------")
        print(prompt + completion)
