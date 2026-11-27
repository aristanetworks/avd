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

# Document correctness and non-semantic compatibility exceptions

## Context and Current State

AVD's compatibility documentation permits narrow changes to stable generated behavior when correcting objectively incorrect behavior or when EOS CLI
reordering does not affect resulting device configuration. The exception is bounded by the SemVer guarantees in `versioning/0002` and `versioning/0003`.

This record governs corrections that can change stable generated behavior before a major release. It does not permit removal of accepted inputs,
replacement of one valid policy with another preferred policy, or a newly asserted safety goal to bypass deprecation and future-flag requirements.

## Implemented Decision

A stable output may change in a minor or patch release only when at least one of these conditions is demonstrated:

- The old behavior objectively contradicts a documented AVD input contract or authoritative EOS semantics.
- The old behavior violates an explicit, testable safety invariant stated in released AVD documentation or authoritative EOS documentation. The
  change cites that normative source, reproduces the violation, and adds regression coverage for the corrected result.
- A textual ordering or formatting change produces equivalent effective EOS configuration and does not break a separately documented textual or
  machine-readable contract.

The change includes regression evidence and release-note disclosure proportional to user impact. Input removal, intentional policy change, and
replacement of one valid behavior with another valid preference follow `versioning/0004` or `versioning/0005`.

A general claim that new behavior is “safer” is insufficient. If the safety invariant was not already normative, the change establishes a new policy
and uses deprecation, a future flag, or a major release. The pull request names the applicable exception criterion, and approving maintainers
explicitly confirm the classification.

## Consequences and Boundaries

- Demonstrably invalid or unsafe output can be corrected without preserving it until a major release.
- Semantically equivalent ordering or formatting may change while separately documented textual and machine-readable contracts remain protected.
- Exception classification requires normative evidence, explicit maintainer judgment, regression coverage, and user-impact disclosure.
- Feature redesigns cannot be presented as corrections to bypass the SemVer contract.

## Risks and Mitigations

A feature redesign can be presented as a correction and weaken the SemVer contract. A cited prior contract, reproducible evidence, regression coverage,
and explicit maintainer confirmation of the exception criterion contain that risk.

## Confirmation

The pull request identifies the violated normative contract or demonstrates EOS equivalence, adds focused expected-output coverage, and calls out
observable changes in release notes when users may need to react. Reviewers explicitly confirm both the exception criterion and that the change is not
an unannounced design preference.

## Examples or Expected Semantics

- A correction is eligible when released documentation promises one result, the implementation reproducibly emits a contradictory result, and a
  regression case proves that the change restores the documented contract.
- A formatting change is eligible when EOS semantic evidence shows the effective configuration is identical and no stable textual contract is changed.
- Replacing valid output with a newly preferred or broadly described “safer” design is not eligible without a previously documented safety invariant.

## Evidence

- [Semantic Versioning documentation](../../docs/versioning/semantic-versioning.md) describes the existing bug-fix and CLI-reordering qualifications.
- [`ansible_collections/arista/avd/extensions/molecule`](../../ansible_collections/arista/avd/extensions/molecule) contains reviewed intended configuration artifacts.
- [AVD 6.x release notes](../../docs/release-notes/6.x.x.md) are the user-facing channel for observable corrections.
