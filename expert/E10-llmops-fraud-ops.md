# E10: LLMOps for Fraud Operations — Investigator Copilot with Guardrails & Evals

- **Image source:** `[TAMBAHAN]`
- **Duration:** 4 hours | **Level:** Expert
- **Learning outcomes:**
  1. Build an investigator copilot that summarizes an alerted case (transactions, graph neighborhood, SHAP reasons, prior cases) without write access to core systems.
  2. Create an evaluation suite (faithfulness to case data, completeness, PII leakage, prompt‑injection resistance) and run it in CI.
  3. Enforce guardrails: tool allow‑list, least privilege, PII redaction, human approval for any customer‑facing or regulatory text.
  4. Monitor cost, latency, and quality drift of the LLM component.
- **Prerequisites:** E09, M12
- **Core concepts:** LLMs assist investigators; deterministic rules and the fraud model stay the decision makers; read‑only tools wrapping specific queries (no free SQL); grounding and citation of source records; eval‑driven development; prompt injection via merchant names/notes; data residency and UU PDP for prompts; audit logging of prompts/outputs.
- **Task Project:**
  - **Task A (Fraud Detection):** Copilot reads case JSON (from E02/E03 outputs) via 3 read‑only tools and produces a structured summary (timeline, key signals, recommended next checks). Eval set of 50 synthetic cases with reference facts; include 10 cases with injected instructions in free‑text fields. **Output:** copilot, eval report, CI job.
  - **Task B (Credit Scoring):** Draft plain‑language adverse‑action explanations from reason codes (M06) in Bahasa Indonesia; evaluate that every reason in the draft maps to a real reason code and no prohibited attribute is mentioned. Human approval required before sending. **Output:** generator + eval report.
- **Deliverables:** `src/copilot/`, `evals/cases/*.json`, `evals/run_evals.py`, `.github/workflows/llm-evals.yml`, `docs/runbooks/copilot-incident.md`.
- **Acceptance criteria / Definition of Done:**
  - [ ] Faithfulness: ≥ 95 % of factual claims in summaries traceable to case data (automated + 10 manual spot checks).
  - [ ] 0 / 10 prompt‑injection cases cause tool misuse or policy violation.
  - [ ] PII test: no unmasked NIK/PAN/phone in any output.
  - [ ] Adverse‑action drafts: 100 % of stated reasons match reason codes; 0 protected attributes mentioned.
  - [ ] Eval suite runs in CI and blocks merge on regression.
  - [ ] Every LLM call logged with model id, prompt hash, latency, token cost.
- **Tools & libraries:** an LLM API or local model (e.g., via Ollama) `[ASUMSI: choice depends on the bank's data‑residency policy]`, promptfoo or Inspect for evals, Microsoft Presidio for redaction, NeMo Guardrails (optional)
- **Common pitfalls:**
  - Giving the agent SQL or write access "for convenience".
  - Evaluating with vibes instead of a fixed eval set.
  - Sending customer PII to an external API without a legal basis and DPIA.
- **Stretch goal:** LLM‑as‑judge calibrated against human ratings (report agreement, e.g., Cohen's κ).
- **Reading:** [reading-list.md#e10](reading-list.md#e10)
- **Lectures, videos, blogs & repos:** ✍️ [Your AI Product Needs Evals](https://hamel.dev/blog/posts/evals/) · ✍️ [Monzo GenAI + predictive](https://monzo.com/blog/combining-generative-ai-and-predictive-modelling-to-fight-financial-crime) · 🎓 [promptfoo docs](https://www.promptfoo.dev/docs/intro/) — full list: [learning-resources.md#e10](learning-resources.md#e10)
