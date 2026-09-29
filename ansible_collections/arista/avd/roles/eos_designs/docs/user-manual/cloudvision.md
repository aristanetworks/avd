---
# This title is used for search results
title: AVD Design data models for cloudvision
---
<!--
  ~ Copyright (c) 2023-2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

## CloudVision Settings

--8<--
schemas/avd_design/docs/tables/cloudvision-settings.md
--8<--

## CloudVision Tags Settings

--8<--
schemas/avd_design/docs/tables/cloudvision-tags.md
--8<--

## CloudVision Topology settings

Generate AVD topology configurations directly from a given CloudVision topology.

This feature is intended to be used for the integration of AVD and CloudVision Studios.

The topology should be pulled from the CloudVision "Inventory and Topology Studio" inputs. Device IDs must be translated to hostnames.

This feature currently provides the following configurations based on the given CloudVision topology:

- `uplink_switches`
- `uplink_interfaces`
- `uplink_switch_interfaces`
- `mlag_interfaces`
- `platform` (if set)
- `mgmt_interface` (if interface "ManagementX" is found in the list)

!!! note
    `cv_topology` can not be combined with manually set `uplink_switches`, `uplink_interfaces`, `uplink_switch_interfaces` and `mlag_interfaces`.

    When using parallel links between the same devices for L3 uplinks it is important to set
    `max_uplink_switches` and `max_parallel_uplinks` to ensure consistent IP addressing.

??? example "`cv_topology` example"
    To use this feature set `cv_topology_levels` according to the intended design and set `use_cv_topology` to `true`.
    Provide a full topology under `cv_topology` like this example:

    ```yaml
    use_cv_topology: true
    cv_topology_levels:
      - type: super-spine
        level: 1
      - type: spine
        level: 2
      - type: l3leaf
        level: 3
      - type: l2leaf
        level: 4
      - type: overlay-controller
        level: 5
    cv_topology:
      - hostname: s2-spine2
        platform: vEOS-LAB
        interfaces:
          - name: Ethernet2
            neighbor: s2-leaf1
            neighbor_interface: Ethernet3
          - name: Ethernet3
            neighbor: s2-leaf2
            neighbor_interface: Ethernet3
          - name: Ethernet4
            neighbor: s2-leaf3
            neighbor_interface: Ethernet3
          - name: Ethernet5
            neighbor: s2-leaf4
            neighbor_interface: Ethernet3
          - name: Ethernet7
            neighbor: s2-brdr1
            neighbor_interface: Ethernet3
          - name: Ethernet8
            neighbor: s2-brdr2
            neighbor_interface: Ethernet3
          - name: Management0
            neighbor: 00:1c:73:aa:bb:cc
            neighbor_interface: Ethernet21
      - hostname: s1-spine1
      ...cut for readability...
    ```

--8<--
schemas/avd_design/docs/tables/cv-topology.md
--8<--
