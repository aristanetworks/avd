# BETA Feature

The MPLS design feature is in BETA until the release of AVD 4.0.0. Changes to data models and default behavior for the MPLS design should be expected.

# Fabric Topology Variables for MPLS Design

The fabric topology variables define the connectivity between the various node types, as well as override the default switch properties.

- The MPLS design supports any fabric topology variables already supported by l3ls-evpn, barring the exceptions outlined in this document.
- Additionally the MPLS design supports several new fabric topology variables that are outlined in this document.
- Connectivity is defined in a free-standing core_interfaces construct.
- A static unique identifier (id) is assigned to each device.
  - This is leveraged to derive the IP address assignment from each summary defined in the Fabric Underlay and Overlay Topology Variables.
- Within the pe, p and rr dictionary variables, defaults can be defined.
  - This reduces user input requirements, limiting errors.
  - The default variables can be overridden when defined under the node groups or individual nodes.

## Supported designs

`eos_designs` with the `mpls` design type supports any arbitrary physical mesh topology by combining and interconnecting different node types with the core_interfaces dictionary. You can also extend `eos_designs` to support your own topology by using [`node_type_keys`](node-types.html) to create your own node type

### Arbitrary Mesh or L3LS Topology

- The **eos_designs** role with the `mpls` design type supports any type of topology consisting of any combination of pe-routers, p-routers and rr-routers.
- Any node group of 2 or more rr-routers will form a Route Reflector cluster. The core_interfaces construct is used to define underlay interfaces and associated interface profiles.

### Variables and Options

By setting the `design.type` to `mpls`, the default node-types and templates described in these documents will be used.

```yaml
# AVD Design | Optional
design:
  type: < "l3ls-evpn" | "mpls" | default -> "l3ls-evpn" >
```

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

Unlike with the l3ls-evpn design type, underlay p2p links are built using the `core_interfaces` data model described [here](core-interfaces-BETA.md).

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
    mpls_overlay_role: < client | server | none | default -> refer to node type variable table >

    # List of inventory hostname acting as MPLS route-reflectors.
    mpls_route_reflectors: [ '< inventory_hostname_of_mpls_route_reflectors >' ]

    # Overlay Address Families to activate. Any subset of evpn, vpn-ipv4, vpn-ipv6.
    overlay_address_families: [ '< address_family_1 >', '< address_family_2 >', '< address_family_3 >' ] -> default [ 'evpn' ]
```

## Unsupported variables

```yaml
< node_type_key >:

  defaults:
    vtep_loopback_ipv4_pool: < IPv4_address/Mask  >
    vtep_loopback: < Loopback_interface_1 >
    evpn_role: < client | server | none | default -> refer to node type variable table >
    evpn_route_servers: [ '< inventory_hostname_of_evpn_server >' ]
    evpn_services_l2_only: < false | true >
    mlag: < true | false -> default true >
    mlag_dual_primary_detection: < true | false -> default false >
    mlag_interfaces: [ < ethernet_interface_3 >, < ethernet_interface_4 > ]
    mlag_interfaces_speed: < interface_speed | forced interface_speed | auto interface_speed >
    mlag_peer_l3_vlan: < 0-4094 | false | default -> 4093 >
    mlag_peer_l3_ipv4_pool: < IPv4_network/Mask >
    mlag_peer_vlan: < 0-4094 | default -> 4094 >
    mlag_peer_link_allowed_vlans: < vlans as string | default -> "2-4094" >
    mlag_peer_ipv4_pool: < IPv4_network/Mask >
    uplink_ipv4_pool: < IPv4_address/Mask  >
    uplink_interfaces: [ < ethernet_interface_1 >, < ethernet_interface_2 > ]
    uplink_switches: [ < uplink_switch_inventory_hostname 01 >, < uplink_switch_inventory_hostname 02 > ]
    max_uplink_switches: < integer >
    max_parallel_uplinks: < integer >
    uplink_ptp:
      enable: < boolean >
    uplink_macsec:
      profile: "< MacSec profile name >"
    uplink_interface_speed: < interface_speed | forced interface_speed | auto interface_speed >
        uplink_switch_interfaces: [ < ethernet_interface_1 >, < ethernet_interface_2 > ]
```
