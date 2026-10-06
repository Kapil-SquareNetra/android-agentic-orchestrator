---
name: android-maestro
description: >-
  Maestro YAML UI automation for Android user journeys. Preferred for E2E unless
  a technical reason requires another tool. Use in UI automation phase and
  **/maestro/**/*.yaml files.
disable-model-invocation: true
---

# Maestro (UI automation)

## Purpose

Validate real user workflows on device or emulator.

## When to load

UI automation phase after build/unit/integration. Maestro YAML edits.

## Inputs

- FR user flows and acceptance criteria.
- App `appId` from manifest.
- [maestro-runbook.md](../android-orchestrator/references/maestro-runbook.md)

## Outputs

- Create or update flows; run `maestro test <flow.yaml>` or `maestro test <directory>`.

## Rules

- [Maestro flows](https://docs.maestro.dev/maestro-flows)
- [Android](https://docs.maestro.dev/get-started/supported-platform/android)
- [Selectors](https://docs.maestro.dev/reference/selectors/core-selectors.md)

**Preferred** UI automation unless technical reason otherwise.

Journey pattern: Launch → Login (if needed) → Navigate → Act → Verify → Back → Verify state.

```yaml
appId: com.example.app
env:
  TEST_USER: ${TEST_USER}  # supply locally; never commit real credentials
---
- launchApp
- runFlow: login.yaml
- tapOn:
    id: book_appointment
- assertVisible: "Confirmed"
```

Use semantic matchers; `testTag` / `id:` when text is ambiguous.

For Jetpack Compose, `id:` matches `Modifier.testTag` only when the app sets `Modifier.semantics { testTagsAsResourceId = true }` high in the UI tree.

Do not load database/Compose implementation skills while authoring flows — only FR journey context.

## Dependencies

- `android-testing`
- `android-functional-requirements`

## Validation

- Flow passes locally or blocker documented with runbook fallback (Compose UI tests).

## Anti-patterns

- Maestro loaded during pure repository implementation.
- Marking UI gate done when no device/emulator was available and no fallback tests ran.
