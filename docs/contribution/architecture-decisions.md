<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# Architecture Decisions

Arista AVD records architecturally significant choices as Architecture Decision Records (ADRs). An ADR explains the context, alternatives, outcome,
and consequences of one decision. Contributor guides continue to describe how to implement and validate changes; ADRs explain why important
boundaries and policies exist.

## Live decision log

The [AVD decision log on GitHub](https://github.com/aristanetworks/avd/tree/devel/adr) is the canonical source for current ADRs and their status.

ADRs follow the `devel` branch and can be proposed, rejected, accepted, deprecated, or superseded. A proposed ADR is under discussion and is not an
AVD compatibility commitment.

## Relationship to versioned documentation

This documentation site is published in versioned snapshots, while the decision log is a live engineering record. Consequently, ADR files are not
copied into each documentation version.

Released documentation remains the normative description of released behavior. In particular, consult the [Semantic Versioning](../versioning/semantic-versioning.md)
page for the compatibility guarantees of the AVD version you are using. ADRs provide rationale and future direction but do not retroactively change a
released contract.

## Contributing a decision

Start with the process and template in the [decision log README](https://github.com/aristanetworks/avd/blob/devel/adr/README.md). ADRs are appropriate
for decisions that materially affect component boundaries, public compatibility, schema or generated-output semantics, supported constraints, or
architectural quality gates. Ordinary code style and procedural instructions belong in the contributor guides instead.
