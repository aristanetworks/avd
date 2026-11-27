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

## Context and Current State

AVD schemas are implementation inputs and user-facing contracts. New EOS and design features are added while renaming, retyping, narrowing, or
removing an accepted input can break inventory before generation begins.

This record governs accepted stable public input schemas across releases. It does not grant stability to internal facts or explicitly unstable
representations, and it delegates generated-output behavior and narrow correctness exceptions to the versioning ADRs.

## Implemented Decision

Within a major release, new fields are optional or have defaults that preserve existing effective behavior. An existing optional field is not made
required, its canonical type is not changed, previously valid values are not narrowed, and an accepted conversion is not removed without treating the
change as breaking.

For a replacement or rename, AVD adds the new model, marks the old model with schema deprecation metadata, identifies the replacement and earliest
removal version, and defines conflict or precedence behavior if both appear. Removal follows `versioning/0004`; planned generated behavior follows
`versioning/0005`; objectively incorrect behavior uses only the narrow exception in `versioning/0006`.

This policy applies to schemas identified as stable public inputs. Internal facts and explicitly unstable output representations follow their
published stability classification.

## Consequences and Boundaries

- Compatible features normally enter as optional fields or behavior-preserving defaults without invalidating existing inventory.
- Renames and replacements require a period where old and new models, warnings, conflict rules, and tests coexist.
- Deprecated vocabulary remains until a major-version cleanup satisfies the published removal contract.
- The schema policy and the broader public-surface policy in `versioning/0004` describe the same migration boundary from different layers.

## Risks and Mitigations

Temporary compatibility paths can become permanent and leave competing input models. Recording the replacement and earliest removal version, testing
conflicts, and removing expired paths during major-version preparation contain that risk.

## Confirmation

Schema review classifies the affected surface using the released SemVer documentation. Deprecations include warnings, replacement links, conflict
coverage, and deprecated-input regression tests. Removals include evidence of prior released deprecation and porting-guide documentation.

## Examples or Expected Semantics

Adding an optional field in a minor release is compatible when omission preserves existing effective behavior. Renaming `old_setting` to `new_setting`
requires adding the new field, deprecating the old field, documenting precedence or conflict when both are supplied, and retaining the old field until
the declared major-release removal. Making an existing optional field required is breaking even when most current inventories already set it.

## Evidence

- [Semantic Versioning documentation](../../docs/versioning/semantic-versioning.md) classifies stable role and PyAVD inputs.
- [Input validation documentation](../../docs/contribution/input-variable-validation.md) describes deprecation warnings, removals, replacements, and conflicts.
- [`python-avd/schema_tools/metaschema/meta_schema_model.py`](../../python-avd/schema_tools/metaschema/meta_schema_model.py) models deprecation metadata.
- [`ansible_collections/arista/avd/extensions/molecule/eos_designs_deprecated_vars`](../../ansible_collections/arista/avd/extensions/molecule/eos_designs_deprecated_vars) preserves deprecated-input coverage.
