import argparse
import csv
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from src.config import Config


def read_log(run_dir):
    """Read log.csv of a training run (one row per epoch). Returns epochs, train losses, validation losses."""
    with (Path(run_dir) / "log.csv").open(newline="") as log_file:
        rows = list(csv.DictReader(log_file))

    epochs = [int(row["epoch"]) for row in rows]
    train_loss = [float(row["train_loss"]) for row in rows]
    val_loss = [float(row["val_loss"]) for row in rows]
    return epochs, train_loss, val_loss


def plot_runs(run_dirs, labels, output_path, title, y_max=None):
    """Plot training (dashed) and validation (solid) loss per epoch, one colour per run."""
    colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]
    figure, axis = plt.subplots(figsize=(6.5, 4.2))

    for index, (run_dir, label) in enumerate(zip(run_dirs, labels)):
        epochs, train_loss, val_loss = read_log(run_dir)
        color = colors[index % len(colors)]

        axis.plot(epochs, train_loss, linestyle="--", color=color, label=f"{label} (train)")
        axis.plot(epochs, val_loss, linestyle="-", marker="o", markersize=3, color=color, label=f"{label} (validation)")

        # star = epoch with the lowest validation loss, the checkpoint that is kept (best.pt)
        best = min(range(len(val_loss)), key=val_loss.__getitem__)
        axis.scatter(epochs[best], val_loss[best], marker="*", s=110, color=color, zorder=3)

    axis.set_xlabel("Epoch")
    axis.set_ylabel("Cross-entropy loss")
    axis.set_title(title)
    if y_max is not None:
        axis.set_ylim(top=y_max)
    axis.grid(True, alpha=0.3)
    axis.legend(fontsize=8)

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    figure.tight_layout()
    figure.savefig(output_path, dpi=200)
    print(f"Saved {output_path}")


def parse_args():
    parser = argparse.ArgumentParser(description="Plot training and validation loss from log.csv files.")
    parser.add_argument("runs", nargs="+", help="Run folders that contain a log.csv, e.g. models/codegpt.")
    parser.add_argument("--labels", nargs="+", help="One label per run (default: the folder names).")
    parser.add_argument("--title", default="Training and validation loss")
    parser.add_argument("--y-max", type=float, help="Upper limit of the y axis, to cut off the high first epochs.")
    parser.add_argument("--output", default=f"{Config.REPORTS_FIG_DIR}/loss_curve.png",
                        help="Image file to write; the extension (.png, .pdf, .svg) sets the format.")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    labels = args.labels or [Path(run).name for run in args.runs]
    if len(labels) != len(args.runs):
        raise SystemExit("Give one --labels entry per run.")

    plot_runs(args.runs, labels, args.output, args.title, args.y_max)
