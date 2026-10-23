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

- `docs/test-cases.md` (positive, negative, and edge cases tied to FR IDs)
- `docs/testing-strategy.md`
- Impact matrix test column.

## Outputs

- Unit, integration, UI tests; regression tests for bug fixes.

## Rules

- [What to test](https://developer.android.com/training/testing/fundamentals/what-to-test)
- [Compose testing](https://developer.android.com/develop/ui/compose/testing)
- [Testing Kotlin flows](https://developer.android.com/kotlin/flow/test)

Choose the lowest layer that can catch the bug ([testing strategies](https://developer.android.com/training/testing/fundamentals/strategies)). Put negative and edge cases on the JVM when the rule is logic or state. Keep Maestro for a few critical journeys.

**Unit (JVM):** use cases, mappers, repository behavior with fakes. ViewModels: if UI state uses `stateIn` / `WhileSubscribed`, start a collector in `runTest` `backgroundScope` (or use Turbine) before reading `StateFlow.value`.

**Component:** one screen (`createComposeRule` or Robolectric), one DAO, or one API client.

**Feature:** screen, ViewModel, and a fake repository together, including navigation inside the feature.

**Application:** instrumented or Maestro journeys. Few of these.

**Regression:** significant bug fixes get a test when feasible.

Prefer **fakes** over mocks. Targeted runs by change type; full DoD before feature complete.

## Dependencies

- `android-kotlin`

## Validation

- Named tests map to FR IDs and, where a row exists, to TC IDs in `docs/test-cases.md`.

## Anti-patterns

- Running entire suite on every typo fix when targeted tests suffice (but DoD still applies at end).
- Asserting `StateFlow.value` with no collector when the ViewModel uses `WhileSubscribed`.
