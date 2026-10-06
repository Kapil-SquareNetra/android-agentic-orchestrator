---
name: android-functional-requirements
description: >-
  Authors Android functional requirements with acceptance criteria, states, and
  edge cases. Use when writing or updating docs/functional-requirements.md in
  the requirement phase.
disable-model-invocation: true
---

# Functional requirements

## Purpose

Produce a complete FR document the implementation and tests trace to.

## When to load

Requirement phase. Not during Detekt or Maestro-only work.

## Inputs

- Requirement analysis outline.
- User corrections to scope.

## Outputs

- `docs/functional-requirements.md` from [assets/functional-requirements-template.md](assets/functional-requirements-template.md).
- `docs/implementation-plan.md` from [assets/implementation-plan-template.md](assets/implementation-plan-template.md) (plan phase).
- `docs/testing-strategy.md` from [assets/testing-strategy-template.md](assets/testing-strategy-template.md).
- `docs/acceptance-criteria.md` from [assets/acceptance-criteria-template.md](assets/acceptance-criteria-template.md) when separate from the FR.

## Rules

Use the table:

| ID | Requirement | Description | Actor | Preconditions | Expected Result | Priority |

Also document where relevant: user actions, inputs, outputs, validation, success, failure, empty, loading, error, permissions, authentication, network, persistence, navigation, offline, analytics, accessibility, edge cases.

Official context: [Guide to app architecture](https://developer.android.com/topic/architecture) for layer vocabulary.

## Dependencies

- `android-requirement-analysis`

## Validation

- Each FR has testable expected results.
- UI features specify loading/empty/error when user-visible.

## Anti-patterns

- Vague AC (“works well”).
- Copying another app’s FR verbatim from a past project without adapting scope.
