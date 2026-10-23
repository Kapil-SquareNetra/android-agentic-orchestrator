# Definition of Done (Android feature)

A feature is **not** complete merely because it compiles.

Complete when **all** apply (with evidence: commands, test output, or review notes):

- Functional requirements and every positive, negative, and edge row in `docs/test-cases.md` are **approved**, and each row is traced to a passing test or a recorded manual check in `docs/acceptance-criteria.md`
- Evidence is from a run after the last code change (command, exit, tests run)
- Impact analysis is completed (or lane-appropriate skip documented)
- Architecture is appropriate for the change
- Kotlin standards are followed
- When Detekt is **in scope** ([quality-tooling.md](quality-tooling.md)): `./gradlew detekt` passes and there are no unjustified suppressions. When Detekt was skipped or not configured, status shows **Detekt: N/A** — not required.
- Android Lint passes for affected modules (or documented N/A)
- Existing reusable components were considered
- Loading, empty, error, and content states handled where applicable
- Navigation is validated when navigation changed
- Relevant unit, integration, UI, and regression tests pass. When Maestro is **in scope**, Maestro flows pass; when Maestro was skipped or not installed, status shows **Maestro: N/A** — not required.
- Security, performance, and accessibility considered
- Code review passes (hub code-review phase)
- Acceptance criteria satisfied with evidence
- When docs list a **Figma** frame: design verification recorded in acceptance (screenshot compare via Figma MCP + app capture) or skip reason (MCP not installed, no device, user declined)
- When docs list a **Jira** key: FR tracking matches the issue; ticket updates only if the user asked
- Documentation updated to match implementation
- Retrospective captured for meaningful work (feature lane)
- New guardrails in skills/rules only for **recurring universal** failure patterns
