---
Owner: Codex
Task: token-throttling
Status: completed
Updated: 2026-03-13 12:54:21 +08:00
---

# Token 节流与子 Agent 规则二次优化 Decision Note

## Scope
- 本文记录同一 `token-throttling_20260313-115713` 任务包下的第二轮全局 `AGENTS.md` 治理优化。
- 本轮目标不是再改 `config.toml`，而是把上一轮已固化的原则补成更可执行的默认规则。

## Confirmed Decisions
1. `Communication Rules` 中的“先指出明显问题并确认”规则，明确扩展到治理和流程类指令，包含：
   - 开启 child agent
   - 跳过验证
   - 不生成 handoff
   - 强制过度压缩或过度展开输出
2. `Default Token Throttling And Context Hygiene` 增加高风险例外：
   - 高风险、高争议、精度敏感、审计敏感任务不得过度摘要化
   - 此类任务必须保留足够原始证据定位信息
3. `Child-Agent Request Mechanism` 从“只有评估维度”升级为“评估维度 + 申请检查清单 + 默认不开条件”。
4. child agent 的效率判断改为净收益判断，必须把委派、回收、审查、集成成本算进去，而不是只看局部执行速度。
5. `Code Change Process Rules` 扩展到所有会改变长期行为的持久文件，而不再只限于代码文件。

## Chosen Defaults
- child agent 申请采用检查清单，不采用固定模板。
- 默认不开 child agent 的情形显式化，但仍允许用户确认后例外处理。
- 默认压缩仍成立，但准确性、可审计性和证据保留优先级更高。

## Non-Goals
- 不修改全局 child-agent 角色链。
- 不增加新的 `config.toml` 参数。
- 不把 `AGENTS.md` 改成重型 SOP 或固定话术模板。
