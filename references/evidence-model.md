# Evidence and decision model

Use this vocabulary when a design, exploration, compatibility claim, or completion statement would
otherwise blur facts and assumptions.

## Epistemic state

| Label | Meaning | Promotion rule |
| --- | --- | --- |
| `Observed` | Directly demonstrated by source, tests, protocol behavior, or an identified runtime environment | Preserve the evidence scope |
| `Hypothesis` | A falsifiable candidate judgment | Promote only after relevant evidence |
| `Open` | Missing information prevents a safe decision | Keep open until the missing fact is obtained or the scope is narrowed |
| `Decision` | A reviewed conclusion accepted for an explicit scope | Use an `Accepted` ADR when the repository's ADR trigger applies |

Design validation or ADR acceptance promotes only the statements it explicitly covers. Never
promote adjacent `Hypothesis` or `Open` items by association.

## Unknown classification

Classify an unknown by the action needed to resolve it:

| Kind | Meaning | Next action |
| --- | --- | --- |
| `Requirement decision` | An unresolved user or product choice materially changes outcome, scope, or acceptance | Ask only when the choice was not delegated or resolved by the user, accepted requirements, or an ADR; exploration cannot choose by implementation |
| `Contract evidence gap` | An authoritative read contract, call chain, schema, test, or runtime fact is missing | Audit the owner and source contract or run a minimal bounded probe before implementing dependent production logic |
| `Technical hypothesis` | A falsifiable technical judgment may invalidate the approach | Run one bounded experiment with stop conditions |
| `Implementation concern` | The design stays valid; only delivery detail remains | Put it in the plan and use `Code -> Verify` |

The classification is not permanent. Stop and reclassify when an evidence audit exposes a product
choice, new trust boundary, protocol shape, or failure model.

## Evidence class

Record verification with four distinct classes:

- `Executed`: Record the exact action, relevant inputs, environment identity, and result.
- `Static evidence`: Record what source inspection, generated artifacts, schemas, or static tests
  prove and what they cannot prove.
- `Not executed`: Record the missing verification, reason, and effect on completion or support.
- `Residual risk`: Record behavior that remains outside the evidence boundary.

Do not turn a suggested command, cross-build, fixture, or zero-event smoke into stronger runtime
evidence than it provides.

## Dirty execution state

A dirty worktree is a valid and common exploration state. Record only the source identity needed
to bound the claim:

- base ref when it is available;
- `clean | dirty`;
- relevant paths or change scope;
- diff, patch hash, or artifact identity only when exact reproduction materially affects the
  technical decision or support claim.

If the retained result is committed later, record that commit separately as a retained outcome.
Never rewrite it as the source snapshot on which historical commands were executed. When the base
ref or diff was not retained, say so and narrow the evidence claim instead of inventing precision.

## Hypothesis result and implementation disposition

Keep these separate:

- Hypothesis result: `Supported | Revised | Rejected | Inconclusive`.
- Implementation disposition: `keep | rework | discard`.

A prototype may be discarded even when it supports a hypothesis. Conversely, reusable code may
remain temporarily even after a hypothesis is revised.

`keep` does not promote a prototype into production implementation. Cross-session or multi-slice
expansion requires the corresponding delivery design to be `Validated` and a tracked plan or an
established project-defined equivalent authoritative delivery record. In the bundled specs
workflow, use a plan. Record an explicit exit decision—for example, stop, promote retained work
into design and delivery, or run one distinct next experiment—without requiring a fixed literal
unless project tooling defines one.

## Evidence scope

Attach the material dimensions to every completion, compatibility, or support claim:

- source/base revision and working-state identity when material;
- version and configuration;
- architecture and operating environment;
- backend, deployment form, and runtime path;
- test data or workload;
- permissions and external dependencies.

Use only the dimensions relevant to the feature. Never infer broad support from one environment.

## Project-defined auxiliary documents

Let the project or feature introduce auxiliary documents only when its concrete problem needs them.
Define their role locally, link their authoritative fact source, and do not promote a one-off
artifact into this cross-project workflow.
