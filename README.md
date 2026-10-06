# Android Agentic Orchestrator (Cursor skills)

Reusable **hub-and-spoke** Agent Skills for Android + Kotlin development in [Cursor](https://cursor.com): structured requirements, file-scoped expertise, Detekt → build → tests → Maestro, self-healing, and review.

**Read the flow and install steps in [INDEX.md](INDEX.md).**

## Quick install

```bash
git clone https://github.com/Kapil-SquareNetra/android-agentic-orchestrator.git
cd android-agentic-orchestrator
cp -R skills/android ~/.cursor/skills/
cp rules/*.mdc ~/.cursor/rules/   # optional
```

Restart or open a new Agent chat, then start with the [initial requirement template](skills/android/android-requirement-analysis/assets/initial-requirement-template.md) and `/android-orchestrator`.

## Repository layout

```text
INDEX.md                 Flow, phases, skill catalog
README.md                This file
skills/android/          Hub + spoke SKILL.md trees
rules/                   Description-only Cursor rules (optional)
```

## License

MIT — see [LICENSE](LICENSE).
