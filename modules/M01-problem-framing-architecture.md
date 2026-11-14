# Module 1: Problem Framing & ML System Architecture (Batch vs Real‑Time)

- **Image source:** [Gambar 1, 2, 3]; business framing and regulatory context `[TAMBAHAN]`
- **Duration:** 6 hours | **Level:** Basic
- **Learning outcomes:**
  1. Draw an end‑to‑end architecture diagram that labels every component and data flow from data source to retrain loop for both use cases.
  2. Classify each use case as real‑time (online) or batch (offline) inference and justify it with a latency number and a decision cadence.
  3. Write a problem statement that defines the target label, observation window, performance window, and decision point.
  4. Quantify the cost of a false negative and a false positive in IDR for each use case.
  5. Complete the image's design checklist (reproducibility, versioning, rollback, drift monitoring) with a concrete mechanism for each item.
- **Prerequisites:** Python, SQL, scikit‑learn, Docker basics `[ASUMSI: menengah]`
- **Core concepts:**
  - Lifecycle `Data → Train → Track → Register → Serve → Monitor → Retrain` and the retrain loop [Gambar 1, 3].
  - Offline training vs online serving; real‑time API vs scheduled batch job writing CSV/table output [Gambar 3].
  - Key components: data pipeline, experiment tracker, model registry, serving layer, monitoring [Gambar 3].
  - "A notebook is an experiment; production is a system — design the system." [Gambar 3]
  - `[TAMBAHAN]` Fraud: decision within the authorization path (target p95 ≤ 100 ms model time), labels arrive via chargebacks 30–90 days later. Credit: decision at application time or monthly portfolio re‑score; default definition (e.g., 90+ DPD within 12 months) aligned with PSAK 71 staging.
- **Task Project:**
  - **Task A (Fraud Detection):** Write `docs/design/fraud-architecture.md` with (1) a Mermaid diagram of the real‑time path (transaction → feature lookup → model API → decision → case management) and the offline path (warehouse → training pipeline → registry), (2) latency budget table per hop, (3) label definition including chargeback delay, (4) cost matrix. **Input:** data dictionary of `data/synth/fraud_transactions.parquet` from `make data`. **Output:** the design doc and a one‑page `pipeline = [...]` step list in `src/common/pipeline_steps.py` mirroring [Gambar 3].
  - **Task B (Credit Scoring):** Write `docs/design/credit-architecture.md` with (1) a Mermaid diagram of the application‑time API path and the monthly batch re‑scoring path, (2) target definition (bad = 90+ DPD within 12 months), observation and performance windows, (3) list of decisions the score drives (approve/decline/limit), (4) cost of approving a bad vs declining a good applicant. **Input:** data dictionary of `data/synth/credit_applications.parquet`. **Output:** the design doc.
- **Deliverables:**
  - `docs/design/fraud-architecture.md`, `docs/design/credit-architecture.md`
  - `docs/adr/0001-online-vs-batch.md` (Architecture Decision Record)
  - `src/common/pipeline_steps.py`
- **Acceptance criteria / Definition of Done:**
  - [ ] Each diagram contains all 7 components from [Gambar 3] (data source, data pipeline, feature store, training, model registry, inference service, monitoring) plus a retrain loop edge.
  - [ ] Latency budget table sums to ≤ 150 ms end‑to‑end for fraud and lists p95 per hop.
  - [ ] Label definitions state window lengths in days/months as numbers.
  - [ ] Cost matrix has 4 numeric cells per use case.
  - [ ] Design checklist table has 4 rows (reproducibility, versioning, rollback, drift) each naming a tool and an owner.
  - [ ] ADR follows Context / Decision / Consequences format and is merged via PR.
- **Tools & libraries:** Mermaid (in Markdown), draw.io (optional), Git
- **Common pitfalls:**
  - Defining the fraud label at transaction time when it is only known after chargeback → leakage in later modules.
  - Treating credit scoring as real‑time only and forgetting the monthly portfolio re‑score needed for ECL.
  - Skipping design → rework later; no rollback plan → high risk [Gambar 3].
- **Stretch goal:** Add a capacity estimate (peak TPS, e.g., 500 TPS) and derive the number of API replicas needed at the measured per‑request latency.
