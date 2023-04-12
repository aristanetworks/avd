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

## Supported designs

`eos_designs` supports multiple options such as L3LS-EVPN with 3-stage or 5-stage, and L2LS. The sections below highlight these 2 topologies, but you can extend `eos_designs` to support your own topology by using [`node_type_keys`](node-types.md) to create your own node type.

## Design type

By setting the `design.type` variable, the default node-types and templates described in these documents will be used.

!!! note
    Please note, MPLS is currently in beta. For full node type information, see [MPLS Design](./fabric-topology-mpls-BETA.md) section.

```yaml
# AVD Design | Optional
design:
  type: < "l3ls-evpn" | "l2ls" | "mpls" | default -> "l3ls-evpn" >
```

### 3-stage Clos Topology Support (Leaf & Spine)

- The **eos_designs** role support various deployments with layer 3 leaf and spine (3-stage Clos) and optionally, with dedicated overlay controllers.
- 3 stage Clos fabric can be represented as spines, L3 leafs and L2 leafs, and also referred to as a "POD".

### 5-stage Clos Topology Support (Super Spine)

- The **eos_designs** role support lager deployments with super-spines (5-stage Clos) and optionally, with dedicated overlay controllers.
- 5 stage Clos fabric can be represented as multiple leaf-spine structures (called PODs - Point of Delivery) interconnected by super-spines.
- The logic to deploy every leaf-spine POD fabric remains unchanged.
- Super-spines can be deployed as a single plane (typically chassis switches) or multiple planes.

### Layer 2 Leaf Spine

- The **eos_designs** role support various deployments with layer 2 leaf and spine. For example, routing may terminate at the spine level or an external L3 device.
- The Clos fabric can be represented as L3 spines, spines, and leafs.

## Node Type Variables

