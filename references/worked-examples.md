# Worked examples

These fictional examples illustrate the existing workflow; they are not execution records or
additional rules. Commands, dates, environments, paths, and results below are synthetic. Each pair starts from the same
known material; the recommended version adds no unsupported requirements or verification results. Read only the example relevant to the current decision.

## 1. Turn vague requirements into observable acceptance

### Known material

- User request: "Improve download stability. After a read times out, retry using the existing
  retry limit. When the limit is exhausted, return the timeout error. Do not change uploads."
- The existing configuration sets the retry limit to 3.
- The source does not specify a retry delay or a throughput target. No tests have been run.

### Poor version

"Optimize downloads with three retries at 100 ms intervals. Downloads will always succeed and
throughput will improve by 20%."

### Recommended version

A `spec.md` excerpt:

| ID | Observable criterion | Required evidence |
| --- | --- | --- |
| AC-1 | After a download read times out, the client retries up to the configured limit; the current configuration allows 3 retries. | A timeout scenario checks retry count against the configuration. |
| AC-2 | After the retry limit is exhausted, the client returns the timeout error. | A persistent-timeout scenario checks the returned error. |
| AC-3 | Upload behavior remains unchanged. | Relevant upload regression checks. |

No fixed retry delay or throughput target is claimed. Whether a delay becomes part of the public
behavior is a requirement question only if it materially changes acceptance and remains
undelegated; internal scheduling otherwise belongs to design or implementation.

These are proposed acceptance criteria and evidence requirements, not passing test results.

### Basis

`SKILL.md` sections "Classify Before Exploring" and "Maintain Fact Sources" separate observable
requirements from technical choices. The [spec template](../assets/specs/_template/spec.md)
provides acceptance and requirement-level questions. Preserve the source's explicit retry count
and scope; do not invent a delay, performance target, or success guarantee.

## 2. Classify an unknown before selecting its next action

### Known material

Four independent questions are open:

- A write may commit before the client times out. The user has not decided or delegated whether
  timeout handling may repeat the write, and no accepted requirement or ADR resolves that choice.
- An adapter must know when its source releases a borrowed buffer. The authoritative contract and
  direct call chain have not yet been inspected.
- A proposed buffer pool might reduce allocations on the existing read path. No benchmark
  supports that judgment yet.
- An accepted internal refactor has two equivalent helper names. Neither changes public behavior.

### Poor version

"All four items are unconfirmed. Ask the user to decide every item, then prototype automatic write
retries to discover the desired timeout behavior."

### Recommended version

| Question | Classification | Next action |
| --- | --- | --- |
| May a timed-out write be repeated after a possible commit? | Requirement decision | Ask the user to choose the observable timeout behavior before implementing the dependent retry policy. |
| When does the source release the borrowed buffer? | Contract evidence gap | Inspect the authoritative contract and call chain; use a minimal probe if that evidence remains insufficient. |
| Does a buffer pool reduce allocations on the read path? | Technical hypothesis | Compare allocations on the same workload with and without pooling in a bounded spike; stop when that question is answered. |
| Which equivalent internal helper name should be used? | Implementation concern | Choose using repository conventions and verify under the current plan. |

Only the first question requires a user decision on the supplied facts. If later contract evidence
reveals another material, undelegated behavior choice, reclassify it before dependent work.

### Basis

See [Unknown classification](evidence-model.md#unknown-classification). Missing evidence is not
itself a request for user approval; implementation cannot resolve an undelegated requirement by
choosing a behavior. The pool remains a hypothesis until relevant evidence supports it.

## 3. Separate partial verification from delivery completion

### Known material

- Retry implementation changes are finished.
- The plan requires both AC-1 (retry count with a fake transport) and AC-2 (resume a real download
  after disconnecting and reconnecting the test server).
- In Linux amd64 with Go 1.24.3 and a fake transport,
  `go test ./internal/download -run TestRetryTimeout -count=1` returned `ok`.
- Source inspection found retry count bounded by the configuration. It did not exercise reconnect.
- The real-server reconnect check was not run because the test server is unavailable.

### Poor version

"Completed: downloads now support reconnect. All tests passed."

### Recommended version

An excerpt from the plan's verification record, following the existing
[plan template](../assets/specs/_template/plan.md):

| Date | Scope | Evidence class | Actual environment / coverage | Command / action | Result | Residual risk |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-01-15 | AC-1: retry count | Executed | Linux amd64; Go 1.24.3; fake transport | `go test ./internal/download -run TestRetryTimeout -count=1` | passed (`ok`) | Does not exercise a real server or reconnect. |
| 2026-01-15 | Retry count bound | Static evidence | Retry branch in source; no runtime reconnect coverage | Inspect retry count against configuration | Bound found in source | Does not establish runtime reconnect behavior. |
| 2026-01-15 | AC-2: real-server reconnect | Not executed | Test server unavailable | Disconnect and reconnect during a real download | not run | Required reconnect acceptance remains unverified. |

Keep AC-2 open and record the missing server as its blocker. Do not mark the feature `Completed`;
implementation is finished, but the required delivery evidence is incomplete. Link acceptance and
slice completion evidence to the plan's verification record instead of duplicating it.

A user-facing summary derived from that record:

> 代码改动完成，任务尚未完成验收。模拟传输的重试计数检查通过；真实服务端重连检查未执行，
> 原因是测试服务端不可用。AC-2 仍待验证。证据见计划的验证记录。

### Basis

See [Evidence class](evidence-model.md#evidence-class) and
[Evidence scope](evidence-model.md#evidence-scope). A passing fake-transport test and source
inspection do not establish real reconnect support. The plan's gate determines completion;
finishing the code alone does not satisfy it.
