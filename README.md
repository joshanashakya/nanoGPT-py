# nanoGPT-py

nanoGPT-py is a small GPT-style language model trained from scratch on Python code, with scripts to evaluate it, break it with probes and improve it with one change. The code is a fork of [nanoGPT](https://github.com/karpathy/nanoGPT) (MIT licence, see `LICENSE`).

## Project Organization

```
├── README.md          <- The top-level README for developers using this project.
├── DATA_SOURCES.md    <- The 30 training repositories and their licences.
├── data
│   ├── raw            <- The downloaded repositories and extracted .py files.
│   └── processed      <- Filtered corpus, train/val/test split and tokenized .bin files.
│                         NOTE: All files and dirs are ignored. So, these directories are created
│                         by the data scripts below.
│
├── config             <- gptconfig_<name>.json: model and training settings. GPT_CONFIG_NAME
│                         selects one (default: baseline).
│
├── models             <- Trained checkpoints (best.pt, last.pt), log.csv and test_results.json.
│
├── phase1             <- One prompt (inputs), the original function (references) and the completions of the baseline and each ablation (outputs).
├── phase2             <- The 20 real inputs, model outputs and sources (SOURCES.md).
├── phase3             <- The 24 probes, model outputs, sources and findings.csv.
├── phase4             <- Outputs of the Phase 4 model (8 layers) on the same probes.
│
├── report
│   └── figures        <- Generated graphics and figures to be used in reporting (loss plots).
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment.
│
└── src                <- Source code for use in this project.
    │
    ├── config.py               <- Store useful variables, paths and the config name.
    │
    ├── data                    <- Download, filter, deduplicate and split the training data.
    │   ├── collect_data.py     <- Downloads the 30 repositories and builds the corpus.
    │   └── make_dataset.py     <- 80/10/10 split per repository (seed 42).
    │
    ├── codegpt                 <- The model and everything around it.
    │   ├── model.py            <- The GPT model and text generation.
    │   ├── tokenizer.py        <- Byte-level BPE tokenizer (8,192) and .bin files.
    │   ├── char_tokenizer.py   <- Character-level tokenizer for the ablation.
    │   ├── dataloader.py       <- Reads the token files in windows.
    │   ├── gptconfig.py        <- Loads the JSON config.
    │   ├── train.py            <- Training loop; saves checkpoints and log.csv.
    │   ├── evaluate.py         <- Loss, accuracy and perplexity on a split.
    │   └── sample.py           <- Generates a completion from a checkpoint.
    │
    ├── experiments             <- Runs the model on the Phase 2 inputs and Phase 3 probes.
    │
    └── utils                   <- Helper scripts.
        ├── check_parse.py      <- Does each output parse as Python?
        ├── test_outputs.py     <- Simple tests on the outputs (runs generated code).
        └── plot_loss.py        <- Training and validation loss plots.
```

## Codebase Version
- Repository: `git@github.com:joshanashakya/nanoGPT-py.git`, branch `param-change`.

## Project Setup
### Prerequisites
- Python 3.12
- An NVIDIA GPU
- Install required dependencies:
```
pip install -r requirements.txt
```

## Running the Project
### 1. Phase 1: build the data
```
python -m src.data.collect_data      # download 30 repositories, filter, remove duplicates
python -m src.data.make_dataset      # 80/10/10 split per repository
python -m src.codegpt.tokenizer      # BPE tokenizer (train split only) and .bin files
```

### 2. Phase 1: train and evaluate the final model
```
python -m src.codegpt.train --checkpoint-dir models/codegpt
python -m src.codegpt.evaluate
```

### 3. Phase 1 ablations
The ablations were run on a smaller preliminary configuration (6 layers, 6 heads, width 384, context 512, 11 epochs, no dropout, 10-repository data kept in `data/processed`). Each ablation changes one thing from the preliminary baseline; the exact settings of every run are in its `run_config.json`.
```
python -m src.codegpt.train --checkpoint-dir models/codegpt
python -m src.codegpt.train --no-pos-emb   --checkpoint-dir models/codegpt_ablation_no_pos_emb
python -m src.codegpt.train --no-layer-norm --checkpoint-dir models/codegpt_ablation_no_layer_norm
python -m src.codegpt.train --num-heads 1  --checkpoint-dir models/codegpt_ablation_num_heads_1
python -m src.codegpt.train --num-layers 3 --checkpoint-dir models/codegpt_ablation_num_layers_3
python -m src.codegpt.train --context-length 256 --checkpoint-dir models/codegpt_ablation_context_length_256
```
(Later flags override earlier ones, so each ablation line replaces the matching setting in `$BASE`.) The character-level ablation needs its own tokenizer first: run `python -m src.codegpt.char_tokenizer`, then train with `--char-level`.

To compare generations, give every model the same prompt (`phase1/inputs/01_transform.py`) and save the completions to `phase1/outputs`:
```
python -m src.codegpt.sample --checkpoint models/codegpt_ablation_no_pos_emb/best.pt \
  --tokenizer data/processed/tokenized/tokenizer.json \
  --prompt-file phase1/inputs/01_transform.py
```

### 4. Generate code
```
python -m src.codegpt.sample --checkpoint models/codegpt/best.pt \
  --tokenizer data/processed/tokenized/tokenizer.json --prompt "def add(a, b):"
```
Generation settings used in all experiments: temperature 1.0, top-k 50, 256 new tokens, seed 1337.

### 5. Phase 2 and Phase 3
```
python -m src.experiments.phase2
python -m src.experiments.phase3 --checkpoint models/codegpt/best.pt --outputs-dir phase3/outputs
python -m src.utils.check_parse phase3/outputs
python -m src.utils.test_outputs --outputs-dir phase3/outputs
```
**Note:** `test_outputs.py` runs the generated code without a sandbox.

### 6. Phase 4 (8 layers, 15 epochs)
```
GPT_CONFIG_NAME=layers_8 python -m src.codegpt.train --checkpoint-dir models/codegpt_layers_8
python -m src.experiments.phase3 --checkpoint models/codegpt_layers_8/best.pt \
  --outputs-dir phase4/layers_8/outputs
```

### 7. Plots
```
python -m src.utils.plot_loss models/codegpt models/codegpt_layers_8 \
  --labels "Baseline" "8 layers" --output report/figures/loss_layers_8.png
```


