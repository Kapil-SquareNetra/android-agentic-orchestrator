---
name: android-networking
description: >-
  Remote data sources and HTTP clients for Android repositories. Use for *Api.kt
  and remote networking implementation work.
disable-model-invocation: true
paths:
  - "**/*Api.kt"
  - "**/network/**/*.kt"
---

# Networking

## Purpose

Implement remote data sources behind repositories.

## When to load

`*Api.kt`, network modules, API change tasks.

## Inputs

- API contracts, DTOs, auth requirements from FR.

## Outputs

- API interfaces, DTOs, mappers; error mapping to domain.

## Rules

- [Data layer](https://developer.android.com/topic/architecture/data-layer) — networking is a data source, not an app-wide entry point.
- Retrofit or Ktor only if already in project or justified in plan.
- No secrets in source; use BuildConfig or secure storage per `android-security`.
- Timeouts, cancellation via coroutines; map HTTP errors for UI.

## Dependencies

- `android-kotlin`, `android-data`

## Validation

- Integration or fake-server tests for critical endpoints.

## Anti-patterns

- Calling APIs from ViewModels or Composables.
