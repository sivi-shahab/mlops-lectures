# Module 10: Retraining Strategy, Champion/Challenger, Shadow & Canary Deployment, Rollback

- **Image source:** [Gambar 12]; regulatory re‑approval trigger for credit `[TAMBAHAN]`
- **Duration:** 6 hours | **Level:** Advanced
- **Learning outcomes:**
  1. Implement scheduled, drift‑based, and performance‑based retraining triggers.
  2. Run a challenger in shadow mode and compare it to the champion on identical traffic.
  3. Execute a canary release (10 % traffic) with automatic promotion criteria.
  4. Perform and time a rollback to the previous champion.
- **Prerequisites:** M04, M08, M09
- **Core concepts:**
  - Loop: drift/decay detected → retrain → evaluate vs current → register → deploy [Gambar 12].
  - Triggers: scheduled (weekly), drift‑based, performance‑based [Gambar 12].
  - Champion/challenger + shadow or canary; new model must beat the live one before full traffic; "never auto‑promote a retrained model — prove it beats the champion first" [Gambar 12].
  - Rollback via registry or `kubectl`/`helm rollback`; "don't forget to rollback traffic filters" [Gambar 12].
  - `[TAMBAHAN]` Fraud: frequent retrain (weekly) with human approval of promotion. Credit: retrain is a *model change* that requires validation and governance approval; recalibration vs redevelopment decision.
- **Task Project:**
  - **Task A (Fraud Detection):** Airflow DAG `dags/fraud_retrain.py` triggered by the M09 alert (via `scripts/trigger_retrain.py`) or weekly. Challenger registered with alias `challenger`; API runs it in shadow (score logged, not used) for N requests; comparison job on matured labels; canary 10 % via header/hash routing; promotion requires recall@P0.9 ≥ champion + 0.01 and p95 latency ≤ champion + 5 ms. **Input:** drifted synthetic data. **Output:** shadow comparison report, promotion decision record, rollback drill log.
  - **Task B (Credit Scoring):** Quarterly challenger build; side‑by‑side on the latest matured vintage; swap‑set analysis (who is approved by one model and declined by the other) with bad rates; decision memo recommending recalibrate / redevelop / keep. **Input:** later vintages from generator. **Output:** `reports/credit_challenger_<yyyyq>.md`, swap‑set table.
- **Deliverables:**
  - `dags/fraud_retrain.py`
  - Shadow/canary routing in `src/api/fraud_app.py` (`ROUTING_MODE=shadow|canary|champion`)
  - `src/registry/promote.py --rollback`
  - `docs/runbooks/rollback.md`
  - `reports/m10_*`
- **Acceptance criteria / Definition of Done:**
  - [ ] Shadow mode: 100 % of requests produce both champion and challenger scores in the log; response uses champion only (asserted in API test).
  - [ ] Canary routing sends 10 % ± 1 % of 10 000 test requests to the challenger, deterministic per `card_id`.
  - [ ] Promotion script refuses promotion when criteria are not met (tested).
  - [ ] Rollback drill: alias `champion` reverted and API serving old version in ≤ 5 minutes (timestamps in `reports/m10_rollback.md`).
  - [ ] Credit swap‑set table shows counts and bad rates for all 4 quadrants.
  - [ ] Every promotion/rollback writes an audit record (who, when, from_version, to_version, reason).
- **Tools & libraries:** Airflow, MLflow Registry aliases, FastAPI, PostgreSQL; Argo Rollouts / Helm (stretch) [Gambar 12]
- **Common pitfalls:**
  - Auto‑promoting on validation metrics without live evidence.
  - Shadow comparisons on immature fraud labels.
  - Canary split by request (not entity) → the same card scored by both models inconsistently.
  - Forgetting to revert traffic filters/rules when rolling back [Gambar 12].
- **Stretch goal:** Do the canary with Argo Rollouts on `kind` using an analysis template that queries Prometheus for error rate.
- **Reading & reference repos:** [docs/05-reading-list.md#m10](../docs/05-reading-list.md#m10) (⭐ = read first)
