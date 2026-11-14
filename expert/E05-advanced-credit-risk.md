# E05: Advanced Credit Risk — Glass‑Box GBM, Lifetime PD, PSAK 109 (ex‑PSAK 71) ECL

- **Image source:** `[TAMBAHAN]`
- **Duration:** 10 hours | **Level:** Expert
- **Learning outcomes:**
  1. Train a monotonic‑constrained GBM and an Explainable Boosting Machine (EBM) and benchmark them against the WoE scorecard on OOT KS/Gini, calibration, and stability ("price of monotonicity").
  2. Build a lifetime PD term structure with discrete‑time survival (and a Cox benchmark) including macroeconomic covariates.
  3. Produce ECL under ≥ 3 weighted macro scenarios with Stage 1 (12‑month) vs Stage 2/3 (lifetime) logic and SICR rules.
  4. Apply and evaluate one reject‑inference method on through‑the‑door population metrics.
  5. Distinguish point‑in‑time (PIT) vs through‑the‑cycle (TTC) calibration and document which one each use (pricing, ECL, capital) needs.
- **Prerequisites:** M05, M06, M11
- **Core concepts:** monotone constraints in XGBoost/LightGBM; EBMs as GAMs with pairwise interactions; discrete‑time survival (person‑period data, hazard → cumulative PD); macro covariates shifting the hazard; IFRS 9 / PSAK 109 staging, SICR, forward‑looking scenarios and weighting; ECL = Σ PD_t × LGD × EAD × discount; reject inference (parcelling, augmentation) limits; PIT vs TTC.
- **Task Project:**
  - **Task A (Fraud Detection):** Bridge task — estimate fraud *loss* (not just probability) per segment: expected fraud loss = P(fraud) × exposure × (1 − recovery). Use it to set segment‑specific thresholds and show IDR impact vs a single threshold. **Output:** `reports/e05_fraud_expected_loss.md`.
  - **Task B (Credit Scoring):** Extend the generator with monthly performance panels (DPD by month on book) and a synthetic macro series (GDP growth, BI rate, unemployment) for 24 months. Build: (1) monotonic XGBoost + EBM vs scorecard; (2) discrete‑time survival lifetime PD with macro covariates; (3) ECL engine with base/upside/downside scenarios (weights e.g. 50/20/30 `[ASUMSI]`) and Stage 1/2 allocation via SICR (e.g. PD ratio ≥ 2× origination or 30+ DPD backstop). **Output:** `reports/e05_credit_benchmark.md`, `reports/e05_ecl.md`, ECL table by stage and scenario.
- **Deliverables:** `src/credit/glassbox.py`, `src/credit/survival_pd.py`, `src/credit/ecl.py`, `configs/macro_scenarios.yaml`, `data/synth/generate_panel.py`, tests (monotonicity, PD term structure is non‑decreasing cumulative, ECL reconciliation).
- **Acceptance criteria / Definition of Done:**
  - [ ] Benchmark table: scorecard, monotonic XGBoost, EBM × (OOT Gini with CI, KS, Brier, max PSI), plus monotonicity violations = 0 for constrained models.
  - [ ] Cumulative lifetime PD curves are non‑decreasing for every account (test).
  - [ ] Downside scenario ECL > base > upside (test), and scenario‑weighted ECL reconciles to the sum of account ECLs ±0.01 %.
  - [ ] Stage migration matrix produced between two reporting dates.
  - [ ] Reject‑inference report shows metric change and states why it is not a guaranteed fix.
  - [ ] A one‑page note explains PIT vs TTC choice per use case.
- **Tools & libraries:** XGBoost/LightGBM (`monotone_constraints`), InterpretML (EBM), lifelines / scikit‑survival, statsmodels, pandas
- **Common pitfalls:**
  - Using a 12‑month PD model directly as lifetime PD.
  - Macro variables measured with look‑ahead (using revised data not available at the time).
  - Over‑fitting macro sensitivity on 24 months with one cycle — state the limitation.
  - Monotone constraints that contradict data without business justification.
- **Stretch goal:** Compare a gradient‑boosted survival model (e.g., XGBoost AFT or random survival forest) against discrete‑time logistic hazard.
- **Reading:** [reading-list.md#e05](reading-list.md#e05)
- **Lectures, videos, blogs & repos:** 🎓 [InterpretML/EBM](https://interpret.ml/docs/) · 🎓 [lifelines](https://lifelines.readthedocs.io/en/latest/) · ✍️ [Nubank transformers](https://building.nubank.com/how-nubank-uses-transformers-to-model-financial-habits-at-scale/) — full list: [learning-resources.md#e05](learning-resources.md#e05)
