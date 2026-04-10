---
Owner: Codex
Task: sdes-rewrite
Status: active
Updated: 2026-03-25
---

# 软件设计师 L02-L03 重写计划

## Goal

- 保留旧版 `L02/L03` 课案
- 新增可独立承担主学习材料的重写版 `L02/L03`
- 将课程当前有效进度回退到“从重写版 L02 重新开始”

## Affected Files

- Create: `doc/Software-Designer-master/课案/02_上午快得分模块I_重写版.md`
- Create: `doc/Software-Designer-master/课案/03_数据结构与算法I_重写版.md`
- Create: `doc/agent/sdes-rewrite_20260325-102738/decisions/20260325_sdes-teaching-standard_note_v01.md`
- Create: `doc/agent/sdes-rewrite_20260325-102738/reports/20260325_sdes-progress-reset_report_v01.md`
- Create: `doc/agent/sdes-rewrite_20260325-102738/handoffs/20260325_sdes-rewrite-reset_handoff_v01.md`

## Work Packages

1. 固化新版教学标准
2. 重写 L02
3. 重写 L03
4. 回退课程有效进度
5. 写新交接单

## Risk

1. `L02` 若继续只依赖仓库 `真题/` 目录，会把下午案例卷误当上午快得分题库，导致频率统计失真。
2. `L03` 若一味追求“从零讲透”，容易膨胀成教材复写，失去真题导向。
3. 若不显式声明旧版与新版的基线关系，下个会话容易误读旧版进度为当前有效进度。

## Verification

1. 新版 `L02/L03` 必须包含：
   - 零基础讲法
   - 真题方向
   - 习题权重字段
   - 严格批改口径
2. 决议、报告、交接单三份工件必须明确：
   - 新版课案路径
   - 有效进度回退到 L02
   - 旧版保留但不再作为当前主线

## Rollback

- 删除 `sdes-rewrite_20260325-102738` task bundle
- 删除 `02_上午快得分模块I_重写版.md`
- 删除 `03_数据结构与算法I_重写版.md`
- 继续沿用旧版 `L02/L03` 和旧进度台账
