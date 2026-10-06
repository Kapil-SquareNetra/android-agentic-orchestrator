---
name: android-kotlin
description: >-
  Kotlin coding standards for Android apps including coroutines, Flow, and
  Detekt-oriented quality habits. Use when editing Kotlin sources, Detekt phase,
  or code review for idiomatic Kotlin.
disable-model-invocation: true
---

# Kotlin (Android)

## Purpose

Write idiomatic, maintainable Kotlin in Android layers.

## When to load

File routing for `**/*.kt`. Architecture, Detekt, and code-review phases.

## Inputs

- File being edited.
- Layer (UI, domain, data).

## Outputs

- Kotlin code and fixes aligned with project style.

## Rules

[Coding conventions](https://kotlinlang.org/docs/coding-conventions.html). [Code quality tools](https://kotlinlang.org/docs/jvm-code-analysis.html).

**Prefer:** immutability, `val`, null safety, sealed types, data classes, value classes where useful, coroutines, structured concurrency, Flow, small functions, clear naming, composition.

**Avoid:** `!!`, global mutable state, blocking calls, unnecessary singletons, excessive scope functions, clever unreadable code, unnecessary abstraction, business logic in UI.

### Quality (Detekt phase)

Run `./gradlew detekt` (and module tasks if configured). Fix violations in the owning layer skill before suppressing.

## Dependencies

- None (base spoke).

## Validation

- Detekt passes or suppressions follow `android-detekt` five-step process.

## Anti-patterns

- Business rules in Composables or Activities.
