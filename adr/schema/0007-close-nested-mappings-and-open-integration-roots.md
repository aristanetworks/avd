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

## Context and Problem Statement

Rejecting unknown mapping keys catches misspellings and unsupported input early. AVD nevertheless consumes top-level Ansible variable namespaces and
supports deliberate custom-data or integration boundaries where unrelated keys must coexist. Should dictionary schemas reject or retain unknown keys?

## Decision Drivers

- Misspelled nested settings must not be silently ignored.
- AVD must coexist with inventory variables owned by Ansible, other collections, and user integrations.
- Generated models need to know whether unknown data should be discarded, retained, or rejected.
- Openness should be an explicit extension contract, not a convenience used to avoid schema authoring.

## Considered Options

- Close controlled nested mappings and explicitly open only integration roots.
- Reject unknown keys everywhere.
- Allow unknown keys in every mapping.

## Decision Outcome

Chosen option: **Close controlled nested mappings and explicitly open only integration roots**. Dictionary schemas reject undeclared keys by default.
Use `allow_other_keys: true` only where the mapping intentionally contains data owned outside that schema, such as a role-variable root or documented
custom-data boundary. It must not be used merely to defer modeling supported AVD settings.

Reserved underscore-prefixed custom keys may coexist where documented, but AVD must not assign behavior to unknown custom keys. A mapping that accepts
arbitrary keys with a common value shape should use a documented dynamic-key mechanism under `schema/0008` instead of becoming untyped.

### Consequences

- Good, because invalid nested AVD keys fail early instead of disappearing from output.
- Good, because intentional integration boundaries remain possible.
- Bad, because adding a supported nested setting always requires a schema change.
- Bad, because open roots cannot detect every top-level typo without knowing which project owns the key.

### Confirmation

The meta-schema default for `allow_other_keys` remains false. Reviewers must require a stated external owner or extension contract for each true value.
Validation tests must cover both rejection in a controlled mapping and retention at each new open boundary.

## Pros and Cons of the Options

### Closed mappings with explicit open roots

- Good, because strictness follows ownership.
- Bad, because the validation rule depends on knowing the boundary's purpose.

### Closed everywhere

- Good, because every typo is detectable.
- Bad, because AVD could not safely consume shared Ansible inventory namespaces or extensible custom data.

### Open everywhere

- Good, because schemas never block new keys.
- Bad, because typos and unsupported settings appear valid and can silently change generated results.

## Future Direction and Revisit Triggers

Reduce open surface as ownership becomes more precise, but do not close shared integration roots without a migration path. Revisit underscore-prefixed
custom keys if AVD introduces a formally namespaced metadata or extension model.

## Evidence

- [Input validation documentation](../../docs/contribution/input-variable-validation.md) describes `allow_other_keys` and custom underscore-prefixed keys.
- [`python-avd/schema_tools/metaschema/meta_schema_model.py`](../../python-avd/schema_tools/metaschema/meta_schema_model.py) defaults `allow_other_keys` to false.
- [`python-avd/pyavd/_eos_designs/schema/schema_fragments/_defaults.schema.yml`](../../python-avd/pyavd/_eos_designs/schema/schema_fragments/_defaults.schema.yml) demonstrates an open integration root.
