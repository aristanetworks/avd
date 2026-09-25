<!--
  ~ Copyright (c) 2025-2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# L2 Ring Topology

## Introduction

**L2 ring topology** chains a sequence of L2 leafs together with plain
ethernet trunks. AVD supports this design with `uplink_type: l2-ethernet`,
where each ring node is modeled with individual trunk interfaces toward
its neighbor devices. The ring is closed by
landing both ends on a pair of L3 leafs (typically MLAG), which gives the
ring a redundant path back into the EVPN underlay without requiring
spanning tree to block a port.

### When to Use L2 Ring Topology

- **Linear or ring cabling** in a rack row, building floor, or industrial
  cabinet where running parallel uplinks back to a pair of leafs is
  impractical.
- **Out-of-band or campus extension** where a small group of access
  switches must reach the fabric over a chained path.
- **Replacing a stacked access design** with a chain of L2 switches
  configured by AVD.

## Concepts

**uplink_type: l2-ethernet** — A new value (added in AVD 6.2) that tells
AVD to model each uplink as a single L2 trunk ethernet interface, instead
of a port-channel or routed P2P link. Use it on nodes with
`type: l2leaf`; the node group must also set `mlag: false`.

**Bidirectional uplink declaration** — In a ring, every node must declare
its neighbors on **both** sides under `uplink_switches`, even though the
physical link is the same cable. This is what allows AVD to compute the
correct VLAN list on each trunk and is required for `filter.only_vlans_in_use`
to behave correctly.

## Basic L2 Ring

The L2 part of the ring is defined under a single `node_group` with
`mlag: false` and `uplink_type: l2-ethernet`. Two uplinks must be
defined for each node towards both neighbor devices. The L3 leafs at both
ends terminate the ring on their downlink ports.

```yaml title="HTL2R_L2_LEAFS/l2leafs.yml"
--8<--
ansible_collections/arista/avd/extensions/molecule/howto/inventory/group_vars/HTL2R_L2_LEAFS/l2leafs.yml:ring
--8<--
```

1. `uplink_type: l2-ethernet` is not supported for MLAG, so the
   node group must set `mlag: false`.
2. `uplink_type: l2-ethernet` switches AVD's uplink generator from
   port-channel to a plain switchport trunk per uplink.
3. Define two links for each ring node.
4. Bidirectional declaration — `htl2r-l2leaf2` lists both neighboring
   L2 leafs as `uplink_switches`, and those neighbors reciprocate. Without
   this, AVD cannot reason about which VLANs belong on each ring trunk.
5. `filter.only_vlans_in_use: true` keeps `l2leaf2` lean — it would
   otherwise carry every VLAN defined in network services, even ones it
   never trunks.

### Generated configuration on a ring node

AVD renders each configured ring link as a trunk ethernet interface with
the computed VLAN list:

```cli title="htl2r-l2leaf1 ring uplinks"
--8<--
docs/howto/l2_ring_topology/artifacts/l2leaf1-ring-uplinks.cfg
--8<--
```

`Ethernet1` connects to `htl2r-leaf1a Et10`; `Ethernet2` connects
to `htl2r-l2leaf2 Et1`. The opposite end of the chain terminates on
`htl2r-leaf1b Et10`.

### Generated configuration on the ring entry leaf

The L3 leaf pair is defined as a normal MLAG pair. The ring nodes point
to the L3 leaf downlink interfaces through their `uplink_switches` and
`uplink_switch_interfaces` values.

```yaml title="HTL2R_L3_LEAFS/l3leaf.yml"
--8<--
ansible_collections/arista/avd/extensions/molecule/howto/inventory/group_vars/HTL2R_L3_LEAFS/l3leaf.yml:l3leafs
--8<--
```

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
configure only the VLANs consumed by an attached endpoint or required by
another ring member reachable through that node. This keeps access
switches from carrying the full fabric VLAN set while preserving the
VLANs needed to keep the ring intact:

```cli title="htl2r-l2leaf2 with only_vlans_in_use"
--8<--
docs/howto/l2_ring_topology/artifacts/l2leaf2-filtered-ring.cfg
--8<--
```

`Ethernet10` (the server port) only trunks the VLANs declared on the
attached endpoint (`100,200`). `Ethernet1` and `Ethernet2` (the ring
trunks) carry every VLAN reachable through the ring (`100-101,200`),
because removing any of them would break connectivity to another ring node.

!!! note
    `filter.only_vlans_in_use` depends on each ring node listing both
    neighbors under `uplink_switches` so AVD can preserve VLANs required
    farther along the ring.

## Best Practices

1. **Always declare uplinks both ways.** Every ring node lists its left
   and right neighbor under `uplink_switches`. This is the single most
   common cause of ring breakage in practice.
2. **Use MLAG L3 leafs to terminate the ring.** Landing the two ring
   ends on the same L3 leaf is supported but eliminates the redundancy
   the ring exists to provide.
3. **Keep `mlag: false` explicit.** `uplink_type: l2-ethernet` is only
   valid on non-MLAG L2 nodes; AVD will reject the combination otherwise.

## Troubleshooting

### A VLAN works on the L3 leafs but is missing on a ring node

**Issue**: A tenant VLAN is configured under network services and shows
up on the L3 leafs and the closest ring nodes, but disappears beyond a
node mid-ring.

**Solution**:

- Verify the affected ring node lists **both** neighbors under
  `uplink_switches`. A common mistake is to copy the head node's config
  (which only declares one neighbor) onto a middle node.
- If `filter.only_vlans_in_use: true` is set on any node along the
  path, confirm an endpoint or another ring member reachable through the
  declared neighbors actually uses that VLAN. The filter computes "in use"
  per node.

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
- [Node type variables](../../../ansible_collections/arista/avd/roles/eos_designs/docs/data-models.md#node-type-variables)
