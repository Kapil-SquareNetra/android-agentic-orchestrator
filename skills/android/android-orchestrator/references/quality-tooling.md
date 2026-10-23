# Quality tooling (Detekt, Maestro)

Detekt and Maestro are **optional gates**. The hub **detects** them once per session. If a tool is not set up or the user **skips** it, **do not run that gate** — omit Detekt or Maestro from the pipeline and record **N/A** in final status with a one-line reason.

Do not install Gradle plugins, brew packages, or curl installers without user approval.

**Setup guides:** When asking the user to add Detekt or Maestro, paste the matching section from [setup-guides.md](setup-guides.md) (**Detekt** or **Maestro CLI**), then offer **Set up now** · **Already have it** · **Skip (N/A)**.

## Detekt (project Gradle task)

**When:** start of the **Detekt** phase.

**Detect:**

1. Gradle wrapper exists (`./gradlew`).
2. A `detekt` task exists (or the project documents an equivalent in `AGENTS.md`).

**If missing**, ask once using the **Detekt** section in [setup-guides.md](setup-guides.md) ([Detekt Gradle docs](https://detekt.dev/docs/gettingstarted/gradle)).

| User response | Action |
|---------------|--------|
| Will add / added | Run `./gradlew detekt` when the task exists. |
| Skip / not using Detekt | **Do not run Detekt.** Record **Detekt: N/A (not configured or skipped)**. Continue build, unit tests, and the rest of the lane. |

**If the task exists:** run `./gradlew detekt`. On failure, use `android-detekt` self-heal and re-run.

## Maestro CLI (host install)

**When:** **UI automation** phase, or Maestro smoke after UI changes — **only if Maestro is in scope** for this session.

**Detect:**

1. `maestro --version` (or `which maestro`).
2. Emulator or device when the user wants Maestro (`adb devices`).

**If CLI missing**, ask once using the **Maestro CLI** section in [setup-guides.md](setup-guides.md) ([Maestro install docs](https://docs.maestro.dev/maestro-cli/how-to-install-maestro-cli)).

| User response | Action |
|---------------|--------|
| Will install / installed | Run `maestro test …` when CLI and device are ready. |
| Skip / not using Maestro | **Do not run Maestro.** Record **Maestro: N/A (not installed or skipped)**. |

**If CLI present but no device and user still wants Maestro:** share the device steps in the Maestro guide; if they skip, **do not run Maestro** — **N/A**.

**Optional — Maestro MCP:** See setup guide; CLI alone is sufficient when in scope.

## In-scope summary

| Gate | Run when | Do not run when |
|------|----------|-----------------|
| **Detekt** | `detekt` Gradle task exists and user did not skip | No task, or user skipped / declined setup |
| **Maestro** | CLI (or agreed MCP) available, device ready if needed, user did not skip | CLI missing, no device and user will not run Maestro, or user skipped |

## Evidence

Final status lists Detekt and Maestro with **pass**, **fail**, or **N/A (reason)**. Build and unit tests still run when those gates are N/A.
