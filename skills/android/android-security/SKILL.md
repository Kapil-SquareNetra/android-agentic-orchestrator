---
name: android-security
description: >-
  Android security practices for auth, secrets, storage, and network safety. Use
  in code-review phase always, and when tasks touch credentials or sensitive
  data.
disable-model-invocation: true
---

# Security

## Purpose

Prevent secrets leakage and unsafe data handling.

## When to load

**Code-review phase (mandatory).** Task routing for auth, credentials, permissions, sensitive data, network security.

## Inputs

- FR security-related requirements.

## Outputs

- Review findings or secure implementation patterns.

## Rules

- [Security tips](https://developer.android.com/topic/security/best-practices)

- No secrets or API keys in source or logs.
- Use Android Keystore / EncryptedSharedPreferences / DataStore as appropriate.
- Validate inputs; least-privilege permissions.
- Certificate pinning only when required and documented.

## Dependencies

- `android-architecture`

## Validation

- Code review security section passes.

## Anti-patterns

- Loading security spoke for every static Composable with no sensitive data.
