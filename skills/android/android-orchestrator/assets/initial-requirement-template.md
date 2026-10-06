# Initial requirement — {Feature name}

Copy into your project as `docs/initial-requirement.md` or fill the same sections in chat, then run **android-orchestrator**.

**Full template with examples:** `~/.cursor/skills/android/android-requirement-analysis/assets/initial-requirement-template.md`

## Required to start

| Section | You fill in | Example (appointment booking) |
|---------|-------------|-------------------------------|
| One-line summary | One sentence outcome | User picks a date and books an available slot from the app |
| Problem / goal | Why now | Replace phone booking with self-serve scheduling |
| Primary actor | Who | Logged-in patient |
| Happy path | 3–7 steps | Appointments tab → Book → pick date → pick slot → confirm → success |
| Must-have AC | When / Then table | When no slots on date → empty state; When confirm succeeds → list sorted by start time |
| In scope | This slice | Calendar, slots, confirm, upcoming list |
| Out of scope | Non-goals | Cancel, reminders, admin calendar |

## Recommended before implement

| Section | Example |
|---------|---------|
| Preconditions | Logged in; network for book; phone MVP |
| UI states | Loading skeleton; empty no slots; error + retry |
| Navigation | Entry from Appointments tab; back preserves list |
| Edge cases | Slot taken at confirm; session expiry |
| Priority | P0 book+list; P1 cancel |

## Plan-driven

Link `docs/implementation-plan.md` if the plan already exists — hub validates, does not rewrite a sufficient plan.
