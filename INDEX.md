# Android Agentic Orchestrator — Index

Hub-and-spoke Cursor skills for **Android + Kotlin** feature delivery: requirement or plan in, architecture-aware implementation, quality pipeline, self-heal, review, and retrospective out.

## Install (personal / team)

```bash
# Skills (hub + spokes)
cp -R skills/android ~/.cursor/skills/

# Optional lightweight rules (description-only; no file globs)
cp rules/*.mdc ~/.cursor/rules/
```

Enable **Sync Skills for Cloud Agents** in Cursor Settings if you use cloud agents.

For a single Android repo, copy `skills/android/android-orchestrator/assets/AGENTS.md` to the project root and optionally `assets/cursor-routing/` → `.cursor/routing/`.

## Start a feature

1. Copy `skills/android/android-requirement-analysis/assets/initial-requirement-template.md` to `docs/initial-requirement.md` (or paste sections in chat).
2. Fill **Required to start**: summary, goal, actor, happy path, When/Then AC, in/out of scope.
3. In Agent chat, invoke **`android-orchestrator`** (or describe Android feature work so the hub attaches).
4. Hub runs the lifecycle below; spokes load only for the current **file**, **task**, and **phase**.

FamWise or `requirement-retrospective.md` is a **past-miss lesson catalog** only — not the product spec.

## End-to-end flow

```text
Requirement or Plan
        │
        ▼
Understand input (requirement-driven vs plan-driven)
        │
        ▼
Functional requirements  →  docs/functional-requirements.md
        │
        ▼
Impact analysis          →  docs/requirement-impact.md
        │                    (past-miss checklist — reference only)
        ▼
Architecture             →  docs/architecture.md (when useful)
        │
        ▼
Implementation plan      →  docs/implementation-plan.md
        │                    docs/testing-strategy.md
        ▼
Implementation           →  file + task + phase routing
        │
        ▼
Detekt → Build → Unit → Integration → Maestro/UI
        │
        ├─ fail → classify → root cause → fix → re-run FAILED check → regression
        │         (escalate after 3 identical failures with no new evidence)
        ▼
Code review              →  architecture, kotlin, security, performance, testing
        │
        ▼
Acceptance criteria      →  docs/acceptance-criteria.md (evidence)
        │
        ▼
Retrospective            →  docs/retrospective.md
        │
        ▼
Update guardrails        →  only recurring universal patterns
        │
        ▼
Hub final status         →  done | blocked | next (+ command output)
```

## Hub vs spokes

| Role | Skill | Auto-invoke |
|------|--------|-------------|
| **Hub** | `android-orchestrator` | Yes (from description) |
| **Spokes** | All other `android-*` skills | No (`disable-model-invocation: true`) |

The hub **reads** spoke `SKILL.md` files when the phase or file requires them. This keeps Maestro, Detekt, and data-layer guidance out of unrelated Compose work.

## Phase → which spokes to load

| Phase | Skills |
|-------|--------|
| Requirement | `android-requirement-analysis`, `android-functional-requirements`, `android-impact-analysis` |
| Architecture | `android-architecture`, `android-kotlin`, + affected layer skills |
| Implementation | Routing from `file-routing.yml` + task extras + `android-architecture` |
| Detekt | `android-detekt`, `android-kotlin` |
| UI automation | `android-maestro`, `android-testing`, FR context |
| Code review | `android-architecture`, `android-kotlin`, `android-security`, `android-performance`, `android-testing`, `android-code-review`; + `android-accessibility` if UI changed |

Canonical routing: `skills/android/android-orchestrator/references/file-routing.yml` and `skill-dependencies.yml`.

## Skill catalog

| Folder | Purpose |
|--------|---------|
| `android-orchestrator` | Hub, DoD, routing YAML, AGENTS template |
| `android-requirement-analysis` | Understand ask; initial requirement template |
| `android-functional-requirements` | FR doc + plan/testing/AC templates |
| `android-impact-analysis` | Impact matrix + past-miss checklist |
| `android-architecture` | Layers, modules, stack choices |
| `android-kotlin` | Kotlin + Detekt quality habits |
| `android-compose` | UI, design system, screen patterns |
| `android-viewmodel` | StateFlow, events, screen VM |
| `android-domain` | Use cases |
| `android-data` | Repositories |
| `android-networking` | Remote APIs |
| `android-database` | Room / DAO |
| `android-navigation` | Nav Compose, deep links |
| `android-testing` | Unit, integration, UI |
| `android-maestro` | YAML UI journeys |
| `android-detekt` | Static analysis gate |
| `android-security` | Secrets, storage, auth |
| `android-performance` | Perf review |
| `android-accessibility` | A11y on screens |
| `android-code-review` | Pre-merge checklist |
| `android-retrospective` | Post-delivery lessons |

## Definition of done

See `skills/android/android-orchestrator/references/definition-of-done.md`. A feature is not done because it compiles.

## Not in scope

- **KMM / KMP** — use separate `kmm-*` skills; do not mix unless the user asks.
- This repo does not modify `~/.cursor/skills/kmm-*`.

## References

- Cursor [Agent Skills](https://cursor.com/docs/skills)
- Android [app architecture](https://developer.android.com/topic/architecture)
- [Maestro](https://docs.maestro.dev/maestro-flows) · [Detekt](https://detekt.dev/docs/gettingstarted/gradle)
