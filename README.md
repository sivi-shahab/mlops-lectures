# MLOps Hands‑On Curriculum — Fraud Detection & Credit Scoring

A **project‑based MLOps syllabus** for banking/fintech, derived from a 12‑image "Notebook to Live Model" infographic series and extended with what fraud detection and credit scoring require in production (imbalance, delayed labels, PSI/CSI, explainability, fairness, OJK / PSAK 71 / Basel III / UU PDP governance).

- **Learner level:** intermediate `[ASUMSI]` (Python, SQL, scikit‑learn, Docker basics)
- **Duration:** 12 weeks × 8 h = **96 h** `[ASUMSI]`
- **Stack:** Python, FastAPI, PostgreSQL, Docker, MLflow, DVC, Airflow, Great Expectations, Evidently, Feast, Prometheus/Grafana, GitHub Actions

**Labels used everywhere:** `[Gambar n]` = derived from image *n* · `[TAMBAHAN]` = added by the curriculum author · `[ASUMSI]` = assumption · `[PERLU KONFIRMASI]` = unreadable/ambiguous in the image.

## Contents

| Step | Document |
|------|----------|
| 1. Image inventory | [docs/00-image-inventory.md](docs/00-image-inventory.md) |
| 2. Competency map | [docs/01-competency-map.md](docs/01-competency-map.md) |
| 3–4. Modules (task specs) | [modules/](modules/) — see table below |
| 5. Datasets, synthetic data, repo structure, environment | [docs/02-datasets-and-environment.md](docs/02-datasets-and-environment.md) |
| 6. Capstone (architecture, milestones, rubric) | [capstone/README.md](capstone/README.md) |
| 7. Assessment, weekly schedule, dependency map | [docs/03-assessment-and-schedule.md](docs/03-assessment-and-schedule.md) |
| Risks, assumptions, clarifying questions | [docs/04-risks-assumptions-questions.md](docs/04-risks-assumptions-questions.md) |

## Modules

Lifecycle from the images: `Data → Train → Track → Register → Serve → Monitor → Retrain` [Gambar 1, 2].

| # | Module | Hours | Image source | Week |
|---|--------|-------|--------------|------|
| M01 | [Problem framing & architecture (batch vs real‑time)](modules/M01-problem-framing-architecture.md) | 6 | 1, 2, 3 | 1 |
| M02 | [Data engineering: versioning, validation, features, feature store](modules/M02-data-engineering-feature-store.md) | 10 | 1, 2, 4 | 1–2 |
| M03 | [Experiment tracking & reproducibility](modules/M03-experiment-tracking-reproducibility.md) | 6 | 1, 5, 6 | 3 |
| M04 | [Training pipeline & orchestration](modules/M04-training-pipeline-orchestration.md) | 6 | 3, 12 | 3–4 |
| M05 | [Domain model evaluation (PR‑AUC, KS, Gini, cost, calibration)](modules/M05-domain-model-evaluation.md) | 8 | 5 + TAMBAHAN | 4–5 |
| M06 | [Explainability & fairness](modules/M06-explainability-fairness.md) | 6 | 7, 10 + TAMBAHAN | 5–6 |
| M07 | [CI/CD/CT for ML](modules/M07-cicd-ct.md) | 6 | 2, 12 + TAMBAHAN | 6 |
| M08 | [Registry, packaging & serving](modules/M08-registry-packaging-serving.md) | 10 | 1, 7, 8, 9 | 7–8 |
| M09 | [Monitoring: drift, PSI/CSI, decay, alerting](modules/M09-monitoring-drift.md) | 10 | 1, 3, 10, 11 | 8–9 |
| M10 | [Retraining, champion/challenger, shadow & canary, rollback](modules/M10-retraining-release-strategy.md) | 6 | 12 | 9–10 |
| M11 | [Governance, audit trail, model risk, regulation](modules/M11-governance-model-risk.md) | 5 | 3, 7, 12 + TAMBAHAN | 10 |
| M12 | [Security & privacy (PII, access control, UU PDP)](modules/M12-security-privacy.md) | 4 | 9 + TAMBAHAN | 10–11 |
| M13 | [Capstone](modules/M13-capstone.md) | 13 | 1, 2 | 11–12 |
| | **Total** | **96** | | |

Every module has a **Task A (Fraud Detection)** and a **Task B (Credit Scoring)** with measurable acceptance criteria.

## Quick start

```bash
python -m venv .venv && source .venv/bin/activate
pip install numpy pandas pyarrow          # enough for the generator; full list in requirements.txt
make data                                 # synthetic fraud + credit data with drift, delayed labels, fraud ring
python tests/test_generate.py             # generator self-check
make up                                   # Postgres, MLflow :5000, Prometheus :9090, Grafana :3000
```

## Quality self‑check

- [x] Every image maps to ≥ 1 module ([coverage table](docs/01-competency-map.md#coverage-check--every-image-maps-to--1-module))
- [x] Fraud detection and credit scoring tasks in every module
- [x] Dedicated modules for drift monitoring (M09), governance (M11), data security (M12)
- [x] Total hours = 96 ≤ 96 available
- [x] Image claims limited to visible content; ambiguous items marked `[PERLU KONFIRMASI]`

## Source images

The 12 source infographics ("Tech Fusionist" series) are third‑party content and are **git‑ignored**, not redistributed. File names and descriptions are in the [image inventory](docs/00-image-inventory.md).

## Risks, assumptions & open questions

See [docs/04-risks-assumptions-questions.md](docs/04-risks-assumptions-questions.md). The three questions that matter most:

1. Is the learner level intermediate and the budget 12 weeks × 8 h?
2. Must Kubernetes (or the bank's target platform) be core instead of a stretch goal?
3. Should M11 map to the bank's actual MRM policy and specific POJK/SEOJK clauses?
