# Reading List & Reference Repositories

All items are `[TAMBAHAN]`. Types: 📘 book · 📄 paper · 📚 docs/guide · 💻 GitHub repo · ⚖️ regulation/standard.
⭐ = read first (core). Everything else is optional depth. Links were checked when this list was written; regulation links point to official portals — always use the latest version.

## General (whole program)

| Type | Resource | Why |
|------|----------|-----|
| 📘 ⭐ | Chip Huyen — *Designing Machine Learning Systems* (O'Reilly, 2022) · companion: [chiphuyen/dmls-book](https://github.com/chiphuyen/dmls-book) | Best single book for this curriculum; ch. 1–2 (framing), 4–5 (data/features), 6 (evaluation), 7 (deployment), 8 (drift), 9 (continual learning), 11 (responsible ML) |
| 📄 ⭐ | Sculley et al. — [Hidden Technical Debt in Machine Learning Systems](https://proceedings.neurips.cc/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html) (NeurIPS 2015) | Why "MLOps" exists |
| 📚 ⭐ | Google — [Rules of Machine Learning](https://developers.google.com/machine-learning/guides/rules-of-ml) | Practical heuristics for production ML |
| 📚 | Google Cloud — [MLOps: continuous delivery and automation pipelines](https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning) | MLOps maturity levels 0/1/2 |
| 📚 | [ml-ops.org](https://ml-ops.org) | Principles, reference process |
| 💻 ⭐ | [DataTalksClub/mlops-zoomcamp](https://github.com/DataTalksClub/mlops-zoomcamp) | Free course with code: MLflow, orchestration, deployment, monitoring (Evidently, Grafana) |
| 💻 ⭐ | [GokuMohandas/Made-With-ML](https://github.com/GokuMohandas/Made-With-ML) | End‑to‑end production ML repo with testing, CI/CD, serving |
| 💻 | [visenger/awesome-mlops](https://github.com/visenger/awesome-mlops) · [EthicalML/awesome-production-machine-learning](https://github.com/EthicalML/awesome-production-machine-learning) | Curated tool and paper indexes |

## Domain foundations (fraud & credit)

| Type | Resource | Why |
|------|----------|-----|
| 📚 💻 ⭐ | Le Borgne et al. — [Reproducible Machine Learning for Credit Card Fraud Detection – Practical Handbook](https://fraud-detection-handbook.github.io/fraud-detection-handbook/) · [repo](https://github.com/Fraud-Detection-Handbook/fraud-detection-handbook) | Transaction simulator, velocity features, delayed feedback, prequential validation, fraud metrics — maps directly onto M02, M05, M09 |
| 📄 | Dal Pozzolo et al. — [Credit Card Fraud Detection: A Realistic Modeling and a Novel Learning Strategy](https://doi.org/10.1109/TNNLS.2017.2736643) (IEEE TNNLS 2018) | Delayed labels, alert‑feedback interaction, concept drift in fraud |
| 📘 ⭐ | Naeem Siddiqi — *Intelligent Credit Scoring: Building and Implementing Better Credit Risk Scorecards* (2nd ed., Wiley, 2017) | Scorecard development, WoE/IV, reject inference, validation, monitoring |
| 📘 | Thomas, Crook & Edelman — *Credit Scoring and Its Applications* (2nd ed., SIAM, 2017) | Statistical depth for PD models |

---

## M01

Problem framing & architecture

| Type | Resource |
|------|----------|
| 📘 ⭐ | Huyen, *DMLS* ch. 1–2 (ML systems design, framing) |
| 📚 | [Rules of ML](https://developers.google.com/machine-learning/guides/rules-of-ml) — rules 1–15 |
| 📚 | Uber — [Meet Michelangelo: Uber's ML platform](https://www.uber.com/blog/michelangelo-machine-learning-platform/) (online/offline architecture, feature store) |
| 📚 | Stripe — [How we built it: Stripe Radar](https://stripe.com/blog/how-we-built-it-stripe-radar) (real‑time fraud system) |
| 💻 | [joelparkerhenderson/architecture-decision-record](https://github.com/joelparkerhenderson/architecture-decision-record) — ADR templates |
| 📚 | [Mermaid docs](https://mermaid.js.org) — diagrams in Markdown |

## M02

Data engineering, versioning, validation, feature store

| Type | Resource |
|------|----------|
| 📚 ⭐ | [DVC — Get Started](https://dvc.org/doc/start) · 💻 [iterative/dvc](https://github.com/iterative/dvc) |
| 📚 ⭐ | [Great Expectations docs](https://docs.greatexpectations.io) · 💻 [great-expectations/great_expectations](https://github.com/great-expectations/great_expectations) |
| 💻 | [unionai-oss/pandera](https://github.com/unionai-oss/pandera) — lighter dataframe validation |
| 📚 ⭐ | [Feast docs](https://docs.feast.dev) · [Point‑in‑time joins](https://docs.feast.dev/getting-started/concepts/point-in-time-joins) · 💻 [feast-dev/feast](https://github.com/feast-dev/feast) |
| 💻 | [feast-dev/feast-credit-score-local-tutorial](https://github.com/feast-dev/feast-credit-score-local-tutorial) — Feast applied to credit scoring |
| 📄 | Kapoor & Narayanan — [Leakage and the Reproducibility Crisis in ML‑based Science](https://reproducible.cs.princeton.edu) |
| 📚 | Fraud Detection Handbook — ch. 3 (baseline feature transformation: velocity & risk features) |
| 📘 | Siddiqi — chapters on data preparation, WoE binning, reject inference |

## M03

Experiment tracking & reproducibility

| Type | Resource |
|------|----------|
| 📚 ⭐ | [MLflow Tracking](https://mlflow.org/docs/latest/tracking.html) · 💻 [mlflow/mlflow](https://github.com/mlflow/mlflow) |
| 📚 | [Weights & Biases docs](https://docs.wandb.ai) (alternative shown in [Gambar 6]) |
| 📚 | [uv](https://docs.astral.sh/uv/) · 💻 [jazzband/pip-tools](https://github.com/jazzband/pip-tools) — dependency locking |
| 💻 | [optuna/optuna](https://github.com/optuna/optuna) — hyperparameter search (stretch) |
| 📄 | Pineau et al. — [Improving Reproducibility in Machine Learning Research](https://arxiv.org/abs/2003.12206) |

## M04

Training pipeline & orchestration

| Type | Resource |
|------|----------|
| 📚 ⭐ | [Airflow — Best Practices](https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html) · 💻 [apache/airflow](https://github.com/apache/airflow) |
| 📚 ⭐ | Maxime Beauchemin — [Functional Data Engineering](https://maximebeauchemin.medium.com/functional-data-engineering-a-modern-paradigm-for-batch-data-processing-2327ec32c42a) (idempotency, partitions, backfills) |
| 📚 | [Kubeflow Pipelines](https://www.kubeflow.org/docs/components/pipelines/) ([Gambar 12]) |
| 💻 | [PrefectHQ/prefect](https://github.com/PrefectHQ/prefect) — lighter alternative |

## M05

Domain evaluation

| Type | Resource |
|------|----------|
| 📄 ⭐ | Saito & Rehmsmeier — [The Precision‑Recall Plot Is More Informative than the ROC Plot on Imbalanced Datasets](https://doi.org/10.1371/journal.pone.0118432) (PLoS ONE 2015) |
| 📚 ⭐ | Fraud Detection Handbook — ch. 4 (performance metrics, precision top‑k, card precision) and ch. 5 (validation strategies) |
| 📚 | scikit‑learn — [Model evaluation](https://scikit-learn.org/stable/modules/model_evaluation.html) · [Probability calibration](https://scikit-learn.org/stable/modules/calibration.html) · [Tuning the decision threshold](https://scikit-learn.org/stable/modules/classification_threshold.html) |
| 💻 | [scikit-learn-contrib/imbalanced-learn](https://github.com/scikit-learn-contrib/imbalanced-learn) |
| 💻 ⭐ | [guillermo-navas-palencia/optbinning](https://github.com/guillermo-navas-palencia/optbinning) — optimal binning, WoE, scorecards |
| 💻 | [ShichenXie/scorecardpy](https://github.com/ShichenXie/scorecardpy) — scorecard toolkit (KS, PSI, points) |
| 📘 | Siddiqi — scorecard validation chapter (KS, Gini, score distributions) |

## M06

Explainability & fairness

| Type | Resource |
|------|----------|
| 📄 ⭐ | Lundberg & Lee — [A Unified Approach to Interpreting Model Predictions (SHAP)](https://arxiv.org/abs/1705.07874) · 💻 [shap/shap](https://github.com/shap/shap) |
| 📘 ⭐ | Christoph Molnar — [Interpretable Machine Learning](https://christophm.github.io/interpretable-ml-book/) (free online) |
| 📘 | Barocas, Hardt & Narayanan — [Fairness and Machine Learning](https://fairmlbook.org) (free online) |
| 💻 ⭐ | [fairlearn/fairlearn](https://github.com/fairlearn/fairlearn) · [fairlearn.org](https://fairlearn.org) (includes a credit‑card default case study) |
| 💻 | [Trusted-AI/AIF360](https://github.com/Trusted-AI/AIF360) — more fairness metrics/mitigations |
| 💻 | [interpretml/DiCE](https://github.com/interpretml/DiCE) — counterfactuals (stretch) |
| ⚖️ | US CFPB — [Circular 2022‑03: adverse action notices and complex algorithms](https://www.consumerfinance.gov/compliance/circulars/circular-2022-03-adverse-action-notification-requirements-in-connection-with-credit-decisions-based-on-complex-algorithms/) (international benchmark for reason codes) |

## M07

CI/CD/CT

| Type | Resource |
|------|----------|
| 📄 ⭐ | Breck et al. — [The ML Test Score: A Rubric for ML Production Readiness](https://research.google/pubs/the-ml-test-score-a-rubric-for-ml-production-readiness-and-technical-debt-reduction/) |
| 📚 ⭐ | Martin Fowler / ThoughtWorks — [Continuous Delivery for Machine Learning (CD4ML)](https://martinfowler.com/articles/cd4ml.html) |
| 📄 | Ribeiro et al. — [Beyond Accuracy: Behavioral Testing of NLP Models with CheckList](https://arxiv.org/abs/2005.04118) (invariance / directional tests pattern) |
| 📚 | [GitHub Actions docs](https://docs.github.com/en/actions) |
| 💻 | [iterative/cml](https://github.com/iterative/cml) — metric diff comments on PRs (stretch) |
| 💻 | [deepchecks/deepchecks](https://github.com/deepchecks/deepchecks) — data & model test suites |

## M08

Registry, packaging & serving

| Type | Resource |
|------|----------|
| 📚 ⭐ | [MLflow Model Registry](https://mlflow.org/docs/latest/model-registry.html) (aliases replace stages) |
| 📚 ⭐ | [FastAPI](https://fastapi.tiangolo.com) · [Pydantic](https://docs.pydantic.dev) |
| 📚 ⭐ | [Docker build best practices](https://docs.docker.com/build/building/best-practices/) |
| 💻 | [bentoml/BentoML](https://github.com/bentoml/BentoML) · [kserve/kserve](https://github.com/kserve/kserve) · [SeldonIO/seldon-core](https://github.com/SeldonIO/seldon-core) ([Gambar 8, 9]) |
| 💻 | [locustio/locust](https://github.com/locustio/locust) — load testing |
| 📚 | [kind](https://kind.sigs.k8s.io) · [Helm docs](https://helm.sh/docs/) (stretch) |

## M09

Monitoring & drift

| Type | Resource |
|------|----------|
| 💻 ⭐ | [evidentlyai/evidently](https://github.com/evidentlyai/evidently) · [Evidently docs](https://docs.evidentlyai.com) |
| 💻 ⭐ | [NannyML/nannyml](https://github.com/NannyML/nannyml) — performance estimation without labels (CBPE) |
| 💻 | [SeldonIO/alibi-detect](https://github.com/SeldonIO/alibi-detect) — drift & outlier detectors |
| 📚 ⭐ | [Prometheus docs](https://prometheus.io/docs/introduction/overview/) · 💻 [prometheus/client_python](https://github.com/prometheus/client_python) · [Grafana docs](https://grafana.com/docs/grafana/latest/) |
| 📚 | Google SRE Book — [Monitoring Distributed Systems](https://sre.google/sre-book/monitoring-distributed-systems/) (four golden signals) |
| 📄 | Gama et al. — [A Survey on Concept Drift Adaptation](https://doi.org/10.1145/2523813) (ACM CSUR 2014) |
| 📄 | Yurdakul — [Statistical Properties of Population Stability Index](https://scholarworks.wmich.edu/dissertations/3208) (PSI thresholds and their sampling behaviour) |
| 📘 | Huyen, *DMLS* ch. 8 (distribution shifts & monitoring) |

## M10

Retraining & release strategy

| Type | Resource |
|------|----------|
| 📘 ⭐ | Huyen, *DMLS* ch. 9 (continual learning, test in production: shadow, A/B, canary, bandits) |
| 📚 | Chip Huyen — [Real‑time machine learning: challenges and solutions](https://huyenchip.com/2022/01/02/real-time-machine-learning-challenges-and-solutions.html) |
| 📚 | Martin Fowler — [Canary Release](https://martinfowler.com/bliki/CanaryRelease.html) |
| 📚 💻 | [Argo Rollouts docs](https://argoproj.github.io/argo-rollouts/) · [argoproj/argo-rollouts](https://github.com/argoproj/argo-rollouts) ([Gambar 12]) |

## M11

Governance, model risk & regulation

| Type | Resource |
|------|----------|
| 📄 ⭐ | Mitchell et al. — [Model Cards for Model Reporting](https://arxiv.org/abs/1810.03993) |
| 📄 | Gebru et al. — [Datasheets for Datasets](https://arxiv.org/abs/1803.09010) |
| ⚖️ ⭐ | Federal Reserve / OCC — [SR 11‑7: Guidance on Model Risk Management](https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107.htm) (global de‑facto MRM reference) |
| ⚖️ | NIST — [AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) |
| ⚖️ ⭐ | OJK — [Regulation portal](https://www.ojk.go.id/id/regulasi/Default.aspx): look up POJK 11/POJK.03/2022 (IT governance of commercial banks) and OJK's 2023 responsible & trustworthy AI code of conduct for fintech `[ASUMSI: confirm current version with Compliance]` |
| ⚖️ | IFRS 9 — [Financial Instruments](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-9-financial-instruments/). Indonesian adoption: PSAK 71, **renumbered PSAK 109 by IAI from 1 Jan 2024** `[ASUMSI: verify on iaiglobal.or.id]` — ECL staging, 12‑month vs lifetime PD |
| ⚖️ | BIS — [Basel Framework](https://www.bis.org/basel_framework/) (CRE30–36: IRB approach, PD estimation & validation) |
| ⚖️ | EBA — [Guidelines on PD/LGD estimation (EBA/GL/2017/16)](https://www.eba.europa.eu/regulation-and-policy/model-validation/guidelines-on-pd-lgd-estimation-and-treatment-of-defaulted-assets) (detailed practice for PD calibration, OOT validation) |

## M12

Security & privacy

| Type | Resource |
|------|----------|
| ⚖️ ⭐ | UU No. 27 Tahun 2022 tentang Pelindungan Data Pribadi — [JDIH BPK](https://peraturan.bpk.go.id/Details/229798/uu-no-27-tahun-2022) |
| ⚖️ | [PCI Security Standards Council](https://www.pcisecuritystandards.org) — PCI DSS (card data) |
| 📚 ⭐ | [OWASP Machine Learning Security Top 10](https://owasp.org/www-project-machine-learning-security-top-10/) · [OWASP API Security Top 10](https://owasp.org/API-Security/) |
| 📚 | [MITRE ATLAS](https://atlas.mitre.org) — adversarial threat landscape for ML |
| 📄 | Tramèr et al. — [Stealing Machine Learning Models via Prediction APIs](https://arxiv.org/abs/1609.02943) |
| 💻 | [microsoft/presidio](https://github.com/microsoft/presidio) — PII detection & anonymization |
| 💻 ⭐ | [aquasecurity/trivy](https://github.com/aquasecurity/trivy) · [gitleaks/gitleaks](https://github.com/gitleaks/gitleaks) · [pypa/pip-audit](https://github.com/pypa/pip-audit) |

## M13

Capstone — reuse everything above; reference implementations to compare against:

- 💻 [DataTalksClub/mlops-zoomcamp](https://github.com/DataTalksClub/mlops-zoomcamp) (project rubric is a good benchmark)
- 💻 [GokuMohandas/Made-With-ML](https://github.com/GokuMohandas/Made-With-ML)
- 💻 [Fraud-Detection-Handbook/fraud-detection-handbook](https://github.com/Fraud-Detection-Handbook/fraud-detection-handbook)
- 💻 [feast-dev/feast-credit-score-local-tutorial](https://github.com/feast-dev/feast-credit-score-local-tutorial)

## Datasets (links)

| Dataset | Link |
|---------|------|
| Credit Card Fraud (ULB) | https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud |
| IEEE‑CIS Fraud Detection | https://www.kaggle.com/c/ieee-fraud-detection |
| PaySim | https://www.kaggle.com/datasets/ealaxi/paysim1 |
| Give Me Some Credit | https://www.kaggle.com/c/GiveMeSomeCredit |
| Home Credit Default Risk | https://www.kaggle.com/c/home-credit-default-risk |
| German Credit (Statlog) | https://archive.ics.uci.edu/dataset/144/statlog+german+credit+data |
