# Module 5: Domain‑Specific Model Evaluation

- **Image source:** [Gambar 5]; PR‑AUC, recall@precision, KS, Gini, cost‑sensitive metrics, calibration `[TAMBAHAN]`
- **Duration:** 8 hours | **Level:** Intermediate
- **Learning outcomes:**
  1. Compute and explain why accuracy is misleading at a 0.5 % fraud rate, using PR‑AUC and recall@precision instead.
  2. Select a fraud decision threshold that minimizes expected cost from the M01 cost matrix and a manual‑review capacity constraint.
  3. Compute AUC, Gini (= 2·AUC − 1), KS, and a calibration curve / Brier score for the credit model on an out‑of‑time sample.
  4. Produce an evaluation report with bootstrap 95 % confidence intervals for each primary metric.
  5. Write an automated evaluation gate that returns pass/fail against declared thresholds.
- **Prerequisites:** M03
- **Core concepts:**
  - Training flow features → train → validate → evaluate on held‑out test set; accuracy, precision/recall, F1, AUC; traps: leakage, overfitting, imbalanced classes; cross‑validation [Gambar 5].
  - "A great test score with leaked data is a lie — isolate your test set." [Gambar 5]
  - `[TAMBAHAN]` PR‑AUC; recall at fixed precision; alert rate vs analyst capacity; expected cost; KS & Gini; rank‑ordering by score decile; calibration (Platt / isotonic) and PD calibration to long‑run default rate; time‑series cross‑validation.
- **Task Project:**
  - **Task A (Fraud Detection):** `src/evaluate/fraud.py` produces PR curve, recall@precision ∈ {0.8, 0.9}, cost curve over thresholds, alerts/day at chosen threshold. Compare class weighting vs undersampling vs focal‑style `scale_pos_weight`. **Input:** best M03 fraud runs + test split. **Output:** `reports/fraud_eval.md`, `artifacts/fraud/threshold.json`.
  - **Task B (Credit Scoring):** `src/evaluate/credit.py` produces AUC/Gini/KS on train, valid, OOT; decile table (bad rate per score band, monotonic check); calibration plot and Brier score; score‑to‑PD mapping. **Input:** best M03 credit runs + OOT split. **Output:** `reports/credit_eval.md`, `artifacts/credit/score_bands.csv`.
- **Deliverables:**
  - `src/evaluate/{fraud,credit}.py`, `src/evaluate/gate.py`
  - `configs/gates.yaml` with numeric thresholds
  - Two evaluation reports logged as MLflow artifacts
- **Acceptance criteria / Definition of Done:**
  - [ ] Fraud report shows accuracy of an all‑zero baseline next to the model's PR‑AUC (demonstrates accuracy trap).
  - [ ] Chosen fraud threshold yields ≤ the review capacity configured in `gates.yaml` (e.g., 200 alerts/day) on the test set.
  - [ ] Credit decile table bad rate is monotonic across ≥ 9 of 10 deciles (check coded).
  - [ ] OOT Gini drop vs train ≤ 10 percentage points, or the report explains why.
  - [ ] Every primary metric reported with bootstrap 95 % CI (n ≥ 500 resamples).
  - [ ] `python -m src.evaluate.gate --run-id <id>` exits 0 for passing runs and 1 for failing runs (both cases tested).
- **Tools & libraries:** scikit‑learn (`precision_recall_curve`, `roc_auc_score`, `CalibratedClassifierCV`, `TimeSeriesSplit`), scipy (`ks_2samp`), optbinning or scorecardpy, matplotlib, MLflow
- **Common pitfalls:**
  - Reporting ROC‑AUC only for fraud (looks great at extreme imbalance).
  - Tuning the threshold on the test set.
  - Evaluating credit on loans without a full performance window (immature bads).
  - Survivorship / reject bias: metrics on approved‑only population overstate performance on through‑the‑door applicants.
  - Using SMOTE before the split → synthetic leakage.
- **Stretch goal:** Implement a simple reject‑inference method (parcelling or fuzzy augmentation) and compare OOT KS with and without it.
- **Reading & reference repos:** [docs/05-reading-list.md#m05](../docs/05-reading-list.md#m05) (⭐ = read first)
