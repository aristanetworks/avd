# Fabric Topology Variables

The fabric topology variables define the connectivity between the super-spine, spines, L3 leafs, L2 leafs and overlay controllers.
The variables should be applied to all devices in the fabric.

<div style="text-align:center">
  <img src="../../../../../media/topology.gif" />
</div>

As per the diagram above, the topology hierarchy is the following:

fabric_name > dc_name > pod_name

- Fabric Name, required to match Ansible Group name covering all devices in the Fabric | Required.

```yaml
fabric_name: < Fabric_Name >
```

- DC Name, required to match Ansible Group name covering all devices in the DC | Required for 5-stage CLOS (Super-spines)

```yaml
dc_name: < DC_Name >
```

-  POD Name, only used in Fabric Documentation | Optional, fallback to dc_name and then to fabric_name. Recommended to be common between Spines, Leafs within a POD (One l3ls topology)

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

## 3 Stage CLOS Topology Support (Leaf & Spine)

 - The **eos_designs** role support various deployments with layer 3 leaf and spine (3 stage CLOS) and optionally, with dedicated overlay controllers.
 - 3 stage CLOS fabric can be represented as spines, L3 leafs and L2 leafs, and also referred to as a "POD".


## 5 Stage CLOS Topology Support (Super Spine)

- The **eos_designs** role support lager deployments with super-spines (5 stage CLOS) and optionally, with dedicated overlay controllers.
- 5 stage CLOS fabric can be represented as multiple leaf-spine structures (called PODs - Point of Delivery) interconnected by super-spines.
- The logic to deploy every leaf-spine POD fabric remains unchanged.
- Super-spines can be deployed as a single plane (typically chassis switches) or multiple planes.

**Limitations:**

- Current AVD release supports single plane deployment only.
- Only eBGP underlay is supported for super-spine deployment.
- Spines in every POD must have unique AS per POD.

## Type Variable

- The `type:` variable needs to be defined for each device in the fabric.
- This is leveraged to load the appropriate template to generate the configuration.

**Variables and Options:**

```yaml
# define the layer type
type: < spine | l3leaf | l2leaf | super-spine | overlay-controller >
```

**Example:**

```yaml
# Defined in SPINE.yml file
type: spine

# Defined in L3LEAFS.yml
type: l3leaf

# Defined in L2LEAFS.yml
type: l2leaf

# Defined in SUPER-SPINES.yml
type: super-spine

# Defined in ROUTE-SERVERS.yml
type: overlay-controller
```

## Spine Variables

**Variables and Options:**

```yaml
# Defined in FABRIC.yml

# Maximum number of spines, changing this parameter affects address allocation.
# Set this number to potential growth of spine nodes, so fabric IPs don't get recalculated
# when additional spines are added in the future
max_spines: < integer >= number of spine nodes | default spine.nodes | length >

spine:

  # Arista platform family | Required.
  platform: < Arista Platform Family >

  # Rack that the switch is located in (only used in snmp_settings location) | Optional
  rack: < rack_name >

  # Spine BGP AS | Required.
  bgp_as: < bgp_as >

  defaults:
    # EOS CLI rendered directly on the root level of the final EOS configuration
    raw_eos_cli: |
      < multiline eos cli >

  # Specify dictionary of Spine nodes | Required.
  nodes:
    < inventory_hostname >:

      # Unique identifier | Required.
      id: < integer >

      # EVPN Role for Overlay BGP Peerings | Optional, default is server
      # For IBGP overlay "server" means route-reflector. For EBGP overlay "server" means route-server.
      evpn_role: < client | server | none | default -> server  >

      # Peer with these EVPN Route Servers / Route Reflectors | Optional
      evpn_route_servers: [ < route_server_inventory_hostname >, < route_server_inventory_hostname >]

      # Node management IP address | Optional.
      mgmt_ip: < IPv4_address/Mask >

      # EOS CLI rendered directly on the root level of the final EOS configuration
      raw_eos_cli: |
        < multiline eos cli >

    < inventory_hostname >:
      id: < integer >
      mgmt_ip: < IPv4_address/Mask >
```

**Example:**

```yaml
# Defined in FABRIC.yml

max_spines: 4

spine:
  platform: vEOS-LAB
  bgp_as: 65001
  nodes:
    DC1-SPINE1:
      id: 1
      mgmt_ip: 192.168.2.101/24
    DC1-SPINE2:
      id: 2
      mgmt_ip: 192.168.2.102/24
```

