<!--
  ~ Copyright (c) 2025-2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# Inventory Organisation

## Introduction

**Inventory Organisation** defines how Ansible inventory files and `group_vars` are structured on disk. As your fabric grows from a lab topology to a production multi-DC network, the right structure prevents variables from becoming hard to find, hard to reuse, and hard to maintain.

This guide covers four topology scales — **Small**, **Medium**, **Large**, and **XL** — and explains when to split variables across files, when to introduce subdirectory hierarchies, and how each scale maps to a concrete file layout.

### When to Think About Inventory Organisation

- When adding a second data centre to an existing single-DC fabric
- When a single `group_vars/all.yml` file has grown beyond a few hundred lines
- When multiple teams need to manage different parts of the same inventory
- When you want to reuse common settings (default interfaces, BGP policies) across groups

## Concepts

**inventory**: The set of Ansible files that define which devices exist and how they are grouped. For AVD, this includes `hosts.yml` and the `group_vars/` directory.

**group_vars**: A directory where Ansible automatically loads YAML files named after inventory groups. AVD reads these to build per-device structured configurations.

**group hierarchy**: The parent-child relationships between inventory groups. Variables defined in a parent group are inherited by all children, which allows sharing common settings across the fabric.

**fabric_name**: The top-level inventory group that covers all devices in scope of a single AVD run. It must match the group name exactly.

**node_groups**: Within AVD data models (e.g., `l3leaf`), a `node_groups` list pairs devices that share settings — most commonly an MLAG pair. Each `node_group` can override defaults for its members.

## Choosing Your Topology Scale

| Scale | Nodes | DCs | File Strategy |
| ------- | ------- | ---- | ---------------------------------------------- |
| **Small** | < 10 | 1 | One file per group, minimal hierarchy |
| **Medium** | 10–50 | 1 | Multiple files per group, split by purpose |
| **Large** | 50–200 | 1–2 | Files split by function + DC-level subgroups |
| **XL** | 200+ | 3+ | Full directory hierarchy, per-DC group_vars |

## Small Topology

A Small topology suits lab environments, proof-of-concept builds, and small branch sites. Keep all variables for each group in a single file. Avoid splitting prematurely — one file per group is easy to navigate at this scale.

**Typical layout:**

```text
inventory/
├── hosts.yml
└── group_vars/
    ├── FABRIC.yml       # fabric-wide settings
    ├── SPINES.yml       # spine nodes
    └── L3_LEAFS.yml     # leaf nodes
```

**Example `hosts.yml` for a 1-spine / 2-leaf topology:**

```yaml title="hosts.yml"
---
all:
  children:
    FABRIC:
      children:
        SPINES:
          hosts:
            lab-spine1:
              ansible_host: 192.168.1.11
        L3_LEAFS:
          hosts:
            lab-leaf1:
              ansible_host: 192.168.1.101
            lab-leaf2:
              ansible_host: 192.168.1.102
```

**Example `group_vars/FABRIC.yml`** for a Small topology — all fabric settings in one place:

```yaml title="group_vars/FABRIC.yml"
---
fabric_name: FABRIC
underlay_routing_protocol: ebgp
overlay_routing_protocol: ebgp
p2p_uplinks_mtu: 1500

default_interfaces:
  - types: [spine]
    platforms: [default]
    uplink_interfaces: [Ethernet1-2]
    downlink_interfaces: [Ethernet1-8]
  - types: [l3leaf]
    platforms: [default]
    uplink_interfaces: [Ethernet1-2]
    mlag_interfaces: [Ethernet3-4]

default_node_types:
  - match_hostnames: [".*spine.*"]
    node_type: spine
  - match_hostnames: [".*leaf.*"]
    node_type: l3leaf
```

!!! tip
    At Small scale, `group_vars/FABRIC.yml` (a flat file) is simpler than `group_vars/FABRIC/fabric.yml` (a directory). Both are valid Ansible — use whichever is easier for your team to navigate.

## Medium Topology

A Medium topology is the most common AVD deployment: one data centre, 2 spines, and multiple MLAG leaf pairs. At this scale, split variables across **one file per purpose** within each group folder. This makes it easy to find and modify fabric settings, interface assignments, and node definitions independently.

**Typical layout:**

```text
inventory/
├── hosts.yml
└── group_vars/
    ├── FABRIC/
    │   ├── fabric.yml            # BGP, underlay/overlay protocols, MTU
    │   └── default_interfaces.yml # Interface assignments by node type
    ├── SPINES/
    │   └── spines.yml            # Spine node definitions
    └── L3_LEAFS/
        └── l3_leafs.yml          # Leaf node groups and defaults
```

### Inventory

The example below shows a medium-scale topology: 2 spines and 2 MLAG leaf pairs (4 leafs total).

```yaml title="hosts.yml"
---
all:
  children:
    FABRIC:
      children:
        SPINES:
          hosts:
            htio-spine1:
              ansible_host: 172.16.3.11
            htio-spine2:
              ansible_host: 172.16.3.12
        L3_LEAFS:
          hosts:
            htio-leaf1a:
              ansible_host: 172.16.3.101
            htio-leaf1b:
              ansible_host: 172.16.3.102
            htio-leaf2a:
              ansible_host: 172.16.3.103
            htio-leaf2b:
              ansible_host: 172.16.3.104
```

