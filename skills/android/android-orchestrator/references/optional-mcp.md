# Optional MCP integrations (Figma, Jira)

For **Detekt** and **Maestro**, see [quality-tooling.md](quality-tooling.md) and [setup-guides.md](setup-guides.md).

Figma and Jira are **never required**. The hub proceeds without them and records **N/A** or **manual** in acceptance when they are absent.

## Detect before use

1. Call dynamic tool discovery with a pattern (`figma`, `jira`, or `atlassian`) or inspect the namespace (`user-Figma`, or your team’s Jira MCP id).
2. If the namespace is missing, in **needsAuth**, or **error**: ask the user once (see below), then continue without blocking the lane.

## When asking the user to install

Do **not** send a one-line “please install Figma.” Include the full **Setup guide** from [setup-guides.md](setup-guides.md):

| Tool | Section to share |
|------|------------------|
| Figma MCP | **Figma MCP (Cursor)** |
| Jira MCP or `acli` | **Jira — MCP or Atlassian CLI** |

Then offer: **Set up now** · **Already configured** · **Skip (N/A)**.

| Integration | If unavailable after ask |
|-------------|-------------------------|
| **Figma** | Skip design compare; note in `docs/acceptance-criteria.md`. |
| **Jira** | Track the issue key in docs only; no automatic ticket updates. |

Do not install MCP servers or store API tokens in the repo without user approval.

## When the hub loads optional spokes

| Signal in docs or chat | Load |
|------------------------|------|
| `figma.com/design/` (or `/make/`) URL, or “Figma frame” in FR | `android-figma` |
| Jira key (`PROJ-123`), “Jira”, or `acli` | `android-jira` |

Task routing in `task-routing.yml` mirrors these signals.
