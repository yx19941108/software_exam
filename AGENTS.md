# SoftwareExam Project AGENTS

## Scope
These rules apply to the current repository `C:\kuguaHome\personal resource\study\book\SoftwareExam`.

## Teaching Baseline
1. Teaching is no longer driven by the existing lesson plans. Future teaching is driven by real questions.
2. Existing old lesson plans do not serve as references. Lesson plans must be regenerated only according to the lesson-plan outline described in `AGENTS.md`, and old lesson plans must not be read.
3. When the user explicitly asks to start a new lesson, the agent must not read or rely on any existing or historical lesson-plan files as teaching references.
4. For a new lesson, the agent must first obtain the corresponding chapter content from the textbook, then screen chapter-matched real questions through the local question-bank index and the local Markdown real-question repository first. If that local path is insufficient, it must consult 游工 before expanding to online sources.
5. For textbook chapter positioning and directory lookup, the agent must first use the persisted textbook-catalog Markdown instead of repeatedly trying to extract the local PDF table of contents.
6. The local PDF remains the canonical local textbook file, but it is not the default entrypoint for directory discovery. Use it for chapter content lookup only after the target chapter has already been identified through the catalog reference or another confirmed readable source for the same fifth-edition textbook.
7. Existing or historical lesson-plan files must not be used as persistence targets.
8. After teaching, the only allowed persistence target for newly generated chapter lesson plans is `C:\kuguaHome\personal resource\study\book\SoftwareExam\doc\Software-Designer-master\课案\真题驱动`.
9. For day-to-day question lookup, lesson question assembly, and in-repo real-question retrieval, the agent must first use the local question-bank index `doc/Software-Designer-master/真题/xisai_md/xisai_md_总索引.md`, then search the local Markdown real-question repository under `doc/Software-Designer-master/真题/xisai_md/题目`.
10. If the local index and local Markdown real-question repository cannot satisfy the current question requirement, the agent must not automatically expand to new online sources. It must first consult 游工, explain the gap, and provide handling options.
11. The skill `$softwareexam-question-sourcing` is no longer the default first step for normal teaching-time question lookup. It is reserved for question-bank expansion, source recovery, or other online sourcing work that 游工 has explicitly requested or approved after the local index/local repository path is exhausted.
12. The active lesson-plan structure is now `17` plans in total:
   - `12` textbook-chapter lesson plans first
   - then `5` afternoon case-analysis type lesson plans
13. During the textbook-chapter phase, questions should be morning questions only. Do not add afternoon case-analysis questions into chapter-based rounds.
14. Any older rule that implies "only 12 lesson plans in total" or "chapter rounds must include afternoon case-analysis questions" is superseded by the rules above.

## Source And Storage Locations
1. Lesson plans are divided into two phases:
   - textbook Chapters `1` to `12`
   - afternoon case-analysis type plans `13` to `17`
2. All lesson-plan outputs in both phases are stored under `C:\kuguaHome\personal resource\study\book\SoftwareExam\doc\Software-Designer-master\课案\真题驱动`.
3. This `课案\真题驱动` directory is the only allowed persistence location for lesson-plan outputs. Do not write back to old lesson-plan files elsewhere.
4. Local real questions are stored under `C:\kuguaHome\personal resource\study\book\SoftwareExam\doc\Software-Designer-master\真题`.
5. The textbook is `C:\kuguaHome\personal resource\study\book\SoftwareExam\2018软件设计师教程_第5版_-_9787302491224.pdf`.
6. The persisted textbook-catalog reference is `C:\kuguaHome\personal resource\study\book\SoftwareExam\doc\agent\sdes-textbook-catalog_20260417-181907\reports\20260417_sdes-textbook-catalog_report_v01.md`.
7. This textbook-catalog reference is the default source for chapter directory lookup, chapter numbering confirmation, and quick textbook navigation.
8. The local question-bank index is `C:\kuguaHome\personal resource\study\book\SoftwareExam\doc\Software-Designer-master\真题\xisai_md\xisai_md_总索引.md`.
9. The primary local Markdown real-question repository is `C:\kuguaHome\personal resource\study\book\SoftwareExam\doc\Software-Designer-master\真题\xisai_md\题目`.

## Teaching Workflow

