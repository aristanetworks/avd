<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# Data Modelling Decision Backlog

This domain covers representation choices that cross schema, Python, Ansible, rendering, and external interfaces. It is separate from the Schema
domain: Schema governs how AVD declares and validates data, while this domain governs which concepts AVD represents, where normalization occurs, and
which layer owns each representation.

| ID | Proposed decision question | Why it is architecturally significant |
| -- | -------------------------- | ------------------------------------- |
| `data-modeling/0001` | Separate external inputs, normalized internal models, and generated outputs | Prevent compatibility concerns at user boundaries from leaking into every internal calculation. |
| `data-modeling/0002` | Define ownership of structured configuration | Clarify which layer may create, extend, merge, or override each output subtree. |
| `data-modeling/0003` | Normalize data once at explicit boundaries | Avoid consumers applying conflicting aliases, defaults, and type conversions. |
| `data-modeling/0004` | Preserve semantic states through serialization | Define how absent, defaulted, empty, and null values survive model and JSON/YAML boundaries. |
| `data-modeling/0005` | Use stable identities for mergeable collections | Keep inheritance, deduplication, ordering, and conflict reporting consistent across representations. |
| `data-modeling/0006` | Keep transport and presentation details outside domain models | Allow CLI, documentation, Ansible, and API adapters to evolve without duplicating domain meaning. |
