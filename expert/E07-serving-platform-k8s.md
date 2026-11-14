# E07: High‑Performance Serving & Kubernetes‑Native Platform

- **Image source:** extends [Gambar 8] (BentoML, Seldon/KServe), [Gambar 9] (Kubernetes, HPA, Helm, probes), [Gambar 12] (Argo Rollouts); platform design `[TAMBAHAN]`
- **Duration:** 8 hours | **Level:** Expert
- **Learning outcomes:**
  1. Convert the fraud GBM to ONNX (or Treelite/FIL) and serve it with NVIDIA Triton or ONNX Runtime; verify numerical equivalence.
  2. Deploy on a `kind` cluster via GitOps (Argo CD), with KServe or a Deployment + HPA, probes, resource limits, and PodDisruptionBudget.
  3. Define SLOs (availability, p99 latency) with error budgets and multi‑window burn‑rate alerts.
  4. Run a progressive canary with Argo Rollouts using a Prometheus analysis template that auto‑aborts.
  5. Produce a capacity and cost model (replicas vs RPS vs p99).
- **Prerequisites:** E01, M08, M10
- **Core concepts:** model compilation (ONNX, Treelite/FIL, Hummingbird); dynamic batching vs latency; CPU vs GPU economics (GPU only when batching/throughput justifies it); GitOps; SLO/SLI/error budget; burn‑rate alerting; tail latency; graceful shutdown.
- **Task Project:**
  - **Task A (Fraud Detection):** Target p99 ≤ 20 ms model time at 1 000 RPS. Benchmark sklearn/XGBoost native vs ONNX Runtime vs Triton (FIL backend). Deploy best option via Argo CD; canary 5 → 25 → 100 % with automatic abort on error rate > 0.5 % or p99 regression > 10 %. **Output:** `reports/e07_serving_benchmark.md`, `deploy/` manifests, rollout recording.
  - **Task B (Credit Scoring):** Batch scoring of 5 M accounts as a Kubernetes Job (or Argo Workflow) with parallelism; target ≤ 15 min; idempotent re‑runs. Online credit API with SLO 99.9 % availability. **Output:** job manifests, run report with throughput and cost per million scores.
- **Deliverables:** `deploy/helm/fraud-api/`, `deploy/argocd/`, `deploy/rollouts/analysis-template.yaml`, `monitoring/slo_rules.yml`, `src/serving/export_onnx.py`, `tests/test_onnx_equivalence.py`.
- **Acceptance criteria / Definition of Done:**
  - [ ] ONNX vs native predictions: max abs difference ≤ 1e‑5 on 100 000 rows.
  - [ ] Benchmark table: 3 runtimes × (p50, p99, max RPS, CPU/memory) on fixed hardware.
  - [ ] All cluster state reproducible from Git (`argocd app diff` clean).
  - [ ] Failed canary (injected latency) auto‑aborts without manual action (log evidence).
  - [ ] Burn‑rate alerts (fast 1 h/5 m and slow 6 h/30 m windows) defined and `promtool` tested.
  - [ ] Batch job re‑run produces identical output row count and checksum.
- **Tools & libraries:** ONNX / onnxmltools / Hummingbird, ONNX Runtime, NVIDIA Triton (FIL/ONNX backends), kind, Helm, Argo CD, Argo Rollouts, KServe (optional), Prometheus, k6 or Locust
- **Common pitfalls:**
  - Measuring latency without feature lookup and network → unrealistic p99.
  - GPU serving for small tree models with no batching → higher cost, no gain.
  - HPA on CPU only while the bottleneck is feature store latency.
  - Manual `kubectl apply` drifting from Git.
- **Stretch goal:** Multi‑model serving (fraud champion + challenger + credit) in one Triton instance with per‑model metrics.
- **Reading:** [reading-list.md#e07](reading-list.md#e07)
