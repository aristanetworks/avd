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

## Context and Current State

AVD combines list data from defaults, profiles, fabric variables, node variables, and structured-configuration contributors. Mergeable dictionary
items use a stable semantic identity rather than list position or a comparison of complete dictionaries.

This record governs lists whose dictionary items merge by logical identity across input sources. It does not require primary keys for ordered
sequences, atomic replace-only lists, or lists whose documented behavior is append-only.

## Implemented Decision

Lists merged by item identity require a schema-declared primary key. The key must be present on every item and unique by default. Generated models use
the primary key for lookup, merge, inheritance, and duplicate detection.

An unkeyed list is used only when it is an ordered sequence or an atomic replace/append value. `allow_duplicate_primary_key` is an explicit exceptional
semantic and is not used for lists expected to merge by identity.

## Consequences and Boundaries

- Mergeable items combine independently of position and duplicate identity is detectable.
- The chosen primary key becomes structural identity and must remain stable for the life of the public model.
- Lists without identity require an explicit ordered, append, or replace semantic instead of heuristic merge behavior.
- Some domains without a natural single-field identity require a deliberately constructed key.

## Risks and Mitigations

A convenient but unstable field can be selected as identity and later require a breaking migration. Review keys for domain-level permanence and require
migration planning before changing an established primary key.

## Confirmation

Reviews identify the merge behavior of every new list of dictionaries. Mergeable lists have primary-key presence and uniqueness coverage, merge and
inheritance coverage, and generated indexed-list models.

## Examples or Expected Semantics

Given `primary_key: name`, one source may define `{name: Ethernet1, description: Uplink}` and another may define `{name: Ethernet1, shutdown: false}`.
They resolve as one logical item containing both contributed fields, regardless of list position. Duplicate `name: Ethernet1` items in one uniqueness scope
are rejected instead of silently overwriting one another.

## Evidence

- [Input validation documentation](../../docs/contribution/input-variable-validation.md) describes primary-key presence and uniqueness.
- [`python-avd/schema_tools/generate_classes/class_src_gen.py`](../../python-avd/schema_tools/generate_classes/class_src_gen.py) generates indexed-list models from primary keys.
- [`python-avd/pyavd/_schema/models/avd_indexed_list.py`](../../python-avd/pyavd/_schema/models/avd_indexed_list.py) implements keyed merge and inheritance.
