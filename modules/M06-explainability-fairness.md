# Module 6: Explainability & Fairness

- **Image source:** [Gambar 7] (bias/fairness checks in the approval gate), [Gambar 10] (fairness in quality checks); SHAP, reason codes, adverse action `[TAMBAHAN]`
- **Duration:** 6 hours | **Level:** Intermediate
- **Learning outcomes:**
  1. Generate global and local SHAP explanations for the fraud and credit models.
  2. Produce the top‑4 reason codes per declined credit application from scorecard points or SHAP values.
  3. Compute disparate impact ratio and equal‑opportunity difference across a protected attribute and an age band.
  4. Add a fairness check to the evaluation gate from M05 with numeric thresholds.
- **Prerequisites:** M05
- **Core concepts:**
  - Bias / fairness checks as part of the approval gate before Production [Gambar 7].
  - Feedback loop quality checks include fairness [Gambar 10].
  - `[TAMBAHAN]` SHAP (TreeExplainer), reason codes for adverse action (customer must be told the main reasons for a decline — consumer protection under POJK on consumer protection `[ASUMSI: confirm the exact POJK with Compliance]`), four‑fifths rule (DI ≥ 0.8), proxy variables (region → ethnicity), explanation latency budget for fraud.
- **Task Project:**
  - **Task A (Fraud Detection):** Add `explain=true` option to the fraud scoring function returning top‑3 SHAP features for analyst case review; measure added latency. Check alert rate parity across `region` and `device_os` segments. **Input:** M05 fraud model + test split. **Output:** `reports/fraud_explain.md` with global SHAP summary, 5 local examples, segment alert‑rate table.
  - **Task B (Credit Scoring):** `src/explain/reason_codes.py` maps each decline to ≥ 4 human‑readable reasons (Bahasa Indonesia + English text table `configs/reason_codes.csv`). Fairness report over `gender` (used **only** for testing, not as a feature) and `age_band`. **Input:** M05 credit model + OOT split. **Output:** `reports/credit_fairness.md`, `artifacts/credit/reason_codes_sample.csv`.
- **Deliverables:**
  - `src/explain/{shap_utils,reason_codes}.py`
  - `configs/reason_codes.csv`
  - Updated `configs/gates.yaml` with fairness thresholds
  - Two reports logged to MLflow
- **Acceptance criteria / Definition of Done:**
  - [ ] Every declined application in the OOT sample receives ≥ 4 non‑empty reason codes (assert in test).
  - [ ] Reason code text exists for 100 % of model features (CSV join has no nulls).
  - [ ] Disparate impact ratio and equal‑opportunity difference reported per group with group sizes.
  - [ ] Gate fails when DI < 0.8 (verified with a synthetic biased model in `tests/test_fairness_gate.py`).
  - [ ] Fraud explanation adds ≤ 20 ms p95 for a single request (benchmark result in report).
  - [ ] Protected attributes are absent from the model feature list (asserted).
- **Tools & libraries:** SHAP, fairlearn, pandas, MLflow
- **Common pitfalls:**
  - Dropping the protected attribute and assuming fairness — proxies remain.
  - Using SHAP on the WoE‑transformed space and showing customers bin codes instead of plain‑language reasons.
  - Computing fairness only on the approved population.
  - Running SHAP inline for every fraud transaction and blowing the latency budget.
- **Stretch goal:** Add a counterfactual ("what would change the decision") for 10 declines using DiCE and discuss feasibility constraints.
- **Reading & reference repos:** [docs/05-reading-list.md#m06](../docs/05-reading-list.md#m06) (⭐ = read first)
