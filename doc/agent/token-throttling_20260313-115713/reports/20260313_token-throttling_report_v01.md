---
Owner: Codex
Task: token-throttling
Status: completed
Updated: 2026-03-13 11:57:13 +08:00
---

# Token 节流固化方案（平衡型）最终版 Execution Report

## Goal
- 按用户指定值收紧全局 token 节流配置。
- 在全局 `AGENTS.md` 固化默认输出压缩、阶段性 handoff、以及子 agent 申请机制。
- 在当前仓库写入独立任务包，作为后续新会话首读材料。

## Changes Applied
### 1. Global Config
- 文件：`C:\Users\65430\.codex\config.toml`
- 已修改：
  - `model_auto_compact_token_limit: 600000 -> 350000`
  - `tool_output_token_limit: 20000 -> 12000`
- 未修改：
  - `model_context_window`
  - `service_tier`
  - `agents`
  - `memories`
  - 其他 provider / project / MCP 段

### 2. Global AGENTS
- 文件：`C:\Users\65430\.codex\AGENTS.md`
- 已新增：
  - `Default Token Throttling And Context Hygiene`
  - `Child-Agent Request Mechanism`

## Verification Evidence
- `config.toml` 关键值回读已确认：
  - `model_auto_compact_token_limit = 350000`
  - `tool_output_token_limit = 12000`
- `AGENTS.md` 关键段回读已确认：
  - 默认工具输出摘要化
  - 默认只读关键段/关键行/关键配置项
  - 默认不生成过程性长文档
  - 默认 commentary 降频
  - 长任务阶段边界默认 handoff + 强烈建议新会话
  - 不强制结束当前会话
  - 用户可显式覆盖
  - 子 agent 必须先评估、说明理由、请求确认
- 独立任务包已创建于：
  - `doc/agent/token-throttling_20260313-115713/`

## Notes
- 本次执行遵守“只改目标项”的约束，没有顺手合并其他全局治理事项。
- 若后续继续调 token 策略，应以本任务包为基线，而不是回到旧任务包混写。
