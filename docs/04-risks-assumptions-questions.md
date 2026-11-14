# Risks, Assumptions & Clarifying Questions

## Assumptions `[ASUMSI]`

| # | Assumption | Impact if wrong |
|---|------------|-----------------|
| A1 | Level = intermediate (Python, SQL, scikit‑learn, Docker basics) | Beginners need +20–30 h for Docker/SQL/Git warm‑up; advanced learners can drop M03 to 3 h and add Kubernetes |
| A2 | 12 weeks × 8 h = 96 h | All hour allocations and the schedule scale with this |
| A3 | Image order = file modification time; images 3–12 are the "10 modules" | Only labels "Gambar n" change, not content |
| A4 | Local laptop (8 cores, 16 GB) with Docker; no cloud account | Cloud options (SageMaker/Vertex in [Gambar 7]) not exercised |
| A5 | Synthetic data is the default; public datasets are secondary | Real‑world messiness is under‑represented |
| A6 | Kubernetes, KServe, Helm, Argo Rollouts [Gambar 7, 9, 12] are stretch goals, not core | Learners who need K8s for work must add ~8 h |
| A7 | Regulation references (OJK, PSAK 71, Basel III, UU PDP) are framed at concept level; exact POJK/SEOJK clause numbers must be confirmed by the bank's Compliance/MRM team | Citing wrong clauses in a validation report |
| A8 | MLflow ≥ 2.9 aliases are used instead of the deprecated stages shown in [Gambar 7, 12] | If the bank runs an older MLflow, use stages as shown in the images |

## Risks

| Risk | Likelihood | Mitigation |
|------|------------|------------|
| Scope too large for 96 h (two use cases in every module) | High | Every task has a minimal path; stretch goals are optional; capstone reuses module outputs |
| Docker stack too heavy for learner laptops (Airflow + MLflow + Grafana) | Medium | Airflow is behind a compose profile; can be replaced by Prefect locally |
| Synthetic data too easy → unrealistic metrics | Medium | Tune generator noise; validate on IEEE‑CIS / Home Credit in M05 |
| Regulatory content becomes outdated | Medium | Regulatory mapping is a living doc with "last verified" date |
| Image content reflects a churn/generic example, not banking | Low | Banking specifics are explicitly labeled `[TAMBAHAN]` |
| Use of real customer data in exercises | Low / severe | Repository allows only synthetic or public data; PII tests in M12 |

## Clarifying questions (max 3)

1. **Level and time budget:** Is the learner profile really intermediate, and is 12 weeks × 8 h/week correct? (This drives all hour allocations.)
2. **Target deployment platform:** Should production‑like deployment be docker compose only, or must Kubernetes (or a specific cloud/on‑prem platform used by the bank) be a core module rather than a stretch goal?
3. **Regulatory depth:** Should M11 produce documents aligned to the bank's actual internal MRM policy and specific POJK/SEOJK clauses (needs input from Compliance), or is a concept‑level mapping sufficient for this learning program?
