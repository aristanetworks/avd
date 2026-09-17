<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# Agent instructions

## Architecture decision records

Before planning or implementing an architecturally significant change, read the [ADR guide](adr/README.md), inspect the index for every affected
decision domain, and follow all relevant accepted ADRs. Proposed ADRs provide design context but are not authoritative.

An ADR is required when a new choice would materially affect any of these areas:

- Component boundaries or dependency direction.
- Public compatibility, versioning, SemVer, or extension contracts.
- Schema, generated output, or data-processing semantics.
- Supported runtime or dependency constraints.
- CI quality gates that preserve an architectural property.

Do not create an ADR merely to implement an accepted decision. Formatting, naming, command recipes, and ordinary review checklists belong in
contributor documentation rather than ADRs.

When a new architectural decision is needed:

1. Prefer proposing the decision before implementation.
2. Copy [the ADR template](adr/template.md) into the appropriate domain using its next four-digit number and set its status to `proposed`.
3. Record the alternatives, consequences, confirmation method, evidence, and future direction or objective revisit triggers.
4. Update the domain index. Update the root ADR index when adding a decision domain.
5. Treat the ADR as policy only after maintainers accept it.

Do not silently deviate from or rewrite the decision in an accepted ADR. Propose a new ADR that explicitly supersedes it, and cross-reference both
records with their domain-qualified identifiers.
