The fabric topology variables define the connectivity between the various node types, as well as override the default switch properties.

<div style="text-align:center">
  <img src="../../../media/5-stage-topology.gif" />
</div>

As per the diagram above, the topology hierarchy is the following:

fabric_name > dc_name > pod_name

- Fabric Name, required to match Ansible Group name covering all devices in the Fabric | Required and **must** be an inventory group name.

```yaml
fabric_name: < Fabric_Name >
```

- DC Name, required to match Ansible Group name covering all devices in the DC | Required for 5-stage Clos (Super-spines)

```yaml
dc_name: < DC_Name >
```

- POD Name (optional), fallback to dc_name and then to fabric_name. Recommended to be common between Spines, Leafs within a POD (One l3ls topology)

```yaml
pod_name: < POD_Name >
```

- Connectivity is defined from the child's device perspective.
  - Source uplink interfaces and parent interfaces are defined on the child.
- A static unique identifier (id) is assigned to each device.
  - This is leveraged to derive the IP address assignment from each summary defined in the Fabric Underlay and Overlay Topology Variables.
- Within the l3_leaf and l2_leaf dictionary variables, defaults can be defined.
  - This reduces user input requirements, limiting errors.
  - The default variables can be overridden when defined under the node groups.

### Supported designs

`eos_designs` supports multiple options such as L3LS-EVPN with 3-stage or 5-stage, and L2LS. The sections below highlight these 2 topologies, but you can extend `eos_designs` to support your own topology by using [`node_type_keys`](node-types.md) to create your own node type.

### Design type

By setting the `design.type` variable, the default node-types and templates described in these documents will be used.

```yaml
# AVD Design | Optional
design:
  type: < "l3ls-evpn" | "l2ls" | "mpls" | default -> "l3ls-evpn" >
```

#### 3-stage clos topology support (Leaf & Spine)

- The **eos_designs** role support various deployments with layer 3 leaf and spine (3-stage Clos) and optionally, with dedicated overlay controllers.
- 3 stage Clos fabric can be represented as spines, L3 leafs and L2 leafs, and also referred to as a "POD".

#### 5-stage clos topology support (Super Spine)

- The **eos_designs** role support lager deployments with super-spines (5-stage Clos) and optionally, with dedicated overlay controllers.
- 5 stage Clos fabric can be represented as multiple leaf-spine structures (called PODs - Point of Delivery) interconnected by super-spines.
- The logic to deploy every leaf-spine POD fabric remains unchanged.
- Super-spines can be deployed as a single plane (typically chassis switches) or multiple planes.

#### Layer 2 Leaf Spine

- The **eos_designs** role support various deployments with layer 2 leaf and spine. For example, routing may terminate at the spine level or an external L3 device.
- The Clos fabric can be represented as L3 spines, spines, and leafs.

#### TODO MPLS

### Node Type Variables

The following table provide information on the default node types that have been pre-defined in [`eos_designs/defaults/main/defaults-node-type-keys.yml`](https://github.com/aristanetworks/ansible-avd/tree/devel/ansible_collections/arista/avd/roles/eos_designs/defaults). To customize or create new node types, please refer to [node types definition](node-types.md)

#### L3LS EVPN

| Node Type Key      | Underlay Router | Uplink Type | Default EVPN Role  | L2 Network Services | L3 Network Services | VTEP | MLAG Support | Connected Endpoints |
| ------------------ | --------------- | ------------ | ----------------- | ------------------- | ------------------- | ---- | ------------ | ------------------- |
| super_spine        | ✅              | p2p          | none              | ✘                   | ✘                   | ✘    | ✘            | ✘                  |
| spine              | ✅              | p2p          | server            | ✘                   | ✘                   | ✘    | ✘            | ✘                  |
| l3leaf             | ✅              | p2p          | client            | ✅                  | ✅                  | ✅   | ✅           | ✅                 |
| l2leaf             | ✘               | port-channel | none              | ✅                  | ✘                   | ✘    | ✅           | ✅                 |
| overlay_controller | ✅              | p2p          | server            | ✘                   | ✘                   | ✘    | ✘            | ✘                  |

#### L2LS

| Node Type Key      | Underlay Router | Uplink Type | Default EVPN Role  | L2 Network Services | L3 Network Services | VTEP | MLAG Support | Connected Endpoints |
| ------------------ | --------------- | ------------ | ----------------- | ------------------- | ------------------- | ---- | ------------ | ------------------- |
| l3spine            | ✅              | p2p          | none              | ✅                  | ✅                  | ✘    | ✅           | ✅                  |
| spine              | ✘               | port-channel | none              | ✅                  | ✘                   | ✘    | ✅           | ✅                 |
| leaf               | ✘               | port-channel | none              | ✅                  | ✘                   | ✘    | ✅           | ✅                 |

#### MPLS

| Node Type Key | Underlay Router | Uplink Type | Default Overlay Role | L2 Network Services | L3 Network Services | VTEP | MLAG Support | Connected Endpoints |
| --------------| --------------- | ----------- | -------------------- | ------------------- | ------------------- | ---- | ------------ | ------------------- |
| p             | ✅              | p2p          | none                | ✘                   | ✘                   | ✘    | ✘            | ✘                   |
| rr            | ✅              | p2p          | server              | ✘                   | ✘                   | ✘    | ✘            | ✘                   |
| pe            | ✅              | p2p          | client              | ✅                  | ✅                  | ✅   | ✘            | ✅                  |

### MPLS design guidance and limitations

The MPLS design supports any fabric topology variables already supported by l3ls-evpn, barring the exceptions outlined below:

- Connectivity is defined in a free-standing core_interfaces construct (TODO add link)

#### MPLS designs unsupported variables

TODO - link to unsupported parameters instead instead of yaml

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
    mlag_peer_link_allowed_vlans: < vlans as string >
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
