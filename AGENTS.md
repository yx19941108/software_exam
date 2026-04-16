# SoftwareExam Project AGENTS

## Scope
These rules apply to the current repository `C:\kuguaHome\personal resource\study\book\SoftwareExam`.

## Teaching Baseline
1. Teaching is no longer driven by the existing lesson plans. Future teaching is driven by real questions.
2. Existing old lesson plans do not serve as references. Lesson plans must be regenerated only according to the lesson-plan outline described in `AGENTS.md`, and old lesson plans must not be read.
3. When the user explicitly asks to start a new lesson, the agent must not read or rely on any existing or historical lesson-plan files as teaching references.
4. For a new lesson, the agent must first obtain the corresponding chapter content from the textbook, then screen chapter-matched real questions from both online sources and the local real-question repository.
5. Existing or historical lesson-plan files must not be used as persistence targets.
6. After teaching, the only allowed persistence target for newly generated chapter lesson plans is `C:\kuguaHome\personal resource\study\book\SoftwareExam\doc\Software-Designer-master\课案\真题驱动`.
7. When sourcing or recovering real questions for this project, the agent must use the skill `$softwareexam-question-sourcing` first.
8. The active lesson-plan structure is now `17` plans in total:
   - `12` textbook-chapter lesson plans first
   - then `5` afternoon case-analysis type lesson plans
9. During the textbook-chapter phase, questions should be morning questions only. Do not add afternoon case-analysis questions into chapter-based rounds.
10. Any older rule that implies "only 12 lesson plans in total" or "chapter rounds must include afternoon case-analysis questions" is superseded by the rules above.

## Source And Storage Locations
1. Lesson plans are divided into two phases:
   - textbook Chapters `1` to `12`
   - afternoon case-analysis type plans `13` to `17`
2. All lesson-plan outputs in both phases are stored under `C:\kuguaHome\personal resource\study\book\SoftwareExam\doc\Software-Designer-master\课案\真题驱动`.
3. This `课案\真题驱动` directory is the only allowed persistence location for lesson-plan outputs. Do not write back to old lesson-plan files elsewhere.
4. Local real questions are stored under `C:\kuguaHome\personal resource\study\book\SoftwareExam\doc\Software-Designer-master\真题`.
5. The textbook is `C:\kuguaHome\personal resource\study\book\SoftwareExam\2018软件设计师教程_第5版_-_9787302491224.pdf`.

## Teaching Workflow

### 1. Conversation Start And Question Delivery
1. At the start of each conversation, check the teaching progress.
2. If the user has not made the path explicit, ask whether to continue learning from the current progress or start a new lesson.
3. If the user explicitly asks to start a new lesson, do not ask the path-selection question again. Instead:
   - identify the target textbook chapter for that lesson
   - read the corresponding chapter content from the textbook first
   - use `$softwareexam-question-sourcing` to screen chapter-matched real questions from online sources and the local real-question repository
   - during the textbook-chapter phase, provide morning questions only for that chapter
4. If the user chooses to continue from the current progress:
   - during the textbook-chapter phase, provide morning questions only corresponding to that progress
   - during the afternoon case-analysis phase, provide case-analysis questions corresponding to that progress
5. During the textbook-chapter phase, do not force or append afternoon case-analysis questions into chapter-based rounds.
6. The `5` afternoon case-analysis type lesson plans are a later separate phase that begins only after all `12` textbook chapter lesson plans are completed.
7. Prefer real questions. If no real questions are available, non-real-question materials may be used, but self-created questions are absolutely not allowed.
8. Prioritize questions from approximately the most recent 10 years.
9. If there are not enough questions, do not force the count. Explain that the tested point has a low exam frequency.
10. If some real questions include images or other content that are not easy to show in the chat box, tell the user to view the original question in the corresponding webpage or file and answer there.
11. Score the questions according to the real exam scoring rules:
   - each multiple-choice question is worth 1 point
   - each case-analysis question is worth 15 points
   - if the original source specifies the score for each sub-question, use the original source
   - if the original source does not specify the score for each sub-question, use your inferred score
12. For each round, the total time budget for textbook-positioning, question-searching, and question-assembly must not exceed 15 minutes.
13. If the agent cannot find enough chapter-matched morning questions within that 15-minute budget, it must not force the target count. It must report the exact number found, the missing count, and the reason.

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
