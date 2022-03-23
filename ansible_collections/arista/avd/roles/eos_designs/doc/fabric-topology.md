# Fabric Topology Variables

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

- DC Name, required to match Ansible Group name covering all devices in the DC | Required for 5-stage CLOS (Super-spines)

```yaml
dc_name: < DC_Name >
```

- POD Name, only used in Fabric Documentation | Optional, fallback to dc_name and then to fabric_name. Recommended to be common between Spines, Leafs within a POD (One l3ls topology)

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

## Supported designs

`eos_designs` supports multiple flavors of L3LS-EVPN topology such as 3-stage CLOS and 5-stage CLOS. Sections below highlight these 2 topologies, but you can extend `eos_designs` to support your own topology by using [`node_type_keys`](node-types.html) to create your own node type

### 3-stage CLOS Topology Support (Leaf & Spine)

- The **eos_designs** role support various deployments with layer 3 leaf and spine (3-stage CLOS) and optionally, with dedicated overlay controllers.
- 3 stage CLOS fabric can be represented as spines, L3 leafs and L2 leafs, and also referred to as a "POD".

### 5-stage CLOS Topology Support (Super Spine)

- The **eos_designs** role support lager deployments with super-spines (5-stage CLOS) and optionally, with dedicated overlay controllers.
- 5 stage CLOS fabric can be represented as multiple leaf-spine structures (called PODs - Point of Delivery) interconnected by super-spines.
- The logic to deploy every leaf-spine POD fabric remains unchanged.
- Super-spines can be deployed as a single plane (typically chassis switches) or multiple planes.

## Node Type Variables

