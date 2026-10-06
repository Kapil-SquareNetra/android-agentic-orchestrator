---
name: android-testing
description: >-
  Android unit, integration, Compose UI, and instrumented testing with fakes.
  Use in test phase, code review, and **/test/** or **/androidTest/** files.
disable-model-invocation: true
paths:
  - "**/test/**/*.kt"
  - "**/androidTest/**/*.kt"
---

# Testing

## Purpose

Prove FRs at the right level with maintainable tests.

## When to load

Testing phase, code-review phase (mandatory), test file routing.

## Inputs

- `docs/testing-strategy.md`
- Impact matrix test column.

## Outputs

- Unit, integration, UI tests; regression tests for bug fixes.

## Rules

- [What to test](https://developer.android.com/training/testing/fundamentals/what-to-test)
- [Compose testing](https://developer.android.com/develop/ui/compose/testing)

**Unit:** ViewModels (`StateFlow.value`), use cases, mappers, repository behavior with fakes.

**Integration:** DB, API, repository with test doubles.

**UI:** screen behaviors, navigation smoke, state restoration.

**Regression:** significant bug fixes get a test when feasible.

Prefer **fakes** over mocks. Targeted runs by change type; full DoD before feature complete.

## Dependencies

- `android-kotlin`
- Layer skills for code under test

## Validation

- Named tests map to FR IDs where possible.

## Anti-patterns

- Running entire suite on every typo fix when targeted tests suffice (but DoD still applies at end).
