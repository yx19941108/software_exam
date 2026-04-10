---
Owner: Codex
Task: codex-role-system
Status: completed
Updated: 2026-03-13
---

# Codex 子 Agent 调用指南

## 目的

这份文档给出当前全局角色系统的实际调用方式，重点回答两个问题：

1. 你该怎么跟我说，才能稳定调起指定角色。
2. 这些角色之间会不会自动互相调起。

## 当前可用角色

| 中文名称 | role id | 主要职责 |
| --- | --- | --- |
| 产品经理 | `product_manager` | 输出需求文档，定义功能要求、数据可见边界、完整流程链路 |
| 架构师 | `architect` | 审需求基线、出技术方案、拆工作包、审测试摘要、终审签发 |
| UI 设计师 | `ui_designer` | 在架构确认后输出界面结构、状态和交互说明 |
| 前端开发 | `frontend_developer` | 实现前端页面、交互、联调与前端验证 |
| 资深开发 | `senior_developer` | 承接复杂实现和工作包级日常协调 |
| 业务 QA 总控 | `business_qa_lead` | 输出测试用例、自动化测试方案并执行全流程测试 |
| API 测试专员 | `api_tester` | 接口专项测试、契约和接口风险验证 |
| 项目审查员 | `project_reviewer` | 对架构师确认过的内容再审，并与架构师进行二次讨论 |

## 默认协作链路

当前默认链路是：

`product_manager -> architect -> ui_designer -> frontend_developer / senior_developer -> business_qa_lead -> api_tester as needed -> project_reviewer -> architect`

含义是：

- `product_manager` 先把需求写清楚。
- `architect` 审需求并给出技术方案。
- `ui_designer` 只在架构确认后启动。
- `frontend_developer` 和 `senior_developer` 负责实现。
- `business_qa_lead` 负责全流程测试，需要时再调 `api_tester`。
- `project_reviewer` 在最终落盘前做再审。
- `architect` 做最终签发。

## 自动调起规则

这些角色不是后台常驻进程，也不是固定 BPM 节点。

更准确的说法是：

- 它们可以被我编排调起。
- 它们不会在没有上下文和明确目标时自己无条件串行执行。
- 任务小的时候，我通常不会强行拉整条链路。
- 任务复杂、你又明确要求按链路推进时，我会按角色顺序组织它们。

最稳的使用方式是：

- 明确写出 `role id`
- 明确写目标
- 明确写边界
- 明确写输出
- 明确写“是否允许继续调其他角色”

## 最短可用模板

```text
请用 `角色ID` 处理这个任务。
目标：...
边界：...
输出：...
```

例如：

```text
请用 `product_manager` 处理这个任务。
目标：把我下面这段描述整理成正式需求文档。
边界：只做需求，不做技术方案。
输出：功能要求、数据可见边界、完整流程链路、异常流程、验收口径。
```

## 常用调用方式

### 1. 只调单个角色

适合你已经知道想让谁干活的时候。

```text
请只用 `architect` 处理这个需求。
目标：审核需求并给出技术方案。
边界：先不要调起 `ui_designer` 和测试角色。
输出：技术方案、关键风险、工作包拆解。
```

### 2. 先跑前两级

适合需求还没定，不想太早进入实现。

```text
按 `product_manager -> architect` 先推进这个需求。
目标：先把需求基线和技术方案定下来。
边界：不要启动 `ui_designer`、开发角色、测试角色。
输出：需求文档和技术方案。
```

### 3. 完整链路推进

适合一个新需求从需求到最终审查都走一遍。

```text
按完整链路推进这个需求：
`product_manager -> architect -> ui_designer -> frontend_developer / senior_developer -> business_qa_lead -> api_tester as needed -> project_reviewer -> architect`

需求：xxx

要求：
1. 由你决定何时调起下一个角色
2. 不要跳过 `architect` 审核
3. 最后由 `architect` 定稿
4. 每个阶段先给我阶段摘要
```

### 4. 只走测试链

适合功能已经实现，你只想做测试和复核。

```text
请用 `business_qa_lead` 为这个功能输出测试用例、自动化测试方案并执行测试。
如果遇到接口专项问题，再调用 `api_tester`。
测试结论先提交给 `architect` 审核。
```

### 5. 只做最终审查

适合方案和测试都已有，你只要最后再过一轮。

```text
请用 `project_reviewer` 对 `architect` 已确认的内容做再审。
要求：
1. 聚焦可落地性、遗漏和风险
2. 和 `architect` 再讨论一次
3. 不改最终签发权，最终仍由 `architect` 定稿
```

## 推荐写法

如果你想要结果稳定，建议每次都补这 4 项：

- `目标`：你到底想解决什么问题
- `边界`：先不要做什么，或不能碰什么
- `输出`：你要文档、方案、代码、测试报告，还是审查意见
- `调度权限`：是否允许它继续调其他角色

推荐句式：

```text
请用 `architect` 处理这个任务。
目标：...
边界：...
输出：...
允许继续调度：是/否
```

## 什么时候我会自动继续调度

如果你已经明确说：

- “按完整链路推进”
- “由你决定何时调起下一个角色”
- “按架构师审批链走完”

那我就会更主动地继续调度后续角色。

如果你没有明确说，我会倾向保守：

- 先做当前最必要的角色
- 不默认把整条链路都跑一遍
- 避免无谓扩大范围

## 角色调度上的三个建议

### 建议 1：大需求用链路，小需求点名

- 新功能、新业务流：用完整链路
- 单一方案评审：点 `architect`
- 只做需求澄清：点 `product_manager`
- 只做测试：点 `business_qa_lead`

### 建议 2：不要把“是否能改代码”说漏

如果你只想先分析，不要默认我进入实现，最好直接写：

```text
先不要改代码。
```

如果你已经允许执行，再写：

```text
可以进入实现。
```

### 建议 3：要并行时直接说

例如：

```text
请并行使用这几个角色：
1. `ui_designer` 做界面方案
2. `architect` 审技术边界
3. `business_qa_lead` 先列测试关注点

要求：
- 先各自独立输出
- 最后再汇总冲突点
```

## 直接可复制的示例

### 示例 A：从零开始做需求

```text
按 `product_manager -> architect` 先推进这个需求。

需求：
我要做一个 xxx 功能。

要求：
1. `product_manager` 先输出正式需求文档
2. `architect` 审需求并给出技术方案
3. 先不要调起 `ui_designer` 和开发角色
4. 输出给我文档和方案摘要
```

### 示例 B：进入设计和开发

```text
在需求和方案已经确认的前提下，继续推进：
`ui_designer -> frontend_developer / senior_developer`

要求：
1. 先由 `ui_designer` 出界面和状态说明
2. 再由你决定哪些工作分给 `frontend_developer`
3. 哪些工作分给 `senior_developer`
4. 可以改代码
```

### 示例 C：做完整验收

```text
请从测试阶段开始推进：
`business_qa_lead -> api_tester as needed -> project_reviewer -> architect`

要求：
1. 先出测试用例和自动化测试方案
2. 再执行测试
3. 接口专项问题交给 `api_tester`
4. 最后由 `project_reviewer` 再审
5. 最终由 `architect` 定稿
6. 先不要省略任何审查环节
```

## 一句话结论

最稳的用法不是问“你自己会不会调”，而是直接说：

```text
按哪个角色或哪条链路推进，目标是什么，边界是什么，输出是什么，是否允许继续调其他角色。
```

这样最不容易跑偏。
