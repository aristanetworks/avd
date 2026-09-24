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

# Reuse schema definitions with explicit references

## Context and Problem Statement

AVD schemas repeat structures such as interfaces, source-interface-per-VRF settings, flow tracking, and authentication methods. Copying those shapes
makes local files self-contained but allows constraints to diverge. Unrestricted deep references reduce duplication but can couple unrelated features
to incidental schema layout. When should `$defs` and `$ref` be used?

This record governs exact semantic reuse and AVD's merge behavior at a `$ref` site. It does not make similar-looking concepts identical, create a
global shared-type domain, or relax the dependency direction established by `schema/0002`.

## Decision Drivers

- One semantic concept should not acquire contradictory copied definitions.
- References must be resolvable during validation, class generation, and documentation generation.
- Domain dependency direction from `schema/0002` must remain visible.
- A referenced list's primary-key semantics must survive class generation and merging.

## Considered Options

- Use `$defs` and explicit named-schema `$ref` values for exact semantic reuse.
- Copy every reused shape into each feature fragment.
- Build one global pool of definitions shared freely by every domain.

## Decision Outcome

Chosen option: **Use `$defs` and explicit named-schema `$ref` values for exact semantic reuse**.

Place reusable shapes without independent top-level meaning under the owning schema's `$defs`. Reference paths use the form
`<schema-name>#/<path>`. Use a reference only when the target and source represent the same semantic contract, including types, constraints, merge
identity, and future evolution. A similar-looking structure expected to diverge should be defined separately.

References must follow `schema/0002`, must not form cycles, and must resolve through the common schema store. Local description, documentation, or
deprecation metadata may specialize a reference only where resolver semantics define that merge unambiguously. The referring schema may also extend
the referenced shape with additional fields. The resolver deep-merges same-level schema data, keeps explicitly declared local values on conflicts,
and rejects incompatible types. Local extension changes the resolved referring shape; it does not modify the owned base definition.

### Consequences

- One owned definition supplies shared constraints and generated types while a consumer may add fields or specialize supported local metadata.
- Changes to a referenced definition have a wider review and compatibility impact across every resolved consumer.
- Deep reference paths couple consumers to the target schema's organization as well as its semantic contract.

### Risks and Mitigations

- **Risk:** A local override weakens a base constraint or turns exact reuse into an undocumented fork.
  **Mitigation:** Require compatible types, review the merged shape, and test both the shared fields and every local extension.

### Confirmation

Schema builds must resolve all references and validate compatible types. Reviewers must inspect reference consumers when changing a shared definition
and reject references chosen only to avoid a small amount of duplication.

## Examples or Expected Semantics

The following referring list inherits the base list and item shape, changes local identity to `profile`, and adds a `profile` field to the referenced
item keys:

```yaml
l3_interface_profiles:
  type: list
  primary_key: profile
  $ref: "eos_designs#/$defs/node_type_l3_interfaces"
  items:
    type: dict
    keys:
      profile:
        type: str
```

The resolved `l3_interface_profiles` shape contains both the referenced item keys and the added `profile` key. The `$defs` target remains unchanged.

## Pros and Cons of the Options

### Explicit semantic references

- Good, because one definition governs one concept.
- Bad, because reference impact is less local than copied YAML.

### Copied shapes

- Good, because each feature owns a self-contained definition.
- Bad, because fixes and constraints drift between copies.

### Global definition pool

- Good, because reuse is easy from anywhere.
- Bad, because ownership and dependency direction disappear and unrelated domains become coupled.

## Future Direction and Revisit Triggers

Prefer references to stable owned concepts rather than incidental deep paths. Revisit the path syntax or introduce named reusable types if refactoring
shared definitions repeatedly causes broad path churn while their semantic identity remains stable.

## Evidence

- [`python-avd/schema_tools/metaschema/resolvemodel.py`](../../python-avd/schema_tools/metaschema/resolvemodel.py) defines reference lookup and merge behavior.
- [`python-avd/pyavd/_eos_cli_config_gen/schema/schema_fragments`](../../python-avd/pyavd/_eos_cli_config_gen/schema/schema_fragments) contains `$defs` and intra-domain references.
- [`python-avd/pyavd/_eos_designs/schema/schema_fragments`](../../python-avd/pyavd/_eos_designs/schema/schema_fragments) demonstrates justified cross-domain reuse.
