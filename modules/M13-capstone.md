# Module 13: Integrated Capstone

- **Image source:** [Gambar 1, 2] (full lifecycle "train, deploy, monitor, retrain"); integration of all modules; governance package `[TAMBAHAN]`
- **Duration:** 13 hours | **Level:** Advanced
- **Learning outcomes:**
  1. Integrate M01–M12 into one platform runnable with `make up && make demo`.
  2. Demonstrate the full loop: data → train → track → register → serve → monitor → drift → retrain → promote/rollback.
  3. Deliver a governance package (model cards, validation report, runbooks) a reviewer can audit without asking questions.
  4. Present the platform in a 15‑minute demo with live drift injection.
- **Prerequisites:** M01–M12
- **Core concepts:** See [`capstone/README.md`](../capstone/README.md) for architecture, milestones, and rubric.
- **Task Project:**
  - **Task A (Fraud Detection):** Real‑time fraud scoring service with shadow/canary, Prometheus metrics, drift alert → retrain DAG → gated promotion. **Input:** synthetic stream (`scripts/replay_stream.py`) with drift + fraud ring injected mid‑demo. **Output:** live dashboard and promotion/rollback evidence.
  - **Task B (Credit Scoring):** Application‑time API + monthly batch scoring, stability report, challenger memo, validation report, PSAK 71 PD hand‑off table. **Input:** synthetic applications over 24 monthly vintages. **Output:** batch tables, reports, governance docs.
- **Deliverables:** listed in [`capstone/README.md`](../capstone/README.md#deliverables).
- **Acceptance criteria / Definition of Done:** see [`capstone/README.md`](../capstone/README.md#definition-of-done).
- **Tools & libraries:** everything from M01–M12.
- **Common pitfalls:**
  - Demo depends on manual steps → script everything in `Makefile`.
  - Running out of time on Kubernetes — it is optional; docker compose is sufficient.
  - Governance docs out of sync with deployed model versions.
- **Stretch goal:** Deploy the full stack on a `kind` cluster with Helm and Argo Rollouts.
- **Reading & reference repos:** [docs/05-reading-list.md#m13](../docs/05-reading-list.md#m13) (⭐ = read first)
