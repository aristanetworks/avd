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

## Context and Current State

AVD exposes individual opt-ins below `avd_design_future` and `eos_config_future` for behavior changes that are not suitable as the default during the
current major release. Legacy behavior remains the default until the planned transition.

## Implemented Decision

Each future flag names one independently understandable behavior, defaults to `false` during the current major release, documents its introduction and
intended future-major transition, exercises both legacy and future paths in tests, and is removed when the future behavior becomes unconditional.

`avd_design_future` covers intent-to-structured-configuration behavior and `eos_config_future` covers structured-configuration-to-EOS rendering
behavior. Future flags are not used for additive features that can remain optional indefinitely or for changes safe under `versioning/0006`.

The current 6.x flags are intended to graduate in a future major release, and each flag's documentation identifies its specific target before the
transition.

## Consequences and Boundaries

- Users can preview major-release behavior without moving their entire deployment to a prerelease.
- Legacy and future implementations and expected outputs coexist temporarily.
- Maintainers receive regression coverage for the future path before it becomes mandatory.
- Every flag is a short-lived public input requiring documentation, tests, and removal discipline.
- Major-release preparation enumerates remaining flags, makes their behavior unconditional, and removes legacy paths, schemas, and tests.

## Confirmation

Future-flag reviews verify a stated transition, separate legacy/future coverage, and release documentation. The release process verifies removal of the
flag and legacy behavior when the target major transition occurs.

## Evidence

- [`avd_design_future` schema](../../python-avd/pyavd/_eos_designs/schema/schema_fragments/avd_design_future.schema.yml) contains opt-ins for future AVD design behavior.
- [`eos_config_future` schema](../../python-avd/pyavd/_eos_cli_config_gen/schema/schema_fragments/eos_config_future.schema.yml) contains opt-ins for future EOS rendering behavior.
- [AVD 6.x release notes](../../docs/release-notes/6.x.x.md) communicate future behaviors to users.
