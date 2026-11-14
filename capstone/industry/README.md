# Professional Industry Capstone — Credit Scoring & Fraud Transaction Detection

The professional edition of the capstone. It is grounded in industry papers, industry benchmark datasets, workshop standards and reference repositories. The evidence is in [docs/08-industry-capstone-research.md](../../docs/08-industry-capstone-research.md).

- **Who:** learners who finished the Expert track (it replaces E11), or teams of 2–4 practitioners.
- **Duration:** 40 h. `[ASUMSI]` This is 4 weeks × 10 h, or E11's 10 h plus 30 h extension.
- **Output:** a working platform, a bank‑style model documentation pack, and a workshop‑format paper + seminar talk.

## 1. Business scenario

A mid‑size Indonesian bank wants one **Risk Scoring Platform**:

1. **Card / digital transaction fraud** — real‑time scoring in the authorization path, with an analyst alert budget.
2. **Account‑opening fraud** — scoring at onboarding with a fairness constraint.
3. **Consumer credit** — application score, monthly behavioural re‑score, and a PD hand‑off to PSAK 109 ECL.

Constraints:
- Use only public or synthetic data.
- Follow OJK *Tata Kelola Kecerdasan Artifisial Perbankan Indonesia* (2025) and UU PDP.
- Every number must be traceable to a run.

## 2. Data — industry benchmark mix

