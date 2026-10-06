---
name: android-retrospective
description: >-
  Captures post-delivery lessons and updates universal guardrails only for
  recurring patterns. Use after acceptance in android-orchestrator, not during
  FR authoring.
disable-model-invocation: true
---

# Retrospective

## Purpose

Compare delivery to the original requirement; improve the workflow for the next feature.

## When to load

After acceptance criteria pass. **Not** during requirement phase (past-miss checklist lives in impact analysis).

## Inputs

- Original requirement or plan.
- `docs/functional-requirements.md`, test results, review notes.

## Outputs

- `docs/retrospective.md` from [assets/retrospective-template.md](assets/retrospective-template.md).
- Optional skill/rule update proposal (universal patterns only).

## Rules

1. What was missed vs the requirement?
2. What required rework?
3. Unexpected failures?
4. Testing and architecture gaps?
5. Project-specific vs universal?
6. If universal and recurring, propose a guardrail update — do not auto-edit skills for one-off issues.

Docs must reflect actual implementation; no documentation for its own sake.

## Dependencies

- Hub definition of done.

## Validation

- Retrospective exists for meaningful features.
- `requirement-retrospective.md` in a repo remains a **lesson catalog**, not a spec for other apps.

## Anti-patterns

- Copying FamWise-specific details into universal skills.
- Skipping retrospective because compile passed.
