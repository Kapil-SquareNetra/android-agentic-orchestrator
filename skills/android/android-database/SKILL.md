---
name: android-database
description: >-
  Room and local persistence as Android data sources. Use for *Dao.kt and
  database module work.
disable-model-invocation: true
paths:
  - "**/*Dao.kt"
  - "**/database/**/*.kt"
---

# Database (Room)

## Purpose

Local persistence behind repositories.

## When to load

`*Dao.kt`, entities, migrations.

## Inputs

- Schema requirements from FR (offline, cache).

## Outputs

- DAOs, entities, migrations tested.

## Rules

- [Room](https://developer.android.com/training/data-storage/room)
- [Data layer](https://developer.android.com/topic/architecture/data-layer)

- DAOs are data sources; repositories coordinate them.
- Migrations for schema changes; migration tests required.
- Do not load Compose skills for DAO-only work.

## Dependencies

- `android-kotlin`, `android-data`

## Validation

- Database and repository tests after schema change.

## Anti-patterns

- Exposing Room entities to UI layer without mapping.
