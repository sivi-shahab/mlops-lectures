# Expert Level for Fraud & Credit MLOps: Research Report

*Generated: 2026‑11‑14 | Sources: 30+ (search results, papers, official pages) | Confidence: Medium‑High for technical patterns, Medium for regulatory dates*

## Executive summary

Moving from intermediate to expert MLOps in banking means moving from *operating one pipeline* to *designing a platform* and defending it to risk and regulators. The research points to five capability gaps that the intermediate track does not cover: (1) streaming features with provable online/offline parity, (2) graph signals for organized fraud, (3) learning and monitoring under delayed labels, (4) credit models that meet both interpretability and IFRS 9 / PSAK 109 lifetime‑PD needs, and (5) governance that is enforced in code and aligned with OJK's 2025 AI governance guide. Adversarial robustness, causal decisioning, privacy‑enhancing ML, and LLM copilots are emerging areas with growing but less settled evidence. These findings define modules E01–E11.

## 1. Streaming features and train/serve parity

- The standard pattern is a stream processor (Flink, Kafka Streams, Spark) computing features from Kafka into a low‑latency online store, with a historical offline store for training ([Kai Waehner](https://www.kai-waehner.de/blog/2025/09/15/online-feature-store-for-ai-and-machine-learning-with-apache-kafka-and-flink/)).
- The main failure is two pipelines computing nearly the same feature; the remedy is one definition materialized to both stores and point‑in‑time joins ([RisingWave](https://risingwave.com/blog/unified-online-offline-feature-store-sql/), vendor).
- A single sink writing to online and offline stores keeps them consistent; out‑of‑order or duplicate events cause false positives/negatives in velocity features ([Alibaba Cloud](https://www.alibabacloud.com/blog/real-time-fraud-detection-pipeline-architecture-on-alibaba-cloud_603297), vendor).
- Feast supports streaming feature views; AWS documents MSK + Flink + SageMaker Feature Store for near‑real‑time fraud ([AWS](https://aws.amazon.com/blogs/machine-learning/use-streaming-ingestion-with-amazon-sagemaker-feature-store-and-amazon-msk-to-make-ml-backed-decisions-in-near-real-time/); [Kai Waehner](https://www.kai-waehner.de/blog/2025/09/15/online-feature-store-for-ai-and-machine-learning-with-apache-kafka-and-flink/)).
- **Gap:** no authoritative public benchmark for parity; hence E01 requires learners to *measure* it.

## 2. Graph ML for fraud

- BRIGHT splits GNN work into batch entity embeddings and real‑time transaction scoring and restricts message passing to past data to avoid leakage ([arXiv 2205.13084](https://arxiv.org/abs/2205.13084)).
- Capital One reports a graph formulation (GraphSAGE on session graphs) beating its production XGBoost for account takeover, attributing gains mostly to the graph framing ([Capital One](https://www.capitalone.com/tech/publications/spatio-temporal-directed-graph-learning-for-fraud-detection)).
- Recent work reports real‑time dynamic graph learning on industrial fraud within latency limits ([Frontiers in AI 2026](https://public-pages-files-2025.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2026.1774013/xml)).
- Vendor claims of 15–25 % fewer false positives ([Kumo](https://kumo.ai/pyg/use-cases/fraud-detection/)) are unverified.
- **Inference:** the expert skill is the *serving pattern and leakage control*, not the GNN architecture → E02 uses an ablation (tabular vs graph features vs embeddings).

## 3. Delayed labels, analyst feedback, uncertainty

- Fraud labels can arrive 1–6 months after prediction; a 2025 ECML‑PKDD paper proposes predicting model error under that delay ([Sethi et al.](https://mlanthology.org/ecmlpkdd/2025/sethi2025ecmlpkdd-proactive)).
- Investigator feedback and delayed labels should be handled separately ([Dal Pozzolo et al.](https://boracchi.faculty.polimi.it/docs/2015_04_Credit_Card_Fraud_Detection_DalPozzolo_Boracchi_Caelen_Alippi_Bontempi.pdf)); streaming active learning for fraud is established ([Carcillo et al.](https://arxiv.org/abs/1804.07481)); Feedzai reports competitive results with 1/10–1/50 of labels ([Barata et al.](https://research.feedzai.com/oshuzuxa/2022/08/Barata_ActiveLearning_KDD-MLF2021.pdf)).
- Conformal prediction for analyst routing appears only in a 2026 preprint ([Preprints.org](https://www.preprints.org/manuscript/202601.0447)); combining conformal guarantees with delayed labels is an **open gap** → E03 treats it as an experiment, not a settled method.

## 4. Adversarial robustness

- Tabular threat models must respect feature constraints and attacker cost/utility; gains differ by transaction value ([Kireev et al., NDSS 2023](https://www.ndss-symposium.org/wp-content/uploads/2023-924-paper.pdf)).
- Early work showed high attack success on imbalanced fraud data ([Cartella et al.](https://arxiv.org/abs/2101.08030)); a recent benchmark argues conclusions depend on evaluation protocol ([FraudBench](https://arxiv.org/abs/2608.24551), preprint).
- **Gap:** this search did not cover defenses in depth → E04 requires learners to evaluate ≥ 2 defenses empirically.

## 5. Advanced credit risk

- Survival analysis is the dominant recommendation for lifetime PD under IFRS 9 ([arXiv 2507.15441](https://arxiv.org/abs/2507.15441)); macro variables enter as hazard covariates ([Edinburgh CRC](https://crc.business-school.ed.ac.uk/sites/crc/files/2021-10/Assessment-of-Survival-Analysis-Approaches-to-IFRS9-Implementation-for-Retail-Portfolios-Paper.docx); [Cox + macro](https://journals.ue.wroc.pl/eada/article/view/1320)); multiple scenarios are required ([MathWorks](https://www.mathworks.com/help/risk/overview-of-lifetime-probability-of-default.html)).
- EBMs perform on par with or better than XGBoost while being transparent in credit scoring ([Schwartz et al.](https://arxiv.org/abs/2509.11389), preprint); monotonic XGBoost outperformed a scorecard by 7 % KS in an AAAI 2020 paper (reported via search; [AAAI](https://aaai.org/?p=52685)).
- **Gap:** no regulator‑endorsed ML approach for scenario weighting found → E05 keeps the ECL engine transparent and documents assumptions.

## 6. Causal decisioning

- Credit‑limit uplift with continuous treatments (Multi‑Treatment DML) ([arXiv 2508.02183](https://arxiv.org/abs/2508.02183), preprint); causal learning for limit adjustment validated with influence functions ([Edinburgh CRC](https://www.crc.business-school.ed.ac.uk/sites/crc/files/2024-01/Causal-Learning-for-Credit-Limit-Adjustment-in-Revolving-Lending-Under-Adversarial-Goals.pdf)).
- Dedicated bank OPE studies were **not found**; E06 uses a simulator where ground truth is known.

## 7. Serving performance

- American Express serves fraud models with Triton + TensorRT under a ~2 ms latency requirement ([NVIDIA](https://www.nvidia.com/en-us/case-studies/american-express-prevents-fraud-and-foils-cybercrime-with-nvidia-ai-solutions/), vendor); NVIDIA documents XGBoost fraud on Triton ([NVIDIA docs](https://docs.nvidia.com/launchpad/data-science/fraud-detection/latest/fraud-detection-overview.html)); Oracle describes GPU XGBoost + Triton ([Oracle](https://blogs.oracle.com/cloud-infrastructure/post/nvidia-triton-oci-enhances-fraud-detection)).
- **Inference:** GPU is justified only with batching/high throughput; E07 makes learners benchmark CPU vs Triton.

## 8. Privacy‑enhancing ML

- FL can approach centralized fraud performance; DP‑SGD at ε < 10 with moderate degradation ([arXiv 2603.13617](https://arxiv.org/abs/2603.13617), preprint). Bank consortium FL for mule detection (RBC Borealis/Vector) uses horizontal FL ([RBC Borealis](https://rbcborealis.com/?p=18429)). Adoption is held back by privacy, competition, and trust concerns ([UK Finance](https://www.ukfinance.org.uk/news-and-insight/blog/how-federated-learning-strengthens-fraud-detection-in-2025)).

## 9. Governance and regulation

- OJK launched *Tata Kelola Kecerdasan Artifisial Perbankan Indonesia* on 29 April 2025 as a minimum reference, drawing on the EU AI Act and BCBS, and urged banks to form an AI committee ([OJK](https://ojk.go.id/id/Publikasi/Roadmap-dan-Pedoman/Perbankan/Pages/Tata-Kelola-Kecerdasan-Artifisial-Perbankan-Indonesia.aspx); [OJK press release](https://ojk.go.id/id/berita-dan-kegiatan/siaran-pers/Pages/Peluncuran-Tata-Kelola-Kecerdasan-Artifisial-Perbankan-Indonesia.aspx); [Antara](https://www.antaranews.com/berita/4802981/ojk-bank-perlu-bentuk-komite-ai-untuk-awasi-tata-kelola)). OJK was still refining the policy in Nov 2025 ([Kontan](https://keuangan.kontan.co.id/news/ojk-matangkan-kebijakan-tata-kelola-ai-perbankan-untuk-perkuat-transformasi-digital)) and later described a scale‑ and risk‑based approach ([Bisnis.com](https://finansial.bisnis.com/read/20261015/90/2013049/ojk-beri-ruang-perbankan-berinovasi-pada-ai-sesuai-skala-dan-risiko)).
- EU AI Act: credit scoring of natural persons is high‑risk (Annex III 5(b)). Sources conflict on the deadline: 2 Aug 2026 originally; several 2026 reports describe a Digital Omnibus agreement moving it to 2 Dec 2027 ([Openlayer](https://www.openlayer.com/blog/eu-ai-act-financial-services); [Lewis Silkin](https://www.lewissilkin.com/insights/2026/05/29/eu-ai-act-guidance-on-classifying-high-risk-ai-systems-102mx9l)). **Unverified — check EUR‑Lex.** Relevance for an Indonesian bank: benchmark only, since OJK's guide references it.

## 10. LLMs in fraud operations

- Bank pilots show most value in alert‑to‑case summaries and evidence gathering, with a gap between vendor promises and production ([American Banker](https://www.americanbanker.com/news/how-banks-can-safely-use-ai-in-the-cyber-operations-center)).
- Guardrails are mostly architectural: no direct SQL, safe tool wrappers, deterministic rules separate from LLM summarization ([Global Economics Group](https://www.globaleconomicsgroup.com/wp-content/uploads/2026/01/Agentic-AI-development-for-risk-based-workflows-in-banking.pdf)); keep thresholds and hard policy in rules ([Taktile](https://taktile.com/articles/ai-agents-fraud-prevention-investigation), vendor).
- **Gap:** little public material on eval methods for these copilots → E10 makes the eval suite the core deliverable.

## Key takeaways

- Expert = platform design + rigor + governance evidence; each expert module therefore requires trade‑off analysis and confidence intervals, not just working code.
- Several promising areas (conformal + delayed labels, bank OPE, LLM copilot evals) lack settled public evidence; the track frames them as controlled experiments with simulators.
- Regulatory dates are moving (EU AI Act) and Indonesian guidance is evolving (OJK 2025); E09 builds horizon scanning and `[ASUMSI]` labeling into the deliverable.

## Methodology

12 web searches (2026‑11‑14) across: GNN fraud in production; streaming feature stores; EU AI Act credit scoring; OJK AI governance; IFRS 9 lifetime PD; federated learning for fraud; delayed labels / active learning / conformal; Triton serving; adversarial tabular attacks; causal credit‑limit modeling; LLM agents in fraud ops; EBM/monotonic credit models. Preference given to peer‑reviewed papers and official sources; vendor and preprint items are labeled. Sources were not all read in full; claims rely on abstracts and search summaries where noted.
