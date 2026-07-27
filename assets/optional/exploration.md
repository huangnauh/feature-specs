# <exploration title>

> Status: Active | Blocked | Concluded | Abandoned
> Type: Bounded spike | Retrospective
> Date: YYYY-MM-DD
> Related design: `../design.md`
> Related hypothesis / question: <H-N or question>
> Execution source: none for non-code exploration | `<base ref or unavailable> + clean | dirty`
> Relevant change identity: none | `<paths / change scope / optional diff or artifact identity>`
> Retained outcome: none | `<later commit or artifact; not the execution snapshot>`
> Reference identity: none | `<source / build / schema identity>`

## Question

<One design question this exploration must answer.>

## Hypothesis and falsification

- Hypothesis: <candidate judgment>
- Falsification condition: <result that rejects or materially revises it>

## Invariants and scope

- <correctness, safety, compatibility, or data boundary>
- In scope: <...>
- Out of scope: <...>

## Environment

- Version / configuration:
- Architecture / operating environment:
- Backend / deployment / runtime path:
- Permissions / external dependencies:
- Test data / workload:

Do not record credentials or sensitive values.

## Minimal success evidence

<Smallest observable or machine-verifiable result that answers the question.>

## Stop conditions

- <Fact that requires stopping implementation and revising design.>

## Meaningful attempts

<Record only attempts, failures, and adjustments that affect technical judgment.>

## Evidence

### Executed

- <exact action, environment, and result>

### Static evidence

- <source, schema, artifact, or static-test fact and its limit>

### Not executed

- <missing verification, reason, and impact>

### Residual risk

- <remaining behavior outside the evidence boundary>

## Result

`Supported | Revised | Rejected | Inconclusive`

<Explain the hypothesis result and its evidence scope.>

## Design impact

- <Supported, changed, or rejected design statement>
- ADR impact: none | required | `<ADR path>`

## Implementation disposition

`keep | rework | discard`

<Explain the prototype disposition separately from the hypothesis result.>

## Exit decision

<State the exit explicitly, for example: stop; promote retained work into a validated design and
tracked delivery record; or run one distinct next experiment. Explain why the question is answered
and do not append routine delivery progress.>
