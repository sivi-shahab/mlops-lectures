# Step 2 — Competency Map

Labels: `[Gambar n]` = derived from image *n* (see [image inventory](00-image-inventory.md)); `[TAMBAHAN]` = added because it is critical for fraud / credit scoring but not on any image; `[ASUMSI]` = assumption.

| # | Competency area | Sub‑competencies | Source | Module(s) |
|---|-----------------|------------------|--------|-----------|
| C1 | System design & problem framing | Lifecycle mapping Data→Train→Track→Register→Serve→Monitor→Retrain; component diagram; retrain loop | [Gambar 1, 2, 3] | M01 |
| | | Offline training vs online inference; real‑time vs batch inference | [Gambar 3] | M01, M08 |
| | | Design checklist: reproducibility, versioning, rollback, drift monitoring | [Gambar 3] | M01 |
| | | Business framing: cost of FN/FP, latency SLA (fraud), decision horizon & default definition (credit) | [TAMBAHAN] | M01 |
| C2 | Data management | Ingest → clean → transform → feature engineering → split | [Gambar 4] | M02 |
| | | Data versioning & lineage with DVC | [Gambar 4, 6] | M02, M03 |
| | | Schema / null / outlier validation before training | [Gambar 2, 4] | M02 |
| | | Train/serve consistency, shared transforms | [Gambar 4, 8] | M02, M08 |
| | | Feature store (Feast) | [Gambar 1, 3, 4] | M02 |
| | | Point‑in‑time correct features, temporal split, label maturity (delayed labels), reject inference | [TAMBAHAN] | M02, M05 |
| C3 | Experiment tracking & reproducibility | Log params, metrics, artifacts, code & dataset version | [Gambar 1, 6] | M03 |
| | | Compare runs; lineage dataset→commit→run | [Gambar 6] | M03 |
| | | Fixed seeds, pinned deps, logged hyperparameters | [Gambar 5, 6] | M03 |
| C4 | Pipeline orchestration | Pipeline steps ingest→validate→train→evaluate→register→deploy→monitor | [Gambar 3] | M04 |
| | | Orchestrator (Airflow / Kubeflow Pipelines) | [Gambar 12] | M04, M10 |
| C5 | Model training & evaluation | Train/validate/held‑out test; cross‑validation; leakage, overfitting, class imbalance | [Gambar 5] | M05 |
| | | Accuracy, precision/recall, F1, AUC | [Gambar 5] | M05 |
| | | PR‑AUC, recall@precision, cost‑sensitive threshold, KS, Gini, calibration, scorecard (WoE/IV) | [TAMBAHAN] | M05 |
| C6 | Explainability & fairness | Bias / fairness checks as approval gate; fairness in quality checks | [Gambar 7, 10] | M06 |
| | | SHAP, reason codes, adverse action notices, disparate impact | [TAMBAHAN] | M06 |
| C7 | CI/CD/CT | "Automate early" | [Gambar 2] | M07 |
| | | Automated retrain trigger | [Gambar 12] | M07, M10 |
| | | Unit tests for code, data tests, model tests in GitHub Actions; CT trigger | [TAMBAHAN] | M07 |
| C8 | Model registry & governance gate | Register, stages None→Staging→Production→Archived; approval gate; model metadata & model card | [Gambar 7] | M08, M11 |
| | | MLflow aliases instead of deprecated stages | [TAMBAHAN] | M08 |
| C9 | Packaging & serving | FastAPI `/predict` `/health` `/metrics`, Pydantic validation, shared preprocessing | [Gambar 1, 8] | M08 |
| | | Docker image, non‑root, pinned versions, probes, resources | [Gambar 1, 9] | M08, M12 |
| | | Kubernetes Deployment/Service/HPA, Helm, KServe, BentoML, Seldon | [Gambar 8, 9] | M08 (stretch) |
| | | Latency budget & load test (fraud p95 target), batch scoring job (credit) | [TAMBAHAN] | M08 |
| C10 | Monitoring | System metrics (latency p50/p95/p99, error rate, RPS, CPU, uptime) | [Gambar 10] | M09 |
| | | Prediction metrics (distribution, confidence) and quality metrics when labels arrive | [Gambar 10, 11] | M09 |
| | | Prometheus → Grafana → alerts | [Gambar 3, 10] | M09 |
| | | Data drift vs concept drift; PSI, KS; Evidently / NannyML | [Gambar 1, 11] | M09 |
| | | Segment slicing | [Gambar 11] | M09 |
| | | CSI per characteristic, scorecard stability report, delayed‑label performance estimation | [TAMBAHAN] | M09 |
| C11 | Retraining & release strategy | Triggers (scheduled, drift, performance); champion/challenger; shadow/canary; rollback | [Gambar 12] | M10 |
| | | Argo Rollouts, Helm/kubectl rollback | [Gambar 12] | M10 (stretch) |
| C12 | Governance & model risk | Model card, approval sign‑off, metadata | [Gambar 7] | M11 |
| | | Rollback strategy as a control | [Gambar 3, 12] | M11 |
| | | Model inventory, tiering, independent validation report, audit trail, OJK / PSAK 71 (ECL) / Basel III mapping | [TAMBAHAN] | M11 |
| C13 | Security & privacy | No secrets in images, non‑root containers | [Gambar 9] | M12 |
| | | PII masking/tokenization, RBAC, UU PDP (UU 27/2022), audit logs, adversarial abuse of the fraud API | [TAMBAHAN] | M12 |
| C14 | Integration | End‑to‑end platform | [Gambar 1, 2] | M13 Capstone |

## Coverage check — every image maps to ≥ 1 module

| Image | Modules |
|-------|---------|
| 1 | M01, M02, M03, M08, M09, M13 |
| 2 | M01, M02, M07, M13 |
| 3 | M01, M04, M09, M11 |
| 4 | M02 |
| 5 | M03, M05 |
| 6 | M03 |
| 7 | M06, M08, M11 |
| 8 | M02, M08 |
| 9 | M08, M12 |
| 10 | M06, M09 |
| 11 | M09 |
| 12 | M04, M07, M10, M11 |
