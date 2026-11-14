# Learning Resources — Expert Track (E01–E11)

Lectures, videos, blogs and repos for each expert module. Papers and books are in the [expert reading list](reading-list.md).
🎓 lecture/course · 🎥 video · ✍️ blog/case study · 💻 GitHub repo. ⭐ = do this first. Checked 2026‑11‑14 (videos via YouTube oEmbed).

## E01

Streaming feature platform

| Type | Resource |
|------|----------|
| 🎓 ⭐ | Confluent — [Apache Flink 101](https://developer.confluent.io/courses/apache-flink/intro/) (video course, ~3 h, includes event time & watermarks) · [Apache Kafka 101](https://developer.confluent.io/courses/apache-kafka/events/) *(vendor, free)* |
| 🎥 | [Apache Kafka Crash Course](https://www.youtube.com/watch?v=R873BlNVUB4) — Hussein Nasser |
| 🎥 | [Feature Stores: an Operational Bridge Between ML Models and Data](https://www.youtube.com/watch?v=_omcXenypmo) — PyData Global 2021 |
| ✍️ ⭐ | Nubank — [Avalanche stack and real‑time streaming applications at Nu](https://building.nubank.com/avalanche-stack-and-real-time-streaming-applications-at-nu/) |
| ✍️ | Kai Waehner — [Online feature store with Kafka and Flink](https://www.kai-waehner.de/blog/2025/09/15/online-feature-store-for-ai-and-machine-learning-with-apache-kafka-and-flink/) |
| 💻 | [confluentinc/demo-scene](https://github.com/confluentinc/demo-scene) · [feast-dev/feast-workshop](https://github.com/feast-dev/feast-workshop) |

## E02

Graph ML for fraud

| Type | Resource |
|------|----------|
| 🎓 ⭐ | [Stanford CS224W — Machine Learning with Graphs](https://web.stanford.edu/class/cs224w/) · 🎥 [Lecture 1.1 — Why Graphs (2021 series)](https://www.youtube.com/watch?v=JAB_plj2rbA) — Stanford Online |
| 🎥 | [Graph Neural Networks — a perspective from the ground up](https://www.youtube.com/watch?v=GXhBEj1ZtE8) |
| 🎓 | [Neo4j GraphAcademy](https://graphacademy.neo4j.com/) (free) · [PyG introduction](https://pytorch-geometric.readthedocs.io/en/latest/get_started/introduction.html) · [Splink docs](https://moj-analytical-services.github.io/splink/) |
| ✍️ | Neo4j — [Fraud detection use case](https://neo4j.com/use-cases/fraud-detection/) *(vendor)* · Capital One — [Spatio‑temporal graph learning for fraud](https://www.capitalone.com/tech/publications/spatio-temporal-directed-graph-learning-for-fraud-detection) |
| 💻 | [safe-graph/graph-fraud-detection-papers](https://github.com/safe-graph/graph-fraud-detection-papers) |

## E03

Delayed labels, active learning, conformal prediction

| Type | Resource |
|------|----------|
| 🎥 ⭐ | [A Tutorial on Conformal Prediction](https://www.youtube.com/watch?v=nql000Lu_iE) — Anastasios Angelopoulos |
| 🎓 | [MAPIE docs](https://mapie.readthedocs.io/) · [NannyML docs (CBPE)](https://nannyml.readthedocs.io/) |
| ✍️ | [NannyML blog](https://www.nannyml.com/blog) (performance estimation without labels) |
| 🎓 | Fraud Detection Handbook — [delayed feedback chapters](https://fraud-detection-handbook.github.io/fraud-detection-handbook/) |
| 💻 | [scikit-learn-contrib/MAPIE](https://github.com/scikit-learn-contrib/MAPIE) |

## E04

Adversarial robustness

| Type | Resource |
|------|----------|
| 🎓 ⭐ | [MITRE ATLAS](https://atlas.mitre.org) — case studies & tactics · [ART documentation](https://adversarial-robustness-toolbox.readthedocs.io/) |
| ✍️ | Monzo — [Representation learning for enhanced fraud detection](https://monzo.com/blog/representation-learning-for-enhanced-fraud-detection) (features fraudsters cannot cheaply manipulate) |
| 💻 | [Trusted-AI/adversarial-robustness-toolbox](https://github.com/Trusted-AI/adversarial-robustness-toolbox) |

> Gap: no verified free video on *tabular* fraud adversarial attacks; use the Kireev et al. and Cartella et al. papers.

## E05

Advanced credit risk

| Type | Resource |
|------|----------|
| 🎓 ⭐ | [InterpretML / EBM docs](https://interpret.ml/docs/) · [lifelines docs](https://lifelines.readthedocs.io/en/latest/) · [scikit‑survival docs](https://scikit-survival.readthedocs.io/) |
| 🎥 | [QuintEdge — free credit risk demo lectures](https://quintedge.com/credit-risk-modeling-demo-videos) *(vendor)* |
| ✍️ | Nubank — [How Nubank uses transformers to model financial habits at scale](https://building.nubank.com/how-nubank-uses-transformers-to-model-financial-habits-at-scale/) |
| 💻 | [interpretml/interpret](https://github.com/interpretml/interpret) · [amphibian-dev/toad](https://github.com/amphibian-dev/toad) |

> Gap: no verified free video course on IFRS 9 lifetime PD; rely on the arXiv survival tutorial and EBA guidelines in the reading list.

## E06

Causal decisioning

| Type | Resource |
|------|----------|
| 🎓 ⭐ | [Brady Neal — Introduction to Causal Inference](https://www.bradyneal.com/causal-inference-course) · 🎥 [lecture playlist](https://www.youtube.com/playlist?list=PLoazKTcS0Rzb6bb9L508cyJ1z-U9iWkA0) |
| 🎥 | [Susan Athey — Counterfactual Inference (NeurIPS 2018 tutorial)](https://www.youtube.com/watch?v=yKs6msnw9m8) |
| 🎓 | [Causal Inference for the Brave and True](https://matheusfacure.github.io/python-causality-handbook/) · [EconML docs](https://econml.azurewebsites.net/) · [DoWhy docs](https://www.pywhy.org/dowhy/) |
| 💻 | [py-why/EconML](https://github.com/py-why/EconML) · [st-tech/zr-obp](https://github.com/st-tech/zr-obp) |

## E07

High‑performance serving & Kubernetes

| Type | Resource |
|------|----------|
| 🎥 ⭐ | [ArgoCD Tutorial for Beginners — GitOps CD for Kubernetes](https://www.youtube.com/watch?v=MeU5_k9ssrs) — TechWorld with Nana |
| 🎥 ⭐ | [SLIs, SLOs, SLAs, oh my!](https://www.youtube.com/watch?v=tEylFyxbDLE) — Google Cloud Tech |
| 🎥 | [Kubernetes Course — Full Beginners Tutorial](https://www.youtube.com/watch?v=d6WC5n9G_sM) — freeCodeCamp |
| 🎓 | [Triton user guide](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/index.html) · [ONNX Runtime docs](https://onnxruntime.ai/docs/) · [KServe](https://kserve.github.io/website/) · [Kubernetes basics](https://kubernetes.io/docs/tutorials/kubernetes-basics/) · [Google SRE Workbook](https://sre.google/workbook/table-of-contents/) |
| 💻 | [argoproj/argocd-example-apps](https://github.com/argoproj/argocd-example-apps) · [triton-inference-server/fil_backend](https://github.com/triton-inference-server/fil_backend) |

## E08

Privacy‑enhancing ML

| Type | Resource |
|------|----------|
| 🎥 ⭐ | [Federated Learning: Machine Learning on Decentralized Data (Google I/O'19)](https://www.youtube.com/watch?v=89BGjQYA0uE) — TensorFlow |
| 🎓 ⭐ | DeepLearning.AI — [Intro to Federated Learning (with Flower)](https://www.deeplearning.ai/short-courses/intro-to-federated-learning/) · [Flower tutorial series](https://flower.ai/docs/framework/tutorial-series-what-is-federated-learning.html) |
| 🎓 | [Opacus tutorials (DP‑SGD)](https://opacus.ai/tutorials/) · [SDV docs](https://docs.sdv.dev/sdv) |
| ✍️ | UK Finance — [How federated learning strengthens fraud detection](https://www.ukfinance.org.uk/news-and-insight/blog/how-federated-learning-strengthens-fraud-detection-in-2025) |
| 💻 | [adap/flower](https://github.com/adap/flower) · [NVIDIA/NVFlare](https://github.com/NVIDIA/NVFlare) |

## E09

AI governance at scale

| Type | Resource |
|------|----------|
| ✍️ ⭐ | OJK — [Tata Kelola Kecerdasan Artifisial Perbankan Indonesia](https://ojk.go.id/id/Publikasi/Roadmap-dan-Pedoman/Perbankan/Pages/Tata-Kelola-Kecerdasan-Artifisial-Perbankan-Indonesia.aspx) · [press release](https://ojk.go.id/id/berita-dan-kegiatan/siaran-pers/Pages/Peluncuran-Tata-Kelola-Kecerdasan-Artifisial-Perbankan-Indonesia.aspx) |
| 🎓 | [Open Policy Agent docs](https://www.openpolicyagent.org/docs/latest/) |
| 🎓 | [GWU Responsible ML](https://jphall663.github.io/GWU_rml/) — governance lectures |
| 💻 | [open-policy-agent/conftest](https://github.com/open-policy-agent/conftest) |

## E10

LLMOps for fraud operations

| Type | Resource |
|------|----------|
| ✍️ ⭐ | Hamel Husain — [Your AI Product Needs Evals](https://hamel.dev/blog/posts/evals/) |
| ✍️ ⭐ | Monzo — [Combining generative AI and predictive modelling to fight financial crime](https://monzo.com/blog/combining-generative-ai-and-predictive-modelling-to-fight-financial-crime) |
| 🎓 | [promptfoo docs](https://www.promptfoo.dev/docs/intro/) · [Inspect docs](https://inspect.aisi.org.uk/) · [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/) |
| 💻 | [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) · [UKGovernmentBEIS/inspect_ai](https://github.com/UKGovernmentBEIS/inspect_ai) · [microsoft/presidio](https://github.com/microsoft/presidio) |

## E11

Capstone

| Type | Resource |
|------|----------|
| 🎓 | Google SRE — [Postmortem culture](https://sre.google/sre-book/postmortem-culture/) |
| ✍️ | [Evidently — ML system design case studies](https://www.evidentlyai.com/ml-system-design) — benchmark your design against industry write‑ups |
