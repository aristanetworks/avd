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

## Context and Problem Statement

Large AVD schemas are represented in feature-oriented YAML fragments, while runtime validation, Python typing, packaging, and user documentation need
combined schemas, pickled stores, generated classes, and tables. Which representation is authoritative, and how should the others stay synchronized?

## Decision Drivers

- Schema reviews should be scoped to the feature being changed.
- Runtime and packaged forms should be efficient and reproducible.
- Python models and documentation must derive from the same semantics as validation.
- Contributors must know where edits belong.

## Considered Options

- Author YAML fragments and generate all combined and consumer-specific artifacts.
- Author the combined schema and manually maintain derived files.
- Treat generated Python models as the source and derive schemas from code.

## Decision Outcome

Chosen option: **Author YAML fragments and generate all combined and consumer-specific artifacts**. Fragment directories are the normal authoring
surface. Combined YAML schemas, compressed or pickled stores, generated Python classes, and generated schema documentation are derived artifacts and
must not be edited by hand.

Generation must be deterministic. In particular, fragment processing order and archive metadata must not make identical sources produce different
tracked output.

### Consequences

- Good, because validation, Python models, and documentation share one source.
- Good, because feature-oriented fragments keep reviews manageable.
- Bad, because even a small schema edit can update large generated files.
- Bad, because contributors must run the correct generator and review both source and derived changes.

### Confirmation

Schema generation and pre-commit checks must reproduce committed derived artifacts without a diff. Reviews must trace semantic changes back to a
fragment rather than accepting direct edits to generated outputs.

## Pros and Cons of the Options

### Fragment source with generated artifacts

- Good, because authoring is modular while consumers remain synchronized.
- Bad, because generation tooling is part of the development and release critical path.

### Combined schema plus manual derivatives

- Good, because the complete model is visible in one authored file.
- Bad, because Python, packaged stores, and documentation can disagree with it.

### Python model as source

- Good, because types are native to the implementation language.
- Bad, because schema-specific documentation, editor metadata, deprecation, and merge semantics become harder to author declaratively.

## Future Direction and Revisit Triggers

Keep YAML fragments authoritative while they remain the clearest common representation. Revisit the physical fragmentation strategy if tooling can
provide equally reviewable feature ownership in a single source without increasing merge conflicts or duplicating models.

## Evidence

- [`python-avd/schema_tools/build_schemas.py`](../../python-avd/schema_tools/build_schemas.py) combines fragments and generates stores, classes, and tables.
- [`python-avd/schema_tools/constants.py`](../../python-avd/schema_tools/constants.py) maps schema sources to derived artifacts.
- [`python-avd/pyavd/_eos_cli_config_gen/schema/schema_fragments`](../../python-avd/pyavd/_eos_cli_config_gen/schema/schema_fragments) is a primary schema authoring surface.
