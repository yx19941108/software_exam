---
Owner: Codex
Task: softwareexam-policy
Status: active
Updated: 2026-05-06
---

# Training Round Policy

## File Placement And Naming

Training-round question sets must be generated under:

`doc/Software-Designer-master/真题/xisai_md/真题训练/`

Unless 游工 explicitly requests a chat-only preview, question delivery for learning rounds, practice rounds, and newly assembled training sets must be persisted to this directory instead of fully printed in chat.

When 游工 does not specify a filename, create or update the appropriate file using these patterns:

- Textbook-chapter rounds: `章节 + 第x轮真题训练`, for example `第4章第三轮真题训练.md`
- Afternoon specialized rounds: `课次 + 第x轮真题训练`, for example `第13课第一轮真题训练.md`

## Hidden-Answer Question Files

In training-round Markdown files:

- Every option of every multiple-choice question must occupy its own line.
- Question images must be embedded directly in the body by default, preferably using relative paths.
- Answers, analyses, and conclusion-level hints must be hidden.
- Composite questions must preserve complete `问题1 / 问题2 / 问题3` structure and must not leak answers.
- Text-answer areas may be blank, but do not provide answer templates that reveal scoring logic.

## Coverage Reporting

When assembling a training round, prioritize coverage across as many relevant knowledge points and question types as the local pool allows. Do not repeatedly select highly similar questions from a small subset unless the local pool forces it.

Coverage-first does not override the local-pool and time-budget constraints. If full coverage is not achievable, report uncovered knowledge points and question types instead of silently narrowing the round.

After every newly assembled training round, report a quantified coverage summary in chat. Include total questions and total blanks or scoring units, covered and uncovered baseline items, coverage percentage, and concrete uncovered points.

The coverage baseline must be evidence-based and should be derived from the local candidate pool actually inspected for the current round. If the baseline is partial because the local pool is sparse or the time budget is exhausted, say so explicitly.

## Drawing-Answer Workflow

Before creating any `.drawio` answer file, decide strictly from question wording whether the answer requires drawing. Do not infer drawing only from the broad problem type such as DFD, database design, or UML.

Create `.drawio` only when the stem explicitly asks the candidate to draw, complete, supplement, modify, or directly edit a diagram, such as `补充 E-R 图`, `完善实体联系图`, `对图进行补充`, `画出修改后的实体间联系和联系类型`, `补充类图/用例图/顺序图/活动图/状态图/通信图`, or equivalent wording.

Do not create `.drawio` when the stem only asks for textual or tabular answers, even if a diagram is shown in the stem. For example, DFD questions asking for `数据流名称 / 起点 / 终点`, entity names, data-store names, relationship names, class names, participant names, use-case names, code blanks, algorithm strategy, complexity, or reason explanations must be answered in Markdown text/table areas unless the stem also explicitly requires diagram completion.

When a training question requires drawing, diagram completion, or direct editing under the criteria above, package the training round as a folder under `doc/Software-Designer-master/真题/xisai_md/真题训练/` rather than leaving only a standalone Markdown file.

The folder name must use the training-round file stem exactly. The Markdown training file remains the question entrypoint and must still hide answers and analyses.

For each drawing-answer question, create an editable `.drawio` answer file in the same folder. The file name pattern is `<training-round-file-stem>-<question-label>.drawio`, for example `第14课第一轮真题训练-训练一.drawio`.

Do not create a duplicate `题干原图.png` in the training folder by default. The original question image should remain referenced from the Markdown file or local source question file.

The `.drawio` file is 游工's answer workspace. It should contain a reasonable editable canvas for completing the diagram and may reference or visually reproduce the necessary question figure only to the extent needed for answering.

Do not modify original question-bank image assets under `题目素材/`. All user-editable drawing-answer artifacts must live under the corresponding training-round folder.
