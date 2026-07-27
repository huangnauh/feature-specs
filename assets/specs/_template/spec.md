# <feature> specification

> Feature status: Exploring | Shaping | Ready | Implementing | Verifying | Blocked | Completed | Superseded
> Priority: P0 | P1 | P2 | P3
> Owner: @name | unassigned
> Created: YYYY-MM-DD
> Updated: YYYY-MM-DD
> Primary area: `<path>`
> Scope: `<path>`, `<path>`
> Dependencies: none | `specs/<feature>`
> Blocker: none | <blocking condition>
> Successor: none | `specs/<feature>`
> Related: `design.md | none`, `plan.md | none`, `<ADR path> | none`
> Purpose: Record tracked feature state and observable requirements, not technical design or implementation steps.

## 1. Observable outcome

<What a user or system can observe when this feature is complete.>

## 2. Background and problem

- <current behavior>
- <trigger>
- <why now>

## 3. Goals

- <goal>

## 4. Constraints

- <behavior or contract that must remain true>
- <safety, compatibility, data, or organizational boundary>

## 5. Non-goals

- <non-goal>

## 6. Acceptance criteria

| ID | Observable criterion | Required evidence |
| --- | --- | --- |
| AC-1 | <criterion> | <unit / integration / E2E / manual evidence> |

## 7. Requirement-level open questions

- <Question that could change outcome, scope, or acceptance.>

Keep technical hypotheses and implementation questions in `design.md`.

## 8. Completion evidence

Use this section only for a local, single-slice tracked change that does not need cross-session
delivery and has no independent `plan.md`. In this bundled specs workflow, multi-slice,
cross-session, or retained-spike delivery requires a plan. Otherwise link the plan's verification
record.

- Executed verification: <command or action + result>
- E2E: passed | failed | blocked | not required
- Known limitation: none | <limitation>
- Documentation impact: none | updated `<path>`
