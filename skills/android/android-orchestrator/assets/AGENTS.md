# Android agentic development

This project uses the **Android orchestrator** hub-and-spoke workflow.

1. Start from a filled **initial requirement** (`docs/initial-requirement.md` using the template in the orchestrator or requirement-analysis skill assets), a requirement in chat with the same sections, or an existing **implementation plan** — do not rewrite a sufficient plan.
2. Produce or update `docs/functional-requirements.md`, `docs/requirement-impact.md`, `docs/implementation-plan.md`, and `docs/testing-strategy.md` for meaningful features.
3. Implement with **file + task + phase** routing; load only the skills the orchestrator selects.
4. Quality order: Detekt → build → unit → integration → Maestro/UI → review → acceptance.
5. On failure: classify, fix the correct layer, re-run the **failed** check, then regression.
6. Done means the full Definition of Done in the orchestrator skill — not compile-only.

Personal skills live under `~/.cursor/skills/android/`. FamWise or `requirement-retrospective.md` is a **past-miss reference**, not the product spec.
