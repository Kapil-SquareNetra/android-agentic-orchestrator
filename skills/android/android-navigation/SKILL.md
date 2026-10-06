---
name: android-navigation
description: >-
  Navigation Compose routes, args, back stack, deep links, and conditional
  navigation. Use for **/navigation/** and navigation change tasks.
disable-model-invocation: true
---

# Navigation

## Purpose

Type-safe navigation aligned with FR entry points and back behavior.

## When to load

Navigation files; deep-link or auth-gated route tasks.

## Inputs

- FR navigation section.
- Route graph in project.

## Outputs

- Nav graph updates; ViewModel scoping per destination when needed.

## Rules

- [Navigation Compose](https://developer.android.com/develop/ui/compose/navigation)
- [Getting started](https://developer.android.com/guide/navigation/navigation-getting-started)

- When the project uses Navigation 2.8+, prefer type-safe routes: `@Serializable` destinations, `composable<T>()`, and `NavBackStackEntry.toRoute<T>()`.
- Document: entry points, routes, arguments, back behavior, state restoration, deep links, conditional navigation, auth requirements, failure navigation.

**Validation for nav changes:** navigation tests + affected UI tests + Maestro nav flows (not Maestro alone).

## Dependencies

- `android-kotlin`
- `android-architecture`
- `android-compose`

## Validation

- Navigation tests and targeted Maestro flows.

## Anti-patterns

- Hard-coded route strings scattered without a single graph definition.
