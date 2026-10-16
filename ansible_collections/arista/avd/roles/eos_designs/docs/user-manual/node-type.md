---
# This title is used for search results
title: AVD Design data models for node types
---
<!--
  ~ Copyright (c) 2023-2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# Node types

Use these variables to select default node roles, define custom node types, and override behavior per device or group—for example uplinks, MLAG, loopbacks, VTEPs, and services attached to a node.

## Node Type Variables

The following tables provide information on the default node types that are pre-defined in AVD.

To customize or create new node types, please refer to [node type customization](#node-type-customization) section.

--8<--
ansible_collections/arista/avd/roles/eos_designs/docs/node-type-variables.md
--8<--

## Node type customization

AVD provides the capability to customize your node types, supporting a variety of designs.

!!! note
    The default values will be overridden if this key is defined.
    If you need to change all the existing `node_type_keys`, it is recommended to copy the defaults and modify them.
    If you need to add custom `node_type_keys`, create them under `custom_node_type_keys`; if named identically to default `node_type_keys` entries, custom entries will replace the equivalent default entry.

??? example "Default value for design `l3ls-evpn`"

    ```yaml
    node_type_keys:

      - key: spine
        type: spine
        default_evpn_role: server
        default_ptp_priority1: 20
        cv_tags_topology_type: spine

      - key: l3leaf
        type: l3leaf
        connected_endpoints: true
        default_evpn_role: client
        mlag_support: true
        network_services:
          l2: true
          l3: true
        vtep: true
        default_ptp_priority1: 30
        cv_tags_topology_type: leaf

      - key: l2leaf
        type: l2leaf
        connected_endpoints: true
        mlag_support: true
        network_services:
          l2: true
        underlay_router: false
        uplink_type: port-channel
        cv_tags_topology_type: leaf

      - key: l3spine
        type: l3spine
        connected_endpoints: true
        mlag_support: true
        network_services:
          l2: true
          l3: true
        default_overlay_routing_protocol: none
        default_underlay_routing_protocol: none

      - key: l2spine
        type: spine
        connected_endpoints: true
        mlag_support: true
        network_services:
          l2: true
        underlay_router: false
        uplink_type: port-channel

      - key: super_spine
        type: super-spine
        cv_tags_topology_type: core

      - key: overlay_controller
        type: overlay-controller
        default_evpn_role: server
        cv_tags_topology_type: spine

      - key: wan_router
        type: wan_router
        default_evpn_role: client
        default_wan_role: client
        default_underlay_routing_protocol: none
        default_overlay_routing_protocol: ibgp
        default_flow_tracker_type: hardware
        vtep: true
        network_services:
          l3: true

      - key: wan_rr
        type: wan_rr
        default_evpn_role: server
        default_wan_role: server
        default_underlay_routing_protocol: none
        default_overlay_routing_protocol: ibgp
        default_flow_tracker_type: hardware
        vtep: true
        network_services:
          l3: true

      - key: p
        type: p
        mpls_lsr: true
        default_mpls_overlay_role: none
        default_overlay_routing_protocol: ibgp
        default_underlay_routing_protocol: isis-sr

      - key: pe
        type: pe
        mpls_lsr: true
        connected_endpoints: true
        default_mpls_overlay_role: client
        default_evpn_role: client
        network_services:
          l1: true
          l2: true
          l3: true
        default_overlay_routing_protocol: ibgp
        default_underlay_routing_protocol: isis-sr
        default_overlay_address_families:
        - vpn-ipv4
        default_evpn_encapsulation: mpls

      - key: rr
        type: rr
        mpls_lsr: true
        default_mpls_overlay_role: server
        default_evpn_role: server
        default_overlay_routing_protocol: ibgp
        default_underlay_routing_protocol: isis-sr
        default_overlay_address_families:
          - vpn-ipv4
        default_evpn_encapsulation: mpls
    ```

??? example "Default value for design `l2ls`"

    ```yaml
    node_type_keys:

      - key: l3spine
        type: l3spine
        connected_endpoints: true
        mlag_support: true
        network_services:
          l2: true
          l3: true
        default_overlay_routing_protocol: none
        default_underlay_routing_protocol: none

      - key: spine
        type: spine
        connected_endpoints: true
        mlag_support: true
        network_services:
          l2: true
        underlay_router: false
        uplink_type: port-channel

      - key: leaf
        type: leaf
        connected_endpoints: true
        mlag_support: true
        network_services:
          l2: true
        underlay_router: false
        uplink_type: port-channel
    ```

??? example "Default value for design `mpls`"

    ```yaml
    node_type_keys:

      - key: p
        type: p
        mpls_lsr: true
        default_mpls_overlay_role: none
        default_overlay_routing_protocol: ibgp
        default_underlay_routing_protocol: isis-sr

      - key: pe
        type: pe
        mpls_lsr: true
        connected_endpoints: true
        default_mpls_overlay_role: client
        default_evpn_role: client
        network_services:
          l1: true
          l2: true
          l3: true
        default_overlay_routing_protocol: ibgp
        default_underlay_routing_protocol: isis-sr
        default_overlay_address_families:
          - vpn-ipv4
        default_evpn_encapsulation: mpls

      - key: rr
        type: rr
        mpls_lsr: true
        default_mpls_overlay_role: server
        default_evpn_role: server
        default_overlay_routing_protocol: ibgp
        default_underlay_routing_protocol: isis-sr
        default_overlay_address_families:
          - vpn-ipv4
        default_evpn_encapsulation: mpls
    ```

--8<--
schemas/avd_design/docs/tables/node-type-keys.md
--8<--

### Context for ip_addressing templates

To help calculate the custom IP addressing, the following contextual variables are available to the custom templates:

router_id:

- `{{ switch_id }}`
- `{{ loopback_ipv4_pool }}`
- `{{ loopback_ipv4_offset }}`
- All group/hostvars

mlag_ip_primary & mlag_ip_secondary:

- `{{ mlag_primary_id }}`
- `{{ mlag_secondary_id }}`
- `{{ switch_data.combined.mlag_peer_address_family }}`
- `{{ switch_data.combined.mlag_peer_ipv4_pool }}`
- `{{ switch_data.combined.mlag_peer_ipv6_pool }}`
- All group/hostvars

mlag_l3_ip_primary & mlag_l3_ip_secondary:

- `{{ mlag_primary_id }}`
- `{{ mlag_secondary_id }}`
- `{{ switch_data.combined.mlag_peer_l3_ipv4_pool }}`
- All group/hostvars

mlag_ibgp_peering_ip_primary & mlag_ibgp_peering_ip_secondary:

- `{{ mlag_primary_id }}`
- `{{ mlag_secondary_id }}`
- `{{ vrf.mlag_ibgp_peering_ipv4_pool }}`
- All group/hostvars

p2p_uplinks_ip & p2p_uplinks_peer_ip:

- `{{ switch.uplink_ipv4_pool }}`
- `{{ switch.id }}`
- `{{ switch.max_uplink_switches }}`
- `{{ switch.max_parallel_uplinks }}`
- `{{ uplink_switch_index }}`
- All group/hostvars

vtep_ip_mlag:

- `{{ switch_vtep_loopback_ipv4_pool }}`
- `{{ mlag_primary_id }}`
- `{{ loopback_ipv4_offset }}`
- All group/hostvars

vtep_ip:

- `{{ switch_vtep_loopback_ipv4_pool }}`
- `{{ switch_id }}`
- `{{ loopback_ipv4_offset }}`
- All group/hostvars

### Context for interface_descriptions templates

To help format the custom interface descriptions, the following contextual variables are available to the custom templates:

underlay_ethernet_interfaces:

- `{{ interface }}`
- `{{ link_type }} (underlay_p2p, underlay_l2, l3_edge or core_interfaces)`
- `{{ peer }}`
- `{{ peer_interface }}`
- `{{ wan_carrier }}`
- `{{ wan_circuit_id }}`
- `{{ main_interface_wan_carrier }}`
- `{{ link.interface }}`
- `{{ link.peer }}`
- `{{ link.peer_interface }}`
- `{{ link.type }} (underlay_p2p, underlay_l2, l3_edge or core_interfaces)`
- `{{ link.wan_carrier }}`
- `{{ link.wan_circuit_id }}`
- `{{ link.main_interface_wan_carrier }}`
- All group/hostvars

Note: Variables like `link.*` are deprecated and will be removed in AVD 7.0.

underlay_port_channel_interfaces:

- `{{ interface }}`
- `{{ channel_description }}`
- `{{ channel_group_id }}`
- `{{ peer }}`
- `{{ peer_channel_group_id }}`
- `{{ peer_node_group }}`
- `{{ wan_carrier }}`
- `{{ wan_circuit_id }}` for `l3_port_channels` defined under the node config.
- `{{ main_interface_wan_carrier }}`
- `{{ link.interface }}`
- `{{ link.channel_description }}`
- `{{ link.channel_group_id }}`
- `{{ link.peer }}`
- `{{ link.peer_channel_group_id }}`
- `{{ link.peer_node_group }}`
- `{{ link.wan_circuit_id }}` for `l3_port_channels` defined under the node config.
- `{{ link.wan_carrier }}` for `l3_port_channels` defined under the node config.
- `{{ link.main_interface_wan_carrier }}` for `l3_port_channels` subintefaces defined under the node config.
- All group/hostvars

Note: Variables like `link.*` are deprecated and will be removed in AVD 7.0.

mlag_ethernet_interfaces:

- `{{ mlag_interface }}`
- `{{ mlag_peer }}`
- All group/hostvars

mlag_port_channel_interfaces:

- `{{ interface }}`
- `{{ mlag_interfaces }}` (list of strings)
- `{{ mlag_peer }}`
- `{{ mlag_port_channel_id }}`
- All group/hostvars

connected_endpoints_ethernet_interfaces:

- `{{ interface }}`
- `{{ peer }}`
- `{{ peer_interface }}`
- `{{ adapter_description }}`
- All group/hostvars

connected_endpoints_port_channel_interfaces:

- `{{ interface }}`
- `{{ peer }}`
- `{{ peer_interface }}`
- `{{ adapter_port_channel_id }}`
- `{{ adapter_port_channel_description }}`
- `{{ adapter_description }}`
- All group/hostvars

router_id_loopback_interfaces:

- `{{ interface }}`
- `{{ router_id_loopback_description }}`
- All group/hostvars

vtep_loopback_interface:

- `{{ interface }}`
- `{{ vtep_loopback_description }}`
- All group/hostvars

## Type setting

- The `type:` variable needs to be defined for each device in the fabric.
- This is leveraged to load the appropriate settings to generate the configuration.

!!! tip
    The node type setting can be automatically derived from a switch name by defining the patterns in the [`default_node_types`](#default-node-types-settings) data model.

??? example "Type setting example"

    ```yaml
    # Defined in SPINE.yml file
    # Can also be set directly in your inventory file under spine group
    type: spine

    # Defined in L3LEAFS.yml
    # Can also be set directly in your inventory file under l3leaf group
    type: l3leaf

    # Defined in L2LEAFS.yml
    # Can also be set directly in your inventory file under l2leaf group
    type: l2leaf

    # Defined in SUPER-SPINES.yml
    # Can also be set directly in your inventory file under super-spine group
    type: super-spine

    # Defined in ROUTE-SERVERS.yml
    # Can also be set directly in your inventory file under route-server group
    type: overlay-controller
    ```

--8<--
schemas/avd_design/docs/tables/type-setting.md
--8<--

## Default node types settings

Node types can be defined statically on each node or in each group of nodes.  By leveraging `default_node_types`, regular expressions can be used to determine the node type based
on the hostname.

--8<--
schemas/avd_design/docs/tables/default-node-types.md
--8<--

## Node type settings

Node type settings are defined under the `node_type_keys.key` i.e `spine:`, `l3leaf:`, `l2leaf:` to configure management, underlay, overlay functionality.

### Node type structure

All node types have the same structure based on `defaults`, `node_group`, `node_group.node`, `node` and all variables can be defined in any section and support inheritance like this:

Under `node_type_keys.key:`

```bash
defaults <- node_group <- node_group.node <- node
```

!!! tip
    Define common node settings under defaults. This reduces user input requirements, limiting errors.

--8<--
schemas/avd_design/docs/tables/node-type-structure.md
--8<--

### Node type common configuration

Define your nodes, id, management and common configuration elements.

!!! tip
    If a node is not deployed, leverage `is_deployed: false` to indicate the node as offline.

!!! info
    A static unique identifier (id) is assigned to each device. This is leveraged to derive the IP address assignment from each summary defined in the Fabric Underlay and Overlay Topology Variables.

--8<--
schemas/avd_design/docs/tables/node-type-common-configuration.md
--8<--

### Node type inband management

--8<--
schemas/avd_design/docs/tables/node-type-inband-management-configuration.md
--8<--

### Node type uplink management

Connectivity is defined from the child's device perspective.
Source uplink interfaces and parent interfaces are defined on the child.

!!! tip
    Leverage [`default_interfaces`](topology.md#default-interface-settings) data model to auto define uplink and downlink interfaces based on the node id.

--8<--
schemas/avd_design/docs/tables/node-type-uplink-configuration.md
--8<--

### Node type L2 and MLAG configuration

!!! tip
    Alternate addressing schemes are available at [`fabric_ip_addressing`](topology.md#fabric-ip-addressing).

--8<--
schemas/avd_design/docs/tables/node-type-l2-mlag-configuration.md
--8<--

### Node type Loopback and VTEP configuration

--8<--
schemas/avd_design/docs/tables/node-type-loopback-vtep-configuration.md
--8<--

### Node type L3 interfaces configuration

--8<--
schemas/avd_design/docs/tables/node-type-l3-interfaces-configuration.md
--8<--

### Node type L3 port-channels configuration

--8<--
schemas/avd_design/docs/tables/node-type-l3-port-channels-configuration.md
--8<--

### Node type BGP configuration

--8<--
schemas/avd_design/docs/tables/node-type-bgp-configuration.md
--8<--

### Node type Multicast configuration

--8<--
schemas/avd_design/docs/tables/node-type-multicast.md
--8<--

### Node type network services configuration

--8<--
schemas/avd_design/docs/tables/node-type-evpn-services-configuration.md
--8<--

### Node type EVPN to MPLS IP-VPN gateway configuration

--8<--
schemas/avd_design/docs/tables/node-type-evpn-ipvpn-gateway-configuration.md
--8<--

### Node type EVPN multi-domain gateway configuration

--8<--
schemas/avd_design/docs/tables/node-type-evpn-multi-domain-gateway-configuration.md
--8<--

### Node type ISIS Configuration

--8<--
schemas/avd_design/docs/tables/node-type-isis-configuration.md
--8<--

### Node type MPLS configuration

--8<--
schemas/avd_design/docs/tables/node-type-mpls-configuration.md
--8<--

### Node type WAN configuration

--8<--
schemas/avd_design/docs/tables/node-type-wan-configuration.md
--8<--

### Node type PTP configuration

--8<--
schemas/avd_design/docs/tables/node-type-ptp-configuration.md
--8<--

## PREVIEW - New devices models

See the [Node type settings](#node-type-settings) section for available keys.

--8<--
schemas/avd_design/docs/tables/devices.md
--8<--
