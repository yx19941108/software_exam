---
Owner: Codex
Task: sdes-l06-db-design
Status: active
Updated: 2026-04-08
---

# 软件设计师 L06《数据库设计》实施计划

> For Claude: required sub-skill intent already satisfied in-session via brainstorming and writing-plans workflow; execute this plan directly in the current session.

**Goal:** 基于当前课程承接状态，新建一份可独立授课的 `L06` 数据库设计下午题课案，并同步生成本轮报告与交接单。

**Architecture:** 以 `2018上` 数据库设计下午题作为主锚点，围绕 `ER 图补全 -> 关系模式补全 -> 弱实体增补与关系模式修改` 三段稳定问法组织整课。课案正文延续当前重写版风格，继续采用“先直觉，再术语，再真题模板，再练习”的结构。

**Tech Stack:** Markdown, Mermaid, 本地 PDF 样本锚点, SoftwareExam 仓库 task-bundle 工件规范

---

### Task 1: 恢复上下文并确认 L06 边界

**Goal:** 明确 `L05` 已基本通过，`L06` 必须是一节下午数据库设计模板课，而不是重复上午数据库基础课。

**Affected Files:** 无

**Risk:** 如果课时边界判断错，会把 `L06` 讲散，和 `L05` 重复。

**Verification:** 已读取 `20260311_sdes-course-plan_plan_v01.md`、`L05` 启动报告、`L05` 练习批改报告与两份交接单。

**Rollback:** 无需回滚。

### Task 2: 提取可用真题锚点

**Goal:** 从本地真题中抓到一套可支撑 `L06` 的真实数据库设计下午题。

**Affected Files:** 无

**Risk:** 当前 PDF 文本层存在编码噪声，若只依赖文本抽取会误判题型。

**Verification:** 已用 `2018上.pdf` 第 `4-5` 页确认：
- 题型核心是数据库设计
- 稳定问法包括 `补 ER 图`、`补关系模式`、`增加弱实体并修改关系模式`

**Rollback:** 无需回滚。

### Task 3: 编写 L06 正式课案

**Goal:** 新建 `06_下午专题II_数据库设计_重写版.md`。

**Affected Files:**
- Create: `doc/Software-Designer-master/课案/06_下午专题II_数据库设计_重写版.md`

**Risk:** 若把证据不足的内容写成“近年逐字真题还原”，会抬高证据强度。

**Verification:** 课案必须包含：
- 学习目标
- 前置知识
- 资料依据
- 真题锚点
- Mermaid 图
- 随堂练习
- 课后作业
- 常见错误
- 复盘清单

**Rollback:** 删除新课案文件即可。

### Task 4: 生成本轮报告与交接单

**Goal:** 把 `L05 -> L06` 的课程承接和当前状态固化到 task bundle。

**Affected Files:**
- Create: `doc/agent/sdes-l06-db-design_20260408-113945/reports/20260408_sdes-l06-db-design_report_v01.md`
- Create: `doc/agent/sdes-l06-db-design_20260408-113945/handoffs/20260408_sdes-l06-db-design_handoff_v01.md`

**Risk:** 若不写清课程承接状态，下次会话又要重复恢复和重新判定。

**Verification:** 报告与交接单都必须明确：
- `L05` 已基本通过
- 当前进入 `L06`
- `L06` 的核心问法与下一步动作

**Rollback:** 删除新增 task-bundle 文件即可。

### Task 5: 最小校验并开始授课

**Goal:** 确认文件落地无误，然后在对话中正式开始 `L06`。

**Affected Files:** 无

**Risk:** 如果未校验就开讲，容易出现“文件已写但结构不合规”的问题。

**Verification:** 检查文件存在、关键标题存在、报告与交接单状态准确。

**Rollback:** 如发现结构问题，修正新增文件后再继续授课。
