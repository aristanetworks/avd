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

# Require primary keys for mergeable lists

## Context and Problem Statement

AVD combines list data from defaults, profiles, fabric variables, node variables, and structured-configuration contributors. Position does not identify
the same interface, peer, VLAN, or policy across those sources. Comparing entire dictionaries also fails once two sources contribute different fields
to the same object. How should list items acquire stable identity for merging and inheritance?

## Decision Drivers

- The same logical item must merge independent of its position.
- Duplicate identity should fail instead of silently overwriting data.
- Generated models need efficient keyed access and deterministic ordering.
- Some lists are intentionally ordered sequences and should not be merged by identity.

## Considered Options

- Require a schema-declared primary key for lists merged by item identity.
- Merge list items by position.
- Infer identity from all item fields or feature-specific heuristics.
- Treat every list as replace-only.

## Decision Outcome

Chosen option: **Require a schema-declared primary key for lists merged by item identity**. The key must represent stable semantic identity, be present
on every item, and be unique by default. Generated models represent these lists as indexed collections and use the primary key for lookup, merge,
inheritance, and duplicate detection.

Use an unkeyed list only when it is an ordered sequence or an atomic replace/append value. `allow_duplicate_primary_key` is an explicit exceptional
semantic and must not be used for lists expected to merge by identity.

### Consequences

- Good, because items from different sources combine predictably without depending on order.
- Good, because duplicate identifiers are detectable and lookup is efficient.
- Bad, because schema authors must choose an identity that remains stable for the life of the public model.
- Bad, because changing a primary key is a structural and potentially breaking migration.

### Confirmation

Reviews must identify the merge behavior of every new list of dictionaries. Mergeable lists require primary-key presence and uniqueness tests plus
merge and inheritance coverage. Generated-class tests must confirm indexed-list generation.

## Pros and Cons of the Options

### Schema-declared primary key

- Good, because identity is explicit and shared by validation, models, and merge logic.
- Bad, because some domains have no natural single-field identity and may require a deliberately constructed key.

### Positional merge

- Good, because no additional schema metadata is required.
- Bad, because inserting or reordering an item changes which objects merge.

### Inferred or heuristic identity

- Good, because schemas stay concise.
- Bad, because identity becomes feature-specific, unstable, and difficult for users to predict.

### Replace-only lists

- Good, because semantics are simple.
- Bad, because profiles and contributors cannot safely add fields to existing logical items.

## Future Direction and Revisit Triggers

Keep single-field primary keys as the normal identity mechanism. Revisit if repeated domains require composite identity; any composite-key design must
remain declarative, stable, and supported identically by validation, documentation, and generated models.

## Evidence

- [Input validation documentation](../../docs/contribution/input-variable-validation.md) describes primary-key presence and uniqueness.
- [`python-avd/schema_tools/generate_classes/class_src_gen.py`](../../python-avd/schema_tools/generate_classes/class_src_gen.py) generates indexed-list models from primary keys.
- [`python-avd/pyavd/_schema/models/avd_indexed_list.py`](../../python-avd/pyavd/_schema/models/avd_indexed_list.py) implements keyed merge and inheritance.
