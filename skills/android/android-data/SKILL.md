---
name: android-data
description: >-
  Android data layer and repository patterns as the sole entry to data sources.
  Use for **/data/** and *Repository.kt files.
disable-model-invocation: true
paths:
  - "**/data/**/*.kt"
  - "**/*Repository.kt"
---

# Data layer and repositories

## Purpose

Expose app data through repositories; isolate data sources.

## When to load

Data paths and repository files; repository change-impact tasks.

## Inputs

- Domain/repository contracts.
- Remote and local source APIs.

## Outputs

- Repository implementations, mappers, offline-first behavior per FR.

## Rules

- [Data layer](https://developer.android.com/topic/architecture/data-layer)

- One repository per data type; repositories are the only entry to data sources.
- Map DTO/entity → domain where shapes differ.
- UI and ViewModels never depend on data sources directly.
- Flow for observed data; suspend for one-shot operations.
- After meaningful edits, walk change impact: API, DTO, mapper, domain, repository, use case, ViewModel, UI, pagination, states, nav, persistence, analytics, Maestro, regression.

## Dependencies

- `android-kotlin`, `android-architecture`
- `android-networking` / `android-database` when those sources change

## Validation

- Repository unit tests with fakes; integration tests when persistence/API changes.

## Anti-patterns

- Loading Compose skills while editing repositories only.
