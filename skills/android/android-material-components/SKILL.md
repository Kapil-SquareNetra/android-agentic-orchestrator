---
name: android-material-components
description: >-
  Chooses Jetpack Compose Material 3 components by purpose: actions, navigation,
  lists, dialogs, sheets, fields, chips, and progress. Use for **/ui/**,
  *Screen.kt, and when picking a Material component.
disable-model-invocation: true
---

# Material components

## Purpose

Pick one `androidx.compose.material3` component for the job. If the app already wraps that component, use the wrapper.

## When to load

UI file routing. Task signal `material`. Code review when UI changed.

## Inputs

- What the user must do (act, navigate, choose, enter text, wait, or be told).
- Window size and how many peer actions already exist.
- Project design-system wrappers, if any.

## Outputs

- The Material 3 component (or the project wrapper that maps to it).

## Rules

Sources: [M3 components](https://m3.material.io/components), [Compose components](https://developer.android.com/develop/ui/compose/components), [Buttons](https://m3.material.io/components/buttons), [FAB](https://m3.material.io/components/floating-action-button/guidelines), [Navigation rail](https://m3.material.io/components/navigation-rail/overview), [Bottom sheets](https://m3.material.io/components/bottom-sheets/overview), [Dialogs](https://m3.material.io/components/dialogs), [Text fields](https://m3.material.io/components/text-fields/overview), [Chips](https://m3.material.io/components/chips/overview), [Segmented buttons](https://m3.material.io/components/segmented-buttons).

Use the project wrapper when it delegates to the same Material component. Do not restyle a different component to imitate the right one.

| Purpose | Use |
|---------|-----|
| Screen structure | `Scaffold` with slots for app bar, navigation, FAB, and snackbar |
| Most important action on the screen | One `FloatingActionButton` or `ExtendedFloatingActionButton`. Not one FAB per card |
| High-emphasis action | Filled `Button` |
| Medium emphasis | `FilledTonalButton` or `ElevatedButton` |
| Lower emphasis | `OutlinedButton` |
| Lowest emphasis | `TextButton` |
| Minor icon-only action | `IconButton` in the app bar or toolbar |
| Several related actions from that FAB | FAB menu only when no toolbar or navigation rail sits with the FAB |
| Top-of-screen navigation and secondary actions | `TopAppBar` or a floating toolbar, not a second FAB |
| Switch top-level views, compact window (under 600dp), about 3–5 destinations | `NavigationBar` |
| Same job, medium and larger windows | `NavigationRail` (collapsed). Expanded rail when labels must stay visible; expressive M3 uses that instead of a drawer |
| Existing large-window apps still on drawers | `ModalNavigationDrawer` or `PermanentNavigationDrawer` until the app adopts an expanded rail |
| In-screen sections, not app destinations | `TabRow` / `PrimaryTabRow` |
| Continuous index of text or images | `ListItem` in a lazy list |
| Settings hub: navigate to a screen | `ListItem` + chevron, `clickable`; subtitle = current value |
| Settings hub: boolean pref (e.g. dark mode) | `ListItem` + `Switch` in `trailingContent` — no extra screen |
| One subject with its own content and actions | `Card` |
| Urgent prompt, alert, or confirmation that blocks the flow | `AlertDialog` / `BasicAlertDialog` |
| Extra or secondary content anchored to the bottom; user can dismiss it | `ModalBottomSheet` on compact and medium widths. Standard sheet only when primary content stays usable |
| Short, non-blocking process update | `Snackbar` via `SnackbarHost`. Not a dialog |
| Free text | `TextField` (filled: short forms and dialogs) or `OutlinedTextField` (long forms) |
| Keyword search | `SearchBar` |
| Short known list of choices | `DropdownMenu` |
| One option in a set, or a numeric range | `RadioButton`, or `Slider` / `RangeSlider` |
| Date or time | `DatePicker` or `TimePicker` |
| Filter tags, suggestions, entered tokens, or a smart action | `FilterChip`, `SuggestionChip`, `InputChip`, `AssistChip` |
| Two to five simple choices that switch a view or sort | Connected button group. Compose still exposes segmented-button rows; prefer the project’s expressive group when it exists. More items or richer filters use chips |
| Known progress | Determinate linear or circular progress |
| Unknown wait | Indeterminate progress. A dialog only if the user must not continue |
| Count or status on a nav icon | `Badge` |

Button labels are short sentence case. One filled button or one FAB is the primary action in a region.

## Dependencies

- `android-compose`
- `android-material`

## Validation

- The chosen component matches the table, or the screen states why the project wrapper differs.
- Primary action is visually unique. Confirmations are dialogs. Transient messages are snackbars.

## Anti-patterns

- A custom clickable `Box` where `Button`, `ListItem`, or `IconButton` fits.
- Dialog for a message the user does not need to confirm.
- Navigation drawer and an expanded rail for the same destinations.
- FAB menu beside a toolbar or navigation rail.
