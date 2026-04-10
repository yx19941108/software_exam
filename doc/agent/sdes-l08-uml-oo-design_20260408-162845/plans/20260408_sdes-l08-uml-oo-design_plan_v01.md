---
Owner: Codex
Task: sdes-l08-uml-oo-design
Status: active
Updated: 2026-04-08
---

# 软件设计师 L08《UML / OO 设计》实施计划

> For Claude: brainstorming intent and documentation workflow are satisfied in-session; execute this lesson-build plan directly in the current session.

**Goal:** 基于 `L07` 已通过“可继续推进”的验收状态，新建一份可独立授课的 `L08` 下午 OO/UML 固定题模板课案，并同步生成本轮报告与交接单。

**Architecture:** 以 `2018上` 的“用例图 + 分析类图识别”和 `2018下` 的“已有类图 + 新需求 + 改图”为双主锚点，把 `L08` 的主模板收敛到 `读需求 -> 圈参与者/用例 -> 识别类图 -> 新需求改图`。`2016下` 的状态图只作为辅助证据，不抢占主线；设计模式系统讲授继续留给 `L09`。

**Tech Stack:** Markdown, Mermaid, `pdfplumber` 本地 PDF 抽取, SoftwareExam 仓库 task-bundle 工件规范

---

### Task 1: 承接 L07 验收结果并确认可进 L08

**Goal:** 明确 `L07` 已达到“可继续进入 L08”的最低门槛，但仍有术语边界补强项。

**Affected Files:** 无

**Risk:** 若承接错误，会把 `L07` 的遗留问题误报成必须回退重讲，打乱阶段 B 节奏。

**Verification:** 已读取 `L07` 练习批改报告和交接单，确认：
- `L07 主线已建立`
- `可继续进入 L08`
- `类 / 属性 / 操作 / 用例` 边界仍需持续观察

**Rollback:** 无需回滚。

### Task 2: 确认 L08 的真题锚点与主模板边界

**Goal:** 选出能真正支撑 `L08` 的本地下午题样本，并划清与 `L07 / L09` 的边界。

**Affected Files:** 无

**Risk:** 若边界不清，会把 `L08` 写成泛 UML 复习课，或提前混入 `L09` 的模式识别。

**Verification:** 已确认：
- `2018上` 支撑 `用例图 + 分析类图`
- `2018下` 支撑 `新增需求改类图`
- `2016下` 只作为“可能伴随状态图”的补充证据

**Rollback:** 无需回滚。

### Task 3: 编写 L08 正式课案

**Goal:** 新建 `08_下午专题III_UML_OO设计_重写版.md`。

**Affected Files:**
- Create: `doc/Software-Designer-master/课案/08_下午专题III_UML_OO设计_重写版.md`

**Risk:** 若课案不够“模板化”，会继续停留在 `L07` 的识图层，无法建立下午题固定答题框架。

**Verification:** 课案必须包含：
- 学习目标
- 前置知识
- 真题锚点
- 主模板步骤
- Mermaid 图
- 真题风格综合例题
- 连续案例随堂练习
- 课后作业
- 常见错误
- 复盘清单

**Rollback:** 删除新课案文件即可。

### Task 4: 生成本轮报告与交接单

**Goal:** 把 `L07 -> L08` 的承接关系和 `L08` 的课程边界固化到新 task bundle。

**Affected Files:**
- Create: `doc/agent/sdes-l08-uml-oo-design_20260408-162845/reports/20260408_sdes-l08-uml-oo-design_report_v01.md`
- Create: `doc/agent/sdes-l08-uml-oo-design_20260408-162845/handoffs/20260408_sdes-l08-uml-oo-design_handoff_v01.md`

**Risk:** 若不写清 `L08 != L09`，下次会话很容易把设计模式或状态图主线提前混进来。

**Verification:** 报告与交接单都必须明确：
- `L07` 当前真实状态
- `L08` 的主模板
- `L08` 与 `L09` 的边界

**Rollback:** 删除新增 task-bundle 文件即可。

### Task 5: 最小校验并正式开始 L08

**Goal:** 校验新增文件结构与口径，然后在对话中直接用其作为主学习材料开始 `L08`。

**Affected Files:** 无

**Risk:** 若不校验就开讲，可能出现文件已落地但主线表述混乱。

**Verification:** 检查文件存在、关键标题存在、报告与交接单口径准确。

**Rollback:** 如发现问题，仅修正本轮新增文件。