### Fabric-wide Settings

Fabric-wide variables belong in the group that covers all devices — typically named `FABRIC`.

```yaml title="group_vars/FABRIC/fabric.yml"
--8<--
ansible_collections/arista/avd/extensions/molecule/howto/inventory/group_vars/HTIO/fabric.yml
--8<--
```

1. `fabric_name` must exactly match the inventory group covering all devices in scope of the AVD run.
2. Underlay protocol — eBGP is standard for EVPN/VXLAN fabrics.
3. Overlay protocol — eBGP for EVPN peering between leafs and spines.
4. Set `1500` for vEOS-lab and cEOS; `9214` for physical production hardware.

### Default Interfaces

Splitting `default_interfaces` into its own file keeps the fabric file focused on global settings and makes it easier to adapt interface assignments per platform.

```yaml title="group_vars/FABRIC/default_interfaces.yml"
--8<--
ansible_collections/arista/avd/extensions/molecule/howto/inventory/group_vars/HTIO/default_interfaces.yml
--8<--
```

1. AVD applies these interface assignments automatically — no need to repeat `uplink_interfaces` on every node.
2. Leaf uplinks connect to spines, allocated in order from this list.
3. MLAG peer-link interfaces, bundled into a Port-Channel by AVD.
4. Hostname patterns auto-assign node types, removing the need to set `type:` on each node.

### Spine Configuration

```yaml title="group_vars/SPINES/spines.yml"
--8<--
ansible_collections/arista/avd/extensions/molecule/howto/inventory/group_vars/HTIO_SPINES/spines.yml
--8<--
```

1. Platform controls which EOS features are available. Use `vEOS-lab` for virtual topologies.
2. All spine loopbacks are allocated from this pool sequentially by node `id`.
3. All spines share one BGP AS in an eBGP spine-leaf design.
4. Each entry defines one spine. The `id` drives IP allocation and loopback numbering.

### Leaf Configuration

```yaml title="group_vars/L3_LEAFS/l3_leafs.yml"
--8<--
ansible_collections/arista/avd/extensions/molecule/howto/inventory/group_vars/HTIO_L3_LEAFS/l3_leafs.yml
--8<--
```

1. Leaf loopbacks (router-id) are allocated from this pool, offset by `loopback_ipv4_offset` to avoid collision with spine loopbacks from the same pool.
2. VTEP loopbacks (Loopback1) are allocated from a separate pool — one per MLAG pair (shared between the two peers).
3. All leafs connect upstream to these two spines.
4. MLAG peer-link IP pool (Vlan4094). Each pair gets a /31 allocated automatically.
5. Two nodes in this group form an MLAG pair. The `group` name becomes the MLAG `domain-id`.
6. A second MLAG pair with its own BGP AS. Each pair needs a unique AS.

### Generated Configuration

With this layout, AVD generates a complete spine configuration without any per-device interface or BGP neighbor definitions in the vars:

```cli title="Spine P2P interfaces and loopback"
--8<--
docs/howto/inventory_organisation/artifacts/htio-spine1-p2p.cfg
--8<--
```

Each leaf connection is automatically described and addressed from the `uplink_ipv4_pool`. The leaf MLAG configuration is also fully derived from the `node_groups` definition:

```cli title="MLAG configuration on htio-leaf1a"
--8<--
docs/howto/inventory_organisation/artifacts/htio-leaf1a-mlag.cfg
--8<--
```

The `domain-id` matches the `group` name from `node_groups`, and the peer address is allocated from `mlag_peer_ipv4_pool`.

## Large Topology

A Large topology typically spans one or two data centres with 50–200 nodes. Add a **DC-level group** in the inventory hierarchy to isolate per-DC settings, and split node variables further — for example, separating network services from node definitions.

**Typical layout:**

```text
inventory/
├── hosts.yml
└── group_vars/
    ├── FABRIC/
    │   ├── fabric.yml
    │   └── default_interfaces.yml
    ├── DC1/
    │   └── dc1.yml               # DC1-specific overrides (ASN range, pools)
    ├── DC1_SPINES/
    │   └── spines.yml
    ├── DC1_L3_LEAFS/
    │   ├── l3_leafs.yml          # Node definitions
    │   └── network_services.yml  # Tenant/VRF/VLAN assignments for this DC
    ├── DC2/
    │   └── dc2.yml
    ├── DC2_SPINES/
    │   └── spines.yml
    └── DC2_L3_LEAFS/
        ├── l3_leafs.yml
        └── network_services.yml
```

**Example `hosts.yml` with DC groups:**

