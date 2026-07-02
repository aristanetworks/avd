<!--
  ~ Copyright (c) 2025-2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# L2 Ring Topology

## Introduction

**L2 ring topology** chains a sequence of L2 leafs together with plain
ethernet trunks instead of port-channels, so each ring node uses one uplink
to its upstream switch and one uplink to its downstream ring neighbor. AVD
supports this with `uplink_type: l2-ethernet`. The ring is closed by
landing both ends on a pair of L3 leafs (typically MLAG), which gives the
ring a redundant path back into the EVPN underlay without requiring
spanning-tree to break a cable in the middle.

### When to Use L2 Ring Topology

- **Linear or ring cabling** in a rack row, building floor, or industrial
  cabinet where running parallel uplinks back to a pair of leafs is
  impractical.
- **Out-of-band or campus extension** where a small group of access
  switches must reach the fabric over a chained path.
- **Replacing a stacked access design** with discrete switches that
  cross-connect, while still configured from the AVD data model.

## Concepts

**uplink_type: l2-ethernet** — A new value (added in AVD 6.2) that tells
AVD to model each uplink as a single L2 trunk ethernet interface, instead
of a port-channel or routed P2P link. Allowed only for L2 nodes
(`mlag: false`).

**Ring closure** — Both ends of the L2 ring uplink to L3 leafs (commonly
an MLAG pair). The L3 leafs source the SVI gateways and the EVPN/VXLAN
encapsulation; the ring just trunks the VLANs.

**Bidirectional uplink declaration** — In a ring, every node must declare
its neighbors on **both** sides under `uplink_switches`, even though the
physical link is the same cable. This is what allows AVD to compute the
correct VLAN list on each trunk and is required for `filter.only_vlans_in_use`
to behave correctly.

**filter.only_vlans_in_use** — Restricts a node's VLAN configuration to
only the VLANs actually consumed by an attached endpoint or required by a
declared downstream ring member. Useful on access switches that should
not carry the full fabric VLAN set.

## Basic L2 Ring

The ring itself is defined under a single `node_group` with
`mlag: false` and `uplink_type: l2-ethernet`. Each node lists two uplinks:
one toward its upstream (an L3 leaf for the head and tail of the ring,
the previous L2 leaf for nodes in the middle) and one toward its
downstream neighbor. The L3 leafs at the two ends terminate the ring on
their downlink ports.

```yaml title="HTL2R_L2_LEAFS/l2leafs.yml"
--8<--
ansible_collections/arista/avd/extensions/molecule/howto/inventory/group_vars/HTL2R_L2_LEAFS/l2leafs.yml:ring
--8<--
```

1. `mlag: false` is required — `uplink_type: l2-ethernet` is rejected for
   MLAG nodes because there is no port-channel to bundle.
2. `uplink_type: l2-ethernet` switches AVD's uplink generator from
   port-channel to a plain switchport trunk per uplink.
3. Two physical uplinks per node — one upstream, one downstream — each
   declared as its own ethernet interface.
4. Bidirectional declaration — `htl2r-l2leaf2` lists both `htl2r-l2leaf1`
   (upstream) and `htl2r-l2leaf3` (downstream) as `uplink_switches`. Both
   `l2leaf1` and `l2leaf3` reciprocate. Without this, AVD cannot reason
   about which VLANs belong on each ring trunk.
5. `filter.only_vlans_in_use: true` keeps `l2leaf2` lean — it would
   otherwise carry every VLAN defined in network services, even ones it
   never trunks.
6. `inband_mgmt_vlan: 110` together with `inband_mgmt_ip` puts
   management traffic for `l2leaf3` on a tenant VLAN already trunked
   through the ring; the matching SVI is created automatically. The VLAN
   must exist in network services and be reachable on every hop along the
   ring.

### Generated configuration on a ring node

AVD turns each L2 leaf's two uplinks into trunk ethernet interfaces with
the computed VLAN list:

```cli title="htl2r-l2leaf1 ring uplinks"
--8<--
docs/howto/l2_ring_topology/artifacts/l2leaf1-ring-uplinks.cfg
--8<--
```

`Ethernet1` faces the L3 leaf (`htl2r-leaf1a Et10`); `Ethernet2` faces
the next ring node (`htl2r-l2leaf2 Et1`). The ring closes on the other
side at `htl2r-leaf1b Et10`.

### Generated configuration on the ring entry leaf

The L3 leaf treats the ring uplink as a normal trunk-mode L2 downlink —
nothing special is required on the L3 leaf side beyond pointing the L2
leafs at it.

```cli title="htl2r-leaf1a ring entry interface"
--8<--
docs/howto/l2_ring_topology/artifacts/leaf1a-ring-entry.cfg
--8<--
```

## VLAN Filtering on a Ring Member

Adding `filter.only_vlans_in_use: true` to a ring member tells AVD to
configure only the VLANs the node actually needs. With bidirectional
uplink declaration, "needs" includes VLANs required by other ring
members reachable through this node, so trunks remain wide enough to
keep the ring intact:

