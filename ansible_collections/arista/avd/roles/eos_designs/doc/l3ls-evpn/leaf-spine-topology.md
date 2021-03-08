# Fabric Topology Variables

The fabric topology variables define the connectivity between the super-spine, spines, L3 leafs, L2 leafs and overlay controllers.
The variables should be applied to all devices in the fabric.

<!-- ![Figure 2: Topology - naming convention](../../media/topology.gif) -->
<div style="text-align:center">
  <img src="../../../media/topology-l3ls.gif" />
</div>

- Connectivity is defined from the child's device perspective.
  - Source uplink interfaces and parent interfaces are defined on the child.
- A static unique identifier (id) is assigned to each device.
  - This is leveraged to derive the IP address assignment from each summary defined in the Fabric Underlay and Overlay Topology Variables.
- Within the l3_leaf and l2_leaf dictionary variables, defaults can be defined.
  - This reduces user input requirements, limiting errors.
  - The default variables can be overridden when defined under the node groups.
- The ability to define a super-spine layer is planned for a future release of ansible-avd.

## Type Variable

- The `type:` variable needs to be defined for each device in the fabric.
- This is leveraged to load to appropriate template, to generate the configuration.

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

### Spine Variables

**Variables and Options:**

```yaml
# Defined in FABRIC.yml

spine:

  # Arista platform family | Required.
  platform: < Arista Platform Family >

  # Spine BGP AS | Required.
  bgp_as: < bgp_as >

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

      # Node management IP address | Required.
      mgmt_ip: < IPv4_address/Mask >
    < inventory_hostname >:
      id: < integer >
      mgmt_ip: < IPv4_address/Mask >
```

**Example:**

```yaml
# Defined in FABRIC.yml

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

### L3 Leaf Variables

**Variables and Options:**

```yaml
l3leaf:

  # All variables defined under `node_groups` dictionary can be defined under the defaults key will be inherited by all L3 leafs.
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

      # Parent spine switches (list), corresponding to uplink_to_spine_interfaces and spine_interfaces | Required.
      spines: [ < spine_inventory_hostname >, < spine_inventory_hostname > ]

      # Uplink to spine interfaces (list), interface located on L3 Leaf,
      # corresponding to spines and spine_interfaces | Required.
      uplink_to_spine_interfaces: [ < ethernet_interface_1 >, < ethernet_interface_2 > ]

      # Point-to-Point interface speed - will apply to L3 Leaf and Spine switches | Optional.
      p2p_link_interface_speed: < interface_speed | forced interface_speed | auto interface_speed >

      # Enable / Disable auto MLAG, when two nodes are defined in node group.
      mlag: < true | false -> default true >

      # Enable / Disable MLAG dual primary detectiom
      mlag_dual_primary_detection: < true | false -> default false >

      # MLAG interfaces (list) | Required when MLAG leafs present in topology.
      mlag_interfaces: [ < ethernet_interface_3 >, < ethernet_interface_4 >]

      # Spanning tree mode | Required.
      spanning_tree_mode: < mstp | rstp | rapid-pvst | none >

      # Spanning tree priority.
      spanning_tree_priority: < spanning-tree priority -> default 32768 >

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

      # Filter L3 and L2 network services based on tenant and tags ( and operation filter )| Optional
      # If filter is not defined will default to all
      filter:
        tenants: [ < tenant_1 >, < tenant_2 > | default all ]
        tags: [ < tag_1 >, < tag_2 > | default -> all ]

      # Possibility to prevent configuration of Tenant VRFs and SVIs | Optional, default is false
      # This allows support for centralized routing.
      evpn_services_l2_only: < false | true >

      # The node name must be the same name as inventory_hostname | Required
      # When two nodes are defined, this will automatically configure the nodes as an MLAG pair,
      # unless the "l3leaf.defaults.mlag:" key is set to false.
      nodes:

        # First node
        < l3_leaf_inventory_hostname_1 >:

          # Unique identifier | Required.
          id: < integer >

          # Node management IP address | Required.
          mgmt_ip: < IPv4_address/Mask >

          # Spine interfaces (list), interface located on Spine,
          # corresponding to spines and uplink_to_spine_interfaces | Required.
          spine_interfaces: [ < ethernet_interface_1 >, < ethernet_interface_1 > ]

          # L3 Leaf BGP AS. | Required.
          # Inheritence: node > node_group > defaults
          bgp_as: < bgp_as >

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

### L2 Leafs Variables

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

      # Parent L3 switches (list), corresponding to uplink_interfaces and l3leaf_interfaces | Required.
      parent_l3leafs: [ DC1-LEAF2A, DC1-LEAF2B]

      # Uplink interfaces (list), interface located on L2 Leaf,
      # corresponding to parent_l3leafs and l3leaf_interfaces | Required.
      uplink_interfaces: [ < ethernet_interface_1 >, < ethernet_interface_2 > ]

      # Point-to-Point interface speed - will apply to L2 Leaf and L3 Leaf switches | Optional.
      p2p_link_interface_speed: < interface_speed | forced interface_speed | auto interface_speed >

      # Enable / Disable auto MLAG, when two nodes are defined in node group.
      mlag: < true | false -> default true >

      # Enable / Disable MLAG dual primary detectiom
      mlag_dual_primary_detection: < true | false -> default false >

      # MLAG interfaces (list) | Required when MLAG leafs present in topology.
      mlag_interfaces: [ < ethernet_interface_3 >, < ethernet_interface_4 > ]

      # Set origin of routes received from MLAG iBGP peer to incomplete. The purpose is to optimize routing for leaf
      # loopbacks from spine perspective and avoid suboptimal routing via peerlink for control plane traffic.
      mlag_ibgp_origin_incomplete: < true | false -> default true >

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

      # The node name must be the same name as inventory_hostname | Required
      # When two nodes are defined, this will automatically configure the nodes as an MLAG pair,
      # unless the "l2leaf.defaults.mlag:" key is set to false.
      nodes:

        # First node
        < l2_leaf_inventory_hostname_1 >:

          # Unique identifier | Required.
          id: < integer >

          # Node management IP address | Required.
          mgmt_ip: < IPv4_address/Mask >

          # l3leaf interfaces (list), interface located on l3leaf,
          # corresponding to parent_l3leafs and uplink_interfaces | Required.
          l3leaf_interfaces: [ < ethernet_interface_6 >, < ethernet_interface_6 > ]

    # node_group_2, will result in MLAG pair.
    < node_group_1 >:
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
```
