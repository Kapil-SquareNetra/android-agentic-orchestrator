# Maestro runbook (defaults)

Use with `android-maestro` in the UI automation phase. Commands: [quality-commands.md](quality-commands.md).

## Before running

- Per [quality-tooling.md](quality-tooling.md): if Maestro is not in scope (CLI missing, no device, user skipped), **do not run** Maestro flows; record **N/A**.
- When Maestro **is** in scope: confirm CLI (`maestro --version`) and emulator or device before `maestro test`.
- Read `appId` from the application `AndroidManifest.xml` (or product flavor manifest).
- For credentials, use Maestro `env` or local-only config files — never commit secrets; do not echo env values in agent logs.
- If the smoke path depends on **empty state** or first launch, run `adb shell pm clear <appId>` (or uninstall) before the flow.
- After **any UI change**, run smoke (or the FR-critical Maestro path) again — not only on first delivery.

## Flow structure

- One journey per FR critical path; use `runFlow` / subflows for login and shared setup.
- Prefer stable selectors: visible text, then `id:` (Compose `testTag` with `testTagsAsResourceId` enabled).
- After failures, distinguish **flow/script errors** (selector, timing) from **app defects** (crash, wrong state) before fixing code.

## Evidence for Definition of Done

- Command run (e.g. `maestro test .maestro/`) and pass/fail summary in final status.
- If flaky, note retry policy or file a follow-up; do not mark done on a single lucky re-run without noting instability.
