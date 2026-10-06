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

- No secrets or API keys in source, logs, or `BuildConfig`.
- Prefer not storing long-lived secrets on device. Use short-lived tokens from your backend when possible.
- For secrets that must remain on device, use Android Keystore-backed keys — not plain SharedPreferences or unencrypted DataStore.
- `EncryptedSharedPreferences` and `androidx.security.crypto` are deprecated; do not recommend them for new work.
- Preferences DataStore is not encrypted storage. Optional: `androidx.datastore:datastore-tink` `AeadSerializer` (still alpha) when the project already depends on it.
- Validate inputs; least-privilege permissions.
- Certificate pinning only when required and documented.

### Review checklist (when in scope)

- `AndroidManifest.xml`: `android:exported`, intent filters, permissions
- `PendingIntent` mutability (`FLAG_IMMUTABLE` / `FLAG_MUTABLE`)
- Network security config (`res/xml/network_security_config.xml`) and cleartext traffic
- ProGuard / R8 rules (`proguard-rules.pro`) and release shrinking
- WebView: JavaScript, file access, mixed content
- `allowBackup`, backup rules, and data-extraction rules
- Release builds: no PII or tokens in logs; ProGuard/R8 rules for release

## Dependencies

- `android-architecture`

## Validation

- Code review security section passes.

## Anti-patterns

- Treating `BuildConfig` fields as secret storage.
- Loading security spoke for every static Composable with no sensitive data.
