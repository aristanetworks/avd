# Node types definition

The fabric topology variables define the connectivity between the various switch types, as well as override the default switch properties.

## Default nodes

The following table provide information on the default switch types that have been pre-defined in [`default variables`](eos_designs/defaults/main.yml).

| Switch Type Key    | Underlay Router | Uplink Type  | Default EVPN Role | L2 Network Services | L3 Network Services | VTEP | MLAG Support | Connected Endpoints |
| :----------------: | :-------------: | :----------: | :---------------: | :-----------------: | :-----------------: | :--: | :----------: | :-----------------: |
| super_spine        | ✅              | p2p          | none              | ✘                   | ✘                   | ✘    | ✘            | ✘                   |
| spine              | ✅              | p2p          | server            | ✘                   | ✘                   | ✘    | ✘            | ✘                   |
| spline             | ✅              | p2p          | none              | ✅                  | ✅                   | ✘    | ✅           | ✘                   |
| l3leaf             | ✅              | p2p          | client            | ✅                  | ✅                   | ✅   | ✅           | ✅                   |
| l2leaf             | ✘               | port-channel | none              | ✅                  | ✘                   | ✘    | ✅           | ✅                   |
| overlay_controller | ✅              | p2p          | none              | ✘                   | ✘                   | ✘    | ✘            | ✘                   |

## Node type definition

Node type definition is done under `switch_type_keys`. This dictionary has all type of devices you can use in your topologies. Each node type can be configured with the following knobs:

```yaml
switch_type_keys:
  < node type >:
    type: < node type >

    # Define if node type will have endpoints connected.
    connected_endpoints: < true | false | Default -> false >

    # Define if node acts as server or client in BGP EVPN sessions management
    default_evpn_role: < server | client | Default -> client >

    # Enable MLAG support for the specific type of nodes
    mlag_support: < true | false | Default -> false >

    # Section to define what type of services can be deployed on this node type
    network_services:

      # Activate L2 services
      l2: < true | false | Default -> false >

      # Activate L3 services
      l3: < true | false | Default -> false >

    # Define if node type is acting as vtep or not
    vtep: < true | false | Default -> false >

    # List of templates to use for ip-address management.
    # This section overrides templates defined under templates.<design> section
    ip_addressing:
      router_id: < path to template for router-id management >
      p2p_uplinks_ip: < path to template for uplink IP management >
      p2p_uplinks_peer_ip: < path to template for peer uplink IP management >
      mlag_ip_primary: < path to template for MLAG for primary node management >
      mlag_ip_secondary: < path to template for MLAG for secondary node management >
      mlag_l3_ip_primary: < path to template for MLAG for primary node for the L3 part management >
      mlag_l3_ip_secondary: < path to template for MLAG for secondary node for the L3 part management >
      vtep_ip_mlag: < path to template for VTEP address management in MLAG situation >
      vtep_ip: < path to template for VTEP address management management >
```

The next output is structure example based on default definition:

```yaml
switch_type_keys:
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
```

!!! info
    The default node definition is available in the [default section](https://github.com/aristanetworks/ansible-avd/blob/devel/ansible_collections/arista/avd/roles/eos_designs/defaults/main.yml) of the eos_designs role.
