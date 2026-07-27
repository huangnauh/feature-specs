# Feature Specs（功能规格工作流）

面向 **证据驱动交付** 的 Agent Skill：把需求、技术设计、交付进度与执行证据拆成独立事实源，
不为简单改动强加文档。

用于在项目中初始化或修复本地 `specs/` 工作流，为非平凡已跟踪功能创建或重构 `spec.md` /
`design.md` / `plan.md`，或在有界探索膨胀为实施时恢复「探索 → 交付」阶段边界。

## 何时使用

| 适用 | 不适用 |
| --- | --- |
| 工作流引入或修复 | 已有工作流下的常规实现 |
| 需求或设计发生实质变化 | 局部 bug 修复、测试、进度记录 |
| 用户明确要求 feature-spec | 已有项目路径可走的验证 |
| 探索退出 / 交付提升边界 | 可安全走 `Code → Verify` 的一次性局部改动 |

项目本地 specs 工作流建立后，日常实现、测试、修复、进度与验证直接遵循该工作流；
不要仅因 skill 可用就初始化 `specs/`。

## 核心思路

按风险选择**最小工作流**：

| 工作流 | 适用场景 |
| --- | --- |
| `Code → Verify` | 明确、局部、可回滚的改动 |
| `Design → Plan → Code → Verify` | 关键假设已有证据 |
| `Explore → Draft Design → Spike → Findings → Revise Design` | 实质未知可能否定方案 |
| `Spike → Retrospective Design → Review → Reimplementation` | 用代码发现设计成本更低 |

### 事实源

| 文档 | 职责 |
| --- | --- |
| `spec.md` | 可观察结果、范围、约束、验收、功能状态 |
| `design.md` | 证据、不变量、假设、契约、替代方案、设计增量 |
| `plan.md` | 交付切片、门禁、进度、验证、回滚 |
| `explorations/*.md` | 有界探索的过程证据（不是动态设计或交付状态） |

文档之间链接，不要复制结论。不要新增第二个重复 plan 进度的任务看板。

### 证据语言

| 标签 | 含义 |
| --- | --- |
| `Observed` | 已直接证明的事实 |
| `Hypothesis` | 可证伪的候选判断 |
| `Open` | 缺失信息导致无法安全决策 |
| `Decision` | 经评审并在明确范围内接受的结论 |

探索前先对未知分类：`Requirement decision`、`Contract evidence gap`、`Technical hypothesis`、
`Implementation concern`。完整词汇见
[references/evidence-model.md](references/evidence-model.md)。

## 快速开始

在本 skill 目录下，向目标仓库初始化：

```bash
# 仓库非空或约定不明时，先 dry-run
python3 scripts/init_feature_specs.py --dry-run /path/to/repo

python3 scripts/init_feature_specs.py /path/to/repo
```

初始化器行为：

- 仅复制核心资产：`specs/README.md` 与 `spec` / `design` / `plan` 模板
- 拒绝覆盖与内置副本内容不同的文件
- **不**修改 `AGENTS.md`

初始化之后：

1. 按项目适配状态枚举、验证命令、ADR 位置与模块词汇。
2. 仅当仓库 `AGENTS.md` 尚未指向 `specs/README.md` 时，补一句路由说明。
3. 用于真实功能前，删掉无关占位内容。
4. 按仓库文档语言本地化新建 prose（`assets/demo/zh-CN/` 是非权威的简体中文示例；
   语义真源为 `assets/specs/`）。

## 仓库结构

```text
feature-specs/
├── SKILL.md                      # Skill 入口：调用时机、规则、校验
├── agents/openai.yaml            # Agent 界面元数据
├── assets/
│   ├── specs/                    # 安装到项目中的核心模板
│   │   ├── README.md
│   │   └── _template/
│   │       ├── spec.md
│   │       ├── design.md
│   │       └── plan.md
│   ├── optional/exploration.md   # 可选的有界探索模板
│   └── demo/zh-CN/               # 中文初始化示例（非权威）
├── references/evidence-model.md  # 认知标签、未知分类、证据类别
└── scripts/init_feature_specs.py # 安全的项目初始化脚本
```

## 项目侧工作流（初始化后）

除非项目另有约定，功能目录默认命名为 `YYYYMMDD-feature-name`。只创建工作真正需要的文档：

| 场景 | `spec.md` | `design.md` | `plan.md` |
| --- | --- | --- | --- |
| 明确的一次性局部变更 | 可选 | 可选 | 可选 |
| 不跟踪的有界探索 | 可选 | 必需 | 不创建 |
| 跨会话跟踪的功能 | 必需 | 按不确定性需要 | 按交付复杂度需要 |
| 多切片交付 | 必需 | 已验证，或说明为何不需要 | 必需 |

若存在 `plan.md`，则必须存在 `spec.md`。切片完成以可观察结果与门禁为准，
不以创建文件或抽象为完成条件。

### 设计优先

```text
想法 → 规格（已跟踪时）+ 草稿设计
    → 可选探索 → 修订 / 验证设计
    → 计划 → 生产实现 → 验证
```

### 原型优先

```text
想法 → 有界探索 → 回顾式设计 → 评审
    → keep / rework / discard
    → 验证设计 → 计划 → 生产实现 → 验证
```

探索或保留的原型**不是**自动变成生产实现。`keep` 仅表示原型代码可以留下；
在跨会话或多切片扩展前，须使对应 design 达到 `Validated`，并创建 plan
（或项目已定义的等效交付记录）。

## 项目权威

1. 先阅读最近的项目指引与既有文档工作流。
2. 除非用户要求替换或修复，否则遵循现有项目约定。
3. 协议、模块、测试、部署等项目规则放在仓库内，不写进本 skill。

## 文档

| 文档 | 语言 |
| --- | --- |
| [README.md](README.md) | English |
| [README.zh.md](README.zh.md) | 简体中文（本文件） |
| [SKILL.md](SKILL.md) | 面向 Agent 的 skill 规则 |
| [assets/specs/README.md](assets/specs/README.md) | 安装到项目后的 specs 工作流说明 |
| [references/evidence-model.md](references/evidence-model.md) | 证据与决策模型 |

中文初始化形态可参考 [assets/demo/zh-CN/](assets/demo/zh-CN/)，
其中 `specs/README.md` 与 `AGENTS.md` 为示例，不替代 `assets/specs/` 语义真源。

## 许可

除非仓库所有者另有说明，使用与改编条款与承载本 skill 的项目或 skill 包保持一致。