### 1. Conversation Start And Question Delivery
1. At the start of each conversation, check the teaching progress.
2. If the user has not made the path explicit, ask whether to continue learning from the current progress or start a new lesson.
3. If the user explicitly asks to start a new lesson, do not ask the path-selection question again. Instead:
   - identify the target textbook chapter for that lesson
   - first use `doc/agent/sdes-textbook-catalog_20260417-181907/reports/20260417_sdes-textbook-catalog_report_v01.md` to confirm the correct chapter number, chapter title, and section range
   - do not spend repeated effort trying to extract the local PDF directory before chapter identification is complete
   - after the chapter is confirmed, read the corresponding chapter content from the textbook; if the local PDF body is unreadable in the current environment, use another confirmed readable source for the same fifth-edition textbook
   - first consult `doc/Software-Designer-master/真题/xisai_md/xisai_md_总索引.md`
   - then search the local Markdown real-question repository under `doc/Software-Designer-master/真题/xisai_md/题目` for chapter-matched real questions
   - if the local index/local Markdown repository still cannot satisfy the question requirement, consult 游工 first and provide handling options before using `$softwareexam-question-sourcing` or any new online source
   - during the textbook-chapter phase, provide morning questions only for that chapter
4. If the user chooses to continue from the current progress:
   - during the textbook-chapter phase, provide morning questions only corresponding to that progress
   - during the afternoon case-analysis phase, provide case-analysis questions corresponding to that progress
5. During the textbook-chapter phase, do not force or append afternoon case-analysis questions into chapter-based rounds.
6. The `5` afternoon case-analysis type lesson plans are a later separate phase that begins only after all `12` textbook chapter lesson plans are completed.
7. Prefer real questions. If no real questions are available, non-real-question materials may be used, but self-created questions are absolutely not allowed.
8. Prioritize questions from approximately the most recent 10 years.
9. If there are not enough questions, do not force the count. Explain that the tested point has a low exam frequency.
10. Unless 游工 explicitly requests a chat-only preview, assembled question sets for teaching or training rounds must not be fully delivered in the chat box. They must be written to the training-round directory first, and the chat should only provide the target file path, a brief summary, and answering instructions.
11. If 游工 explicitly requests a chat-only preview and some real questions include images or other content that are not easy to show in the chat box, tell the user to view the original question in the corresponding webpage or file and answer there.
12. Score the questions according to the real exam scoring rules:
   - each multiple-choice question is worth 1 point
   - each case-analysis question is worth 15 points
   - if the original source specifies the score for each sub-question, use the original source
   - if the original source does not specify the score for each sub-question, use your inferred score
13. For each round, the total time budget for textbook-positioning, question-searching, and question-assembly must not exceed 15 minutes.
14. If the agent cannot find enough chapter-matched morning questions within that 15-minute budget, it must not force the target count. It must report the exact number found, the missing count, and the reason.

### 1B. Textbook Chapter Lesson-Plan Authoring Method
1. This method is mandatory for the `12` textbook-chapter lesson plans and should be reused chapter by chapter according to the textbook catalog.
2. After the target textbook chapter is confirmed, the agent must first retrieve the chapter-matched local morning multiple-choice questions from the local index and the local Markdown question repository. Do not begin by drafting explanations from memory or from old lesson plans.
3. The chapter lesson plan must be question-driven. The agent should first assemble the relevant local objective-question pool for that chapter, then derive the lesson-plan structure from the real question coverage.
4. The agent must extract the tested knowledge points from the collected objective questions and assign each question to exactly one primary knowledge point for weighting purposes. Do not count a single question multiple times across different knowledge points when calculating weights.
5. The default weight definition is: `knowledge-point weight = number of objective questions primarily testing that knowledge point / total number of chapter-related objective questions in the selected pool`.
6. The lesson plan must sort knowledge points by weight from high to low. Heavier knowledge points must appear earlier and lighter knowledge points later.
7. Each knowledge-point section title must explicitly display its weight in a clear form such as `权值：x/y` and may also include the approximate percentage when helpful.
8. Each knowledge-point section must include detailed beginner-oriented explanation, not outline-only prompts. At minimum, it should cover:
   - what the concept means
   - why it matters in this chapter
   - the core distinctions, formulas, algorithms, or judgment rules involved
   - a recommended solving procedure
   - common traps or easy-mistake points
9. If the section mentions a term, abbreviation, algorithm name, data structure name, or mechanism name that a beginner may not already understand, the lesson plan must explain it in place. Do not leave key terms as unexplained labels.
10. The quality bar is: after reading the lesson plan, the user should not need to go back to the textbook just to understand the core knowledge points named in the lesson plan.
11. Each knowledge-point section must include `1` to `2` representative objective real-question examples from the local repository showing how that knowledge point is tested.
12. Real-question examples must be embedded directly in the lesson plan body. Do not only reference a filename and question number. Include:
   - the question stem
   - the options
   - the correct answer
   - a detailed explanation, preferably including why the correct option is correct and why the wrong options are wrong when that adds teaching value
