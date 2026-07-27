# <feature> 规格

> 功能状态: Exploring | Shaping | Ready | Implementing | Verifying | Blocked | Completed | Superseded
> 优先级: P0 | P1 | P2 | P3
> 负责人: @name | unassigned
> 创建日期: YYYY-MM-DD
> 更新日期: YYYY-MM-DD
> 主要区域: `<path>`
> 范围: `<path>`, `<path>`
> 依赖: none | `specs/<feature>`
> 阻塞项: none | <阻塞条件>
> 后继功能: none | `specs/<feature>`
> 关联文档: `design.md | none`, `plan.md | none`, `<ADR path> | none`
> 目的: 记录已跟踪功能的状态和可观察需求，而不是技术设计或实施步骤。

## 1. 可观察结果

<此功能完成后，用户或系统可以观察到什么。>

## 2. 背景与问题

- <当前行为>
- <触发因素>
- <为何现在需要处理>

## 3. 目标

- <目标>

## 4. 约束

- <必须保持成立的行为或契约>
- <安全、兼容性、数据或组织边界>

## 5. 非目标

- <非目标>

## 6. 验收条件

| ID | 可观察条件 | 必需证据 |
| --- | --- | --- |
| AC-1 | <条件> | <单元 / 集成 / E2E / 人工验证证据> |

## 7. 需求层开放问题

- <可能改变结果、范围或验收条件的问题。>

技术假设和实施问题应写入 `design.md`。

## 8. 完成证据

仅当功能是局部、单切片、不需要跨会话推进且不存在独立 `plan.md` 时使用本节。
多切片、跨会话或保留原型后继续扩展的交付必须创建计划；否则链接到计划中的验证记录。

- `Executed`: <命令或动作 + 结果>
- E2E: passed | failed | blocked | not required
- 已知限制: none | <限制>
- 文档影响: none | updated `<path>`
