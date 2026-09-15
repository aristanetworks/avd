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

- Good, because users receive early and consistent validation results.
- Good, because core code can rely on typed access instead of defensive dictionary traversal.
- Bad, because entry points must share or faithfully delegate to the same boundary pipeline.
- Bad, because domain validation still needs a clear home when constraints depend on multiple fields or runtime context.

### Confirmation

Public Ansible and PyAVD entry points must exercise the common conversion and validation semantics before generation. Core feature code should accept
generated models rather than independently parsing raw role variables. Tests must compare diagnostics across entry points where both are public.

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
