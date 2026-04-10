---
Owner: Codex
Task: artifact-guide
Status: completed
Updated: 2026-03-13
---

# Agent Artifact Guide

## Storage Policy
- Persistent, versioned artifacts live under `doc/agent/`.
- Temporary or generated working files live under `.agent-temp/`.

## Preferred Task Bundle Layout
- `doc/agent/<task-id>_<YYYYMMDD-HHmmss>/plans/`
- `doc/agent/<task-id>_<YYYYMMDD-HHmmss>/decisions/`
- `doc/agent/<task-id>_<YYYYMMDD-HHmmss>/reports/`
- `doc/agent/<task-id>_<YYYYMMDD-HHmmss>/reviews/`
- `doc/agent/<task-id>_<YYYYMMDD-HHmmss>/handoffs/`

## Naming Convention
- Regular files: `YYYYMMDD_<task-id>_<type>_vNN.<ext>`
- ADR files: `ADR-XXXX_<short-title>.md`
- Allowed `<type>` values: `plan`, `report`, `review`, `handoff`, `note`

## Usage Notes
- Do not store temporary, debug, or throwaway files in `doc/agent/`.
- `.agent-temp/` must remain ignored by Git.
- Each persistent artifact should include metadata headers: `Owner`, `Task`, `Status`, `Updated`.
- Default task bundle directories should use an ASCII `task-id` plus timestamp in the root directory name; put the Chinese title in the document metadata instead of the directory name.
- When resuming work, prefer the latest relevant task bundle first; use legacy flat folders only as fallback for older artifacts.
