# Fabric Topology Variables for mpls Design

The fabric topology variables define the connectivity between the various node types, as well as override the default switch properties.

- The mpls design supports any fabric topology variables already supported by l3ls-evpn, barring the exceptions outlined in this document.
- The mpls design additionally supports several new fabric topology variables that are outlined in this document.
- Fabric Name, required to match Ansible Group name covering all devices in the Fabric | Required and **must** be an inventory group name.

```yaml
fabric_name: < Fabric_Name >
```

- Connectivity is defined in a free-standing backbone_interfaces construct.
- A static unique identifier (id) is assigned to each device.
  - This is leveraged to derive the IP address assignment from each summary defined in the Fabric Underlay and Overlay Topology Variables.
- Within the pe, p and rr dictionary variables, defaults can be defined.
  - This reduces user input requirements, limiting errors.
  - The default variables can be overridden when defined under the node groups.

## Supported designs

`eos_designs` with the mpls design type supports any arbitrary physical mesh topology by combining and interconnecting different node types with the backbone_interfaces dictionary. You can also extend `eos_designs` to support your own topology by using [`node_type_keys`](node-types.html) to create your own node type

### Arbitrary Mesh or L3LS Topology

- The **eos_designs** role with the mpls design type supports any type of topology consisting of any combination of pe-routers, p-routers and rr-routers.
- Any node group of 2 or more rr-routers will form a Route Reflector cluster. The backbone_interfaces construct is used to define underlay interfaces and associated interface profiles.

## Node Type Variables

The following table provide information on the default node types that have been pre-defined in [`eos_designs/defaults/main/defaults-node-type-keys.yml`](https://github.com/aristanetworks/ansible-avd/tree/devel/ansible_collections/arista/avd/roles/eos_designs/defaults). To customize or create new node types, please refer to [node types definition](node-types.md)

| Node Type Key | Underlay Router | Uplink Type | Default Overlay Role | L2 Network Services | L3 Network Services | VTEP | Connected Endpoints |
| --------------| --------------- | ----------- | -------------------- | ------------------- | ------------------- | ---- | ------------------- |
| p             | ✅              | p2p          | none                | ✘                   | ✘                   | ✘     | ✘                  |
| rr            | ✅              | p2p          | server              | ✘                   | ✘                   | ✘     | ✘                  |
| pe            | ✅              | p2p          | client              | ✅                  | ✅                   | ✅    | ✅                  |

The variables should be applied to all devices in the fabric.

- The `type:` variable needs to be defined for each device in the fabric.
- This is leveraged to load the appropriate templates to generate the configuration.

### Variables and Options

As explained above, you can defined your own types of devices. CLI only provides default node types.

```yaml
# define the layer type
type: < p | pe | rr >
```

### Example

```yaml
# Defined in PE.yml file
# Can also be set directly in your inventory file under pe-routers group vars
type: pe

# Defined in P.yml
# Can also be set directly in your inventory file under p-routers group vars
type: p

# Defined in RR.yml
# Can also be set directly in your inventory file under rr-routers group vars
type: rr
```

All node types have the same structure based on `defaults`, `node_group`, `node` and all variables can be defined in any section and support inheritance exactly like in the l3ls-evpn design.

## Point-to-point link management

Unlike with the l3ls-evpn design type, underlay p2p links are built using the backbone_interfaces dictionary:

```yaml
backbone_interfaces:
  p2p_links_ip_pools:
    < pool name >: < IPv4_address/Mask >
  p2p_links_profiles:
    < backbone profile name >:
      speed: < speed >
      mtu: < mtu >
      isis_hello_padding: < true | false >
      isis_metric: < metric >
      ip_pool: < pool name >
      isis_circuit_type: < isis circuit type >
      ipv6_enable: < true | false >
  p2p_links:
    - id: < Link ID, used for selecting a subnet from the provided pool >
      nodes: ['< node1 inventory_hostname >', '< node2 inventory_hostname >']
      interfaces: ['< node1 interface >', '< node2 interface >']
      profile: < backbone profile name >
    - id: < Link ID >
      ...
```

## ISIS underlay protocol management and node-SID management

```yaml
< node_type_key >:

  defaults:
    # Any isis variables already supported by l3ls-evpn will work here, plus additionally:
    # Base value for ISIS-SR Node-SID
    node_sid_base: 100

    # Node is-type as configured under the router isis instance.
    is_type: level-2

    # IPv6 subnet for Loopback0 allocation
    loopback_ipv6_pool: < IPv6_address/Mask >

    # Offset all assigned loopback IP addresses.
    loopback_ipv6_offset: 2
```

### BGP & Overlay Control plane

```yaml
< node_type_key >:

  defaults:

    # Acting role in overlay control plane.
    # Override role definition from node_type_keys
    # Can be set per node
    mpls_overlay_role: < client | server | none | Default -> refer to node type variable table >

    # List of inventory hostname acting as MPLS route-reflectors.
    mpls_route_reflectors: [ '< inventory_hostname_of_mpls_route_reflectors >' ]
```

## Unsupported variables

### Loopback and VTEP management

```yaml
< node_type_key >:

  defaults:
    # IPv4 subnet for VTEP/Loopback1 allocation.
    vtep_loopback_ipv4_pool: < IPv4_address/Mask  >

    # Set VXLAN source interface. Loopback1 is default
    vtep_loopback: < Loopback_interface_1 >

    # Acting role in EVPN control plane.
    # Replaced by mpls_overlay_role
    evpn_role: < client | server | none | Default -> refer to node type variable table >

    # List of inventory hostname acting as EVPN route-servers
    # Replaced by mpls_route_reflectors
    evpn_route_servers: [ '< inventory_hostname_of_evpn_server >' ]

    # Possibility to prevent configuration of Tenant VRFs and SVIs
    # Override node definition "network_services_l3" from node_type_keys
    # This allows support for centralized routing.
    evpn_services_l2_only: < false | true >

    # Enable / Disable auto MLAG, when two nodes are defined in node group.
    mlag: < true | false -> default true >

    # Enable / Disable MLAG dual primary detection
    mlag_dual_primary_detection: < true | false -> default false >

    # MLAG interfaces (list) | Required when MLAG leafs present in topology.
    mlag_interfaces: [ < ethernet_interface_3 >, < ethernet_interface_4 > ]

    # MLAG interfaces speed | Optional and depends on mlag_interfaces to be defined
    mlag_interfaces_speed: < interface_speed | forced interface_speed | auto interface_speed >

    # Underlay L3 peering SVI interface id
    # If set to false or the same vlan as mlag_peer_vlan the mlag_peer_vlan will be used for L3 peering.
    mlag_peer_l3_vlan: < 0-4094 | false | default -> 4093 >

    # IP address pool used for MLAG underlay L3 peering | *Required when MLAG leafs present in topology.
    # IP is derived from the node id.
    mlag_peer_l3_ipv4_pool: < IPv4_network/Mask >

    # MLAG Peer Link (control link) SVI interface id
    mlag_peer_vlan: < 0-4094 | default -> 4094 >

    # MLAG Peer Link allowed VLANs
    mlag_peer_link_allowed_vlans: < vlans as string | default -> "2-4094" >

    # IP address pool used for MLAG Peer Link (control link)| *Required when MLAG leafs present in topology.
    # IP is derived from the node id.
    mlag_peer_ipv4_pool: < IPv4_network/Mask >
```
