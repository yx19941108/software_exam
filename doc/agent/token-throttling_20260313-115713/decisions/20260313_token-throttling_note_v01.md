---
Owner: Codex
Task: token-throttling
Status: completed
Updated: 2026-03-13 11:57:13 +08:00
---

# Token 节流固化方案（平衡型）最终版 Decision Note

## Scope
- 本任务包只记录本次 token 节流固化方案，与既有 `codex-role-system`、`global-agents-trim` 任务包分离。
- 目标是同时固化配置项、全局行为规则、子 agent 申请机制，以及可续跑的 handoff。

## Confirmed Decisions
1. `C:\Users\65430\.codex\config.toml` 仅调整两项：
   - `tool_output_token_limit = 12000`
   - `model_auto_compact_token_limit = 350000`
2. 除上述两项外，其余相关配置保持原值，不借机清理或重排其他段落。
3. `C:\Users\65430\.codex\AGENTS.md` 新增默认 token 节流与上下文治理规则，核心行为为：
   - 工具输出默认摘要化，只保留结论、关键证据行、下一步
   - 默认不全文回读文件，只读关键段、关键行、关键配置项
   - 默认不生成过程性长文档，只保留最终必要产物
   - 默认 commentary 降频
   - 长任务阶段边界默认生成 handoff，并强烈建议切新会话
   - 不因生成 handoff 而强制终止当前会话
   - 用户可显式覆盖全文输出、不切会话、不压缩工具输出、不生成 handoff
4. `C:\Users\65430\.codex\AGENTS.md` 同时固化子 agent 申请机制：
   - 用户主动要求开启子 agent 时，先评估、说明理由、请求确认
   - 用户未提及时，如判断更优，也可主动申请
   - 固定评估维度为上下文是否更干净、腐化风险是否更小、任务规模是否值得拆分、效率是否提升、是否有独立审查或并行收益

## Non-Goals
- 不修改全局角色链定义。
- 不调整其他模型、provider、memory、sandbox、MCP 配置。
- 不强制结束当前会话。

## Expected Operating Effect
- 默认降低工具输出与 commentary 对上下文的占用。
- 把长任务拆段和 handoff 变成默认动作，但仍保留用户覆盖权。
- 把子 agent 从“直接开”改为“先评估、再申请、后启用”的显式机制。