```cli title="htl2r-l2leaf2 with only_vlans_in_use"
--8<--
docs/howto/l2_ring_topology/artifacts/l2leaf2-filtered-ring.cfg
--8<--
```

`Ethernet10` (the server port) only trunks the VLANs declared on the
attached endpoint (`100,200`). `Ethernet1` and `Ethernet2` (the ring
trunks) carry every VLAN reachable through the ring (`100-101,110,200`),
because removing any of them would break a downstream node.

!!! warning
    `filter.only_vlans_in_use` only works on a ring if every node in the
    ring lists its neighbors **bidirectionally** under `uplink_switches`.
    A one-way declaration causes AVD to drop VLANs from the trunk on the
    side that did not declare the other neighbor — which silently breaks
    connectivity for that VLAN past that point.

## Inband Management Over the Ring

Ring switches that lack an out-of-band management port can be managed
via an inband VLAN trunked through the ring. Configure
`inband_mgmt_vlan` and `inband_mgmt_ip` on each ring node that needs it,
and make sure the VLAN exists in network services with a gateway SVI on
the L3 leafs:

```yaml title="HTL2R/services.yml — inband VLAN in tenant"
--8<--
ansible_collections/arista/avd/extensions/molecule/howto/inventory/group_vars/HTL2R/services.yml:tenants
--8<--
```

1. The inband management VLAN (110) is declared as a tenant SVI so the
   L3 leafs source the gateway and EVPN extends it across the fabric.

The ring node gets a routed SVI with the per-node IP. AVD also adds VLAN
110 to the upstream trunks automatically because the node declared both
`inband_mgmt_vlan: 110` and `inband_mgmt_ip`:

```cli title="htl2r-l2leaf3 inband management"
--8<--
docs/howto/l2_ring_topology/artifacts/l2leaf3-inband-mgmt.cfg
--8<--
```

!!! note
    If different ring nodes use different inband VLANs, every VLAN in
    use must be present and trunked end-to-end on the ring path that
    serves it. Mixing inband VLANs along a single ring is supported but
    requires `inband_mgmt_vlan` to either appear in network services or
    be declared on every node along the path so the trunk computation
    permits it.

## Best Practices

1. **Always declare uplinks both ways.** Every ring node lists its left
   and right neighbor under `uplink_switches`. This is the single most
   common cause of ring breakage in practice.
2. **Use MLAG L3 leafs to terminate the ring.** Landing the two ring
   ends on the same L3 leaf is supported but eliminates the redundancy
   the ring exists to provide.
3. **Keep `mlag: false` explicit.** `uplink_type: l2-ethernet` is only
   valid on non-MLAG L2 nodes; AVD will reject the combination otherwise.
4. **Reserve two dedicated Ethernet interfaces per ring node for the ring path.** Ring nodes use
   `Ethernet1` and `Ethernet2` by default (from the fabric-level
   `default_interfaces` for `l2leaf`). Override per-node only when the
   physical cabling requires it.
5. **Use `filter.only_vlans_in_use` selectively.** It pairs cleanly with
   bidirectional declarations but masks misconfiguration on incomplete
   rings. Add it only after the ring is verified to be stable.

## Troubleshooting

### A VLAN works on the L3 leafs but is missing on a ring node

**Issue**: A tenant VLAN is configured under network services and shows
up on the L3 leafs and the closest ring nodes, but disappears beyond a
node mid-ring.

**Solution**:

- Verify the affected ring node lists **both** neighbors under
  `uplink_switches`. A common mistake is to copy the head node's config
  (which only declares its downstream neighbor) onto a middle node.
- If `filter.only_vlans_in_use: true` is set on any node along the
  path, confirm an endpoint or a downstream declared neighbor actually
  uses that VLAN. The filter computes "in use" per node.

### `uplink_type: l2-ethernet` rejected at validation time

**Issue**: AVD validation fails with a message about `uplink_type`
being incompatible with the node settings.

**Solution**:

- Confirm `mlag: false` is set on the same node group. The `l2-ethernet`
  uplink type is only allowed on non-MLAG nodes.
- Confirm the node type is `l2leaf` (or another type that does not
  require `vtep`/`underlay_router`). Routed types reject anything other
  than `p2p`.

### Spanning tree blocks a ring uplink unexpectedly

**Issue**: A ring uplink shows blocking in `show spanning-tree` even
though the cabling is correct.

**Solution**:

- Confirm both ends of every ring link agree on the spanning-tree mode
  (the default in this guide is `mstp`).
- Adjust `spanning_tree_priority` on the L3 leafs (the guide uses
  `4096`) versus the L2 leafs (`16384`) so the L3 leafs are the root
  bridge.

## Reference

For complete details on all available properties, see:

- [Node type uplink management](../../../ansible_collections/arista/avd/roles/eos_designs/docs/data-models.md#node-type-uplink-management)
- [Node type inband management](../../../ansible_collections/arista/avd/roles/eos_designs/docs/data-models.md#node-type-inband-management)
- [Node type variables](../../../ansible_collections/arista/avd/roles/eos_designs/docs/data-models.md#node-type-variables)
