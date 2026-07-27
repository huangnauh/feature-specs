# Feature Specs

An agent skill for **evidence-driven feature delivery**: keep requirements, technical design,
delivery progress, and execution evidence as separate fact sources—without forcing documentation
onto simple changes.

Use it to initialize or repair a project-local `specs/` workflow, restructure `spec.md` /
`design.md` / `plan.md` for a nontrivial tracked feature, or restore the exploration-to-delivery
boundary when a spike has expanded into implementation.

## When to use

| Use | Do not use |
| --- | --- |
| Workflow adoption or repair | Routine implementation under an established workflow |
| Material requirement or design changes | Local bug fixes, tests, progress reporting |
| Explicit feature-spec requests | Verification that already has a project path |
| Spike exit / delivery promotion boundaries | One-off reversible `Code → Verify` changes |

Once a project-local specs workflow exists, follow it directly for day-to-day work. Do not
initialize `specs/` merely because this skill is available.

## Core idea

Smallest workflow that fits the risk:

| Workflow | When |
| --- | --- |
| `Code → Verify` | Clear, local, reversible change |
| `Design → Plan → Code → Verify` | Key assumptions already have evidence |
| `Explore → Draft Design → Spike → Findings → Revise Design` | A material unknown can invalidate the approach |
| `Spike → Retrospective Design → Review → Reimplementation` | Code is the cheapest way to discover the design |

### Fact sources

| Document | Owns |
| --- | --- |
| `spec.md` | Observable outcome, scope, constraints, acceptance, feature state |
| `design.md` | Evidence, invariants, hypotheses, contracts, alternatives, design delta |
| `plan.md` | Delivery slices, gates, progress, verification, rollback |
| `explorations/*.md` | Bounded spike process evidence (not living design or delivery state) |

Link between documents; do not copy conclusions. Never add a second task board that duplicates
plan progress.

### Evidence language

| Label | Meaning |
| --- | --- |
| `Observed` | Directly demonstrated fact |
| `Hypothesis` | Falsifiable candidate judgment |
| `Open` | Missing information blocks a safe decision |
| `Decision` | Reviewed conclusion accepted for an explicit scope |

Classify unknowns before exploring: `Requirement decision`, `Contract evidence gap`,
`Technical hypothesis`, or `Implementation concern`. Full vocabulary:
[references/evidence-model.md](references/evidence-model.md).

## Quick start

From this skill directory, initialize a repository:

```bash
# Preview first when the repo is non-empty or conventions are unclear
python3 scripts/init_feature_specs.py --dry-run /path/to/repo

python3 scripts/init_feature_specs.py /path/to/repo
```

The initializer:

- Copies only core assets: `specs/README.md` and `spec` / `design` / `plan` templates
- Refuses to overwrite files that differ from the bundled copies
- Does **not** edit `AGENTS.md`

After initialization:

1. Adapt project-local statuses, validation commands, ADR location, and module vocabulary.
2. Add one routing sentence to the repository `AGENTS.md` only if it does not already point at
   `specs/README.md`.
3. Remove irrelevant placeholders before using a template for a real feature.
4. Localize newly initialized prose to the repository’s documentation language when needed
   (`assets/demo/zh-CN/` is a non-authoritative Simplified Chinese example; `assets/specs/` is
   the semantic source of truth).

## Repository layout

```text
feature-specs/
├── SKILL.md                      # Skill entry: when to invoke, rules, validation
├── agents/openai.yaml            # Agent interface metadata
├── assets/
│   ├── specs/                    # Core templates installed into a project
│   │   ├── README.md
│   │   └── _template/
│   │       ├── spec.md
│   │       ├── design.md
│   │       └── plan.md
│   ├── optional/exploration.md   # Optional bounded-spike template
│   └── demo/zh-CN/               # Example Chinese initialization (non-authoritative)
├── references/evidence-model.md  # Epistemic labels, unknown classification, evidence class
└── scripts/init_feature_specs.py # Safe project initializer
```

## Project workflow (after init)

Feature directories default to `YYYYMMDD-feature-name` unless the project defines another
convention. Create only the documents the work needs:

| Scenario | `spec.md` | `design.md` | `plan.md` |
| --- | --- | --- | --- |
| Clear one-off local change | optional | optional | optional |
| Untracked bounded spike | optional | required | do not create |
| Cross-session tracked feature | required | as uncertainty requires | as delivery complexity requires |
| Multi-slice delivery | required | validated, or explain why unnecessary | required |

If `plan.md` exists, `spec.md` must exist. Slice completion is based on an observable outcome and
a gate—not on creating files or abstractions.

### Design-first

```text
Idea → Spec (when tracked) + Draft Design
    → Optional Spike → Revise / Validate Design
    → Plan → Production Implementation → Verify
```

### Prototype-first

```text
Idea → Bounded Spike → Retrospective Design → Review
    → keep / rework / discard
    → Validate Design → Plan → Production Implementation → Verify
```

A spike or retained prototype is **not** automatically production implementation. `keep` only
means prototype code may remain; before cross-session or multi-slice expansion, make the
corresponding design `Validated` and create a plan (or the project’s equivalent delivery record).

## Project authority

1. Read the nearest project guidance and existing documentation workflow first.
2. Follow an existing project convention unless the user asks to replace or repair it.
3. Keep project-specific protocol, module, test, and deployment rules in the repository—not in
   this skill.

## Documentation

| Doc | Language |
| --- | --- |
| [README.md](README.md) | English (this file) |
| [README.zh.md](README.zh.md) | 简体中文 |
| [SKILL.md](SKILL.md) | Skill rules for agents |
| [assets/specs/README.md](assets/specs/README.md) | Project-facing specs workflow |
| [references/evidence-model.md](references/evidence-model.md) | Evidence and decision model |

## License

Unless otherwise stated by the repository owner, use and adapt under the same terms as the
containing project or skill pack that ships this skill.
