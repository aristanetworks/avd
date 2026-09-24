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

# Separate boundary validation from internal models

## Context and Problem Statement

External YAML and Ansible variables begin as untrusted dictionaries, while PyAVD generation benefits from typed, schema-derived objects. Repeatedly
validating loose data inside feature logic would mix user-boundary concerns with domain generation. Loading unchecked dictionaries directly into core
logic would instead produce late and inconsistent failures. Where should validation occur, and what representation should the core use?

This record governs conversion, schema validation, and model loading at public input boundaries. It does not assign cross-field or runtime-dependent
domain invariants to the static schema, and it does not define output rendering policy.

## Decision Drivers

- Users need complete, contextual validation errors before generation proceeds.
- Core code needs typed access and predictable defaults.
- Conversion must happen once and in a documented order.
- Internal models should not become a second independent validator with different rules.

## Considered Options

- Validate and convert at external boundaries, then load schema-generated models.
- Pass dictionaries through the core and validate locally where values are used.
- Let model construction alone perform all user-facing validation.

## Decision Outcome

Chosen option: **Validate and convert at external boundaries, then load schema-generated models**. Boundary adapters own user-facing type conversion,
schema validation, and aggregated diagnostics. Once data is accepted, core generation should use schema-derived models and enforce only domain
invariants that cannot be expressed as static schema constraints.

Model loading must preserve the states defined by `schema/0011`; it is not permission to reinterpret invalid external values.

### Consequences

- Users receive boundary diagnostics before generation, while core code operates on typed schema-derived models.
- Every public adapter must share or faithfully delegate to the same conversion and validation pipeline.
- Constraints that depend on several fields or runtime context remain explicit domain-validation responsibilities.

### Risks and Mitigations

- **Risk:** Ansible and direct PyAVD entry points accept or normalize the same input differently.
  **Mitigation:** Reuse one boundary implementation and maintain parity cases for every public entry point.

### Confirmation

Public Ansible and PyAVD entry points must exercise the common conversion and validation semantics before generation. Core feature code should accept
generated models rather than independently parsing raw role variables. Tests must compare diagnostics across entry points where both are public.

## Examples or Expected Semantics

The processing sequence is `raw YAML or Python data -> declared type conversion -> schema validation -> model loading -> domain invariants`. An invalid
external value is rejected before model-backed generation begins. A relationship that is valid by shape but inconsistent across several fields is
checked after model loading by the owning domain.

## Pros and Cons of the Options

### Boundary validation plus typed models

- Good, because responsibilities and failure timing are clear.
- Bad, because boundary and model-loading implementations must remain synchronized.

### Distributed dictionary validation

- Good, because checks can be written near their use.
- Bad, because errors are late, partial, duplicated, and entry-point dependent.

### Model construction as the only validator

- Good, because there is one loading operation.
- Bad, because typed-model construction is poorly suited to aggregating every user-facing validation and deprecation diagnostic.

## Future Direction and Revisit Triggers

Move shared boundary behavior toward one reusable PyAVD implementation invoked by every adapter. Revisit the separation if a generated model framework
can provide equivalent aggregated diagnostics, conversions, and deprecations without coupling feature code to validation internals.

## Evidence

- [Input validation documentation](../../docs/contribution/input-variable-validation.md) describes conversion followed by validation in central action plugins.
- [`python-avd/pyavd/_schema`](../../python-avd/pyavd/_schema) contains validators and schema-derived model foundations.
- [`python-avd/pyavd/api`](../../python-avd/pyavd/api) defines direct PyAVD boundaries.
