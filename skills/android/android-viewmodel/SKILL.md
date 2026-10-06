---
name: android-viewmodel
description: >-
  Android screen ViewModels with StateFlow UI state, SharedFlow one-shot events,
  and state management. Use for *ViewModel.kt and presentation layer work.
disable-model-invocation: true
paths:
  - "**/*ViewModel.kt"
---

# ViewModel

## Purpose

Own screen UI state and route user actions to domain/data.

## When to load

`*ViewModel.kt` and presentation tasks (pagination, etc.).

## Inputs

- Use cases or repositories (via constructor injection).
- FR acceptance criteria for states.

## Outputs

- ViewModel with single `StateFlow` UI state; events via `SharedFlow` when needed.

## Rules

- [Architecture recommendations](https://developer.android.com/topic/architecture/recommendations)
- [UI layer](https://developer.android.com/topic/architecture/ui-layer)

- ViewModels at **screen** level; not in reusable leaf composables.
- Expose `StateFlow`; do not expose `MutableStateFlow`.
- Use `stateIn(WhileSubscribed(5000))` when collecting upstream Flows.
- Model UI state as data class or sealed interface: Loading, Content, Empty, Error.
- No `Context`, Activity, or Android resources in ViewModel.
- Trigger use cases; map domain → UI models; centralize state updates.

## Dependencies

- `android-kotlin`, `android-architecture`

## Validation

- Unit tests on `StateFlow.value` and event handling.

## Anti-patterns

- Multiple scattered `_state.value` updates without a single reducer.
