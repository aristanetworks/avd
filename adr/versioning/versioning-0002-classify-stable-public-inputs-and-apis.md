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

## Context and Current State

AVD exposes Ansible role variables, plugins, documented PyAVD functions, importable internal Python modules, and internal action plugins. The released
Semantic Versioning documentation defines which of these surfaces are supported.

## Implemented Decision

The stable public surface covers documented role inputs, documented plugins, and explicitly exported PyAVD APIs. A symbol or plugin is not public
merely because it is technically importable or present in a collection artifact.

Undocumented Python code, underscore-prefixed implementation modules, and action plugins documented as internal are outside the public contract.
Output stability is classified separately by `versioning/0003`.

## Consequences and Boundaries

- Consumers have an intentional set of supported integration points.
- Internal refactoring remains possible in minor releases when it does not change a stable surface.
- Maintainers keep exports and public documentation aligned.
- Downstream use of internal code may break without deprecation even when it worked previously.

## Confirmation

Reviews check public exports, plugin documentation, role inputs, and the Semantic Versioning table when introducing or changing an entry point. Breaking
changes to a stable surface follow `versioning/0004` unless the narrow exception in `versioning/0006` applies.

## Evidence

- [Semantic Versioning documentation](../../docs/versioning/semantic-versioning.md) lists stable role, plugin, and PyAVD function inputs.
- [`python-avd/pyavd/api`](../../python-avd/pyavd/api) contains public PyAVD entry points.
- [`ansible_collections/arista/avd/plugins`](../../ansible_collections/arista/avd/plugins) contains both supported and internal collection adapters.
