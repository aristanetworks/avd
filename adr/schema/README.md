<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# Schema Decisions

These records govern the proprietary AVD Schema dialect used to describe inputs and structured configuration and to generate validation data, typed
Python models, and documentation.

| ID | Decision | Status |
| -- | -------- | ------ |
| [schema/0001](0001-use-constrained-avd-yaml-schema-dialect.md) | Use a constrained AVD YAML schema dialect | Proposed |
| [schema/0002](0002-separate-schema-domains.md) | Separate schema domains with one-way dependencies | Proposed |
| [schema/0003](0003-author-fragments-and-generate-artifacts.md) | Author schema fragments and generate derived artifacts | Proposed |
| [schema/0004](0004-preserve-cross-consumer-semantics.md) | Preserve schema semantics across consumers | Proposed |
| [schema/0005](0005-separate-boundary-validation-from-models.md) | Separate boundary validation from internal models | Proposed |
| [schema/0006](0006-reuse-schema-definitions-with-refs.md) | Reuse schema definitions with explicit references | Proposed |
| [schema/0007](0007-close-nested-mappings-and-open-integration-roots.md) | Close controlled mappings and open only integration roots | Proposed |
| [schema/0008](0008-restrict-data-dependent-schema-features.md) | Restrict data-dependent schema features | Proposed |
| [schema/0009](0009-require-primary-keys-for-mergeable-lists.md) | Require primary keys for mergeable lists | Proposed |
| [schema/0010](0010-use-canonical-types-and-explicit-conversion.md) | Use canonical types and explicit conversion | Proposed |
| [schema/0011](0011-model-unset-default-empty-and-null.md) | Model unset, default, empty, and null distinctly | Proposed |
| [schema/0012](0012-evolve-schemas-additively-with-deprecation.md) | Evolve stable schemas additively with deprecation | Proposed |
