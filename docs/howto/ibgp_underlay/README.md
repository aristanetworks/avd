<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# iBGP Underlay with Automatic Route Reflection

## Introduction

With `underlay_routing_protocol: ibgp`, every fabric node uses the same BGP AS, and AVD builds the route reflection automatically from the uplinks it already knows:

- A node is a route reflector (RR) for its downlink switches.
- This works at any depth, for example leaf, spine, super-spine.
- Every session uses `next-hop-self`, so routes are reachable from every tier.

!!! note "Supported designs"
    For now, `ibgp` only supports RFC 5549 (IPv4 over IPv6 link-local) underlays with no overlay, as commonly used in AI frontend and backend fabrics.
    Support for overlays can be added later as required.
    See [Restrictions](#restrictions) for the full list.

## Enabling the iBGP underlay

```yaml title="Fabric settings"
underlay_routing_protocol: ibgp
underlay_rfc5549: true
overlay_routing_protocol: none

# Same AS on all nodes. Either set it globally or with the same value on every node type.
bgp_as: "65000"

bgp_peer_groups:
  # Sessions towards uplink switches (the route reflectors).
  rr_underlay_peers:
    name: RR-UNDERLAY-PEERS  # Default
  # Sessions towards downlink switches (the route reflector clients).
  rr_clients_underlay_peers:
    name: RR-CLIENTS-UNDERLAY-PEERS  # Default
```

`ibgp` is also valid for `node_type_keys[].default_underlay_routing_protocol`.

Both peer groups support the same keys as `ipv4_underlay_peers`: `name`, `password`, `cleartext_password`, `bfd`, `maximum_routes` and `structured_config`.
`bgp_peer_groups.ipv4_underlay_peers` is not used with `ibgp`, and AVD raises an error if it is set.

Every session uses `rr_underlay_peers` on the client and `rr_clients_underlay_peers` on the route reflector, so both groups must have the same password and the same `bfd` value.
AVD compares the cleartext passwords. A type 7 `password` must be encrypted with the name of its own peer group, since EOS decrypts it with that name.
The same password therefore renders different type 7 strings on the two groups.

!!! info "Why two peer groups"
    RFC 5549 `neighbor interface` statements only accept a peer group, a remote AS, a peer filter and a description.
    The route reflector attributes must therefore live on peer groups, and a spine needs one per direction.

## What AVD renders

### Sessions and peer groups

- Uplinks use `rr_underlay_peers`, downlinks use `rr_clients_underlay_peers`.
- Both groups render `next-hop-self`, `send-community`, `maximum-routes`, IPv4 activation and `next-hop address-family ipv6 originate`, plus the optional password, BFD and `structured_config`.
- `rr_clients_underlay_peers` also renders `route-reflector-client`.
- Each group only renders when at least one session uses it.
- `redistribute connected` is unchanged from eBGP, and `l3_edge` or `core_interfaces` links with `include_in_underlay_protocol: false` are advertised through it.
- Interface-level uplink features (MTU, PTP, MACsec, sFlow, flow tracking, QoS) are unchanged.

### Cluster ID

The route reflectors that serve the same clients form an RR group, and share one cluster ID:

- `bgp_cluster_id` is required on every route reflector, which is any node with downlink switches.
- It must be the same on all the route reflectors of the group, and unique across RR groups.

Leaves have no downlink switches, so they render no cluster ID and must not set `bgp_cluster_id`.

```yaml title="Cluster IDs in a three-tier fabric"
super_spine:
  defaults:
    bgp_cluster_id: 1.1.1.1

spine:
  node_groups:
    - group: POD1_SPINES
      bgp_cluster_id: 2.2.2.2
    - group: POD2_SPINES
      bgp_cluster_id: 3.3.3.3
```

AVD checks the RR groups and their cluster IDs once for the whole fabric while generating facts, so these errors stop the build of the whole fabric.

### Example

Spine of POD2 in a three-tier fabric, with leaves below and super-spines above, using the cluster IDs above.

```eos
router bgp 65000
   router-id 10.254.2.10
   bgp cluster-id 3.3.3.3
   maximum-paths 128 ecmp 128
   neighbor RR-CLIENTS-UNDERLAY-PEERS peer group
   neighbor RR-CLIENTS-UNDERLAY-PEERS next-hop-self
   neighbor RR-CLIENTS-UNDERLAY-PEERS route-reflector-client
   neighbor RR-CLIENTS-UNDERLAY-PEERS send-community
   neighbor RR-CLIENTS-UNDERLAY-PEERS maximum-routes 256000
   neighbor RR-UNDERLAY-PEERS peer group
   neighbor RR-UNDERLAY-PEERS next-hop-self
   neighbor RR-UNDERLAY-PEERS send-community
   neighbor RR-UNDERLAY-PEERS maximum-routes 256000
   redistribute connected
   neighbor interface Ethernet1 peer-group RR-CLIENTS-UNDERLAY-PEERS remote-as 65000
   neighbor interface Ethernet2 peer-group RR-CLIENTS-UNDERLAY-PEERS remote-as 65000
   neighbor interface Ethernet7 peer-group RR-UNDERLAY-PEERS remote-as 65000
   neighbor interface Ethernet8 peer-group RR-UNDERLAY-PEERS remote-as 65000
   !
   address-family ipv4
      neighbor RR-CLIENTS-UNDERLAY-PEERS activate
      neighbor RR-CLIENTS-UNDERLAY-PEERS next-hop address-family ipv6 originate
      neighbor RR-UNDERLAY-PEERS activate
      neighbor RR-UNDERLAY-PEERS next-hop address-family ipv6 originate
```

A leaf only renders `RR-UNDERLAY-PEERS` and its uplink neighbor interfaces. A top-tier super-spine only renders `RR-CLIENTS-UNDERLAY-PEERS`.

## Topology rules

- One BGP AS for the whole fabric.
- Any number of tiers.
- Full mesh between adjacent tiers. All clients of a route reflector must have the same uplink switches, and all those uplink switches must have the same downlink switches.
  Partial meshes and links that skip a tier raise an error, since a shared cluster ID would then drop valid routes.

## Why route reflectors share a cluster ID

Using a distinct cluster ID per route reflector, like the router ID default used for overlay route reflectors, causes hairpin ECMP paths.
For example, with two spines per POD below two super-spines:

1. A leaf advertises its loopback to both spines of its POD.
2. Each super-spine learns the route from both spines, and reflects its best path to the other spines, including the spine that has the leaf directly connected.
3. That spine sees a cluster list that does not contain its own cluster ID, so it accepts the reflected routes.
4. The spine installs three ECMP paths to its own directly connected leaf: the direct one, and two through the super-spines.

When both spines of the POD share one cluster ID, the spine drops the routes reflected through the other POD spine, so only the direct path to the leaf loopback remains.
On a leaf-to-spine link failure, the spine then has no path to the leaf and withdraws it, which matches eBGP behavior.

This only applies to prefixes learned from clients. A route reflector does not add its own cluster ID to the prefixes it originates, like its loopback.
For example, spine 2 advertises its loopback to the super-spines without a cluster list. A super-spine reflects it to spine 1 with the super-spine cluster ID only, so spine 1 accepts it and reflects it to its leaves.
A leaf of the POD then has ECMP paths to the spine 2 loopback, directly and through spine 1, a super-spine and spine 2 (cluster list `2.2.2.2 1.1.1.1` with the IDs above).
The impact is limited to the prefixes originated by route reflectors, which are the spine and super-spine loopbacks.

!!! warning "Never enable `bgp route-reflector preserve-attributes always`"
    `preserve-attributes always` silently suppresses reflected routes with IPv6 link-local next hops.
    AVD never renders it, but it can still be added with custom structured configuration or `eos_cli`.

## ECMP

ECMP uses the existing `bgp_maximum_paths` and `bgp_ecmp` keys, with the same defaults as eBGP (`maximum-paths 4`).
EOS applies `next-hop-self` to reflected routes, so no add-path configuration is needed.

These keys apply to all the nodes that read them. Set them in inventory group vars if tiers need different values.

## Restrictions

AVD raises an error on an `ibgp` underlay router when one of the following is true.
Each restriction can be relaxed later as needed.
The topology and cluster ID checks of the route reflector groups run once for the whole fabric while generating facts. The others run per device while generating structured config.

| Condition | Reason |
| --------- | ------ |
| `underlay_rfc5549` is not `true` | IPv4 numbered sessions are not supported yet. |
| `underlay_ipv6` or `underlay_ipv6_numbered` is set | Not tested. |
| `overlay_routing_protocol` is not `none` (EVPN, HER, CVX, MPLS) | Not tested. `bgp cluster-id` is shared with the overlay route reflectors. |
| `uplink_type` is not `p2p`, or the node type has `mpls_lsr: true` | Not tested. `lan` would render `router bgp` without sessions. |
| MLAG | iBGP split horizon breaks the MLAG backup path. |
| WAN router (`wan_role` set) | WAN logic lives on the underlay peer group. |
| An uplink or downlink switch is not an `ibgp` underlay router with `p2p` uplinks (L2 switches, other protocols) | Keeps the route reflector client sets clean. |
| Local and peer BGP AS differ on a fabric link, also with AS ranges | Strict iBGP. |
| An `l3_edge` or `core_interfaces` link has `include_in_underlay_protocol: true` (the default) or `routing_protocol: ebgp` | These links have no up or down direction, and external routes are not tested. |
| Node `l3_interfaces` or `l3_port_channels` with BGP peers | External routes are not tested. |
| Network services (VRFs or L2 VLANs) on the node after filtering | Not tested. |
| Inband management or inband ZTP, on the node or its downlink switches | Inband host routes are only exported with eBGP today. |
| Underlay multicast (PIM-SM or static, fabric or node level) | Not tested. |
| `bgp_peer_groups.ipv4_underlay_peers` is set | Not used with `ibgp`. Move the settings to the new peer groups. |
| `uplink_bfd: true` | RFC 5549 neighbor interfaces can't carry per-neighbor BFD. Use `bgp_peer_groups.<group>.bfd`. |
| `underlay_filter_peer_as: true` | Not used with RFC 5549, and meaningless with one AS. |
| `bgp_cluster_id` is set on a node without downlink switches | It would be silently ignored. |
| The clients of a route reflector don't all have the same uplink switches, or those don't all have the same downlink switches | A shared cluster ID would drop routes. |
| `bgp_cluster_id` is missing on a route reflector, or differs between the route reflectors of a group | A shared cluster ID would drop routes. |
| Two RR groups use the same `bgp_cluster_id` | Cluster list loop detection would drop routes between them. |
| `rr_underlay_peers.name` equals `rr_clients_underlay_peers.name` | The attributes of both directions would merge. |
| The password or `bfd` of `rr_underlay_peers` and `rr_clients_underlay_peers` differ | Each session uses one group on each end. |
| A type 7 `password` can't be decrypted with the name of its peer group | EOS decrypts it with that name. |
