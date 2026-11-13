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

## Context and Current State

AVD ships its core behavior through both the PyAVD Python package and the `arista.avd` Ansible collection. The collection invokes PyAVD and its
development requirements pin the PyAVD version matching the collection version.

## Implemented Decision

PyAVD and `arista.avd` are released with the same AVD version. Development and release automation updates both versions as one operation, while
translating the common version into each package ecosystem's syntax where necessary.

## Consequences and Boundaries

- One version identifies a mutually tested set of Python code, collection adapters, schemas, and templates.
- Support and porting guidance can refer to one AVD release.
- A change affecting only one artifact participates in the common release cadence.
- Collection CI installs the PyAVD build from the same source revision or matching released version.

## Confirmation

Version-bump configuration updates the collection manifest, PyAVD package metadata, and `pyavd.__version__` together. Collection CI installs the PyAVD
build from the same source revision or the matching released version.

## Evidence

- [`pyproject.toml`](../../pyproject.toml) updates all product-version locations through one bump configuration.
- [`python-avd/pyproject.toml`](../../python-avd/pyproject.toml) defines the PyAVD distribution and the matching development dependency.
- [`ansible_collections/arista/avd/galaxy.yml`](../../ansible_collections/arista/avd/galaxy.yml) declares the collection version.
