<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# IPv6 Addressing in AVD

## Introduction

AVD provides a powerful automatic IPv6 addressing system that assigns IPv6 addresses to fabric devices based on pools and node identifiers. This eliminates manual IPv6 planning and ensures consistent, predictable addressing across your network.

This guide covers IPv6 pool types, allocation mechanisms, and customization options available in AVD for pure IPv6 numbered underlay deployments.

!!! note "RFC 5549 Not Covered"
    This guide focuses on IPv6 numbered addressing. RFC 5549 (IPv6 link-local with IPv4 NLRI) uses a different approach and is not covered here.

## Key Concepts

Before diving into specifics, understand these core concepts:

**IPv6 Pool**: A range of IPv6 addresses from which AVD allocates individual addresses

**Node ID**: A unique numeric identifier for each device, used to calculate address offsets

**Offset**: A value added to the base pool address to derive a specific IPv6 address

**Prefix Length**: The subnet mask size for allocated addresses (e.g., /128, /64)

## Enabling IPv6 Addressing

To use IPv6 pools for underlay addressing, enable IPv6 numbered mode at the fabric level:

```yaml hl_lines="28 29" title="Enable IPv6 Addressing"
--8<--
ansible_collections/arista/avd/extensions/molecule/howto/inventory/group_vars/HTIPV6_NUMBERED/fabric.yml
--8<--
```

!!! warning "Requirements"
    IPv6 numbered underlay requires:

    - `underlay_ipv6: true` - Enables IPv6 on underlay interfaces
    - `underlay_ipv6_numbered: true` - Uses explicit IPv6 addresses (not link-local)
    - `underlay_routing_protocol: ebgp` - Default for spine/l3leaf node types (no explicit setting needed)
    - `loopback_ipv6_pool` defined for each node type
    - `router_id_pool` for BGP Router ID (IPv4 format required by BGP)

## IPv6 Pool Types

AVD uses several IPv6 pools for different purposes:

| Pool Variable | Purpose | Default Interface |
| ------------- | ------- | ----------------- |
| `loopback_ipv6_pool` | Router ID and BGP peering | Loopback0 |
| `vtep_loopback_ipv6_pool` | VXLAN tunnel endpoints | Loopback1 |
| `uplink_ipv6_pool` | P2P links between devices | Ethernet uplinks |
| `mlag_peer_ipv6_pool` | MLAG peer-link SVI | VLAN 4094 |
| `mlag_peer_l3_ipv6_pool` | MLAG L3 iBGP peering | VLAN 4093 |
| `router_id_pool` | BGP Router ID only (IPv4) | None (ID only) |

### Pool Hierarchy

Pools can be defined at multiple levels with the following precedence (highest to lowest):

1. **Node level** - Specific to a single device
2. **Node group level** - Shared by devices in a group (e.g., MLAG pair)
3. **Node type defaults** - Applied to all nodes of a type

!!! note "Router ID Pool"
    Even in pure IPv6 deployments, BGP requires an IPv4-formatted Router ID. The `router_id_pool` provides this without configuring any IPv4 addresses on interfaces.

## Loopback IPv6 Allocation

### Basic Formula

For Loopback0 (Router ID interface):

```text
IPv6 = pool_base + node_id + loopback_ipv6_offset
```

!!! note
    When spines and leafs share the same pool, use `loopback_ipv6_offset` to prevent address conflicts

### Spine Example

Spine assignment from pool `2001:db8:1::/48`:

- spine1 (id=1): `2001:db8:1::1/128` - calculation (pool + id[1])
- spine2 (id=2): `2001:db8:1::2/128` - calculation (pool + id[2])

```yaml hl_lines="8 10 14 17" title="Loopback0 for spines"
--8<--
ansible_collections/arista/avd/extensions/molecule/howto/inventory/group_vars/HTIPV6_NUMBERED_SPINES/spines.yml
--8<--
```

```cli title="spine1 configuration"
--8<--
docs/howto/ipv6_numbered/artifacts/spine1-loopback.cfg
--8<--
```

```cli title="spine2 configuration"
--8<--
docs/howto/ipv6_numbered/artifacts/spine2-loopback.cfg
--8<--
```

### Leaf Example

Leaf assignment from pool `2001:db8:1::/48` with offset of 2:

