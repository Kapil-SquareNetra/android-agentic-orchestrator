---
name: android-compose
description: >-
  Jetpack Compose UI architecture, design-system reuse, and screen-level
  patterns including ui-architecture and design-system concerns. Use for
  **/ui/** and *Screen.kt files.
disable-model-invocation: true
---

# Compose UI

## Purpose

Stateless, testable Compose UI that renders explicit UI state.

## When to load

File routing for UI paths. Implementation phase for screens.

## Inputs

- `UiState` from ViewModel.
- Design system components available in the project.

## Outputs

- Composables, previews where useful, `Modifier.testTag` on interactive controls.

## Rules

- [Compose architecture](https://developer.android.com/develop/ui/compose/architecture)
- [UI layer](https://developer.android.com/topic/architecture/ui-layer)
- [Accessibility](https://developer.android.com/develop/ui/compose/accessibility)
- [Compose / UiAutomator interoperability](https://developer.android.com/develop/ui/compose/testing/interoperability)

- Prefer stateless composables; hoist state to ViewModel.
- Collect ViewModel state with `collectAsStateWithLifecycle()`.
- Do not pass ViewModels deep into the tree; use `state` + `onAction`.
- Handle loading, empty, error, and content explicitly.
- Reuse design-system components; keep business logic out of Composables.
- Modifier order is semantic (touch target, clipping, drawing) — reason about each chain; there is no single universal order.
- For Maestro `id:` selectors on `testTag`, set `Modifier.semantics { testTagsAsResourceId = true }` once high in the hierarchy (Compose 1.2.0+).
- One composable, one responsibility.

## Dependencies

- `android-kotlin`
- `android-architecture`

## Validation

- Compose UI tests or Maestro for critical interactions when FR requires.

## Anti-patterns

- Repository or use case calls inside Composables.
- Omitting empty/error states for user-visible lists.
- Expecting Maestro `id:` to match `testTag` without `testTagsAsResourceId`.
