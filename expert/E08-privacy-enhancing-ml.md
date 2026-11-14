# E08: Privacy‑Enhancing ML — Federated Learning, Differential Privacy, Synthetic Data

- **Image source:** `[TAMBAHAN]` (extends M12)
- **Duration:** 6 hours | **Level:** Expert
- **Learning outcomes:**
  1. Simulate a cross‑silo consortium of 3–5 banks and train a horizontal federated fraud model; compare with local‑only and centralized baselines.
  2. Add DP‑SGD and report the privacy–utility trade‑off at several ε values.
  3. Generate a synthetic credit dataset and evaluate fidelity, utility (train‑synthetic‑test‑real), and privacy (membership/nearest‑neighbor risk).
  4. Write a data‑sharing assessment that maps each technique to UU PDP principles and residual risks.
- **Prerequisites:** E07, M12
- **Core concepts:** horizontal vs vertical FL; non‑IID data across banks; secure aggregation; DP‑SGD, ε/δ accounting; attacks on FL (gradient inversion, poisoning); synthetic data is not automatically anonymous; consortium governance (who owns the global model).
- **Task Project:**
  - **Task A (Fraud Detection):** Split synthetic fraud data into 4 "banks" with different fraud mixes (non‑IID). Train an MLP (or federated XGBoost) with Flower or NVIDIA FLARE. Compare PR‑AUC: local‑only per bank, federated, centralized; then DP at ε ∈ {1, 3, 8}. **Output:** `reports/e08_federated.md`.
  - **Task B (Credit Scoring):** Generate synthetic applications with SDV (CTGAN or Gaussian copula). Evaluate fidelity (column shapes, pair correlations), TSTR Gini vs train‑real‑test‑real, and distance‑to‑closest‑record privacy. **Output:** `reports/e08_synthetic_credit.md`, decision on whether the synthetic set can be shared with a vendor.
- **Deliverables:** `src/privacy/federated/`, `src/privacy/dp_train.py`, `src/privacy/synthetic.py`, `governance/data_sharing_assessment.md`.
- **Acceptance criteria / Definition of Done:**
  - [ ] Table: local vs federated vs centralized PR‑AUC per bank with CI over ≥ 3 seeds.
  - [ ] DP results list ε, δ, and accountant used for every run.
  - [ ] Synthetic data report includes fidelity, TSTR utility, and privacy metric with a pass/fail threshold set in advance.
  - [ ] No raw row from the real set appears in the synthetic set (exact‑match test).
  - [ ] Assessment maps ≥ 6 UU PDP obligations to controls and residual risk.
- **Tools & libraries:** Flower or NVIDIA FLARE, Opacus, SDV (SDMetrics), PyTorch
- **Common pitfalls:**
  - Claiming "privacy‑preserving" for FL without secure aggregation/DP.
  - IID splits that hide the real FL difficulty.
  - Sharing synthetic data generated from small segments (high re‑identification risk).
- **Stretch goal:** Vertical FL between a bank and an e‑commerce partner on shared customers (private set intersection + split learning) — design doc only.
- **Reading:** [reading-list.md#e08](reading-list.md#e08)
- **Lectures, videos, blogs & repos:** 🎥 [Federated learning (Google I/O)](https://www.youtube.com/watch?v=89BGjQYA0uE) · 🎓 [Intro to FL (DeepLearning.AI)](https://www.deeplearning.ai/short-courses/intro-to-federated-learning/) · 🎓 [Opacus tutorials](https://opacus.ai/tutorials/) — full list: [learning-resources.md#e08](learning-resources.md#e08)
