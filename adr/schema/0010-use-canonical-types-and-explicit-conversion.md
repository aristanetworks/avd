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

# Use canonical types and explicit conversion

## Context and Problem Statement

YAML scalar inference can turn an unquoted value into a different Python type than a user intended. Common examples include autonomous-system numbers
that are semantically strings but appear as integers. Accepting multiple types everywhere weakens generated typing, while rejecting every convenient
YAML form creates avoidable friction. How should a schema define type and coercion?

## Decision Drivers

- Each field needs one predictable type after boundary processing.
- Common YAML interpretation mistakes should have an intentional compatibility path.
- Validation, models, documentation, and direct APIs must apply the same conversions.
- Broad implicit coercion can hide genuinely invalid input.

## Considered Options

- Declare one canonical type and list each accepted source type explicitly with `convert_types`.
- Permit union types throughout the schema.
- Coerce any value whenever Python can construct the target type.
- Reject all non-canonical input without conversion.

## Decision Outcome

Chosen option: **Declare one canonical type and list each accepted source type explicitly with `convert_types`**. A field's `type` describes the
normalized representation used by validation and generated models. Boundary processing performs only conversions supported by the meta-schema and
explicitly enabled on that field, then validates the converted value.

Do not add conversion preemptively. It must address a documented input ambiguity or compatibility need and must have unambiguous results. Collection
or mapping conversions follow the same rule and may require identity metadata such as the primary key in `schema/0009`.

### Consequences

- Good, because core code and generated classes receive one type.
- Good, because selected ergonomic YAML forms remain supported and documented.
- Bad, because conversion adds input forms that may need long-term compatibility support.
- Bad, because authors must distinguish a harmless representation difference from an invalid value.

### Confirmation

Schema validation must reject undeclared source types. Each conversion requires tests for the accepted source form, normalized result, invalid values,
and parity between public entry points. Generated documentation must list supported conversions.

## Pros and Cons of the Options

### Canonical type with explicit conversion

- Good, because flexibility is local and auditable.
- Bad, because schema authors must enumerate and test every allowed conversion.

### Union types

- Good, because multiple representations remain visible to the core.
- Bad, because every consumer and feature must branch on types and may interpret them differently.

### General implicit coercion

- Good, because many user values appear to work automatically.
- Bad, because surprising conversions can conceal errors or lose information.

### Strict canonical input only

- Good, because behavior is simplest.
- Bad, because ordinary YAML parsing can make natural input unexpectedly invalid.

## Future Direction and Revisit Triggers

Keep the conversion set small. Revisit an existing conversion when YAML parser behavior, ambiguity, or loss of information makes it unsafe; removing a
conversion from a stable input follows `schema/0012`.

## Evidence

- [Input validation documentation](../../docs/contribution/input-variable-validation.md) documents supported scalar conversions and processing order.
- [`python-avd/schema_tools/metaschema/meta_schema_model.py`](../../python-avd/schema_tools/metaschema/meta_schema_model.py) constrains conversions per canonical type.
- [`python-avd/pyavd/_schema`](../../python-avd/pyavd/_schema) implements runtime conversion and validation.
