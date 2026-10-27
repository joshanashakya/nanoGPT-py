# Phase 2 input sources

Where each of the 20 Phase 2 inputs comes from, and its licence. Copied functions are used
unchanged, for evaluation only; copyright stays with the original authors.

- **01–10**: random functions from the held-out **test split** of the corpus, checked so that
  neither the `def` line nor the first docstring line appears in the train split. File names are
  the corpus names (`<repo>-<path with "/" replaced by "-">`), taken from the branch snapshot
  downloaded by `src/data/collect_data.py`.
- **11–15**: functions from my own repositories (not in the training corpus).
- **16–18**: HumanEvalComm tasks. Prompts are the task prompts; references are the canonical
  solutions.
- **19–20**: libraries outside the training corpus.

| ID | Function | Source | Licence |
|---|---|---|---|
| 01 | `estimate_gaussian_entropy` | dowhy: `dowhy/gcm/uncertainty.py`, line 62 | MIT |
| 02 | `add_floating_axis1` | matplotlib: `galleries/examples/axisartist/demo_axis_direction.py`, line 39 | Matplotlib licence (PSF-based) |
| 03 | `write_file` | numpy: `numpy/_core/code_generators/genapi.py`, line 315 | BSD-3-Clause |
| 04 | `tuple2str` | nltk: `nltk/tag/util.py`, line 34 | Apache-2.0 |
| 05 | `_preprocess` | scikit-learn: `sklearn/feature_extraction/text.py`, line 52 | BSD-3-Clause |
| 06 | `_range2cols` | pandas: `pandas/io/excel/_util.py`, line 137 | BSD-3-Clause |
| 07 | `get_RMSE` | statsmodels: `archive/examples/l1_demo/demo.py`, line 365 | BSD-3-Clause |
| 08 | `_as2d` | scipy: `scipy/sparse/linalg/_eigen/lobpcg/lobpcg.py`, line 47 | BSD-3-Clause |
| 09 | `_freedman_diaconis_bins` | seaborn: `seaborn/distributions.py`, line 2376 | BSD-3-Clause |
| 10 | `get_storage` | optuna: `optuna/storages/__init__.py`, line 41 | MIT |
| 11 | `_prepare_data` | own repository: TODO repo/file | TODO |
| 12 | `calculate_multilabel_confusion_matrix` | own repository: TODO repo/file | TODO |
| 13 | `concat_dir_dataframes` | own repository: TODO repo/file | TODO |
| 14 | `perform_rca` | own repository: TODO repo/file | TODO |
| 15 | `JunkProcessor.correct_spelling` | own repository: TODO repo/file | TODO |
| 16 | `has_close_elements` | HumanEval/0, https://github.com/openai/human-eval | MIT |
| 17 | `below_zero` | HumanEval/3, https://github.com/openai/human-eval | MIT |
| 18 | `count_distinct_characters` | HumanEval/16, https://github.com/openai/human-eval | MIT |
| 19 | `tokenize` | gensim: `gensim/utils.py` (branch `develop`, TODO commit), https://github.com/piskvorky/gensim | LGPL-2.1 |
| 20 | `check_documents_type` | BERTopic: `bertopic/_utils.py` (branch `master`, TODO commit), https://github.com/MaartenGr/BERTopic | MIT |

## Licence links

- dowhy (MIT): https://github.com/py-why/dowhy/blob/main/LICENSE
- matplotlib: https://github.com/matplotlib/matplotlib/blob/main/LICENSE/LICENSE
- numpy (BSD-3-Clause): https://github.com/numpy/numpy/blob/main/LICENSE.txt
- nltk (Apache-2.0): https://github.com/nltk/nltk/blob/develop/LICENSE.txt
- scikit-learn (BSD-3-Clause): https://github.com/scikit-learn/scikit-learn/blob/main/COPYING
- pandas (BSD-3-Clause): https://github.com/pandas-dev/pandas/blob/main/LICENSE
- statsmodels (BSD-3-Clause): https://github.com/statsmodels/statsmodels/blob/main/LICENSE.txt
- scipy (BSD-3-Clause): https://github.com/scipy/scipy/blob/main/LICENSE.txt
- seaborn (BSD-3-Clause): https://github.com/mwaskom/seaborn/blob/master/LICENSE.md
- optuna (MIT): https://github.com/optuna/optuna/blob/master/LICENSE
- HumanEval (MIT): https://github.com/openai/human-eval/blob/master/LICENSE
- gensim (LGPL-2.1): https://github.com/piskvorky/gensim/blob/develop/COPYING
- BERTopic (MIT, Copyright (c) 2020, Maarten P. Grootendorst): https://github.com/MaartenGr/BERTopic/blob/master/LICENSE
