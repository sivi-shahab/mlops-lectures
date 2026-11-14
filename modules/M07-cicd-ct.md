# Module 7: CI/CD/CT for ML — Testing Data, Models, and Code

- **Image source:** [Gambar 2] ("Automate early"), [Gambar 12] (automated retrain); CI/CD/CT design and test types `[TAMBAHAN]`
- **Duration:** 6 hours | **Level:** Intermediate
- **Learning outcomes:**
  1. Build a GitHub Actions workflow that runs lint, unit tests, data validation, and a small training smoke test on every PR.
  2. Write model behavioral tests (invariance, directional expectation, minimum functionality).
  3. Add a CD job that builds and pushes the API image only when the evaluation gate passes.
  4. Define a continuous‑training (CT) trigger that starts the Airflow DAG via its REST API.
- **Prerequisites:** M04, M05, M06
- **Core concepts:**
  - "Automate early. Track always. Monitor everything." [Gambar 2]
  - Drift‑triggered retraining is automated [Gambar 12].
  - `[TAMBAHAN]` Test pyramid for ML: code unit tests → data tests → model tests → integration tests; CI (code), CD (artifact/service), CT (model refresh); gates as code; branch protection.
- **Task Project:**
  - **Task A (Fraud Detection):** Behavioral tests in `tests/model/test_fraud_behavior.py`: (1) increasing `amount` by 10× on a risky merchant must not decrease score, (2) changing `customer_name` does not change score (invariance), (3) 20 known fraud‑ring patterns are flagged. **Input:** sample of synthetic data + registered candidate model. **Output:** passing tests in CI.
  - **Task B (Credit Scoring):** Behavioral tests in `tests/model/test_credit_behavior.py`: (1) monotonic constraints — higher DTI never lowers PD, more delinquencies never lowers PD, (2) score range within [300, 850], (3) reason codes always present for declines. **Input:** sample + candidate model. **Output:** passing tests in CI.
- **Deliverables:**
  - `.github/workflows/ci.yml` (lint → unit → data → model smoke)
  - `.github/workflows/cd.yml` (build image, run gate, push to GHCR on tag)
  - `tests/{unit,data,model}/`
  - `docs/ci-cd-ct.md` diagram
- **Acceptance criteria / Definition of Done:**
  - [ ] CI completes in ≤ 10 minutes on a PR (workflow run duration visible).
  - [ ] A PR that breaks a monotonic constraint fails CI (demonstrated with a deliberately broken branch, link in `reports/m07.md`).
  - [ ] Code coverage of `src/features` and `src/evaluate` ≥ 70 % (`pytest --cov` output).
  - [ ] `cd.yml` refuses to push an image when `gate.py` exits 1.
  - [ ] Branch protection on `main` requires CI green (screenshot or `gh api` output).
  - [ ] CT trigger script `scripts/trigger_retrain.py` successfully calls Airflow REST API (`POST /api/v1/dags/{dag_id}/dagRuns`) in local compose.
- **Tools & libraries:** GitHub Actions, pytest, pytest‑cov, ruff, Great Expectations/Pandera, Docker Buildx, GHCR
- **Common pitfalls:**
  - Full training in CI → slow, flaky; use a 1 % sample smoke train.
  - Tests that depend on the MLflow server being up — mock or use a file‑based tracking URI in CI.
  - Secrets (MLflow / registry credentials) echoed in logs.
- **Stretch goal:** Add CML or a PR comment bot that posts the metric diff between the PR model and the current champion.
- **Reading & reference repos:** [docs/05-reading-list.md#m07](../docs/05-reading-list.md#m07) (⭐ = read first)
- **Lectures, videos, blogs & repos:** 🎥 [GitHub Actions CI/CD](https://www.youtube.com/watch?v=R8_veQiYBjI) · 🎓 [Actions quickstart](https://docs.github.com/en/actions/writing-workflows/quickstart) — full list: [07-learning-resources.md#m07](../docs/07-learning-resources.md#m07)
