---
status: proposed
date: 2026-09-15
decision-type: prospective
decision-makers: [AVD maintainers]
consulted: [AVD contributors]
informed: [AVD users and contributors]
---
<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# Define schema feature semantics per consumer

## Context and Problem Statement

AVD Schema is not interpreted by one engine. Build tooling validates schema authorship and generates combined schemas, Python models, editor metadata,
and documentation. At runtime, `pyavd-utils` validates and converts external data, while generated models implement defaults, merge and inheritance,
and serialization behavior.

Some vocabulary is intentionally local to one consumer. For example, `documentation_options` affects generated documentation without changing
runtime data. Other fields cross boundaries: `allow_other_keys` affects both validation and whether generated models preserve extension data, while a
`default` may be documented even though it is applied lazily by a generated model rather than inserted by boundary validation. Requiring identical
behavior everywhere would be wrong, but leaving consumer scope implicit can produce documentation, validation, and model behavior that contradict
one another. How should a new schema feature define its consumer scope and observable semantics?

This record governs new meta-schema vocabulary and changes to the meaning of existing vocabulary. It does not require every consumer to implement
every field or to share an implementation.

## Decision Drivers

- Ansible and direct PyAVD entry points must expose compatible observable behavior when they use the same schema path.
- Documentation and editor assistance must distinguish runtime constraints from documentation-only metadata.
- Cross-cutting fields must not be accepted by validation and then discarded or reinterpreted by generated models.
- Consumer-local metadata must remain possible without forcing meaningless implementations elsewhere.

## Considered Options

- Require each schema feature to define its affected consumers and observable semantics before adoption.
- Require identical implementation and behavior in every schema consumer.
- Allow consumer-specific interpretation without an explicit central contract.
- Designate only runtime validation as authoritative and treat other consumers as best-effort.

## Decision Outcome

Chosen option: **Require each schema feature to define its affected consumers and observable semantics before adoption**.

A proposal for new meta-schema vocabulary must identify its effects on boundary validation and conversion, generated models and merge behavior,
documentation and editor artifacts, and schema build tooling. For each consumer, the proposal must state the intended behavior or explicitly state
that the field has no effect. Consumers required for the observable contract must be implemented and covered together; implementation details may
differ.

A consumer-local field may be implemented only by its owner. Cross-consumer parity is required only for shared observable semantics, not for
internal processing steps or for metadata outside a consumer's scope.

### Consequences

- Each field has an explicit scope instead of an assumption that every consumer treats it identically.
- Adding cross-cutting vocabulary requires an impact analysis and coordinated changes in affected implementations.
- Consumer-local documentation or generation metadata can evolve without adding no-op runtime implementations.

### Risks and Mitigations

- **Risk:** Authors classify a cross-cutting feature as consumer-local and hide an observable inconsistency.
  **Mitigation:** Review the feature against boundary validation, generated models, merge and serialization, documentation, editor artifacts, and build
  tooling; require coverage wherever behavior is observable.

### Confirmation

Meta-schema changes must include a consumer-impact list and focused validation, generated-model, merge, documentation, or build coverage as applicable.
Review must reject a field whose effect is undefined for a consumer needed by its stated contract.

## Examples or Expected Semantics

- `documentation_options` may alter table placement without affecting validation or generated-model values; that consumer-local scope is explicit.
- `allow_other_keys` affects whether input is valid and whether a generated model retains unknown keys. Those observable behaviors must agree even
  though validator and model implementations differ.
- A `default` can be shown in documentation and exposed lazily by a generated model while boundary validation leaves an absent key absent. That is a
  valid difference when the field's contract states where the default is applied.

## Pros and Cons of the Options

### Explicit affected consumers and semantics

- Good, because shared behavior is consistent without inventing work for unrelated consumers.
- Bad, because every new schema feature requires an impact analysis before implementation.

### Identical behavior in every consumer

- Good, because parity is simple to state.
- Bad, because documentation metadata, boundary conversion, model defaults, and merge behavior have legitimately different owners and phases.

### Consumer-specific interpretation

- Good, because individual tools can evolve quickly.
- Bad, because validity and generated behavior depend on which entry point processes the data.

### Validator-only authority

- Good, because there is one minimal definition of validity.
- Bad, because valid data can still be represented, merged, or documented incorrectly.

## Future Direction and Revisit Triggers

Add a lightweight consumer-impact checklist for meta-schema changes and shared fixtures where behavior crosses consumer boundaries. Revisit this
decision if schema consumers become independently versioned profiles with explicit conversion contracts.

## Evidence

- [`python-avd/schema_tools/build_schemas.py`](../../python-avd/schema_tools/build_schemas.py) feeds multiple generated artifacts from one schema store.
- [`python-avd/schema_tools/generate_classes`](../../python-avd/schema_tools/generate_classes) implements generated-model semantics.
- [`python-avd/schema_tools/generate_docs`](../../python-avd/schema_tools/generate_docs) consumes documentation-specific schema metadata.
- [`python-avd/pyavd/_schema`](../../python-avd/pyavd/_schema) implements model, merge, and serialization behavior.
- [`validate_inputs.py`](../../python-avd/pyavd/validate_inputs.py) delegates boundary validation and conversion to `pyavd-utils`.
