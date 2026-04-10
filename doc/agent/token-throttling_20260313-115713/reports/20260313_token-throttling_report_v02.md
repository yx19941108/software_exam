---
Owner: Codex
Task: token-throttling
Status: completed
Updated: 2026-03-13 12:54:21 +08:00
---

# Token 节流与子 Agent 规则二次优化 Execution Report

## Goal
- 在不新增 `config.toml` 变更的前提下，继续优化全局 `AGENTS.md` 的可执行性。
- 把上一轮的 child agent 原则、token 节流原则、以及治理类变更纪律补成更稳定的默认行为。

## Changes Applied
### 1. Communication Rules
- 增补治理类指令也受“先指出问题并确认”约束。

### 2. Default Token Throttling And Context Hygiene
- 新增高风险、高争议、精度敏感、审计敏感工作不得过度压缩。
- 新增必须保留足够原始证据定位信息的要求。

### 3. Child-Agent Request Mechanism
- 新增申请检查清单：
  - 为什么本地直接做不是更优默认值
  - 建议 child-agent 角色
  - ownership 边界
  - 预期产物
  - 预期收益
- 新增默认不开 child agent 的条件。
- 把效率判断改为净收益判断。

### 4. Code Change Process Rules
- 把规划前置规则扩展到代码之外的持久行为文件，包括配置、全局或仓库级 `AGENTS.md`、持久治理文档等。

## Verification Evidence
- 已回读 `C:\Users\65430\.codex\AGENTS.md` 并确认以下新增规则命中：
  - 治理类指令同样受 challenge-and-confirm 约束
  - 高风险工作不得过度压缩输出
  - child agent 请求必须带检查清单
  - 默认不开 child agent 的典型情形已显式化
  - child agent 判断标准改为净收益
  - 规划前置规则扩展到持久行为文件
- 已检查 `token-throttling_20260313-115713` 任务包中的 `v02` decision / report / handoff 全部存在且 metadata 正确。
- 已检查 `C:\Users\65430\.codex\memories\MEMORY.md` 与 `memory_summary.md` 相关段落，未发现与本轮规则直接冲突的 stale memory。

## Expected Effect
- child agent 不再是“想到就开”，而是先给出边界和收益，再确认。
- 默认节流不再等于默认丢失证据。
- 全局治理文件修改将和代码修改一样，先交代目标、风险、验证、回滚。

## Continuity
- `v01` 是第一次固化 token 节流与 child agent 原则的基线。
- `v02` 是在不改角色链和参数值的前提下，对执行细则做补全。
