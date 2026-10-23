# Requirement prompt

Do not read the codebase, write docs, or start implementation.

Reply with one sentence: copy the block, fill every **Required** section, then paste it into Agent chat.

Then output **one** fenced `markdown` block containing the prompt below, character for character. Do not fill placeholders. Do not add a second copy outside the fence.

````markdown
Use **android-orchestrator** for this Android feature. This message is the initial requirement (`docs/initial-requirement.md` sections). With the functional requirements, list test cases that cover them (positive, negative, and edge). Do not implement until I explicitly approve the functional requirements and those test cases.

## Feature name

{Feature name}

## Required to start

### One-line summary

{What the user gets, in one sentence.}

### Problem / goal

{Why we are building this; what is wrong or missing today.}

### Primary actor

{Who uses this feature.}

### Happy path

1. {Step}
2. {Step}
3. {Step}

### Must-have acceptance criteria

| # | When … | Then … |
|---|--------|--------|
| 1 |  |  |
| 2 |  |  |
| 3 |  |  |

### In scope

- {What this slice will include.}

### Out of scope

- {What this slice will not include.}

## Strongly recommended

### Preconditions

- {Auth, data, and platform assumptions.}

### UI states

- Loading:
- Empty:
- Error:
- Content:

### Navigation

- Entry:
- Exit / back:

### Edge cases

- {Known tricky cases.}

### Constraints

- {Design system, performance, accessibility, analytics.}

### Priority

{MVP vs later.}

### Open questions

{Blockers, or "None".}

## Optional — Figma (skip if unused)

| Screen / flow | Figma URL |
|---------------|-----------|
| | |

## Optional — Jira (skip if unused)

| Issue key | Link |
|-----------|------|
| | |

## Plan-driven (optional)

{Path to an existing docs/implementation-plan.md, or leave blank.}
````
