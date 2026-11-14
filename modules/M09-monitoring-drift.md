# Module 9: Monitoring — Service Health, Data Drift, Concept Drift, PSI/CSI, Performance Decay, Alerting

- **Image source:** [Gambar 1, 3, 10, 11]; CSI, scorecard stability report, delayed‑label estimation `[TAMBAHAN]`
- **Duration:** 10 hours | **Level:** Advanced
- **Learning outcomes:**
  1. Expose system and model metrics on `/metrics` and visualize them in a Grafana dashboard.
  2. Compute PSI on the score and CSI on each characteristic between a reference and a current window.
  3. Detect data drift with Evidently (KS / PSI) and generate an HTML report on a schedule.
  4. Join delayed labels to stored predictions by `request_id` and plot live performance decay by segment.
  5. Configure alert rules for p95 latency, error rate, PSI, and live recall, routed to a channel.
- **Prerequisites:** M08
- **Core concepts:**
  - Three layers: system metrics, prediction metrics, model‑quality metrics [Gambar 10].
  - System: latency p50/p95/p99, error rate, RPS, CPU/GPU, uptime; flow `/metrics` → Prometheus → Grafana → alerts [Gambar 10].
  - Model: prediction distribution, confidence, live accuracy/F1/AUC when labels arrive; `prediction_drift_psi` [Gambar 10].
  - Data/feature drift vs concept drift; PSI > 0.2 significant, KS p < 0.05; slice by user/region/device/category; alert → kick off retraining [Gambar 11].
  - "A model can pass every health check while quietly getting less accurate." [Gambar 10]
  - `[TAMBAHAN]` PSI bands 0.1/0.25 used in credit risk practice; CSI per characteristic; fraud label delay → use proxy signals (alert rate, analyst confirm rate) and NannyML CBPE for estimated performance; adversarial drift (fraudsters adapt).
- **Task Project:**
  - **Task A (Fraud Detection):** Instrument the fraud API with `prometheus_client` (histogram `model_inference_duration_seconds`, counter by decision, gauge `prediction_score_mean`). Run the synthetic generator with `--drift-start` to inject an amount/merchant shift and a new fraud ring. Daily job computes Evidently drift report and joins chargeback labels (30–90 days delayed) to compute recall@threshold by week and by `merchant_category`. **Input:** prediction log + delayed label table. **Output:** Grafana dashboard JSON, `reports/fraud_drift_<date>.html`, alert firing on the injected drift.
  - **Task B (Credit Scoring):** Monthly stability job `src/monitor/credit_stability.py`: score PSI, CSI per characteristic, approval rate, bad rate by vintage (when matured), Gini on matured vintage vs development. **Input:** `credit_scores` table + synthetic later vintages with drift. **Output:** `reports/credit_stability_<yyyymm>.md` with traffic‑light status (green < 0.1, amber 0.1–0.25, red > 0.25).
- **Deliverables:**
  - `monitoring/prometheus.yml`, `monitoring/alert_rules.yml`
  - `monitoring/grafana/dashboards/{fraud,credit}.json`
  - `src/monitor/{psi,fraud_drift,credit_stability}.py`
  - `tests/test_psi.py`
- **Acceptance criteria / Definition of Done:**
  - [ ] Grafana dashboard shows ≥ 6 panels: RPS, p95 latency, error rate, score distribution, PSI, live recall.
  - [ ] `psi()` unit test: identical distributions → PSI < 0.01; known shifted distributions → PSI within ±0.01 of a hand‑computed value.
  - [ ] Injected drift (generator `--drift-start`) causes PSI > 0.2 on `amount` and an alert in Prometheus/Alertmanager within one evaluation cycle.
  - [ ] Alert rules exist for p95 latency, error rate, PSI, and live recall (4 rules, `promtool check rules` passes).
  - [ ] Live performance table is sliced by ≥ 2 segments and reports sample sizes.
  - [ ] Credit stability report lists PSI/CSI with numeric values and status for every model characteristic.
- **Tools & libraries:** prometheus_client, Prometheus, Alertmanager, Grafana, Evidently, NannyML, scipy, PostgreSQL [Gambar 10, 11]
- **Common pitfalls:**
  - Only checking accuracy periodically — too late; monitor continuously [Gambar 11].
  - No alerts — "silence is not signal" [Gambar 2].
  - Computing fraud recall on immature weeks → false "improvement".
  - PSI with bins defined on the current window instead of the reference window.
  - Alert fatigue from per‑feature KS tests on large samples (p‑values always tiny) — use effect size (PSI/Wasserstein) thresholds.
- **Stretch goal:** Implement NannyML CBPE to estimate fraud model precision before labels arrive and compare it to realized precision once labels mature.
- **Reading & reference repos:** [docs/05-reading-list.md#m09](../docs/05-reading-list.md#m09) (⭐ = read first)
- **Lectures, videos, blogs & repos:** 🎓 [Evidently ML observability course](https://learn.evidentlyai.com/) · 🎥 [Prometheus explained](https://www.youtube.com/watch?v=h4Sl21AKiDg) · 💻 [ml_observability_course](https://github.com/evidentlyai/ml_observability_course) — full list: [07-learning-resources.md#m09](../docs/07-learning-resources.md#m09)
