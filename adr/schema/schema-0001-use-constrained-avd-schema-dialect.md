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

# Use a constrained AVD schema dialect

## Context and Current State

AVD uses one schema model for input validation, type conversion, inheritance and merge behavior, generated Python classes, and data-model
documentation. General-purpose formats such as JSON Schema and Ansible argument specifications cover only parts of these semantics. The current
meta-schema defines a finite AVD-specific vocabulary for the consumers.

This record governs the authoring language and supported vocabulary of AVD Schema. It does not decide physical fragment layout (`schema/0003`),
dependency direction between schema domains (`schema/0002`), or compatibility rules for individual public fields (`schema/0012`).

## Implemented Decision

AVD uses a constrained schema dialect governed by a JSON Schema meta-schema. Only vocabulary defined by the AVD meta-schema is supported; an arbitrary
JSON Schema keyword is not supported merely because a third-party validator understands it. The dialect may be inspired by other schema systems
without claiming full compatibility with them.

New vocabulary is described together with its affected consumers and observable semantics under `schema/0004` before it becomes supported.

## Consequences and Boundaries

- AVD owns the dialect specification, validator, model generator, documentation generator, and compatibility behavior that consume it.
- Contributors use the finite vocabulary declared by the meta-schema rather than assuming arbitrary JSON Schema compatibility.
- Integrations requiring standard JSON Schema need a converter or a deliberately reduced representation of AVD-specific semantics.
- A proprietary keyword must have one defined meaning across the consumers covered by its contract.

## Risks and Mitigations

A proprietary keyword can develop different meanings in separate consumers. The consumer-scope contract in `schema/0004` and the meta-schema's
undeclared-vocabulary rejection contain that risk.

## Confirmation

Schema files are validated against `avd_meta_schema.json`. Contributor documentation and generated tables describe the supported types and options,
and reviews reject undeclared vocabulary.

## Examples or Expected Semantics

A schema containing a standard JSON Schema keyword absent from the AVD meta-schema is invalid, even if an editor or third-party validator understands
it. A new AVD keyword becomes valid only after its meta-schema entry, consumer semantics, documentation, and confirmation coverage are defined.

## Evidence

- [Input validation documentation](../../docs/contribution/input-variable-validation.md) describes the proprietary AVD Schema format.
- [`avd_meta_schema.json`](../../python-avd/pyavd/_schema/avd_meta_schema.json) defines its supported vocabulary.
- [`python-avd/schema_tools`](../../python-avd/schema_tools) implements validation and derived-artifact generation.
