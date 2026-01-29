# Glossary

## Table of Contents

- [C](#c)
- [G](#g)
- [N](#n)

## C

### custom_node_type_keys

**Type**: List, items: Dictionary  
**Path**: `custom_node_type_keys`  

Define Custom Node Type Keys, to specify the properties of each node type in the fabric.
This allows for complete customization of the fabric layout and functionality.
`custom_node_type_keys` should be defined in top level group_var for the fabric.
These values will be combined with the defaults; custom node type keys named the same as a
default node_type_key will replace the default.

---

### cv_tags_topology_type

**Type**: String  
**Path**: `cv_tags_topology_type`  

Device type that CloudVision should use when generating the Topology like "leaf", "spine", "core", "edge" or "member-leaf". Defaults to the setting under node_type_keys.

---

## G

### generate_cv_tags

**Type**: Dictionary  
**Path**: `generate_cv_tags`  

Generate CloudVision Tags based on AVD data.

---

## N

### node_type_keys

**Type**: List, items: Dictionary  
**Path**: `node_type_keys`  
**Default**: `See documentation`  

Define Node Type Keys, to specify the properties of each node type in the fabric.
This allows for complete customization of the fabric layout and functionality.
`node_type_keys` should be defined in top level group_var for the fabric.

The default values will be overridden if this key is defined.
If you need to change all the existing `node_type_keys`, it is recommended to copy the defaults and modify them.
If you need to add custom `node_type_keys`, create them under `custom_node_type_keys` - if named identically to default `node_type_keys` entries,
custom entries will replace the equivalent default entry.

---
