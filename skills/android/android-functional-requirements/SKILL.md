---
name: android-functional-requirements
description: >-
  Authors Android functional requirements and the positive, negative, and edge
  test cases that cover them. Use when writing or updating
  docs/functional-requirements.md or docs/test-cases.md in the requirement phase.
disable-model-invocation: true
---

# Functional requirements

## Purpose

Produce a complete FR document and the test cases that cover it, so implementation and tests trace to the same IDs.

## When to load

Requirement phase. Not during Detekt or Maestro-only work.

## Inputs

- Requirement analysis outline.
- User corrections to scope.

## Outputs

- `docs/functional-requirements.md` from [assets/functional-requirements-template.md](assets/functional-requirements-template.md).
- `docs/test-cases.md` from [assets/test-cases-template.md](assets/test-cases-template.md), in the same step as the FR.
- `docs/implementation-plan.md` from [assets/implementation-plan-template.md](assets/implementation-plan-template.md) (plan phase).
- `docs/testing-strategy.md` from [assets/testing-strategy-template.md](assets/testing-strategy-template.md).
- `docs/acceptance-criteria.md` from [assets/acceptance-criteria-template.md](assets/acceptance-criteria-template.md) when separate from the FR.

## Rules

Use the table:

| ID | Requirement | Description | Actor | Preconditions | Expected Result | Priority |

Also document where relevant: user actions, inputs, outputs, validation, success, failure, empty, loading, error, permissions, authentication, network, persistence, navigation, offline, analytics, accessibility, edge cases.

Official context: [Guide to app architecture](https://developer.android.com/topic/architecture) for layer vocabulary.

### Test cases (same step as the FR)

Write `docs/test-cases.md` before asking for approval. Method, in order:

1. Turn each FR into one behavior that can pass or fail ([write test cases from requirements](https://www.testdart.com/blog/how-to-write-test-cases-from-requirements)).
2. List the conditions that change the outcome: valid inputs, invalid inputs, and limits.
3. **Positive** — one row for each distinct valid outcome. A single happy path is enough when every valid input behaves the same (equivalence partition, [ISTQB CTFL](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf)).
4. **Negative** — one row for each distinct invalid condition, not one row for the whole FR. Empty, unknown, expired, and unauthorized are separate cases when the FR names them. The app rejects that case and does not apply the change. Do not put two invalid conditions in the same row.
5. **Edge** — one row for each side of a limit (the boundary and the closest value on the other side), and one row for each unusual condition the FR names (empty, exact minimum, offline, expired session). Several edge rows for one FR are expected.
6. Each row names the FR ID, category, preconditions, concrete data, steps, and one observable expected result ([test planning](https://microsoft.github.io/code-with-engineering-playbook/automated-testing/test-planning/)).

Show the user the counts (positive, negative, edge) with the FR summary.

### Approval and traceability

1. Mark `docs/functional-requirements.md` and `docs/test-cases.md` **DRAFT** until the user explicitly approves (e.g. “approve FR”).
2. **Stop implementation** after publishing or updating the FR or its test cases until approval — plan-only or chat requests do not replace sign-off.
3. When the user changes scope mid-project (plan edits, new settings UX, design system), update the FR and the affected test cases **before** coding and show a short **delta** (new/changed FR IDs).
4. Sync `docs/initial-requirement.md`, `docs/requirement-impact.md`, `docs/test-cases.md`, and `docs/acceptance-criteria.md` when FR IDs or behavior change.

## Dependencies

- `android-requirement-analysis`

## Validation

- Each FR has testable expected results.
- Every FR ID has at least one Positive case, one Negative row per distinct invalid condition, and one Edge row per boundary side and per unusual condition the FR names.
- UI features specify loading/empty/error when user-visible.

## Anti-patterns

- Vague AC (“works well”) or test cases with no concrete data.
- A test case that mixes two invalid conditions, so a failure does not show which rule broke.
- Collapsing several invalid or boundary conditions into a single Negative or Edge row.
- Copying another app’s FR verbatim from a past project without adapting scope.
