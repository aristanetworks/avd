# Glossary

## Table of Contents

- [C](#c)
- [U](#u)

## C

### cv_topology

**Type**: List, items: Dictionary  
**Path**: `cv_topology`  

Generate AVD configurations directly from the given CloudVision topology.
Activate this feature by setting `use_cv_topology` to `true`.
Interfaces are assigned according to the following rules:
  - All interfaces connected to the MLAG peer (only other device in the same node group) will be `mlag_interfaces`.
  - For connections between devices with different `cv_topology_levels[type=<type>].level`, the lowest level will be considered the "parent switch"
    and the highest level will be considered the "child switch".
  - Connections between devices with the same `cv_topology_levels[type=<type>].level` will be ignored and must be created manually.
  - The first Management interface is assigned as `mgmt_interface` unless it is set for the node or under platform_settings.
Neighbor hostnames must match the inventory hostnames of the AVD inventory to be taken into consideration.

---

### cv_topology_levels

**Type**: List, items: Dictionary  
**Path**: `cv_topology_levels`  

Type to level assignment used for generation of the AVD topology from the CloudVision topology.
See `cv_topology` for details.

---

## U

### use_cv_topology

**Type**: Boolean  
**Path**: `use_cv_topology`  

Generate AVD configurations directly from a given CloudVision topology.
See `cv_topology` for details.
Requires both `cv_topology` and `cv_topology_levels` to be set.

---
