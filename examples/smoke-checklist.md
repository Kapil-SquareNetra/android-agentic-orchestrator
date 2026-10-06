# Smoke checklist (dogfood the pack)

Run after installing skills into `~/.cursor/skills/android/` and optional rules.

1. Invoke **android-orchestrator** with a one-line feature ask; confirm only the hub attaches first.
2. Confirm a Compose screen edit loads `android-compose`, `android-material`, and `android-material-components` (not Maestro/Detekt).
3. Run `python scripts/validate_pack.py` from this repo — must print `OK`.
4. Complete a **bugfix** lane task; status documents skipped FR with reason.
5. Run Detekt + unit tests + (if device available) one Maestro flow; capture commands in final status.
