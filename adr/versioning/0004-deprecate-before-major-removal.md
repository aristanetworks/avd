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

# Deprecate stable surfaces before major-version removal

## Context and Problem Statement

Inputs and APIs sometimes need replacement because names, structure, or abstractions no longer fit AVD. Immediate removal gives maintainers a clean
implementation but leaves users no supported migration interval. Keeping every historical interface forever transfers an unbounded compatibility cost
to the project. How should AVD retire stable surfaces?

## Decision Drivers

- Production users need actionable warning before an upgrade stops accepting existing automation.
- Maintainers need a predictable point at which compatibility code can be removed.
- Old and replacement inputs can conflict and require deterministic precedence or validation.
- Porting guidance must be available before removal.

## Considered Options

- Deprecate first and remove in a later major release.
- Remove stable surfaces as soon as a replacement is available.
- Retain deprecated surfaces indefinitely.

## Decision Outcome

Chosen option: **Deprecate first and remove in a later major release**. A stable input or API must have at least one released deprecation period before
removal. The deprecation identifies the replacement, emits an actionable warning where possible, documents conflicts, and names the earliest removal
version. Removal occurs in a major release and is described in release notes and the porting guide.

The exception for an objectively incorrect behavior is governed by `versioning/0006`; relabeling a design change as a fix is not sufficient.

### Consequences

- Good, because users can migrate while both old and new interfaces are understood by AVD.
- Good, because major releases provide regular cleanup points.
- Bad, because maintainers carry compatibility branches and tests during the deprecation period.
- Bad, because using both forms requires explicit conflict or precedence behavior.

### Confirmation

Reviews for deprecation must verify a warning, replacement guidance, removal version, compatibility coverage, and conflict handling. Reviews for removal
must verify that a prior released deprecation existed and that porting documentation is present.

## Pros and Cons of the Options

### Deprecation followed by major removal

- Good, because it balances migration time with bounded maintenance.
- Bad, because temporary dual-path complexity is unavoidable.

### Immediate removal

- Good, because the implementation remains simple.
- Bad, because minor upgrades can break valid user input and integrations without preparation.

### Indefinite retention

- Good, because old automation continues to work.
- Bad, because obsolete concepts and tests accumulate without a cleanup mechanism.

## Future Direction and Revisit Triggers

Keep deprecation duration expressed in released versions rather than elapsed time. Revisit if AVD adopts a formally supported long-term-support release
policy that requires longer overlap or backport-specific rules.

## Evidence

- [Semantic Versioning documentation](../../docs/versioning/semantic-versioning.md) requires notice before breaking stable role inputs and PyAVD functions.
- [Input validation documentation](../../docs/contribution/input-variable-validation.md) describes schema deprecation warnings, replacements, and conflicts.
- [`ansible_collections/arista/avd/meta/runtime.yml`](../../ansible_collections/arista/avd/meta/runtime.yml) retains Ansible plugin tombstones with removal versions.
