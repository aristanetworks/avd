---
status: proposed
date: 2026-09-15
decision-type: retrospective
decision-makers: [AVD maintainers]
consulted: [AVD contributors]
informed: [AVD users and contributors]
---
<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# Separate schema domains with one-way dependencies

## Context and Current State

AVD models user design intent, EOS structured configuration, internal facts protocols, and CloudVision deployment inputs in separate named schema
domains. Some EOS Designs fields reuse EOS CLI Config Gen shapes because EOS Designs produces that structured configuration.

This record governs ownership and dependency direction between named schema domains. It does not define local `$ref` merge behavior (`schema/0006`)
or determine whether an individual field is a stable public contract.

## Implemented Decision

Each domain owns its roots and reusable definitions. Cross-domain references are permitted only when the producer-to-consumer relationship is justified,
directional, and acyclic. EOS Designs may reference EOS CLI Config Gen when the design input intentionally uses the exact structured-configuration
shape it produces; EOS CLI Config Gen does not depend on EOS Designs.

Internal facts and deployment schemas remain separate unless an explicit producer-to-consumer relationship justifies a new one-way edge. References
follow `schema/0006` and must not create a cycle.

## Consequences and Boundaries

- Each processing stage retains a named model, owner, and stability boundary while allowing exact producer-to-consumer reuse.
- A referenced-shape change can affect consumers outside the edited domain and requires dependency-aware review.
- Schema tooling and reviewers preserve the dependency direction rather than assessing each fragment in isolation.
- Similar structures remain separate when they do not represent the same semantic concept.
- Cross-domain compatibility still requires coordination when a referenced shape changes.

## Risks and Mitigations

Convenient cross-domain references can create cycles or erase ownership boundaries. Directionally justified edges, owner review, and cycle rejection
contain that risk.

## Confirmation

Schema build tooling resolves named-domain references and fails on missing targets. Reviews verify the owner and direction of every new cross-domain
reference and reject edges that would create a cycle.

## Examples or Expected Semantics

- `eos_designs` may reference an `eos_cli_config_gen` shape when the design input embeds the exact structured configuration it produces.
- The reverse dependency is rejected because rendering structured configuration must not depend on fabric-design intent.
- A new edge is rejected when following existing references would lead back to its source domain.

## Evidence

- [`python-avd/schema_tools/constants.py`](../../python-avd/schema_tools/constants.py) registers separate named schemas and output locations.
- [`python-avd/schema_tools/metaschema/resolvemodel.py`](../../python-avd/schema_tools/metaschema/resolvemodel.py) resolves named schema references.
- [`python-avd/pyavd/_eos_designs/schema/schema_fragments`](../../python-avd/pyavd/_eos_designs/schema/schema_fragments) contains deliberate references to EOS CLI Config Gen shapes.
