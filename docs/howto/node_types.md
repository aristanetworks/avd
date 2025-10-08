<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

## What is a Node Type?

A **Node Type** is a data model template that defines the behavior and configuration of a group of devices with a similar function. Instead of configuring every switch from scratch, you assign a `node_type` to it, and AVD applies a pre-defined set of design rules.

Think of node types as blueprints for your network. You have a blueprint for your switches (`spine`). Every switch built from the same blueprint will have the same fundamental design, ensuring consistency.

## Default node types

Here are the default node type keys organized by their primary design.

### Data Center/Campus L3LS (Leaf-Spine) Design

These are the most common node types for a standard datacenter fabric.

| Node Type Key | Primary Role / Function |
| --- | --- |
| `spine` | Core switch in a leaf-spine fabric, responsible for high-speed interconnects. |
| `l3spine` | A spine switch with additional L3 P2P links, often used for external connectivity. |
| `l2spine` | A spine switch used in a collapsed core or smaller fabric design. |
| `l3leaf` | A switch providing both L2 and L3 services, acting as the gateway for endpoints. |
| `l2leaf` | A switch providing only L2 services, extending VLANs to an L3 leaf for routing. |
| `overlay_controller` | A control-plane node, often a virtual switch, acting as an EVPN route server or reflector. |

### WAN (SD-WAN / AutoVPN) Design

These node types are used for building Wide Area Networks.

| Node Type Key | Primary Role / Function |
| --- | --- |
| `wan_rr` | **WAN Route Reflector**: A control-plane node that reflects BGP VPN routes between sites. |
| `wan_ce` | **WAN Customer Edge**: A router at a remote site or branch that connects to the WAN fabric. |

### MPLS Design

These node types are used for building MPLS core networks.

| Node Type Key | Primary Role / Function |
| --- | --- |
| `pe` | **Provider Edge**: A router at the edge of the MPLA core that connects to customer networks. |
| `p` | **Provider**: A core router within the MPLS network, responsible for high-speed label switching. |
| `rr` | **Route Reflector**: A control-plane node that reflects BGP routes between PE routers. |

Note: node_type are not tied to a design you can use any type within your network configuration

## How to Use Node Types

### Concepts

The keys required to use node types are defined in the following table.

| Key | Description |
| --- | --- |
| node type | A data model template that defines the behavior and configuration of a group of devices |
| defaults | Define default variables for all nodes of this type |
| nodes | Define variables for a specific device |
| nodes_groups | Define variables for all nodes of this type for a group of devices i.e. MLAG pair |

Using node types is a simple process, you assign the type and AVD handles the rest.

### Step 1: Assign a Node Type

The recommended approach is to assign the node type to an entire group of devices in your `group_vars` files. This simplifies scaling and management, especially in large networks.

`inventory/inventory.yml`

```yaml
all:
  children:
    SPINES:
      hosts:
        spine-1:
        spine-2:
    L3_LEAFS:
      hosts:
        leaf-1:
        leaf-2:
```

Now, create a group variables file for each group and define the type there.

`group_vars\SPINES.yml`

```yaml
spine:
  defaults:
    platform: vEOS-lab
    loopback_ipv4_pool: 10.255.0.0/27
    bgp_as: 65100
  nodes:
    - name: spine-1
      id: 1
      mgmt_ip: 172.16.1.11/24

    - name: spine-2
      id: 2
      mgmt_ip: 172.16.1.12/24
```

`group_vars\L3_LEAFS.yml`

```yaml
type: l3leaf
```

### Step 2: AVD Generates the Configuration

When you run your AVD playbook, AVD reads the `type` for each device and applies the corresponding configuration logic.

- **`spine-1` and `spine-2`** will be configured as high-speed IP cores, with BGP settings suitable for a spine.

- **`leaf-1` and `leaf-2`** will be configured with Layer 2 and Layer 3 features, including SVIs for VLANs, VXLAN for network virtualization, and MLAG for redundancy.

## Assigning Defaults to Node Types

Similarly, you can set default values for your spine switches. For example, you might want to set a default BGP password and adjust the MLAG reload delay for all spines.

**In `group_vars/SPINES.yml`:**

``` yaml
type: spine
  defaults:
    bgp_password: "SpineCorePassword"
    reload_delay:
      mlag: 900
      non_mlag: 1020
```

Now, every device you assign the `spine` type will inherit these specific settings, saving time and preventing misconfigurations.

## Create a Custom Node Type

You can also create entirely new node types for specialized roles, such as a "firewall service leaf" or a "border leaf".

Let's create a `border_leaf` type that uses a different loopback VTEP IP range and has a unique MLAG configuration.

### Step 1: Define the New Node Type Key

Create a new entry under `node_type_keys`.

```yaml
node_type_keys:
  - key: border_leaf # (1)!
    type: border_leaf
    defaults:
      vtep_loopback: #(2)!
        ipv4_pool: 10.10.20.0/24
      mlag_ibgp_peering_vlan_pool: 10.10.30.0/24 # (3)!
      evpn_gateway: #(4)!
        enabled: false
```

1. Definition for our new 'border_leaf' node type
2. Use a dedicated loopback pool for VTEP IPs
3. Use a different VLAN pool for MLAG iBGP peering
4. Disable EVPN gateway features by default for this node type

### Step 2: Assign the Custom Node Type in Your Inventory

Now, in your inventory files (e.g., `host_vars/border-leaf-1a.yml`), you can assign this new type to your devices.

```yaml
type: border_leaf #(1)!
```

1. Assign our custom node type

The device `border-leaf-1a` will now be configured using the settings you defined for `border_leaf`, while other devices can continue to use the standard `l3leaf` or `spine` types.
