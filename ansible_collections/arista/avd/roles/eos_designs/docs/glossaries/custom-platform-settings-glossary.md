# Glossary

## Table of Contents

- [A](#a)
- [C](#c)

## A

### act_node_type

**Type**: String  
**Path**: `custom_platform_settings.[].digital_twin.act_node_type`  
**Valid Values**: `cloudeos`, `cvp`, `generic`, `third-party`, `tools-server`, `veos`  

ACT node type.

---

## C

### custom_platform_settings

**Type**: List, items: Dictionary  
**Path**: `custom_platform_settings`  

Custom Platform settings to override the default `platform_settings`. This list will be prepended to the list of `platform_settings`. The first entry found where the `platform` node setting is fully matched by any regex in the `platforms` list will be chosen. If no matches are found, the first entry containing a platform `default` will be chosen.

---
