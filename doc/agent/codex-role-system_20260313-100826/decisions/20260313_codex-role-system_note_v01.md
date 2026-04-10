---
Owner: Codex
Task: codex-role-system
Status: completed
Updated: 2026-03-13
---

# Codex Role System Decisions

## Title

Global child-agent role system refactor for Codex.

## Confirmed Decisions

- Removed `evidence_collector`.
- Removed `senior_project_manager`.
- Replaced `backend_architect` with `architect`.
- Added `product_manager`, `business_qa_lead`, and `project_reviewer`.
- Kept `frontend_developer`, `senior_developer`, `ui_designer`, and `api_tester`, but rewrote their prompts to remove project-specific framework, path, and script assumptions.
- Adopted milestone-only approval for `architect`.
- Assigned package-level day-to-day coordination to `senior_developer`.
- Adopted task-bundle persistence under `doc/agent/<task-id>_<timestamp>/...`.

## Implemented Global File Set

Prompts:

- `C:\Users\65430\.codex\agency-agents\prompts\architect.md`
- `C:\Users\65430\.codex\agency-agents\prompts\product-manager.md`
- `C:\Users\65430\.codex\agency-agents\prompts\engineering-frontend-developer.md`
- `C:\Users\65430\.codex\agency-agents\prompts\engineering-senior-developer.md`
- `C:\Users\65430\.codex\agency-agents\prompts\design-ui-designer.md`
- `C:\Users\65430\.codex\agency-agents\prompts\testing-business-qa-lead.md`
- `C:\Users\65430\.codex\agency-agents\prompts\testing-api-tester.md`
- `C:\Users\65430\.codex\agency-agents\prompts\project-reviewer.md`

Role configs:

- `C:\Users\65430\.codex\roles\agency-agents\architect.toml`
- `C:\Users\65430\.codex\roles\agency-agents\product-manager.toml`
- `C:\Users\65430\.codex\roles\agency-agents\frontend-developer.toml`
- `C:\Users\65430\.codex\roles\agency-agents\senior-developer.toml`
- `C:\Users\65430\.codex\roles\agency-agents\ui-designer.toml`
- `C:\Users\65430\.codex\roles\agency-agents\business-qa-lead.toml`
- `C:\Users\65430\.codex\roles\agency-agents\api-tester.toml`
- `C:\Users\65430\.codex\roles\agency-agents\project-reviewer.toml`

## Backup Location

- `.agent-temp/codex-role-system-backup-20260313/`
