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

Numbering restarts in each domain. Always qualify an ADR reference with its domain, for example `schema/0006` or `versioning/0003`.

| Domain | Purpose | Current state |
| ------ | ------- | ------------- |
| [Versioning](versioning/README.md) | Product versioning, SemVer surfaces, deprecation, and planned future behavior | Initial records proposed |
| [Schema](schema/README.md) | AVD Schema authoring, composition, validation, generation, and evolution | Initial records proposed |
| [Code](code/README.md) | Python architecture and authoring boundaries | Backlog |
| [Jinja2](jinja2/README.md) | Template responsibilities, compilation, ordering, and extension points | Backlog |
| [CI](ci/README.md) | Test-layer selection, generated artifacts, compatibility matrices, and release validation | Backlog |
| [Dependencies](dependencies/README.md) | Dependency sources, constraints, automation, exceptions, and supply-chain pinning | Backlog |
| [Ansible collection](ansible-collection/README.md) | Controller execution, PyAVD delegation, public interfaces, packaging, and support | Backlog |

## When to write an ADR

Write an ADR when a choice has a measurable effect on one or more of the following:

- AVD component boundaries or direction of dependencies.
- A public compatibility, versioning, or extension contract.
- Schema, generated output, or data-processing semantics.
- Supported runtime or dependency constraints.
- A quality gate needed to preserve an architectural property.

Keep formatting rules, naming preferences, command recipes, and ordinary review checklists in contributor documentation. If reversing a choice would
not meaningfully affect AVD's structure or qualities, it probably does not need an ADR.

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

1. Copy [the template](template.md) into the appropriate domain using the next four-digit number.
2. Keep the record focused on one decision and give every viable alternative a fair treatment.
3. Add the record to the domain index and link any related ADRs with qualified identifiers.
4. Describe how conformance can be confirmed in code, tests, generated artifacts, or review.
5. State future direction and objective revisit triggers without making unsupported roadmap commitments.
6. Submit the proposed ADR for maintainer review before treating it as policy.

Released user and contributor documentation remains the normative description of released AVD behavior. The decision log follows `devel` and can
contain proposed or future decisions that do not apply to a released version yet.
