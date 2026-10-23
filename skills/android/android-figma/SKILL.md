---
name: android-figma
description: >-
  Optional Figma design context and visual acceptance for Android Compose UI.
  Use when docs include a Figma URL, at UI implementation, or at acceptance
  to compare device or Maestro screenshots against Figma.
disable-model-invocation: true
---

# Figma (optional)

## Purpose

Keep UI work aligned with design files when the team uses Figma. **Acceptance** may compare the running app to the referenced frame.

## When to load

- Requirement or FR lists a Figma link.
- Implementation touches screens that map to a Figma node.
- **Acceptance** phase when `docs/functional-requirements.md` (or initial requirement) still lists Figma URLs.

Not for logo-only or token-only mentions with no frame to compare.

## MCP availability

Follow [optional-mcp.md](../android-orchestrator/references/optional-mcp.md). If Figma MCP is missing, ask the user once and include the **Figma MCP (Cursor)** section from [setup-guides.md](../android-orchestrator/references/setup-guides.md) ([Figma help](https://help.figma.com/hc/en-us/articles/39889260656407-Cursor-and-Figma-Set-up-the-MCP-server)). Offer skip → record **Figma compare: skipped (MCP not installed)** in acceptance. Do not block delivery.

When available, use the **Figma** dynamic namespace (often `user-Figma`). Inspect tool schemas before calling. For `use_figma` / design reads, follow the server’s session workflow (`create_session` with `fileKey`, then file tools).

## Inputs

- Figma URLs and optional node ids from docs (see templates).
- Screen list from FR / plan.
- Maestro MCP, mobile MCP, or Compose UI capture for app screenshots.

## Outputs

- Design notes in FR or plan (components, spacing, states) when read at plan/impl.
- **Design verification** rows in `docs/acceptance-criteria.md` at acceptance.

## Rules

### URL parsing

- `figma.com/design/:fileKey/...?node-id=1-2` → `nodeId` `1:2` (replace `-` with `:` in the id segment).
- Branch URLs: use branch key as `fileKey` when the URL indicates a branch.

### Implementation

- Prefer project design-system components over raw Figma export paste.
- Load design context once per file or screen; do not replace FR approval.

### Acceptance (visual compare)

When Figma MCP is available and a frame is linked for the screen:

1. Capture **Figma**: `get_screenshot` (or equivalent) for the linked `nodeId`.
2. Capture **app**: same screen state on emulator or device (Maestro `take_screenshot` / mobile MCP / instrumented screenshot). Use the same theme and content as the AC row (loading vs content, etc.).
3. **Compare**: layout, hierarchy, typography roles, primary actions, and visible states. List **match**, **minor drift** (spacing, copy), or **mismatch** (missing control, wrong flow).
4. Record in acceptance: frame URL, screenshot sources, verdict, and user confirmation if mismatches remain.

If MCP works but the device is unavailable, record **blocked for visual compare** and fall back to Compose UI tests plus Figma screenshot review in chat.

## Dependencies

- `android-compose`
- `android-maestro`
- `android-testing`

## Validation

- Every linked Figma frame used for UI has either a compare row at acceptance or an documented skip reason.

## Anti-patterns

- Treating Figma MCP output as the product spec (FR and approved test cases still win).
- Skipping FR approval because a Figma file exists.
- Committing Figma export assets or tokens that belong in `.gitignore`.