## L3 Leaf Variables

**Variables and Options:**

```yaml
l3leaf:

  # All variables defined under `node_groups` dictionary can be defined under the defaults key will be inherited by all L3 leafs.
  # The variables defined under a specific `node_group` will take precedence over defaults.
  defaults:

  # The node groups are groups of one or multiple nodes where specific variables can be defined related to the topology
  # and allowed L3 and L2 network services.
  node_groups:

    # node_group_1, will result in stand-alone leaf.
    < node_group_1 >:

      # All variables defined under `defaults` will be inherited by the node group, if not specifically set inside it.

      # Arista platform family. | Required
      platform: < Arista Platform Family >

      # Rack that the switch is located in (only used in snmp_settings location) | Optional
      rack: < rack_name >

      # Parent spine switches (list), corresponding to uplink_to_spine_interfaces and spine_interfaces | Required.
      spines: [ < spine_inventory_hostname >, < spine_inventory_hostname > ]

      # Uplink to spine interfaces (list), interface located on L3 Leaf,
      # corresponding to spines and spine_interfaces | Required.
      uplink_to_spine_interfaces: [ < ethernet_interface_1 >, < ethernet_interface_2 > ]

      # Point-to-Point interface speed - will apply to L3 Leaf and Spine switches | Optional.
      p2p_link_interface_speed: < interface_speed | forced interface_speed | auto interface_speed >

      # Enable / Disable auto MLAG, when two nodes are defined in node group.
      mlag: < true | false -> default true >

      # Enable / Disable MLAG dual primary detection
      mlag_dual_primary_detection: < true | false -> default false >

      # MLAG interfaces (list) | Required when MLAG leafs present in topology.
      mlag_interfaces: [ < ethernet_interface_3 >, < ethernet_interface_4 >]

      # Underlay L3 peering SVI interface id
      mlag_peer_l3_vlan: < 0-4094 | default -> 4093 >

      # MLAG Peer Link (control link) SVI interface id
      mlag_peer_vlan: < 0-4094 | default -> 4094 >

      # Spanning tree mode | Required.
      spanning_tree_mode: < mstp | rstp | rapid-pvst | none >

      # Spanning tree priority.
      spanning_tree_priority: < spanning-tree priority -> default 32768 >

      # Spanning tree priority.
      spanning_tree_root_super: < true | false  >

      # Virtual router mac address for anycast gateway | Required.
      virtual_router_mac_address: < mac address >

      # Activate or deactivate IGMP snooping | Optional, default is true
      igmp_snooping_enabled: < true | false >

      # L3 Leaf BGP AS. | Required.
      # Inheritence: node > node_group > defaults
      bgp_as: < bgp_as >

      # EVPN Role for Overlay BGP Peerings | Optional, default is client
      # For IBGP overlay "server" means route-reflector. For EBGP overlay "server" means route-server.
      evpn_role: < client | server | none | default -> client  >

      # Peer with these EVPN Route Servers / Route Reflectors | Optional, default to content of spines variable
      evpn_route_servers: [ < route_server_inventory_hostname >, < route_server_inventory_hostname >]

      # Filter L3 and L2 network services based on tenant and tags (and operation filter) | Optional
      # If filter is not defined will default to all
      filter:
        tenants: [ < tenant_1 >, < tenant_2 > | default all ]
        tags: [ < tag_1 >, < tag_2 > | default -> all ]

        # Force VRFs in a tenant to be configured even if VLANs are not included in tags | Optional
        # Useful for "border" leaf.
        always_include_vrfs_in_tenants: [ < tenant_1 >, < tenant_2 >, "all" ]

      # Possibility to prevent configuration of Tenant VRFs and SVIs | Optional, default is false
      # This allows support for centralized routing.
      evpn_services_l2_only: < false | true >

      # EOS CLI rendered directly on the root level of the final EOS configuration
      raw_eos_cli: |
        < multiline eos cli >

      # The node name must be the same name as inventory_hostname | Required
      # When two nodes are defined, this will automatically configure the nodes as an MLAG pair,
      # unless the "l3leaf.defaults.mlag:" key is set to false.
      nodes:

        # First node
        < l3_leaf_inventory_hostname_1 >:

          # Unique identifier | Required.
          id: < integer >

          # Node management IP address | Optional.
          mgmt_ip: < IPv4_address/Mask >

          # Uplink to spine interfaces (list), interface located on L3 Leaf,
          # corresponding to spines and spine_interfaces | Required.
          # Inheritance: node > node_group > defaults
          uplink_to_spine_interfaces: [ < ethernet_interface_1 >, < ethernet_interface_2 > ]

          # Spine interfaces (list), interface located on Spine,
          # corresponding to spines and uplink_to_spine_interfaces | Required.
          spine_interfaces: [ < ethernet_interface_1 >, < ethernet_interface_1 > ]

          # L3 Leaf BGP AS. | Required.
          # Inheritance: node > node_group > defaults
          bgp_as: < bgp_as >

          # EOS CLI rendered directly on the root level of the final EOS configuration
          # Overrides the setting on node_group level.
          raw_eos_cli: |
            < multiline eos cli >

    # node_group_2, will result in MLAG pair.
    < node_group_2 >:
      bgp_as: < bgp_as >
      filter:
        tenants: [ < tenant_1 >, < tenant_2 > | default all ]
        tags: [ < tag_1 >, < tag_2 > | default -> all ]
      nodes:

        # Second node
        < l3_leaf_inventory_hostname_2 >:
          id: < integer >
          mgmt_ip: < IPv4_address/Mask >
          spine_interfaces: [ < ethernet_interface_2 >, < ethernet_interface_2 > ]

        # Third node
        < l3_leaf_inventory_hostname_3 >:
          id: < integer >
          mgmt_ip: < IPv4_address/Mask >
          spine_interfaces: [ < ethernet_interface_3 >, < ethernet_interface_3 > ]
```

