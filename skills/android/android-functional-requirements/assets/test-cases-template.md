# Test cases — {Feature name}

Drafted with `docs/functional-requirements.md`. Both stay **DRAFT** until the user approves the functional requirements.

| TC ID | FR ID | Category | Title | Preconditions | Test data | Steps | Expected result |
|-------|-------|----------|-------|---------------|-----------|-------|-----------------|
| TC-1 | FR-1 | Positive | | | | | |
| TC-2 | FR-1 | Negative | | | | | |
| TC-3 | FR-1 | Negative | | | | | |
| TC-4 | FR-1 | Edge | | | | | |
| TC-5 | FR-1 | Edge | | | | | |

**Category** is one of:

- **Positive** — a valid case that should succeed.
- **Negative** — one row per invalid condition. The app rejects it and does not apply the change.
- **Edge** — one row per side of a limit, and one row per unusual specified condition (empty, exact minimum, offline, expired session).

Add rows until every distinct condition has its own case. The sample rows above are a starting shape, not a limit of one Negative and one Edge.

## Coverage check

- Every FR ID has at least one Positive row.
- Every distinct invalid condition has its own Negative row.
- Every boundary side and every unusual condition the FR names has its own Edge row. If an FR has no limit or unusual condition, say so instead of inventing one.
- Each row has concrete test data and one result you can observe.
