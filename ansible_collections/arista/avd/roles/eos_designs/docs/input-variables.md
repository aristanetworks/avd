---
# This title is used for search results
title: Input variables for eos_designs
---
<!--
  ~ Copyright (c) 2023-2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# Input variables for eos_designs

This document describes the supported input variables for the role `arista.avd.eos_designs`.

Since several data models have changed between AVD versions 5.x and 6.x, it is recommended to study the [Porting Guide for AVD 6.x.x](../../../../../../docs/porting-guides/6.x.x.md) for existing deployments.

The input variables are documented below in tables and YAML.

!!! note
    All input variables are validated by a schema. If additional custom keys are desired, a key starting with an underscore `_`, will be ignored.

!!! warning
    Available features and variables may vary by platforms, refer to documentation on arista.com for specifics.

!!! warning
    All the keys marked as PREVIEW or children of a key marked as PREVIEW are subject to change and are not supported.

## Supported designs

`eos_designs` supports multiple options such as L3LS-EVPN with 3-stage or 5-stage, L2LS, MPLS, AutoVPN and CV Pathfinder. The sections below highlight some of these topologies, but you can extend `eos_designs` to support your own topology by using [`node_type_keys`](input-variables-node-type.md#customization) to create your own node type.

### 3-stage clos topology support (Leaf & Spine)

- The **eos_designs** role support various deployments with layer 3 leaf and spine (3-stage Clos) and optionally, with dedicated overlay controllers.
- 3 stage Clos fabric can be represented as spines, L3 leafs and L2 leafs, and also referred to as a "POD".

See the following examples:

- [AVD example for a single data center using L3LS](../../../examples/single-dc-l3ls/README.md).
- [AVD example for a dual data center using L3LS](../../../examples/dual-dc-l3ls/README.md).

### 5-stage clos topology support (Super Spine)

- The **eos_designs** role support larger deployments with super-spines (5-stage Clos) and optionally, with dedicated overlay controllers.
- 5 stage Clos fabric can be represented as multiple leaf-spine structures (called PODs - Point of Delivery) interconnected by super-spines.
- The logic to deploy every leaf-spine POD fabric remains unchanged.
- Super-spines can be deployed as a single plane (typically chassis switches) or multiple planes.

### Layer 2 Leaf Spine

- The **eos_designs** role support various deployments with layer 2 leaf and spine. For example, routing may terminate at the spine level or an external L3 device.
- The Clos fabric can be represented as L3 spines, spines, and leafs.

See the following examples:

- [Example for L2LS Fabric](../../../examples/l2ls-fabric/README.md).
- [Example for Campus Fabric](../../../examples/campus-fabric/README.md).

### MPLS

The **eos_designs** role supports any arbitrary physical mesh topology by combining and interconnecting different node types with the `core_interfaces` settings.

The following underlay routing protocols are supported:

- ISIS-SR (default)
- ISIS + LDP
- ISIS-SR + LDP
- OSPF + LDP

The following overlay routing protocols are supported:

- IBGP (default)

Any node group of 2 or more rr-routers will form a Route Reflector cluster.

The MPLS design supports most fabric topology variables already supported by l3ls-evpn, barring the exceptions outlined below:

- Connectivity is defined with the [`core_interfaces`](#core-interfaces-settings) settings instead of [Node type uplink](input-variables-node-type.md#uplink-management) settings.
- No MLAG support.
- No VXLAN support.
- EVPN overlay settings are set with `mpls_overlay_role` and `mpls_route_reflectors` instead of `evpn_role` and `evpn_route_servers`.
- No Inband Management support.

See the following example:

- [AVD example for a MPLS-VPN based WAN Network](../../../examples/isis-ldp-ipvpn/README.md).

### WAN - AutoVPN and CV Pathfinder

The **eos_designs** role with the `l3ls-evpn` design type supports the node types `wan_rr` and `wan_router`.
The default underlay routing protocol is set to none but eBGP is supported as well.

The following overlay routing protocols are supported:

- IBGP (default)

For more information please read the [WAN how-to guide](./how-to/wan.md).

## Fabric topology hierarchy

<div style="text-align:center">
  <img src="../../../../../../docs/_media/5-stage-topology.gif" alt="5 stage topology"/>
</div>

As per the diagram above, the topology hierarchy is the following:

- fabric_name
  - dc_name
    - pod_name

You **must** define the `fabric_name` variable and it **must** match the Ansible inventory group name covering all devices in scope of the fabric.

--8<--
ansible_collections/arista/avd/roles/eos_designs/docs/tables/fabric-topology.md
--8<--

## Fabric IP Addressing

--8<--
ansible_collections/arista/avd/roles/eos_designs/docs/tables/fabric-ip-addressing.md
--8<--

## PREVIEW - Fabric Numbering

Fabric Numbering controls how various numbers are derived across the fabric.

--8<--
ansible_collections/arista/avd/roles/eos_designs/docs/tables/fabric-numbering.md
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
ansible_collections/arista/avd/roles/eos_designs/docs/tables/default-interfaces.md
--8<--

## L3 edge and DCI settings

The `l3_edge` data model can be used to configure extra L3 P2P links anywhere in the fabric. It can be between two switches that are already part of the fabric inventory, or it can be towards another device, where only one end of the link is on a switch in the fabric.

The data model supports using IP pools, Subnet per link, specifying the IP addresses manually or using ipv6 with rfc5549. One of these options must be set.
For BGP peerings the AS number must be specified. If the AS number is different than the AS number configured for the node, the local-as will be replaced on this BGP peering (`neighbor <ip> local-as <as> no-prepend replace-as`).

Make sure to configure the variables in a group_vars file covering all devices mentioned in the data model.

--8<--
ansible_collections/arista/avd/roles/eos_designs/docs/tables/l3-edge.md
--8<--

## Core interfaces settings

The `core_interfaces` data model can be used to configure L3 P2P links anywhere in the fabric. It can be between two switches that are already part of the fabric inventory, or it can be towards another device, where only one end of the link is on a switch in the fabric.

The data model supports using IP pools, Subnet per link or specifying the IP addresses manually.
For BGP peerings the AS number must be specified. If the AS number is different than the AS number configured for the node, the local-as will be replaced on this BGP peering (`neighbor <ip> local-as <as> no-prepend replace-as`).

Make sure to configure the variables in a group_vars file covering all devices mentioned in the data model.

--8<--
ansible_collections/arista/avd/roles/eos_designs/docs/tables/core-interfaces.md
--8<--

## Setting a device as not deployed

You can provision configurations for an entire network topology while marking specific devices as undeployed by setting the host-level variable `is_deployed: false`.

This setting does not affect the configuration generation roles (`eos_designs`, `eos_cli_config_gen`), which will still build the complete intended configuration for all devices. However, behavior during deployment depends on the role used:

- The `eos_config_deploy_eapi` role will ignore this setting and attempt to push the configuration to every device.
- The `cv_deploy` role will respect this setting and skip any device marked as `is_deployed: false`, not attempting to configure it via CloudVision.

This practice can create validation challenges. Active, deployed devices will still have configurations for interfaces and BGP sessions pointing to the undeployed neighbor, causing test failures by the `anta_runner` role.

To maintain a clean operational state and ensure validation tests pass on the active devices, AVD enables the following variables by default:

- `shutdown_interfaces_towards_undeployed_peers: true`: On deployed devices, this will add a `shutdown` command to the interfaces connected to undeployed devices. This ensures the ANTA interface and LLDP tests will be skipped for those interfaces.
- `shutdown_bgp_towards_undeployed_peers: true`: On deployed devices, this will add a `shutdown` command to the BGP neighbor configuration towards undeployed devices. This ensures the ANTA BGP tests will be skipped for those neighbors.

!!! note
    `anta_runner` will also **automatically skip all tests** for devices that are themselves marked as `is_deployed: false`.

--8<--
ansible_collections/arista/avd/roles/eos_designs/docs/tables/is-deployed.md
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

    ![Figure: Enable Trunk Groups](../../../../../../docs/_media/enable_trunk_groups.png)

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

    ![Figure: Enable only_local_vlan_trunk_groups](../../../../../../docs/_media/only_local_vlan_trunk_groups.png)

--8<--
ansible_collections/arista/avd/roles/eos_designs/docs/tables/fabric-settings.md
--8<--

## BFD settings

--8<--
ansible_collections/arista/avd/roles/eos_designs/docs/tables/bfd-settings.md
--8<--

## BGP settings

--8<--
ansible_collections/arista/avd/roles/eos_designs/docs/tables/bgp-settings.md
--8<--

## IPv4 ACL settings

--8<--
ansible_collections/arista/avd/roles/eos_designs/docs/tables/ipv4-acls.md
--8<--

### IPv4 Prefix-List Catalog settings

--8<--
ansible_collections/arista/avd/roles/eos_designs/docs/tables/ipv4-prefix-list-catalog.md
--8<--

## OSPF settings

--8<--
ansible_collections/arista/avd/roles/eos_designs/docs/tables/ospf-settings.md
--8<--

## ISIS settings

--8<--
ansible_collections/arista/avd/roles/eos_designs/docs/tables/isis-settings.md
--8<--

## Overlay settings

The following overlay routing protocols are supported:

- EBGP (default for l3ls-evpn)
- IBGP (only with OSPF or ISIS variants in underlay)
- none¹
- HER (Head-End Replication)²
- CVX (CloudVision eXchange)

¹ For use with design type "l2ls" or other designs where there is no requirement for a routing protocol for underlay and/or overlay on l3 devices.<br />
² By setting `overlay_routing_protocol:HER`, `eos_designs` will configure static VXLAN flood-lists instead of using a dynamic overlay protocol.

--8<--
ansible_collections/arista/avd/roles/eos_designs/docs/tables/overlay-settings.md
--8<--

## EVPN settings

--8<--
ansible_collections/arista/avd/roles/eos_designs/docs/tables/evpn-settings.md
--8<--

## Address locking settings

--8<--
ansible_collections/arista/avd/roles/eos_designs/docs/tables/address-locking-settings.md
--8<--

## WAN Settings

### WAN generic settings

--8<--
ansible_collections/arista/avd/roles/eos_designs/docs/tables/wan-settings.md
--8<--

### WAN hierarchy

!!! note

    This section is only relevant for CV Pathfinder and not for AutoVPN

--8<--
ansible_collections/arista/avd/roles/eos_designs/docs/tables/wan-cv-pathfinder-regions.md
--8<--

### WAN path-groups and carriers

--8<--
ansible_collections/arista/avd/roles/eos_designs/docs/tables/wan-path-groups-and-carriers.md
--8<--

### WAN route-servers

--8<--
ansible_collections/arista/avd/roles/eos_designs/docs/tables/wan-route-servers.md
--8<--

### WAN Virtual topologies

WAN virtual topologies leverage Deep Packet Inspection Engine to match traffic.

--8<--
ansible_collections/arista/avd/roles/eos_designs/docs/tables/wan-virtual-topologies.md
--8<--

#### Application Classification

--8<--
ansible_collections/arista/avd/roles/eos_designs/docs/tables/application-classification.md
--8<--

#### Internet Exit policies

!!! note

    This section is only relevant for CV Pathfinder and not for AutoVPN

--8<--
ansible_collections/arista/avd/roles/eos_designs/docs/tables/cv-pathfinder-internet-exit-policies.md
--8<--

##### Zscaler Internet Exit

!!! note

    This data model is intended to be autofilled using a lookup plugin.
    See the top level key description for more information.

--8<--
ansible_collections/arista/avd/roles/eos_designs/docs/tables/zscaler-endpoints.md
--8<--

### WAN Zscaler Integration

--8<--
ansible_collections/arista/avd/roles/eos_designs/docs/tables/wan-cv-pathfinder-zscaler-integration.md
--8<--

## Management settings

### AAA

--8<--
ansible_collections/arista/avd/roles/eos_designs/docs/tables/aaa-settings.md
--8<--

### DNS

--8<--
ansible_collections/arista/avd/roles/eos_designs/docs/tables/dns-settings.md
--8<--

### Event handlers

--8<--
ansible_collections/arista/avd/roles/eos_designs/docs/tables/event-handlers.md
--8<--

### Flow tracking

--8<--
ansible_collections/arista/avd/roles/eos_designs/docs/tables/management-flow-tracking-settings.md
--8<--

### Logging

--8<--
ansible_collections/arista/avd/roles/eos_designs/docs/tables/logging-settings.md
--8<--

### Management eAPI

--8<--
ansible_collections/arista/avd/roles/eos_designs/docs/tables/management-eapi.md
--8<--

### Management interface

--8<--
ansible_collections/arista/avd/roles/eos_designs/docs/tables/management-interface-settings.md
--8<--

### Time configuration

--8<--
ansible_collections/arista/avd/roles/eos_designs/docs/tables/time-configuration.md
--8<--

### sFlow

--8<--
ansible_collections/arista/avd/roles/eos_designs/docs/tables/management-sflow-settings.md
--8<--

### Source-interfaces

--8<--
ansible_collections/arista/avd/roles/eos_designs/docs/tables/management-source-interfaces-settings.md
--8<--

### SNMP

--8<--
ansible_collections/arista/avd/roles/eos_designs/docs/tables/management-snmp-settings.md
--8<--

### SSH

--8<--
ansible_collections/arista/avd/roles/eos_designs/docs/tables/ssh-settings.md
--8<--

### ZTP

--8<--
ansible_collections/arista/avd/roles/eos_designs/docs/tables/inband-ztp-bootstrap-file.md
--8<--

## Monitoring

### Event monitor

--8<--
ansible_collections/arista/avd/roles/eos_designs/docs/tables/event-monitor.md
--8<--

### Load interval

--8<--
ansible_collections/arista/avd/roles/eos_designs/docs/tables/load-interval.md
--8<--

## Quality of Service

### Queue monitor-streaming

--8<--
ansible_collections/arista/avd/roles/eos_designs/docs/tables/queue-monitor-streaming.md
--8<--

## System settings

--8<--
ansible_collections/arista/avd/roles/eos_designs/docs/tables/system-settings.md
--8<--

## CloudVision Settings

--8<--
ansible_collections/arista/avd/roles/eos_designs/docs/tables/cloudvision-settings.md
--8<--

## CloudVision Tags Settings

--8<--
ansible_collections/arista/avd/roles/eos_designs/docs/tables/cloudvision-tags.md
--8<--

## Endpoint connectivity

AVD supports two different data models for defining connectivity to endpoints:

- ["Connected Endpoints"](input-variables-connected-endpoints.md) is an endpoint-centric model intended for servers or other use cases where most ports have unique configurations.
- ["Network Ports"](input-variables-network-ports.md) is a compact and port-centric model intended for configuration of generic port configurations on large ranges of ports.

Both data models share the same underlying implementation and can coexist without conflicts.
If a switch port is defined in both "Connected Endpoints" and "Network Ports", the "Connected Endpoints" configuration will take precedence.

Both data models support variable inheritance from profiles defined under `port_profiles`. The profiles can be shared between the models. Any setting defined under the `port_profiles` will be inherited from `parent_profile` to `profile` to `adapter`.

## Platform settings

Set platform specific settings like TCAM profile and reload delay.

If the platform is not defined, it will load parameters from the platform tagged `default`.

Management interface is modified for specific platforms like modular platforms with dual supervisor support and container EOS.

!!! note
    The reload delay values should be reviewed and tuned to the specific environment.

!!! note
    The default values will be overridden if `platform_settings` is defined.
    If you need to replace all the default platforms, it is recommended to copy the defaults and modify them.
    If you need to add custom platforms, create them under `custom_platform_settings`; if named identically to default `platform_settings` entries, custom entries will replace the equivalent default entry.

### Platform

--8<--
ansible_collections/arista/avd/roles/eos_designs/docs/tables/platform-settings.md
--8<--

### Custom platform

--8<--
ansible_collections/arista/avd/roles/eos_designs/docs/tables/custom-platform-settings.md
--8<--

### Platform speed groups

--8<--
ansible_collections/arista/avd/roles/eos_designs/docs/tables/platform-speed-groups.md
--8<--

## Validation Profiles

--8<--
ansible_collections/arista/avd/roles/eos_designs/docs/tables/validation-profiles.md
--8<--

## PTP settings

See the [Configuring PTP](how-to/ptp.md) how-to for details.

--8<--
ansible_collections/arista/avd/roles/eos_designs/docs/tables/ptp_settings.md
--8<--

## Custom Structured Configuration

See the [Custom Structured Configuration](how-to/custom-structured-configuration.md) how-to for details.

--8<--
ansible_collections/arista/avd/roles/eos_designs/docs/tables/custom-structured-configuration.md
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
ansible_collections/arista/avd/roles/eos_designs/docs/tables/cv-topology.md
--8<--

## PREVIEW - Digital Twin settings

!!! note
    To easily switch between production mode and digital twin mode, it is recommended to create a dedicated playbook where `avd_digital_twin_mode: true` is set in the playbook vars.

    By default, Digital Twin artifacts (such as the topology file, adjusted structured and EOS configuration, device and fabric documentation)
    will replace original fabric artifacts.

    To keep Digital Twin artifacts separate, adjust the `output_dir_name` and `documentation_dir_name` variables for both `eos_designs`
    and `eos_cli_config_gen` to point to a dedicated output location.

AVD Digital Twin functionality natively generates all artifacts required to deploy a virtual replica of a production AVD fabric.
The generated artifacts are automatically optimized for the specific Digital Twin environment. For example, an EOS configuration generated for an ACT environment will automatically remove or adjust any unsupported features.

AVD currently supports the following Digital Twin environments:

- ACT (Arista Cloud Test)

To generate the ACT Digital Twin artifacts, run the `eos_designs` and `eos_cli_config_gen` roles with the `avd_digital_twin_mode`  flag set to `true` in your Ansible playbook:

```yaml
---

# Production playbook to generate production fabric artifacts
- name: Build Configurations and Documentation
  hosts: FABRIC
  gather_facts: false
  tasks:

    - name: Generate AVD Structured Configurations and Fabric Documentation
      ansible.builtin.import_role:
        name: arista.avd.eos_designs

    - name: Generate Device Configurations and Documentation
      ansible.builtin.import_role:
        name: arista.avd.eos_cli_config_gen

# Digital Twin playbook to generate Digital Twin mode artifacts
- name: Build Configurations and Documentation
  hosts: FABRIC
  gather_facts: false
  vars:
    # Adjust the output dirs to keep Digital Twin artifacts in a separate directory
    output_dir_name: "digital_twin/intended"
    documentation_dir_name: "digital_twin/documentation"
    # Set this flag to True to enable Digital Twin mode
    avd_digital_twin_mode: true
  tasks:

    - name: Generate AVD Structured Configurations and Fabric Documentation
      ansible.builtin.import_role:
        name: arista.avd.eos_designs

    - name: Generate Device Configurations and Documentation
      ansible.builtin.import_role:
        name: arista.avd.eos_cli_config_gen

```

Produced artifacts:

```text
.
├── digital_twin
│   ├── documentation
│   │   ├── devices
│   │   │   ├── <DEVICE_NAME>.md
│   │   │   └── ...
│   │   └── fabric
│   │       ├── <FABRIC_NAME>-documentation.md
│   │       ├── <FABRIC_NAME>-p2p-links.csv
│   │       ├── <FABRIC_NAME>-topology.csv
│   │       └── <FABRIC_NAME>-topology.yml
│   └── intended
│       ├── configs
│       │   ├── <DEVICE_NAME>.cfg
│       │   └── ...
│       └── structured_configs
│           ├── <DEVICE_NAME>.yml
│           └── ...
```

If not specified otherwise, AVD uses the following default values when generating ACT Digital Twin artifacts:

| Attribute | Description | Default value | Source of information |
| --------- | ----------- | ------------- | --------------------- |
| act_os_version | OS version of the replica device | `cloudeos`: `4.33.2F`<br>`cvp`: `2024.3.2`<br>`generic`: `ubuntu-2204-lts`<br>`third-party`: `byod`<br>`tools-server`: `ubuntu-2204-lts`<br>`veos`: `4.33.1.1F` | `node_config.digital_twin.act_os_version` or `digital_twin.fabric.act_os_version` |
| act_username | username of the default account deployed on the replica device | `admin` | `digital_twin.fabric.act_username` |
| act_password | password of the default account deployed on the replica device | `admin` | `digital_twin.fabric.act_password` |

--8<--
ansible_collections/arista/avd/roles/eos_designs/docs/tables/digital-twin-configuration.md
--8<--

### Node type Digital Twin configuration

--8<--
ansible_collections/arista/avd/roles/eos_designs/docs/tables/node-type-digital-twin-configuration.md
--8<--

### PREVIEW - New devices models

--8<--
ansible_collections/arista/avd/roles/eos_designs/docs/tables/devices.md
--8<--
