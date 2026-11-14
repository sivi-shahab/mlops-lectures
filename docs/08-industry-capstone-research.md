# Industry‑Grade Capstone for Credit Scoring & Fraud Detection: Research Report

*Generated: 2026‑11‑14 | Sources: 45+ | Confidence: High for datasets/repos/venues, Medium for vendor performance claims, Low for Indonesian bank case studies (little public data)*

## Executive summary

A professional capstone should copy what industry does, not just what a tutorial does. Four kinds of evidence point the same way:

- **Research from industry teams:** practitioners at Feedzai, Capital One, eBay, IBM, NVIDIA and J.P. Morgan publish on time‑aware data splits, fixed false‑positive‑rate budgets, fairness checks under data bias, and streaming features.
- **Benchmarks built by industry:** Feedzai's BAF, IBM's TabFormer and AMLworld, and the Home Credit Stability competition encode real operating constraints. These are temporal drift, extreme class imbalance, protected attributes, and **stability over time**, not only accuracy.
- **Venues:** the ACM ICAIF workshops on fraud and on AI in digital finance, the KDD Machine Learning in Finance workshop, and the Edinburgh Credit Scoring & Credit Control conference set the bar for how results are written and defended.
- **Reference implementations:** the NVIDIA Financial Fraud Blueprint, the RAPIDS fraud MLOps pipeline, Databricks fraud accelerators, IBM Multi‑GNN and Feedzai's BAF code show how the pieces fit together.

The resulting capstone, in [`capstone/industry/README.md`](../capstone/industry/README.md), uses these datasets, evaluation protocols and deliverable formats.

## 1. Industry research on real or realistic data

