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

# Classify stable public inputs and APIs

## Context and Problem Statement

AVD exposes Ansible role variables, plugins, documented PyAVD functions, importable internal Python modules, and internal action plugins. Applying the
same compatibility promise to every reachable symbol would prevent normal refactoring, but leaving the public boundary implicit would make upgrades
unsafe. Which inputs and APIs are covered by Semantic Versioning?

## Decision Drivers

- Users need to know which integrations can safely survive minor and patch upgrades.
- Maintainers need freedom to refactor undocumented implementation details.
- A public surface must be discoverable and intentionally reviewed.
- Stability of function outputs and generated artifacts may differ from stability of their inputs.

## Considered Options

- Cover documented role inputs, documented plugins, and explicitly exported PyAVD APIs.
- Cover all importable Python and Ansible content.
- Make no API or input compatibility promises.

## Decision Outcome

Chosen option: **Cover documented role inputs, documented plugins, and explicitly exported PyAVD APIs**. A symbol or plugin is not public merely because
it is technically importable or present in a collection artifact.

The released Semantic Versioning documentation lists the supported surfaces. Undocumented Python code, underscore-prefixed implementation modules,
and action plugins documented as internal are outside the public contract. Output stability is classified separately by `versioning/0003`.

### Consequences

- Good, because consumers have an intentional set of supported integration points.
- Good, because internal refactoring remains possible in minor releases.
- Bad, because maintainers must keep exports and public documentation aligned.
- Bad, because downstream use of internal code may break without deprecation even when it worked previously.

### Confirmation

Review public exports, plugin documentation, role inputs, and the Semantic Versioning table when introducing or changing an entry point. Breaking changes
to a stable surface must follow `versioning/0004` unless the narrow exception in `versioning/0006` applies.

## Pros and Cons of the Options

### Explicit documented surface

- Good, because the promise is useful and bounded.
- Good, because adding a public API becomes a deliberate design decision.
- Bad, because documentation omissions can create ambiguity and must be corrected promptly.

### All importable content

- Good, because any downstream use is protected.
- Bad, because Python and Ansible make many implementation details reachable even when they were never designed as APIs.
- Bad, because normal refactoring would require major releases.

### No compatibility promise

- Good, because maintainers can change anything at any time.
- Bad, because production automation cannot upgrade AVD with reasonable confidence.

## Future Direction and Revisit Triggers

Keep the public boundary explicit and documentation-driven. Revisit if AVD adopts machine-readable API stability annotations or separately versioned
extension APIs; such a mechanism should generate or verify the public documentation rather than create a second conflicting list.

## Evidence

- [Semantic Versioning documentation](../../docs/versioning/semantic-versioning.md) lists stable role, plugin, and PyAVD function inputs.
- [`python-avd/pyavd/api`](../../python-avd/pyavd/api) contains public PyAVD entry points.
- [`ansible_collections/arista/avd/plugins`](../../ansible_collections/arista/avd/plugins) contains both supported and internal collection adapters.
