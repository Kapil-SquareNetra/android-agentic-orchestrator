---
name: android-performance
description: >-
  Android and Compose performance considerations for lists, recomposition, and
  main-thread work. Use in code-review phase always and for performance tasks.
disable-model-invocation: true
---

# Performance

## Purpose

Keep UI smooth and avoid main-thread and memory issues.

## When to load

**Code-review phase (mandatory).** Performance optimization tasks.

## Inputs

- Profiling signals or FR performance constraints.

## Outputs

- Recommendations or fixes (lazy lists, stable keys, background work).

## Rules

- [Performance](https://developer.android.com/topic/performance)
- Compose: stable lambdas, keyed lazy lists, avoid unbounded work in composition.

- Lifecycle-safe, configuration-safe, memory-safe, main-thread-safe (review checklist).
- Use `Dispatchers.IO` for disk/network; structured concurrency in ViewModels.

## Dependencies

- `android-compose`

## Validation

- No obvious jank paths; heavy work off main thread.

## Anti-patterns

- Premature optimization without a measured issue.
