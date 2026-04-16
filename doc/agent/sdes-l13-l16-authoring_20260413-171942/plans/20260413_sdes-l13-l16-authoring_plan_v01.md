---
Owner: Codex
Task: sdes-l13-l16-authoring
Status: active
Updated: 2026-04-13
---

# 软件设计师 L13-L16 课案补齐执行计划

## 目标

- 在不覆写现有 `L01-L12` 基线的前提下，补齐以下 4 份正式课案：
  - `doc/Software-Designer-master/课案/13_上午送分题清扫_重写版.md`
  - `doc/Software-Designer-master/课案/14_上午综合刷题课_重写版.md`
  - `doc/Software-Designer-master/课案/15_下午综合套卷I_重写版.md`
  - `doc/Software-Designer-master/课案/16_全真模拟与考前总复盘_重写版.md`
- 同步补齐本轮进度报告与交接单，避免会话续接再次断档。

## 已确认依据

- 课程总表：`doc/agent/plans/20260311_sdes-course-plan_plan_v01.md`
- 当前正式课案基线：`doc/Software-Designer-master/课案/01_考试全景与得分路线.md`、`02_上午快得分模块I_重写版.md` 至 `12_操作系统_网络_安全_重写版.md`
- 最新 handoff：`doc/agent/sdes-l09-l12-authoring_20260409-164934/handoffs/20260409_sdes-l09-l12-authoring_handoff_v01.md`
- 真题资料边界：`doc/Software-Designer-master/真题/2009上.pdf` 至 `2020下.pdf`

## 范围决策

- 采用用户确认的方案 A：
  - 只补齐缺失的 `L13-L16`
  - 不重写已存在的 `L01-L12`
  - 新增本轮治理材料，不回写旧 bundle

## 执行步骤

### 步骤 1：锁定统一写法与证据口径

- Goal
  - 复用现有重写课案的正式结构、练习样式、真题锚点表述，避免写法漂移。
- Affected Files
  - 只读：`doc/Software-Designer-master/课案/09_设计模式_Java路线_重写版.md`
  - 只读：`doc/Software-Designer-master/课案/12_操作系统_网络_安全_重写版.md`
  - 只读：`doc/Software-Designer-master/真题/`
- Risk
  - 若结构判断不准，新增课案会和现有重写版风格脱节。
- Verification
  - 确认统一包含：课案信息、Mermaid 预览说明、资料依据、当前样本结论、学习目标、前置知识、主体讲解、案例/练习/作业/常见错误/复盘清单。
- Rollback
  - 不涉及写入，无需回滚。

### 步骤 2：编写 L13《上午送分题清扫》

- Goal
  - 将英语、标准化、知识产权、合同法/招投标、职业规范等送分模块整合成一份高频速判课。
- Affected Files
  - 新增：`doc/Software-Designer-master/课案/13_上午送分题清扫_重写版.md`
- Risk
  - 该模块题面分散，若写成名词清单会失去可操作性。
- Verification
  - 确认正文包含“识别信号 -> 速判模板 -> 常见混淆点 -> 严格练习”。
- Rollback
  - 删除新文件并回到未补齐状态。

### 步骤 3：编写 L14《上午综合刷题课》

- Goal
  - 将上午题整卷策略、排除法、时间分配、错题复盘方法固化成一节刷题方法课。
- Affected Files
  - 新增：`doc/Software-Designer-master/课案/14_上午综合刷题课_重写版.md`
- Risk
  - 若只讲技巧、不讲题型归类，容易变成空泛经验贴。
- Verification
  - 确认包含“整卷时间策略 + 高频陷阱归类 + 真实题风格小套题 + 复盘模板”。
- Rollback
  - 删除新文件并回到未补齐状态。

### 步骤 4：编写 L15《下午综合套卷 I》

- Goal
  - 把 DFD、数据库设计、UML/OO、算法代码、设计模式五类固定题型串成一套综合下午课。
- Affected Files
  - 新增：`doc/Software-Designer-master/课案/15_下午综合套卷I_重写版.md`
- Risk
  - 若只做题型列表，会丢失跨题型切换时的答题节奏训练价值。
- Verification
  - 确认包含“整套卷顺序建议 + 每题固定检查表 + 综合案例 + 严格评分口径”。
- Rollback
  - 删除新文件并回到未补齐状态。

### 步骤 5：编写 L16《全真模拟与考前总复盘》

- Goal
  - 产出考前一周可直接执行的模拟、查漏、心态和考试日动作清单。
- Affected Files
  - 新增：`doc/Software-Designer-master/课案/16_全真模拟与考前总复盘_重写版.md`
- Risk
  - 若引入未经核实的时政/报名/准考证细节，会污染稳定课案。
- Verification
  - 只写稳定备考策略，不写需实时联网核验的具体报名安排；包含模拟安排、错题归档、考前动作、考场策略。
- Rollback
  - 删除新文件并回到未补齐状态。

### 步骤 6：补进度报告与交接单

- Goal
  - 把“课案已补齐到 L16”的新状态沉淀到持续化文档。
- Affected Files
  - 新增：`doc/agent/sdes-l13-l16-authoring_20260413-171942/reports/20260413_sdes-l13-l16-authoring_report_v01.md`
  - 新增：`doc/agent/sdes-l13-l16-authoring_20260413-171942/handoffs/20260413_sdes-l13-l16-authoring_handoff_v01.md`
  - 新增：`doc/agent/reports/20260413_sdes-progress_report_v05.md`
  - 新增：`doc/agent/handoffs/20260413_sdes-session05_handoff_v01.md`
- Risk
  - 若仍沿用旧进度台账，会让后续会话误判当前只到 `L03`。
- Verification
  - 明确写出：课案全集已补齐；“已生成课案”不等于“已全部讲授”；下个会话默认从课程推进或刷题/批改模式继续。
- Rollback
  - 删除本轮新增报告与交接，恢复到旧台账。

## 完成判据

1. `课案/` 目录出现 `13-16` 四份新文件。
2. 新课案结构与现有重写版一致。
3. 真题口径继续区分“稳定本地题源锚点”和“保守真题式案例”。
4. `doc/agent` 中新增本轮 plan/report/handoff，且总进度台账更新到 `v05`。
