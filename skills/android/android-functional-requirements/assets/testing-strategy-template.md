# Testing strategy — {Feature name}

Map each test case to the lowest layer that can fail it ([testing strategies](https://developer.android.com/training/testing/fundamentals/strategies)). Most rows should be unit or component. Maestro is for a few critical journeys.

| TC IDs | Layer | Subject | Runs on | Trigger | Command |
|--------|-------|---------|---------|---------|---------|
| | Unit | | JVM | every slice | |
| | Component | | JVM / Robolectric | every slice | |
| | Feature | | JVM or emulator | pre-merge | |
| | Application | | emulator / device | critical journey | |

Layers: **Unit** (one class, fakes), **Component** (one screen, DAO, or API client), **Feature** (screen plus ViewModel plus fake repository), **Application** (Maestro or instrumented journey).

## Regression

- Bug fixes requiring new tests:

## Commands

Use project defaults from the orchestrator [quality-commands.md](../../android-orchestrator/references/quality-commands.md) (Detekt, Lint, assemble, unit, instrumented, Maestro). Record the exact commands run:

```bash
# Example — replace module and paths for your project
./gradlew detekt
./gradlew :app:lintDebug
./gradlew :app:testDebugUnitTest
```
