# E01: Real‑Time Streaming Feature Platform

- **Image source:** extends [Gambar 1, 4] (feature store, train/serve consistency); streaming design `[TAMBAHAN]`
- **Duration:** 10 hours | **Level:** Expert
- **Learning outcomes:**
  1. Compute sliding‑window velocity features from a Kafka transaction stream with Apache Flink using event time and watermarks.
  2. Write each feature value to both the online store (Redis) and the offline store (Parquet/Iceberg) from one definition.
  3. Prove online/offline parity with an automated test (≥ 99.9 % of sampled values equal).
  4. Handle late, out‑of‑order, and duplicate events with explicit, tested semantics.
  5. Measure end‑to‑end freshness (event → feature available) and keep p99 ≤ 1 s.
- **Prerequisites:** M02, M08
- **Core concepts:** event time vs processing time; watermarks and allowed lateness; exactly‑once vs at‑least‑once + idempotent sinks; single‑definition features materialized to both stores (the root cause of skew is two pipelines computing "almost the same" feature); point‑in‑time joins; backfill from the offline log; Feast streaming/push sources.
- **Task Project:**
  - **Task A (Fraud Detection):** Replay `fraud_transactions.parquet` into Kafka (Redpanda locally) at 2 000 events/s with 2 % out‑of‑order and 0.5 % duplicate events. Flink job computes per‑card count/sum over 1 h/24 h, distinct devices per card in 24 h, distinct cards per device in 24 h (ring signal). Sink to Redis and Parquet. Fraud API reads features from Redis. **Output:** running pipeline, parity test, freshness dashboard.
  - **Task B (Credit Scoring):** Stream application and bureau‑inquiry events; compute "number of credit applications in last 7/30 days per NIK token" (loan‑stacking signal) and feed it to the credit API. Show that the same feature recomputed in batch for training matches. **Output:** feature + parity test + updated credit model with the new feature and its lift on OOT.
- **Deliverables:** `streaming/docker-compose.streaming.yml` (Redpanda, Flink, Redis), `streaming/jobs/velocity.py` (PyFlink) or `.sql` (Flink SQL), `tests/test_feature_parity.py`, `docs/adr/00xx-streaming-semantics.md`, Grafana panel for freshness and consumer lag.
- **Acceptance criteria / Definition of Done:**
  - [ ] Parity: for 10 000 random (entity, timestamp) pairs, online value equals offline point‑in‑time value in ≥ 99.9 % of cases; mismatches explained.
  - [ ] Duplicates do not double‑count (test with a replayed duplicate).
  - [ ] Events later than allowed lateness are routed to a side output and counted.
  - [ ] Freshness p99 ≤ 1 s and consumer lag < 5 s at 2 000 events/s for 10 minutes.
  - [ ] Killing the Flink task manager and restarting from checkpoint loses or duplicates 0 events in the sink (verified by count).
  - [ ] ADR states chosen delivery guarantee and why.
- **Tools & libraries:** Apache Kafka or Redpanda, Apache Flink (PyFlink / Flink SQL), Redis, Feast (push/stream source), Apache Iceberg (optional), Prometheus
- **Common pitfalls:**
  - Processing‑time windows → features differ between replay and live.
  - Re‑implementing the feature in pandas for training → skew.
  - Unbounded state (distinct‑count per device) without TTL → memory blow‑up.
  - Velocity features that include the current transaction at serving but not at training (or vice versa).
- **Stretch goal:** Replace Flink with a streaming database (RisingWave) or Bytewax and compare operational complexity and latency.
- **Reading:** [reading-list.md#e01](reading-list.md#e01)
