# E06: Causal Decisioning & Off‑Policy Evaluation

- **Image source:** extends [Gambar 12] (champion/challenger) with causal evaluation `[TAMBAHAN]`
- **Duration:** 6 hours | **Level:** Expert
- **Learning outcomes:**
  1. Explain why a PD model alone cannot choose credit limits (it predicts outcomes under the *historical* policy).
  2. Estimate heterogeneous treatment effects of a credit limit increase on spend and default with double machine learning / meta‑learners and evaluate with Qini/AUUC.
  3. Evaluate a new fraud threshold or rule set offline with off‑policy estimators (IPS, doubly robust) using logged decisions and propensities.
  4. Design an experiment (holdout or randomized exploration) that makes future causal evaluation possible.
- **Prerequisites:** E05, E03
- **Core concepts:** potential outcomes, confounding by the existing policy; DML, T/X/DR‑learners; uplift metrics; logging propensities; IPS / SNIPS / DR estimators and their variance; exploration as a governance‑approved design choice; fairness of treatment allocation.
- **Task Project:**
  - **Task A (Fraud Detection):** Log the current policy's decisions with propensities (add 2 % randomized "step‑up auth instead of decline" exploration in the simulator). Evaluate a candidate threshold/rule set with IPS and DR; compare with the true simulated outcome. **Output:** `reports/e06_fraud_ope.md` with estimate, CI, and bias vs ground truth.
  - **Task B (Credit Scoring):** Simulate a credit‑limit‑increase campaign with confounded assignment plus a 10 % random holdout. Estimate CATE on profit (interest revenue − expected loss) with EconML; build a policy "increase only if CATE > 0 and PD < cap"; validate with the holdout. **Output:** `reports/e06_credit_uplift.md` with Qini curve and policy value vs current policy.
- **Deliverables:** `src/causal/uplift.py`, `src/causal/ope.py`, simulator extension `data/synth/policy_sim.py`, experiment design doc `docs/design/exploration-policy.md`.
- **Acceptance criteria / Definition of Done:**
  - [ ] Naive (correlational) estimate vs causal estimate shown side by side with the simulator's true effect.
  - [ ] OPE estimate within its own 95 % CI of the true policy value in the simulator.
  - [ ] Qini/AUUC reported on the random holdout only.
  - [ ] Exploration design states the cost cap, eligible population, and approval owner.
  - [ ] Treatment allocation fairness: limit‑increase rate by protected group reported.
- **Tools & libraries:** EconML, DoWhy, CausalML, Open Bandit Pipeline (OBP), scikit‑learn
- **Common pitfalls:**
  - No logged propensities → OPE impossible later; log them now.
  - Evaluating uplift on observational data without overlap checks.
  - Optimizing spend uplift and ignoring default uplift.
- **Stretch goal:** Contextual bandit for step‑up authentication choice with a safety constraint on fraud loss.
- **Reading:** [reading-list.md#e06](reading-list.md#e06)
