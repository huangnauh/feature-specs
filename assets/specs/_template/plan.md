# <feature> implementation plan

> Status: Draft | Ready | In Progress | Verifying | Blocked | Replan Required | Completed
> Created: YYYY-MM-DD
> Updated: YYYY-MM-DD
> Current slice: none | Slice N
> Current delivery stage: none | <stage composed of one or more slices>
> Blocker: none | <blocking condition>
> Design baseline: `design.md@YYYY-MM-DD` | none (<reason>)
> Related spec: `spec.md`
> ADR: none | required | `<ADR path> (Draft | Accepted)`
> Purpose: Derive delivery order and verification from stable design; do not redefine technical choices here.

**Delivery outcome:** <observable result>

**Scope:** `<path>`, `<path>`

**Constraints:** <link spec/design/ADR>

## 1. Preconditions

- [ ] Design is `Validated`, or the reason no independent design is needed is recorded
- [ ] Any contract-freezing ADR is `Accepted`
- [ ] Dependencies, blockers, compatibility, and rollback boundaries are known
- [ ] Feature state, priority, owner, dependencies, and blockers are current in `spec.md`

## 2. Delivery slices

Complete a slice by its observable outcome and gate, not by creating directories, types,
interfaces, or abstractions.

### Slice 1: <independently verifiable result>

- Status: Pending | In Progress | Blocked | Completed
- Outcome: <observable result>
- Gate: <evidence sufficient to complete this slice>
- Acceptance: `AC-N`
- Expected paths: `<path>`, `<path>` (planning scope, not a frozen file list)
- Dependencies: <slice / contract / external condition>
- Work:
  - [ ] <item>
- Verification: `<command or action>`
- Completion evidence: <result / commit / artifact>
- Design feedback trigger: <fact that requires design revision instead of another patch>

### Slice 2: <independently verifiable result>

- Status: Pending | In Progress | Blocked | Completed
- Outcome: <observable result>
- Gate: <evidence sufficient to complete this slice>
- Acceptance: `AC-N`
- Expected paths: `<path>`
- Dependencies: <...>
- Work:
  - [ ] <item>
- Verification: `<command or action>`
- Completion evidence: <...>
- Design feedback trigger: <...>

Set the plan to `Replan Required` and update design before continuing when evidence invalidates a
key assumption or implementation would change an accepted contract.

## 3. Dependency and patch order

- <dependency order>
- <reviewable patch order>

## 4. Verification and rollback

- [ ] Record external services, environment, versions, test data, and mutation scope
- [ ] Targeted gate: run the smallest relevant package or component checks per operation/slice
- [ ] Batch gate: when batch risk or this plan requires it, run the relevant repository checks and smoke tests; documentation-only batches exclude code checks
- [ ] Stage/final gate: run expensive repository-wide checks once per plan-defined delivery stage and at final delivery; one final-stage run may satisfy both
- [ ] Rerun trigger: repeat an expensive gate after dependency/generated artifact, runtime wiring, concurrency, protocol/fact-source boundary, material code, toolchain/environment changes, stale evidence, prior failure/flakiness, or an explicit user/CI request
- [ ] Run required integration, E2E, compatibility, or manual verification
- [ ] Verify rollback, or record why it is not required

### Verification record

| Date | Scope | Evidence class | Actual environment / coverage | Command / action | Result | Residual risk |
| --- | --- | --- | --- | --- | --- | --- |
| YYYY-MM-DD | <scope> | Executed / Static evidence / Not executed | <version / arch / backend / path> | `<command>` | passed / failed / blocked / not run | <risk> |

## 5. Documentation and state writeback

- [ ] Update feature state and blockers in `spec.md`
- [ ] Update long-lived architecture or module documentation only when its facts changed
- [ ] Record documentation impact

## 6. Completion

- [ ] Every slice is `Completed`
- [ ] Every acceptance criterion links to evidence
- [ ] Required verification is complete, or an actual blocker and residual risk are recorded
- [ ] Compatibility and support claims stay within actual evidence scope
- [ ] Verification, rollback, documentation, plan, and spec state are current
