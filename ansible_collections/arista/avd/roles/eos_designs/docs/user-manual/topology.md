---
# This title is used for search results
title: AVD Design data models for design settings
---
<!--
  ~ Copyright (c) 2023-2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# Topology and fabric design

These variables describe the overall fabric design: supported topologies, hierarchy and numbering, IP addressing, default interface behavior, and fabric-wide routing protocol settings.

## Supported designs

Arista AVD supports multiple network design types such as L3LS-EVPN with 3-stage, 5-stage, L2LS, MPLS, AutoVPN and CV Pathfinder. The sections below highlight some of these topologies, but you can extend Arista AVD to support your own topology by using [`node_type_keys`](#node-type-customization) to create your own node type.

### 3-stage clos topology support (Leaf & Spine)

- Arista AVD supports various deployments with layer 3 leaf and spine (3-stage Clos) and optionally, with dedicated overlay controllers.
- 3 stage Clos fabric can be represented as spines, L3 leafs and L2 leafs, and also referred to as a "POD".

See the following examples:

- [AVD example for a single data center using L3LS](../../../../examples/single-dc-l3ls/README.md).
- [AVD example for a dual data center using L3LS](../../../../examples/dual-dc-l3ls/README.md).

### 5-stage clos topology support (Super Spine)

- Arista AVD supports larger deployments with super-spines (5-stage Clos) and optionally, with dedicated overlay controllers.
- 5 stage Clos fabric can be represented as multiple leaf-spine structures (called PODs - Point of Delivery) interconnected by super-spines.
- The logic to deploy every leaf-spine POD fabric remains unchanged.
- Super-spines can be deployed as a single plane (typically chassis switches) or multiple planes.

### Layer 2 Leaf Spine

- Arista AVD supports various deployments with layer 2 leaf and spine. For example, routing may terminate at the spine level or an external L3 device.
- The Clos fabric can be represented as L3 spines, spines, and leafs.

See the following examples:

- [Example for L2LS Fabric](../../../../examples/l2ls-fabric/README.md).
- [Example for Campus Fabric](../../../../examples/campus-fabric/README.md).

### MPLS

Arista AVD supports any arbitrary physical mesh topology by combining and interconnecting different node types with the `core_interfaces` settings.

The following underlay routing protocols are supported:

- ISIS-SR (default)
- ISIS + LDP
- ISIS-SR + LDP
- OSPF + LDP

The following overlay routing protocols are supported:

- IBGP (default)

Any node group of 2 or more rr-routers will form a Route Reflector cluster.

The MPLS design supports most fabric topology variables already supported by l3ls-evpn, barring the exceptions outlined below:

- Connectivity is defined with the [`core_interfaces`](#core-interfaces-settings) settings instead of [Node type uplink](#node-type-uplink-management) settings.
- No MLAG support.
- No VXLAN support.
- EVPN overlay settings are set with `mpls_overlay_role` and `mpls_route_reflectors` instead of `evpn_role` and `evpn_route_servers`.
- No Inband Management support.

See the following example:

- [AVD example for a MPLS-VPN based WAN Network](../../../../examples/isis-ldp-ipvpn/README.md).

### WAN - AutoVPN and CV Pathfinder

Arista AVD supports AutoVPN and CV Pathfinder deployments with the node types `wan_rr` and `wan_router`.
The default underlay routing protocol is set to none but eBGP is supported as well.

The following overlay routing protocols are supported:

- IBGP (default)

For more information please read the [WAN how-to guide](../how-to/wan.md).

## Fabric topology hierarchy

<div style="text-align:center">
  <img src="../../../../../../../docs/_media/5-stage-topology.gif" alt="5 stage topology"/>
</div>

As per the diagram above, the topology hierarchy is the following:

- fabric_name
  - dc_name
    - pod_name

You **must** define the `fabric_name` variable and it **must** match the Ansible inventory group name covering all devices in scope of the fabric.

--8<--
schemas/avd_design/docs/tables/fabric-topology.md
--8<--

## Fabric IP Addressing

--8<--
schemas/avd_design/docs/tables/fabric-ip-addressing.md
--8<--

## PREVIEW - Fabric Numbering

Fabric Numbering controls how various numbers are derived across the fabric.

--8<--
schemas/avd_design/docs/tables/fabric-numbering.md
--8<--

### Node ID Algorithm

IDs will be automatically assigned according to the configured algorithm.

- `static` will use the statically set IDs under node setting.
- `pool_manager` will activate the pool manager for ID pools.
  Any statically set ID under node settings will be reserved in the pool if possible.
  Otherwise an error will be raised.

!!! note
    It is strongly encouraged to use the same Node ID algorithm for all devices in the fabric.
    Using different algorithms for groups of devices may lead to duplicates or inconsistent allocations.

    The pool manager will not change IDs if they are already set under the node settings,
    so it is possible to enable the pool manager on an existing inventory without changes.

#### Details on `pool_manager` for Node IDs

When using `pool_manager` for node IDs the pools are dynamically built and matched on the following device variables:

- `fabric_name`
- `dc_name`
- `pod_name`
- `type`
- `rack`

Each pool will assign the first available ID starting from 1. Any statically set ID under node settings will be reserved in the pool if possible, otherwise an error will be raised.

It is important to make sure the *combination* of the variables above is unique for each intended pool of devices.

!!! warning
    This means changing any of these fields may renumber the node IDs and, in turn, lead to the renumbering of IP addresses, etc.

Stale entries will be reclaimed from each pool automatically after every run.
A stale entry is an entry that was not accessed during the run.

!!! note
    Since stale entries are only reclaimed *after* every run, it is not possible to reuse an ID when removing and adding a new device
    as part of the same execution of AVD.

    To reuse a freed ID, first remove the old device and run AVD. Then add the new device and rerun AVD.

The pool manager stores data in a YAML file per fabric. The default path is `<root_dir>/intended/data/<fabric_name>-ids.yml`

!!! tip
    It is possible to override the automatic assignments by editing the data files manually.
    Just make sure to have a backup or use source control like Git and rerun AVD after changing the file.

## Default interface settings

- Set default uplink, downlink, and MLAG interfaces, which will be used if these interfaces are not defined on a device (either directly or through inheritance).
- These are defined based on the combination of node_type (e.g., l3leaf or spine) and a regex for matching the platform.
- A list of interfaces or interface ranges can be specified.
- Each list item supports range syntax that can be expanded into a list of interfaces. Interface range examples:
  - Ethernet49-52/1: Expands to [ Ethernet49/1, Ethernet50/1, Ethernet51/1, Ethernet52/1 ]
  - Ethernet1/31-34/1: Expands to [ Ethernet1/31/1, Ethernet1/32/1, Ethernet1/33/1, Ethernet1/34/1 ]
  - Ethernet49-50,53-54: Expands to [ Ethernet49, Ethernet50, Ethernet53, Ethernet54 ]
  - Ethernet1-2/1-4: Expands to [ Ethernet1/1, Ethernet1/2, Ethernet1/3, Ethernet1/4, Ethernet2/1, Ethernet2/2, Ethernet2/3, Ethernet2/4 ]
- `uplink_interfaces` and `mlag_interfaces` under `default_interfaces` are directly inherited by `uplink_interfaces` and `mlag_interfaces`.
- `downlink_interfaces` are referenced by the child switch (e.g., the leaf in a leaf/spine network). The child switch leverages an upstream switch's `default_downlink_interfaces` using the child switch ID.  This is then used to build `uplink_switch_interfaces` for that child.
  - In the case of `max_parallel_uplinks` > 1 the `default_downlink_interfaces` are mapped with consecutive downlinks per child ID.
  - Example for `max_parallel_uplinks: 2`, downlink interfaces will be mapped as `[ <downlink1 to leaf-id1>, <downlink2 to leaf-id1>, <downlink1 to leaf-id2>, <downlink2 to leaf-id2> ...]`
- Please note that no default interfaces are defined in AVD itself. You will need to create your own based on the example below.

??? example "Default interfaces example"

    ```yaml
    default_interfaces:
      - types: [ spine, l3leaf ]
        platforms: [ "7050[SC]X3", vEOS.*, default ]
        uplink_interfaces: [ Ethernet49-54/1 ]
        mlag_interfaces: [ Ethernet55-56/1 ]
        downlink_interfaces: [ Ethernet1-32/1 ]
    ```

--8<--
schemas/avd_design/docs/tables/default-interfaces.md
--8<--

## Fabric settings

The following underlay routing protocols are supported:

- EBGP (default for l3ls-evpn)
- OSPF.
- ISIS.
- ISIS-SR¹.
- ISIS-LDP¹.
- ISIS-SR-LDP¹.
- OSPF-LDP¹.
- none².

¹ Only supported with core_interfaces data model.<br />
² For use with design type "l2ls" or other designs where there is no requirement for a routing protocol for underlay and/or overlay on l3 devices.

??? note "Details on `enable_trunk_groups`"
    <a id="details-on-enable_trunk_groups"></a>
    Enabling the use of trunk groups will change the behavior of several components in AVD.

    Changes:

    - **Requires** Trunk Groups to be defined on all trunks towards connected endpoints
    - `MLAG` Trunk Group will be configured on all vlans on MLAG switches
    - Use Trunk Groups for uplinks to L2 switches instead of "switchport trunk allow vlan" lists.
      - On the parent switch a Trunk Group with the name of the L2 switch will be assigned on all vlans
        that are allowed towards the L2 switch.
      - The port-channel towards the L2 switch will be assigned to this trunk group only
      - Add `UPLINK` Trunk Group to all vlans on the L2 Switch and assign this to the uplink port-channel

    ![Figure: Enable Trunk Groups](../../../../../../../docs/_media/enable_trunk_groups.png)

    While it is recommended for consistency to set `enable_trunk_groups` for all devices in the fabric,
    it can also be set in group_vars or host_vars since trunk-groups are only local to a switch.

    !!! warning
        Because of the nature of the EOS Trunk Group feature, enabling this is "all or nothing".
        *All* vlans and *all* trunks towards connected endpoints must be using trunk groups as well.
        If trunk groups are not assigned to a trunk, no vlans will be enabled on that trunk.

??? note "Details on `only_local_vlan_trunk_groups`"
    Enabling this feature will prevent unneeded trunk groups from being configured on vlans.

    Using the figure under [Details on `enable_trunk_groups`](#details-on-enable_trunk_groups) as basis
    enabling with feature would remove the unmatched trunk groups like this:

    ![Figure: Enable only_local_vlan_trunk_groups](../../../../../../../docs/_media/only_local_vlan_trunk_groups.png)

--8<--
schemas/avd_design/docs/tables/fabric-settings.md
--8<--

## BFD settings

--8<--
schemas/avd_design/docs/tables/bfd-settings.md
--8<--

## BGP settings

--8<--
schemas/avd_design/docs/tables/bgp-settings.md
--8<--

## OSPF settings

--8<--
schemas/avd_design/docs/tables/ospf-settings.md
--8<--

## ISIS settings

--8<--
schemas/avd_design/docs/tables/isis-settings.md
--8<--

## Overlay settings

The following overlay routing protocols are supported:

- EBGP (default for l3ls-evpn)
- IBGP (only with OSPF or ISIS variants in underlay)
- none¹
- HER (Head-End Replication)²
- CVX (CloudVision eXchange)

¹ For use with design type "l2ls" or other designs where there is no requirement for a routing protocol for underlay and/or overlay on l3 devices.<br />
² By setting `overlay_routing_protocol:HER`, Arista AVD will configure static VXLAN flood-lists instead of using a dynamic overlay protocol.

--8<--
schemas/avd_design/docs/tables/overlay-settings.md
--8<--

## EVPN settings

--8<--
schemas/avd_design/docs/tables/evpn-settings.md
--8<--

## Spanning Tree settings

--8<--
schemas/avd_design/docs/tables/spanning-tree-settings.md
--8<--

## PTP settings

See the [Configuring PTP](../how-to/ptp.md) how-to for details.

--8<--
schemas/avd_design/docs/tables/ptp_settings.md
--8<--
