---
name: feature-specs
description: Initialize or repair an evidence-driven specs workflow, remove duplicated fact sources, create or restructure spec.md, design.md, and plan.md for a nontrivial tracked feature, or restore the exploration-to-delivery phase boundary when a bounded spike has expanded into implementation. Use for workflow adoption, material requirement or design changes, workflow repair, and explicit feature-spec requests. Do not use for routine implementation, tests, local bug fixes, progress reporting, or verification under an established project workflow.
---

# Feature Specs

Build a small, explicit fact-source chain for nontrivial work without forcing documentation onto
simple changes. Keep requirements, technical reasoning, delivery progress, and execution evidence
separate.

## Preserve Project Authority

1. Read the nearest project guidance and existing documentation workflow first.
2. Follow an existing project convention unless the user asks to replace or repair it.
3. Once a project-local specs workflow exists, follow it directly for routine implementation,
   tests, local bug fixes, progress reporting, and verification.
4. Do not initialize `specs/` merely because the skill is available.
5. Do not create a tracked feature for a one-off local change that can safely follow
   `Code -> Verify`.
6. Keep project-specific protocol, module, test, and deployment rules in the repository rather
   than in this skill.

## Select the Documentation Language

1. Honor an explicit artifact-language request.
2. Otherwise, use the repository's established documentation language. If none exists, use the
   dominant natural language of the current user request for prose created in this turn.
3. Localize headings, explanatory prose, table headings, and placeholders in newly initialized
   `specs/` files. Treat localizing the initializer's bundled English copies as part of
   initialization, not as an optional follow-up.
4. Preserve filenames, paths, commands, code identifiers, Markdown structure, links, and stable
   controlled literals such as statuses, evidence labels, hypothesis results, and implementation
   dispositions unless the project defines canonical localized equivalents.
5. Keep an existing specs workflow in its established language unless the user asks to
   relocalize it. If tooling requires exact text, preserve the required literals and localize only
   the surrounding prose.
6. Use `assets/demo/zh-CN/` only as a non-authoritative example of a completed Simplified Chinese
   initialization. Keep `assets/specs/` as the semantic source of truth.

## Choose the Smallest Workflow

- Use `Code -> Verify` for a clear, local, reversible change.
- Use `Design -> Plan -> Code -> Verify` when key assumptions already have evidence.
- Use `Explore -> Draft Design -> Spike -> Findings -> Revise Design` when a material unknown can
  invalidate the approach.
- Use `Spike -> Retrospective Design -> Review -> Reimplementation` when code is the cheapest way
  to discover the design.

## Classify Before Exploring

Classify each unknown before choosing a spike:

- `Requirement decision`: An unresolved user or product choice that materially changes observable
  outcome, scope, or acceptance. Ask only when it has not already been delegated or resolved by
  the user, accepted requirements, or an ADR; implementation cannot substitute for that decision.
- `Contract evidence gap`: A fact answerable by an authoritative source contract, direct call
  chain, test, schema, or runtime observation. Audit that evidence or run a minimal bounded probe
  before writing the dependent production evaluator or adapter; the probe itself may supply the
  missing evidence.
- `Technical hypothesis`: A falsifiable technical judgment that may justify a bounded spike.
- `Implementation concern`: A delivery detail that does not change the design. Handle it under the
  plan with `Code -> Verify`; do not create an exploration.

Reclassify when evidence changes the nature of the unknown. Stop implementation only when an
audit exposes a material requirement decision that remains unresolved and was not delegated.

Create only the documents required by the selected workflow:

- `spec.md`: tracked feature state, observable outcome, scope, constraints, and acceptance.
- `design.md`: evidence, invariants, hypotheses, open questions, candidate contracts, alternatives,
  and design delta.
- `plan.md`: delivery slices, dependency order, gates, progress, verification, and rollback.
- `explorations/*.md`: bounded process evidence for a risky or disposable spike.

Never add a second task board that duplicates plan progress. If a project already has one, treat
its documented fact-source rules as authoritative.

## Initialize a New Project