- leaf1 (id=1): `2001:db8:1::3/128` - calculation (pool + id[1] + offset[2])
- leaf2 (id=2): `2001:db8:1::4/128` - calculation (pool + id[2] + offset[2])

```yaml hl_lines="10 11 13" title="Loopback0 for leafs"
--8<--
ansible_collections/arista/avd/extensions/molecule/howto/inventory/group_vars/HTIPV6_NUMBERED_L3_LEAFS/leafs.yml
--8<--
```

```cli title="leaf1 loopback configuration"
--8<--
docs/howto/ipv6_numbered/artifacts/leaf1-loopback.cfg
--8<--
```

```cli title="leaf2 loopback configuration"
--8<--
docs/howto/ipv6_numbered/artifacts/leaf2-loopback.cfg
--8<--
```

!!! note "MLAG VTEP Sharing"
    MLAG pairs share the same VTEP IPv6 address. AVD automatically uses the **MLAG primary ID** in the group for both peers. This translates to `IPv6 = pool + mlag_primary_id + loopback_ipv6_offset`. Non-MLAG nodes use their own ID.

## P2P Uplink IPv6 Allocation

Uplink IPv6 addresses are calculated using a formula to ensure unique /64 subnets for each link.

### Formula

```text
subnet_offset = ([node_id - 1] * max_uplink_switches * max_parallel_uplinks) + uplink_switch_index
```

Where:

- `node_id`: The leaf's ID
- `max_uplink_switches`: Maximum number of uplink switches (default: length of `uplink_switches`)
- `max_parallel_uplinks`: Maximum parallel uplinks per switch (default: 1)
- `uplink_switch_index`: Index of the uplink switch (0-based)

### Example

```yaml hl_lines="15 16" title="P2P Uplink for leafs"
--8<--
ansible_collections/arista/avd/extensions/molecule/howto/inventory/group_vars/HTIPV6_NUMBERED_L3_LEAFS/leafs.yml
--8<--
```

Resulting allocations for leaf1 (id=1) from pool `2001:db8:10::/48`:

| Uplink | Subnet Offset | Leaf IPv6 | Spine IPv6 |
| ------ | ------------- | --------- | ---------- |
| To spine1 | 0 | 2001:db8:10::2/64 | 2001:db8:10::1/64 |
| To spine2 | 1 | 2001:db8:10:1::2/64 | 2001:db8:10:1::1/64 |

```cli title="leaf1 P2P to spines"
--8<--
docs/howto/ipv6_numbered/artifacts/leaf1-uplinks.cfg
--8<--
```

## MLAG IPv6 Allocation

MLAG requires two pools for peer connectivity:

| Pool | Purpose | Default VLAN |
| ---- | ------- | ------------ |
| `mlag_peer_ipv6_pool` | L2 peer-link SVI | 4094 |
| `mlag_peer_l3_ipv6_pool` | L3 iBGP peering | 4093 |

### Enabling MLAG IPv6

To use IPv6 for MLAG peering, set `mlag_peer_address_family` to `ipv6`:

```yaml hl_lines="18 20 22" title="MLAG IPv6 Settings"
--8<--
ansible_collections/arista/avd/extensions/molecule/howto/inventory/group_vars/HTIPV6_NUMBERED_L3_LEAFS/leafs.yml
--8<--
```

### MLAG Allocation Algorithms

AVD supports three MLAG IPv6 allocation algorithms configured via `fabric_ip_addressing.mlag.algorithm`:

=== "first_id (default)"

    Uses the first node's ID in the MLAG group:

    ```yaml
    fabric_ip_addressing:
      mlag:
        algorithm: first_id  # Default
    ```

    Formula: `offset = (mlag_primary_id - 1)`

=== "odd_id"

    Requires one node with an odd ID and one with an even ID:

    ```yaml
    fabric_ip_addressing:
      mlag:
        algorithm: odd_id
    ```

    Formula: `offset = (odd_id - 1)`

=== "same_subnet"

    All MLAG pairs share the same subnet (first in pool):

    ```yaml
    fabric_ip_addressing:
      mlag:
        algorithm: same_subnet
    ```

    Formula: `offset = 0` (always)

```cli title="leaf1 MLAG VLANs"
--8<--
docs/howto/ipv6_numbered/artifacts/leaf1-mlag.cfg
--8<--
```

