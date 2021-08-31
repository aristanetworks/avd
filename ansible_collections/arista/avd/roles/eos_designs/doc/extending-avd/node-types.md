# Node Types Definition

The node type definition is done under `node_type_keys`. This dictionary defines type of devices you can use in your topologies. Each node type can be configured with the following options:

```yaml
# Define Node Type Keys, to specify the properties of each node type in the fabric
# This allows for complete customization of the fabric layout.
# This should be defined in top level group_var for the fabric.
node_type_keys:
  <node_type_key>:
    # Required | The value of "type" set on each switch
    type: <type value matching this node_type_key>

    # Optional | Are endpoints connected to this node type
    connected_endpoints: < true | false | default -> false >

    # Optional | Default evpn_role. Can be overridden in topology vars.
    default_evpn_role: < none | client | server | default -> none >

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
```

The next output is structure example based on default definition:

```yaml
# Example
# The below key/pair values are the role defaults.
node_type_keys:
  spine:
    type: spine
    default_evpn_role: server
  l3leaf:
    type: l3leaf
    connected_endpoints: true
    default_evpn_role: client
    mlag_support: true
    network_services:
      l2: true
      l3: true
    vtep: true
  l2leaf:
    type: l2leaf
    connected_endpoints: true
    mlag_support: true
    network_services:
      l2: true
    underlay_router: false
    uplink_type: port-channel
  super_spine:
    type: super-spine
  overlay_controller:
    type: overlay-controller
```

!!! info
    The default node definition is available in the [default section](https://github.com/aristanetworks/ansible-avd/blob/devel/ansible_collections/arista/avd/roles/eos_designs/defaults/main/main.yml) of the eos_designs role.
