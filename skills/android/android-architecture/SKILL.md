---
name: android-architecture
description: >-
  Defines modern Android layer boundaries, module layout, and stack choices for
  Kotlin Compose apps. Use in architecture and implementation phases and code
  review when validating dependency direction.
disable-model-invocation: true
---

# Android architecture

## Purpose

Keep UI → Presentation → Domain → Data → Infrastructure clear and testable.

## When to load

Architecture phase (with `android-kotlin` and layer skills). Implementation and code review when structure is in scope.

## Inputs

- FR and impact docs.
- Existing Gradle modules and packages.

## Outputs

- `docs/architecture.md` when the change is non-trivial.
- Stack decisions recorded only when new dependencies are justified.

## Rules

Official guides:

- [App architecture](https://developer.android.com/topic/architecture)
- [Recommendations](https://developer.android.com/topic/architecture/recommendations)
- [Data layer](https://developer.android.com/topic/architecture/data-layer)
- [UI layer](https://developer.android.com/topic/architecture/ui-layer)
- [Domain layer](https://developer.android.com/topic/architecture/domain-layer) (optional; use when logic is reused or complex)

Add Hilt, Room, Retrofit/Ktor, Serialization, WorkManager, Paging, DataStore, Navigation Compose **only when the requirement needs them**.

Multi-module example when justified: `app`, `core/*`, `feature/*` — one responsibility per module; do not inflate module count.

**Do not replace** working project architecture without integration analysis.

## Dependencies

- `android-kotlin` for language conventions.

## Validation

- Repositories are the data-layer entry; UI does not call data sources directly.
- ViewModels at screen level; no business logic in Composables.

## Anti-patterns

- KMM/CMP stack unless user explicitly requests.
- Global singletons for session state instead of explicit state holders.
