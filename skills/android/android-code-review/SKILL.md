---
name: android-code-review
description: >-
  Pre-completion Android code review across architecture, Kotlin, Android
  lifecycle, UI, quality, testing, and security. Use in code-review phase after
  tests pass.
disable-model-invocation: true
---

# Code review

## Purpose

Gate completion before acceptance criteria sign-off.

## When to load

Code-review phase with `android-architecture`, `android-kotlin`, `android-security`, `android-performance`, `android-testing` (all mandatory in this phase). Add `android-accessibility`, `android-material`, and `android-material-components` when UI changed.

## Inputs

- Diff, test results, Detekt report, the plan step, and `docs/test-cases.md`.

## Outputs

- Pass or actionable fix list.

## Rules

Run spec compliance before quality. Label each finding Critical, Important, or Suggestion.

### Spec compliance

- The diff matches the plan step’s files and FR / TC IDs.
- Each TC for that step has a test, or a recorded reason it stays manual.
- No behavior outside the approved FR.

### Architecture

- Correct layer and dependency direction
- No business logic in UI
- Appropriate abstractions

### Kotlin

- Idiomatic, null-safe, coroutine-safe, maintainable

### Android

- Lifecycle-safe, configuration-safe, memory-safe, main-thread-safe

### UI

- Correct states, reusable components, accessibility, navigation

### Quality

- When Detekt was in scope: it passes; no unjustified suppressions; no unnecessary dependencies

### Testing

- Appropriate unit, integration, UI automation, regression coverage

### Security

- No secrets; no sensitive logging; safe storage; input validation

## Dependencies

- Hub loads related spokes in same phase.

## Validation

- Review checklist complete before AC sign-off.

## Anti-patterns

- Approve because compile succeeded.
