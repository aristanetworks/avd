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

## Context and Problem Statement

Strictly preserving every observable output can also preserve defects or prevent harmless normalization. The current compatibility documentation allows
rare breaking changes when correcting bugs and permits EOS CLI reordering that does not affect resulting device configuration. Without a narrow rule,
however, these exceptions could undermine the SemVer guarantees defined by `versioning/0002` and `versioning/0003`.

This record governs narrow corrections that can change stable generated behavior before a major release. It does not permit removal of accepted inputs,
replacement of one valid policy with another preferred policy, or a newly asserted safety goal to bypass deprecation and future-flag requirements.

## Decision Drivers

- Incorrect configuration or validation should not be preserved solely because users observed it.
- Textual differences do not always imply different EOS state.
- Users need visibility when a correction can change their generated artifacts.
- Feature redesigns must not bypass the future-flag and major-release process by being labelled fixes.

## Considered Options

- Permit narrowly evidenced and documented exceptions.
- Forbid all observable changes to stable behavior before a major release.
- Allow maintainers to classify any bug fix as SemVer-compatible without additional criteria.

## Decision Outcome

Chosen option: **Permit narrowly evidenced and documented exceptions**.

A stable output may change in a minor or patch release only when at least one of these is demonstrated:

- The old behavior objectively contradicts a documented AVD input contract or authoritative EOS semantics.
- The old behavior violates an explicit, testable safety invariant stated in released AVD documentation or authoritative EOS documentation. The
  change must cite that normative source, reproduce the violation, and add regression coverage for the corrected result.
- A textual ordering or formatting change produces equivalent effective EOS configuration and does not break a separately documented textual or
  machine-readable contract.

The change must include regression evidence and release-note disclosure proportional to user impact. Input removal, intentional policy change, and
replacement of one valid behavior with another valid preference are not exceptions; they follow `versioning/0004` or `versioning/0005`.

A general claim that new behavior is “safer” is insufficient. If the safety invariant was not already normative, the change establishes a new policy
and must use deprecation, a future flag, or a major release. The pull request must name the applicable exception criterion, and approving maintainers
must explicitly confirm that classification during review.

### Consequences

- Demonstrably invalid or unsafe output can be corrected without preserving it until a major release.
- Semantically equivalent ordering or formatting may change while separately documented textual and machine-readable contracts remain protected.
- Exception classification requires normative evidence, explicit maintainer judgment, regression coverage, and user-impact disclosure.

### Risks and Mitigations

- **Risk:** A feature redesign is presented as a correction and weakens the SemVer contract.
  **Mitigation:** Require a cited prior contract, reproducible evidence, regression coverage, and explicit maintainer confirmation of the criterion.

### Confirmation

The pull request must identify the violated normative contract or demonstrate EOS equivalence, add or update focused expected-output coverage, and call
out observable changes in release notes when users may need to react. Reviewers must explicitly confirm both the exception criterion and that the
change is not an unannounced design preference.

## Examples or Expected Semantics

- A correction is eligible when released documentation promises one result, the current implementation reproducibly emits a contradictory result,
  and a regression case proves that the change restores the documented contract.
- A formatting change is eligible when EOS semantic evidence shows the effective configuration is identical and no stable textual contract is changed.
- Replacing valid output with a newly preferred or broadly described “safer” design is not eligible without a previously documented safety invariant;
  it follows `versioning/0004` or `versioning/0005` instead.

## Pros and Cons of the Options

### Narrow evidenced exceptions

- Good, because correctness and compatibility are balanced through reviewable criteria.
- Bad, because the classification cannot always be automated.

### No exceptions before a major release

- Good, because stable artifacts never change unexpectedly.
- Bad, because known defects and unsafe results may persist for an entire major-release lifetime.

### Unconstrained bug-fix exceptions

- Good, because maintainers can act quickly.
- Bad, because any breaking design change can be framed as a fix, making SemVer meaningless.

## Future Direction and Revisit Triggers

Keep the exception deliberately narrow. Revisit if EOS provides a reliable canonical semantic comparison that CI can use to prove equivalence, or if AVD
publishes a byte-stable configuration format whose contract intentionally forbids textual churn.

## Evidence

- [Semantic Versioning documentation](../../docs/versioning/semantic-versioning.md) describes the existing bug-fix and CLI-reordering qualifications.
- [`ansible_collections/arista/avd/extensions/molecule`](../../ansible_collections/arista/avd/extensions/molecule) contains reviewed intended configuration artifacts.
- [AVD 6.x release notes](../../docs/release-notes/6.x.x.md) are the user-facing channel for observable corrections.
