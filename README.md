# Android Agentic Orchestrator (Cursor skills)

Reusable **hub-and-spoke** Agent Skills for Android + Kotlin development in [Cursor](https://cursor.com): structured requirements, file-scoped expertise, Detekt → build → tests → Maestro, self-healing, and review.

**Read the flow and install steps in [INDEX.md](INDEX.md).**

## Quick install

```bash
git clone https://github.com/Kapil-SquareNetra/android-agentic-orchestrator.git
cd android-agentic-orchestrator
cp -R skills/android ~/.cursor/skills/
cp rules/*.mdc ~/.cursor/rules/   # optional; globs attach rules to matching files
```

Restart or open a new Agent chat, then start with the [initial requirement template](skills/android/android-requirement-analysis/assets/initial-requirement-template.md) and `/android-orchestrator`.

## Validation

```bash
python3 -m pip install pyyaml
python3 scripts/validate_pack.py
```

Runs on every push/PR via GitHub Actions. See [CHANGELOG.md](CHANGELOG.md) (current pack version **0.2.0**).

## Repository layout

```text
INDEX.md                 Flow, phases, skill catalog
README.md                This file
CHANGELOG.md             Pack version history
scripts/                 validate_pack.py, routing_resolve.py
tests/routing_cases.yml  File routing golden paths
examples/                Smoke checklist for dogfooding
skills/android/          Hub + spoke SKILL.md trees
rules/                   Glob-scoped Cursor rules (optional)
```

## License

MIT — see [LICENSE](LICENSE).
