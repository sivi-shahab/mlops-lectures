# E02: Graph ML for Fraud Rings & Entity Resolution

- **Image source:** `[TAMBAHAN]`
- **Duration:** 8 hours | **Level:** Expert
- **Learning outcomes:**
  1. Build a heterogeneous transaction graph (card, device, merchant, NIK token, phone token) with time‑respecting edges.
  2. Resolve duplicate customer identities with probabilistic record linkage before graph construction.
  3. Train a GNN (GraphSAGE) and compare it with tabular GBM + graph features (degree, shared‑device counts, connected‑component size) on an out‑of‑time split.
  4. Serve graph signals in production by splitting batch embedding computation from real‑time scoring.
  5. Detect and visualize fraud rings and measure how many ring members are caught before their first chargeback.
- **Prerequisites:** E01, M05
- **Core concepts:** homogeneous vs heterogeneous graphs; inductive GNNs (GraphSAGE) for unseen nodes; temporal leakage in message passing (only use edges that existed before the scored transaction); two‑stage serving (batch entity embeddings + real‑time lookup, as in eBay's BRIGHT); community detection (Louvain/Leiden, WCC) for rings; entity resolution as a precondition.
- **Task Project:**
  - **Task A (Fraud Detection):** Use the synthetic fraud ring from the generator (`device_id` shared by ≥ 5 cards after drift). Build graph with PyG; baseline = XGBoost on tabular features; variant 1 = XGBoost + handcrafted graph features; variant 2 = GraphSAGE embeddings + XGBoost. Report PR‑AUC and recall@P0.9 with bootstrap CI on OOT, and "ring members flagged before first chargeback". **Output:** `reports/e02_graph_ablation.md`, ring visualization.
  - **Task B (Credit Scoring):** First‑party fraud / loan stacking: link applications sharing phone/device/address tokens, apply Splink entity resolution, compute "network bad rate" (share of linked accounts in default as of application time) and test it as a credit feature with OOT Gini lift and PSI stability. **Output:** `reports/e02_credit_network.md`.
- **Deliverables:** `src/graph/build_graph.py`, `src/graph/train_gnn.py`, `src/graph/entity_resolution.py`, batch embedding DAG `dags/graph_embeddings.py`, online lookup in fraud API.
- **Acceptance criteria / Definition of Done:**
  - [ ] Temporal leakage test: for every training example, all edges used have timestamp < example timestamp (asserted).
  - [ ] Ablation table has 3 variants × 2 metrics with 95 % CI.
  - [ ] Graph features add ≤ 5 ms p95 to online scoring (embedding lookup, not GNN inference, on the hot path).
  - [ ] Entity resolution: precision/recall of matches measured on a labeled sample of ≥ 200 pairs.
  - [ ] Ring report lists detected communities with size, fraud share, and earliest detection time.
- **Tools & libraries:** PyTorch Geometric (or DGL), NetworkX / igraph, Neo4j Graph Data Science (optional), Splink, XGBoost
- **Common pitfalls:**
  - Building the graph on the full time range then splitting → future edges leak.
  - Transductive GNNs that cannot score new cards.
  - Running GNN message passing inside the authorization path.
  - Using network bad rate in credit without checking fairness (proxy for neighborhood/ethnicity).
- **Stretch goal:** Temporal GNN (TGN) or heterogeneous GNN (HGT) and compare with GraphSAGE.
- **Reading:** [reading-list.md#e02](reading-list.md#e02)
- **Lectures, videos, blogs & repos:** 🎓 [Stanford CS224W](https://web.stanford.edu/class/cs224w/) · 🎥 [CS224W Lecture 1.1](https://www.youtube.com/watch?v=JAB_plj2rbA) · 🎓 [Neo4j GraphAcademy](https://graphacademy.neo4j.com/) — full list: [learning-resources.md#e02](learning-resources.md#e02)
