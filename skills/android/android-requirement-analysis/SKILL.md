---
name: android-requirement-analysis
description: >-
  Turns an Android feature ask or plan into structured requirement understanding
  before implementation. Use in the requirement phase of android-orchestrator when
  deriving scope, actors, flows, and open questions from a raw requirement.
disable-model-invocation: true
---

# Requirement analysis

## Purpose

Understand the ask and decide what must be documented before code.

## When to load

Requirement phase only. Hub loads this with `android-functional-requirements` and `android-impact-analysis`.

## Inputs

- **Initial requirement** — user text or [assets/initial-requirement-template.md](assets/initial-requirement-template.md) (project copy e.g. `docs/initial-requirement.md`). Execution may start when all **Required to start** sections in that template are filled.
- Optional plan-driven path: existing `docs/implementation-plan.md`.

## Outputs

- Outline for `docs/functional-requirements.md` (use template in `android-functional-requirements/assets/`).
- List of user flows, edge cases, non-goals, open questions.
- Recommendation: requirement-driven vs gaps in supplied plan.

## Rules

- **Plan-driven:** validate against [Android architecture](https://developer.android.com/topic/architecture); list missing FRs; do not rewrite a sufficient plan.
- **Requirement-driven:** if the user provides only a short ask, offer or apply `initial-requirement-template.md`; once **Required to start** is satisfied, derive FRs, flows, edges, then hand off to impact and architecture.
- Scan past-miss checklist in `android-impact-analysis` during FR work (FamWise file is reference only).
- Scale depth to complexity; simple bugs still need explicit AC.

## Dependencies

- `android-functional-requirements` for the FR document shape.
- `android-impact-analysis` for impact and past-miss checklist.

## Validation

- Every meaningful feature has traceable FR IDs before implementation starts.
- Open questions are explicit or resolved with user input.

## Anti-patterns

- Starting Compose or repository code before FR outline exists.
- Treating FamWise retrospective as product spec.
