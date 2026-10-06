---
name: android-impact-analysis
description: >-
  Maps Android functional requirements through UI, navigation, presentation,
  domain, data, API, database, and testing with an impact matrix. Includes a
  past-miss checklist from retrospectives. Use in requirement phase before
  implementation.
disable-model-invocation: true
---

# Impact analysis

## Purpose

Show what changes, why, what could regress, and what tests protect each FR.

## When to load

Requirement phase (with FR work). Not during implementation-only hotfixes unless impact is unclear.

## Inputs

- `docs/functional-requirements.md`
- Optional: `requirement-retrospective.md` (lesson catalog only)

## Outputs

- `docs/requirement-impact.md` from [assets/requirement-impact-template.md](assets/requirement-impact-template.md).

## Rules

Trace each requirement: UI → Navigation → Presentation → Domain → Data → API → Database → Cache → Config → Analytics → Testing.

Impact matrix columns: Requirement, Component, Impact, Change Required, Test Required.

### Past-miss checklist (reference, not spec)

Before sign-off on impact, confirm the FR/plan addresses:

- Missed or ambiguous FRs
- Edge cases and validation rules
- Empty / loading / error UI states
- Navigation entry, back, deep links, auth-gated routes
- Architecture layer mistakes (logic in UI, skipping repository)
- Unit vs integration vs UI vs Maestro coverage
- Wrong assumptions about API or persistence
- Impact analysis and regression tests for bug fixes

If `requirement-retrospective.md` exists, propose **generalized** new checklist items for user approval — do not edit installed skills automatically. Do not copy another product’s details. If absent, use this list only.

## Dependencies

- `android-functional-requirements`

## Validation

- Every high-priority FR has at least one component and test row.
- Slice order respects domain → data → UI when types are new.

## Anti-patterns

- Impact doc that only lists file names without regression risk.
- Blocking delivery because retrospective file is missing.
