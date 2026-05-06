---
Owner: Codex
Task: softwareexam-policy
Status: active
Updated: 2026-05-06
---

# SoftwareExam Policy Index

This directory holds detailed execution policies referenced by the project `AGENTS.md`.

`AGENTS.md` remains the mandatory routing and priority entrypoint. These files hold longer operating details so the main rule file does not keep growing without control.

## Policy Files

| File | Use When | Required Action |
| --- | --- | --- |
| `lesson-authoring-policy.md` | Writing or updating lesson plans for textbook chapters or afternoon specialized lessons | Read before drafting or modifying lesson-plan bodies. |
| `training-round-policy.md` | Assembling practice rounds, mock exams, hidden-answer question files, or `.drawio` answer workspaces | Read before creating or updating training-round artifacts. |
| `case-grading-policy.md` | Grading software-designer afternoon case-analysis answers | Read before scoring; apply when user challenges a grading result. |

## Governance Rule

Do not add long procedural examples directly to `AGENTS.md` when they belong to one of these policy files. Keep `AGENTS.md` as a compact trigger-and-routing contract.
