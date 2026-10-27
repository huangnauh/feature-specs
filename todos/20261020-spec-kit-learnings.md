# 借鉴 spec-kit 与 Ryugi 的后续改进

- 创建日期：2026-10-20
- 更新日期：2026-10-27
- 状态：待推进
- 分析对象：本地 `/disk/ssd1/tools/spec-kit`，commit `f68ffcab`（2026-10-19）
- 补充来源：本地 `/disk/ssd1/tools/ryugi/skills`，以及其开发侧 `writing-skills`（2026-10-27）。
- spec-kit 分析时项目基线：`794ea3e`（2026-10-10）
- 证据范围：spec-kit 已静态阅读核心模板、命令、相关脚本与测试；Ryugi 已静态阅读 skill、
  执行脚本及相关测试说明。未执行测试或 Agent 行为评估。

本文件保存改进候选与推进顺序。若后续工作进入正式 feature 交付流程，在这里链接对应文档，
交付进度与验证记录由该 feature 的 plan 维护，不在此重复记录。

## 目标与边界

保留当前项目的轻量、证据驱动和项目优先定位，把已有原则补充为可操作的评审动作。
优先完善现有文档与示例，不因借鉴引入新的文档套件、公共接口或执行平台。

注意文档职责不同：spec-kit 的 `plan.md` 主要承载技术设计，`tasks.md` 承载执行任务；
当前项目分别由 `design.md` 和 `plan.md` 承载，不能按同名文件直接迁移。

Ryugi 中经用户批准的设计文档和临时 `tasks.md` / `progress.md` 也不能直接映射为当前项目的事实源。
推进时优先完善[行为回归材料](20261027-workflow-behavior-evals.md)，再用相关场景验证交接检查、
恢复规则和其他候选；根据实际偏差决定是否调整规则、模板或示例。

## 优先推进：评审与交付闭环

- [ ] **补充需求质量检查。** 在需求趋于稳定时，按风险检查完整性、清晰度、一致性、
  可度量性和场景覆盖。后端场景可考虑幂等、部分失败、并发冲突、恢复和兼容性，
  只检查与当前功能有关的维度。发现缺口后，使用现有未知分类决定查证、实验或询问用户。
  在设计转交付时，从接手实现者的角度检查仍需猜测且猜错会影响实施或验收的问题；
  跳过已明确交给实现者决定的细节，已有答案通过查证补齐。
  - 位置：`assets/specs/README.md`；按需要补充 `references/worked-examples.md`。
  - 验收：能够发现规格遗漏和关键交接缺口；不重复询问已有结论，不自动增加需求、
    固定澄清轮次、通用审批门禁或 subagent 要求。
  - 参考：[spec-kit checklist](/disk/ssd1/tools/spec-kit/templates/commands/checklist.md:150)、
    [Ryugi builder check](/disk/ssd1/tools/ryugi/skills/brainstorming/builder-check-prompt.md:6)。

- [ ] **补充跨文档一致性检查。** 在需求或设计实质变化、replan 和最终交付时，检查验收项
  是否有切片和证据承接、必要设计约束是否进入实现与验证、切片是否有需求或设计依据，
  以及 spec、design、plan 是否相互矛盾。
  - 位置：`assets/specs/README.md`、`assets/specs/_template/plan.md`。
  - 验收：复用现有 `AC-N` 引用和事实源分工；不新增覆盖看板，不要求每轮加载全部文档。
  - 参考：[spec-kit analyze](/disk/ssd1/tools/spec-kit/templates/commands/analyze.md:115)。

- [ ] **补充最终行为收敛检查。** 对照需求与设计重新核对当前实现，包括已经勾选完成的工作；
  检查缺失、部分满足、与约定冲突和缺少依据的额外实现。
  对与验收相关、但测试未覆盖的具体输入或失败路径，明确后续评审或运行验证动作，
  避免只记录风险而没有检查安排；仅检查当前功能涉及的路径，不生成通用风险清单。
  - 位置：`assets/specs/README.md`、`assets/specs/_template/plan.md`；
    在 `references/worked-examples.md` 补一个遗漏或额外实现的例子。
  - 验收：实现缺口回写原 plan；契约或关键假设变化进入已有的 `Replan Required`；
    不以任务勾选替代证据，不通过修改规格使其迁就实现，不把静态检查等同运行验收通过。
  - 参考：[spec-kit converge](/disk/ssd1/tools/spec-kit/templates/commands/converge.md:145)、
    [Ryugi Review Focus](/disk/ssd1/tools/ryugi/skills/executing-specs/SKILL.md:199)。

