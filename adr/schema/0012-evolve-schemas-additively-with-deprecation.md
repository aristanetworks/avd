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

# Evolve stable schemas additively with deprecation

## Context and Problem Statement

AVD schemas are both implementation inputs and user-facing contracts. New EOS and design features require continued evolution, while renaming,
retyping, narrowing, or removing an accepted input can break inventory before generation begins. How should stable schema surfaces change within and
between major releases?

## Decision Drivers

- Role inputs and public API inputs are covered by the SemVer boundary in `versioning/0002`.
- Users need time and actionable guidance to migrate valid inventory.
- New functionality should normally be deliverable in minor releases.
- Validation should detect ambiguous simultaneous use of old and replacement models.

## Considered Options

- Prefer additive compatible changes and use declared deprecation before major removal.
- Allow schema changes whenever generated output remains broadly similar.
- Freeze stable schemas until the next major release.

## Decision Outcome

Chosen option: **Prefer additive compatible changes and use declared deprecation before major removal**.

Within a major release, new fields must be optional or have defaults that preserve existing effective behavior. Do not make an existing optional field
required, change its canonical type, narrow previously valid values, or remove an accepted conversion without treating the change as breaking.

For replacement or rename, add the new model, mark the old model with schema deprecation metadata, identify the replacement and earliest removal
version, and define conflict or precedence behavior if both appear. Removal follows `versioning/0004`. Planned changes to generated behavior follow
`versioning/0005`; objectively incorrect behavior uses only the narrow exception in `versioning/0006`.

This policy applies to schemas identified as stable public inputs. Internal facts and explicitly unstable output representations follow their
published stability classification rather than acquiring stability merely because they are expressed with AVD Schema.

### Consequences

- Good, because most features can be added without invalidating existing inventory.
- Good, because migrations are machine-detectable and documented before removal.
- Bad, because renamed structures require temporary compatibility code and tests.
- Bad, because schemas can carry deprecated vocabulary until the next major cleanup.

### Confirmation

Schema review must classify the affected surface using the released SemVer documentation. Deprecations require warnings, replacement links, conflict
coverage, and deprecated-input regression tests. Removals require evidence of prior released deprecation and porting-guide documentation.

## Pros and Cons of the Options

### Additive evolution with deprecation

- Good, because the model can grow while upgrades remain predictable.
- Bad, because compatibility paths add temporary complexity.

### Unrestricted schema changes

- Good, because schemas remain locally clean and can adopt better designs immediately.
- Bad, because valid inventory can fail after an ordinary minor upgrade.

### Major-release-only schema changes

- Good, because each major has a completely fixed input model.
- Bad, because even compatible feature additions would wait for the next major release.

## Future Direction and Revisit Triggers

Continue removing expired deprecated inputs during major-version preparation. Revisit the exact deprecation duration if AVD adopts a long-term-support
release policy, but retain an overlap period and machine-readable migration metadata for every stable replacement.

## Evidence

- [Semantic Versioning documentation](../../docs/versioning/semantic-versioning.md) classifies stable role and PyAVD inputs.
- [Input validation documentation](../../docs/contribution/input-variable-validation.md) describes deprecation warnings, removals, replacements, and conflicts.
- [`python-avd/schema_tools/metaschema/meta_schema_model.py`](../../python-avd/schema_tools/metaschema/meta_schema_model.py) models deprecation metadata.
- [`ansible_collections/arista/avd/extensions/molecule/eos_designs_deprecated_vars`](../../ansible_collections/arista/avd/extensions/molecule/eos_designs_deprecated_vars) preserves deprecated-input coverage.
