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

# Model unset, default, empty, and null distinctly

## Context and Current State

AVD combines schema defaults, inherited data, explicit user values, and structured-configuration contributors. A missing key, a lazily available
default, an explicitly empty collection, and YAML `null` express different intent when they affect inheritance, deletion, rendering, or serialization.

This record governs presence states in schema-derived models and operations where presence affects merge or inheritance. It does not prescribe whether
every output renderer emits empty or defaulted values; each public output contract decides which equivalent states it serializes.

## Implemented Decision

AVD preserves unset, default, explicit empty, and explicit null as distinct model states wherever they affect merge, inheritance, or output.

- **Unset** means no value was supplied and remains eligible for inheritance or lazy default access.
- **Default** is a schema-provided fallback and does not become explicit input merely because code reads it.
- **Empty** is an explicit value and can block inheritance even when a later output stage omits a semantically empty structure.
- **Null** is an explicit sentinel that can clear data or block inheritance according to the model's documented merge semantics.

Consumers do not use generic truth testing when these distinctions matter. A boundary may collapse states only when its public output contract defines
them as equivalent.

## Consequences and Boundaries

- Inheritance, deletion, and default access preserve whether a value was absent or explicitly supplied.
- Generated models require presence sentinels and state-aware access beyond ordinary Python false-like values.
- Schema and feature authors define when empty and null have distinct meaning along each data path.

## Risks and Mitigations

Generic truth testing can collapse valid `false`, zero, empty, null, and unset states. Presence-aware model helpers and coverage of construction, merge,
inheritance, and serialization for each meaningful state contain that risk.

## Confirmation

Model coverage includes construction, default access, serialization, deep merge, and inheritance for relevant states. Feature code uses explicit
presence checks rather than truth checks when `false`, zero, empty, or null have distinct meanings.

## Examples or Expected Semantics

| Input state | Expected model meaning |
| ----------- | ---------------------- |
| Key absent | Unset; inheritance or lazy schema default may still apply. |
| Schema default read | Available as a fallback without becoming explicit user input. |
| `items: []` | Explicitly empty; may block inherited list content. |
| `items: null` | Explicit null sentinel; may clear or block inheritance according to the documented merge contract. |

## Evidence

- [`python-avd/pyavd/_utils/undefined.py`](../../python-avd/pyavd/_utils/undefined.py) defines a sentinel distinct from `None`.
- [`python-avd/pyavd/_schema/models/avd_model.py`](../../python-avd/pyavd/_schema/models/avd_model.py) implements lazy defaults and defined-value access.
- [`python-avd/pyavd/_schema/models/avd_base.py`](../../python-avd/pyavd/_schema/models/avd_base.py) records models created from YAML null for merge and inheritance.
