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

# Use canonical types with centralized coercion

## Context and Problem Statement

YAML scalar inference can turn an unquoted value into a different Python type than a user intended. Common examples include autonomous-system numbers
that are semantically strings but appear as integers. Accepting multiple types throughout core code weakens generated typing, while rejecting every
convenient YAML form creates avoidable friction.

AVD Schema still exposes the legacy `convert_types` field-level metadata, but `pyavd-utils` 0.0.7 applies centralized scalar coercion without consulting
that declaration. For example, integer and boolean values supplied for `hostname` or `fabric_name` are converted to strings even though those fields
do not declare `convert_types`. The runtime behavior has moved beyond the field-level model, while schema vocabulary and documentation still describe
the older design. Should AVD retain per-field conversion declarations or make the centralized coercion policy authoritative and remove the legacy
metadata?

This prospective record governs coercion at external data boundaries and removal of the old schema vocabulary. It does not authorize feature code to
infer business meaning or perform lossy normalization.

## Decision Drivers

- Each field needs one predictable type after boundary processing.
- Common YAML interpretation mistakes should have an intentional compatibility path.
- Equivalent target types must receive the same coercion behavior across fields and public entry points.
- The schema vocabulary should not retain metadata that no longer controls runtime behavior.
- Centralized coercion must remain bounded enough to avoid hiding genuinely invalid input.

## Considered Options

- Declare one canonical type and apply a centralized coercion policy based on source and target types.
- Declare accepted source types separately on every field with `convert_types`.
- Permit union types throughout the schema.
- Reject all non-canonical input without conversion.

## Decision Outcome

Chosen option: **Declare one canonical type and apply a centralized coercion policy based on source and target types**. A field's `type` describes the
normalized representation used by validation and generated models. Boundary processing applies only the project's bounded, deterministic coercions,
then validates the normalized value against the field's remaining constraints.

The legacy `convert_types` vocabulary must be removed from the meta-schema, schema fragments, generated documentation, and authoring guidance after
confirming that no remaining build consumer relies on it. Since runtime coercion is already centralized, removing the unused declarations is a schema
authoring cleanup and must not change which user inputs are accepted.

### Consequences

- Core code and generated classes receive one canonical type after boundary processing.
- Fields with the same canonical target type use the same coercion policy instead of repeating source types throughout the schema.
- Removing `convert_types` makes the authored schema describe the runtime model instead of retaining ineffective metadata.
- A field cannot independently opt out of a globally supported source-to-target coercion; its post-coercion constraints remain authoritative.

### Risks and Mitigations

- **Risk:** A broad or lossy global coercion hides invalid input or changes information.
  **Mitigation:** Keep one narrow coercion matrix in the boundary validator and test accepted, normalized, and rejected values for every supported pair.
- **Risk:** Removing legacy metadata accidentally changes a generator or documentation consumer.
  **Mitigation:** Audit consumers before removal and confirm identical runtime acceptance and normalized output before and after the cleanup.

### Confirmation

Conformance requires one covered coercion matrix shared by public validation entry points. Tests must prove accepted source forms, normalized results,
rejected source forms, and post-coercion validation. The meta-schema and generated documentation must no longer expose `convert_types`, and removing it
from schema fragments must not change runtime results.

## Examples or Expected Semantics

`hostname` and `fabric_name` both have `type: str` and no field-level conversion declaration. Input `hostname: 123` is normalized by `pyavd-utils`
0.0.7 to the string `"123"` because integer-to-string coercion is part of the centralized boundary policy. The same source and target types must behave
consistently on other string fields. Coercion does not infer whether the resulting string is semantically valid; the field's remaining constraints
still validate it.

## Pros and Cons of the Options

### Canonical type with centralized coercion

- Good, because schema authors declare the normalized type once and runtime behavior remains consistent across fields.
- Good, because removing ineffective field metadata aligns the schema with the validator implementation.
- Bad, because individual fields cannot opt out of a globally supported coercion pair.

### Field-level `convert_types`

- Good, because accepted source types can differ for each field.
- Bad, because declarations are repeated across the schema and can drift from centralized runtime behavior.
- Bad, because this metadata no longer controls coercion in `pyavd-utils`.

### Union types

- Good, because multiple representations remain visible to the core.
- Bad, because every consumer and feature must branch on types and may interpret them differently.

### Strict canonical input only

- Good, because behavior is simplest.
- Bad, because ordinary YAML parsing can make natural input unexpectedly invalid.

## Future Direction and Revisit Triggers

Remove `convert_types` from the AVD meta-schema, fragments, generated documentation, and contributor guidance after completing the consumer audit.
Keep the centralized coercion matrix small. Revisit a coercion when YAML parser behavior, ambiguity, or information loss makes it unsafe; changing
accepted input on a stable surface follows `schema/0012` and the applicable versioning decision.

## Evidence

- [Input validation documentation](../../docs/contribution/input-variable-validation.md) documents the legacy field-level conversion model that must be updated.
- [`pyproject.toml`](../../pyproject.toml) pins the current validator implementation to `pyavd-utils==0.0.7`.
- [`hostname.schema.yml`](../../python-avd/pyavd/_eos_cli_config_gen/schema/schema_fragments/hostname.schema.yml) declares a string without `convert_types`.
- [`fabric_name.schema.yml`](../../python-avd/pyavd/_eos_designs/schema/schema_fragments/fabric_name.schema.yml) declares a string without `convert_types`.
- [`python-avd/schema_tools/metaschema/meta_schema_model.py`](../../python-avd/schema_tools/metaschema/meta_schema_model.py) still exposes the legacy metadata.
- [`validate_inputs.py`](../../python-avd/pyavd/validate_inputs.py) delegates runtime conversion and validation to `pyavd-utils`.
