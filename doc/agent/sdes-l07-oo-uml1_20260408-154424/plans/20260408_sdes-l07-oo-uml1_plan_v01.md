---
Owner: Codex
Task: sdes-l07-oo-uml1
Status: active
Updated: 2026-04-08
---

# 软件设计师 L07《面向对象与 UML I》实施计划

> For Claude: required sub-skill intent already satisfied in-session via documentation workflow and verification workflow; execute this plan directly in the current session.

**Goal:** 基于本轮续课恢复结果，新建一份可独立授课的 `L07` 课案，并同步生成本轮报告与交接单，保证下次会话能从 `L07` 的真实边界继续。

**Architecture:** 以近 10 年本地可核验样本中的 `用例图 + 类图 + 新需求改图` 为锚点，但把本课边界收在 `OO 基础直觉 + UML 用例图/类图识读 + 真题风格练习`。整题化改图和连续案例留给 `L08`，设计模式系统讲授留给 `L09`。

**Tech Stack:** Markdown, Mermaid, `pdfplumber` 本地 PDF 抽取, SoftwareExam 仓库 task-bundle 工件规范

---

### Task 1: 按续课规则恢复 L07 入口

**Goal:** 读取课程总表、L05/L06 报告、L06 练习交接，确认本轮应推进到 `L07`。

**Affected Files:** 无

**Risk:** 如果恢复不完整，会把 `L06` 的拆解训练误报成整题闭环，或者错误回退重讲。

**Verification:** 已读取用户指定的 7 个文件，并核对课程总表与 L06 两份 handoff 的口径一致。

**Rollback:** 无需回滚。

### Task 2: 确认真题锚点与 L07 边界

**Goal:** 用本地真题确认 OO/UML 在本仓库中的稳定问法，并划清 `L07 / L08 / L09` 边界。

**Affected Files:** 无

**Risk:** 若把 `L07` 讲成泛 OO 理论，或把 `L08` 的整题模板、`L09` 的模式识别提前混入，会造成课程分层失真。

**Verification:** 已用 `pdfplumber` 抽取 `2016上 / 2016下 / 2018上 / 2018下` 相关页，确认可支撑：
- 从需求识别参与者与用例
- 从需求或给定图识别类图元素
- 根据新需求改图

**Rollback:** 无需回滚。

### Task 3: 编写 L07 正式课案

**Goal:** 新建 `07_面向对象与UMLI_重写版.md`。

**Affected Files:**
- Create: `doc/Software-Designer-master/课案/07_面向对象与UMLI_重写版.md`

**Risk:** 若把证据不足的内容包装成“逐字官方真题”，或跳过直觉直接堆术语，会违背当前课程规则。

**Verification:** 课案必须包含：
- 学习目标
- 前置知识
- 真题锚点
- Mermaid 图
- 真题风格例题
- 随堂练习
- 课后作业
- 常见错误
- 复盘清单

**Rollback:** 删除新课案文件即可。

### Task 4: 生成本轮报告与交接单

**Goal:** 固化本轮续课恢复结论与 `L07` 的下次会话入口。

**Affected Files:**
- Create: `doc/agent/sdes-l07-oo-uml1_20260408-154424/reports/20260408_sdes-l07-oo-uml1_report_v01.md`
- Create: `doc/agent/sdes-l07-oo-uml1_20260408-154424/handoffs/20260408_sdes-l07-oo-uml1_handoff_v01.md`

**Risk:** 若不把 `L06` 的真实状态和本轮推进理由写清，下次会话又会重复做阶段边界判断。

**Verification:** 报告与交接单必须明确：
- 当前课程进度
- `L06` 的真实状态
- 本轮为什么推进 `L07`
- `L07` 的下一步直接动作

**Rollback:** 删除新增 task-bundle 文件即可。

### Task 5: 最小校验并正式进入 L07

**Goal:** 校验新文件结构后，在对话中用其作为主教学材料开始 `L07`。

**Affected Files:** 无

**Risk:** 如果不做最小校验就开讲，可能出现文件已落地但结构或口径不合规。

**Verification:** 检查文件存在、关键标题存在、报告与交接单状态准确。

**Rollback:** 如发现问题，仅修正本轮新增文件。
