---
name: android-accessibility
description: >-
  Compose accessibility semantics, content descriptions, and TalkBack-friendly
  UI. Use for *Screen.kt baseline and when UI changed in code review.
disable-model-invocation: true
---

# Accessibility

## Purpose

Meet FR a11y expectations and Android accessibility guidelines.

## When to load

`*Screen.kt` file routing. Code review when UI changed. A11y-specific tasks.

## Inputs

- FR accessibility requirements.

## Outputs

- Semantics, content descriptions, touch targets, contrast via design system.

## Rules

- [Compose accessibility](https://developer.android.com/develop/ui/compose/accessibility)

- Meaningful content descriptions for icons and images.
- Merge semantics where appropriate; test with TalkBack for critical flows.

## Dependencies

- `android-compose`

## Validation

- Manual or automated a11y checks for critical user paths.

## Anti-patterns

- Clickable icons without contentDescription.