| Workstream | Primary dataset | Secondary | What it lets you prove |
|------------|-----------------|-----------|------------------------|
| Transaction fraud (real time) | [IBM TabFormer](https://github.com/IBM/TabFormer) (~24 M transactions, ~0.12 % fraud) | Repo generator (`data/synth/generate.py`) for Indonesian fields, drift, fraud rings, delayed labels | Velocity features, time‑based split, latency, label delay |
| Account‑opening fraud | [Feedzai BAF](https://github.com/feedzai/bank-account-fraud) (6 variants) | — | Recall at a fixed false‑positive rate, fairness of false‑positive rates under bias, monthly drift |
| Credit (application + stability) | Home Credit — *Credit Risk Model Stability* (Kaggle 2024) | [FICO HELOC](https://api.openml.org/d/45554) for adverse‑action explanations | Weekly Gini stability, out‑of‑time performance, reason codes |
| Credit (behavioural) | Amex Default Prediction (Kaggle 2022) | — | Statement‑sequence features, monthly batch re‑score |
| Graph extension (optional) | [IBM AMLworld](https://arxiv.org/abs/2306.16424) + [Multi‑GNN](https://github.com/IBM/Multi-GNN) | — | Graph models for laundering/fraud networks |

Read each dataset's licence (Kaggle competition rules restrict use) and record it in `governance/data_sources.md`.

## 3. Industry evaluation protocol (fixed before modelling)

| Workstream | Primary metric | Required secondary metrics | Source of protocol |
|------------|----------------|----------------------------|--------------------|
| Transaction fraud | Recall at 1 % false‑positive rate **and** at the daily alert budget | Amount‑weighted recall, PR‑AUC, p99 latency, time to detection after label delay | Fraud Detection Handbook; Railgun (latency) |
| Account‑opening fraud | Recall at 5 % false‑positive rate | False‑positive‑rate ratio across age groups (predictive equality), behaviour across the 6 bias variants | Feedzai BAF / Aequitas |
| Credit application | Home Credit Gini stability metric = mean(weekly gini) + 88·min(0, slope) − 0.5·std(residuals) | Out‑of‑time Gini with 95 % CI, KS, calibration (Brier), PSI/CSI | Kaggle Home Credit 2024; credit risk practice |
| Credit behavioural | Gini + top‑4 % capture rate | Monthly PSI, batch vs API reconciliation | Amex 2022 competition metric family |

All splits are **by time**. Thresholds and costs go in `configs/gates.yaml` before the first model is trained, and changes after that are logged.

## 4. Required architecture

Build on the intermediate and expert platform:

- **Streaming features (E01):**
  - Kafka + Flink velocity features.
  - Online/offline parity test.
- **Fraud models:**
  - Champion: gradient boosting on tabular + velocity features.
  - Challenger: graph embeddings (BRIGHT/NVIDIA Blueprint pattern: embeddings computed in batch, looked up in real time).
  - Optional: a sequence model in the style of a TabFormer transformer.
- **Credit models:**
  - Monotonic GBM or EBM, versus a WoE scorecard.
  - Lifetime PD and ECL scenarios (E05).
- **Serving:** ONNX/Triton or FastAPI.
  - Fraud p99 ≤ 20 ms model time at 1 000 transactions per second.
  - Monthly credit batch job on Kubernetes.
- **Operations:**
  - MLflow registry with aliases.
  - Policy‑as‑code promotion gates (E09).
  - Shadow → canary → rollback.
- **Monitoring:**
  - Prometheus/Grafana.
  - Evidently/NannyML drift and estimated performance.
  - Weekly Gini stability dashboard for credit.
- **Fairness:**
  - Aequitas audit.
  - FairGBM or threshold adjustment as mitigation on BAF.

## 5. Deliverables (bank‑style package)

| # | Deliverable | Format / standard |
|---|-------------|-------------------|
| D1 | Working platform, one command to run (`make industry-demo`) | Repo + CI green |
| D2 | **Model Development Document (MDD)** per model | Sections: purpose, data, methodology, performance, limitations, monitoring plan (SR 11‑7 style) |
| D3 | **Independent Validation Report**, written by another learner acting as validator | Findings with High/Medium/Low severity, owner, due date |
| D4 | Model cards + evidence packs (auto‑generated) | E09 tooling |
| D5 | **Workshop paper**, 4–8 pages, ACM format, structured like an ICAIF fraud workshop or KDD‑MLF submission | Abstract, problem, data, method, time‑based evaluation with CIs, fairness, deployment lessons, limitations |
| D6 | **Seminar talk** (20 min) + poster | Presented to a mock panel: AI committee, model validator, OJK examiner, business owner |
| D7 | Runbooks: drift alert, rollback, incident, data subject request (UU PDP) | Markdown in `docs/runbooks/` |
| D8 | Benchmark table against public references | Your metric vs BAF paper baselines, Home Credit public leaderboard range, TabFormer baselines, with an explanation of differences |

## 6. Milestones (40 h)

| Week | Hours | Milestone | Exit evidence |
|------|-------|-----------|---------------|
| 1 | 10 | **Data & protocol freeze** — ingest TabFormer, BAF, Home Credit; licences logged; time‑based splits; evaluation protocol and gates committed | `governance/data_sources.md`, `configs/gates.yaml`, data validation green |
| 2 | 10 | **Models & benchmarks** — champions and challengers for the 3 workstreams; benchmark table D8; fairness audit on BAF | MLflow experiments, `reports/benchmark.md` |
| 3 | 10 | **Production path** — streaming features, Triton/FastAPI, batch job, policy gates, shadow/canary, monitoring and stability dashboard | `make industry-demo` passes; Grafana screenshots |
| 4 | 10 | **Validation & dissemination** — MDD, peer validation report, paper, talk, live scenario (drift + new fraud ring + forced rollback) | D2–D7 submitted; panel session held |

## 7. Definition of Done

- [ ] All metrics in Section 3 reported on time‑based hold‑outs with 95 % CIs.
- [ ] The benchmark table (D8) places each result next to a public reference and explains the gaps.
- [ ] BAF: the false‑positive‑rate ratio between age groups is reported for all 6 variants; one mitigation is evaluated with its recall cost.
- [ ] Home Credit stability metric computed by your own code and checked against a hand calculation on 3 weeks.
- [ ] Fraud p99 latency and throughput targets met, or a documented capacity plan explains the gap.
- [ ] A challenger that breaks any gate is blocked by CI (evidence link).
- [ ] The validation report has ≥ 5 findings, and each High finding is closed or has an accepted‑risk sign‑off.
- [ ] The paper passes an internal double‑blind review by 2 peers using the rubric below.
- [ ] No PII and no licence violations (`tests/test_no_pii.py`, data source register reviewed).

## 8. Rubric (100 %)

| Criterion | Weight | Excellent (4) |
|-----------|--------|---------------|
| Industry‑grade evaluation (time‑based, fixed false‑positive rate / alert budget, stability, CIs) | 20 % | Protocol fixed in advance; all metrics with CIs; honest comparison with public baselines |
| System & MLOps (streaming, serving, CI/CD/CT, monitoring, rollback) | 20 % | Runs with one command; SLOs met; automated rollout and rollback |
| Credit risk depth (stability, calibration, ECL hand‑off, explanations) | 15 % | Stability metric strong; reason codes compliant; ECL scenarios reconcile |
| Fraud depth (velocity, graph, delayed labels, adversarial awareness) | 15 % | Graph/sequence challenger evaluated by ablation; label delay handled |
| Responsible AI & compliance (fairness, privacy, OJK/UU PDP mapping, validation) | 15 % | BAF fairness analysis + mitigation; complete MDD and validation report |
| Dissemination (paper + talk) | 15 % | Paper is workshop‑ready; talk answers validator and examiner questions |

Each criterion is scored 1–4. Score = Σ weight × level / 4. **Pass ≥ 75 %. Distinction ≥ 90 %** (suggest submitting to an ICAIF or KDD‑MLF workshop).

## 9. Reference implementations to study first

| Repo / tutorial | Use for |
|-----------------|---------|
| [feedzai/bank-account-fraud](https://github.com/feedzai/bank-account-fraud) | BAF loading, baselines, fairness metrics |
| [dssg/aequitas](https://github.com/dssg/aequitas) · [feedzai/fairgbm](https://github.com/feedzai/fairgbm) | Bias audit, fairness‑constrained gradient boosting |
| [IBM/TabFormer](https://github.com/IBM/TabFormer) | Transaction data, sequence modelling |
| [IBM/Multi-GNN](https://github.com/IBM/Multi-GNN) | Graph models |
| [NVIDIA Financial Fraud Detection Blueprint](https://build.nvidia.com/nvidia/financial-fraud-detection) | GraphSAGE → XGBoost → Triton with SHAP |
| [RAPIDS fraud MLOps pipeline](https://docs.rapids.ai/deployment/stable/examples/fraud-detection-mlops-pipeline/notebook/) | Prefect + MLflow + Triton lifecycle |
| [databricks-industry-solutions/fraud-orchestration](https://github.com/databricks-industry-solutions/fraud-orchestration) | Rules + ML orchestration |
| [Fraud-Detection-Handbook](https://github.com/Fraud-Detection-Handbook/fraud-detection-handbook) | Prequential validation, simulator |
| [AIX360 HELOC tutorial](https://nbviewer.jupyter.org/github/IBM/AIX360/blob/master/examples/tutorials/HELOC.ipynb) | Credit explanations |

## 10. Papers to cite in your workshop paper (minimum set)

- **Datasets and benchmarks:** Jesus et al., *Turning the Tables* (BAF, NeurIPS 2022) · Padhi et al., *Tabular Transformers* (TabFormer) · Altman et al., *Realistic Synthetic Financial Transactions for AML* (NeurIPS 2023).
- **Fraud systems:** Lu et al., *BRIGHT* (CIKM 2022) · Bizarro et al., *Railgun* (VLDB 2021) · Dal Pozzolo et al., *Realistic modeling and novel learning strategy* (IEEE TNNLS 2018).
- **Fairness:** Cruz et al., *FairGBM* (ICLR 2023).
- **Credit risk:** discrete‑time survival tutorial for IFRS 9 (arXiv 2507.15441).
- **Governance:** OJK (2025) *Tata Kelola Kecerdasan Artifisial Perbankan Indonesia* · SR 11‑7.
