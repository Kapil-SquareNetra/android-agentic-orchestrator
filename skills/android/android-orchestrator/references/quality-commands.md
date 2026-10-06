# Quality commands (defaults)

Override in project `AGENTS.md` when module names or variants differ. Record the exact commands run in final status evidence.

| Gate | Default command | Notes |
|------|-----------------|-------|
| Detekt | `./gradlew detekt` | Use `detektMain` when type resolution is configured and main sources compile. |
| Android Lint | `./gradlew :app:lintDebug` | Replace `:app` with the application module. |
| Build | `./gradlew :app:assembleDebug` | |
| Unit tests | `./gradlew :app:testDebugUnitTest` | |
| Instrumented | `./gradlew :app:connectedDebugAndroidTest` | Requires a running emulator or device. |
| Maestro | `maestro test <flow-or-directory>` | Typical dirs: `.maestro/` or `maestro/`. |

Mark a gate **N/A** in status only when the change cannot affect that layer (document why).

## Multi-module projects

Replace `:app` with the affected module (`:feature:foo`, `:core:data`, etc.). Run Detekt/Lint on the modules you touched; for library-only changes, `assembleDebug` may target a consuming app module. Document the exact module list in `AGENTS.md` when the repo differs from a single `:app` layout.
