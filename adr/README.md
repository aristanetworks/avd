<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# AVD Architecture Decision Records

This directory is the decision log for architecturally significant choices in Arista AVD. An Architecture Decision Record (ADR) explains the
context, alternatives, outcome, and consequences of one decision. It complements implementation and contributor documentation by recording why a
design was chosen.

The records use an AVD adaptation of the [MADR 4.0 template](https://github.com/adr/madr/tree/4.0.0). MADR was selected because considered options and
their trade-offs are essential to understanding a decision; a rule without its alternatives is not an architectural rationale.

## Decision domains

Numbering restarts in each domain. Always qualify an ADR reference with its domain, for example `schema/0006` or `versioning/0003`. The filename also
includes the domain, such as `schema/schema-0006-reuse-schema-definitions-with-refs.md`, so the decision area remains visible when a file is linked,
downloaded, or copied outside its domain directory.

| Domain | Purpose | Current state |
| ------ | ------- | ------------- |
| [Versioning](versioning/README.md) | Product lifecycle, versioning, SemVer surfaces, deprecation, and planned future behavior | Initial records proposed |
| [Schema](schema/README.md) | AVD Schema authoring, composition, validation, generation, and evolution | Initial records proposed |
| [Data modelling](data-modeling/README.md) | Representation boundaries, ownership, normalization, serialization, and cross-area modelling rules | Backlog |
| [Code](code/README.md) | Python architecture and authoring boundaries | Backlog |
| [Jinja2](jinja2/README.md) | Template responsibilities, compilation, ordering, and extension points | Backlog |
| [CI](ci/README.md) | Test-layer selection, generated artifacts, compatibility matrices, and release validation | Backlog |
| [Dependencies](dependencies/README.md) | Dependency sources, constraints, automation, exceptions, and supply-chain pinning | Backlog |
| [Ansible collection](ansible-collection/README.md) | Controller execution, PyAVD delegation, public interfaces, packaging, testing, and support | Backlog |

## When to write an ADR

Use an ADR when all of these conditions are true:

- There are multiple viable alternatives, and selecting between them requires an architectural trade-off rather than a local implementation choice.
- The outcome is intended to guide more than one implementation or change, or it establishes a public or cross-component contract.
- Reversing the outcome would require coordinated migration, compatibility handling, or changes across components.

Keep local and readily reversible implementation details, formatting rules, naming preferences, command recipes, and ordinary review checklists in
contributor documentation, source comments, or code review. Implementing an accepted ADR does not require another ADR unless the implementation
introduces a distinct decision that passes the test above.

## Lifecycle

All new records start as `proposed`. AVD maintainers determine the outcome during review.

- `proposed`: Under consideration and not yet authoritative.
- `accepted`: Approved and expected to guide implementation and review.
- `rejected`: Considered but not selected.
- `deprecated`: Retained for history but no longer recommended for new work.
- `superseded`: Replaced by a newer, explicitly linked ADR.

Do not rewrite an accepted ADR to make a different decision. Add a new ADR that supersedes it. Corrections, clearer evidence, and links may be added as
long as they do not change the recorded outcome or rationale.

Initial records can be marked `decision-type: retrospective` when they formalize an observable existing design. A retrospective ADR must cite current
repository evidence and frame its alternatives as a present-day evaluation. It must not present reconstructed reasoning as historical fact.

## Authoring and review

1. Copy [the template](template.md) into the appropriate domain directory using `<domain>-<four-digit-number>-<short-title>.md`.
2. Keep the record focused on one decision and give every viable alternative a fair treatment. If its boundary with an adjacent decision is easy to
   confuse, state that boundary briefly in the context.
3. Describe the selected outcome's effects neutrally under Consequences; reserve `Good` and `Bad` comparisons for the option analysis.
4. Add a focused example when it clarifies input, output, processing order, or accepted and rejected behavior.
5. Add the record to the domain index and link any related ADRs with qualified identifiers.
6. Describe how conformance can be confirmed in code, tests, generated artifacts, or review.
7. State future direction and objective revisit triggers without making unsupported roadmap commitments.
8. Submit the proposed ADR for maintainer review before treating it as policy.

The template follows MADR 4.0 by placing the concise Decision Outcome before the detailed option comparison. This makes accepted records fast to
scan; it does not imply that authors choose an outcome before evaluating alternatives. The Considered Options and Decision Drivers establish the
comparison, and Pros and Cons records the detailed trade-offs that justify the outcome.

Released user and contributor documentation remains the normative description of released AVD behavior. The repository decision log follows `devel`
and can contain proposed or future decisions that do not apply to a released version yet. ADRs remain in the repository instead of the versioned
documentation site because their evidence links and review context follow the source tree.
