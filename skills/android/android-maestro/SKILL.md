---
name: android-maestro
description: >-
  Maestro YAML UI automation for Android user journeys. Preferred for E2E unless
  a technical reason requires another tool. Use in UI automation phase and
  **/maestro/**/*.yaml files.
disable-model-invocation: true
paths:
  - "**/maestro/**/*.yaml"
---

# Maestro (UI automation)

## Purpose

Validate real user workflows on device or emulator.

## When to load

UI automation phase after build/unit/integration. Maestro YAML edits.

## Inputs

- FR user flows and acceptance criteria.
- App `appId` from manifest.

## Outputs

- Create or update flows; run `maestro test <flow.yaml>`.

## Rules

- [Maestro flows](https://docs.maestro.dev/maestro-flows)
- [Android](https://docs.maestro.dev/get-started/supported-platform/android)
- [Selectors](https://docs.maestro.dev/maestro-flows/flow-control-and-logic/how-to-use-selectors)

**Preferred** UI automation unless technical reason otherwise.

Journey pattern: Launch → Login (if needed) → Navigate → Act → Verify → Back → Verify state.

```yaml
appId: com.example.app
---
- launchApp
- tapOn: "..."
- assertVisible: "..."
```

Use semantic matchers; `testTag` / `id:` when text is ambiguous. Framework-agnostic (Compose, Views, etc.).

Do not load database/Compose implementation skills while authoring flows — only FR journey context.

## Dependencies

- `android-testing`, `android-functional-requirements` (journey context)

## Validation

- Flow passes locally or blocker documented.

## Anti-patterns

- Maestro loaded during pure repository implementation.
