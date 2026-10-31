# Phase 4: 8 layers, 15 epochs

## Intervention

| Item | Value |
|---|---|
| Change | `num_layers` 6 → 8 and `epochs` 9 → 15 (data, tokenizer, context 1024, width 512, 8 heads, dropout 0.1, batch 32, lr 3e-4 and seed 1337 unchanged) |
| Config | `config/gptconfig_layers_8.json` |
| Train | `GPT_CONFIG_NAME=layers_8 python -m src.codegpt.train --checkpoint-dir models/codegpt_layers_8` |
| Probes | `python -m src.experiments.phase3 --checkpoint models/codegpt_layers_8/best.pt --outputs-dir phase4/layers_8/outputs` |
| Parse check | `python -m src.utils.check_parse phase3/outputs phase4/layers_8/outputs` |

## Before and after results

| | Baseline (6 layers, 9 epochs) | 8 layers, 15 epochs |
|---|---:|---:|
| Best epoch | 9 | 15 |
| Validation loss | 1.4694 | 1.3592 |
| Test loss | 1.4187 | 1.3056 |
| Test accuracy | 69.49% | 71.53% |
| Test perplexity | 4.13 | 3.69 |
| Probe outputs that parse | 12 of 24 | 12 of 24 |
| Empty answers | 5 | 6 |

Parses by group (baseline → 8 layers): ordinary 1 → 1, misleading 3 → 2, long context 4 → 4, security 1 → 3, prompt variations 2 → 1, training-like 1 → 1.

The loss is lower, but the generated code did not improve: the same 12 of 24 outputs parse and none does what its prompt asks.

### Per probe
The same table is in `phase4/before_after.csv`.

| Probe | Before (baseline) | After (8 layers) |
|---|---|---|
| long_context/01_soft_evaluate | parses | parses |
| long_context/02_ridge_plot | empty | empty |
| long_context/03_TestToPeriod | empty | empty |
| long_context/04_effectsize_oneway | parses | empty |
| misleading/01_tuple2str | empty | empty |
| misleading/02_prepare_data | empty | empty |
| misleading/03_below_zero | parses | parses |
| misleading/04_convert_to_line_delimits | parses | syntax error |
| ordinary/01_tuple2str | syntax error | syntax error |
| ordinary/02_prepare_data | empty | empty |
| ordinary/03_below_zero | parses | parses |
| ordinary/04_convert_to_line_delimits | syntax error | syntax error |
| prompt_variations/01_lemma_base | parses | syntax error |
| prompt_variations/02_lemma_reword | parses | syntax error |
| prompt_variations/03_lemma_w_code | syntax error | syntax error |
| prompt_variations/04_lemma_pos | syntax error | parses |
| security/01_yaml_load | syntax error | syntax error |
| security/02_parse_xml | parses | parses |
| security/03_profile | syntax error | parses |
| security/04_profile | syntax error | parses |
| training/01_num2date | syntax error | parses |
| training/02_binary_distance | parses | syntax error |
| training/03_log_base2 | syntax error | syntax error |
| training/04_optimize_qap | syntax error | syntax error |

## Files

| Path | Contents |
|---|---|
| `phase4/results/baseline/` | `log.csv`, `test_results.json`, `run_config.json` of `models/codegpt` (baseline) |
| `phase4/results/layers_8/` | the same three files for `models/codegpt_layers_8` |
| `phase3/outputs/` | probe outputs of the baseline (before) |
| `phase4/layers_8/outputs/` | probe outputs of the 8-layer model (after) |
