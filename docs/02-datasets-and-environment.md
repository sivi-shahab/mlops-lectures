# Step 5 — Datasets & Environment

All content in this file is `[TAMBAHAN]` (the images only show `raw.csv`, `churn_data_v3`, and a `fraud-model` name — no specific datasets).

## Public datasets

| Dataset | Use case | Size / imbalance | Strengths | Limitations |
|---------|----------|------------------|-----------|-------------|
| Kaggle Credit Card Fraud (ULB, 2013) | Fraud | 284 807 tx, 0.17 % fraud | Classic imbalance benchmark; fast | Features are PCA‑anonymized (V1–V28) → no real feature engineering, no entity IDs for velocity features, only 2 days → no drift/delayed label |
| IEEE‑CIS Fraud Detection (Vesta) | Fraud | ~590 k tx, ~3.5 % fraud | Rich raw features (card, device, email domain); time delta column enables temporal split | Partially masked columns; no true timestamp; labels already final (no delay simulation); Kaggle license — not for commercial use |
| PaySim (synthetic mobile money) | Fraud | 6.3 M tx | Has steps (time), account IDs → velocity features; mobile money similar to digital banking | Synthetic, simplistic fraud patterns; very separable |
| Give Me Some Credit | Credit | 150 k borrowers, ~6.7 % bad | Simple tabular, quick scorecard | No application date → no vintages/OOT; no protected attributes |
| Home Credit Default Risk | Credit | 307 k applications, ~8 % bad, multiple tables | Realistic multi‑table feature engineering (bureau, previous apps) | Large; no application date for true OOT; competition license |
| German Credit (Statlog) | Credit / fairness | 1 000 rows, 30 % bad | Has sex/age → fairness exercises | Tiny, old (1994), cost matrix given; not representative of Indonesian market |
| Lending Club (2007–2018, archived) | Credit | > 2 M loans | Issue dates → vintages, OOT, PSI over time | Availability varies (removed from official site); US population; selection bias (approved only) |

**Recommendation `[ASUMSI]`:** use the synthetic generator below as the default (it supports drift, delayed labels, fraud rings, and vintages), and use IEEE‑CIS (fraud) + Home Credit (credit) as "real‑world" replays in M05 and the capstone.

## Synthetic data generator

`data/synth/generate.py` (in this repo) produces:

| File | Columns (main) | Simulated phenomena |
|------|----------------|--------------------|
| `fraud_transactions.parquet` | `tx_id, event_time, card_id, device_id, merchant_id, merchant_category, region, device_os, amount, is_fraud, label_available_at, card_number, customer_name, phone` | ~0.5 % fraud; **delayed labels** (chargeback 30–90 days); **fraud ring** (cluster of cards sharing few devices, high‑velocity small→large amounts); **drift** after `--drift-start` (amount scale ×1.6, new merchant category `crypto_exchange`, more Android) |
| `credit_applications.parquet` | `app_id, application_date, vintage, age, income, dti, utilization, months_oldest_account, n_delinquencies, region, gender, nik, full_name, is_approved, default_12m` | Monthly **vintages**; **reject bias** (`default_12m` is NaN for declined applicants); **drift** after `--drift-start` (income down, DTI up → population shift + higher bad rate) |

Fake PII columns (`card_number`, `nik`, …) exist on purpose for M12. They are random, not real.

```bash
python data/synth/generate.py --out data/synth --n-tx 200000 --n-apps 50000 \
  --start 2025-01-01 --months 18 --drift-start 2026-01-01 --seed 42
python tests/test_generate.py   # self-check
```

Generator structure (extend it in your modules):

```text
generate.py
├── fraud(n, start, months, drift_start, rng)
│   ├── base population of cards/devices/merchants
│   ├── legit transactions (log-normal amounts, Poisson timing)
│   ├── fraud_ring(): k cards × few devices, burst of escalating amounts
│   ├── drift(): post drift_start shift in amount, merchant mix, device OS
│   └── delayed labels: label_available_at = event_time + U(30, 90) days
└── credit(n, start, months, drift_start, rng)
    ├── applicant features with correlated income/DTI/utilization
    ├── true PD via logistic function → default_12m ~ Bernoulli(PD)
    ├── approval policy (score cutoff) → reject bias
    └── drift(): post drift_start income ↓, DTI ↑
```

## Repository structure (monorepo)

Monorepo is chosen `[ASUMSI]` because one learner owns both use cases and shared code (`src/features`, `src/common`) must stay consistent.

```text
mlops-lectures/
├── README.md
├── Makefile
├── docker-compose.yml            # postgres, mlflow, prometheus, grafana, airflow (profile)
├── requirements.txt              # lock it in M03 → requirements.lock
├── docs/                         # syllabus docs, design docs, ADRs, runbooks, model cards
├── modules/                      # M01–M13 task specs
├── capstone/
├── data/
│   ├── synth/generate.py         # synthetic data generator
│   └── processed/                # DVC outputs (git-ignored)
├── pipelines/{fraud,credit}/dvc.yaml          # M02
├── feature_repo/                               # Feast (M02)
├── configs/                                    # fraud.yaml, credit.yaml, gates.yaml
├── src/
│   ├── common/      features/   train/   evaluate/   explain/
│   ├── registry/    api/        batch/   monitor/    privacy/
├── dags/                                       # Airflow (M04, M10)
├── monitoring/prometheus.yml, alert_rules.yml, grafana/
├── governance/                                 # inventory, mappings (M11, M12)
├── sql/                                        # roles, audit trail
├── loadtest/                                   # Locust (M08)
├── tests/{unit,data,model}/
└── .github/workflows/                          # ci.yml, cd.yml, security.yml (M07, M12)
```

Folders that do not yet exist are created by the learner in the module that introduces them.

## Environment setup

Requirements: Docker ≥ 24 with Compose v2, Python 3.11, 16 GB RAM recommended.

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
make data                 # synthetic data
make up                   # postgres, mlflow, prometheus, grafana
make up-airflow           # adds Airflow (from M04)
```

| Service | URL | Credentials (local only) |
|---------|-----|--------------------------|
| MLflow | http://localhost:5000 | none |
| PostgreSQL | localhost:5432 | `mlops` / `mlops` (override in `.env`) |
| Prometheus | http://localhost:9090 | none |
| Grafana | http://localhost:3000 | `admin` / `admin` |
| Airflow | http://localhost:8080 | printed by `airflow standalone` in container logs |
