---
name: android-material
description: >-
  Material Design 3 guidelines for Android Compose: theme roles, color,
  typography, shape, elevation, and adaptive layout. Use for **/ui/**,
  *Screen.kt, and when the user mentions Material, MaterialTheme, or M3.
disable-model-invocation: true
---

# Material Design

## Purpose

Apply Material Design 3 through the app theme. Do not invent a parallel visual system.

## When to load

UI file routing. Task signal `material`. Code review when UI changed.

## Inputs

- Existing `MaterialTheme` (or project theme wrapper) if the app already has one.
- Screen purpose and window size.

## Outputs

- Theme usage (`colorScheme`, `typography`, `shapes`) and layout that follows Material roles.

## Rules

Official sources: [Material Design 3](https://m3.material.io/), [Develop](https://m3.material.io/develop), [Styles](https://m3.material.io/styles), [Layout](https://m3.material.io/foundations/layout/layout-overview/overview), [Material 3 in Compose](https://developer.android.com/develop/ui/compose/designsystems/material3).

- Android UI is Compose-first. Use `androidx.compose.material3`. Material Views (MDC-Android) is maintenance-only; do not add it for new UI.
- Theme the app once with `MaterialTheme` (`colorScheme`, `typography`, `shapes`). Screens read `MaterialTheme.*`. Do not hardcode colors, type sizes, or corner radii when a theme role fits.
- Keep an existing project theme. Extend its scheme, type, and shape scale. Do not replace a working theme with stock defaults.
- Color roles: `primary` for prominent actions and active state, `secondary` for less prominent controls, `tertiary` for contrast accents. Pair each container with its on-color (`onPrimary` on `primary`, `onPrimaryContainer` on `primaryContainer`, same for surface and other roles).
- Support light and dark with `isSystemInDarkTheme()`. On API 31+, dynamic color (`dynamicLightColorScheme` / `dynamicDarkColorScheme`) may follow the wallpaper; always fall back to the app’s static schemes.
- **User-controlled theme:** when Settings offers dark mode, persist the choice (e.g. DataStore) and pass `darkTheme` into the root `MaterialTheme` from Activity/`ThemeViewModel`; use dynamic color only when the user is not forcing light/dark.
- **Dates:** use Material 3 `DatePicker` / `DatePickerDialog` for calendar dates — not separate month/day/year text fields.
- **Settings (M3):** use `Scaffold` + `LazyColumn` of `ListItem`s; keep instant toggles (e.g. dark mode) on the hub with `Switch` in `trailingContent`; navigate to a detail screen for multi-step or destructive actions (API key tutorial, clear data with confirm).
- Type scale roles are display, headline, title, body, and label (large, medium, small). Set `fontFamily` on each `TextStyle` you customize. M3 `Typography` has no single default font parameter.
- Shape scale: extra small through extra large via `MaterialTheme.shapes`. Use it for component corners.
- Elevation is mostly tonal (surface tone), with shadow as a secondary cue. Prefer `tonalElevation` on `Surface`.
- Layout: use a scaffold, canonical layouts, and breakpoints (compact, medium, expanded, large, extra-large). Support LTR and RTL. Component choice is `android-material-components`.
- Motion: use Material ripple and theme motion. Do not add a second animation system for standard presses and transitions.
- Custom colors must keep accessible on-color pairs. Material roles are selected for contrast; mismatched roles are not.

## Dependencies

- `android-compose`

## Validation

- Light and dark (and dynamic color, if enabled) still show readable content and a visible primary action.
- No new one-off colors or type sizes that bypass the theme.

## Anti-patterns

- `androidx.compose.material` (Material 2) on new screens.
- Raw `Color(...)` or `sp` text styles where a theme role exists.
- Mixing `tertiaryContainer` content on a `primary` container for contrast.
