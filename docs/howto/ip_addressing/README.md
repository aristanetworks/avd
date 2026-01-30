<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# IP Addressing in AVD

## Introduction

AVD provides a powerful automatic IP addressing system that assigns IP addresses to fabric devices based on pools and node identifiers. This eliminates manual IP planning and ensures consistent, predictable addressing across your network.

This guide covers all IP pool types, allocation mechanisms, and customization options available in AVD.

## Key Concepts

Before diving into specifics, understand these core concepts:

**IP Pool**: A range of IP addresses from which AVD allocates individual addresses

**Node ID**: A unique numeric identifier for each device, used to calculate IP offsets

**Offset**: A value added to the base pool address to derive a specific IP

**Prefix Length**: The subnet mask size for allocated addresses (e.g., /32, /31)

## IP Pool Types

AVD uses several IP pools for different purposes:

| Pool Variable | Purpose | Default Interface |
| ------------- | ------- | ----------------- |
| `loopback_ipv4_pool` | Router ID and BGP peering | Loopback0 |
| `vtep_loopback_ipv4_pool` | VXLAN tunnel endpoints | Loopback1 |
| `uplink_ipv4_pool` | P2P links between devices | Ethernet uplinks |
| `mlag_peer_ipv4_pool` | MLAG peer-link SVI | VLAN 4094 |
| `mlag_peer_l3_ipv4_pool` | MLAG L3 iBGP peering | VLAN 4093 |
| `router_id_pool` | BGP Router ID only (IPv6 underlay) | None (ID only) |

### Pool Hierarchy

Pools can be defined at multiple levels with the following precedence (highest to lowest):

1. **Node type defaults** - Applied to all nodes of a type
2. **Node group level** - Shared by devices in a group (e.g., MLAG pair)
3. **Node level** - Specific to a single device

```yaml hl_lines="5 19 25" title="Pool Hierarchy Example"
--8<--
ansible_collections/arista/avd/extensions/molecule/howto/inventory/group_vars/HTIPA_L3_LEAFS/leafs.yml
--8<--
```

## Loopback IP Allocation

### Basic Formula

For Loopback0 (Router ID):

```text
IP = pool_base + node_id + loopback_ipv4_offset
```

!!! note
    When spines and leafs share the same pool, use `loopback_ipv4_offset` to prevent IP conflicts

### Example

In the example below, spine1 will be assigned 10.255.0.1/32 (10.255.0.0 + id(1)) and spine2 will get 10.255.0.2/32 (10.255.0.0 + id(2)).

```yaml hl_lines="5 9 12" title="Loopback0 for spines"
--8<--
ansible_collections/arista/avd/extensions/molecule/howto/inventory/group_vars/HTIPA_SPINES/spines.yml
--8<--
```

In the example below, leaf1 will get 10.255.2.3/32 (node specific pool + id(1) + offset(2)) and leaf2 will get 10.255.1.4/32 (group specific pool + id(2) + offset(2)).

```yaml hl_lines="5 6 19 22 25 27" title="Loopback0 for leafs"
--8<--
ansible_collections/arista/avd/extensions/molecule/howto/inventory/group_vars/HTIPA_L3_LEAFS/leafs.yml
--8<--
```

## VTEP Loopback Allocation

VTEP loopbacks (Loopback1) use `vtep_loopback_ipv4_pool`:

```yaml hl_lines="7" title="VTEP Loopback for leafs"
--8<--
ansible_collections/arista/avd/extensions/molecule/howto/inventory/group_vars/HTIPA_L3_LEAFS/leafs.yml
--8<--
```

!!! note "MLAG VTEP Sharing"
    MLAG pairs share the same VTEP IP. AVD automatically uses the **MLAG primary ID** in the group for both peers. This translates to `IP = pool + mlag_primary_id + loopback_ipv4_offset`. Non-MLAG nodes use their own ID.

## P2P Uplink Allocation

Uplink IP addresses are calculated using a more complex formula to ensure unique /31 subnets for each link.

### Formula

```text
subnet_offset = ((node_id - 1) * max_uplink_switches * max_parallel_uplinks) + uplink_switch_index
```

Where:

- `node_id`: The leaf's ID
- `max_uplink_switches`: Maximum number of uplink switches (default: 4)
- `max_parallel_uplinks`: Maximum parallel uplinks per switch (default: 1)
- `uplink_switch_index`: Index of the uplink switch (0-based)

### Example

```yaml hl_lines="8 9 22 24" title="P2P Uplink for leafs"
--8<--
ansible_collections/arista/avd/extensions/molecule/howto/inventory/group_vars/HTPIA_L3_LEAFS/leafs.yml
--8<--
```

Resulting allocations for leaf1 (id=1):

| Uplink | Subnet Offset | Leaf IP | Spine IP |
| ------ | ------------- | ------- | -------- |
| To spine1 | 0 | 10.255.255.1/31 | 10.255.255.0/31 |
| To spine2 | 1 | 10.255.255.3/31 | 10.255.255.2/31 |

```cfg title="leaf1 P2P to spines"
--8<--
docs/howto/ip_addressing/artifacts/leaf1-to-spines.cfg
--8<--
```

## MLAG IP Allocation

MLAG requires two pools for peer connectivity:

| Pool | Purpose | Default VLAN |
| ---- | ------- | ------------ |
| `mlag_peer_ipv4_pool` | L2 peer-link SVI | 4094 |
| `mlag_peer_l3_ipv4_pool` | L3 iBGP peering | 4093 |

### MLAG Allocation Algorithms

AVD supports three MLAG IP allocation algorithms configured via `fabric_ip_addressing.mlag.algorithm`:

