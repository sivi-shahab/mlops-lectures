# E03: Learning Under Delayed & Noisy Labels — Active Learning, Conformal Prediction, Label‑Free Performance Estimation

- **Image source:** extends [Gambar 10] (feedback loop, store predictions with request ID) and [Gambar 11] (accuracy decay once labels arrive); methods `[TAMBAHAN]`
- **Duration:** 6 hours | **Level:** Expert
- **Learning outcomes:**
  1. Separate investigator feedback (fast, biased to alerted cases) from delayed chargeback labels (slow, unbiased) and combine them in training.
  2. Implement an active‑learning query strategy under a fixed analyst budget and quantify label efficiency.
  3. Calibrate conformal prediction sets and route uncertain transactions to analysts with a guaranteed error rate on the auto‑decided set.
  4. Estimate live model performance before labels arrive (CBPE) and compare with realized performance.
- **Prerequisites:** E01, M09
- **Core concepts:** feedback vs delayed supervised samples (Dal Pozzolo et al.); selection bias from alert‑only feedback; uncertainty / expected‑cost query strategies; split conformal and Mondrian (class‑conditional) conformal for imbalance; coverage drift as a monitoring signal; confidence‑based performance estimation; prequential evaluation.
- **Task Project:**
  - **Task A (Fraud Detection):** Simulate a daily analyst budget of 100 reviews. Compare (a) top‑score alerts only, (b) top‑score + uncertainty sampling, (c) top‑score + 10 % random exploration. Train on feedback + matured labels with sample weights. Add class‑conditional conformal sets with α = 0.01 and route empty/multi‑label sets to review. Monitor empirical coverage weekly. **Output:** `reports/e03_label_strategy.md` with recall@budget per strategy over 12 simulated weeks.
  - **Task B (Credit Scoring):** Labels mature after 12 months. Use early‑delinquency proxies (30+ DPD at 3 months) and NannyML CBPE to estimate Gini of recent vintages; backtest the estimate against vintages that later matured. **Output:** `reports/e03_credit_early_warning.md` with estimated vs realized Gini per vintage.
- **Deliverables:** `src/labels/feedback_mixer.py`, `src/active/query.py`, `src/conformal/router.py`, `src/monitor/performance_estimation.py`, tests.
- **Acceptance criteria / Definition of Done:**
  - [ ] Strategy comparison over ≥ 12 simulated weeks, mean ± std across ≥ 5 seeds.
  - [ ] Conformal empirical coverage on hold‑out within ±1 pp of 1 − α for each class.
  - [ ] Share of traffic routed to analysts reported and ≤ the configured budget.
  - [ ] CBPE estimated vs realized metric: mean absolute error reported per vintage/week.
  - [ ] Unit test proves feedback labels never enter training before their `label_available_at`.
- **Tools & libraries:** MAPIE (conformal), NannyML, modAL or custom AL loop, scikit‑learn, XGBoost
- **Common pitfalls:**
  - Training only on analyst feedback → model learns the previous model's blind spots (feedback loop).
  - Marginal conformal coverage looks fine while fraud‑class coverage fails (use class‑conditional).
  - Treating "not yet charged back" as legitimate.
- **Stretch goal:** Online conformal (adaptive conformal inference) that keeps coverage under drift.
- **Reading:** [reading-list.md#e03](reading-list.md#e03)
