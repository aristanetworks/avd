<!--
  ~ Copyright (c) 2025-2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# Fabric Topology

## Introduction

**Fabric Topology** defines how devices are physically and logically connected in your network. AVD uses a hierarchical data model to describe the relationships between spines, leafs, and other network devices. This guide explains how to define your fabric topology, configure uplinks, and leverage automatic interface allocation.

### Key Concepts

- **Node Types**: Define the role of each device (spine, l3leaf, l2leaf, etc.)
- **Uplinks**: Connections from leafs to spines or from L2 leafs to L3 leafs
- **MLAG**: Multi-Chassis Link Aggregation for leaf redundancy
- **Default Interfaces**: Automatic interface assignment based on node type and platform

## Topology Building Blocks

### Inventory Structure

The inventory below is an example of an Ansible inventory used to define a fabric hierarchy. Devices are organized into groups that map to their roles:

```yaml title="inventory.yml"
---
all:
  children:
    FABRIC:
      children:
        HTFT:
          children:
            HTFT_SPINES:
              hosts:
                htft-spine1:
                  ansible_host: 172.16.2.11
                htft-spine2:
                  ansible_host: 172.16.2.12
            HTFT_LEAFS:
              hosts:
                topo-leaf1a:
                  ansible_host: 172.16.2.101
                topo-leaf1b:
                  ansible_host: 172.16.2.102
```

### Fabric-Wide Settings

Define global settings that apply to all devices in the fabric:

```yaml title="fabric.yml"
--8<--
ansible_collections/arista/avd/extensions/molecule/howto/inventory/group_vars/HTFT/fabric.yml
--8<--
```

1. `fabric_name` must be defined and match group name covering all devices in scope of the fabric.
2. Underlay routing protocol - eBGP is common for EVPN/VXLAN fabrics
3. Overlay routing protocol for EVPN peering

### Default Interfaces

Automatically assign interfaces based on node type and platform, eliminating repetitive per-node definitions:

```yaml title="default_interfaces.yml"
--8<--
ansible_collections/arista/avd/extensions/molecule/howto/inventory/group_vars/HTFT/default_interfaces.yml
--8<--
```

1. Define interface mappings per node type and platform
2. Spine downlink interfaces connect to leafs
3. You can define different default interfaces for different platforms
4. Leaf uplink interfaces connect to spines
5. MLAG peer-link interfaces for leaf redundancy

### Spine Configuration

Spines are the core of the fabric, providing connectivity between all leafs:

```yaml title="spines.yml"
--8<--
ansible_collections/arista/avd/extensions/molecule/howto/inventory/group_vars/HTFT_SPINES/spines.yml
--8<--
```

1. Platform determines default settings and validation rules
2. IP pool for Loopback0 interfaces (used for BGP router-id and EVPN peering)
3. BGP AS number for the spine layer
4. List of spine nodes
5. Unique identifier for IP address allocation
6. Management IP address

### L3 Leaf Configuration

L3 leafs provide network services (VLANs, VRFs, SVIs) and connect to endpoints:

```yaml title="l3_leas.yml"
--8<--
ansible_collections/arista/avd/extensions/molecule/howto/inventory/group_vars/HTFT_LEAFS/l3_leafs.yml
--8<--
```

1. Loopback IP pool (shared with spines in this example)
2. Offset to avoid IP conflicts with spines
3. VTEP loopback pool for VXLAN tunnel endpoints
4. List of uplink switches (spines)
5. IP pool for point-to-point uplinks to spines
6. IP pool for MLAG peer-link (VLAN 4094)
7. IP pool for MLAG iBGP peering (VLAN 4093)
8. Virtual MAC for anycast gateway on SVIs
9. Node groups allow shared configuration and automatic MLAG pairing
10. Group name for documentation and identification
11. BGP AS for this leaf pair (unique per MLAG pair in eBGP designs)
12. Spine interfaces this leaf connects to

## MLAG Pairing

When exactly two nodes are in the same `node_group`, AVD automatically configures them as an MLAG pair:

- Allocates MLAG peer-link interfaces from `mlag_interfaces` or `default_interfaces`
- Configures VLAN 4094 for MLAG control plane
- Configures VLAN 4093 for iBGP peering between MLAG peers
- Assigns matching virtual MAC addresses for anycast gateway

## Generated Configuration

AVD generates complete device configurations based on your topology definitions.

### Spine Configuration

=== "Links to Leafs"

    ```cli
    --8<--
    docs/howto/fabric_topology/artifacts/htft-spine1-links.cfg
    --8<--
    ```

