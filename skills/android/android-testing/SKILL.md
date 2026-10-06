---
name: android-testing
description: >-
  Android unit, integration, Compose UI, and instrumented testing with fakes.
  Use in test phase, code review, and **/test/** or **/androidTest/** files.
disable-model-invocation: true
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
- [Testing Kotlin flows](https://developer.android.com/kotlin/flow/test)

**Unit:** use cases, mappers, repository behavior with fakes. ViewModels: if UI state uses `stateIn` / `WhileSubscribed`, start a collector in `runTest` `backgroundScope` (or use Turbine) before reading `StateFlow.value`.

**Integration:** DB, API, repository with test doubles.

**UI:** screen behaviors, navigation smoke, state restoration.

**Regression:** significant bug fixes get a test when feasible.

Prefer **fakes** over mocks. Targeted runs by change type; full DoD before feature complete.

## Dependencies

- `android-kotlin`

## Validation

- Named tests map to FR IDs where possible.

## Anti-patterns

- Running entire suite on every typo fix when targeted tests suffice (but DoD still applies at end).
- Asserting `StateFlow.value` with no collector when the ViewModel uses `WhileSubscribed`.
