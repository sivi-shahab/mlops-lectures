# Module 11: Governance, Audit Trail, Model Risk Management & Regulatory Compliance

- **Image source:** [Gambar 7] (approval gate, sign‑off, model card, metadata), [Gambar 3, 12] (rollback strategy); MRM framework and Indonesian/international regulation `[TAMBAHAN]`
- **Duration:** 5 hours | **Level:** Advanced
- **Learning outcomes:**
  1. Create a model inventory entry with risk tier, owner, validator, and review date for both models.
  2. Write a model card and an independent validation report that follow a fixed template.
  3. Query an end‑to‑end audit trail (data version → code commit → run → registry version → deployment → predictions) for any prediction.
  4. Map each model artifact to the regulatory requirement it supports (OJK, PSAK 71, Basel III, UU PDP).
- **Prerequisites:** M06, M08, M10
- **Core concepts:**
  - Approval gate: metrics threshold, bias/fairness checks, sign‑off; model metadata: version, metrics, data lineage, model card, created by/timestamp [Gambar 7].
  - Rollback strategy as a design requirement [Gambar 3, 12].
  - `[TAMBAHAN]` Three lines of defense; model lifecycle governance (development → validation → approval → monitoring → retirement); OJK risk‑management expectations for banks' use of IT/models `[ASUMSI: map to the bank's internal MRM policy; exact POJK/SEOJK references to be confirmed by Compliance]`; PSAK 71 ECL = PD × LGD × EAD with forward‑looking adjustment and staging (SICR); Basel III IRB model requirements (if applicable); UU PDP (UU No. 27/2022) rights including objection to automated decisions.
- **Task Project:**
  - **Task A (Fraud Detection):** Model card (intended use, out‑of‑scope use, training window, metrics with CI, known limitations incl. adversarial adaptation, fairness results, monitoring plan, rollback plan). Audit trail query `sql/audit_trail.sql` that, given a `request_id`, returns model version, run id, git commit, data hash. **Input:** artifacts from M03–M10. **Output:** `docs/model-cards/fraud.md`, query + sample output.
  - **Task B (Credit Scoring):** Validation report `docs/validation/credit_validation_report.md` covering conceptual soundness, data quality, discrimination (Gini/KS), calibration, stability (PSI/CSI), benchmarking vs challenger, fairness, limitations, and findings with severity. Section on how the PD feeds PSAK 71 ECL (12‑month vs lifetime PD for Stage 1 vs Stage 2/3). **Input:** M05, M06, M09 outputs. **Output:** validation report + `governance/model_inventory.yaml`.
- **Deliverables:**
  - `governance/model_inventory.yaml`
  - `docs/model-cards/{fraud,credit}.md` (final)
  - `docs/validation/credit_validation_report.md`
  - `governance/regulatory_mapping.md`
  - `sql/audit_trail.sql`
- **Acceptance criteria / Definition of Done:**
  - [ ] Inventory entries contain all fields: id, name, owner, validator (≠ owner), tier, use, status, last_validation_date, next_review_date.
  - [ ] Model card has all 9 sections listed in Task A, none empty.
  - [ ] Validation report contains ≥ 3 findings each with severity (High/Medium/Low), owner, and due date.
  - [ ] `sql/audit_trail.sql` returns exactly one row with 6 non‑null lineage fields for a sample `request_id`.
  - [ ] Regulatory mapping table has ≥ 8 rows linking requirement → evidence artifact path; every item marked `[ASUMSI]` where the clause number is not verified.
  - [ ] Promotion to `champion` requires a sign‑off record (approver ≠ developer) — enforced by `promote.py` (tested).
- **Tools & libraries:** MLflow (tags, model version descriptions), PostgreSQL, Markdown templates, Git (signed tags optional)
- **Common pitfalls:**
  - Model card written once and never updated after retraining — link it to the registry version.
  - Validator is the same person as the developer.
  - Treating fraud models as "not credit, so no governance".
  - Citing regulations without clause references or with outdated versions — always confirm with Compliance.
- **Stretch goal:** Generate the model card automatically from MLflow metadata with a Jinja2 template in CI and fail CI if any section is empty.
