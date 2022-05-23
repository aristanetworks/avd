# Node Types Definition

The node type definition is done under `node_type_keys`. This dictionary defines type of devices you can use in your topologies. Each node type can be configured to fit the role in the network.

## Variables and Options

```yaml
# Define Node Type Keys, to specify the properties of each node type in the fabric
# This allows for complete customization of the fabric layout.
# This should be defined in top level group_var for the fabric.
node_type_keys:
  - key: <node_type_key>
    # Required | The value of "type" set on each switch
    type: <type value matching this node_type_key>

    # Optional | Are endpoints connected to this node type
    connected_endpoints: < true | false | default -> false >

    # Optional | Default evpn_role. Can be overridden in topology vars.
    default_evpn_role: < none | client | server | default -> none >

    # Optional | Set the default underlay routing_protocol.
    # Can be overridden by setting "underlay_routing_protocol" host/group_vars
    default_underlay_routing_protocol: < routing_protocol | default -> ebgp >

    # Optional | Can this node type support mlag
    mlag_support: < true | false | default -> false >

    # Optional | Will network services be deployed on this node type
    network_services:
      # Vlans
      l2: < true | false | default -> false >
      # VRFs, SVIs (if l2 is true)
      # Only supported with underlay_router
      l3: < true | false | default -> false >

    # Optional | Is this node type a L3 device
    underlay_router: < true | false | default -> true >

    # Optional | Uplinks must be p2p if "vtep" or "underlay_router" is true.
    uplink_type: < "p2p" | "port-channel" | default -> "p2p" >

    # Optional | Is this switch an EVPN VTEP
    vtep: < true | false | default -> false >

    # Optional | Is this switch an MPLS LSR
    mpls_lsr: < true | false | default -> false >

    # Optional | Override ip_adressing templates
    ip_addressing:
      router_id: <path to J2 template - default inherited from templates.ip_addressing.router_id >
      mlag_ip_primary: <path to J2 template - default inherited from templates.ip_addressing.mlag_ip_primary >
      mlag_ip_secondary: <path to J2 template - default inherited from templates.ip_addressing.mlag_ip_secondary >
      mlag_l3_ip_primary: <path to J2 template - default inherited from templates.ip_addressing.mlag_l3_ip_primary >
      mlag_l3_ip_secondary: <path to J2 template - default inherited from templates.ip_addressing.mlag_l3_ip_secondary >
      p2p_uplinks_ip: <path to J2 template - default inherited from templates.ip_addressing.p2p_uplinks_ip >
      p2p_uplinks_peer_ip: <path to J2 template - default inherited from templates.ip_addressing.p2p_uplinks_peer_ip >
      vtep_ip_mlag: <path to J2 template - default inherited from templates.ip_addressing.vtep_ip_mlag >
      vtep_ip: <path to J2 template - default inherited from templates.ip_addressing.vtep_ip >

    # Optional | Override interface_descriptions templates
    # If description templates use Jinja2, they have to strip whitespaces using {%- -%} on any code blocks
    interface_descriptions:
      underlay_ethernet_interfaces: <path to J2 template - default inherited from templates.interface_descriptions.underlay_ethernet_interfaces >
      underlay_port_channel_interfaces: <path to J2 template - default inherited from templates.interface_descriptions.underlay_port_channel_interfaces >
      underlay_ethernet_mlag_interfaces: <path to J2 template - default inherited from templates.interface_descriptions.underlay_ethernet_mlag_interfaces >
      underlay_port_channel_mlag_interfaces: <path to J2 template - default inherited from templates.interface_descriptions.underlay_port_channel_mlag_interfaces >
      connected_endpoints_ethernet_interfaces: <path to J2 template - default inherited from templates.interface_descriptions.connected_endpoints_ethernet_interfaces >
      connected_endpoints_port_channel_interfaces: <path to J2 template - default inherited from templates.interface_descriptions.connected_endpoints_port_channel_interfaces >
      overlay_loopback_interface: <path to J2 template - default inherited from templates.interface_descriptions.overlay_loopback_interface >
      vtep_loopback_interface: <path to J2 template - default inherited from templates.interface_descriptions.vtep_loopback_interface >
```

## Context for ip_addressing templates

