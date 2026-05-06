---
Owner: Codex
Task: softwareexam-policy
Status: active
Updated: 2026-05-06
---

# Case-Analysis Grading Policy

These rules apply when grading software-designer afternoon case-analysis answers. If they conflict with older grading or explanation wording in `AGENTS.md`, this policy takes precedence for case-analysis grading.

## Evidence Levels

Separate three evidence levels:

- `local question-bank reference answer / explanation`
- `publicly verifiable stem or explanation`
- `simulated grading inference`

Do not present local question-bank answers or inferred scoring as official internal marking rules unless an official source has been verified.

The local question-bank reference answer is the primary scoring baseline, but equivalent expressions must be evaluated by meaning and exam scoring point rather than exact wording alone.

## Diagram And Structured-Answer Inspection

For DFD, database-design, UML, and other diagram-related answers, first identify the user's actual answer elements before scoring:

- element type
- name
- line or edge
- direction
- relationship type
- multiplicity
- data-flow start and end
- primary key
- foreign key
- attribute ownership

When grading a drawing-answer question, read the training Markdown first, inspect the user's saved `.drawio` answer file, and then grade against the local reference answer.

## Scoring Format

Grade by sub-question. For each sub-question, report:

- full score
- user's score
- deduction points
- correct scoring points
- whether the error is severe

Hard errors must be deducted strictly:

- wrong direction
- wrong relationship type
- wrong multiplicity
- external-entity / process / data-store confusion
- missing data flow
- primary-key or foreign-key error
- class / attribute / method placed in the wrong compartment
- UML relationship symbol error

Equivalent-expression handling must be explicit. For example, a DFD data store named `信息存储` may receive credit when its business meaning matches the reference answer; a data flow with correct start and end may receive credit even if its name is slightly nonstandard.

## Score Ranges

When uncertainty exists, report three score estimates:

- `conservative score`: strict wording and notation.
- `normal score`: common scoring-point and reasonable-equivalence grading.
- `lenient score`: the upper bound that still respects hard errors.

Always state that `conservative / normal / lenient` scores are simulated grading ranges, not official internal marking rules.

When a scoring judgment has no official detailed rubric, say it is inferred from the local reference answer and common scoring-point practice. Do not say an answer definitely receives zero or full credit unless the evidence supports that certainty.

If 游工 challenges a grading result, re-check the stem, local reference answer including answer images, and user's original Markdown or drawio answer. If the prior grading was wrong, correct it directly and update the score.