```yaml title="hosts.yml"
---
all:
  children:
    FABRIC:
      children:
        DC1:
          children:
            DC1_SPINES:
              hosts:
                dc1-spine1:
                  ansible_host: 172.16.1.11
                dc1-spine2:
                  ansible_host: 172.16.1.12
            DC1_L3_LEAFS:
              hosts:
                dc1-leaf1a:
                  ansible_host: 172.16.1.101
                dc1-leaf1b:
                  ansible_host: 172.16.1.102
        DC2:
          children:
            DC2_SPINES:
              hosts:
                dc2-spine1:
                  ansible_host: 172.16.2.11
            DC2_L3_LEAFS:
              hosts:
                dc2-leaf1a:
                  ansible_host: 172.16.2.101
```

!!! note
    Variables in `group_vars/DC1/` apply to all devices in `DC1` and its children (`DC1_SPINES`, `DC1_L3_LEAFS`). This lets you set DC-specific BGP AS ranges, IP pools, or management VRF settings without repeating them on every subgroup.

## XL Topology

An XL topology covers 200+ nodes across three or more data centres, often with a pod structure. At this scale, introduce **per-DC inventory directories** so that each DC can be managed and tested independently.

**Typical layout:**

```text
inventory/
├── global/
│   └── group_vars/
│       └── all.yml               # Global defaults shared across all DCs
├── dc1/
│   ├── hosts.yml                 # DC1 devices only
│   └── group_vars/
│       ├── DC1/
│       │   ├── fabric.yml
│       │   └── default_interfaces.yml
│       ├── DC1_POD1_SPINES/
│       │   └── spines.yml
│       └── DC1_POD1_LEAFS/
│           └── l3_leafs.yml
├── dc2/
│   ├── hosts.yml
│   └── group_vars/
│       └── ...
└── site.yml                      # Top-level playbook referencing all DC inventories
```

**Ansible inventory merging for XL:**

```ini title="ansible.cfg"
[defaults]
inventory = inventory/global,inventory/dc1,inventory/dc2
```

Ansible merges all specified inventory directories, making groups from each DC visible in a single run while keeping the files physically separated per DC.

!!! warning "AVD limitation"
    Each AVD run processes one `fabric_name` group. If you split inventories across DCs, run AVD once per DC using `-i inventory/dc1` etc., or use a single merged inventory with a shared `FABRIC` group that spans all DCs.

## Best Practices

1. **Match group names to their purpose**: Use names like `DC1_L3_LEAFS`, not generic names like `LEAFS`, to make multi-DC inventories unambiguous.

2. **One file per purpose within a group folder**: Split `fabric.yml`, `default_interfaces.yml`, and `network_services.yml` rather than growing a single file. Each file can then be reviewed, templated, or overridden independently.

3. **Inherit via the group hierarchy instead of duplicating**: Define shared settings (loopback pools, BGP policies, MTU) at the highest common parent group. Only define overrides at the child level.

4. **Keep `hosts.yml` focused on structure, not variables**: `hosts.yml` should only contain group hierarchy and `ansible_host` values. All variable content belongs in `group_vars/`.

5. **Use `default_interfaces` and `default_node_types` to eliminate per-node repetition**: At Medium scale and above, define these once in `group_vars/FABRIC/` rather than repeating interface lists on every node definition.

6. **Avoid mixing flat files and directory group_vars for the same group**: Ansible loads both `group_vars/FABRIC.yml` and `group_vars/FABRIC/*.yml`, but mixing the two patterns in one inventory is confusing. Pick one style per group and be consistent.

## Troubleshooting

### Variable not applying to a device

**Issue**: A variable defined in `group_vars/` is not taking effect on a specific device.

**Solution**:

- Confirm the device is a member of the group: `ansible-inventory -i inventory/ --host <device>`
- Check for a more-specific group overriding the value. Variables from child groups take precedence over parent groups.
- Verify the YAML file is syntactically valid: `yamllint group_vars/<GROUP>/file.yml`

### Duplicate variable definition warning

**Issue**: Ansible warns that a variable is defined in multiple places.

**Solution**:

- Search all `group_vars/` files for the variable name: `grep -r "variable_name" group_vars/`
- Identify which group's definition should win. Remove the duplicate, or move the shared value to the common parent group.

### `fabric_name` does not match any group

**Issue**: AVD errors with `fabric_name 'FABRIC' is not defined as a group in the inventory`.

**Solution**:

- Ensure the group named in `fabric_name` exists in `hosts.yml` and contains all fabric devices.
- The value is case-sensitive — `FABRIC` and `fabric` are different groups.

### Variables from a file are not loaded

**Issue**: A new file added under `group_vars/<GROUP>/` is not being picked up.

**Solution**:

- Ansible loads all `.yml` and `.yaml` files in a `group_vars/<GROUP>/` directory automatically — no registration required.
- Confirm the file has valid YAML and starts with `---`.
- Confirm the directory name exactly matches the inventory group name (case-sensitive).

## Reference

For complete details on all available properties, see:

- [EOS Designs Schema](../../../ansible_collections/arista/avd/roles/eos_designs/docs/data-models.md)
- [Fabric Topology How-To Guide](../fabric_topology/README.md)
- [Ansible Inventory documentation](https://docs.ansible.com/ansible/latest/inventory_guide/intro_inventory.html)
