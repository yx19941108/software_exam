---
Owner: Codex
Task: token-throttling
Status: completed
Updated: 2026-03-13 12:54:21 +08:00
---

# Token 节流与子 Agent 规则二次优化 Handoff

## Scope
- 对全局 `AGENTS.md` 做第二轮规则优化。
- 继续沿用既有 `token-throttling_20260313-115713` 任务包，不另开新包。

## Current Stage
- 规则补丁已写入 `C:\Users\65430\.codex\AGENTS.md`。
- `v02` 决策、报告、交接文档已落盘。
- 关键段回读、任务包检查、以及 memory 冲突检查已完成。

## Confirmed Decisions
1. 治理类指令同样适用“先指出问题并确认”规则。
2. 默认 token 节流不能覆盖高风险证据保留要求。
3. child agent 申请必须说明边界、角色、产物和收益。
4. 默认不开 child agent 的典型情形已显式化。
5. 变更前置规划规则适用于所有持久行为文件。

## Invalidated Assumptions
- “child agent 只要有评估维度就够了”这一假设已被否定。
- “默认压缩输出不会影响高风险取证”这一假设已被否定。
- “只有代码文件才需要 Goal / Affected Files / Risk / Verification / Rollback”这一假设已被否定。

## Remaining Work
- 当前无强制后续工作。
- 如需继续收紧，可在后续会话考虑把 child-agent 检查清单升级为固定申请模板，或为高风险任务增加更明确的证据保留下限。

## Next Session First Reads
1. `C:\Users\65430\.codex\AGENTS.md`
2. `doc/agent/token-throttling_20260313-115713/decisions/20260313_token-throttling_note_v02.md`
3. `doc/agent/token-throttling_20260313-115713/reports/20260313_token-throttling_report_v02.md`
4. `doc/agent/token-throttling_20260313-115713/handoffs/20260313_token-throttling_handoff_v02.md`
5. `C:\Users\65430\.codex\memories\MEMORY.md`

## Continuation Prompt
```text
继续推进全局 AGENTS 治理增强的下一阶段。

执行要求：
1. 先读：
   - `C:\Users\65430\.codex\AGENTS.md`
   - `doc/agent/token-throttling_20260313-115713/decisions/20260313_token-throttling_note_v02.md`
   - `doc/agent/token-throttling_20260313-115713/reports/20260313_token-throttling_report_v02.md`
   - `doc/agent/token-throttling_20260313-115713/handoffs/20260313_token-throttling_handoff_v02.md`
2. 评估是否需要继续收紧以下候选项：
   - child-agent 固定申请模板
   - 高风险任务的最小证据保留下限
   - 更明确的阶段边界 handoff 触发条件
3. 如有新增 durable 规则，同步更新任务包文档；如发现 stale memory，再同步更新 `MEMORY.md` 与 `memory_summary.md`。
```
