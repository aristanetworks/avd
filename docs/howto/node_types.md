<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

## Introduction to Node Types

A **Node Type** is a data model template that defines the behavior and configuration of a group of devices with a similar function. Instead of configuring every switch from scratch, you assign a `node_type` to it, and AVD applies a pre-defined set of design rules.

The `eos_designs` role comes with built-in node types like `spine`, `l3leaf`, `l2leaf` and others. While these defaults cover most L3LS EVPN designs, AVD gives you the option to customize them or create your own.

## Default node types

Based on the Arista AVD `eos_designs` role and its various supported network topologies, here are the default node type keys organized by their primary design.

### Data Center/Campus L3LS (Leaf-Spine) Design

These are the most common node types for a standard datacenter fabric.

| Node Type Key | Primary Role / Function |
| --- | --- |
| `spine` | Core switch in a leaf-spine fabric, responsible for high-speed interconnects. |
| `l3spine` | A spine switch with additional L3 P2P links, often used for external connectivity. |
| `l2spine` | A spine switch used in a collapsed core or smaller fabric design. |
| `l3leaf` | Access switch providing both L2 and L3 services, acting as the gateway for endpoints. |
| `l2leaf` | Access switch providing only L2 services, extending VLANs to an L3 leaf for routing. |
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

## Customize an Existing Node Type

All node type customizations are defined under the `node_type_keys` variable. Each key in this list represents a node type you want to define or override.

The most common use case is to override the default settings for a standard node type, like `l3leaf`.

Let's say you want to change the default BGP password and enable `bfd` on all your L3 leafs.

### Step 1: Define the Node Type Key

In your group variables (e.g., `group_vars/FABRIC.yml`), you define the `node_type_keys` and specify which node type you are customizing.

```yaml
node_type_keys:
  - key: l3leaf # (1)!
    type: l3leaf
```

1. This entry targets all devices where the 'type' is set to 'l3leaf'

### Step 2: Set Default Values for the Node Type

Under the same key, you can now define `defaults`. Any setting here will be applied to all nodes of this type.

```yaml
node_type_keys:
  - key: l3leaf
    type: l3leaf
    defaults: # (1)!
      bgp_password: "MySecurePassword" # (2)!
      bfd: #(3)!
        multihop:
          interval: 300
          min_rx: 300
          multiplier: 3
      management_interface: Management1 # (4)!
```

1. Custom Settings for all l3leaf nodes
2. Set a default BGP password (using Ansible Vault is recommended)
3. Enable BFD on P2P uplinks
4. Set a default management interface

Any device in your inventory with `type: l3leaf` will now inherit these settings.

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

## Per-Node Overrides

Even with defaults set at the node type level, you can still override any setting on a specific device.

For example, if one of your `l3leaf` devices needs a different BGP password, you can set it directly in the host's variables.

`host_vars/special-leaf.yml`

```yaml
type: l3leaf

bgp_password: "A_Different_Password_For_This_Host_Only"
```

1. This value will override the default set under node_type_keys

This multi-layered approach---**global defaults -> node type defaults -> per-node specifics**---is what makes AVD so powerful for managing complex network configurations with minimal repetition.
