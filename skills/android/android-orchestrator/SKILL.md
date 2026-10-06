---
name: android-orchestrator
description: >-
  Coordinates Android-only agentic delivery from a requirement or an existing
  plan through FRs, impact, architecture, implementation, Detekt, build, tests,
  Maestro, self-heal, review, acceptance, and retrospective. Uses file, task,
  and phase routing to load minimum context. Use for Kotlin Android app work,
  not KMM or KMP unless the user explicitly asks.
---

# Android orchestrator (hub)

Read [references/definition-of-done.md](references/definition-of-done.md) before marking work complete. Routing tables: [file-routing.yml](references/file-routing.yml), [skill-dependencies.yml](references/skill-dependencies.yml). New projects: [new-project-init.md](references/new-project-init.md).

## Purpose

Run the master Android lifecycle with a hub-and-spoke model: you coordinate; spokes supply depth only when loaded.

## When to load

- User gives an Android feature requirement or an implementation plan.
- User asks to continue Android delivery, fix failures, or verify acceptance criteria.
- Do **not** use for KMM/KMP/iOS unless explicitly requested.

## Inputs

- **Initial requirement** — filled [initial-requirement-template.md](assets/initial-requirement-template.md) (or same sections in chat). Minimum: summary, goal, actor, happy path, must-have When/Then AC, in/out of scope. See `android-requirement-analysis/assets/initial-requirement-template.md` for the full template.
- Or `docs/implementation-plan.md` (plan-driven).
- Optional: `requirement-retrospective.md` (lesson catalog only, not a spec).

## Outputs

- Phase artifacts (templates in spoke `assets/`): initial requirement, FR, impact, plan, testing strategy, AC, retrospective.
- Final status: **done**, **blocked**, or **next**, each with command or test evidence.

## Rules

### Entry points

1. **Requirement-driven** — derive FRs, flows, edges, impact, architecture, plan, tests, then execute.
2. **Plan-driven** — validate plan against Android architecture, fill gaps, impact, past-miss checklist; **do not recreate** a sufficient plan; execute and self-heal.

Scale depth by complexity. **Do not skip stages** because the ask looks simple.

### Lifecycle (only current-phase spokes)

Understand → FR → impact → (past-miss checklist during FR/impact) → architecture → plan → implement → Detekt → build → unit → integration → Maestro/UI → on failure: classify → RCA → fix → **re-run failed check** → regression → review → acceptance → retrospective → optional universal guardrail update → **final status**.

### Phase skill loads (mandatory)

| Phase | Load these skills (read `SKILL.md`) |
|-------|-------------------------------------|
| Requirement | `android-requirement-analysis`, `android-functional-requirements`, `android-impact-analysis` |
| Architecture | `android-architecture`, `android-kotlin`, plus affected layer skills |
| Implementation | File + task skills from routing + `android-architecture` |
| Detekt | `android-detekt`, `android-kotlin` (quality section) |
| UI automation | `android-maestro`, `android-testing`, FR context |
| Code review | `android-architecture`, `android-kotlin`, `android-security`, `android-performance`, `android-testing`, `android-code-review`; add `android-accessibility` when UI changed |

Spokes use `disable-model-invocation: true` — **you** must read their files when the phase requires them.

### Three-dimensional routing

Before editing a file, determine:

1. **File** — baseline from `file-routing.yml`
2. **Task** — extras (paging, deep links, auth, etc.)
3. **Phase** — table above

Load the **union** of the three. Unload prior phase spokes from active reasoning. Never load a skill because it exists in the project.

### Past-miss reference

The current requirement or plan is the **spec**. FamWise / `requirement-retrospective.md` is a **lesson catalog** only. During FR and impact, scan `android-impact-analysis` past-miss checklist. Do not copy FamWise product details. Do not block if the file is absent.

### Self-heal

Classify: compile, Detekt, dependency, architecture, runtime, UI, nav, API, DB, state, test infra, environment, requirement misunderstanding. Fix the correct layer; re-run the **failed** check; then regression. No symptom patches. After **three identical failures** with no new evidence, **escalate** (blocked).

### Per-file decision (before edit)

1. What requirement am I implementing?
2. What file am I modifying?
3. What layer?
4. What file skills apply?
5. What task skills apply?
6. What phase skills apply?
7. What guardrails apply? (Hub may point at `~/.cursor/rules/android-*.mdc` for the matching group.)
8. What validation follows?

### Agent roles (one spoke at a time)

Product, Architect, Kotlin, UI, Domain, Data, QA, UI Automation, Quality, Reviewer — coordinated by this hub.

## Dependencies

Shallow graph in `skill-dependencies.yml`. Do not transitive-load the whole library.

## Validation

Targeted checks by change type; full [definition-of-done.md](references/definition-of-done.md) before **done**.

## Anti-patterns

- Loading Maestro/Detekt/Room during unrelated Compose-only work.
- Treating FamWise retrospective as source of truth.
- Replacing existing project architecture without integration analysis.
- Marking done when only compile succeeded.
- Parallelizing Domain → UseCase → ViewModel → UI when types are not agreed.
