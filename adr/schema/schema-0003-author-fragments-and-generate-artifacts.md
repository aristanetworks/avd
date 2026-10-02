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

# Author schema fragments and generate derived artifacts

## Context and Current State

Large AVD schemas are represented in feature-oriented YAML fragments, while runtime validation, Python typing, packaging, and user documentation use
combined schemas, stores, generated classes, and tables.

This record governs which schema files contributors author and which artifacts are generated. It does not define schema vocabulary, field semantics,
or the release compatibility classification of generated outputs.

## Implemented Decision

Feature-oriented YAML fragments are the normal authoring surface. Combined YAML schemas, compressed or pickled stores, generated Python classes, and
generated schema documentation are derived artifacts and are not edited by hand.

Generation is deterministic: fragment processing order and archive metadata do not make identical sources produce different tracked output.

## Consequences and Boundaries

- Feature-oriented YAML fragments are the reviewable source for validation, Python models, packaged stores, and schema documentation.
- Generation tooling is part of the development and release critical path.
- Reviewers focus semantic review on authored fragments and generator changes; generated files are trusted as derived output when generation is
  reproducible and the files are marked as generated.
- Editing only a generated output is ineffective because the next generation run replaces it.

## Risks and Mitigations

Generated artifacts can drift from their source fragments or vary between identical builds. Regeneration in pre-commit and CI, comparison with the
worktree, and deterministic ordering and archive metadata contain that risk.

## Confirmation

Schema generation and pre-commit checks reproduce committed derived artifacts without a diff. Reviews reject direct edits to generated outputs and
focus semantic review on the authored fragment or generator that produced them.

## Examples or Expected Semantics

Adding a BGP schema field means editing its feature fragment and running the schema generator. The generator may then update the combined schema,
generated Python models, stores, and data-model tables. Editing only one of those generated outputs is rejected because the next generation run replaces
it.

## Evidence

- [`python-avd/schema_tools/build_schemas.py`](../../python-avd/schema_tools/build_schemas.py) combines fragments and generates stores, classes, and tables.
- [`python-avd/schema_tools/constants.py`](../../python-avd/schema_tools/constants.py) maps schema sources to derived artifacts.
- [`python-avd/pyavd/_eos_cli_config_gen/schema/schema_fragments`](../../python-avd/pyavd/_eos_cli_config_gen/schema/schema_fragments) is a primary schema authoring surface.
- [`.gitattributes`](../../.gitattributes) marks combined schemas and generated Python models as generated and collapses their diffs.