=== "Full Configuration"

    ```cli
    --8<--
    ansible_collections/arista/avd/extensions/molecule/howto/inventory/intended/configs/htft-spine1.cfg
    --8<--
    ```

### L3 Leaf Configuration

=== "Uplinks and MLAG"

    ```cli
    --8<--
    docs/howto/fabric_topology/artifacts/htft-leaf1a-links.cfg
    --8<--
    ```

=== "Full Configuration"

    ```cli
    --8<--
    ansible_collections/arista/avd/extensions/molecule/howto/inventory/intended/configs/htft-leaf1a.cfg
    --8<--
    ```

## Default Interfaces

The `default_interfaces` feature automatically assigns interfaces based on node type and platform, eliminating repetitive configuration:

| Node Type | Uplink Interfaces | MLAG Interfaces | Downlink Interfaces |
| --------- | ----------------- | --------------- | ------------------- |
| spine     | -                 | -               | Ethernet1-8         |
| l3leaf    | Ethernet1-2       | Ethernet3-4     | Ethernet8           |
| l2leaf    | Ethernet1-2       | -               | -                   |

### Interface Range Syntax

AVD supports flexible interface range notation:

- `Ethernet1-4` expands to Ethernet1, Ethernet2, Ethernet3, Ethernet4
- `Ethernet49-52/1` expands to Ethernet49/1, Ethernet50/1, Ethernet51/1, Ethernet52/1
- `[Ethernet1, Ethernet2]` explicit list of interfaces

## Uplink Configuration

### Understanding Uplinks

Uplinks connect lower-tier (L3 Leafs) devices to higher-tier devices (Spines):

- **L3 Leafs** uplink to **Spines** using routed point-to-point links
- **L2 Leafs** uplink to **L3 Leafs** using port-channels

### Key Uplink Variables

| Variable                   | Description                                                |
| -------------------------- | ---------------------------------------------------------- |
| `uplink_switches`          | List of switches this node connects to                     |
| `uplink_switch_interfaces` | Interfaces on the uplink switches                          |
| `uplink_interfaces`        | Local interfaces for uplinks (or use `default_interfaces`) |
| `uplink_ipv4_pool`         | IP pool for point-to-point uplinks                         |

### Uplink IP Allocation

AVD automatically allocates IPs from `uplink_ipv4_pool` using a deterministic algorithm based on node `id`:

```text
Spine interface: uplink_ipv4_pool + (node_id * 2 * uplink_count) + (uplink_index * 2)
Leaf interface:  uplink_ipv4_pool + (node_id * 2 * uplink_count) + (uplink_index * 2) + 1
```

## Best Practices

1. **Consistent naming conventions**: Use predictable hostname patterns that work with `default_node_types`.
2. **Leverage node_groups**: Group related nodes together to share configuration and enable automatic MLAG pairing.
3. **Plan your IP pools**: Ensure IP pools are large enough for your fabric size with room for growth.
4. **Use loopback offsets**: When sharing a loopback pool between node types, use `loopback_ipv4_offset` to prevent IP conflicts.
5. **Use `default_interfaces`**: Define interface mappings once at the fabric level instead of on every node.

## Troubleshooting

### BGP Peering Not Establishing

**Issue**: Underlay or overlay BGP sessions not coming up.

**Solution**:

- Verify `uplink_switches` and `uplink_switch_interfaces` are correctly defined
- Check that the spine's `downlink_interfaces` in `default_interfaces` includes the interfaces used by leafs
- Ensure `uplink_ipv4_pool` has sufficient addresses

### MLAG Not Forming

**Issue**: MLAG peer-link not establishing between leaf pairs.

**Solution**:

- Verify exactly two nodes are in the same `node_group`
- Check that `mlag_interfaces` are defined (directly or via `default_interfaces`)
- Ensure `mlag_peer_ipv4_pool` is defined for the leaf defaults

### IP Address Conflicts

**Issue**: Multiple devices assigned the same IP address.

**Solution**:

- Ensure each node has a unique `id` within its node type
- When sharing loopback pools between node types, use appropriate `loopback_ipv4_offset`
- Verify IP pools are large enough for all nodes

## Reference

For complete details on all available topology properties, see:

- [Node Type Settings](../../../ansible_collections/arista/avd/roles/eos_designs/docs/data-models.md#node-type-settings)
- [Default Interface Settings](../../../ansible_collections/arista/avd/roles/eos_designs/docs/data-models.md#default-interface-settings)
