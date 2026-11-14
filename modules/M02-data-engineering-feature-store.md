# Module 2: Data Engineering — Versioning, Validation, Feature Engineering, Feature Store

- **Image source:** [Gambar 1, 2, 4]; point‑in‑time correctness, temporal split, label maturity, reject inference `[TAMBAHAN]`
- **Duration:** 10 hours | **Level:** Intermediate
- **Learning outcomes:**
  1. Build a DVC pipeline (`dvc.yaml`) with stages ingest → clean → transform → features → split that reproduces bit‑identical outputs on `dvc repro`.
  2. Write a Great Expectations (or Pandera) suite that fails the pipeline on schema, null‑rate, and range violations.
  3. Implement a single shared transform module imported by both training and serving code.
  4. Produce point‑in‑time correct features with Feast for fraud velocity features.
  5. Split data by time (out‑of‑time test set) and verify no entity/time leakage with an automated check.
- **Prerequisites:** M01
- **Core concepts:**
  - Pipeline stages ingest → clean → transform → feature engineering → split [Gambar 4].
  - Data versioning & lineage: `raw.csv → clean.csv → features.csv → train.parquet` [Gambar 4].
  - Quality checks: schema validation, null/outlier checks before training — "Garbage in, garbage out" [Gambar 2, 4].
  - Train/serve consistency: same transforms at training and inference [Gambar 4].
  - `[TAMBAHAN]` Point‑in‑time joins; label maturity (only use fraud labels older than the chargeback window; only credit loans with a full 12‑month performance window); reject inference for credit (only approved applicants have outcomes).
- **Task Project:**
  - **Task A (Fraud Detection):** Build `pipelines/fraud/dvc.yaml`. Features: amount z‑score per card, transaction count & sum per card in last 1h/24h, distinct merchants per device in 24h, time since last transaction, is‑new‑device. Register velocity features in Feast (`feature_repo/fraud.py`) with a `card_id` entity and offline source = Parquet. **Input:** `data/synth/fraud_transactions.parquet` (or IEEE‑CIS). **Output:** `data/processed/fraud/{train,valid,test}.parquet`, Feast feature view, GE validation report.
  - **Task B (Credit Scoring):** Build `pipelines/credit/dvc.yaml`. Features: DTI, utilization, months since oldest account, number of delinquencies, income band; WoE binning stage (fit on train only). Flag `is_approved` and keep rejected applicants in a separate file for reject‑inference experiments. **Input:** `data/synth/credit_applications.parquet` (or Home Credit / Give Me Some Credit). **Output:** `data/processed/credit/{train,valid,oot}.parquet`, WoE bin table `artifacts/credit/woe_bins.json`, GE validation report.
- **Deliverables:**
  - `pipelines/{fraud,credit}/dvc.yaml` and `params.yaml`
  - `src/features/transforms.py` (shared, imported by training and API)
  - `feature_repo/` (Feast) with `feature_store.yaml`
  - `great_expectations/` suites or `src/validation/schemas.py` (Pandera)
  - `tests/test_no_leakage.py`
- **Acceptance criteria / Definition of Done:**
  - [ ] `dvc repro` from a clean clone produces outputs whose `dvc.lock` md5 hashes match the committed lock file.
  - [ ] `dvc dag` shows ≥ 5 stages per use case.
  - [ ] Validation suite has ≥ 10 expectations per dataset, and injecting 5 % nulls into `amount` makes `dvc repro` exit non‑zero.
  - [ ] `max(train.event_time) < min(valid.event_time) < min(test.event_time)` asserted in `tests/test_no_leakage.py`.
  - [ ] No `card_id`/`customer_id` overlap check documented (either asserted disjoint or explicitly justified).
  - [ ] Feast `get_historical_features` result for 100 sampled rows equals a hand‑computed pandas rolling window (assert in test).
  - [ ] `grep -r "def transform" src/api` returns nothing — the API imports from `src/features`.
- **Tools & libraries:** DVC, pandas, scikit‑learn, Great Expectations (or Pandera), Feast, PyArrow, PostgreSQL (as Feast registry / offline source optional)
- **Common pitfalls:**
  - Random split on time‑ordered transactions → optimistic metrics.
  - Computing velocity features with future rows (no `closed='left'` window) → label leakage.
  - Fitting WoE bins / scalers on the full dataset.
  - Training credit models only on approved applicants without acknowledging reject bias.
  - Training/serving skew from re‑implemented transforms [Gambar 4].
- **Stretch goal:** Add an online store (Redis) for Feast and measure online feature retrieval p95 < 10 ms.
