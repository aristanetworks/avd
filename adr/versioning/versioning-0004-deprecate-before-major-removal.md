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

## Context and Current State

Stable inputs and APIs can require replacement when names, structure, or abstractions no longer fit AVD. AVD provides a released deprecation period
before removing a stable surface.

## Implemented Decision

A stable input or API is deprecated before removal in a later major release. The deprecation identifies the replacement, emits an actionable warning
where possible, documents conflicts, and names the earliest removal version. Removal occurs in a major release and is described in release notes and
the porting guide.

Objectively incorrect behavior is governed by `versioning/0006`; relabeling a design change as a fix is not sufficient.

## Consequences and Boundaries

- Users can migrate while old and replacement interfaces coexist.
- Maintainers carry compatibility branches and tests during the deprecation period.
- When both forms can be supplied, conflict or precedence behavior is explicit.
- Major-release preparation provides the cleanup point for expired compatibility paths.

## Confirmation

Deprecation reviews verify a warning, replacement guidance, removal version, compatibility coverage, and conflict handling. Removal reviews verify a
prior released deprecation and porting documentation.

## Evidence

- [Semantic Versioning documentation](../../docs/versioning/semantic-versioning.md) requires notice before breaking stable role inputs and PyAVD functions.
- [Input validation documentation](../../docs/contribution/input-variable-validation.md) describes schema deprecation warnings, replacements, and conflicts.
- [`ansible_collections/arista/avd/meta/runtime.yml`](../../ansible_collections/arista/avd/meta/runtime.yml) retains Ansible plugin tombstones with removal versions.
