---
Owner: Codex
Task: token-throttling
Status: completed
Updated: 2026-03-13 11:57:13 +08:00
---

# Token 节流固化方案（平衡型）最终版 Handoff

## Scope
- 固化全局 token 节流配置。
- 固化全局默认输出压缩与上下文治理规则。
- 固化子 agent 申请机制。
- 在当前仓库生成独立任务包，供后续新会话继续使用。

## Current Stage
- 已完成配置修改、全局规则固化、任务包落盘与验证。
- 当前状态适合直接收尾，也适合作为后续新会话的首读 handoff。

## Confirmed Decisions
1. `tool_output_token_limit` 固定为 `12000`。
2. `model_auto_compact_token_limit` 固定为 `350000`。
3. 默认工具输出只保留结论、关键证据行、下一步。
4. 默认不全文回读，不生成过程性长文档，commentary 默认降频。
5. 长任务阶段边界默认 handoff，并强烈建议切新会话，但不强制中断当前会话。
6. 用户拥有显式覆盖权：全文输出 / 不切会话 / 不压缩工具输出 / 不生成 handoff。
7. 子 agent 采用“先评估、说明理由、请求确认”的默认机制；未明确提及时也可主动申请。

## Invalidated Assumptions
- “为了控 token，必须强制结束当前会话”这一假设已被否定。
- “只要用户提到子 agent 就可以直接开”这一假设已被否定。
- “压缩工具输出就必须牺牲用户覆盖权”这一假设已被否定。

## Remaining Work
- 无强制后续工作。
- 如用户后续还要继续调节节流强度，可基于本任务包讨论更激进或更保守的参数。
- 如用户要求把同类规则同步到其他仓库级 AGENTS，再另起任务包处理。

## Next Session First Reads
1. `doc/agent/token-throttling_20260313-115713/decisions/20260313_token-throttling_note_v01.md`
2. `doc/agent/token-throttling_20260313-115713/reports/20260313_token-throttling_report_v01.md`
3. `doc/agent/token-throttling_20260313-115713/handoffs/20260313_token-throttling_handoff_v01.md`
4. `C:\Users\65430\.codex\config.toml`
5. `C:\Users\65430\.codex\AGENTS.md`

## Continuation Prompt
```text
退出 Plan Mode，开始执行“Token 节流固化方案（平衡型）最终版”。

执行要求：
1. 修改 `C:\Users\65430\.codex\config.toml`
   - `tool_output_token_limit = 12000`
   - `model_auto_compact_token_limit = 350000`
   - 其他相关值保持不变

2. 修改 `C:\Users\65430\.codex\AGENTS.md`
   增加并固化以下默认规则：
   - 工具输出默认摘要化，只给：结论、关键证据行、下一步
   - 默认不全文回读文件，只读关键段/关键行/关键配置项
   - 默认不生成过程性长文档，只保留最终必要产物
   - 默认 commentary 降频
   - 长任务阶段边界默认生成 handoff，并强烈建议切新会话
   - 不强制终止当前会话
   - 用户可显式覆盖：全文输出 / 不切会话 / 不压缩工具输出 / 不生成 handoff

3. 同时在全局 `AGENTS.md` 中固化子 agent 申请机制：
   - 当我要求开启子 agent 时，先评估再向我说明理由并请求确认
   - 当我没提及但你判断开启更优时，也可以主动申请
   - 评估维度固定为：上下文是否更干净、腐化风险是否更小、任务规模是否值得拆分、效率是否提升、是否有独立审查或并行收益

4. 在当前仓库下新建任务包并落盘：
   - `doc/agent/token-throttling_20260313-<执行时间>/decisions/20260313_token-throttling_note_v01.md`
   - `doc/agent/token-throttling_20260313-<执行时间>/reports/20260313_token-throttling_report_v01.md`
   - `doc/agent/token-throttling_20260313-<执行时间>/handoffs/20260313_token-throttling_handoff_v01.md`

5. handoff 至少包含：
   - Scope
   - Current Stage
   - Confirmed Decisions
   - Invalidated Assumptions
   - Remaining Work
   - Next Session First Reads
   - Continuation Prompt

6. 最后做验证：
   - 用真实 TOML 解析器验证 `config.toml`
   - 回读 `AGENTS.md` 关键段
   - 检查任务包文档已生成
   - 如有 stale memory，同步更新 `C:\Users\65430\.codex\memories\MEMORY.md` 和 `memory_summary.md`
```
