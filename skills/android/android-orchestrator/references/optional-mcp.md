# Optional MCP integrations (Figma, Jira)

Figma and Jira are **never required**. The hub proceeds without them and records **N/A** or **manual** in acceptance when they are absent.

## Detect before use

1. Call dynamic tool discovery with a pattern (`figma`, `jira`, or `atlassian`) or inspect the namespace (`user-Figma`, or your team’s Jira MCP id).
2. If the namespace is missing, in **needsAuth**, or **error**: tell the user once what to install, then continue without blocking the lane.

| Integration | Typical install | If unavailable |
|-------------|-----------------|----------------|
| **Figma** | Cursor **Settings → MCP** → add the [official Figma MCP](https://www.figma.com/developers/api) (or your org’s Figma server). Sign in when prompted. | Skip design compare; note in `docs/acceptance-criteria.md`. |
| **Jira** | Cursor **Settings → MCP** → add a Jira / Atlassian MCP, **or** use [Atlassian CLI](https://developer.atlassian.com/cloud/acli/) (`acli`) on your PATH. | Track the issue key in docs only; no automatic ticket updates. |

Do not install MCP servers or CLI tools without the user’s approval. Do not store API tokens in the repo.

## When the hub loads optional spokes

| Signal in docs or chat | Load |
|------------------------|------|
| `figma.com/design/` (or `/make/`) URL, or “Figma frame” in FR | `android-figma` |
| Jira key (`PROJ-123`), “Jira”, or `acli` | `android-jira` |

Task routing in `task-routing.yml` mirrors these signals.
