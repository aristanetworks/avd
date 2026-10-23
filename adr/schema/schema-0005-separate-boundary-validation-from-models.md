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

## Context and Current State

External YAML and Ansible variables begin as untrusted dictionaries, while PyAVD generation uses typed, schema-derived objects. Validating loose data
inside feature logic would mix boundary concerns with generation, while loading unchecked dictionaries would produce late and inconsistent failures.
AVD validates and converts public inputs before loading models; domain generation then enforces invariants that cannot be expressed as static schema
constraints.

This record governs conversion, schema validation, and model loading at public input boundaries. It does not assign cross-field or runtime-dependent
domain invariants to the static schema, and it does not define output rendering policy.

## Implemented Decision

Boundary adapters own user-facing type conversion, schema validation, and aggregated diagnostics. Once data is accepted, core generation uses
schema-derived models and enforces only domain invariants that cannot be expressed as static schema constraints.

Model loading preserves the states defined by `schema/0011`; it does not reinterpret invalid external values.

## Consequences and Boundaries

- Users receive boundary diagnostics before generation, while core code operates on typed schema-derived models.
- Public Ansible and PyAVD adapters share or delegate to the same conversion and validation pipeline.
- Constraints that depend on several fields or runtime context remain explicit domain-validation responsibilities.
- A difference between public entry points is a compatibility defect rather than an alternate validation policy.

## Risks and Mitigations

Ansible and direct PyAVD entry points can accept or normalize the same input differently. A shared boundary implementation and parity coverage for public
entry points contain that risk.

## Confirmation

Public Ansible and PyAVD entry points exercise the common conversion and validation semantics before generation. Core feature code accepts generated
models rather than independently parsing raw role variables. Where both entry points are public, tests compare their diagnostics.

## Examples or Expected Semantics

The processing sequence is `raw YAML or Python data -> declared type conversion -> schema validation -> model loading -> domain invariants`. An invalid
external value is rejected before model-backed generation begins. A relationship that is valid by shape but inconsistent across several fields is
checked after model loading by the owning domain.

## Evidence

- [Input validation documentation](../../docs/contribution/input-variable-validation.md) describes conversion followed by validation in central action plugins.
- [`python-avd/pyavd/_schema`](../../python-avd/pyavd/_schema) contains validators and schema-derived model foundations.
- [`python-avd/pyavd/api`](../../python-avd/pyavd/api) defines direct PyAVD boundaries.
