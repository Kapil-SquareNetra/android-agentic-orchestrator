---
name: android-detekt
description: >-
  Detekt static analysis gate for Kotlin Android projects including suppression
  discipline. Use only in Detekt validation phase, not during feature UI coding.
disable-model-invocation: true
---

# Detekt

## Purpose

Enforce Kotlin quality before merge.

## When to load

**Detekt phase only** — after implementation slice, before or with build.

## Inputs

- Project Gradle Detekt config.

## Outputs

- Clean `detekt` run or justified fixes/suppressions.

## Rules

- [Detekt Gradle plugin](https://detekt.dev/docs/gettingstarted/gradle)

Run `./gradlew detekt` and module/variant tasks when configured. Configure project appropriately.

Checks include: complexity, smells, naming, style, bugs, long methods, large classes, nesting, unsafe patterns, duplication.

### Suppression (required process)

1. Understand the violation.
2. Change code if possible.
3. Is the rule appropriate for this code?
4. Suppress only when justified.
5. Document non-obvious suppressions.

On failure: load the **file** spoke for the violating path, fix, re-run detekt.

## Dependencies

- `android-kotlin`

## Validation

- Detekt passes with no unjustified suppressions.

## Anti-patterns

- Keeping full Detekt docs in context during Compose implementation.