The following table provide information on the default node types that have been pre-defined in [`eos_designs/defaults/main/defaults-node-type-keys.yml`](https://github.com/aristanetworks/ansible-avd/tree/devel/ansible_collections/arista/avd/roles/eos_designs/defaults). To customize or create new node types, please refer to [node types definition](node-types.md)

### L3LS

| Node Type Key      | Underlay Router | Uplink Type | Default EVPN Role  | L2 Network Services | L3 Network Services | VTEP | MLAG Support | Connected Endpoints |
| ------------------ | --------------- | ------------ | ----------------- | ------------------- | ------------------- | ---- | ------------ | ------------------- |
| super_spine        | ✅              | p2p          | none              | ✘                  | ✘                   | ✘   | ✘            | ✘                  |
| spine              | ✅              | p2p          | server            | ✘                  | ✘                   | ✘   | ✘            | ✘                  |
| l3leaf             | ✅              | p2p          | client            | ✅                 | ✅                  | ✅  | ✅           | ✅                 |
| l2leaf             | ✘               | port-channel | none              | ✅                 | ✘                   | ✘   | ✅           | ✅                 |
| overlay_controller | ✅              | p2p          | server            | ✘                  | ✘                   | ✘   | ✘            | ✘                  |

### L2LS

| Node Type Key      | Underlay Router | Uplink Type | Default EVPN Role  | L2 Network Services | L3 Network Services | VTEP | MLAG Support | Connected Endpoints |
| ------------------ | --------------- | ------------ | ----------------- | ------------------- | ------------------- | ---- | ------------ | ------------------- |
| l3spine              | ✅              | p2p          | none            | ✅                  | ✅                   | ✘   | ✅            | ✅                  |
| spine             | ✘              | port-channel | none            | ✅                 | ✘                  | ✘  | ✅           | ✅                 |
| leaf             | ✘               | port-channel | none              | ✅                 | ✘                   | ✘   | ✅           | ✅                 |

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

      # Unique identifier per node_type | Required.
      id: < integer >

      # Node management IP address | Optional.
      mgmt_ip: < IPv4_address/Mask >

      # Node management IPv6 address | Optional.
      ipv6_mgmt_ip: < IPv6_address/Mask >

      # System Mac Address | Optional
      # Set to the same MAC address as available in "show version" on the device.
      # NOTE: the "mac_address" variable used in dhcp_provisioner role is
      # different from this variable
      # "system_mac_address" can also be set directly as a hostvar.
      # If both are set, the setting under "Fabric Topology" takes precedence.
      system_mac_address: < "xx:xx:xx:xx:xx:xx" >
      # Serial Number | Optional
      # Set to the Serial Number of the device
      # For  now only used for documentation purpose in the fabric
      # documentation.
      # "serial_number" can also be set directly as a hostvar.
      # If both are set, the setting under "Fabric Topology" takes precedence.
      serial_number: < string >

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

    # Force configuration of "ip routing" even on L2 devices | Optional
    # Use this to retain behavior of AVD versions below 4.0.0.
    always_configure_ip_routing: < true | false | default -> false >

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

    # Local uplink interfaces (list). | Optional
    # If uplink_interfaces is not defined, platform-specific defaults (defined under default_interfaces) will be used instead.
    # Please note that default_interfaces are not defined by default - you should define these yourself.
    uplink_interfaces: [ < ethernet_interface_1 >, < ethernet_interface_2 > ]

    # Uplink switches (list). | Required.
    # If parallel uplinks are in use, update max_parallel_uplinks below and specify each uplink switch multiple times
    # e.g. uplink_switches: [ 'DC1-SPINE1', 'DC1-SPINE1', 'DC1-SPINE2', 'DC1-SPINE2' ]
    uplink_switches: [ < uplink_switch_inventory_hostname 01 >, < uplink_switch_inventory_hostname 02 > ]

    # Uplink native vlan | Optional
    # Only applicable to switches with layer-2 port-channel uplinks
    # A suspended (disabled) vlan will be created in both ends of the link unless the vlan
    # is defined under network services.
    # By default the uplink will not have a native_vlan configured, so EOS defaults to vlan 1.
    uplink_native_vlan: < vlan_id >

    # Maximum number of uplink switches. | Optional
    # Changing this value may change IP Addressing on uplinks.
    # Can be used to reserve IP space for future expansions.
    max_uplink_switches: < integer >

    # Number of parallel links towards uplink switches | Optional
    # Changing this value may change interface naming on uplinks (and corresponding downlinks)
    # Can be used to reserve interfaces for future parallel uplinks
    max_parallel_uplinks: < integer >

    # Enable PTP on uplink links | Optional
    uplink_ptp:
      enable: < boolean >

    # Enable MacSec on all uplinks | Optional
    uplink_macsec:
      profile: "< MacSec profile name >"

    # Point-to-Point interface speed - will apply to uplinks on both ends | Optional.
    uplink_interface_speed: < interface_speed | forced interface_speed | auto interface_speed >

    # Custom structured config applied to "uplink_interfaces", and "uplink_switch_interfaces"
    # When uplink_type == "p2p", custom structured config added under ethernet_interfaces.<interface> for eos_cli_config_gen
    # Overrides the settings on the ethernet interface level.
    # When uplink_type == "port-channel", custom structured config added under port_channel_interfaces.<interface> for eos_cli_config_gen
    # Overrides the settings on the port-channel interface level.
    # "uplink_structured_config" is applied after "structured_config", so it can override "structured_config" defined on node-level.
    uplink_structured_config: < dictionary >

  # When nodes are part of node group
  node_groups:
    < node-group-name >:
      nodes:
        # Uplink switches interfaces (list), interface located on uplink switch. | Optional
        # If uplink_switch_interfaces is not defined, platform-specific defaults (defined under default_interfaces) will be used instead.
        # Please note that default_interfaces are not defined by default - you should define these yourself.
        uplink_switch_interfaces: [ < ethernet_interface_1 >, < ethernet_interface_2 > ]
        # short_esi only valid for l2leaf devices using port-channel uplink
        # Setting short_esi: auto generates the short_esi automatically using a hash of configuration elements.
        short_esi: < 0000:0000:0000 | auto >

  # When nodes are not in node_group
  nodes:
    <node inventory hostname>:
      # Uplink switches interfaces (list), interface located on uplink switch. | Required.
      uplink_switch_interfaces: [ < ethernet_interface_1 >, < ethernet_interface_2 > ]
```

#### Default Interfaces

- Set default uplink, downlink and mlag interfaces which will be used if these interfaces are not defined on a device (either directly or through inheritance).
- These are defined based on the combination of node_type (e.g. l3leaf or spine) and a regex for matching the platform.
- A list of interfaces or interface ranges can be specified.
- Each list item supports range syntax that can be expanded into a list of interfaces. Interface range examples:
  - Ethernet49-52/1: Expands to [ Ethernet49/1, Ethernet50/1, Ethernet51/1, Ethernet52/1 ]
  - Ethernet1/31-34/1: Expands to [ Ethernet1/31/1, Ethernet1/32/1, Ethernet1/33/1, Ethernet1/34/1 ]
  - Ethernet49-50,53-54: Expands to [ Ethernet49, Ethernet50, Ethernet53, Ethernet54 ]
  - Ethernet1-2/1-4: Expands to [ Ethernet1/1, Ethernet1/2, Ethernet1/3, Ethernet1/4, Ethernet2/1, Ethernet2/2, Ethernet2/3, Ethernet2/4 ]
- `uplink_interfaces` and `mlag_interfaces` under `default_interfaces` are directly inherited by `uplink_interfaces` and `mlag_interfaces`.
- `downlink_interfaces` are referenced by the child switch (e.g. the leaf in a leaf/spine network). Essentially the child switch indexes into an upstream switch's `default_downlink_interfaces` using the child switch ID.  This is then used to build `uplink_switch_interfaces` for that child.
  - In the case of `max_parallel_uplinks` > 1 the `default_downlink_interfaces` are mapped with consecutive downlinks per child ID.
  - Example for `max_parallel_uplinks: 2`, downlink interfaces will be mapped as `[ <downlink1 to leaf-id1>, <downlink2 to leaf-id1>, <downlink1 to leaf-id2>, <downlink2 to leaf-id2> ...]`
- Please note that no default interfaces are defined in AVD itself. You will need to create your own based on the example below.

```yaml
default_interfaces:

    # List of node type keys | Required
  - types: [ < node_type_key >, < node_type_key > ]

    # List of platform families  | Required
    # This is defined as a Python regular expression that matches the full platform type
    platforms: [ < Arista platform family regex >, < Arista platform family regex > ]

    # List of interfaces or interfaces ranges for each type of default interface | Required
    uplink_interfaces: [ < interface_range | interface >, < interface_range | interface > ]
    mlag_interfaces: [ < interface_range | interface >, < interface_range | interface > ]
    downlink_interfaces: [ < interface_range | interface >, < interface_range | interface > ]

    # Example
  - types: [ spine, l3leaf ]
    platforms: [ "7050[SC]X3", vEOS.*, default ]
    uplink_interfaces: [ Ethernet49-54/1 ]
    mlag_interfaces: [ Ethernet55-56/1 ]
    downlink_interfaces: [ Ethernet1-32/1 ]
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
    # Node BGP AS | Required.
    # For eBGP topologies, bgp_as can be defined as a range of ASNs.  This range will be expanded and ASNs allocated
    # according to the following rules:
    #  - Standalone nodes and Non-MLAG (i.e. EVPN A/A multi-homing) node groups will be allocated unique ASNs from the range based on
    #    the node's ID.
    #  - Switches in MLAG pairs will be allocated a single ASN for both, based on the node ID of the first node in the node group.
    # Examples:
    # bgp_as: 65101-65110                 Contiguous range of ASNs.
    # bgp_as: 65001,65010,65020,65030     Non-contiguous range of ASNs.
    # bgp_as: 65000.101-125               Contiguous range of 4-byte ASNs, increment in the last 2 bytes.
    # bgp_as: 64512                       Single AS, no range.
    # Commas and hyphens can be combined in more or less any combination.
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

      # Only configure VLANs, SVIs, VRFs in use by connected endpoints or downstream L2 switches.
      # Note! This feature only considers configuration managed by eos_designs.
      # This excludes structured_config, custom_structured_configuration_, raw_eos_cli, eos_cli, custom templates, configlets etc.
      only_vlans_in_use: < true | false | default -> false >

    # Activate or deactivate IGMP snooping | Optional, default is true
    igmp_snooping_enabled: < true | false >
```

### BGP & EVPN Multi-Domain Gateway

```yaml
< node_type_key >:

  defaults:
    # Node is acting as EVPN Multi-Domain Gateway | Optional.
    # New BGP peer-group is generated between EVPN GWs in different domains or between GWs and Route Servers. Name can be changed under "bgp_peer_groups.evpn_overlay_core" variable
    # L3 rechability for different EVPN GWs must be already in place, it is recommended to use DCI & L3 Edge if Route Servers and GWs are not defined under the same Ansible inventory.
    evpn_gateway:

      # Define remote peers of the EVPN VXLAN Gateway. If the hostname can be found in the inventory, ip_address and BGP ASN will be automatically populated. Manual override takes precedence. If the peer's hostname can not be found in the inventory, ip_address and bgp_as must be defined.
      remote_peers:
        - hostname: < Inventory hostname of remote EVPN GW server >
          ip_address: < Peering IP of remote Route Server >
          bgp_as: < BGP ASN of remote Route Server >
        - hostname: < Hostname of remote EVPN GW server >
          ip_address: < Peering IP of remote Route Server >
          bgp_as: < BGP ASN of remote Route Server >

      # Specific BGP EVPN Gateway functionality for route types 2 (MAC-IP), 3 (IMET) and 5 (IP-PREFIX) can be enabled separately as needed.
      evpn_l2:
        enabled: < true | false | Default -> False >
      evpn_l3:
        enabled: < true | false | Default -> False >
        inter_domain: < true | false | Default -> True >
```

### BGP & IP-VPN Gateway

```yaml
< node_type_key >:

  defaults:
    # Node is acting as IP-VPN Gateway for EVPN to MPLS-IP-VPN Interworking | Optional.
    # The BGP peer group used for this is "bgp_peer_groups.ipvpn_gateway_peers".
    # L3 Reachability is required for this to work, the preferred method to establish underlay connectivity is to use core_interfaces.
    ipvpn_gateway:
        enabled: < true | false | default -> False >

        # Domain IDs are required to perform D-Path lookups for loop prevention. If omitted, the defaults are used.
        evpn_domain_id: < "nn:nn" | default -> "0:1" >
        ipvpn_domain_id: < "nn:nn" | default -> "0:2" >

        # D-path can be turned off for the inter-vpn export if desired.
        enable_d_path: < true | false | default -> true >

        # Maximum number of routes to allow from the MPLS domain.
        maximum_routes: < integer | default -> 0 >

        # Optional local-as to use when peering to the MPLS domain.
        local_as: < bgp_asn >

        # Address families in which to perform interworking.
        address_families: < List of address families | default -> [ vpn-ipv4 ] >

        # Define remote peers of the EVPN to IP-VPN Gateway. The hostname, ip_address and bgp_asn variables must be defined for each remote peer.
        remote_peers:
          - hostname: < Hostname of remote mpls-vpn peer >
            ip_address: < Peering IP of remote mpls-vpn peer >
            bgp_as: < bgp_asn of remote mpls-vpn peer >
          - hostname: < Hostname of remote mpls-vpn peer >
            ip_address: < Peering IP of remote mpls-vpn peer >
            bgp_as: < bgp_asn of remote mpls-vpn peer >
```

### MLAG configuration management

```yaml
< node_type_key >:

  defaults:
    # Enable / Disable auto MLAG, when two nodes are defined in node group.
    mlag: < true | false -> default true >

    # Enable / Disable MLAG dual primary detection
    mlag_dual_primary_detection: < true | false -> default false >

    # Set origin of routes received from MLAG iBGP peer to incomplete. The purpose is to optimize routing for leaf
    # loopbacks from spine perspective and avoid suboptimal routing via peerlink for control plane traffic.
    mlag_ibgp_origin_incomplete: < true | false | default -> true >

    # MLAG interfaces (list) | Optional, even when MLAG leafs present in topology.
    # If mlag_interfaces is not defined, platform-specific defaults (defined under default_interfaces) will be used instead.
    # Please note that default_interfaces are not defined by default - you should define these yourself.
    mlag_interfaces: [ < ethernet_interface_3 >, < ethernet_interface_4 > ]

    # MLAG interfaces speed | Optional and depends on mlag_interfaces to be defined
    mlag_interfaces_speed: < interface_speed | forced interface_speed | auto interface_speed >

    # MLAG peer link port-channel id | Optional; if not set, the mlag port-channel id is
    # generated based on the digits of the first interface present in 'mlag_interfaces'.
    # Valid port-channel id numbers are < 1-2000 > for EOS < 4.25.0F and < 1 - 999999 > for EOS >= 4.25.0F.
    mlag_port_channel_id: < integer >

    # Underlay L3 peering SVI interface id
    # If set to false or the same vlan as mlag_peer_vlan the mlag_peer_vlan will be used for L3 peering.
    mlag_peer_l3_vlan: < 0-4094 | false | default -> 4093 >

    # IP address pool used for MLAG underlay L3 peering | *Required when MLAG leafs present in topology.
    # IP is derived from the node id. Assign a prefix that can accomodate n * /31 subnets, where n is the highest id assigned to an MLAG switch.
    mlag_peer_l3_ipv4_pool: < IPv4_network/Mask >

    # MLAG Peer Link (control link) SVI interface id.
    mlag_peer_vlan: < 0-4094 | default -> 4094 >

    # MLAG Peer Link allowed VLANs
    mlag_peer_link_allowed_vlans: < vlans as string | default -> "2-4094" >

    # IP address pool used for MLAG Peer Link (control link) | *Required when MLAG leafs present in topology.
    # IP is derived from the node id. Assign a prefix that can accomodate n * /31 subnets, where n is the highest id assigned to an MLAG switch.
    mlag_peer_ipv4_pool: < IPv4_network/Mask >

    # Custom structured config applied to MLAG peer link port-channel id.
    # Added under port_channel_interfaces.<interface> for eos_cli_config_gen.
    # Overrides the settings on the port-channel interface level.
    # "mlag_port_channel_structured_config" is applied after "structured_config", so it can override "structured_config" defined on node-level.
    mlag_port_channel_structured_config: < dictionary >

    # Custom structured config applied to MLAG Peer Link (control link) SVI interface id.
    # Added under vlan_interfaces.<interface> for eos_cli_config_gen.
    # Overrides the settings on the vlan interface level.
    # "mlag_peer_vlan_structured_config" is applied after "structured_config", so it can override "structured_config" defined on node-level.
    mlag_peer_vlan_structured_config: < dictionary >

    # Custom structured config applied to MLAG underlay L3 peering SVI interface id.
    # Added under vlan_interfaces.<interface> for eos_cli_config_gen.
    # Overrides the settings on the vlan interface level.
    # "mlag_peer_l3_vlan_structured_config" is applied after "structured_config", so it can override "structured_config" defined on node-level.
    mlag_peer_l3_vlan_structured_config: < dictionary >

    # Spanning tree mode | Required.
    spanning_tree_mode: < mstp | rstp | rapid-pvst | none >

    # Spanning tree priority.
    spanning_tree_priority: < spanning-tree priority -> default 32768 >

    # Spanning tree priority.
    spanning_tree_root_super: < true | false  >

    # Virtual router mac address for anycast gateway | Required when using VARP or Anycast IP on SVIs.
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
