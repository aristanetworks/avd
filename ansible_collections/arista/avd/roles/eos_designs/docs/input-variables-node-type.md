# Node types

The following table provides information on the pre-defined node types available in `eos_designs`.

To customize or create new node types, please refer to [node type customization](#customization) section.

--8<--
ansible_collections/arista/avd/roles/eos_designs/docs/node-type-variables.md
--8<--

## Configuration

Node type settings are defined under the `node_type_keys.key` i.e `spine:`, `l3leaf:`, `l2leaf:`.

### Structure

All node types have the same structure based on `defaults`, `node_group`, `node_group.node`, `node` and all variables can be defined in any section and support inheritance like this:

Under `node_type_keys.key:`

```bash
defaults <- node_group <- node_group.node <- node
```

!!! tip
    Define common node settings under defaults. This reduces user input requirements, limiting errors.

--8<--
ansible_collections/arista/avd/roles/eos_designs/docs/tables/node-type-structure.md
--8<--

### Common

Define your nodes, id, management and common configuration elements.

!!! tip
    If a node is not deployed, leverage `is_deployed: false` to indicate the node as offline.

!!! info
    A static unique identifier (id) is assigned to each device. This is leveraged to derive the IP address assignment from each summary defined in the Fabric Underlay and Overlay Topology Variables.

--8<--
ansible_collections/arista/avd/roles/eos_designs/docs/tables/node-type-common-configuration.md
--8<--

### Inband management

--8<--
ansible_collections/arista/avd/roles/eos_designs/docs/tables/node-type-inband-management-configuration.md
--8<--

### Uplink management

Connectivity is defined from the child's device perspective.
Source uplink interfaces and parent interfaces are defined on the child.

!!! tip
    Leverage [`default_interfaces`](#default-interface-settings) data model to auto define uplink and downlink interfaces based on the node id.

--8<--
ansible_collections/arista/avd/roles/eos_designs/docs/tables/node-type-uplink-configuration.md
--8<--

### L2 and MLAG

!!! tip
    Alternate addressing schemes are available at [`fabric_ip_addressing`](#fabric-ip-addressing).

--8<--
ansible_collections/arista/avd/roles/eos_designs/docs/tables/node-type-l2-mlag-configuration.md
--8<--

### Loopback and VTEP

--8<--
ansible_collections/arista/avd/roles/eos_designs/docs/tables/node-type-loopback-vtep-configuration.md
--8<--

### L3 interfaces

--8<--
ansible_collections/arista/avd/roles/eos_designs/docs/tables/node-type-l3-interfaces-configuration.md
--8<--

### L3 port-channels

--8<--
ansible_collections/arista/avd/roles/eos_designs/docs/tables/node-type-l3-port-channels-configuration.md
--8<--

### BGP

--8<--
ansible_collections/arista/avd/roles/eos_designs/docs/tables/node-type-bgp-configuration.md
--8<--

### Multicast

--8<--
ansible_collections/arista/avd/roles/eos_designs/docs/tables/node-type-multicast.md
--8<--

### Network services

--8<--
ansible_collections/arista/avd/roles/eos_designs/docs/tables/node-type-evpn-services-configuration.md
--8<--

### EVPN gateway

--8<--
ansible_collections/arista/avd/roles/eos_designs/docs/tables/node-type-evpn-ipvpn-gateway-configuration.md
--8<--

### EVPN multi-domain gateway

--8<--
ansible_collections/arista/avd/roles/eos_designs/docs/tables/node-type-evpn-multi-domain-gateway-configuration.md
--8<--

### ISIS

--8<--
ansible_collections/arista/avd/roles/eos_designs/docs/tables/node-type-isis-configuration.md
--8<--

### MPLS

--8<--
ansible_collections/arista/avd/roles/eos_designs/docs/tables/node-type-mpls-configuration.md
--8<--

### WAN

--8<--
ansible_collections/arista/avd/roles/eos_designs/docs/tables/node-type-wan-configuration.md
--8<--

### PTP

--8<--
ansible_collections/arista/avd/roles/eos_designs/docs/tables/node-type-ptp-configuration.md
--8<--

## Customization

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
ansible_collections/arista/avd/roles/eos_designs/docs/tables/node-type-keys.md
--8<--

### IP addressing templates

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

### Interface descriptions templates

To help format the custom interface descriptions, the following contextual variables are available to the custom templates:

underlay_ethernet_interfaces:

- `{{ link.peer }}`
- `{{ link.peer_interface }}`
- `{{ link.type }} (underlay_p2p, underlay_l2, l3_edge or core_interfaces)`
- All group/hostvars

underlay_port_channel_interfaces:

- `{{ link.channel_description }}`
- `{{ link.channel_group_id }}`
- `{{ link.peer }}`
- `{{ link.peer_channel_group_id }}`
- `{{ link.wan_carrier }}` for `l3_port_channels` defined under the node config.
- `{{ link.main_interface_wan_carrier }}` for `l3_port_channels` subintefaces defined under the node config.
- All group/hostvars

mlag_ethernet_interfaces:

- `{{ mlag_interface }}`
- `{{ mlag_peer }}`
- All group/hostvars

mlag_port_channel_interfaces:

- `{{ mlag_interfaces }}` (list of strings)
- `{{ mlag_peer }}`
- `{{ mlag_port_channel_id }}`
- All group/hostvars

connected_endpoints_ethernet_interfaces:

- `{{ peer }}`
- `{{ peer_interface }}`
- `{{ adapter_description }}`
- All group/hostvars

connected_endpoints_port_channel_interfaces:

- `{{ peer }}`
- `{{ peer_interface }}`
- `{{ adapter_port_channel_id }}`
- `{{ adapter_port_channel_description }}`
- `{{ adapter_description }}`
- All group/hostvars

router_id_loopback_interfaces:

- `{{ router_id_loopback_description }}`
- All group/hostvars

vtep_loopback_interface:

- `{{ vtep_loopback_description }}`
- All group/hostvars

## Type setting

- The `type:` variable needs to be defined for each device in the fabric.
- This is leveraged to load the appropriate settings to generate the configuration.

!!! tip
    The node type setting can be automatically derived from a switch name by defining the patterns in the [`default_node_types`](#default-assignment) data model.

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
ansible_collections/arista/avd/roles/eos_designs/docs/tables/type-setting.md
--8<--

### Auto assign

By leveraging `default_node_types`, regular expressions can be used to determine the node type based on the hostname.

--8<--
ansible_collections/arista/avd/roles/eos_designs/docs/tables/default-node-types.md
--8<--
