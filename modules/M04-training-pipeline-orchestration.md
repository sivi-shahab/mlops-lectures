# Module 4: Training Pipeline & Orchestration

- **Image source:** [Gambar 3, 12]; idempotency and backfill `[TAMBAHAN]`
- **Duration:** 6 hours | **Level:** Intermediate
- **Learning outcomes:**
  1. Implement the image's pipeline steps (`ingest_data`, `validate_data`, `train_model`, `evaluate_model`, `register_model`) as an Airflow DAG.
  2. Make every task idempotent and parameterized by a logical date so backfills give identical outputs.
  3. Configure retries, timeouts, and failure alerts per task.
  4. Run one backfill for 3 historical training windows and compare their MLflow runs.
- **Prerequisites:** M02, M03
- **Core concepts:**
  - Pipeline step list from [Gambar 3]: ingest → validate → train → evaluate → register → deploy → monitor.
  - Orchestrators: Airflow / Kubeflow Pipelines [Gambar 12].
  - `[TAMBAHAN]` Idempotency, logical date vs wall‑clock date, sensors for late data, separation of orchestration (Airflow) from compute (Docker task).
- **Task Project:**
  - **Task A (Fraud Detection):** DAG `dags/fraud_training.py`, weekly schedule, rolling 90‑day training window ending at `logical_date − 60 days` (label maturity). Tasks call `dvc repro` and `src/train/fraud.py`. **Input:** synthetic fraud data partitioned by day. **Output:** DAG green for 3 backfilled weeks; 3 MLflow runs tagged `logical_date`.
  - **Task B (Credit Scoring):** DAG `dags/credit_training.py`, monthly schedule, training on vintages with ≥ 12 months performance. Adds a `build_oot` task that holds out the latest mature vintage. **Input:** synthetic credit applications partitioned by month. **Output:** DAG green for 3 backfilled months; OOT metrics logged.
- **Deliverables:**
  - `dags/fraud_training.py`, `dags/credit_training.py`
  - `docker-compose.yml` profile `orchestration` running Airflow
  - `docs/runbooks/rerun-training.md`
- **Acceptance criteria / Definition of Done:**
  - [ ] `airflow dags test fraud_training 2026-03-02` and `airflow dags test credit_training 2026-03-01` exit 0.
  - [ ] Running the same logical date twice produces identical `dvc.lock` hashes and no duplicate rows in output tables.
  - [ ] Each task has `retries ≥ 2` and `execution_timeout` set (asserted by `tests/test_dags.py` loading the DagBag).
  - [ ] DagBag import has 0 errors in CI.
  - [ ] An intentionally failing `validate_data` task stops downstream tasks (screenshot or log excerpt in `reports/m04_failure.md`).
- **Tools & libraries:** Apache Airflow 2.x, DVC, MLflow, Docker; Kubeflow Pipelines (stretch) [Gambar 12]
- **Common pitfalls:**
  - Using `datetime.now()` inside tasks → backfills train on the wrong window.
  - Training fraud models on the most recent weeks whose labels are not yet mature → artificially low fraud rate.
  - Heavy compute inside the Airflow scheduler container.
- **Stretch goal:** Port the fraud DAG to Kubeflow Pipelines or Prefect and write a 1‑page comparison (ops overhead, UI, retries).
