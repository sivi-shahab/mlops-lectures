# Module 12: Security & Privacy (PII Masking, Access Control, UU PDP)

- **Image source:** [Gambar 9] (no secrets in images, non‑root user, pinned versions); PII, RBAC, UU PDP, adversarial abuse `[TAMBAHAN]`
- **Duration:** 4 hours | **Level:** Intermediate
- **Learning outcomes:**
  1. Classify every column in both datasets as direct identifier, quasi‑identifier, sensitive, or non‑personal.
  2. Tokenize/mask direct identifiers before data enters the training pipeline with keyed hashing.
  3. Configure least‑privilege roles in PostgreSQL and require API keys/JWT on the scoring APIs.
  4. Scan images and dependencies for vulnerabilities and secrets in CI.
  5. Add rate limiting and input sanity checks against model probing on the fraud API.
- **Prerequisites:** M08
- **Core concepts:**
  - Pitfall: shipping secrets in images; best practice: run as non‑root, pin versions [Gambar 9].
  - `[TAMBAHAN]` UU PDP (UU No. 27/2022): lawful basis, purpose limitation, data minimization, retention, data subject rights, breach notification within 3×24 hours; PCI DSS for card data (PAN never stored in clear); HMAC‑SHA256 tokenization with key in a secret manager; RBAC; audit logging; model extraction/evasion risk.
- **Task Project:**
  - **Task A (Fraud Detection):** `src/privacy/tokenize.py` replaces `card_number`, `customer_name`, `phone` with HMAC tokens (key from env/secret, never in repo). Add API key auth + rate limit (e.g., 100 req/s per client) to fraud API; never return raw feature values. **Input:** synthetic raw transactions with fake PII. **Output:** tokenized dataset, updated API, security test results.
  - **Task B (Credit Scoring):** Data classification sheet for credit data; PostgreSQL roles `ds_reader` (no PII columns via view), `api_writer`, `auditor` (read audit tables only); retention job deleting application raw PII after the configured period. **Input:** synthetic credit data with fake NIK/name. **Output:** `governance/data_classification.csv`, `sql/roles.sql`, retention job.
- **Deliverables:**
  - `src/privacy/tokenize.py`, `tests/test_tokenize.py`
  - `sql/roles.sql`, `governance/data_classification.csv`
  - `.github/workflows/security.yml` (Trivy image scan, gitleaks, pip‑audit)
  - `docs/security/threat-model.md` (STRIDE‑lite for the scoring APIs)
- **Acceptance criteria / Definition of Done:**
  - [ ] No column in `data/processed/**` matches regex for 16‑digit PAN or 16‑digit NIK (test scans all Parquet files).
  - [ ] Same input + same key → same token; different key → different token (test).
  - [ ] `ds_reader` role gets `permission denied` on raw PII table (SQL test).
  - [ ] Unauthenticated `/predict` returns 401; > rate limit returns 429 (API tests).
  - [ ] `security.yml` fails on a HIGH/CRITICAL CVE or a detected secret (demonstrated once).
  - [ ] Threat model lists ≥ 6 threats with mitigations and owners.
- **Tools & libraries:** Python `hmac`/`hashlib`, PostgreSQL roles & views, FastAPI dependencies, slowapi, Trivy, gitleaks, pip‑audit, Docker secrets / `.env` (local only)
- **Common pitfalls:**
  - Plain SHA‑256 of NIK/phone without a key → reversible by brute force.
  - Logging full request bodies (PII) in API logs.
  - `.env` committed to Git.
  - Returning detailed scores and feature contributions to external clients → enables model probing by fraudsters.
- **Stretch goal:** Add differential‑privacy‑style noise or k‑anonymity check (k ≥ 5 on quasi‑identifiers) to an analytics extract shared with business users.
