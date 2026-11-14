# Module 3: Experiment Tracking & Reproducibility

- **Image source:** [Gambar 1, 5, 6]
- **Duration:** 6 hours | **Level:** Basic
- **Learning outcomes:**
  1. Log params, metrics, artifacts, git commit, and DVC data hash to MLflow for every training run.
  2. Compare ≥ 3 runs in the MLflow UI and select the best by a pre‑declared primary metric.
  3. Reproduce a logged run on a second machine/container and match its primary metric within ±0.001.
  4. Pin all dependencies with a lock file and fix all random seeds.
- **Prerequisites:** M02
- **Core concepts:**
  - What to log: params, metrics, artifacts, code version, dataset version [Gambar 6].
  - Lineage: dataset (DVC) → code commit → model run [Gambar 6].
  - Reproducibility: fixed random seeds, pinned deps, logged hyperparameters [Gambar 5]; "If you can't reproduce a run, you don't really have a model." [Gambar 6]
  - Pitfall: logging only metrics is not enough [Gambar 6].
- **Task Project:**
  - **Task A (Fraud Detection):** `src/train/fraud.py --config configs/fraud.yaml` trains LogisticRegression and XGBoost baselines; logs to MLflow experiment `fraud-detection`; tags `git_commit`, `dvc_data_md5`, `train_window`. **Input:** M02 processed fraud data. **Output:** ≥ 3 MLflow runs with PR‑AUC, recall@precision=0.9, feature importance plot, confusion matrix PNG.
  - **Task B (Credit Scoring):** `src/train/credit.py --config configs/credit.yaml` trains a WoE + LogisticRegression scorecard and a LightGBM challenger; logs to experiment `credit-scoring`. **Input:** M02 processed credit data and WoE bins. **Output:** ≥ 3 runs with AUC, KS, Gini, scorecard points table artifact (`scorecard.csv`).
- **Deliverables:**
  - `src/train/{fraud,credit}.py`, `configs/{fraud,credit}.yaml`
  - `src/common/tracking.py` (one helper that sets tags `git_commit`, `dvc_data_md5`)
  - `requirements.lock` (via `pip-compile` or `uv pip compile`)
  - `docs/reproduce.md` with exact commands
- **Acceptance criteria / Definition of Done:**
  - [ ] Every run in both experiments has non‑empty tags `git_commit` and `dvc_data_md5` (checked by `scripts/check_runs.py` querying the MLflow API).
  - [ ] Each run has ≥ 1 model artifact and ≥ 2 plot artifacts.
  - [ ] Re‑running the best run's command in a fresh `docker compose run trainer` reproduces the primary metric within ±0.001.
  - [ ] `pip install -r requirements.lock` is the only install path documented.
  - [ ] Run comparison screenshot or exported CSV committed in `reports/m03_run_comparison.csv`.
- **Tools & libraries:** MLflow, DVC, Git, scikit‑learn, XGBoost, LightGBM, `uv`/`pip-tools`
- **Common pitfalls:**
  - Choosing the "best" run on the test set → test set is no longer held out; choose on validation.
  - Uncommitted code at run time (`git_commit` points to stale code) — fail the run if `git status --porcelain` is non‑empty.
  - Non‑deterministic XGBoost due to `n_jobs` / `tree_method` without seed.
- **Stretch goal:** Add Optuna hyperparameter search with each trial as a nested MLflow run; compare with Weights & Biases [Gambar 6] for the same 10 trials.
- **Reading & reference repos:** [docs/05-reading-list.md#m03](../docs/05-reading-list.md#m03) (⭐ = read first)