=== "first_id (default)"

    Uses the first node's ID in the MLAG group:

    ```yaml
    fabric_ip_addressing:
      mlag:
        algorithm: first_id  # Default

    l3leaf:
      defaults:
        mlag_peer_ipv4_pool: 10.255.3.64/27
      node_groups:
        - group: HOW_TO_L3_LEAFS
          nodes:
            - name: htipa-leaf1
              id: 1  # Primary: 10.255.3.64/31
            - name: htipa-leaf2
              id: 2  # Secondary: 10.255.3.65/31
    ```

    Formula: `offset = (mlag_primary_id - 1)`

=== "odd_id"

    Requires one node with an odd ID and one with an even ID:

    ```yaml
    fabric_ip_addressing:
      mlag:
        algorithm: odd_id

    l3leaf:
      node_groups:
        - group: HOW_TO_L3_LEAFS
          nodes:
            - name: htipa-leaf1
              id: 1  # Odd - determines subnet
            - name: htipa-leaf2
              id: 2  # Even - must pair with odd
    ```

    Formula: `offset = (odd_id - 1)`

=== "same_subnet"

    All MLAG pairs share the same subnet (first in pool):

    ```yaml
    fabric_ip_addressing:
      mlag:
        algorithm: same_subnet

    # All MLAG pairs get 10.255.3.64/31
    ```

    Formula: `offset = 0` (always)

## Node ID Assignment

Node IDs are critical for IP allocation. AVD supports two assignment methods:

### Static Assignment (Default)

Manually assign IDs to each node:

```yaml
spine:
  nodes:
    - name: htipa-spine1
      id: 1
    - name: htipa-spine2
      id: 2
```

### Dynamic Assignment (Pool Manager)

Automatically assign IDs based on fabric topology:

```yaml
fabric_numbering:
  node_id:
    algorithm: pool_manager
    pools_file: intended/data/fabric-ids.yml
```

IDs are assigned based on: `fabric_name`, `dc_name`, `pod_name`, and `type`.

## Pool Formats

AVD supports flexible pool formats:

### Single Subnet

```yaml
loopback_ipv4_pool: 10.255.0.0/24
```

### Multiple Subnets

Comma-separated list of subnets:

```yaml
loopback_ipv4_pool: 10.255.0.0/25, 10.255.1.0/25
```

### IP Ranges

```yaml
loopback_ipv4_pool: 10.255.0.1-10.255.0.50
```

## Static IP Overrides

Override any pool-calculated address with a static value:

```yaml
l3leaf:
  nodes:
    - name: htipa-leaf1
      id: 1
      loopback_ipv4_address: 10.100.100.1  # Override loopback pool
      vtep_loopback_ipv4_address: 10.100.101.1  # Override VTEP pool
```

Available override variables:

| Override Variable | Overrides Pool |
| ----------------- | -------------- |
| `loopback_ipv4_address` | `loopback_ipv4_pool` |
| `vtep_loopback_ipv4_address` | `vtep_loopback_ipv4_pool` |
| `uplink_ipv4_address` | `uplink_ipv4_pool` |

## Global IP Addressing Settings

Configure fabric-wide IP addressing behavior:

```yaml
fabric_ip_addressing:
  mlag:
    algorithm: first_id  # first_id, odd_id, same_subnet
    ipv4_prefix_length: 31
  p2p_uplinks:
    ipv4_prefix_length: 31
```

## Custom IP Addressing

For complex requirements, create a custom Python module:

```yaml
# In your inventory
node_type_keys:
  - key: l3leaf
    ip_addressing:
      router_id: custom_ip_addressing/router_id.j2
      mlag_ip_primary: custom_ip_addressing/mlag_primary.j2
```

!!! note
    For a list of available variables in custom IP addressing templates, refer to the [documentation](../../../ansible_collections/arista/avd/roles/eos_designs/docs/data-models.md#context-for-ip_addressing-templates).

## Best Practices

1. **Plan your ID scheme**: Use consistent ID numbering across the fabric
2. **Use offsets wisely**: When sharing pools between node types, use `loopback_ipv4_offset`
3. **Size pools appropriately**: Ensure pools have enough addresses for growth
4. **Document your allocation scheme**: Keep records of pool assignments
5. **Use node groups for MLAG**: Define MLAG pairs as node groups for automatic VTEP sharing
6. **Consider the algorithm**: Choose the MLAG algorithm that fits your operational model

## Troubleshooting

### Common Issues

| Issue | Cause | Solution |
| ----- | ----- | -------- |
| IP conflict between spine and leaf | Shared pool without offset | Add `loopback_ipv4_offset` to leaf defaults |
| Missing MLAG peer IP | `mlag_peer_ipv4_pool` not defined | Define pool at node_group or defaults level |
| Unexpected VTEP IP | MLAG pair not in same node_group | Move MLAG peers to same node_group |
| Pool exhausted | Too many nodes for pool size | Use larger pool or multiple subnets |
| Loopback IP not updating | Static IP override in use or more specific pools | Remove override or check pool definitions |

## Reference

- [Node Type VTEP and Loopback Configuration](../../../ansible_collections/arista/avd/roles/eos_designs/docs/data-models.md#node-type-loopback-and-vtep-configuration)
- [Fabric IP Addressing](../../../ansible_collections/arista/avd/roles/eos_designs/docs/data-models.md#fabric-ip-addressing)
- [MLAG Configuration](../../../ansible_collections/arista/avd/roles/eos_designs/docs/data-models.md#node-type-l2-and-mlag-configuration)
- [Custom IP Addressing](../../../ansible_collections/arista/avd/roles/eos_designs/docs/data-models.md#context-for-ip_addressing-templatesl)
