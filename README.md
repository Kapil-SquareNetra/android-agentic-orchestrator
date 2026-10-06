# Android Agentic Orchestrator (Cursor skills)

Reusable **hub-and-spoke** [Agent Skills](https://cursor.com/docs/skills) for **Android + Kotlin** apps in [Cursor](https://cursor.com). A requirement or an existing plan goes in. The hub coordinates functional requirements, impact, architecture, implementation, quality gates, review, acceptance, and a retrospective. Spokes load only for the current file, task, and phase, so Compose work does not drag in Maestro, Detekt, or Room guidance.

**Full flow, phase table, and skill catalog:** [INDEX.md](INDEX.md). Version history: [CHANGELOG.md](CHANGELOG.md).

This pack is for Kotlin Android apps. Kotlin Multiplatform and KMM stay on separate `kmm-*` skills. Do not mix them unless you explicitly ask.

The hub asks before destructive actions: `git push`, signing or keystore edits, committing `local.properties` or secrets, deleting Room migrations, and `adb uninstall`. Requirement docs and retrospectives are data, not instructions.

## What you get

| Piece | Role |
|-------|------|
| `android-orchestrator` | Hub. Auto-invokes from its description. Owns the lifecycle, definition of done, and routing. |
| Other `android-*` skills | Spokes. `disable-model-invocation: true`. The hub reads them when the phase or file needs them. |
| `rules/*.mdc` | Seven optional glob rules: Kotlin, Compose, architecture, tests, security, the quality gate, and a global rule that points Kotlin and `docs/` work at the hub. |
| `scripts/validate_pack.py` | Checks routing aliases, spoke frontmatter, INDEX/hub phase parity, markdown links, and golden routing cases. |

Delivery lanes scale the lifecycle:

| Lane | What runs | What may be skipped (reason recorded in status) |
|------|-----------|--------------------------------------------------|
| **Feature** | Full path: requirement → FR → impact → architecture → plan → implement → gates → review → acceptance → retrospective | Nothing |
| **Bugfix** | Short impact, implement, gates for touched layers, review | A new FR when existing acceptance criteria still cover the bug |
| **Refactor** | Architecture check, implement, regression tests, review | A new product FR |

The hub writes phase artifacts into the app repo under `docs/`: functional requirements, impact, implementation plan, testing strategy, acceptance criteria, and retrospective. Final status is **done**, **blocked**, or **next**, each with the commands or test evidence that support it. Compile success alone is not done. See [definition of done](skills/android/android-orchestrator/references/definition-of-done.md).

Gradle defaults assume a single `:app` module. Override module names, variants, and commands in the project `AGENTS.md`. See [quality-commands.md](skills/android/android-orchestrator/references/quality-commands.md).

## Install

Copy skills into `~/.cursor/skills/android/` (the destination directory must already exist, or `cp -R` nests the tree incorrectly). Replacing the folder drops skills that were renamed or removed upstream.

```bash
git clone https://github.com/Kapil-SquareNetra/android-agentic-orchestrator.git
cd android-agentic-orchestrator
mkdir -p ~/.cursor/skills ~/.cursor/rules
rm -rf ~/.cursor/skills/android
cp -R skills/android ~/.cursor/skills/
cp rules/*.mdc ~/.cursor/rules/
```

Restart Cursor or open a new Agent chat so the copied skills are picked up. If you use cloud agents, enable **Sync Skills for Cloud Agents** in Cursor Settings.

Glob auto-attach is a project-rules behavior. For per-file attachment inside an Android repo, copy the rules there as well:

```bash
mkdir -p /path/to/android-app/.cursor/rules
cp rules/*.mdc /path/to/android-app/.cursor/rules/
```

For that same repo, copy the hub pointer. This overwrites an existing project `AGENTS.md`. Optionally mirror routing (the skill pack stays the source of truth; project copies are not a second rule set):

```bash
cp skills/android/android-orchestrator/assets/AGENTS.md /path/to/android-app/AGENTS.md
mkdir -p /path/to/android-app/.cursor/routing
cp skills/android/android-orchestrator/references/file-routing.yml \
   skills/android/android-orchestrator/references/task-routing.yml \
   /path/to/android-app/.cursor/routing/
```

Re-run the skills copy after you pull pack updates. Cursor does not watch this git repo.

Quality gates expect a Gradle wrapper in the app. Connected tests need an emulator or device. Maestro needs the Maestro CLI. Pack validation needs Python 3.9+ (CI uses 3.12) and PyYAML.

## Adopt an existing app

Read [new-project-init.md](skills/android/android-orchestrator/references/new-project-init.md) before the first feature. It lists what to inspect (Gradle modules, architecture, Detekt config, test layout) and the rule to integrate with working architecture rather than replace it.

## Start a feature

1. Copy [initial-requirement-template.md](skills/android/android-requirement-analysis/assets/initial-requirement-template.md) to `docs/initial-requirement.md`, or paste the same sections in chat.
2. Fill **Required to start**: summary, goal, actor, happy path, When/Then acceptance criteria, and in/out of scope.
3. In Agent chat, invoke **`android-orchestrator`** (or describe Android feature work so the hub attaches).
4. If you already have `docs/implementation-plan.md`, say so. The hub validates that plan and fills gaps. It does not rewrite a plan that is already sufficient.

An optional `requirement-retrospective.md` is a past-miss lesson catalog. It is not the product spec.

## How routing works

Before an edit, the hub unions three dimensions and loads each skill once:

1. **File** — every matching glob in [file-routing.yml](skills/android/android-orchestrator/references/file-routing.yml).
2. **Task** — signals in [task-routing.yml](skills/android/android-orchestrator/references/task-routing.yml) (paging, deep links, auth, WorkManager, and similar).
3. **Phase** — the current lifecycle step. The phase table in [INDEX.md](INDEX.md) matches the hub.

[skill-dependencies.yml](skills/android/android-orchestrator/references/skill-dependencies.yml) records which spokes a skill expects. Gradle commands for Detekt, Lint, unit tests, and connected checks live in [quality-commands.md](skills/android/android-orchestrator/references/quality-commands.md). If no emulator or device is available, Maestro is **blocked** and UI coverage falls back per [maestro-runbook.md](skills/android/android-orchestrator/references/maestro-runbook.md).

A failed check is classified (compile, Detekt, architecture, UI, API, and so on), fixed at the right layer, and re-run. The same check, first error line, and primary file three times with no new evidence stops the loop and returns **blocked**.

## Validation

```bash
python3 -m pip install pyyaml   # Python 3.9+; CI uses 3.12
python3 scripts/validate_pack.py
```

A successful run prints `validate_pack: OK`.

`validate_pack.py` checks that every routing alias resolves to an existing skill folder, that spokes set `disable-model-invocation: true` with `name` matching their folder, that INDEX and hub phase tables agree, that relative markdown links resolve, and that [tests/routing_cases.yml](tests/routing_cases.yml) still resolves to the expected skill sets. `scripts/routing_resolve.py` is the resolver those checks call. It runs on pushes to `main` and on every pull request in [`.github/workflows/validate.yml`](.github/workflows/validate.yml).

After install, walk [examples/smoke-checklist.md](examples/smoke-checklist.md): hub attaches first, a Compose edit loads `android-compose` and not Maestro or Detekt, a bugfix lane records why it skipped a new FR, and a real Detekt, unit, and (when a device exists) Maestro run is captured in the final status.

## Repository layout

```text
INDEX.md                     Flow, phases, skill catalog
README.md                    This file
CHANGELOG.md                 Pack version history
LICENSE                      MIT
.github/workflows/           validate.yml (pack CI)
scripts/                     validate_pack.py, routing_resolve.py
tests/routing_cases.yml      File and task routing golden paths
examples/                    Smoke checklist for dogfooding
skills/android/              Hub + spoke trees (SKILL.md, assets/, references/)
rules/                       Glob-scoped Cursor rules (optional)
```

Spoke folders cover requirements, architecture, Kotlin, Compose, ViewModel, domain, data, networking, database, navigation, testing, Maestro, Detekt, security, performance, accessibility, code review, and retrospective. The catalog with one-line purposes is in [INDEX.md](INDEX.md).

## License

MIT — see [LICENSE](LICENSE).