13. When the local repository contains enough questions, representative examples should preferentially come from roughly the most recent `10` years. If older questions are used, prefer them only when they better cover a high-value knowledge point.
14. The lesson plan should also include a brief chapter-level summary of the local objective-question distribution so the ordering and emphasis are evidence-based rather than impression-based.
15. The agent must self-review the lesson plan from a beginner perspective before finalizing it. If a beginner reader would still not understand a named concept, algorithm, distinction, formula, or solving step without opening the textbook, the lesson plan is not complete and must be expanded before delivery.
16. If a chapter has too few local questions to support a full weight-based breakdown, the agent must still follow this method as far as the evidence allows, clearly state the reduced sample size, and explain which knowledge points therefore have lower confidence.

### 1A. Local Question-Bank Lookup Workflow
1. When the task is to search, retrieve, assemble, or reuse real questions for teaching, practice, or mock-question selection, the agent must first open and use `doc/Software-Designer-master/真题/xisai_md/xisai_md_总索引.md` as the primary entrypoint.
2. After locating candidate files through the index, the agent must search inside the local Markdown real-question repository under `doc/Software-Designer-master/真题/xisai_md/题目`.
3. The local index plus local Markdown repository is the default and preferred path for question retrieval in this project.
4. If the local index/local Markdown repository does not contain enough suitable questions, the agent must pause and consult 游工 with a brief gap summary and concrete options, instead of silently switching to online sourcing.
5. Only after 游工 explicitly approves expansion beyond the local index/local repository may the agent use `$softwareexam-question-sourcing` or other online sourcing paths.

### 1C. Training Round File Workflow
1. Training-round question sets must be generated under `doc/Software-Designer-master/真题/xisai_md/真题训练/`.
2. Unless 游工 explicitly requests a chat-only preview, question delivery for learning rounds, practice rounds, and newly assembled training sets must be persisted to this directory instead of being fully printed in the chat box.
3. When 游工 does not specify a filename but the task is to assemble a round of questions, the agent must create or update the appropriate file in this directory using the `章节 + 第x轮真题训练` naming pattern, for example `第4章第三轮真题训练.md`.
4. In training-round Markdown files, every option of every question must occupy its own line.
5. In training-round Markdown files, question images must be embedded directly in the body by default, preferably using relative paths.
6. If 游工 specifies a training-round file as the grading source, the agent must read that file first and grade strictly against its contents.
7. Composite questions must preserve the complete `问题1 / 问题2 / 问题3` structure and must not leak answers in the prompt.

### 2. Explanation After The User Answers
1. After the user answers, provide detailed knowledge-point explanations for:
   - the questions the user got wrong
   - the questions the user explicitly marked as not knowing and asked to be explained
2. Use the following format for multiple-choice questions:
   - `题干(正确答案)`
   - `4选项`
   - `我的答案，你的解析讲解。`
3. Use the following format for case-analysis questions:
   - complete question stem
   - the user's answer to each sub-question
   - the correct answer to each sub-question
   - knowledge-point explanation

### 3. Lesson-Plan Persistence And Progression
1. After the user states that they understand the explanation, persist the explained knowledge points into the lesson plan.
2. Then determine the next step based on the user's correctness rate:
   - if it is greater than 75%, ask the user whether to enter the next round of learning
   - if it is less than or equal to 75%, recommend that the user continue practicing real questions for the same chapter, unless the user explicitly requires a temporary skip

### 4. Gap-Filling Round After 17 Lesson Plans
1. After all `17` lesson plans are completed, enter the real-question gap-filling round.
2. In the real-question gap-filling round, for:
   - the questions the user got wrong
   - the questions the user requested to be explained
3. After the user states that they understand the explanation, if the corresponding knowledge point is not already in the lesson plan, append it to the lesson plan of the corresponding chapter. Do not overwrite existing content.

### 5. Wrong-Question Collection Rule
1. When the user makes mistakes on questions of the same knowledge point 2 times or more, first ask whether to add them to the wrong-question collection.
2. If the user confirms, add a new wrong-question section to the lesson plan of the corresponding chapter and write the corresponding question into it.
3. If the corresponding question contains images, code blocks, or other content that is not suitable for direct inclusion in the lesson plan, paste the real-question link and index so that the user can locate the original question.
