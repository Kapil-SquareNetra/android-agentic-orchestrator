# New Android project — workflow integration

Before applying this workflow to a project, inspect:

- Project structure and Gradle modules
- Existing architecture and dependency direction
- Design system and navigation setup
- Testing layout (`test`, `androidTest`, Maestro flows)
- Build variants and CI/CD
- Detekt configuration
- Existing Cursor rules and skills

**Integrate** the universal workflow; **do not blindly replace** working architecture.

Copy optional routing from `assets/cursor-routing/` to the project `.cursor/routing/` if the team wants a visible mirror of hub routing.

Use `assets/AGENTS.md` in the project root when the team wants a simple hub pointer.