## Global IPv6 Addressing Settings

Configure fabric-wide IPv6 addressing behavior:

```yaml title="IPv6 Addressing Settings"
fabric_ip_addressing:
  mlag:
    algorithm: first_id  # first_id, odd_id, same_subnet
    ipv6_prefix_length: 64
  p2p_uplinks:
    ipv6_prefix_length: 64
  loopback:
    ipv6_prefix_length: 128
```

| Setting | Default | Valid Values | Description |
| ------- | ------- | ------------ | ----------- |
| `loopback.ipv6_prefix_length` | 128 | 64, 128 | Loopback interface prefix length |
| `mlag.ipv6_prefix_length` | 64 | 1-127 | MLAG peer-link and L3 peering prefix length |
| `p2p_uplinks.ipv6_prefix_length` | 64 | 1-127 | P2P uplink prefix length |

## Pool Formats

AVD supports flexible IPv6 pool formats:

### Single Prefix

```yaml
loopback_ipv6_pool: 2001:db8:1::/48
```

### Multiple Prefixes

Comma-separated list of prefixes:

```yaml
loopback_ipv6_pool: 2001:db8:1::/56, 2001:db8:2::/56
```

### IPv6 Ranges

```yaml
loopback_ipv6_pool: 2001:db8::1-2001:db8::ff
```

## Static IPv6 Overrides

Override VTEP loopback with a static value:

```yaml
l3leaf:
  nodes:
    - name: htipv6-numbered-leaf1
      id: 1
      vtep_loopback_ipv6_address: 2001:db8:101::1 # Override VTEP pool
```

| Override Variable | Overrides Pool |
| ----------------- | -------------- |
| `vtep_loopback_ipv6_address` | `vtep_loopback_ipv6_pool` |

!!! note
    There is no `loopback_ipv6_address` override for Loopback0. Use `loopback_ipv6_pool` with `loopback_ipv6_offset` to control IPv6 address allocation.

## Unsupported Features

Some AVD features are not yet supported with IPv6 numbered underlay:

- `underlay_multicast_pim_sm`
- `underlay_multicast_rp_interfaces`
- `underlay_rfc5549` (mutually exclusive with numbered)
- `wan_role`
- `vtep_vvtep_ip`
- `inband_ztp`

## Best Practices

1. **Plan your ID scheme**: Use consistent ID numbering across the fabric
2. **Use offsets wisely**: When sharing pools between node types, use `loopback_ipv6_offset`
3. **Size pools appropriately**: Ensure pools have enough addresses for growth
4. **Use /128 for loopbacks**: Prevents routing table bloat
5. **Use /64 for P2P links**: Standard practice, though /127 is also valid per RFC 6164
6. **Always define router_id_pool**: BGP requires IPv4 Router ID even in IPv6-only deployments
7. **Use node groups for MLAG**: Define MLAG pairs as node groups for automatic VTEP sharing

## Troubleshooting

### Common Issues

| Issue | Cause | Solution |
| ----- | ----- | -------- |
| BGP session not establishing | Missing `router_id_pool` | Define IPv4 pool for Router ID |
| No IPv6 addresses on interfaces | `underlay_ipv6` not enabled | Set `underlay_ipv6: true` |
| MLAG using IPv4 | `mlag_peer_address_family` not set | Set to `ipv6` |
| Validation error on routing protocol | Wrong underlay protocol | Ensure `underlay_routing_protocol` is `ebgp` (default for spine/l3leaf) |
| Missing VTEP IPv6 address | `vtep_loopback_ipv6_pool` not defined | Define pool for leaf nodes |
| IPv6 address conflict between spine and leaf | Shared pool without offset | Add `loopback_ipv6_offset` to leaf defaults |
| Pool exhausted | Too many nodes for pool size | Use larger pool or multiple prefixes |

## Reference

- [Node Type VTEP and Loopback Configuration](../../../ansible_collections/arista/avd/roles/eos_designs/docs/data-models.md#node-type-loopback-and-vtep-configuration)
- [Fabric IP Addressing](../../../ansible_collections/arista/avd/roles/eos_designs/docs/data-models.md#fabric-ip-addressing)
- [MLAG Configuration](../../../ansible_collections/arista/avd/roles/eos_designs/docs/data-models.md#node-type-l2-and-mlag-configuration)
