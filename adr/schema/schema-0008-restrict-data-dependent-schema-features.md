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

## Context and Problem Statement

Some AVD namespaces are declared by user data: node-type keys, connected-endpoint groups, and catalogs can determine later valid keys or values. The
AVD dialect therefore supports `dynamic_keys` and `dynamic_valid_values`. General data-dependent validation is difficult to reproduce in editors,
documentation, generated models, and multiple entry points. How much dynamic behavior belongs in a schema?

This record governs declarative schema behavior derived from other values in the same normalized input. It does not permit arbitrary expressions,
external lookups, device-capability checks, or general cross-field domain validation inside the schema.

## Decision Drivers

- Genuine user-defined catalogs must be representable without opening an untyped mapping.
- Schema validity should remain deterministic for the same complete input.
- Every consumer must implement the same lookup and default behavior under `schema/0004`.
- Cross-field domain rules and external-state checks need clearer error ownership outside the static schema.

## Considered Options

- Permit only explicit, declarative data-dependent features for true dynamic namespaces and value catalogs.
- Allow arbitrary expressions or callbacks to compute schema behavior.
- Forbid all data-dependent schema behavior.

## Decision Outcome

Chosen option: **Permit only explicit, declarative data-dependent features for true dynamic namespaces and value catalogs**.

Prefer static `keys` and `valid_values`. Use `dynamic_keys` or `dynamic_valid_values` only when user-declared data genuinely defines the later namespace
or catalog. The lookup path must be declarative, scoped relative to the documented parent, deterministic, and evaluated from the same normalized input
including schema defaults. It must not call external services, execute Python callbacks, or depend on processing order.

Rules involving multiple semantic fields, device capabilities, or external state belong in domain validation after boundary schema validation.

### Consequences

- User-defined namespaces and catalogs remain typed through a bounded set of meta-schema features.
- Editors may provide incomplete assistance until the companion input that declares the namespace is available.
- Cross-field, capability-dependent, and external-state constraints remain in a later domain-validation phase.

### Risks and Mitigations

- **Risk:** Consumers evaluate dynamic paths from different input states or in different orders.
  **Mitigation:** Resolve from the same complete normalized input, including defaults, and maintain parity coverage across consumers.

### Confirmation

Every new dynamic feature use must include positive and negative validation cases, default-path coverage, and generated-model coverage. Reviewers must
confirm that a static schema cannot express the use case and that all consumers implement the same lookup.

## Examples or Expected Semantics

If a user catalog declares a node type named `l3leaf`, `dynamic_keys` may add `l3leaf` as a valid key with a predefined value shape. It does not make
all arbitrary keys valid. Whether a particular device platform supports the resulting feature is external state and remains a domain-validation
question rather than a dynamic schema callback.

## Pros and Cons of the Options

### Restricted declarative dynamic features

- Good, because genuine dynamic models remain typed and testable.
- Bad, because the schema engine and tooling must implement data-aware lookups.

### Arbitrary expressions or callbacks

- Good, because almost any constraint can be embedded in the schema.
- Bad, because validation becomes execution-context dependent, hard to document, and unsafe for general tooling.

### No data-dependent behavior

- Good, because the schema stays static and easy to consume.
- Bad, because user-defined AVD namespaces would need open untyped mappings or duplicated special-case code.

## Future Direction and Revisit Triggers

Keep the feature set limited to demonstrated AVD data-model needs. Revisit a dynamic construct if it cannot be represented consistently in editor and
generated-model tooling, or if a static namespaced extension model can replace it without losing user functionality.

## Evidence

- [Input validation documentation](../../docs/contribution/input-variable-validation.md) describes `dynamic_keys` and `dynamic_valid_values`.
- [`python-avd/schema_tools/avdschemaresolver.py`](../../python-avd/schema_tools/avdschemaresolver.py) resolves dynamic schema nodes.
- [`python-avd/pyavd/_schema/models/eos_designs_root_model.py`](../../python-avd/pyavd/_schema/models/eos_designs_root_model.py) loads dynamic keys into typed models.