The following table provide information on the default node types that have been pre-defined in [`eos_designs/defaults/main/defaults-node-type-keys.yml`](https://github.com/aristanetworks/ansible-avd/tree/devel/ansible_collections/arista/avd/roles/eos_designs/defaults). To customize or create new node types, please refer to [node types definition](node-types.md)

| Node Type Key      | Underlay Router | Uplink Type | Default EVPN Role  | L2 Network Services | L3 Network Services | VTEP | MLAG Support | Connected Endpoints |
| ------------------ | --------------- | ------------ | ----------------- | ------------------- | ------------------- | ---- | ------------ | ------------------- |
| super_spine        | ✅              | p2p          | none              | ✘                  | ✘                   | ✘   | ✘            | ✘                  |
| spine              | ✅              | p2p          | server            | ✘                  | ✘                   | ✘   | ✘            | ✘                  |
| l3leaf             | ✅              | p2p          | client            | ✅                 | ✅                  | ✅  | ✅           | ✅                 |
| l2leaf             | ✘               | port-channel | none              | ✅                 | ✘                   | ✘   | ✅           | ✅                 |
| overlay_controller | ✅              | p2p          | server            | ✘                  | ✘                   | ✘   | ✘            | ✘                  |

The variables should be applied to all devices in the fabric.

- The `type:` variable needs to be defined for each device in the fabric.
- This is leveraged to load the appropriate template to generate the configuration.

### Variables and Options

As explained above, you can defined your own types of devices. CLI only provides default node types.

```yaml
# define the layer type
type: < spine | l3leaf | l2leaf | super-spine | overlay-controller >
```

### Example

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

All node types have the same structure based on `defaults`, `node_group`, `node` and all variables can be defined in any section and support inheritance like this:

Under `node_type_key:`

```bash
defaults <- node_group <- node_group.node <- node
```

## Node type structure

```yaml
---
<node_type_key>:
  defaults:
    # Define vars for all nodes of this type
  node_groups:
    <node group name>:
    # Vars related to all nodes part of this group
      nodes:
        <node inventory hostname>:
          # Vars defined per node
  nodes:
    <node inventory hostname>:
      # Vars defined per node

      # Unique identifier | Required.
      id: < integer >

      # Node management IP address | Optional.
      mgmt_ip: < IPv4_address/Mask >
```

## Node Variables details

### Generic configuration management

```yaml
< node_type_key >:

  defaults:
    # Arista platform family | Required.
    platform: < Arista Platform Family >

    # Management interface configuration
    mgmt_interface: < mgmt_interface | default -> platform_management_interface -> mgmt_interface -> Management1 >

    # Rack that the switch is located in (only used in snmp_settings location) | Optional
    rack: < rack_name >

    # This configures the Link Tracking Group on a switch as well as adds the p2p-uplinks of the switch as the upstream interfaces.
    # Useful in EVPN multhoming designs.
    link_tracking:
      enabled: < true | false | default -> false >
      # Link Tracking Groups | Optional
      # By default a single group named "LT_GROUP1" is defined with default values. Any groups defined under "groups" will replace the default.
      groups:
        - name: < tracking_group_name >
          recovery_delay: < 0-3600 | default -> platform_settings_mlag_reload_delay -> 300 >
          # Optional
          links_minimum: < 1-100000 >

    # This will generate the "lacp port-id range", "begin" and "end" values based on node "id" and the number of nodes in the "node_group".
    # Unique LACP port-id ranges are recommended for EVPN Multihoming designs.
    lacp_port_id_range:
      enabled: < true | false | default -> false >
      # Recommended size > = number of ports in the switch.
      size: < 1-65535 | default -> 128 >
      # Offset is used to avoid overlapping port-id ranges of different switches | Optional
      # Useful when a "connected-endpoint" is connected to switches in different "node_groups".
      offset: < offset_for_lacp_port_id_range | default -> 0 >

    # EOS CLI rendered directly on the root level of the final EOS configuration | Optional
    raw_eos_cli: |
      < multiline eos cli >

    # Custom structured config for eos_cli_config_gen | Optional
    structured_config: < dictionary >
```

### Uplink management

```yaml
< node_type_key >:

  defaults:
    # IPv4 subnet to use to connect to uplink switches.
    uplink_ipv4_pool: < IPv4_address/Mask  >

    # Local uplink interfaces (list). | Required.
    uplink_interfaces: [ < ethernet_interface_1 >, < ethernet_interface_2 > ]

    # Uplink switches (list). | Required.
    uplink_switches: [ < uplink_switch_inventory_hostname 01 >, < uplink_switch_inventory_hostname 02 > ]

    # Number of interfaces towards uplink switches | Optional
    max_uplink_switches: < integer >

    # Number of parallel links towards uplink switches | Optional
    max_parallel_uplinks: < integer >

    # Enable PTP on uplink links | Optional
    uplink_ptp:
      enable: < boolean >

    # Enable MacSec on all uplinks | Optional
    uplink_macsec:
      profile: "< MacSec profile name >"

    # Point-to-Point interface speed - will apply to uplinks on both ends | Optional.
    uplink_interface_speed: < interface_speed | forced interface_speed | auto interface_speed >

  # When nodes are part of node group
  node_groups:
    < node-group-name >:
      nodes:
        # Uplink switches interfaces (list), interface located on uplink switch. | Required.
        uplink_switch_interfaces: [ < ethernet_interface_1 >, < ethernet_interface_2 > ]

  # When nodes are not in node_group
  nodes:
    <node inventory hostname>:
      # Uplink switches interfaces (list), interface located on uplink switch. | Required.
      uplink_switch_interfaces: [ < ethernet_interface_1 >, < ethernet_interface_2 > ]
```

#### ISIS underlay protocol management

```yaml
< node_type_key >:

  defaults:
    # isis system-id prefix (4.4 hexadecimal)
    isis_system_id_prefix: < hhhh.hhhh >

    # Number of path to configure in ECMP for ISIS
    isis_maximum_paths: < integer >

    # IS type
    is_type: < level-1-2 | level-1 | level-2 | Default -> level-2 >

    # Node-SID base for isis-sr underlay variants. Combined with node id to generate ISIS-SR node-SID.
    node_sid_base: < integer | Default -> 0 >
```

### Loopback and VTEP management

```yaml
< node_type_key >:

  defaults:
    # IPv4 subnet for Loopback0 allocation
    loopback_ipv4_pool: < IPv4_address/Mask  >

    # IPv4 subnet for VTEP/Loopback1 allocation.
    vtep_loopback_ipv4_pool: < IPv4_address/Mask  >

    # Offset all assigned loopback IP addresses.
    # Required when the < loopback_ipv4_pool > is same for 2 different node_types (like spine and l3leaf) to avoid over-lapping IPs.
    # For example, set the minimum offset l3leaf.defaults.loopback_ipv4_offset: < total # spine switches > or vice versa.
    loopback_ipv4_offset: 2

    # Set VXLAN source interface. Loopback1 is default
    vtep_loopback: < Loopback_interface_1 >
```

### BGP & EVPN Control plane

```yaml
< node_type_key >:

  defaults:
    # node BGP AS | Required.
    bgp_as: < bgp_as >

    # List of EOS command to apply to BGP daemon | Optional
    bgp_defaults: [ < List of EOS commands> ]

    # Acting role in EVPN control plane.
    # Override role definition from node_type_keys
    # Can be set per node
    evpn_role: < client | server | none | Default -> refer to node type variable table >

    # List of inventory hostname acting as EVPN route-servers.
    evpn_route_servers: [ '< inventory_hostname_of_evpn_server >' ]
```

### EVPN services management

```yaml
< node_type_key >:

  defaults:
    # Possibility to prevent configuration of Tenant VRFs and SVIs
    # Override node definition "network_services_l3" from node_type_keys
    # This allows support for centralized routing.
    evpn_services_l2_only: < false | true >

    # Filter L3 and L2 network services based on tenant and tags (and operation filter) | Optional
    # If filter is not defined will default to all
    filter:
      tenants: [ < tenant_1 >, < tenant_2 > | default all ]
      tags: [ < tag_1 >, < tag_2 > | default -> all ]

      # Force VRFs in a tenant to be configured even if VLANs are not included in tags | Optional
      # Useful for "border" leaf.
      always_include_vrfs_in_tenants: [ < tenant_1 >, < tenant_2 >, "all" ]

    # Activate or deactivate IGMP snooping | Optional, default is true
    igmp_snooping_enabled: < true | false >
```

### MLAG configuration management

```yaml
< node_type_key >:

  defaults:
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

    # IP address pool used for MLAG Peer Link (control link) | *Required when MLAG leafs present in topology.
    # IP is derived from the node id.
    mlag_peer_ipv4_pool: < IPv4_network/Mask >

    # Spanning tree mode | Required.
    spanning_tree_mode: < mstp | rstp | rapid-pvst | none >

    # Spanning tree priority.
    spanning_tree_priority: < spanning-tree priority -> default 32768 >

    # Spanning tree priority.
    spanning_tree_root_super: < true | false  >

    # Virtual router mac address for anycast gateway | Required.
    virtual_router_mac_address: < mac address >
```

### Inband management VLAN

```yaml
< node_type_key >:

  defaults:
    # Optional IP subnet assigned to Inband Management SVI on l2leafs in default VRF.
    # Parent l3leafs will have SVI with "ip virtual-router" and host-route injection based on ARP. This allows all l3leafs to reuse the same subnet
    # SVI IP address will be assigned as follows:
    # virtual-router: <subnet> + 1
    # l3leaf A      : <subnet> + 2 (same IP on all l3leaf A)
    # l3leaf B      : <subnet> + 3 (same IP on all l3leaf B)
    # l2leafs       : <subnet> + 3 + <l2leaf id>
    # GW on l2leafs : <subnet> + 1
    # Assign range larger than total l2leafs + 5
    inband_management_subnet: < IPv4subnet/mask >

    # VLAN number assigned to Inband Management SVI on l2leafs in default VRF.
    inband_management_vlan: < vlan-id | Default -> 4092 >
```
