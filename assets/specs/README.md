# Feature Specs

Use `specs/` as the entry point for tracked feature requirements, living design, delivery progress,
and verification. Name feature directories `YYYYMMDD-feature-name` unless the project defines
another stable convention.

## Create only what the work needs

| Scenario | `spec.md` | `design.md` | `plan.md` |
| --- | --- | --- | --- |
| Clear one-off local change | optional | optional | optional |
| Untracked bounded spike | optional | required | do not create |
| Cross-session tracked feature | required | as uncertainty requires | as delivery complexity requires |
| Multi-slice delivery | required | validated, or explain why unnecessary | required |

If `plan.md` exists, `spec.md` must exist. Do not create empty review, exploration, or artifact
directories.

## Fact-source roles

- `spec.md`: observable outcome, goals, constraints, non-goals, acceptance, feature state,
  priority, ownership, dependencies, and blockers.
- `design.md`: evidence, invariants, hypotheses, open questions, candidate contracts, solution,
  alternatives, failure semantics, compatibility, and design delta.
- `plan.md`: delivery slices, dependency order, current progress, executed verification, rollback,
  and residual delivery risk.
- `explorations/*.md`: traceable process evidence for one bounded spike; not current design or
  delivery state.

Keep requirement changes in spec, technical changes in design, and implementation progress in
plan. Link between documents rather than copying conclusions.

Use completion evidence in a spec without a plan only for a local, single-slice tracked change that
does not need cross-session delivery. Multi-slice, cross-session, or retained-spike delivery uses
a plan by default. An established project may instead use its documented equivalent authoritative
delivery record.

Do not add another task board that repeats active plan state.

## Evidence language

Use these labels when the distinction changes technical judgment:

- `Observed`: directly demonstrated fact.
- `Hypothesis`: falsifiable candidate judgment.
- `Open`: missing information prevents a safe decision.
- `Decision`: reviewed conclusion accepted for an explicit scope.

Design validation and ADR acceptance promote only the explicitly covered scope. Record validation
as `Executed`, `Static evidence`, `Not executed`, and `Residual risk`. Never report suggested
commands as executed.

Before exploring, classify the unknown:

- `Requirement decision`: an unresolved user or product choice materially changes outcome, scope,
  or acceptance; ask only when the user, accepted requirements, or an ADR has not already
  delegated or resolved it. Do not choose it through implementation.
- `Contract evidence gap`: audit the authoritative source contract, direct call chain, test,
  schema, or runtime fact, or run a minimal bounded probe before dependent production logic.
- `Technical hypothesis`: run a falsifiable bounded experiment.
- `Implementation concern`: handle it in the plan with `Code -> Verify`.

## Workflow

### Design-first

```text
Idea -> Spec when tracked + Draft Design
     -> Optional Spike -> Revise / Validate Design
     -> Plan -> Production Implementation -> Verify
```

### Prototype-first

```text
Idea -> Bounded Spike -> Retrospective Design -> Review
     -> keep / rework / discard
     -> Validate Design -> Plan -> Production Implementation -> Verify
```

A spike or retained prototype is not automatically production implementation.

## Statuses

Feature:

- `Exploring`: material unknowns remain.
- `Shaping`: outcome, scope, or acceptance is still converging.
- `Ready`: requirements are stable and implementation prerequisites are satisfied.
- `Implementing`: at least one delivery slice is active.
- `Verifying`: implementation exists but required verification remains.
- `Blocked`: a named external fact, dependency, environment, or authorization prevents progress.
- `Completed`: acceptance, verification, documentation, and state writeback are complete.
- `Superseded`: a named successor replaces the feature.

Design:

- `Exploring | Proposed | Validated | Superseded`

Plan:

- `Draft | Ready | In Progress | Verifying | Blocked | Replan Required | Completed`

Set `Replan Required` when evidence invalidates a key assumption or implementation would change an
accepted contract. Update design before continuing.

## Bounded explorations

Create an exploration only when the spike is risky, cross-cutting, disposable, compares competing
approaches, or would otherwise bury the living design in process detail.

Record:

1. question, hypothesis, and falsification condition;
2. invariants, scope, and stop conditions;
3. environment, actual source/worktree state, relevant change scope, and reproducible actions;
4. meaningful attempts, failures, and forced adjustments;
5. executed, static, and unexecuted evidence plus residual risk;
6. hypothesis result and implementation disposition;
7. design impact and an explicit exit decision.

Use `Supported | Revised | Rejected | Inconclusive` for the hypothesis result. Use
`keep | rework | discard` separately for prototype disposition.

### Exploration exit and delivery promotion

- End an exploration as soon as the question or falsification condition is answered. Record the
  result, disposition, design impact, and an explicit exit—for example, stop, promote retained
  work into design and delivery, or run one distinct next experiment. No fixed literal is required
  unless project tooling defines one.
- `keep` does not make a prototype production implementation. Before cross-session or multi-slice
  expansion, make the corresponding delivery design `Validated` and create a plan or use an
  established project-defined equivalent authoritative delivery record. In this bundled specs
  workflow, use a plan; otherwise split, rework, or stop.
- Do not chain equivalent operations, pages, or adapters as repeated spikes once a representative
  contract pattern is established. Continue them under the plan unless a new fact source, trust
  boundary, protocol shape, or failure model appears.
- Do not append routine delivery progress to a concluded exploration or design delta.
- A dirty worktree is a normal code-bearing exploration state. Record the base ref when available,
  `clean | dirty`, and relevant change scope. Preserve a diff/artifact identity only when exact
  reproduction materially affects the decision or support claim. Label a later commit only as the
  retained outcome, not as the historical execution snapshot.

## Project-defined auxiliary documents

A project or feature may add an auxiliary document when its concrete problem requires one. Define
the document's role and authoritative fact source locally. Do not treat one-off artifacts as
cross-project conventions, add them to the core template set, or let them duplicate feature state.

An auxiliary capability matrix may be the sole per-item mapping and delivery ledger when its role
is explicit. In that case, plan owns batches/stages/gates, spec does not copy item counts, design
records only new or invalidated contract patterns, and explorations do not accumulate delivery
progress.

## Completion boundary

Complete a slice by its observable outcome and evidence gate, not by creating files, types,
interfaces, or abstractions. Completion, compatibility, and support claims must not exceed actual
evidence coverage.
