---
name: android-networking
description: >-
  Remote data sources and HTTP clients for Android repositories. Use for *Api.kt
  and remote networking implementation work.
disable-model-invocation: true
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
- No secrets, API keys, or tokens in source, logs, or `BuildConfig` — client-shipped values are extractable from the APK.
- Obtain credentials from a backend or user login; store tokens with guidance from `android-security`.
- Timeouts, cancellation via coroutines; map HTTP errors for UI.

## Dependencies

- `android-kotlin`
- `android-data`

## Validation

- Unit tests for mappers and error mapping; contract tests when project uses them.

## Anti-patterns

- Calling APIs directly from ViewModels or Composables.
