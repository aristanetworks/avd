<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# AVD Architecture Decision Records

This directory is the decision log for architecturally significant choices in Arista AVD. An Architecture Decision Record (ADR) records the context,
decision, boundaries, consequences, and evidence for one architectural direction. Prospective records also explain the alternatives and trade-offs
behind a decision. It complements implementation and contributor documentation by recording the contract that guides future work.

Prospective records use an AVD adaptation of the [MADR 4.0 template](https://github.com/adr/madr/tree/4.0.0), because considered options and their
trade-offs are essential when a decision is still being made. Retrospective records use an evidence-first format because their purpose is to document
observable current design without reconstructing a decision process that was not recorded.

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
repository evidence and describe the implemented decision, its boundaries, consequences, and confirmation. It must not invent historical drivers,
alternatives, or rationale. A present-day alternative belongs in a new prospective ADR or a separately labelled change proposal.

## Authoring and review

1. Copy [the prospective template](template.md) or [the retrospective template](template-retrospective.md) into the appropriate domain directory using
   `<domain>-<four-digit-number>-<short-title>.md`.
2. Keep the record focused on one decision. Prospective records must give every viable alternative a fair treatment; retrospective records must
   describe only the observable current design and its evidence.
3. State boundaries with adjacent decisions briefly in the context instead of creating artificial scope sections.
4. Describe consequences, confirmation, and evidence for both record types. Add an example when it materially clarifies behavior.
5. Add the record to the domain index and link related ADRs with qualified identifiers.
6. State future direction only for a prospective decision or when it is already an explicit part of the current contract.
7. Submit the proposed ADR for maintainer review before treating it as policy.

The prospective template follows MADR 4.0 by placing the concise Decision Outcome before the detailed option comparison. The retrospective template
uses `Implemented Decision` and omits reconstructed option analysis, so the record remains an accurate current-state reference.

Released user and contributor documentation remains the normative description of released AVD behavior. The repository decision log follows `devel`
and can contain proposed or future decisions that do not apply to a released version yet. ADRs remain in the repository instead of the versioned
documentation site because their evidence links and review context follow the source tree.
