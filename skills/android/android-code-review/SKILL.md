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

Code-review phase with `android-architecture`, `android-kotlin`, `android-security`, `android-performance`, `android-testing` (all mandatory in this phase). Add `android-accessibility` when UI changed.

## Inputs

- Diff, test results, Detekt report.

## Outputs

- Pass or actionable fix list.

## Rules

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

- Detekt passes; no unjustified suppressions; no unnecessary dependencies

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
