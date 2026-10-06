---
name: android-viewmodel
description: >-
  Android screen ViewModels with StateFlow UI state and lifecycle-aware state
  management. Use for *ViewModel.kt and presentation layer work.
disable-model-invocation: true
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

- ViewModel with a single `StateFlow` UI state; transient UI effects modeled in that state when needed.

## Rules

- [Architecture recommendations](https://developer.android.com/topic/architecture/recommendations)
- [UI layer](https://developer.android.com/topic/architecture/ui-layer)
- [UI events](https://developer.android.com/topic/architecture/ui-layer/events)
- [Coroutines with lifecycle](https://developer.android.com/topic/libraries/architecture/coroutines)

- ViewModels at **screen** level; not in reusable leaf composables.
- Expose `StateFlow`; do not expose `MutableStateFlow`.
- Use `stateIn(viewModelScope, SharingStarted.WhileSubscribed(5_000), initial)` when exposing upstream `Flow` streams.
- Model one-shot UI effects (snackbars, navigation after validation) as fields on UI state the UI consumes and clears — not a replay-0 `SharedFlow` that can drop events.
- Model UI state as data class or sealed interface: Loading, Content, Empty, Error.
- No `Context`, Activity, or Android resources in ViewModel.
- Trigger use cases in `viewModelScope`; map domain → UI models; centralize state updates.
- In Compose, collect UI state with `collectAsStateWithLifecycle()`.
- **Paging 3:** expose `Flow<PagingData<UiModel>>` from the repository; collect in UI with `collectAsLazyPagingItems()`; keep paging sources in the data layer, not in Composables.

## Dependencies

- `android-kotlin`
- `android-architecture`

## Validation

- Unit tests: with `stateIn` / `WhileSubscribed`, start a collector in `runTest` `backgroundScope` (or Turbine) before asserting `StateFlow.value`. See [Testing Kotlin flows](https://developer.android.com/kotlin/flow/test).

## Anti-patterns

- Multiple scattered `_state.value` updates without a single reducer.
- Asserting `.value` on a `WhileSubscribed` flow with no active collector.
