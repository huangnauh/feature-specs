# <feature> design

> Status: Exploring | Proposed | Validated | Superseded
> Created: YYYY-MM-DD
> Updated: YYYY-MM-DD
> Related spec: `spec.md | none`
> Related plan: `plan.md | none`
> ADR: none | required | `<ADR path> (Draft | Accepted)`
> Experiment reference: none | `<worktree / commit / artifact>`
> Note: `Validated` establishes enough technical evidence to plan; an ADR-triggering contract still requires an `Accepted` ADR.
> Note: Review or ADR acceptance promotes only its explicit scope; other hypotheses and open questions remain unresolved.

## 1. Summary

- <problem and recommended direction>
- <what this design deliberately does not decide>

## 2. Evidence and unknowns

- `Observed`: <directly demonstrated fact and evidence scope>
- `Hypothesis`: <falsifiable candidate judgment>
- `Open`: <missing information that prevents a safe decision>

| Unknown | Classification | Next action |
| --- | --- | --- |
| <question> | Requirement decision / Contract evidence gap / Technical hypothesis / Implementation concern | required user confirmation / source audit or minimal probe / bounded spike / plan delivery |

## 3. Goals and non-goals

### Goals

- <technical goal>

### Non-goals

- <non-goal>

## 4. Invariants, candidate contracts, and implementation freedom

- `Invariant`: <correctness, safety, compatibility, or data boundary>
- Candidate contract: <behavior that may need to become stable>
- Implementation freedom: <internal choices that can vary without changing the contract>
- Boundary adjustment: no | yes — <reason, benefit, risk, and verification>

## 5. Recommended design and failure semantics

<Key flow, state machine, data flow, error priority, lifecycle, and observability.>

## 6. Alternatives

| Option | Benefit | Cost / risk | Result |
| --- | --- | --- | --- |
| <A> | <...> | <...> | Selected |
| <B> | <...> | <...> | Rejected / Open |

## 7. Compatibility, migration, rollback, and verification

- Compatibility: <API / protocol / config / schema / behavior>
- Migration: none | <method>
- Rollback: <method>
- Automated verification: <coverage>
- E2E / manual verification: <environment and checks>
- Risk and mitigation: <risk + mitigation>

## 8. Falsifiable hypotheses

| Hypothesis / question | Current basis | Verification | Falsification condition | Status |
| --- | --- | --- | --- | --- |
| <H1> | <evidence> | <experiment> | <condition> | Open / Supported / Revised / Rejected / Inconclusive |

## 9. Design delta

Record only evidence that changes technical judgment. Do not record routine delivery progress,
per-operation status, compilation fixes, or work already owned by the plan.

| Date | Source | Prior hypothesis | Evidence | Result | Design delta | Implementation disposition |
| --- | --- | --- | --- | --- | --- | --- |
| YYYY-MM-DD | Review / Spike / Implementation | <assumption> | <evidence> | Supported / Revised / Rejected / Inconclusive | <change> | keep / rework / discard |
