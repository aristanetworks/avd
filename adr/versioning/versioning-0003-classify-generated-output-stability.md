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

# Classify generated-output stability

## Context and Current State

AVD produces EOS configuration, structured configuration, fabric and device documentation, facts, reports, and deployment payloads. The released
Semantic Versioning documentation classifies these outputs according to their role and published contract.

## Implemented Decision

Generated EOS configuration and documented deployment outputs are SemVer-stable in their effective behavior, subject to `versioning/0006`.
Structured configuration, internal facts, generated documentation, catalogs, and reports are stable only where released documentation explicitly says
so. Formatting or ordering may change when it does not change effective EOS behavior or a separately documented machine-readable contract.

## Consequences and Boundaries

- Operationally significant output receives a strong compatibility promise.
- Intermediate data models and human-oriented documents can evolve during minor releases when they are not published as stable interfaces.
- Users consult the stability table before treating an artifact as an integration API.
- Reviews of stable output compare effective behavior and generated fixtures, not only Python APIs.
- Determining semantic equivalence can require EOS expertise and regression evidence.

## Confirmation

Any new generated artifact is classified in released documentation before it is presented as a public integration surface. Tests do not imply stability
for artifacts that the public contract marks unstable.

## Evidence

- [Semantic Versioning documentation](../../docs/versioning/semantic-versioning.md) contains the current input/output stability matrix.
- [`python-avd/pyavd/api`](../../python-avd/pyavd/api) exposes generation functions with outputs of different stability classes.
- [`ansible_collections/arista/avd/extensions/molecule`](../../ansible_collections/arista/avd/extensions/molecule) contains intended generated artifacts used for regression review.
