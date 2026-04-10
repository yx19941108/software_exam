---
Owner: Codex
Task: global-agents-trim
Status: completed
Updated: 2026-03-13
---

# Global AGENTS Trim Report

## What Changed

- Trimmed the global `AGENTS.md` by removing long machine-baseline, command-allowlist, and installation-approval detail sections.
- Added compressed replacement sections:
  - `Environment Detection Rule`
  - `Command Safety Rule`
  - `Installation Approval Rule`
  - `External References`
- Added three external reference documents under `C:\Users\65430\.codex\doc\`.

## Expected Benefits

- Smaller global rule injection per turn
- Better separation between stable behavior rules and machine-specific reference material
- Easier maintenance when machine paths, tool versions, or approval templates change

## Validation Targets

- The new global AGENTS still preserves communication, artifact, onboarding, context, child-agent, engineering, and code-change rules.
- The three external reference files exist.
- The new AGENTS contains explicit trigger conditions and absolute-path references to those files.