## 后续推进：执行恢复与判断写回

- [ ] **明确跨会话或上下文压缩后的恢复顺序。** 先读 plan 的当前状态、当前切片及其证据，
  再按引用读取相关验收项和设计约束；用实际代码或提交核对已完成结果，避免重复实现。
  - 位置：`assets/specs/README.md`；按需要补充 `references/worked-examples.md`。
  - 验收：能够恢复未完成工作；默认不加载整个 feature、历史探索或完整验证日志。
    plan 继续作为交付状态事实源，必要的任务摘要仅为派生视图，不另建维护进度的文件。
  - 参考：[Ryugi 恢复与任务 brief](/disk/ssd1/tools/ryugi/skills/executing-specs/SKILL.md:135)。

- [ ] **明确实质自主判断的来源和写回。** 区分用户明确要求、既有契约决定和 Agent 在授权
  范围内的选择；对影响结果的判断说明依据及判断错误的代价，按事件写回对应事实源。
  - 位置：`assets/specs/README.md`；按需要补充 `references/worked-examples.md`。
  - 验收：需求归 spec、技术判断归 design、交付安排归 plan；不记录每个局部实现选择，
    不新增裁决日志。记录判断不能替代必要授权，未授权的实质需求选择仍按
    `Requirement decision` 处理。
  - 参考：[Ryugi Rulings](/disk/ssd1/tools/ryugi/skills/executing-specs/SKILL.md:25)。

## 后续推进：生命周期与验证

- [ ] **明确完成后的文档维护策略。** 指导项目约定何时修订原 feature，何时新建后续 feature，
  以及如何使用 `Superseded`、`Successor` 和替代链接。
  - 位置：`assets/specs/README.md`；必要时调整模板说明。
  - 验收：保留项目选择权；重要设计理由与历史验证范围可追溯；
    不把已经结束的探索改写为持续交付日志。
  - 参考：[spec-kit persistence models](/disk/ssd1/tools/spec-kit/docs/concepts/spec-persistence.md:61)。

- [ ] **为初始化器补充最小行为回归验证。** 覆盖首次复制、重复执行幂等、dry-run 不写入、
  冲突时不覆盖且不创建其他待复制文件，以及不修改 `AGENTS.md`。
  - 对象：`scripts/init_feature_specs.py`；使用临时目录，避免引入不必要的测试依赖。
  - 验收：通过实际执行脚本验证退出码和文件结果，不以实现文本断言替代行为测试。
  - 参考：[spec-kit no-overwrite tests](/disk/ssd1/tools/spec-kit/tests/test_setup_plan_no_overwrite.py:114)。

“用场景评估 Skill 的实际效果”候选已细化为
[开发侧工作流行为回归待办](20261027-workflow-behavior-evals.md)，范围、推进状态和验收条件由该文件维护。
原候选中的遗漏场景与额外实现检查，可在该待办的首批五个场景之后按需要扩展。

## 暂不纳入

- 独立 `tasks.md` 或第二个进度看板：当前 plan 已承载任务与交付状态。
- 固定 research、data-model、contracts、quickstart 文档套件：继续按实际问题增加辅助文档。
- 独立 constitution、逐阶段人工审批、固定数量的澄清问题：遵循现有项目规范与授权边界。
- CLI、MCP、插件目录、preset 系统和工作流引擎：目前没有足够的实际需求支撑这些成本。
- Ryugi 的宽泛 skill 强制触发、普遍强制 TDD、逐任务全量测试及固定评审或修复次数：
  保留按风险选择最小流程和验证范围，不引入默认 subagent 要求。
- Artboard、云发布和 UI 逐组人工验收：保留为特定项目的可选机制，不纳入跨项目核心工作流。

## 推进时的验证要求

- 确认新增内容补充了具体检查动作，没有重复现有事实源或放宽证据边界。
- 仅在语义变化时同步相关说明；中文 demo 保持非权威示例定位。
- 区分实际执行、静态证据、未执行项与剩余风险；本清单中的验收要求不是已通过的验证结果。
