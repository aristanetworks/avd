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

# Stage planned breaking behavior with future flags

## Context and Problem Statement

Some corrections and design improvements intentionally change generated configuration or validation in a way that is unsuitable as the default in a
minor release. AVD currently exposes individual opt-ins below `avd_design_future` and `eos_config_future`, with legacy behavior remaining the default.
What lifecycle turns these flags into a predictable migration mechanism instead of permanent compatibility switches?

## Decision Drivers

- Existing deployments need stable defaults throughout a major release.
- New deployments and willing users should be able to adopt and test the next behavior early.
- Both paths need regression coverage before the next major release.
- Compatibility branches and public inputs must not remain indefinitely.

## Considered Options

- Stage each planned breaking behavior behind an individually documented future flag.
- Change behavior immediately and describe it in release notes.
- Preserve old and new behavior as permanent user-selected profiles.

## Decision Outcome

Chosen option: **Stage each planned breaking behavior behind an individually documented future flag**.

Each flag must:

1. Name one independently understandable behavior.
2. Default to `false` during the current major release.
3. Document the version in which it became available and the intended future-major transition.
4. Exercise both legacy and future paths in tests.
5. Become unconditional in the target major release, at which point the legacy path and flag are removed.

Use `avd_design_future` for intent-to-structured-configuration behavior and `eos_config_future` for structured-configuration-to-EOS rendering behavior.
Do not use a future flag for an additive feature that can remain optional indefinitely or for a change safe under `versioning/0006`.

### Consequences

- Good, because users can preview major-release behavior without moving their entire deployment to a prerelease.
- Good, because maintainers receive real test coverage for the future path before it becomes mandatory.
- Bad, because both implementations and expected outputs must coexist temporarily.
- Bad, because every flag is itself a short-lived public input requiring documentation and removal discipline.

### Confirmation

Review must reject a future flag without a stated transition, separate legacy/future coverage, and release documentation. Major-release preparation must
enumerate all remaining flags, make their behavior unconditional, remove legacy branches, and remove the flag schemas and tests.

## Pros and Cons of the Options

### Individual future flags

- Good, because migrations can be tested incrementally.
- Good, because intent generation and CLI rendering have separate, understandable namespaces.
- Bad, because temporary branches increase maintenance and test cost.

### Immediate behavior changes

- Good, because there is only one implementation path.
- Bad, because a minor upgrade can change production output without an opt-in.

### Permanent behavior profiles

- Good, because users choose when or whether to migrate.
- Bad, because AVD would accumulate combinatorial behavior modes and could never complete architectural transitions.

## Future Direction and Revisit Triggers

The current 6.x flags are intended to graduate in a future major release; each flag's documentation must identify the specific target before acceptance.
Revisit this mechanism if AVD introduces a single versioned compatibility profile that can provide the same incremental testing without creating a
combinatorial matrix or indefinite legacy support.

## Evidence

- [`avd_design_future` schema](../../python-avd/pyavd/_eos_designs/schema/schema_fragments/avd_design_future.schema.yml) contains opt-ins for future AVD design behavior.
- [`eos_config_future` schema](../../python-avd/pyavd/_eos_cli_config_gen/schema/schema_fragments/eos_config_future.schema.yml) contains opt-ins for future EOS rendering behavior.
- [AVD 6.x release notes](../../docs/release-notes/6.x.x.md) communicate future behaviors to users.
