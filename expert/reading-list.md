# Expert Track — Reading List & Reference Repositories

📘 book · 📄 paper · 📚 docs/guide · 💻 GitHub repo · ⚖️ regulation. ⭐ = read first. Items marked *(preprint)* or *(vendor)* are not peer‑reviewed or independently verified.

## E01

Real‑time streaming feature platform

| Type | Resource |
|------|----------|
| 📚 ⭐ | Apache Flink — [Timely stream processing (event time & watermarks)](https://nightlies.apache.org/flink/flink-docs-stable/docs/concepts/time/) · 💻 [apache/flink](https://github.com/apache/flink) |
| 📚 | [Feast — Stream feature views / push sources](https://docs.feast.dev/reference/data-sources/push) |
| 📚 | Kai Waehner — [Online feature store for AI/ML with Apache Kafka and Flink](https://www.kai-waehner.de/blog/2025/09/15/online-feature-store-for-ai-and-machine-learning-with-apache-kafka-and-flink/) *(vendor‑adjacent)* |
| 📚 | Alibaba Cloud — [Real‑time fraud detection pipeline architecture](https://www.alibabacloud.com/blog/real-time-fraud-detection-pipeline-architecture-on-alibaba-cloud_603297) (single sink to online + offline; out‑of‑order/duplicate effects) *(vendor)* |
| 📚 | AWS — [Streaming ingestion with SageMaker Feature Store and Amazon MSK](https://aws.amazon.com/blogs/machine-learning/use-streaming-ingestion-with-amazon-sagemaker-feature-store-and-amazon-msk-to-make-ml-backed-decisions-in-near-real-time/) *(vendor)* |
| 📚 | RisingWave — [The online/offline feature store problem](https://risingwave.com/blog/unified-online-offline-feature-store-sql/) *(vendor)* |
| 💻 | [redpanda-data/redpanda](https://github.com/redpanda-data/redpanda) · [bytewax/bytewax](https://github.com/bytewax/bytewax) · [risingwavelabs/risingwave](https://github.com/risingwavelabs/risingwave) |
| 📘 | Martin Kleppmann — *Designing Data‑Intensive Applications* (ch. 11 Stream Processing) |

## E02

Graph ML for fraud rings & entity resolution

| Type | Resource |
|------|----------|
| 📄 ⭐ | Lu et al. — [BRIGHT: Graph Neural Networks in Real‑Time Fraud Detection](https://arxiv.org/abs/2205.13084) (CIKM 2022; batch embeddings + real‑time scoring, leakage‑safe message passing) |
| 📄 | Capital One — [Spatio‑temporal directed graph learning for fraud detection](https://www.capitalone.com/tech/publications/spatio-temporal-directed-graph-learning-for-fraud-detection) |
| 📄 | Hamilton et al. — [Inductive Representation Learning on Large Graphs (GraphSAGE)](https://arxiv.org/abs/1706.02216) |
| 💻 ⭐ | [pyg-team/pytorch_geometric](https://github.com/pyg-team/pytorch_geometric) · [dmlc/dgl](https://github.com/dmlc/dgl) |
| 💻 | [safe-graph/graph-fraud-detection-papers](https://github.com/safe-graph/graph-fraud-detection-papers) — curated paper list · [safe-graph/DGFraud](https://github.com/safe-graph/DGFraud) |
| 💻 ⭐ | [moj-analytical-services/splink](https://github.com/moj-analytical-services/splink) — probabilistic record linkage |
| 📚 | [Neo4j Graph Data Science docs](https://neo4j.com/docs/graph-data-science/current/) (WCC, Louvain, node embeddings) |

## E03

Delayed & noisy labels, active learning, conformal prediction

| Type | Resource |
|------|----------|
| 📄 ⭐ | Dal Pozzolo et al. — [Credit Card Fraud Detection: A Realistic Modeling and a Novel Learning Strategy](https://doi.org/10.1109/TNNLS.2017.2736643) (feedback vs delayed samples) |
| 📄 | Carcillo et al. — [Streaming Active Learning Strategies for Real‑Life Credit Card Fraud Detection](https://arxiv.org/abs/1804.07481) |
| 📄 | Barata et al. (Feedzai) — [Active learning for imbalanced data under cold start](https://research.feedzai.com/oshuzuxa/2022/08/Barata_ActiveLearning_KDD-MLF2021.pdf) (KDD MLF 2021) |
| 📄 | Sethi et al. — [Proactive Detection of Model Degradation in Financial Fraud Prediction with Delayed Labels](https://mlanthology.org/ecmlpkdd/2025/sethi2025ecmlpkdd-proactive) (ECML‑PKDD 2025) |
| 📄 ⭐ | Angelopoulos & Bates — [A Gentle Introduction to Conformal Prediction](https://arxiv.org/abs/2107.07511) |
| 💻 ⭐ | [scikit-learn-contrib/MAPIE](https://github.com/scikit-learn-contrib/MAPIE) · [NannyML/nannyml](https://github.com/NannyML/nannyml) (CBPE) |
| 📚 | Fraud Detection Handbook — [delayed feedback & prequential validation chapters](https://fraud-detection-handbook.github.io/fraud-detection-handbook/) |

## E04

Adversarial robustness & red‑teaming

| Type | Resource |
|------|----------|
| 📄 ⭐ | Kireev, Kulynych & Troncoso — [Adversarial Robustness for Tabular Data through Cost and Utility Awareness](https://arxiv.org/abs/2208.13058) (NDSS 2023) |
| 📄 | Cartella et al. — [Adversarial Attacks for Tabular Data: Application to Fraud Detection and Imbalanced Data](https://arxiv.org/abs/2101.08030) |
| 📄 | Tramèr et al. — [Stealing Machine Learning Models via Prediction APIs](https://arxiv.org/abs/1609.02943) |
| 💻 ⭐ | [Trusted-AI/adversarial-robustness-toolbox](https://github.com/Trusted-AI/adversarial-robustness-toolbox) |
| 📚 ⭐ | [MITRE ATLAS](https://atlas.mitre.org) · [OWASP ML Security Top 10](https://owasp.org/www-project-machine-learning-security-top-10/) |

## E05

Advanced credit risk

| Type | Resource |
|------|----------|
| 📄 ⭐ | [Approaches for modelling the term‑structure of default risk under IFRS 9: a tutorial using discrete‑time survival analysis](https://arxiv.org/abs/2507.15441) (2025) |
| 📚 | MathWorks — [Overview of Lifetime Probability of Default Models](https://www.mathworks.com/help/risk/overview-of-lifetime-probability-of-default.html) |
| 📄 | Schwartz, Wang & Fang — [Enhancing ML Models Interpretability for Credit Scoring](https://arxiv.org/abs/2509.11389) (EBM vs XGBoost) *(preprint)* |
| 💻 ⭐ | [interpretml/interpret](https://github.com/interpretml/interpret) (EBM, `monotone_constraints`) |
| 📚 | XGBoost — [Monotonic constraints](https://xgboost.readthedocs.io/en/stable/tutorials/monotonic.html) |
| 💻 | [CamDavidsonPilon/lifelines](https://github.com/CamDavidsonPilon/lifelines) · [sebp/scikit-survival](https://github.com/sebp/scikit-survival) |
| ⚖️ | [IFRS 9 Financial Instruments](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-9-financial-instruments/) (PSAK 109 in Indonesia, formerly PSAK 71 `[ASUMSI: verify with IAI]`) |
| ⚖️ | EBA — [Guidelines on PD/LGD estimation](https://www.eba.europa.eu/regulation-and-policy/model-validation/guidelines-on-pd-lgd-estimation-and-treatment-of-defaulted-assets) |
| 📘 | Siddiqi — *Intelligent Credit Scoring*, reject‑inference chapter |

## E06

Causal decisioning & off‑policy evaluation

| Type | Resource |
|------|----------|
| 💻 ⭐ | [py-why/EconML](https://github.com/py-why/EconML) · [py-why/dowhy](https://github.com/py-why/dowhy) · [uber/causalml](https://github.com/uber/causalml) |
| 💻 | [st-tech/zr-obp](https://github.com/st-tech/zr-obp) — Open Bandit Pipeline (IPS, DR estimators) |
| 📄 | [Multi‑Treatment‑DML for credit limit optimization](https://arxiv.org/abs/2508.02183) (2025) *(preprint)* |
| 📄 | [Causal Learning for Credit Limit Adjustment in Revolving Lending Under Adversarial Goals](https://www.crc.business-school.ed.ac.uk/sites/crc/files/2024-01/Causal-Learning-for-Credit-Limit-Adjustment-in-Revolving-Lending-Under-Adversarial-Goals.pdf) (Credit Research Centre, Edinburgh) |
| 📘 ⭐ | Matheus Facure — [Causal Inference for the Brave and True](https://matheusfacure.github.io/python-causality-handbook/) (free online) |

## E07

High‑performance serving & Kubernetes platform

| Type | Resource |
|------|----------|
| 📚 ⭐ | [NVIDIA Triton Inference Server](https://github.com/triton-inference-server/server) · [FIL backend for tree models](https://github.com/triton-inference-server/fil_backend) |
| 📚 | NVIDIA — [Deploy a fraud detection XGBoost model with Triton](https://docs.nvidia.com/launchpad/data-science/fraud-detection/latest/fraud-detection-overview.html) · [American Express case study](https://www.nvidia.com/en-us/case-studies/american-express-prevents-fraud-and-foils-cybercrime-with-nvidia-ai-solutions/) *(vendor)* |
| 💻 | [microsoft/onnxruntime](https://github.com/microsoft/onnxruntime) · [onnx/onnxmltools](https://github.com/onnx/onnxmltools) · [microsoft/hummingbird](https://github.com/microsoft/hummingbird) |
| 📚 ⭐ | [Argo CD](https://argo-cd.readthedocs.io/) · [Argo Rollouts analysis](https://argoproj.github.io/argo-rollouts/features/analysis/) · [KServe](https://kserve.github.io/website/) |
| 📘 ⭐ | Google SRE Workbook — [Alerting on SLOs (burn rates)](https://sre.google/workbook/alerting-on-slos/) |

## E08

Privacy‑enhancing ML

| Type | Resource |
|------|----------|
| 📄 ⭐ | [Federated learning for payment fraud with NVIDIA FLARE and DP‑SGD](https://arxiv.org/abs/2603.13617) (2026) *(preprint)* |
| 📚 | UK Finance — [How federated learning strengthens fraud detection](https://www.ukfinance.org.uk/news-and-insight/blog/how-federated-learning-strengthens-fraud-detection-in-2025) |
| 💻 ⭐ | [adap/flower](https://github.com/adap/flower) · [NVIDIA/NVFlare](https://github.com/NVIDIA/NVFlare) |
| 💻 | [pytorch/opacus](https://github.com/pytorch/opacus) — DP‑SGD |
| 💻 | [sdv-dev/SDV](https://github.com/sdv-dev/SDV) · [sdv-dev/SDMetrics](https://github.com/sdv-dev/SDMetrics) |
| 📄 | Abadi et al. — [Deep Learning with Differential Privacy](https://arxiv.org/abs/1607.00133) |

## E09

AI governance at scale

| Type | Resource |
|------|----------|
| ⚖️ ⭐ | OJK — [Tata Kelola Kecerdasan Artifisial Perbankan Indonesia](https://ojk.go.id/id/Publikasi/Roadmap-dan-Pedoman/Perbankan/Pages/Tata-Kelola-Kecerdasan-Artifisial-Perbankan-Indonesia.aspx) (April 2025) · [press release](https://ojk.go.id/id/berita-dan-kegiatan/siaran-pers/Pages/Peluncuran-Tata-Kelola-Kecerdasan-Artifisial-Perbankan-Indonesia.aspx) |
| ⚖️ ⭐ | [SR 11‑7 Model Risk Management](https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107.htm) · [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework) |
| ⚖️ | [EU AI Act — official text (EUR‑Lex)](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) — Annex III 5(b) credit scoring; check status of 2026 postponement reports before relying on dates |
| 💻 ⭐ | [open-policy-agent/opa](https://github.com/open-policy-agent/opa) · [open-policy-agent/conftest](https://github.com/open-policy-agent/conftest) |

## E10

LLMOps for fraud operations

| Type | Resource |
|------|----------|
| 💻 ⭐ | [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) · [UKGovernmentBEIS/inspect_ai](https://github.com/UKGovernmentBEIS/inspect_ai) — eval frameworks |
| 💻 | [NVIDIA/NeMo-Guardrails](https://github.com/NVIDIA/NeMo-Guardrails) · [microsoft/presidio](https://github.com/microsoft/presidio) |
| 📚 ⭐ | [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/) |
| 📚 | Global Economics Group — [Agentic AI development for risk‑based workflows in banking](https://www.globaleconomicsgroup.com/wp-content/uploads/2026/01/Agentic-AI-development-for-risk-based-workflows-in-banking.pdf) (no direct SQL, safe tool wrappers) |
| 📚 | American Banker — [How banks can safely use AI in the cyber operations center](https://www.americanbanker.com/news/how-banks-can-safely-use-ai-in-the-cyber-operations-center) |

## E11

Capstone: reuse all of the above, plus the Google SRE book chapter on [postmortem culture](https://sre.google/sre-book/postmortem-culture/).
