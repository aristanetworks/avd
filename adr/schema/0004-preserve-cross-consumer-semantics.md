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

# Preserve schema semantics across consumers

## Context and Problem Statement

The AVD Schema is consumed by runtime validation and conversion, generated Python models, merge and inheritance logic, generated documentation, and
editor tooling. A keyword implemented by only one consumer can make an input appear valid in one path and behave differently in another. What level
of cross-consumer parity is required for schema vocabulary?

## Decision Drivers

- The same input must have predictable meaning through Ansible and direct PyAVD APIs.
- Documentation and editor assistance must not advertise unsupported runtime behavior.
- Generated models must preserve validation, default, null, and merge semantics.
- Some metadata is intentionally relevant only to documentation or generation and should be labelled accordingly.

## Considered Options

- Require each keyword to define semantics for every relevant consumer before adoption.
- Allow consumer-specific interpretation without a central contract.
- Designate only runtime validation as authoritative and treat other consumers as best-effort.

## Decision Outcome

Chosen option: **Require each keyword to define semantics for every relevant consumer before adoption**.

A new meta-schema field must identify which consumers it affects and include implementation and confirmation for each of them in the same change. A
field intentionally limited to documentation or generation must be named and documented as metadata; other consumers must ignore it deliberately, not
accidentally. Unsupported consumers must fail or omit the feature explicitly rather than silently applying different semantics.

### Consequences

- Good, because one schema remains a credible shared contract.
- Good, because direct PyAVD and Ansible paths cannot drift unnoticed.
- Bad, because adding schema vocabulary requires coordinated changes across multiple tools.
- Bad, because the least capable required consumer can constrain an otherwise useful feature.

### Confirmation

Meta-schema changes must include focused validation, model-generation, runtime-model, and documentation coverage as applicable. Reviews must include a
consumer-impact list and reject a keyword whose meaning is undefined in any affected path.

## Pros and Cons of the Options

### Required semantic parity

- Good, because authored schemas have one explainable meaning.
- Bad, because cross-tool implementation raises the cost of new features.

### Consumer-specific interpretation

- Good, because individual tools can evolve quickly.
- Bad, because validity and generated behavior depend on which entry point processes the data.

### Validator-only authority

- Good, because there is one minimal definition of validity.
- Bad, because valid data can still be represented, merged, or documented incorrectly.

## Future Direction and Revisit Triggers

Work toward generated conformance cases that exercise one schema fixture through all consumers. Revisit only if consumers are deliberately separated
behind independently versioned schema profiles with explicit conversion between them.

## Evidence

- [`python-avd/schema_tools/build_schemas.py`](../../python-avd/schema_tools/build_schemas.py) feeds validation, documentation, and class generation from one store.
- [`python-avd/schema_tools/generate_classes`](../../python-avd/schema_tools/generate_classes) implements typed-model semantics.
- [`python-avd/pyavd/_schema`](../../python-avd/pyavd/_schema) implements runtime validation and model behavior.
