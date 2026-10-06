---
name: android-compose
description: >-
  Jetpack Compose UI architecture, design-system reuse, and screen-level
  patterns including ui-architecture and design-system concerns. Use for
  **/ui/** and *Screen.kt files.
disable-model-invocation: true
paths:
  - "**/ui/**/*.kt"
  - "**/*Screen.kt"
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

- Prefer stateless composables; hoist state to ViewModel.
- Do not pass ViewModels deep into the tree; use `state` + `onAction`.
- Handle loading, empty, error, and content explicitly.
- Reuse design-system components; keep business logic out of Composables.
- Modifier order: layout, draw, semantics, click.
- One composable, one responsibility.

## Dependencies

- `android-kotlin`
- `android-architecture` for layer boundaries

## Validation

- Compose UI tests or Maestro for critical interactions when FR requires.

## Anti-patterns

- Repository or use case calls inside Composables.
- Omitting empty/error states for user-visible lists.
