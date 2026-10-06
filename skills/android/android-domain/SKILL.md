---
name: android-domain
description: >-
  Optional Android domain layer with single-action use cases and no mutable
  state. Use for **/domain/** Kotlin sources.
disable-model-invocation: true
---

# Domain

## Purpose

Encapsulate reusable business rules between UI and data.

## When to load

`**/domain/**` files and domain-heavy tasks.

## Inputs

- Repository interfaces (not implementations).
- FR business rules.

## Outputs

- Use cases named `{Verb}{Noun}UseCase`; domain models.

## Rules

- [Domain layer](https://developer.android.com/topic/architecture/domain-layer)

- Optional layer — use when logic is complex or shared across ViewModels.
- One action per use case; no mutable state in use cases.
- Naming: present-tense verb + noun + `UseCase`.
- Return domain models; handle errors inside the use case.
- Params as a data class.
- No Android SDK, Room, Retrofit, or Compose imports.

## Dependencies

- `android-kotlin`

## Validation

- JVM unit tests under `src/test` with fake repositories.

## Anti-patterns

- Use cases that know about UI state types.
