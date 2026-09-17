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

## Context and Problem Statement

AVD models user design intent, EOS structured configuration, internal facts protocols, and CloudVision deployment inputs. These models have different
owners and stability promises, but some EOS Designs fields deliberately reuse EOS CLI Config Gen shapes because EOS Designs produces that structured
configuration. Should all data share one schema graph or remain in separate domains?

## Decision Drivers

- Intent models and rendered structured configuration evolve for different reasons.
- Domain ownership and public stability need to remain visible.
- Legitimate semantic reuse should not require copied definitions.
- Circular references would couple generation stages and complicate generated classes.

## Considered Options

- Keep separate named schema domains and permit only acyclic, directionally justified references.
- Combine all AVD data into one global schema.
- Forbid all cross-domain references and copy shared structures.

## Decision Outcome

Chosen option: **Keep separate named schema domains and permit only acyclic, directionally justified references**.

Each domain owns its roots and reusable definitions. Self-references are allowed. EOS Designs may reference EOS CLI Config Gen when design input
intentionally uses the exact structured-configuration shape it will produce. EOS CLI Config Gen must not depend on EOS Designs. Internal facts and
deployment schemas remain separate unless an explicit producer-to-consumer relationship justifies a new one-way edge.

Cross-domain references follow `schema/0006` and must not create a cycle.

### Consequences

- Good, because each processing stage retains a clear model and stability boundary.
- Good, because exact producer-to-consumer reuse is possible without duplication.
- Bad, because moving or changing a referenced shape can affect another domain.
- Bad, because reviewers must assess the dependency graph rather than only the edited file.

### Confirmation

Schema build tooling must resolve named-domain references and fail on missing targets. Review must verify the owner and direction of every new
cross-domain reference. A dependency-cycle check should be added if the graph becomes too large to inspect reliably.

## Pros and Cons of the Options

### Separate domains with acyclic references

- Good, because domain boundaries and legitimate reuse coexist.
- Bad, because cross-domain compatibility still needs coordination.

### One global schema

- Good, because any definition is directly reusable.
- Bad, because intent, intermediate, output, and deployment models lose distinct ownership and stability.

### No cross-domain references

- Good, because domains can change independently.
- Bad, because identical concepts are copied and eventually diverge.

## Future Direction and Revisit Triggers

Preserve the current direction from EOS Designs intent toward EOS CLI Config Gen structured configuration. Revisit an edge when a referenced structure
stops representing the same semantic concept, or when a new shared domain with independent ownership would remove repeated justified references.

## Evidence

- [`python-avd/schema_tools/constants.py`](../../python-avd/schema_tools/constants.py) registers separate named schemas and output locations.
- [`python-avd/schema_tools/metaschema/resolvemodel.py`](../../python-avd/schema_tools/metaschema/resolvemodel.py) resolves named schema references.
- [`python-avd/pyavd/_eos_designs/schema/schema_fragments`](../../python-avd/pyavd/_eos_designs/schema/schema_fragments) contains deliberate references to EOS CLI Config Gen shapes.
