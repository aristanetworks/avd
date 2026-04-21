<!--
  ~ Copyright (c) 2025-2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# Arista AVD A-Care TAC Support Overview

Arista AVD is a network automation framework covering multiple network design domains. AVD is an open-source project maintained by a dedicated Arista engineering team. Customers can purchase TAC support for AVD through the A-Care Service contract. TAC support for AVD must be purchased separately; see the ordering information below.

!!! note
    Without a support contract AVD code can be used as-is, without any warranty and with best-effort problem resolution via [GitHub discussions board](https://github.com/aristanetworks/avd/discussions).

## Support Offering

- AVD software is covered by [A-Care Priority Levels](https://www.arista.com/assets/data/tac/downloads/SRPriorityLevels.pdf).
- TAC support covers software defects and troubleshooting Q&A.
- Provide comprehensive software life cycle policy for AVD according to the AVD software life cycle policy detailed below.

## Support Scope

### AVD Ansible Collections

- arista.avd

!!! note
    Red Hat supports “ansible-core” and Ansible Automation Platform. For non-AVD Ansible issues, please contact Red Hat Ansible TAC.

## Software Life Cycle Policy

Arista AVD Software Release Policy and Life Cycle defines the various phases of development and support to guide customers in transitioning to newer versions of the product based on the milestones in the life cycle. Arista Networks will support each major software release train (i.e., 4.x.x, 5.x.x) during the **Active Development** phase and up to 12 months after the release enters the **Maintenance** and **Support Only** phase. The following diagram depicts the release phases and the Arista TAC support mapping across this timeline.

### Software Life Cycle

![Figure: Arista AVD Software Life Cycle](../_media/software_lifecycle_light.svg#only-light)
![Figure: Arista AVD Software Life Cycle](../_media/software_lifecycle_dark.svg#only-dark)

**Active Development Phase:**

- TAC support available.
- Major release with new features, functionality, and bug fixes.

**Maintenance Phase:**

- TAC support available.
- Bug fixes on previous major release.

**Support Only Phase:**

- TAC support available.
- Software upgrade required for bug fixes.

### Example Release Timeline

The Arista AVD project follows [Semantic Versioning](../versioning/semantic-versioning.md): <font class="v-r">Major</font>.<font class="v-gr">Minor</font>.<font class="v-ygr">Maintenance</font> (ex. <font class="v-r">4</font>.<font class="v-gr">10</font>.<font class="v-ygr">2</font>):

- <font class="v-r">Major: Contains breaking changes, follow the</font> [porting guide](../porting-guides/6.x.x.md).
- <font class="v-gr">Minor: New features and fixes (non-breaking)</font>.
- <font class="v-ygr">Maintenance: Fixes only (non-breaking)</font>.

![Figure: Release timeline example](../_media/release_timeline_example_light.svg#only-light)
![Figure: Release timeline example](../_media/release_timeline_example_dark.svg#only-dark)

## Supported Upgrade Paths

AVD supports the following upgrade paths:

- Between any minor versions in the same release train, i.e., from 5.3.0 to 5.7.2.
  - Skipping minor versions is supported.
- Between major release trains, i.e., from 5.7.2 to 6.0.0.
  - Recommended upgrade path is to do a minor version upgrade to the latest minor version in the current major release train before upgrading to the next major release train.
    - The upgrade should be done sequentially, i.e., from 5.5.0 to 5.7.2, and address all deprecations warnings before proceeding to upgrade to 6.0.0.
  - Skipping a major version is not supported, i.e, from 4.10.0 to 6.0.0.
  - Major versions may contain changes requiring updates to the inventory variables. Required updates will be described in a Porting Guide for each major version.

Release notes and porting guide for version 6.x.x can be found here:

- [Release Notes](../release-notes/6.x.x.md)
- [Porting Guide](../porting-guides/6.x.x.md)

## Support Matrix

The following table depicts the AVD release support matrix, including the timelines for each major software train (based on the life cycle policy) and  the current state of support for each train.

| Release | Initial Release Date | Maintenance Phase | Support Only Phase | End of Support |
| ------- | -------------------- | ----------------- | ------------------ | -------------- |
| 6.x.x | Feb-2026 | - | - | - |
| 5.x.x | Oct-2024 | Feb-2026 | Aug-2026 | Feb-2027 |
| 4.x.x | Jun-2023 | Oct-2024 | Apr-2025 | Oct-2025 |

## Ordering Information

| Product Number | Product Description |
| -------------- | ------------------- |
| SVC-AVD-SWITCH-1M | 1-Month A-Care Ansible AVD support for 1 Arista EOS-based Switch.<br>10G+ Fixed and Modular Platforms. |
| SVC-AVD-G-SWITCH-1M | 1-Month A-Care Ansible AVD support for 1 Arista EOS-based Switch.<br>1G/mG Fixed and Modular Platforms. |
