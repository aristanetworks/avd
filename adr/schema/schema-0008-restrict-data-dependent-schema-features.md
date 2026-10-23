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

# Restrict data-dependent schema features

## Context and Current State

Some AVD namespaces are declared by user data: node-type keys, connected-endpoint groups, and catalogs can determine later valid keys or values. The
AVD dialect supports `dynamic_keys` and `dynamic_valid_values` for these cases.

This record governs declarative schema behavior derived from other values in the same normalized input. It does not permit arbitrary expressions,
external lookups, device-capability checks, or general cross-field domain validation inside the schema.

## Implemented Decision

AVD prefers static `keys` and `valid_values`. It uses `dynamic_keys` or `dynamic_valid_values` only when user-declared data genuinely defines the later
namespace or catalog. The lookup path is declarative, scoped relative to the documented parent, deterministic, and evaluated from the same normalized
input including schema defaults.

Dynamic schema features do not call external services, execute Python callbacks, or depend on processing order. Rules involving multiple semantic fields,
device capabilities, or external state are checked by domain validation after boundary schema validation.

## Consequences and Boundaries

- User-defined namespaces and catalogs remain typed through a bounded set of meta-schema features.
- Editors may provide incomplete assistance until the companion input that declares the namespace is available.
- Cross-field, capability-dependent, and external-state constraints remain in a later domain-validation phase.
- Consumers resolve dynamic paths from the same complete normalized input to preserve consistent behavior.

## Risks and Mitigations

Consumers can evaluate dynamic paths from different input states or in different orders. Resolving from the same complete normalized input, including
defaults, and maintaining parity coverage across consumers contain that risk.

## Confirmation

Dynamic feature uses include positive and negative validation cases, default-path coverage, and generated-model coverage. Reviewers confirm that a static
schema cannot express the use case and that all consumers implement the same lookup.

## Examples or Expected Semantics

If a user catalog declares a node type named `l3leaf`, `dynamic_keys` may add `l3leaf` as a valid key with a predefined value shape. It does not make
all arbitrary keys valid. Whether a device platform supports the resulting feature is external state and remains a domain-validation question.

## Evidence

- [Input validation documentation](../../docs/contribution/input-variable-validation.md) describes `dynamic_keys` and `dynamic_valid_values`.
- [`python-avd/schema_tools/avdschemaresolver.py`](../../python-avd/schema_tools/avdschemaresolver.py) resolves dynamic schema nodes.
- [`python-avd/pyavd/_schema/models/eos_designs_root_model.py`](../../python-avd/pyavd/_schema/models/eos_designs_root_model.py) loads dynamic keys into typed models.
