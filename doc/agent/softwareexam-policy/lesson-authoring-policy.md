---
Owner: Codex
Task: softwareexam-policy
Status: active
Updated: 2026-05-06
---

# Lesson Authoring Policy

## Textbook Chapter Lesson Plans

This method is mandatory for the 12 textbook-chapter lesson plans and should be reused chapter by chapter according to the textbook catalog.

After the target textbook chapter is confirmed, first retrieve chapter-matched local morning multiple-choice questions from the local index and Markdown question repository. Do not begin by drafting explanations from memory or old lesson plans.

The chapter lesson plan must be question-driven. Assemble the relevant local objective-question pool first, then derive the lesson-plan structure from real-question coverage.

Extract tested knowledge points from the collected objective questions and assign each question to exactly one primary knowledge point for weighting. Do not count a single question multiple times across knowledge points when calculating weights.

Default weight definition:

`knowledge-point weight = number of objective questions primarily testing that knowledge point / total number of chapter-related objective questions in the selected pool`

Sort knowledge points by weight from high to low. Each knowledge-point section title must display its weight, such as `权值：x/y`, and may include the approximate percentage.

Each knowledge-point section must include beginner-oriented explanation, not outline-only prompts. At minimum, explain what the concept means, why it matters in this chapter, core distinctions or formulas or algorithms, solving procedure, and common traps.

If a term, abbreviation, algorithm name, data structure name, or mechanism name may be unfamiliar to a beginner, explain it in place. Do not leave key terms as labels.

Quality bar: after reading the lesson plan, 游工 should not need to go back to the textbook just to understand the named core knowledge points.

Each knowledge-point section must include 1 to 2 representative objective real-question examples from the local repository. Embed the question stem, options, correct answer, and detailed explanation directly in the lesson plan body. Prefer questions from roughly the most recent 10 years when the local pool allows.

Include a brief chapter-level summary of local objective-question distribution so the ordering and emphasis are evidence-based.

Before finalizing, self-review from a beginner perspective. If a beginner would not understand a named concept, algorithm, distinction, formula, or solving step without opening the textbook, expand the lesson plan.

If the chapter has too few local questions to support a full weight-based breakdown, still follow this method as far as evidence allows and clearly state reduced sample size and lower-confidence points.

## Afternoon Specialized Lesson Plans

This method is mandatory for the 5 afternoon specialized lesson plans from `第13课` to `第17课`.

Each afternoon specialized lesson plan must cover exactly one major afternoon problem type and must not mix multiple major problem types in the same lesson body.

Required body structure:

- 本课定位
- 本课目标
- 前置知识
- 核心考法识别
- 固定答题步骤
- 判分点模板
- 常见失分点
- 过关标准

Afternoon specialized lesson-plan bodies must not include `课后训练`, `本地原题样本`, or any material that directly exposes answers or analyses for paired training questions.

For afternoon specialized lessons, the lesson plan explains methods, templates, and scoring logic. The training-round file provides hidden-answer questions and the answering entrypoint. Keep them separate.