**Example:**

```yaml
# Defined in FABRIC.yml

l3leaf:
  defaults:
    platform: 7050X3
    bgp_as: 65100
    spines: [ DC1-SPINE1, DC1-SPINE2 ]
    uplink_to_spine_interfaces: [ Ethernet1, Ethernet2 ]
    mlag_interfaces: [ Ethernet3, Ethernet4 ]
    spanning_tree_mode: mstp
    spanning_tree_priority: 4096
    virtual_router_mac_address: 00:1c:73:00:dc:01
  node_groups:
    DC1_LEAF1:
      bgp_as: 65101
      filter:
        tenants: [ Tenant_A, Tenant_B, Tenant_C ]
        tags: [ opzone ]
      mlag_dual_primary_detection: false
      nodes:
        DC1-LEAF1A:
          id: 1
          mgmt_ip: 192.168.2.105/24
          spine_interfaces: [ Ethernet1, Ethernet1 ]
    DC1_LEAF2:
      bgp_as: 65102
      filter:
        tenants: [ Tenant_A ]
        tags: [ opzone, web, app, db, vmotion, nfs ]
      nodes:
        DC1-LEAF2A:
          id: 2
          mgmt_ip: 192.168.2.106/24
          spine_interfaces: [ Ethernet2, Ethernet2 ]
        DC1-LEAF2B:
          id: 3
          mgmt_ip: 192.168.2.107/24
          spine_interfaces: [ Ethernet3, Ethernet3 ]
    DC1_SVC3:
      bgp_as: 65103
      platform: 7280R
      mlag: false
      filter:
        tenants: [ Tenant_A ]
        tags: [ erp1 ]
      nodes:
        DC1-SVC3A:
          id: 4
          mgmt_ip: 192.168.2.108/24
          spine_interfaces: [ Ethernet4, Ethernet4 ]
        DC1-SVC3B:
          id: 5
          mgmt_ip: 192.168.2.109/24
          spine_interfaces: [ Ethernet5, Ethernet5 ]
```

## L2 Leafs Variables

**Variables and Options:**

