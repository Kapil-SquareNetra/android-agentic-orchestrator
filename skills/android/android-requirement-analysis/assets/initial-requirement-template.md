# Initial requirement — {Feature name}

Use this document (or the same sections in chat) to start **android-orchestrator** feature work. If every **Required to start** section is filled, the hub can proceed to FR, impact, architecture, and implementation without waiting for a full `docs/functional-requirements.md` (that doc is produced in the requirement phase).

Replace `{…}` placeholders with your content. **Examples** below use a fictional “appointment scheduling” feature — delete them when you copy this template.

---

## Required to start

### One-line summary

**You write:** What the user gets, in one sentence.

**Example:** Signed-in users can pick a date and book an available appointment slot from the home screen.

---

### Problem / goal

**You write:** Why we are building this; what is wrong or missing today.

**Example:** Users currently call the clinic to book visits. We need self-serve scheduling in the app to reduce support load and show only slots that are actually free.

---

### Primary actor

**You write:** Who uses this feature.

**Example:** Authenticated patient (account with verified email). Not guest users for this slice.

---

### Happy path (user flow)

**You write:** 3–7 numbered steps from the user’s perspective.

**Example:**

1. User opens **Appointments** from the bottom nav.
2. User taps **Book appointment** and sees a calendar for the next 30 days.
3. User selects a date; the app loads time slots for that day.
4. User selects a slot and confirms on a summary screen.
5. User sees a success screen with appointment details and can return to the list.

---

### Must-have acceptance criteria

**You write:** Testable **When / Then** rows (these become FR/AC seeds).

| # | When … | Then … |
|---|--------|--------|
| 1 | *Example:* User selects a date with no available slots | *Example:* An empty state explains no times are open and suggests another date |
| 2 | *Example:* User confirms a valid slot while online | *Example:* Appointment appears in the list sorted by start time, soonest first |
| 3 | *Example:* Slot fetch fails (network error) | *Example:* Error state shows retry; user can change date without crashing |
| 4 | | |
| 5 | | |

---

### In scope (this delivery)

**You write:** What this slice **will** include.

**Example:**

- Calendar + slot picker + confirm flow for one appointment type
- List of upcoming appointments on the appointments tab
- Loading, empty, and error states for list and slot picker

---

### Out of scope (non-goals)

**You write:** What you are **not** doing in this slice.

**Example:**

- Reschedule or cancel (separate story)
- Push notification reminders
- Provider-side calendar admin
- Offline booking without network

---

## Strongly recommended

### Preconditions

**You write:** Auth, data, and platform assumptions.

**Example:**

- Auth: User must be logged in; session token available to API layer
- Data: Network required to load slots and confirm booking; show error if offline on confirm
- Platform: Phone portrait first; tablet can use same layout for MVP

---

### UI states to support

**You write:** What the user should see in each state.

**Example:**

- Loading: Skeleton or spinner on calendar and slot list while fetching
- Empty: No upcoming appointments; no slots on selected date
- Error: Failed to load slots or confirm — message + retry where applicable
- Success / content: Calendar with selectable days; slot chips; confirmation summary

---

### Navigation

**You write:** How the user enters and leaves the flow.

**Example:**

- Entry: Bottom nav → Appointments tab → Book appointment
- Exit / back: Back from summary returns to slot picker; back from list returns to previous tab; success **Done** returns to appointment list

---

### Edge cases (name upfront)

**You write:** Known tricky cases so they are not forgotten in FR/impact.

**Example:**

- User rotates device during slot load (state restored)
- Slot becomes unavailable between select and confirm (show error, refresh slots)
- Session expires during confirm (redirect to login, preserve intent if possible)
- Same-day booking near current time (timezone / clinic rules)

---

### Constraints

**You write:** Reuse, performance, a11y, analytics.

**Example:**

- Design system: Reuse existing `PrimaryButton`, `TopAppBar`, date picker from `:core:designsystem`
- Performance: Slot list paginated or capped per day if API returns many rows
- A11y: Slot chips have content descriptions; errors announced
- Analytics: `appointment_booking_started`, `appointment_booking_confirmed` (names TBD with product)

---

### Priority

**You write:** MVP vs later.

**Example:** P0 MVP — book + list only. P1 — cancel/reschedule.

---

### Open questions

**You write:** Blockers to resolve before implementation (if P0).

**Example:**

- API contract for `GET /slots?date=` — confirmed with backend?
- Maximum bookings per user per day?

*(If none, write “None”.)*

---

## Optional (plan-driven shortcut)

If you already have `docs/implementation-plan.md`, link it here and mark **Plan-driven**. The hub will validate the plan instead of recreating it.

**Example:** `docs/implementation-plan.md` (sprint 3 — appointments)

- Plan path or link:

---

## Handoff

When **Required to start** is complete, invoke **android-orchestrator** with this file or paste the sections into Agent chat. The orchestrator will:

1. Expand into `docs/functional-requirements.md`
2. Produce `docs/requirement-impact.md`
3. Scan the past-miss checklist (`requirement-retrospective.md` is reference only)
4. Continue architecture → plan → implement → quality pipeline
