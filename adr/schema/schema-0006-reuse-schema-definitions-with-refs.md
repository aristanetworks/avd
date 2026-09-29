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

## Context and Current State

AVD schemas reuse structures such as interfaces, source-interface-per-VRF settings, flow tracking, and authentication methods. Reusable definitions
are stored under `$defs` and referenced by explicit named-schema `$ref` values when the structures have the same semantic contract.

This record governs exact semantic reuse and AVD's merge behavior at a `$ref` site. It does not make similar-looking concepts identical, create a global
shared-type domain, or relax the dependency direction established by `schema/0002`.

## Implemented Decision

Reusable shapes without independent top-level meaning are placed under the owning schema's `$defs`. Reference paths use
`<schema-name>#/<path>`. A reference is used only when the target and source represent the same semantic contract, including types, constraints, merge
identity, and evolution.

References follow `schema/0002`, do not form cycles, and resolve through the common schema store. The referring schema may extend the referenced shape
with additional fields. The resolver deep-merges same-level schema data, keeps explicitly declared local values on conflicts, rejects incompatible
types, and leaves the owned base definition unchanged. Local description, documentation, or deprecation metadata may specialize a reference only where
resolver semantics define that merge unambiguously.

## Consequences and Boundaries

- One owned definition supplies shared constraints and generated types while a consumer can add fields or specialize supported local metadata.
- Changes to a referenced definition have a wider review and compatibility impact across every resolved consumer.
- Deep reference paths couple consumers to the target schema's organization as well as its semantic contract.
- A similar-looking structure expected to diverge remains a separate definition.

## Risks and Mitigations

A local override can weaken a base constraint or turn exact reuse into an undocumented fork. Compatible types, review of the merged shape, and tests
covering shared fields and every local extension contain that risk.

## Confirmation

Schema builds resolve all references and validate compatible types. Reviewers inspect reference consumers when changing a shared definition and reject
references chosen only to avoid a small amount of duplication.

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

## Evidence

- [`python-avd/schema_tools/metaschema/resolvemodel.py`](../../python-avd/schema_tools/metaschema/resolvemodel.py) defines reference lookup and merge behavior.
- [`python-avd/pyavd/_eos_cli_config_gen/schema/schema_fragments`](../../python-avd/pyavd/_eos_cli_config_gen/schema/schema_fragments) contains `$defs` and intra-domain references.
- [`python-avd/pyavd/_eos_designs/schema/schema_fragments`](../../python-avd/pyavd/_eos_designs/schema/schema_fragments) demonstrates justified cross-domain reuse.
