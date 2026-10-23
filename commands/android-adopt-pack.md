# Adopt orchestrator pack (existing repo)

Do not read the codebase for a feature or start implementation.

Reply with one sentence: open your **Android app** workspace in Cursor, copy the block below, paste it into **Agent** chat, then review the plan before applying any file edits.

Then output **one** fenced `markdown` block containing the prompt below, character for character. Do not add a second copy outside the fence.

````markdown
Adopt **android-agentic-orchestrator** into THIS Android project. **Do not overwrite** my files blindly.

**Keep (my project wins on conflicts):**
- `AGENTS.md`, `.cursor/rules/*.mdc`, `.cursor/routing/*.yml`, existing `docs/` workflow files
- Gradle module names, build/test commands, CI notes, team architecture rules

**Read from the pack** (local clone, `@` path, or `~/.cursor/skills/android/` + orchestrator repo `rules/` and `commands/`):
- `android-orchestrator/assets/AGENTS.md`
- `android-orchestrator/references/` (`definition-of-done`, `quality-commands`, `quality-tooling`, `setup-guides`, `new-project-init`)
- Pack `rules/*.mdc`, `commands/android-requirement.md`

**Deliver (plan only until I approve edits):**
1. Gap table: what I already have vs what the pack adds (lifecycle, FR + test cases, hub/spoke routing, optional Figma/Jira/Detekt/Maestro).
2. **Merged `AGENTS.md` draft** — my project specifics preserved; orchestrator steps added where missing.
3. **Rules plan** — which pack `.mdc` files to add or how to patch mine; flag glob overlap; do not delete my rules.
4. Explicit **do-not-copy** list (no wholesale architecture/theme replacement).
5. One-page **adoption checklist** for a single PR.

No feature implementation in this chat unless I say to apply the merged files after review.
````
