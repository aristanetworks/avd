<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# IPv6 in AVD

## Introduction

AVD provides comprehensive IPv6 support for building modern dual-stack or IPv6-only network fabrics. This guide covers the different IPv6 deployment modes, configuration options, and best practices for implementing IPv6 in your Arista network using AVD.

This guide covers:

- IPv6 underlay with RFC 5549 (IPv6 link-local with IPv4 NLRI)
- Pure IPv6 numbered underlay
- IPv6 pool configuration for all fabric components
- MLAG IPv6 peering
- IPv6 prefix length customization

## IPv6 Deployment Modes

AVD supports two primary IPv6 underlay modes:

| Mode | Description | Use Case |
| ---- | ----------- | -------- |
| RFC 5549 | IPv6 link-local addresses with IPv4 route advertisements | Transition to IPv6, simplified addressing |
| IPv6 Numbered | Full IPv6 addressing for underlay and overlay | Pure IPv6 deployments |

### RFC 5549 Mode

RFC 5549 allows advertising IPv4 prefixes over IPv6 next-hops. This simplifies IP address management by using IPv6 link-local addresses for P2P links while maintaining IPv4 VTEP addresses.

```yaml title="RFC 5549 Configuration"
underlay_ipv6: true
underlay_rfc5549: true

spine:
  defaults:
    loopback_ipv4_pool: 10.255.0.0/27
    loopback_ipv6_pool: 2001:db8:1::/48

l3leaf:
  defaults:
    loopback_ipv4_pool: 10.255.0.0/27
    loopback_ipv4_offset: # offset >- uplink switches
    vtep_loopback_ipv4_pool: 10.255.1.0/27
    mlag_peer_ipv4_pool: 10.255.2.0/27
    mlag_peer_l3_ipv4_pool: 10.255.3.0/27
    loopback_ipv6_pool: 2001:db8:1::/48
    loopback_ipv6_offset: # offset >- uplink switches
```

### IPv6 Numbered Mode

Pure IPv6 numbered underlay configures explicit IPv6 addresses on all fabric links, loopbacks, and MLAG peerings.

```yaml hl_lines="28 29 32 33" title="IPv6 Numbered Configuration"
--8<--
ansible_collections/arista/avd/extensions/molecule/howto/inventory/group_vars/HTIPV6/fabric.yml
--8<--
```

!!! warning "Requirements"
    IPv6 numbered underlay requires:

    - `underlay_ipv6: true`
    - `underlay_ipv6_numbered: true`
    - `underlay_routing_protocol: ebgp`
    - `loopback_ipv6_pool` defined for each node type
    - `router_id_pool` for BGP Router ID (IPv4 format required)

## IPv6 Pool Types

AVD uses several IPv6 pools for different purposes:

| Pool Variable | Purpose | Default Interface |
| ------------- | ------- | ----------------- |
| `loopback_ipv6_pool` | Router loopback and BGP peering | Loopback0 |
| `vtep_loopback_ipv6_pool` | VXLAN tunnel endpoints | Loopback1 |
| `uplink_ipv6_pool` | P2P links between devices | Ethernet uplinks |
| `mlag_peer_ipv6_pool` | MLAG peer-link SVI | VLAN 4094 |
| `mlag_peer_l3_ipv6_pool` | MLAG L3 iBGP peering | VLAN 4093 |
| `router_id_pool` | BGP Router ID (IPv4) | None (ID only) |

!!! note "Router ID Pool"
    Even in pure IPv6 deployments, BGP requires an IPv4-formatted Router ID. The `router_id_pool` provides this without configuring any IPv4 addresses on interfaces.

## Loopback IPv6 Allocation

### Spine Configuration

Spines require `router_id_pool` for BGP Router ID and `loopback_ipv6_pool` for Loopback0:

```yaml hl_lines="8 10" title="Spine IPv6 Loopbacks"
--8<--
ansible_collections/arista/avd/extensions/molecule/howto/inventory/group_vars/HTIPV6_SPINES/spines.yml
--8<--
```

```cli title="htipv6-spine1 Loopback0"
--8<--
docs/howto/ipv6/artifacts/spine1-loopback.cfg
--8<--
```

```cli title="htipv6-spine2 Loopback0"
--8<--
docs/howto/ipv6/artifacts/spine2-loopback.cfg
--8<--
```

### Leaf Configuration

Leafs require additional pools for VTEP and MLAG:

```yaml hl_lines="8 10 11 13 15 20 22" title="Leaf IPv6 Pools"
--8<--
ansible_collections/arista/avd/extensions/molecule/howto/inventory/group_vars/HTIPV6_L3_LEAFS/leafs.yml
--8<--
```

```cli title="htipv6-leaf1 Loopbacks"
--8<--
docs/howto/ipv6/artifacts/leaf1-loopback.cfg
--8<--
```

## P2P Uplink IPv6 Allocation

P2P uplinks use `uplink_ipv6_pool` with the same allocation formula as IPv4:

```text
subnet_offset = ([node_id - 1] * max_uplink_switches * max_parallel_uplinks) + uplink_switch_index
```

```cli title="htipv6-leaf1 P2P Uplinks"
--8<--
docs/howto/ipv6/artifacts/leaf1-uplinks.cfg
--8<--
```

## MLAG IPv6 Configuration

For IPv6 MLAG peering, set `mlag_peer_address_family` to `ipv6` and configure the IPv6 pools:

```yaml title="MLAG IPv6 Settings"
l3leaf:
  defaults:
    mlag_peer_address_family: ipv6
    mlag_peer_ipv6_pool: 2001:db8:20::/48
    mlag_peer_l3_ipv6_pool: 2001:db8:21::/48
```

```cli title="htipv6-leaf1 MLAG VLANs"
--8<--
docs/howto/ipv6/artifacts/leaf1-mlag.cfg
--8<--
```

## BGP IPv6 Configuration

With IPv6 numbered underlay, BGP peer groups are configured for IPv6:

```cli title="htipv6-spine1 BGP Configuration"
--8<--
docs/howto/ipv6/artifacts/spine1-bgp.cfg
--8<--
```

!!! tip "Peer Group Naming"
    By default, BGP peer groups retain IPv4-style names. Customize them using `bgp_peer_groups`:

    ```yaml
    bgp_peer_groups:
      ipv4_underlay_peers:
        name: IPv6-UNDERLAY-PEERS
      mlag_ipv4_underlay_peer:
        name: MLAG-IPv6-UNDERLAY-PEER
    ```

## IPv6 Prefix Length Settings

Customize IPv6 prefix lengths for different link types:

```yaml title="IPv6 Prefix Length Configuration"
fabric_ip_addressing:
  loopback:
    ipv6_prefix_length: 128  # Default: 128, valid: 64 or 128
  mlag:
    ipv6_prefix_length: 64   # Default: 64, valid: 1-127
  p2p_uplinks:
    ipv6_prefix_length: 64   # Default: 64, valid: 1-127
```

| Setting | Default | Valid Values | Description |
| ------- | ------- | ------------ | ----------- |
| `loopback.ipv6_prefix_length` | 128 | 64, 128 | Loopback interface prefix length |
| `mlag.ipv6_prefix_length` | 64 | 1-127 | MLAG peer-link and L3 peering prefix length |
| `p2p_uplinks.ipv6_prefix_length` | 64 | 1-127 | P2P uplink prefix length |

## IPv6 Pool Formats

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

Override pool-calculated addresses with static values:

```yaml
l3leaf:
  nodes:
    - name: htipv6-leaf1
      id: 1
      loopback_ipv6_address: 2001:db8:100::1      # Override loopback pool
      vtep_loopback_ipv6_address: 2001:db8:101::1 # Override VTEP pool
```

## Unsupported Features with IPv6 Underlay

Some AVD features are not yet supported with IPv6 numbered underlay:

- `underlay_multicast_pim_sm`
- `underlay_multicast_rp_interfaces`
- `underlay_rfc5549` (mutually exclusive with numbered)
- `wan_role`
- `vtep_vvtep_ip`
- `inband_ztp`

## Best Practices

1. **Plan your IPv6 addressing scheme**: Use a consistent hierarchy (e.g., site/function/device)
2. **Use /128 for loopbacks**: Prevents routing table bloat
3. **Use /64 for P2P links**: Standard practice, though /127 is also valid
4. **Always define router_id_pool**: BGP requires IPv4 Router ID even in IPv6-only deployments
5. **Use meaningful pool prefixes**: Document your allocation scheme
6. **Consider dual-stack transition**: Start with RFC 5549 before moving to full IPv6

## Troubleshooting

### Common Issues

| Issue | Cause | Solution |
| ----- | ----- | -------- |
| BGP session not establishing | Missing `router_id_pool` | Define IPv4 pool for Router ID |
| No IPv6 addresses on interfaces | `underlay_ipv6` not enabled | Set `underlay_ipv6: true` |
| MLAG using IPv4 | `mlag_peer_address_family` not set | Set to `ipv6` |
| Validation error on routing protocol | Wrong underlay protocol | Use `underlay_routing_protocol: ebgp` |
| Missing VTEP IPv6 address | `vtep_loopback_ipv6_pool` not defined | Define pool for leaf nodes |

## Reference

- [Fabric Settings - IPv6 Underlay](../../../ansible_collections/arista/avd/roles/eos_designs/docs/tables/fabric-settings.md)
- [Node Type Loopback and VTEP Configuration](../../../ansible_collections/arista/avd/roles/eos_designs/docs/tables/node-type-loopback-vtep-configuration.md)
- [Node Type L2 and MLAG Configuration](../../../ansible_collections/arista/avd/roles/eos_designs/docs/tables/node-type-l2-mlag-configuration.md)
- [Fabric IP Addressing](../../../ansible_collections/arista/avd/roles/eos_designs/docs/tables/fabric-ip-addressing.md)
