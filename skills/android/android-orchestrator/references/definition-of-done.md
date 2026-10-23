# Definition of Done (Android feature)

A feature is **not** complete merely because it compiles.

Complete when **all** apply (with evidence: commands, test output, or review notes):

- Functional requirements and every positive, negative, and edge row in `docs/test-cases.md` are **approved**, and each row is traced to a passing test or a recorded manual check in `docs/acceptance-criteria.md`
- Evidence is from a run after the last code change (command, exit, tests run)
- Impact analysis is completed (or lane-appropriate skip documented)
- Architecture is appropriate for the change
- Kotlin standards are followed
- `./gradlew detekt` (or project equivalent) passes — see [quality-commands.md](quality-commands.md)
- Android Lint passes for affected modules (or documented N/A)
- No unjustified Detekt suppressions
- Existing reusable components were considered
- Loading, empty, error, and content states handled where applicable
- Navigation is validated when navigation changed
- Relevant unit, integration, UI, Maestro, and regression tests pass
- Security, performance, and accessibility considered
- Code review passes (hub code-review phase)
- Acceptance criteria satisfied with evidence
- Documentation updated to match implementation
- Retrospective captured for meaningful work (feature lane)
- New guardrails in skills/rules only for **recurring universal** failure patterns
