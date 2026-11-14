# E04: Adversarial Robustness & Red‑Teaming Fraud Models

- **Image source:** `[TAMBAHAN]` (extends M12 threat model)
- **Duration:** 6 hours | **Level:** Expert
- **Learning outcomes:**
  1. Define a realistic attacker model for transaction fraud: which features the attacker controls, at what cost, and with what query access.
  2. Run a constrained, cost‑aware evasion attack against the fraud model and report attack success rate weighted by fraud amount.
  3. Apply and evaluate at least two defenses (feature hardening, adversarial training, ensemble with rules, rate limiting) with their cost to clean performance.
  4. Detect probing behavior and model‑extraction attempts on the scoring API.
- **Prerequisites:** E02, M12
- **Core concepts:** tabular attacks differ from image attacks — constraints (immutable fields, valid categories, cross‑feature rules) and attacker *cost/utility* matter (Kireev et al., NDSS 2023); attack success on high‑value transactions matters more; robustness‑accuracy trade‑off; adversarial drift (fraudsters adapt after deployment); model extraction via prediction APIs; MITRE ATLAS tactics.
- **Task Project:**
  - **Task A (Fraud Detection):** Mutable features = amount (split into smaller amounts), merchant category (within plausible set), time of day, device (new device costs more). Implement a greedy cost‑bounded search attack; report success rate and "fraud value evaded" at budgets. Defenses: (1) features attackers cannot cheaply change (graph/velocity from E01/E02), (2) adversarial training, (3) score coarsening + rate limiting. **Output:** `reports/e04_redteam.md` with attack/defense matrix.
  - **Task B (Credit Scoring):** "Gaming" analysis: which applicant‑controlled inputs (declared income, employment length) can flip a decline to approve with minimal change? Quantify, then propose verification controls (income verification, bureau cross‑check) and monotonic constraints that limit gaming. **Output:** `reports/e04_credit_gaming.md`.
- **Deliverables:** `src/redteam/attack.py`, `src/redteam/defenses.py`, `src/api/abuse_detection.py` (query‑pattern detector), threat model update.
- **Acceptance criteria / Definition of Done:**
  - [ ] Attacker model documented: controllable features, constraints, cost function, query budget.
  - [ ] All adversarial examples satisfy domain constraints (validator test passes 100 %).
  - [ ] Matrix: ≥ 2 defenses × ≥ 3 attack budgets with success rate, evaded IDR value, and clean PR‑AUC.
  - [ ] Probing detector flags a scripted extraction attempt (≥ 1 000 near‑duplicate queries) within 1 minute.
  - [ ] Credit gaming report lists top‑5 manipulable features with mitigation owner.
- **Tools & libraries:** custom constrained search, Adversarial Robustness Toolbox (ART), XGBoost, FastAPI middleware, Prometheus
- **Common pitfalls:**
  - Unconstrained L_p attacks that produce impossible transactions → meaningless robustness numbers.
  - Reporting robustness without the clean‑accuracy cost.
  - Returning raw scores/explanations to external callers (eases extraction).
- **Stretch goal:** Simulate an adaptive attacker over several retraining cycles and show adversarial drift in E03's monitoring.
- **Reading:** [reading-list.md#e04](reading-list.md#e04)
- **Lectures, videos, blogs & repos:** 🎓 [MITRE ATLAS](https://atlas.mitre.org) · 🎓 [ART docs](https://adversarial-robustness-toolbox.readthedocs.io/) — full list: [learning-resources.md#e04](learning-resources.md#e04)
