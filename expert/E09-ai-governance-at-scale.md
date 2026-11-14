# E09: AI Governance at Scale & Policy‑as‑Code

- **Image source:** extends [Gambar 7] (approval gate: metrics threshold, bias/fairness, sign‑off; model card) `[TAMBAHAN]` for frameworks
- **Duration:** 6 hours | **Level:** Expert
- **Learning outcomes:**
  1. Map the bank's model lifecycle to OJK's *Tata Kelola Kecerdasan Artifisial Perbankan Indonesia* (April 2025), including AI committee oversight and risk‑proportionate controls.
  2. Benchmark against SR 11‑7, NIST AI RMF, and the EU AI Act (credit scoring = high‑risk, Annex III 5(b)) and record gaps.
  3. Encode governance rules as policy‑as‑code (OPA/Rego or Python) evaluated in CI before any promotion.
  4. Automate the validation evidence pack (model card, validation metrics, fairness, stability, lineage) from MLflow metadata.
  5. Design a risk‑tiering scheme and show how controls scale per tier.
- **Prerequisites:** M11 (can run in parallel with E01–E08)
- **Core concepts:** three lines of defense; AI committee; model inventory as a system of record; risk tiering (materiality × complexity × autonomy); policy‑as‑code; continuous validation; regulatory horizon scanning (dates change — e.g., reports in 2026 of an EU "Digital Omnibus" postponing Annex III obligations; always verify the Official Journal).
- **Task Project:**
  - **Task A (Fraud Detection):** Policies: no promotion without shadow evidence ≥ 14 days, recall@P0.9 ≥ champion, p99 within SLO, red‑team report (E04) ≤ 90 days old, approver ≠ developer. Implement in OPA, called by `promote.py` and CI. **Output:** passing and failing policy evaluations.
  - **Task B (Credit Scoring):** Policies: monotonicity violations = 0, DI ≥ 0.8, PSI < 0.25, independent validation sign‑off, reason codes for 100 % of declines, ECL impact assessment attached. Auto‑generate the validation evidence pack (PDF/HTML) from MLflow. **Output:** evidence pack + policy results.
- **Deliverables:** `governance/framework.md` (OJK mapping + benchmarks), `governance/risk_tiering.yaml`, `policies/*.rego` (or `src/governance/policies.py`), `src/governance/evidence_pack.py`, CI job `governance.yml`.
- **Acceptance criteria / Definition of Done:**
  - [ ] Framework maps every lifecycle stage to an OJK guideline section, an owner, and an artifact; unverified references marked `[ASUMSI]`.
  - [ ] Gap table vs SR 11‑7 / NIST AI RMF / EU AI Act with ≥ 10 rows and remediation owner.
  - [ ] Each policy has a passing and a failing unit test.
  - [ ] Promotion attempt violating any policy is blocked in CI (evidence link).
  - [ ] Evidence pack generated in ≤ 2 minutes with 0 manual inputs except sign‑off.
- **Tools & libraries:** Open Policy Agent (OPA) / conftest, MLflow API, Jinja2, WeasyPrint or Quarto, GitHub Actions
- **Common pitfalls:**
  - Governance as documents only — no enforcement point.
  - Copying EU AI Act deadlines into policy without checking the latest legal status.
  - Same controls for every model regardless of risk tier → bottlenecks.
- **Stretch goal:** A model inventory web view (read‑only) backed by PostgreSQL showing tier, status, last validation, open findings.
- **Reading:** [reading-list.md#e09](reading-list.md#e09)
- **Lectures, videos, blogs & repos:** ✍️ [OJK AI governance guide](https://ojk.go.id/id/Publikasi/Roadmap-dan-Pedoman/Perbankan/Pages/Tata-Kelola-Kecerdasan-Artifisial-Perbankan-Indonesia.aspx) · 🎓 [OPA docs](https://www.openpolicyagent.org/docs/latest/) — full list: [learning-resources.md#e09](learning-resources.md#e09)