```yaml
l2leaf:

  # All variables defined under `node_groups` dictionary can be defined under the defaults key will be inherited by all L2 leafs.
  # The variables defined under a specific `node_group` will take precedence over defaults.
  defaults:

  # The node groups are group of one or multiple nodes where specific variables can be defined related to the topology
  # and allowed L3 and L2 network services.
  node_groups:

    # node_group_1, will result in stand-alone leaf.
    < node_group_1 >:

      # All variables defined under `defaults` will be inherited by the node group, if not specifically set inside it.

      # Arista platform family. | Required
      platform: < Arista Platform Family >

      # Rack that the switch is located in (only used in snmp_settings location) | Optional
      rack: < rack_name >

      # Parent L3 switches (list), corresponding to uplink_interfaces and l3leaf_interfaces | Required.
      parent_l3leafs: [ DC1-LEAF2A, DC1-LEAF2B]

      # Uplink interfaces (list), interface located on L2 Leaf,
      # corresponding to parent_l3leafs and l3leaf_interfaces | Required.
      uplink_interfaces: [ < ethernet_interface_1 >, < ethernet_interface_2 > ]

      # Point-to-Point interface speed - will apply to L2 Leaf and L3 Leaf switches | Optional.
      p2p_link_interface_speed: < interface_speed | forced interface_speed | auto interface_speed >

      # Enable / Disable auto MLAG, when two nodes are defined in node group.
      mlag: < true | false -> default true >

      # Enable / Disable MLAG dual primary detection
      mlag_dual_primary_detection: < true | false -> default false >

      # MLAG interfaces (list) | Required when MLAG leafs present in topology.
      mlag_interfaces: [ < ethernet_interface_3 >, < ethernet_interface_4 > ]

      # Set origin of routes received from MLAG iBGP peer to incomplete. The purpose is to optimize routing for leaf
      # loopbacks from spine perspective and avoid suboptimal routing via peerlink for control plane traffic.
      mlag_ibgp_origin_incomplete: < true | false -> default true >

      # MLAG Peer Link (control link) SVI interface id
      mlag_peer_vlan: < 0-4094 | default -> 4094 >

      # Spanning tree mode (note - only mstp has been validated at this time) | Required.
      spanning_tree_mode: < mstp >

      # Spanning tree priority | Required.
      spanning_tree_priority: < spanning-tree priority >

      # Activate or deactivate IGMP snooping for all l2leaf devices | Optional default is true
      igmp_snooping_enabled: < true | false >

      # Filter L3 and L2 network services based on tenant and tags - and filter | Optional
      # If filter is not defined will default to all
      filter:
        tenants: [ < tenant_1 >, < tenant_2 > | default all ]
        tags: [ < tag_1 >, < tag_2 > | default -> all ]

      # Activate or deactivate IGMP snooping for node groups devices
      igmp_snooping_enabled: < true | false >

      # EOS CLI rendered directly on the root level of the final EOS configuration
      raw_eos_cli: |
        < multiline eos cli >

      # The node name must be the same name as inventory_hostname | Required
      # When two nodes are defined, this will automatically configure the nodes as an MLAG pair,
      # unless the "l2leaf.defaults.mlag:" key is set to false.
      nodes:

        # First node
        < l2_leaf_inventory_hostname_1 >:

          # Unique identifier | Required.
          id: < integer >

          # Node management IP address | Optional.
          mgmt_ip: < IPv4_address/Mask >

          # l3leaf interfaces (list), interface located on l3leaf,
          # corresponding to parent_l3leafs and uplink_interfaces | Required.
          l3leaf_interfaces: [ < ethernet_interface_6 >, < ethernet_interface_6 > ]

          # EOS CLI rendered directly on the root level of the final EOS configuration
          # Overrides the setting on node_group level.
          raw_eos_cli: |
            < multiline eos cli >

    # node_group_2, will result in MLAG pair.
    < node_group_2 >:
      parent_l3leafs: [ DC1-SVC3A, DC1-SVC3B ]
      nodes:

        # Second node.
        < l2_leaf_inventory_hostname_2 >:
          id: < integer >
          mgmt_ip: < IPv4_address/Mask >
          l3leaf_interfaces: [ < ethernet_interface_7 >, < ethernet_interface_7 > ]

        # Third node.
        < l2_leaf_inventory_hostname_3 >:
          id: < integer >
          mgmt_ip: < IPv4_address/Mask >
          l3leaf_interfaces: [ < ethernet_interface_8 >, < ethernet_interface_8 > ]

    # node_group_3, will result in Active/Active connection to L3LEAFs.
    # Can be applied on single L2LEAF or MLAG nodes.
    < node_group_3 >:
      parent_l3leafs: [ DC1-SVC3A, DC1-SVC3B ]
      short_esi: < short esi value >
      nodes:

        # First node.
        < l2_leaf_inventory_hostname_2 >:
          id: < integer >
          mgmt_ip: < IPv4_address/Mask >
          l3leaf_interfaces: [ < ethernet_interface_7 >, < ethernet_interface_7 > ]
```

