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

# Use a constrained AVD YAML schema dialect

## Context and Problem Statement

AVD needs one model to drive input validation, type conversion, inheritance and merge behavior, generated Python classes, and data-model documentation.
General-purpose formats such as JSON Schema and Ansible argument specifications cover parts of this problem but do not directly express every AVD
semantic. Should AVD adopt one of those formats directly or retain a purpose-built dialect?

This retrospective ADR ratifies the proprietary schema format described by the current meta-schema and contributor documentation. It does not claim
that the options below reproduce the original adoption discussion.

## Decision Drivers

- One authored model should serve validation, code generation, merge semantics, and documentation.
- The supported vocabulary must be finite and mechanically validated.
- AVD-specific concepts such as primary-keyed lists, explicit conversions, dynamic keys, and deprecation conflicts must be representable.
- Schema authors need YAML editor assistance and clear generated documentation.

## Considered Options

- Use a constrained AVD YAML dialect governed by a JSON Schema meta-schema.
- Use standard JSON Schema directly.
- Use Ansible argument specifications as the source model.
- Maintain independent models for each consumer.

## Decision Outcome

Chosen option: **Use a constrained AVD YAML dialect governed by a JSON Schema meta-schema**. Only vocabulary defined by the AVD meta-schema is supported.
The dialect may be inspired by other schema systems without claiming full compatibility with them.

New vocabulary must first establish semantics for every relevant consumer under `schema/0004`; placing an arbitrary JSON Schema keyword in an AVD
schema does not make it supported.

### Consequences

- Good, because AVD-specific data and merge semantics can be modeled once.
- Good, because the meta-schema bounds the language and enables editor validation.
- Bad, because contributors must learn an AVD-specific format.
- Bad, because integrations expecting standard JSON Schema require a converter or a deliberately reduced representation.

### Confirmation

Schema files must validate against `avd_meta_schema.json`. Contributor documentation and generated tables must list the same supported types and
options. Reviews must reject undeclared vocabulary even when a general JSON Schema implementation would understand it.

## Pros and Cons of the Options

### Constrained AVD YAML dialect

- Good, because one language can express the full AVD generation model.
- Good, because supported features remain intentionally bounded.
- Bad, because AVD owns the validator, model generator, documentation generator, and compatibility burden.

### Standard JSON Schema

- Good, because it has broad tooling and a published specification.
- Bad, because AVD merge, conversion, and generation metadata would require extensions whose semantics are still project-specific.

### Ansible argument specifications

- Good, because they are familiar to collection contributors.
- Bad, because PyAVD is also a direct Python library and needs typed models and semantics not owned by the Ansible runtime.

### Independent consumer models

- Good, because each consumer can use its native representation.
- Bad, because duplicated constraints inevitably drift and produce contradictory behavior.

## Future Direction and Revisit Triggers

Keep the dialect constrained. Revisit only if a standard schema language can represent AVD's required validation, conversion, merge, generation, and
documentation semantics without parallel sources or substantial proprietary extensions.

## Evidence

- [Input validation documentation](../../docs/contribution/input-variable-validation.md) describes the proprietary AVD Schema format.
- [`avd_meta_schema.json`](../../python-avd/pyavd/_schema/avd_meta_schema.json) defines its supported vocabulary.
- [`python-avd/schema_tools`](../../python-avd/schema_tools) implements validation and derived-artifact generation.