| Finding | Source |
|---------|--------|
| Graph neural network inference is split into batch entity embeddings and real‑time scoring, and message passing only uses past data (no future leakage) | eBay — [BRIGHT, CIKM 2022](https://arxiv.org/abs/2205.13084) |
| A graph formulation of account takeover (GraphSAGE on session graphs) beat the bank's production XGBoost model; the authors attribute most of the gain to the graph framing | [Capital One](https://www.capitalone.com/tech/publications/spatio-temporal-directed-graph-learning-for-fraud-detection) |
| A streaming engine built for fraud keeps large real‑time sliding windows at millisecond latency; the authors argue the hopping windows in generic engines such as Flink are inadequate for this | Feedzai — [Railgun, VLDB 2021](https://www.vldb.org/pvldb/vol14/p3069-bizarro.pdf) · [engineering blog](https://medium.com/feedzaitech/railgun-a-new-weapon-for-mission-critical-streaming-tasks-6432dd66a244) |
| Fairness‑blind models trade fairness against accuracy differently under each type of data bias in account‑opening fraud | Feedzai — [Understanding unfairness in fraud detection (KDD 2022 workshop)](https://arxiv.org/abs/2207.06273) |
| Open‑source tooling for fair ML experiments: Aequitas Flow and FairGBM | [Aequitas Flow](https://arxiv.org/abs/2405.05809) · [FairGBM (ICLR 2023)](https://arxiv.org/abs/2103.01632) |
| Sequence models applied to fraud and other financial data | [Capital One at KDD 2025](https://www.capitalone.com/tech/ai/kdd-2025/) |
| American Express serves fraud models with Triton + TensorRT under a ~2 ms requirement *(vendor)* | [NVIDIA case study](https://www.nvidia.com/en-us/case-studies/american-express-prevents-fraud-and-foils-cybercrime-with-nvidia-ai-solutions/) |
| Delayed labels: fraud ground truth arrives 1–6 months after the prediction | [Sethi et al., ECML‑PKDD 2025](https://mlanthology.org/ecmlpkdd/2025/sethi2025ecmlpkdd-proactive) |
| Credit default prediction with recurrent neural networks + XGBoost on Amex statement data (a top‑10 Kaggle solution) | [NVIDIA blog](https://developer.nvidia.com/blog/predicting-credit-defaults-using-time-series-models-with-recursive-neural-networks-and-xgboost/) |
| Transaction "foundation models" trained on TabFormer | [NVIDIA blog](https://developer.nvidia.com/blog/build-your-own-transaction-foundation-model-for-financial-intelligence/) |
| Survival analysis is the recommended method for lifetime PD under IFRS 9 | [arXiv 2507.15441](https://arxiv.org/abs/2507.15441) |
| Interpretable boosting (EBM) performed on par with or better than XGBoost in credit scoring *(preprint)* | [arXiv 2509.11389](https://arxiv.org/abs/2509.11389) |

**Regulator surveys (adoption context):** in the Bank of England/FCA 2024 AI survey, fraud detection was among the top use cases (33 %), and 55 % of AI use cases involve some automated decision‑making ([Bank of England](https://www.bankofengland.co.uk/report/2024/artificial-intelligence-in-uk-financial-services-2024); [Burges Salmon summary](https://www.burges-salmon.com/articles/102jpbu/ai-hot-off-the-press-from-the-bank-of-england-and-fca-how-is-it-being-used-ac)). The 2022 report includes credit underwriting case studies ([Bank of England 2022](https://www.bankofengland.co.uk/report/2022/machine-learning-in-uk-financial-services)).

**Indonesia:**
- Bank Indonesia's working paper WP/14/2025 proposes a hybrid of clustering, classification and graph ML to map illegal online‑gambling payment networks ([BI WP‑14‑2025](https://www.bi.go.id/id/publikasi/kajian/Documents/WP-14-2025.pdf)).
- An earlier study applies ML to e‑channel and ATM fraud at Bank BJB ([BRIN repository](https://karya.brin.go.id/13135/1/2_2_2021_42-61_2714-5794_3.pdf)).
- **Gap:** no public, detailed case study from BCA, BRI or Mandiri was found. Treat vendor claims (e.g., "up to 60 % loss reduction") as unverified.

## 2. Industry benchmark datasets

| Dataset | Domain | Why it is industry‑grade | Limits |
|---------|--------|--------------------------|--------|
| **Feedzai BAF** — [repo](https://github.com/feedzai/bank-account-fraud) · [paper (NeurIPS 2022 D&B)](https://arxiv.org/abs/2211.13358) | Bank account‑opening fraud | 6 variants of ~1 M rows generated from a real dataset; temporal months, strong imbalance, protected attributes, controlled bias types | Synthetic (GAN plus noise); application fraud, not card transactions |
| **IBM TabFormer** — [repo](https://github.com/IBM/TabFormer) · [paper](https://arxiv.org/abs/2011.01843) | Card transactions | ~24 M transactions, ~0.12 % fraud, user/card/merchant IDs and timestamps, which enables velocity features and time‑based splits ([NVIDIA](https://developer.nvidia.com/blog/build-your-own-transaction-foundation-model-for-financial-intelligence/)) | Synthetic; US‑centric |
| **IBM AMLworld** — [paper (NeurIPS 2023)](https://arxiv.org/abs/2306.16424) · [Multi‑GNN repo](https://github.com/IBM/Multi-GNN) | Anti‑money‑laundering (AML) transaction graph | Multi‑agent simulation with criminal agents; datasets of several sizes; graph model baselines | AML, not fraud; synthetic |
| **J.P. Morgan synthetic data** — [program page (payments fraud, AML)](https://www.jpmorganchase.com/about/technology/research/ai/synthetic-data) | Payments fraud, AML | Produced by a bank's AI research team with a planning simulator | Access by request; limited features ([arXiv 2509.18499](https://arxiv.org/abs/2509.18499)) |
| **Home Credit — Credit Risk Model Stability (Kaggle 2024)** | Consumer credit | Multi‑table data with `WEEK_NUM`; the metric rewards *stable* Gini over time: mean(gini) + 88·min(0, slope) − 0.5·std(residuals) ([project write‑up](https://www.erdosinstitute.org/project-database/spring-2024/home-credit---credit-risk-model-stability-iii)) | Competition licence restrictions |
| **Amex Default Prediction (Kaggle 2022)** | Behavioural credit | Monthly statement sequences; the most popular competition of 2022, with more than 4,000 teams ([summary](https://bullettech.github.io/BulletTech/Main_Course/Machine_Learning/2022-08-30-AMEX-Kaggle-Summary/)) | Anonymised features; competition licence |
| **FICO HELOC (xML Challenge)** — [OpenML](https://api.openml.org/d/45554) · [AIX360 tutorial](https://nbviewer.jupyter.org/github/IBM/AIX360/blob/master/examples/tutorials/HELOC.ipynb) | Credit, explainability | Built by FICO for explainability; real anonymised applications | Small (~10 k rows) |
| **TabReD** — [paper](https://arxiv.org/abs/2406.19380) | Tabular benchmarks including Home Credit | Industry tabular data split by time | Benchmarking focus |

## 3. Seminars, workshops & conferences (venue standard)

| Venue | Relevance |
|-------|-----------|
| ACM ICAIF 2025 — [AI for Financial Fraud Detection & Prevention workshop](https://sites.google.com/view/icaif-fraud-detection-workshop) ([CFP](https://easychair.org/cfp/ICAIF25-AIFIND)) | 8‑page full / 4‑page short papers, double‑blind; topics include graph detection, reinforcement learning, federated learning |
| ICAIF 2025 — [AI & Data Science for Digital Finance (AI4DF)](https://sites.google.com/view/ai4df/home) | Fraud, risk, compliance; keynotes and panel |
| [KDD Machine Learning in Finance workshop 2025](https://sites.google.com/view/kdd-mlf-2025) · [2026](https://sites.google.com/view/kdd-mlf-2026) | Fraud/abuse, money laundering, credit; encourages short industry papers |
| [Credit Scoring & Credit Control Conference (Edinburgh)](https://crc.business-school.ed.ac.uk/conferences/highlights) | 2025: >100 papers in five parallel sessions (ML/AI, XAI, fairness, GenAI); Equifax keynote on ML in a regulated bureau; next edition 2027 |
| [AIFIN‑2025 @ ECAI](https://easychair.org/cfp/AIFIN2025) | Card and mortgage fraud, early default detection |
| Free workshops/tutorials: [RAPIDS fraud MLOps pipeline (cuDF, Prefect, MLflow, Triton)](https://docs.rapids.ai/deployment/stable/examples/fraud-detection-mlops-pipeline/notebook/) · [Databricks retail banking fraud demo](https://www.databricks.com/resources/demos/tutorials/lakehouse-platform/retail-banking-fraud-detection) | Hands‑on reference pipelines *(vendor)* |

**Inference:** writing the capstone result as an ICAIF/KDD‑MLF‑style short paper and presenting it as a seminar talk makes the work comparable to industry submissions.

## 4. Industry reference repositories

| Repo | What to reuse |
|------|---------------|
| [feedzai/bank-account-fraud](https://github.com/feedzai/bank-account-fraud) | Variant sampling, LightGBM baselines, fairness evaluation |
| [dssg/aequitas](https://github.com/dssg/aequitas) · [feedzai/fairgbm](https://github.com/feedzai/fairgbm) | Bias audit; fairness‑constrained gradient boosting |
| [IBM/TabFormer](https://github.com/IBM/TabFormer) | Transaction data + tabular transformer |
| [IBM/Multi-GNN](https://github.com/IBM/Multi-GNN) | Graph models (GIN, GAT, PNA, RGCN) for transaction graphs |
| [NVIDIA Financial Fraud Detection Blueprint](https://build.nvidia.com/nvidia/financial-fraud-detection) | GraphSAGE embeddings → XGBoost → Triton with Shapley values |
| [rapidsai/deployment — fraud MLOps example](https://docs.rapids.ai/deployment/stable/examples/fraud-detection-mlops-pipeline/notebook/) | Prefect + MLflow + Triton lifecycle |
| [databricks-industry-solutions/fraud-orchestration](https://github.com/databricks-industry-solutions/fraud-orchestration) · [geoscan-fraud](https://github.com/databricks-industry-solutions/geoscan-fraud) | Rules + ML orchestration; geospatial fraud |
| [Fraud-Detection-Handbook](https://github.com/Fraud-Detection-Handbook/fraud-detection-handbook) | Simulator, prequential validation |
| [IBM/AIX360](https://github.com/Trusted-AI/AIX360) | HELOC explainability tutorial |
| [Nicolas-Bolouri/LGBM-Solution-Amex-Kaggle](https://github.com/Nicolas-Bolouri/LGBM-Solution-Amex-Kaggle) | Community Amex solution (not an official winner's repo) |

## Key takeaways

- **Evaluate like industry.** For fraud, report recall at a fixed false‑positive rate or alert budget, amount‑weighted recall, latency and fairness of false‑positive rates. For credit, report time‑stability of Gini, out‑of‑time performance, calibration and PSI.
- **Combine datasets.** No single public dataset covers everything. Use TabFormer for real‑time transaction fraud, BAF for fairness and drift, Home Credit Stability for credit stability, HELOC for explanations, and the repo's synthetic generator for Indonesian context and drift injection.
- **Package like industry.** Deliver a working system, a Model Development Document, an independent validation report, and a workshop‑format paper + talk.

## Gaps & caveats

- Kaggle competition data has licence/usage restrictions. Use it for learning only and cite the rules.
- Vendor claims (Kumo, Oradian, Feedzai marketing figures) are unverified.
- No first‑hand public case studies from large Indonesian banks were found.
- Official winner write‑ups for Amex and Home Credit are on Kaggle discussion pages, which were not retrieved here.

## Methodology

14 web searches on 2026‑11‑14. Topics: Feedzai BAF; IBM TabFormer, AMLworld and Multi‑GNN; Home Credit Stability; Amex Default; J.P. Morgan synthetic data; ICAIF 2025 workshops; KDD‑MLF; the Bank of England/FCA surveys; NVIDIA and AWS references; Databricks accelerators; FICO HELOC; the Edinburgh credit scoring conference; Feedzai fairness work and Railgun; Indonesian bank cases. Combined with the expert‑track research in [06‑expert‑research‑report.md](06-expert-research-report.md). Sources were prioritised in this order: peer‑reviewed and official first, then industry research labs, then vendor material (labelled as such).