???+ note "Short ESI description"
    To help provide consistency when configuring EVPN A/A ESI values, arista.avd provides an abstraction in the form of a `short_esi` key.
    `short_esi` is an abbreviated 3 octets value to encode [Ethernet Segment ID](https://tools.ietf.org/html/rfc7432#section-8.3.1) and LACP ID.
    Transformation from abstraction to network values is managed by a [filter_plugin](../../../../plugins/README.md) and provides following result:

    - _EVPN ESI_: 0000:0000:0808:0707:0606
    - _LACP ID_: 0808.0707.0606
    - _Route Target_: 08:08:07:07:06:06

    ```yaml
    # Short ESI setting:
    short_esi: 0808:0707:0606

    # Short ESI transformation result:
    esi: 0000:0000:0808:0707:0606
    rt: 08:08:07:07:06:06
    lacp_id: 0808.0707.0606
    ```

**Example:**

```yaml
# Defined in FABRIC.yml

l2leaf:
  defaults:
    platform: vEOS-LAB
    parent_l3leafs: [ DC1-LEAF2A, DC1-LEAF2B ]
    uplink_interfaces: [ Ethernet1, Ethernet2 ]
    mlag_interfaces: [ Ethernet3, Ethernet4 ]
    spanning_tree_mode: mstp
    spanning_tree_priority: 16384
  node_groups:
    DC1_L2LEAF4:
      uplink_interfaces: [ Ethernet11, Ethernet12 ]
      filter:
        tenants: [ Tenant_A ]
        tags: [ opzone, web, app ]
      nodes:
        DC1-L2LEAF4A:
          id: 8
          mgmt_ip: 192.168.2.112/24
          l3leaf_interfaces: [ Ethernet6, Ethernet6 ]
    DC1_L2LEAF5:
      parent_l3leafs: [ DC1-SVC3A, DC1-SVC3B ]
      nodes:
        DC1-L2LEAF5A:
          id: 10
          mgmt_ip: 192.168.2.113/24
          l3leaf_interfaces: [ Ethernet5, Ethernet5 ]
        DC1-L2LEAF5B:
          id: 11
          mgmt_ip: 192.168.2.114/24
          l3leaf_interfaces: [ Ethernet6, Ethernet6 ]
    DC1_L2LEAF6:
      parent_l3leafs: [ DC1-LEAF6A, DC1-LEAF6B ]
      short_esi: 0808:0707:0606
      nodes:
        DC1-L2LEAF6A:
          id: 12
          mgmt_ip: 192.168.200.116/24
          l3leaf_interfaces: [ Ethernet7, Ethernet7 ]
```

## Super Spine Variables

This section provides additional settings to support super-spine in your l3ls-evpn topology

Defaults:

```yaml
max_spine_to_super_spine_links: 1  # number of parallel links between spines and super-spines
```

Assigned to the DC group:

```yaml

# maximum number of super-spines, changing this parameter affects address allocation.
# Set this number to potential growth of super spine nodes, so fabric IPs don't get recalculated
# when additional super spines are added in the future
max_super_spines: < integer >= number of super_spine nodes >
super_spine:
  platform: vEOS-LAB  # super-spine platform
  bgp_as: <super-spine BGP AS>

  defaults:
    # EOS CLI rendered directly on the root level of the final EOS configuration
    raw_eos_cli: |
      < multiline eos cli >

  nodes:
    SU-01:  # super-spine name
      id: 1
      mgmt_ip: 192.168.0.1/24
      # EVPN Role for Overlay BGP Peerings | Optional, default is none
      # For IBGP overlay "server" means route-reflector. For EBGP overlay "server" means route-server.
      evpn_role: < client | server | none | default -> none  >
      # Peer with these EVPN Route Servers / Route Reflectors | Optional
      evpn_route_servers: [ < route_server_inventory_hostname >, < route_server_inventory_hostname >]
      # EOS CLI rendered directly on the root level of the final EOS configuration
      raw_eos_cli: |
        < multiline eos cli >

# IP address range for loopbacks for all super-spines in the DC,
# assigned as /32s
# Assign range larger then total super-spines
super_spine_loopback_network_summary: 192.168.100.0/24

# additional lines for super-spine BGP config
super_spine_bgp_defaults:
  #  - update wait-for-convergence
  #  - update wait-install
  - no bgp default ipv4-unicast
  - distance bgp 20 200 200
  - graceful-restart restart-time 300
  - graceful-restart
```

Assigned to Super Spine Group:

```yaml
type: super-spine  # identifies every host in the group as super-spine
```

Assigned to Every POD Group:

```yaml
spine:
  # list of spine interfaces used as uplinks to super-spines
  # taking `max_spine_to_super_spine_links` into account
  # for example: spine1, spine2, spine3, ...
  # or spine1, spine1, spine2, spine2, etc.
  uplinks_to_super_spine_interfaces: [ Ethernet10, Ethernet11, Ethernet12, Ethernet13 ]
  nodes:
    <spine-hostname>:
      # super-spine interfaces to spines
      # taking `max_spine_to_super_spine_links` into account
      # for example: super-spine1, super-spine2, super-spine3, ...
      # or super-spine1, super-spine1, super-spine2, super-spine2, etc.
      super_spine_interfaces: [ Ethernet1, Ethernet1, Ethernet1, Ethernet1 ]
    <-- etc. -->

# Point to Point Network Summary range, assigned as /31 for each
# uplink interfaces
# Assign range larger then total
# [ max_spines_in_a_POD * max_super_spines * max_spine_to_super_spine_links * 2 ]
super_spine_underlay_p2p_network_summary: 172.31.1.0/24
```

Following variables must be now defined on DC and not POD level:

- `p2p_uplinks_mtu`
- `bgp_peer_groups`

## Overlay Controllers Variables

This section provides options to enable overlay-controller in your l3ls-evpn topology.

Defaults:
```yaml
# The maximum number of uplinks for each overlay_controller.
#This is used to calculate P2P Link IP addresses, and should not be changed after deployment.
max_overlay_controller_to_switch_links: 2
```

Assigned to the DC group:

```yaml
overlay_controller:
  platform: <platform>   # overlay-controller platform

  # All variables defined under `nodes` dictionary can be defined under the defaults key will be inherited by all overlay-controllers.
  # The variables defined under a specific node will take precedence over defaults.
  defaults:

  nodes:
    <inventory_hostname>:
      id: <number> # Starting from 1
      # Rack that the switch is located in (only used in snmp_settings location) | Optional
      rack: < rack_name >
      mgmt_ip: < IPv4_address/Mask >
      remote_switches_interfaces: [ <remote_switch_interface> , <remote_switch_interface> ] # Interfaces on remote switch

      remote_switches: [ <switch_inventory_hostname> , <switch_inventory_hostname> ] #Remote Switches connected to uplink interfaces
      uplink_to_remote_switches: [ <uplink_interface> , <uplink_interface> ]
      bgp_as: <BGP AS>

      # EVPN Role for Overlay BGP Peerings | Optional, default is none
      # For IBGP overlay "server" means route-reflector. For EBGP overlay "server" means route-server.
      evpn_role: < client | server | none | default -> none  >

      # Peer with these EVPN Route Servers / Route Reflectors | Optional
      evpn_route_servers: [ < route_server_inventory_hostname >, < route_server_inventory_hostname > ]

      # EOS CLI rendered directly on the root level of the final EOS configuration
      raw_eos_cli: |
        < multiline eos cli >

# Point to Point Network Summary range, assigned as /31 for each uplink interfaces
# Assign range larger than [ total overlay_controllers * max_overlay_controller_to_switch_links * 2]
overlay_controller_p2p_network_summary: < IPv4_network/Mask >
# IP address summary for BGP evpn overlay peering loopback for Overlay Controllers | Required
# Assigned as /32 to Loopback0
# Assign range larger then:
# [ total overlay_controllers ]
overlay_controller_loopback_network_summary: < IPv4_network/Mask >
# Enable BFD for p2p BGP sessions - useful if the overlay_controller is a VM | Optional
overlay_controller_p2p_bfd: < true | false | default -> false >
# additional lines for overlay-controller BGP config
overlay_controller_bgp_defaults:
  - no bgp default ipv4-unicast
  - distance bgp 20 200 200
  - graceful-restart restart-time 300
  - graceful-restart
```

Assigned to Overlay Controller Group:

```yaml
type: overlay-controller # identifies every host in the group as overlay-controller
```
