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

For Jetpack Compose, `id:` matches `Modifier.testTag` only when the app sets `Modifier.semantics { testTagsAsResourceId = true }` high in the UI tree. **Dialogs and date pickers** often render outside the root — apply the same semantics on dialog content, or fall back to stable visible text (e.g. Material **“OK”** on `DatePickerDialog`).

### UI-change gate

After any user-facing UI change, re-run at least one **smoke** flow before marking the task done (with Gradle unit tests). Typical sequence: install debug APK → `adb shell pm clear <appId>` when the flow assumes empty/first-run state → `maestro test <flow>`.

### Compose flow tips

- Prefer a dedicated `testTag` on the control that opens a picker (e.g. `open_date_picker`), not the read-only field text.
- Empty-list smoke fails if prior runs left data — always clear app data or use a dedicated test account flow.
- When using Maestro MCP, pass an **absolute path** to the flows directory if the tool resolves relative paths from the wrong cwd. Tag filters (`include_tags`) only work when flows declare matching tags.

Do not load database/Compose implementation skills while authoring flows — only FR journey context.

## Dependencies

- `android-testing`
- `android-functional-requirements`

## Validation

- Flow passes locally or blocker documented with runbook fallback (Compose UI tests).

## Anti-patterns

- Maestro loaded during pure repository implementation.
- Marking UI gate done when no device/emulator was available and no fallback tests ran.
