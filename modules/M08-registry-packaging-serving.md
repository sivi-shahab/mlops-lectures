# Module 8: Model Registry, Packaging & Serving (REST API, Batch Scoring, Latency/Throughput)

- **Image source:** [Gambar 1, 7, 8, 9]; MLflow aliases, load testing, batch scoring `[TAMBAHAN]`
- **Duration:** 10 hours | **Level:** Intermediate
- **Learning outcomes:**
  1. Register a validated run in the MLflow Model Registry with a model card and promote it through `staging` → `champion` aliases.
  2. Serve the fraud model behind FastAPI with `/predict`, `/health`, `/metrics` and Pydantic validation.
  3. Containerize the API with a pinned, non‑root, health‑probed image that loads the model from the registry at startup.
  4. Run a batch credit scoring job that writes scores to PostgreSQL.
  5. Load‑test the fraud API and report p50/p95/p99 latency and max sustained RPS.
- **Prerequisites:** M05, M07
- **Core concepts:**
  - Registry flow None → Staging → Production → Archived; approval gate; metadata; model card; "deploy from the registry, never from a notebook" [Gambar 7].
  - API anatomy request → preprocess → `model.predict` → postprocess → response; contract `/predict` `/health` `/metrics`; input validation; reuse SAME preprocessing [Gambar 8].
  - Dockerfile from `python:3.11-slim`; build & run; model loading (bake small, pull large from registry); best practices: pin versions, non‑root, liveness/readiness probes, resource limits, keep models warm [Gambar 1, 9].
  - Serving options: FastAPI, BentoML, Seldon/KServe; K8s Deployment + Service + HPA, Helm [Gambar 8, 9].
  - `[TAMBAHAN]` MLflow ≥ 2.9 aliases (`champion`, `challenger`) replace stages; idempotency key / request ID; batch vs online consistency check.
- **Task Project:**
  - **Task A (Fraud Detection):** `src/api/fraud_app.py` FastAPI service; request schema validated with Pydantic (amount > 0, currency in {IDR}, timestamp ISO‑8601); response `{request_id, score, decision, model_version}`; logs every prediction with `request_id` to PostgreSQL table `fraud_predictions`. Dockerize and load‑test with Locust at 200 RPS for 5 minutes. **Input:** champion fraud model in registry. **Output:** running container, `reports/fraud_loadtest.md`.
  - **Task B (Credit Scoring):** (1) `src/api/credit_app.py` `/score` endpoint returning score, PD, decision, reason codes; (2) `src/batch/score_portfolio.py` monthly batch job scoring all active accounts into `credit_scores(account_id, score, pd, model_version, as_of_date)`. **Input:** champion credit model + synthetic portfolio. **Output:** container + populated table + reconciliation report (batch score = API score for 1 000 sampled accounts).
- **Deliverables:**
  - `src/registry/promote.py` (register + set alias + attach model card)
  - `docs/model-cards/{fraud,credit}.md`
  - `src/api/{fraud_app,credit_app}.py`, `docker/api.Dockerfile`
  - `src/batch/score_portfolio.py`
  - `loadtest/locustfile.py`, `reports/fraud_loadtest.md`
  - (stretch) `deploy/k8s/` or `deploy/helm/`
- **Acceptance criteria / Definition of Done:**
  - [ ] `mlflow` client shows both models with alias `champion` and a `model_card` tag/artifact.
  - [ ] API refuses invalid payloads with HTTP 422 (tested with ≥ 5 invalid cases).
  - [ ] `/health` returns 200 only after the model is loaded (readiness), and the container `HEALTHCHECK` uses it.
  - [ ] `docker run --user` shows a non‑root UID; image has no secrets (`docker history` / `trivy` scan clean for secrets).
  - [ ] Fraud API p95 ≤ 50 ms and error rate < 0.1 % at 200 RPS on the reference laptop (numbers in report).
  - [ ] Batch vs API reconciliation: max absolute score difference = 0 for 1 000 accounts.
  - [ ] Every prediction row has a non‑null `request_id` and `model_version`.
- **Tools & libraries:** MLflow Model Registry, FastAPI, Pydantic v2, Uvicorn, Docker, PostgreSQL, SQLAlchemy, Locust; optional BentoML, KServe, Kubernetes (kind), Helm [Gambar 8, 9]
- **Common pitfalls:**
  - Re‑implementing preprocessing in the API → silent skew [Gambar 8].
  - Loading the model per request instead of at startup.
  - Shipping secrets in images; no resource limits; no health checks [Gambar 9].
  - Using `transition_model_version_stage` in new code (deprecated) — use aliases.
  - Floating‑point differences between batch (pandas) and online (dict) paths.
- **Stretch goal:** Deploy the fraud API to a local `kind` cluster with a Helm chart, HPA on CPU 70 %, and readiness/liveness probes [Gambar 9].
- **Reading & reference repos:** [docs/05-reading-list.md#m08](../docs/05-reading-list.md#m08) (⭐ = read first)
