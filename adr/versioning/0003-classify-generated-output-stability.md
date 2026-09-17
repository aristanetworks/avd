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

## Context and Problem Statement

AVD produces EOS configuration, structured configuration, fabric and device documentation, facts, reports, and deployment payloads. Users apply some
outputs directly to production devices while other outputs are intermediate or informational representations that must evolve as features are added.
Should every output have the same Semantic Versioning guarantee?

## Decision Drivers

- Generated EOS configuration and deployment intent can directly change network state.
- Internal representations must evolve without requiring a major release for every structural improvement.
- Users need an explicit warning before building integrations on unstable artifacts.
- Stability concerns effective behavior, not necessarily byte-for-byte formatting.

## Considered Options

- Classify outputs by their role and published contract.
- Treat every generated artifact as SemVer-stable.
- Treat every generated artifact as unstable and best-effort.

## Decision Outcome

Chosen option: **Classify outputs by their role and published contract**.

- Generated EOS configuration and documented deployment outputs are SemVer-stable in their effective behavior, subject to `versioning/0006`.
- Structured configuration, internal facts, generated documentation, catalogs, and reports are stable only where the released documentation explicitly
  says so.
- Formatting or ordering may change when it does not change effective EOS behavior or a separately documented machine-readable contract.

### Consequences

- Good, because operationally significant output receives a strong compatibility promise.
- Good, because intermediate data models and human-oriented documents can evolve during minor releases.
- Bad, because users must consult the stability table before treating an artifact as an integration API.
- Bad, because determining semantic equivalence can require EOS expertise and regression evidence.

### Confirmation

Any new generated artifact must be classified in released documentation before it is presented as a public integration surface. Reviews of changes to
stable output must compare effective behavior and generated fixtures, not only Python APIs. Tests must not accidentally imply stability for artifacts
that the public contract marks unstable.

## Pros and Cons of the Options

### Stability by output role

- Good, because guarantees align with user impact.
- Good, because internal models retain room to improve.
- Bad, because the contract is more nuanced than a single project-wide rule.

### All outputs stable

- Good, because the rule is simple for consumers.
- Bad, because internal structures and human-readable documents become de facto permanent APIs.

### All outputs unstable

- Good, because generation can evolve freely.
- Bad, because a minor upgrade could unexpectedly change production configuration or deployment behavior.

## Future Direction and Revisit Triggers

Preserve the tiered contract. Revisit the classification of an individual output when AVD deliberately publishes a versioned machine-readable format or
when users are explicitly encouraged to consume an existing internal artifact as an API.

## Evidence

- [Semantic Versioning documentation](../../docs/versioning/semantic-versioning.md) contains the current input/output stability matrix.
- [`python-avd/pyavd/api`](../../python-avd/pyavd/api) exposes generation functions with outputs of different stability classes.
- [`ansible_collections/arista/avd/extensions/molecule`](../../ansible_collections/arista/avd/extensions/molecule) contains intended generated artifacts used for regression review.
