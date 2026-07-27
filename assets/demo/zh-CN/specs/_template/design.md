# <feature> 设计

> 状态: Exploring | Proposed | Validated | Superseded
> 创建日期: YYYY-MM-DD
> 更新日期: YYYY-MM-DD
> 关联规格: `spec.md | none`
> 关联计划: `plan.md | none`
> ADR: none | required | `<ADR path> (Draft | Accepted)`
> 实验引用: none | `<worktree / commit / artifact>`
> 说明: `Validated` 表示已有足够技术证据进入计划阶段；触发 ADR 的契约仍需要 `Accepted` ADR。
> 说明: 评审或 ADR 接受只提升其明确范围；其他假设和开放问题仍未解决。

## 1. 摘要

- <问题和建议方向>
- <本设计有意不作决定的事项>

## 2. 证据与未知项

- `Observed`: <已直接证明的事实及证据范围>
- `Hypothesis`: <可证伪的候选判断>
- `Open`: <导致无法安全决策的缺失信息>

| 未知项 | 分类 | 下一动作 |
| --- | --- | --- |
| <问题> | Requirement decision / Contract evidence gap / Technical hypothesis / Implementation concern | 必要的用户确认 / source audit 或最小 probe / bounded spike / 计划下交付 |

## 3. 目标与非目标

### 目标

- <技术目标>

### 非目标

- <非目标>

## 4. 不变量、候选契约与实现自由度

- `Invariant`: <正确性、安全性、兼容性或数据边界>
- 候选契约: <可能需要稳定下来的行为>
- 实现自由度: <不改变契约即可调整的内部选择>
- 边界调整: no | yes — <原因、收益、风险和验证>

## 5. 建议设计与失败语义

<关键流程、状态机、数据流、错误优先级、生命周期和可观察性。>

## 6. 替代方案

| 方案 | 收益 | 成本 / 风险 | 结果 |
| --- | --- | --- | --- |
| <A> | <...> | <...> | Selected |
| <B> | <...> | <...> | Rejected / Open |

## 7. 兼容性、迁移、回滚与验证

- 兼容性: <API / 协议 / 配置 / schema / 行为>
- 迁移: none | <方法>
- 回滚: <方法>
- 自动化验证: <覆盖范围>
- E2E / 人工验证: <环境和检查项>
- 风险与缓解: <风险 + 缓解措施>

## 8. 可证伪假设

| 假设 / 问题 | 当前依据 | 验证方式 | 证伪条件 | 状态 |
| --- | --- | --- | --- | --- |
| <H1> | <证据> | <实验> | <条件> | Open / Supported / Revised / Rejected / Inconclusive |

## 9. 设计增量

只记录会改变技术判断的证据；不记录逐 operation 状态、普通交付进度、编译修复或计划已负责的工作。

| 日期 | 来源 | 先前假设 | 证据 | 结果 | 设计增量 | 实现处置 |
| --- | --- | --- | --- | --- | --- | --- |
| YYYY-MM-DD | Review / Spike / Implementation | <假设> | <证据> | Supported / Revised / Rejected / Inconclusive | <变更> | keep / rework / discard |
