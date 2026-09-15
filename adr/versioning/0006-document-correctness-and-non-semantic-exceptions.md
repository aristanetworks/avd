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

- The old behavior is objectively incorrect against the documented input contract, EOS semantics, or a required safety property.
- A textual ordering or formatting change produces equivalent effective EOS configuration and does not break a separately documented textual or
  machine-readable contract.

The change must include regression evidence and release-note disclosure proportional to user impact. Input removal, intentional policy change, and
replacement of one valid behavior with another valid preference are not exceptions; they follow `versioning/0004` or `versioning/0005`.

### Consequences

- Good, because AVD can correct unsafe or invalid output without preserving it until a major release.
- Good, because templates can adopt semantically equivalent EOS ordering improvements.
- Bad, because semantic equivalence can require expert judgment and careful regression testing.
- Bad, because some users comparing raw text can still observe churn even when device state is equivalent.

### Confirmation

The pull request must identify the violated contract or demonstrate EOS equivalence, add or update focused expected-output coverage, and call out observable
changes in release notes when users may need to react. Reviewers must explicitly confirm that the change is not an unannounced design preference.

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
