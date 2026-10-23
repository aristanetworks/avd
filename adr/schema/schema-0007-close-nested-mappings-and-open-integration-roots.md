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

# Close controlled mappings and open only integration roots

## Context and Current State

AVD rejects unknown keys in controlled mappings to catch misspellings and unsupported input early. It also consumes top-level Ansible variable
namespaces and supports deliberate custom-data or integration boundaries where unrelated keys must coexist.

This record governs unknown keys in owned mappings and shared integration boundaries. It does not define data-declared key names, which use the bounded
dynamic mechanisms in `schema/0008`, or authorize untyped mappings as a shortcut for incomplete schema work.

## Implemented Decision

Dictionary schemas reject undeclared keys by default. `allow_other_keys: true` is used only where the mapping intentionally contains data owned
outside that schema, such as a role-variable root or documented custom-data boundary. It is not used to defer modeling supported AVD settings.

Reserved underscore-prefixed custom keys may coexist where documented, but AVD does not assign behavior to unknown custom keys. A mapping whose key
names come from a user-defined catalog uses a documented dynamic-key mechanism under `schema/0008` instead of becoming untyped.

## Consequences and Boundaries

- Unknown nested AVD settings fail validation, and adding a supported setting requires a schema change.
- Shared inventory and documented custom-data boundaries may retain keys owned outside the local schema.
- An open root cannot classify every unknown top-level key as a typo because ownership may belong to another integration.
- Each open boundary requires a stated external owner or extension contract.

## Risks and Mitigations

A broadly open mapping can hide misspelled AVD settings. Requiring an external owner or extension contract, keeping controlled descendants closed, and
testing each new open boundary contain that risk.

## Confirmation

The meta-schema default for `allow_other_keys` is false. Reviews require a stated external owner or extension contract for each true value. Validation
tests cover rejection in controlled mappings and retention at documented open boundaries.

## Examples or Expected Semantics

A misspelled key such as `uplnk_type` inside an AVD-controlled node setting is rejected. An unrelated variable at a documented shared inventory root is
retained because AVD does not own that namespace. A mapping whose key names come from a user-defined catalog remains typed through `dynamic_keys`.

## Evidence

- [Input validation documentation](../../docs/contribution/input-variable-validation.md) describes `allow_other_keys` and custom underscore-prefixed keys.
- [`python-avd/schema_tools/metaschema/meta_schema_model.py`](../../python-avd/schema_tools/metaschema/meta_schema_model.py) defaults `allow_other_keys` to false.
- [`python-avd/pyavd/_eos_designs/schema/schema_fragments/_defaults.schema.yml`](../../python-avd/pyavd/_eos_designs/schema/schema_fragments/_defaults.schema.yml) demonstrates an open integration root.
