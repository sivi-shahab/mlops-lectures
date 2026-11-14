# Learning Resources — Intermediate Track (M01–M13)

Lectures, videos, blogs and repos for each module. Books and papers are in the [reading list](05-reading-list.md).
🎓 lecture/course · 🎥 video · ✍️ blog/case study · 💻 GitHub repo. ⭐ = do this first. All links were checked on 2026‑11‑14 (videos via YouTube oEmbed: title and channel confirmed). *(vendor)* = produced by a tool vendor.

## Whole program

| Type | Resource | Notes |
|------|----------|-------|
| 🎓 ⭐ | [MLOps Zoomcamp — DataTalksClub](https://github.com/DataTalksClub/mlops-zoomcamp) · 🎥 [YouTube playlist](https://www.youtube.com/playlist?list=PL3MmuxUbc_hIUISrluw_A7wDSmfOhErJK) | Free; tracking, orchestration, deployment, monitoring with code |
| 🎓 ⭐ | [CMU — Machine Learning in Production (Kästner)](https://mlip-cmu.github.io/) · [open‑access book](https://mlip-cmu.github.io/book/) | University course; slides, labs, free MIT Press book |
| 🎓 | [Stanford CS 329S — ML Systems Design](https://stanford-cs329s.github.io/syllabus.html) | Chip Huyen; lecture notes & slides |
| 🎓 | [Full Stack Deep Learning 2022](https://fullstackdeeplearning.com/course/2022/) · 🎥 [playlist](https://www.youtube.com/playlist?list=PL1T8fO7ArWleMMI8KPJ_5D5XSlovTW_Ur) | Lectures on deployment, continual learning, monitoring |
| 🎓 | [Made With ML](https://madewithml.com) | Self‑paced production ML course |
| ✍️ | [Evidently — ML system design: case studies](https://www.evidentlyai.com/ml-system-design) · [ZenML — MLOps database](https://www.zenml.io/mlops-database) | Hundreds of real company write‑ups (search "fraud", "credit") |
| ✍️ | [Eugene Yan](https://eugeneyan.com) · [Chip Huyen blog](https://huyenchip.com/blog/) | Applied ML systems writing |
| 💻 | [eugeneyan/applied-ml](https://github.com/eugeneyan/applied-ml) · [kelvins/awesome-mlops](https://github.com/kelvins/awesome-mlops) | Curated industry papers & tools |

## M01

Problem framing & architecture

| Type | Resource |
|------|----------|
| 🎥 ⭐ | [A Chat with Andrew on MLOps: From Model‑centric to Data‑centric AI](https://www.youtube.com/watch?v=06-AZXmwHjo) — DeepLearningAI |
| 🎥 | [Machine Learning, Technical Debt, and You — D. Sculley](https://www.youtube.com/watch?v=V18AsBIHlWs) — PAPIs.io |
| 🎓 | [CMU MLiP book](https://mlip-cmu.github.io/book/) — chapters on ML systems and requirements |
| ✍️ ⭐ | Stripe — [How we built it: Stripe Radar](https://stripe.com/blog/how-we-built-it-stripe-radar) · ByteByteGo — [How Stripe detects fraud within 100 ms](https://blog.bytebytego.com/p/how-stripe-detects-fraudulent-transactions) |
| ✍️ | Monzo — [Machine learning at Monzo in 2025](https://monzo.com/blog/machine-learning-at-monzo-in-2025) |
| 💻 | [chiphuyen/machine-learning-systems-design](https://github.com/chiphuyen/machine-learning-systems-design) |

## M02

Data engineering, versioning, validation, feature store

| Type | Resource |
|------|----------|
| 🎥 ⭐ | [Versioning Data with DVC (Hands‑On Tutorial)](https://www.youtube.com/watch?v=kLKBcPonMYw) — DVCorg |
| 🎥 | [Feature Stores: an Operational Bridge Between ML Models and Data](https://www.youtube.com/watch?v=_omcXenypmo) — PyData Global 2021 |
| 🎓 | [DVC — Data versioning tutorial](https://dvc.org/doc/start/data-management/data-versioning) |
| ✍️ | Tecton — [What is a feature store?](https://www.tecton.ai/blog/what-is-a-feature-store/) *(vendor)* · [featurestore.org](https://www.featurestore.org) · Hopsworks — [Feature store dictionary](https://www.hopsworks.ai/dictionary/feature-store) *(vendor)* |
| 💻 ⭐ | [feast-dev/feast-workshop](https://github.com/feast-dev/feast-workshop) |
| 💻 | [amphibian-dev/toad](https://github.com/amphibian-dev/toad) — credit binning/WoE toolkit · [tutorial](https://toad.readthedocs.io/en/latest/tutorial.html) |

## M03

Experiment tracking & reproducibility

| Type | Resource |
|------|----------|
| 🎥 ⭐ | [MLFlow Tutorial | ML Ops Tutorial](https://www.youtube.com/watch?v=6ngxBkx05Fs) — codebasics |
| 🎓 | [MLflow — Getting started](https://mlflow.org/docs/latest/getting-started/index.html) · MLOps Zoomcamp module 2 (experiment tracking) |
| ✍️ | [MLflow blog](https://mlflow.org/blog) |
| 📄 | Shankar et al. — [Operationalizing Machine Learning: An Interview Study](https://arxiv.org/abs/2209.09125) (how practitioners really run experiments) |
| 💻 | [GokuMohandas/Made-With-ML](https://github.com/GokuMohandas/Made-With-ML) |

## M04

Training pipeline & orchestration

| Type | Resource |
|------|----------|
| 🎥 ⭐ | [Airflow Tutorial for Beginners — Full Course in 2 Hours](https://www.youtube.com/watch?v=K9AnJ9_ZAXE) — coder2j |
| 🎓 | [Airflow — Fundamental concepts tutorial](https://airflow.apache.org/docs/apache-airflow/stable/tutorial/fundamentals.html) · MLOps Zoomcamp module 3 (orchestration) |
| ✍️ | Maxime Beauchemin — Functional Data Engineering (see [reading list](05-reading-list.md#m04)) |
| 💻 | [DataTalksClub/mlops-zoomcamp](https://github.com/DataTalksClub/mlops-zoomcamp) — orchestration folder |

## M05

Domain evaluation (fraud & credit)

| Type | Resource |
|------|----------|
| 🎥 ⭐ | [Detecting Financial Fraud at Scale with Machine Learning — Elena Boiarskaia (H2O.ai)](https://www.youtube.com/watch?v=5v0RgVlKiXI) — Databricks |
| 🎥 | [Train, Evaluate, Repeat: Building a Credit Card Fraud Detection System (Stripe)](https://pyvideo.org/pydata-la-2018/train-evaluate-repeat-building-a-credit-card-fraud-detection-system.html) — PyData LA 2018 |
| 🎓 ⭐ | [Fraud Detection Handbook](https://fraud-detection-handbook.github.io/fraud-detection-handbook/) — ch. 4–5 (metrics, validation) |
| 🎓 | [Toad tutorial — WoE binning & scorecard on German Credit](https://toad.readthedocs.io/en/latest/tutorial.html) |
| 🎥 | [QuintEdge — free credit risk demo lectures (PD, WoE/IV, scorecard)](https://quintedge.com/credit-risk-modeling-demo-videos) *(vendor; free per lecture)* |
| 💻 | [Fraud-Detection-Handbook/fraud-detection-handbook](https://github.com/Fraud-Detection-Handbook/fraud-detection-handbook) · [optbinning](https://github.com/guillermo-navas-palencia/optbinning) |

> Gap: no verified free YouTube lecture series on credit scorecards was found; use the Toad/optbinning tutorials and Siddiqi's book.

## M06

Explainability & fairness

| Type | Resource |
|------|----------|
| 🎥 ⭐ | [Tutorial: 21 fairness definitions and their politics](https://www.youtube.com/watch?v=jIXIuYdnyyk) — Arvind Narayanan |
| 🎥 | [Explainable AI for Science and Medicine (SHAP)](https://www.youtube.com/watch?v=B-c8tIgchu0) — Microsoft Research |
| 🎓 ⭐ | [GWU — Responsible Machine Learning (Patrick Hall)](https://jphall663.github.io/GWU_rml/) · [repo](https://github.com/jphall663/GWU_rml) — uses lending data |
| ✍️ | [Google PAIR Explorables](https://pair.withgoogle.com/explorables/) — interactive fairness explainers |
| 💻 | [microsoft/responsible-ai-toolbox](https://github.com/microsoft/responsible-ai-toolbox) · [jphall663/awesome-machine-learning-interpretability](https://github.com/jphall663/awesome-machine-learning-interpretability) |

## M07

CI/CD/CT

| Type | Resource |
|------|----------|
| 🎥 ⭐ | [GitHub Actions Tutorial — CI/CD Pipeline with Docker](https://www.youtube.com/watch?v=R8_veQiYBjI) — TechWorld with Nana |
| 🎓 | [GitHub Actions quickstart](https://docs.github.com/en/actions/writing-workflows/quickstart) · MLOps Zoomcamp module 6 (best practices) |
| ✍️ | Martin Fowler — CD4ML (see [reading list](05-reading-list.md#m07)) |
| 💻 | [GokuMohandas/Made-With-ML](https://github.com/GokuMohandas/Made-With-ML) — CI/CD workflows |

## M08

Registry, packaging & serving

| Type | Resource |
|------|----------|
| 🎥 ⭐ | [Docker Tutorial for Beginners — Full DevOps Course](https://www.youtube.com/watch?v=fqMOX6JJhGo) — freeCodeCamp |
| 🎥 | [Python API Development — Comprehensive Course (FastAPI)](https://www.youtube.com/watch?v=0sOvCWFmrtA) — freeCodeCamp |
| 🎥 | [Kubernetes Course — Full Beginners Tutorial](https://www.youtube.com/watch?v=d6WC5n9G_sM) — freeCodeCamp (stretch) |
| 🎓 | [FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/) · FSDL 2022 Lecture 5: Deployment ([playlist](https://www.youtube.com/playlist?list=PL1T8fO7ArWleMMI8KPJ_5D5XSlovTW_Ur)) |
| 💻 | [DataTalksClub/mlops-zoomcamp](https://github.com/DataTalksClub/mlops-zoomcamp) — deployment folder |

## M09

Monitoring & drift

| Type | Resource |
|------|----------|
| 🎓 ⭐ | [Evidently — Open‑source ML Observability Course](https://learn.evidentlyai.com/) (40 lessons) · 🎥 [playlist](https://www.youtube.com/playlist?list=PL9omX6impEuOpTezeRF-M04BW3VfnPBRF) |
| 🎥 | [How Prometheus Monitoring works](https://www.youtube.com/watch?v=h4Sl21AKiDg) — TechWorld with Nana |
| ✍️ | [Evidently blog](https://www.evidentlyai.com/blog) · [NannyML blog](https://www.nannyml.com/blog) |
| 💻 | [evidentlyai/ml_observability_course](https://github.com/evidentlyai/ml_observability_course) |

## M10

Retraining & release strategy

| Type | Resource |
|------|----------|
| 🎥 ⭐ | FSDL 2022 Lecture 6: Continual Learning ([playlist](https://www.youtube.com/playlist?list=PL1T8fO7ArWleMMI8KPJ_5D5XSlovTW_Ur)) |
| ✍️ | Chip Huyen — Real‑time ML: challenges and solutions (see [reading list](05-reading-list.md#m10)) |
| 🎥 | [ArgoCD Tutorial for Beginners — GitOps](https://www.youtube.com/watch?v=MeU5_k9ssrs) — TechWorld with Nana (stretch) |
| 💻 | [argoproj/argocd-example-apps](https://github.com/argoproj/argocd-example-apps) (stretch) |

## M11

Governance & model risk

| Type | Resource |
|------|----------|
| 🎓 ⭐ | [GWU Responsible ML](https://jphall663.github.io/GWU_rml/) — model governance & risk lectures |
| ✍️ ⭐ | OJK — [Tata Kelola Kecerdasan Artifisial Perbankan Indonesia](https://ojk.go.id/id/Publikasi/Roadmap-dan-Pedoman/Perbankan/Pages/Tata-Kelola-Kecerdasan-Artifisial-Perbankan-Indonesia.aspx) |
| ✍️ | [SR 11‑7](https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107.htm) |
| 💻 | [jphall663/awesome-machine-learning-interpretability](https://github.com/jphall663/awesome-machine-learning-interpretability) — includes governance resources |

## M12

Security & privacy

| Type | Resource |
|------|----------|
| 🎓 ⭐ | [OWASP ML Security Top 10](https://owasp.org/www-project-machine-learning-security-top-10/) · [MITRE ATLAS](https://atlas.mitre.org) |
| 💻 | [microsoft/presidio](https://github.com/microsoft/presidio) · [aquasecurity/trivy](https://github.com/aquasecurity/trivy) |

## M13

Capstone

| Type | Resource |
|------|----------|
| 🎓 ⭐ | MLOps Zoomcamp — [project guidelines](https://github.com/DataTalksClub/mlops-zoomcamp) (peer‑review rubric for comparison) |
| 🎥 | [MLOps Zoomcamp playlist](https://www.youtube.com/playlist?list=PL3MmuxUbc_hIUISrluw_A7wDSmfOhErJK) — project demo examples |
