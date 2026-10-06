# Testing strategy — {Feature name}

## Unit

- ViewModels:
- Use cases / domain:
- Repositories (fakes):

## Integration

- Database / API:

## UI (Compose)

- Screens / behaviors:

## Maestro

- Flows:

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
