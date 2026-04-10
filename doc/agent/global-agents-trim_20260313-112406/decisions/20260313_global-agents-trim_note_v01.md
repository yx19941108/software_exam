---
Owner: Codex
Task: global-agents-trim
Status: completed
Updated: 2026-03-13
---

# Global AGENTS Trim Decision

## Summary

The global `C:\Users\65430\.codex\AGENTS.md` was trimmed to keep high-value behavioral rules while moving machine-specific environment facts, command policy details, and installation approval templates into external reference documents.

## External Reference Files

- `C:\Users\65430\.codex\doc\machine-baseline.md`
- `C:\Users\65430\.codex\doc\command-policy.md`
- `C:\Users\65430\.codex\doc\install-approval-policy.md`

## New Reference Model

The global AGENTS now uses trigger-based references:

- when tool existence depends on machine facts -> read `machine-baseline.md`
- when command-safety judgment matters -> read `command-policy.md`
- when a low-risk install may be justified -> read `install-approval-policy.md`

## Rollback

- Restore `.agent-temp/global-agents-trim-backup-20260313/AGENTS.md.bak`
- Remove the three new files under `C:\Users\65430\.codex\doc\`
