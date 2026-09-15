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

# Co-version PyAVD and `arista.avd`

## Context and Problem Statement

AVD ships its core behavior through both the PyAVD Python package and the `arista.avd` Ansible collection. The collection invokes PyAVD and its
development requirements pin the PyAVD version matching the collection version. Should these artifacts have independent versions, compatible version
ranges, or one AVD product version?

This retrospective record ratifies the observable single-version release configuration. It does not claim to reconstruct why that configuration was
originally introduced.

## Decision Drivers

- Users experience the collection and PyAVD as entry points to the same generation behavior.
- Generated schemas, models, and templates must match the code consuming them.
- Releases and support communication should not require a collection-to-PyAVD compatibility matrix.
- Direct PyAVD users still need a normal Python package version.

## Considered Options

- Release PyAVD and `arista.avd` with the same AVD version.
- Version the artifacts independently and publish a compatibility matrix.
- Version independently while allowing the collection to resolve a range of PyAVD versions.

## Decision Outcome

Chosen option: **Release PyAVD and `arista.avd` with the same AVD version**, because the artifacts expose the same behavior and contain tightly related
generated data. Development and release automation must update both versions as one operation.

### Consequences

- Good, because one version identifies a mutually tested set of Python code, collection adapters, schemas, and templates.
- Good, because support and porting guidance can refer to one AVD release.
- Bad, because a change affecting only one artifact still participates in the common release cadence.
- Bad, because package managers express development versions differently, so release tooling must translate the common version into each ecosystem's
  syntax.

### Confirmation

Version-bump configuration must continue updating the collection manifest, PyAVD package metadata, and `pyavd.__version__` together. Collection CI
must install the PyAVD build from the same source revision or the matching released version.

## Pros and Cons of the Options

### One AVD version

- Good, because compatible artifacts are unambiguous.
- Good, because generated and consuming code cannot be released under accidentally incompatible product versions.
- Bad, because artifact-specific releases are not possible.

### Independent versions with a compatibility matrix

- Good, because each artifact can release on its own cadence.
- Bad, because maintainers and users must reason about and test a growing matrix.
- Bad, because a version pair does not by itself prove that generated assets were built together.

### Independent versions with a PyAVD range

- Good, because Python dependency resolution can choose an available PyAVD version.
- Bad, because apparently compatible versions could differ in internal models or generated assets that are not public SemVer surfaces.

## Future Direction and Revisit Triggers

Keep one version while PyAVD and the collection are released as two distributions of the same AVD behavior. Revisit if either artifact becomes an
independently governed product with a separately supportable API, release cadence, and compatibility test matrix.

## Evidence

- [`pyproject.toml`](../../pyproject.toml) updates all product-version locations through one bump configuration.
- [`python-avd/pyproject.toml`](../../python-avd/pyproject.toml) defines the PyAVD distribution and the matching development dependency.
- [`ansible_collections/arista/avd/galaxy.yml`](../../ansible_collections/arista/avd/galaxy.yml) declares the collection version.
