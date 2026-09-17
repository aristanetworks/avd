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

## Context and Problem Statement

AVD combines schema defaults, inherited data, explicit user values, and structured-configuration contributors. A missing key, a lazily available
default, an explicitly empty collection, and YAML `null` can express different intent. Collapsing them into Python false-like values loses information
needed for inheritance, deletion, rendering, and serialization. Which states must the schema model preserve?

## Decision Drivers

- Inheritance needs to distinguish “not specified” from “specified as empty.”
- Schema defaults should not be mistaken for explicit user input.
- Null can intentionally block inheritance or clear nested data.
- Output renderers may omit semantically empty structures but must do so deliberately.

## Considered Options

- Preserve unset, default, explicit empty, and explicit null as distinct model states.
- Collapse unset and null, while retaining ordinary empty values.
- Collapse all false-like states and rely on truth testing.

## Decision Outcome

Chosen option: **Preserve unset, default, explicit empty, and explicit null as distinct model states wherever they affect merge, inheritance, or output**.

- **Unset** means no value was supplied and remains eligible for inheritance or lazy default access.
- **Default** is a schema-provided fallback and does not become explicit input merely because code reads it.
- **Empty** is an explicit value and can block inheritance even when a later output stage deliberately omits a semantically empty structure.
- **Null** is an explicit sentinel that can clear data or block inheritance according to the model's documented merge semantics.

Consumers must not use generic truth testing when these distinctions matter. A boundary may collapse states only when its public output contract defines
them as equivalent.

### Consequences

- Good, because inheritance and deletion preserve user intent.
- Good, because defaults can evolve without being serialized as if supplied by the user.
- Bad, because generated models require sentinels and state flags beyond ordinary Python values.
- Bad, because authors must decide whether empty and null are meaningful for each data path.

### Confirmation

Model tests must cover construction, default access, serialization, deep merge, and inheritance for all relevant states. Feature tests must use explicit
presence checks rather than truth checks when `false`, zero, empty, or null have distinct meanings.

## Pros and Cons of the Options

### Four distinct states

- Good, because the model can represent configuration intent faithfully.
- Bad, because implementation and testing are more complex.

### Unset and null combined

- Good, because normal optional Python values are sufficient.
- Bad, because an explicit clear cannot be distinguished from absence and inheritance may restore unwanted data.

### All false-like states combined

- Good, because feature code can use simple truth checks.
- Bad, because valid values such as `false`, zero, and empty collections silently acquire the wrong semantics.

## Future Direction and Revisit Triggers

Keep the states explicit in core models. Revisit serialization of defaults or empty structures only as a separately documented output contract; do not
change internal presence semantics merely to simplify one renderer.

## Evidence

- [`python-avd/pyavd/_utils/undefined.py`](../../python-avd/pyavd/_utils/undefined.py) defines a sentinel distinct from `None`.
- [`python-avd/pyavd/_schema/models/avd_model.py`](../../python-avd/pyavd/_schema/models/avd_model.py) implements lazy defaults and defined-value access.
- [`python-avd/pyavd/_schema/models/avd_base.py`](../../python-avd/pyavd/_schema/models/avd_base.py) records models created from YAML null for merge and inheritance.