Run the safe initializer from the skill directory:

```bash
python3 scripts/init_feature_specs.py <repo-root>
```

Use `--dry-run` first when the repository is not empty or its conventions are uncertain. The
initializer copies only the core `specs/README.md` and `spec/design/plan` templates. It refuses to
overwrite differing files and does not edit `AGENTS.md`.

After initialization:

1. Adapt project-local statuses, validation commands, ADR location, and module vocabulary.
2. Add one routing sentence to the repository `AGENTS.md` only if it does not already point to
   `specs/README.md`.
3. Remove irrelevant placeholders before using a template for a real feature.

## Maintain Fact Sources

- Write requirement, scope, or acceptance changes to `spec.md`.
- Write technical evidence, hypotheses, contracts, and design changes to `design.md`.
- Write slice status, executed verification, blockers, and residual delivery risk to `plan.md`.
- Write traceable spike process evidence with source identity appropriate to the claim in
  `explorations/`, then summarize only the resulting design delta in `design.md`.
- Let an ADR accept only its explicit decision scope; keep other hypotheses and open questions
  unresolved.

For complex reasoning or support claims, read
[references/evidence-model.md](references/evidence-model.md) before writing.

## Use Bounded Exploration Only When Needed

- Copy `assets/optional/exploration.md` for a bounded spike whose process evidence would obscure
  the living design.
- Let each project or feature define any other auxiliary document from its actual problem. Do not
  prescribe a standard name or template here.
- Require every auxiliary document to state its role and authoritative fact source; never let it
  become a duplicate feature-status source.

## Exit or Promote an Exploration

1. End the exploration when its question or falsification condition is answered. Record the
   hypothesis result, implementation disposition, design impact, and one explicit exit decision,
   such as stopping, promoting retained work into design and delivery, or running one distinct
   next experiment. Do not require a fixed literal unless project tooling defines one.
2. `keep` means only that prototype code may remain. Before expanding it as a cross-session or
   multi-slice deliverable, make the corresponding delivery design `Validated` and create a
   tracked plan or use an established project-defined equivalent authoritative delivery record.
   In the bundled specs workflow, a plan is the default; otherwise split, rework, or stop.
3. Create another exploration only for a distinct material unknown. Do not chain equivalent
   operations, pages, or adapters as repeated spikes once a representative contract pattern is
   established.
4. Keep routine delivery status and verification in the plan or a project-defined delivery
   ledger. Do not append them to a concluded exploration or design delta.
5. Treat a dirty worktree as a normal execution state. Record the base ref when available,
   `clean | dirty`, and the relevant change scope. Preserve a diff/artifact identity only when
   exact reproduction materially affects the design or support claim. If the result is committed
   later, label that commit as the retained outcome, never as the historical execution snapshot.
6. If later evidence invalidates a concluded exploration, add a short supersession link and update
   design; do not reopen the exploration as an implementation log.

## Validate the Result

Check all of the following:

- Each fact appears in one authoritative document; other documents link to it.
- A plan exists only with a tracked spec.
- A plan is based on validated design evidence or states why no independent design is needed.
- Multi-slice, cross-session, or retained-spike delivery has a plan or an established
  project-defined equivalent authoritative delivery record. In the bundled specs workflow, use a
  plan; no-plan completion evidence there is limited to a local single-slice tracked change.
- Slice completion is based on an observable outcome and a gate, not file or abstraction creation.
- Unknowns are classified, and unresolved material requirement decisions are neither disguised as
  technical experiments nor re-asked after the user or accepted requirements delegated them.
- Every concluded exploration has an exit decision and no routine delivery tail.
- Code-bearing explorations distinguish the actual execution state from any later retained outcome
  and do not overstate reproducibility.
- `Observed`, `Hypothesis`, `Open`, and `Decision` are not conflated.
- Executed, static, and unexecuted verification are labeled accurately.
- Completion, compatibility, and support claims do not exceed actual evidence scope.
- ADR acceptance does not silently promote unrelated hypotheses.
- No suggested command is reported as executed.