To help calculate the custom IP addressing, the following contextual variables are available to the custom templates:

router_id:
- `{{ switch_id }}`
- `{{ loopback_ipv4_pool }}`
- `{{ loopback_ipv4_offset }}`

mlag_ip_primary & mlag_ip_secondary:
- `{{ mlag_primary_id }}`
- `{{ mlag_secondary_id }}`
- `{{ switch_data.combined.mlag_peer_ipv4_pool }}`

mlag_l3_ip_primary & mlag_l3_ip_secondary:
- `{{ mlag_primary_id }}`
- `{{ mlag_secondary_id }}`
- `{{ switch_data.combined.mlag_peer_l3_ipv4_pool }}`

p2p_uplinks_ip & p2p_uplinks_peer_ip:
- `{{ switch.uplink_ipv4_pool }}`
- `{{ switch.id }}`
- `{{ switch.max_uplink_switches }}`
- `{{ switch.max_parallel_uplinks }}`
- `{{ uplink_switch_index }}`

vtep_ip_mlag:
- `{{ switch_vtep_loopback_ipv4_pool }}`
- `{{ mlag_primary_id }}`
- `{{ loopback_ipv4_offset }}`

vtep_ip:
- `{{ switch_vtep_loopback_ipv4_pool }}`
- `{{ switch_id }}`
- `{{ loopback_ipv4_offset }}`

`p2p_uplinks_ip` & `p2p_uplinks_peer_ip` can leverage the switch facts (switch.*) to customize the IP adressing.
All other templates can only leverage the input variables and variables set in switch facts template.

For more information about the available contextual properties, see the following links:
- [underlay_ethernet_interfaces facts](../templates/facts/topology/p2p-uplinks.j2)
- [switch facts](../templates/facts/switch/switch.j2)

## Context for interface_descriptions templates

To help format the custom interface descriptions, the following contextual variables are available to the custom templates:

underlay_ethernet_interfaces:
- `{{ link.peer }}`
- `{{ link.peer_interface }}`
- `{{ link.type }} (underlay_p2p or underlay_l2)`

underlay_port_channel_interfaces:
- `{{ link.channel_description }}`
- `{{ link.channel_group_id }}`
- `{{ link.peer_channel_group_id }}`

mlag_ethernet_interfaces:
- `{{ mlag_interface }}`
- `{{ mlag_peer }}`

mlag_port_channel_interfaces:
- `{{ mlag_interfaces }}`
- `{{ mlag_peer }}`

connected_endpoints_ethernet_interfaces:
- `{{ peer }}`
- `{{ peer_interface }}`

connected_endpoints_port_channel_interfaces:
- `{{ peer }}`
- `{{ adapter_port_channel_description }}`

All templates can leverage the switch facts (switch.*) to customize the interface descriptions.

For more information about the available contextual properties, see the following links:
- [underlay_ethernet_interfaces facts](../templates/facts/topology/p2p-uplinks.j2)
- [underlay_port_channel_interfaces facts](../templates/facts/topology/port-channel-uplinks.j2)
- [mlag_ethernet_interfaces facts](../templates/mlag/ethernet-interfaces.j2)
- [mlag_port_channel_interfaces facts](../templates/mlag/port-channel-interfaces.j2)
- [connected_endpoints_ethernet_interfaces facts](../templates/connected_endpoints/ethernet-interfaces.j2)
- [connected_endpoints_port_channel_interfaces facts](../templates/connected_endpoints/port-channel-interfaces.j2)

The next output is structure example based on default definition:

```yaml
# Example
# The below key/pair values are the role defaults.
node_type_keys:
  - key: spine
    type: spine
    default_evpn_role: server
  - key: l3leaf
    type: l3leaf
    connected_endpoints: true
    default_evpn_role: client
    mlag_support: true
    network_services:
      l2: true
      l3: true
    vtep: true
  - key: l2leaf:
    type: l2leaf
    connected_endpoints: true
    mlag_support: true
    network_services:
      l2: true
    underlay_router: false
    uplink_type: port-channel
  - key: super_spine
    type: super-spine
  - key: overlay_controller
    type: overlay-controller
```

!!! info
    The default node definition is available in the [default section](../defaults/main/main.yml) of the eos_designs role.
