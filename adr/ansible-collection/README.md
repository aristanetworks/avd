<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# Ansible Collection Decision Backlog

This domain covers the architectural boundary between the `arista.avd` collection, Ansible runtime, and PyAVD, including the testing and packaging
contracts needed to support that boundary.

| ID | Proposed decision question | Why it is architecturally significant |
| -- | -------------------------- | ------------------------------------- |
| `ansible-collection/0001` | Run AVD action plugins on the controller | Define where generation accesses inventory, files, Python dependencies, and execution state. |
| `ansible-collection/0002` | Keep collection roles and plugins as thin PyAVD orchestration | Avoid duplicate domain behavior across Python and Ansible entry points. |
| `ansible-collection/0003` | Separate public and internal plugin interfaces | Offer stable extension points without freezing orchestration internals. |
| `ansible-collection/0004` | Delegate reusable filter and test behavior to PyAVD | Maintain one implementation for behavior exposed through multiple adapters. |
| `ansible-collection/0005` | Define the collection package boundary | Make release inclusion intentional instead of equating repository presence with shipped content. |
| `ansible-collection/0006` | Manage the Ansible support window and plugin tombstones | Give users predictable runtime upgrades, deprecations, redirects, and removals. |
