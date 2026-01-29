# Glossary

## Table of Contents

- [A](#a)
- [P](#p)

## A

### act_node_type

**Type**: String  
**Path**: `platform_settings.[].digital_twin.act_node_type`  
**Valid Values**: `cloudeos`, `cvp`, `generic`, `third-party`, `tools-server`, `veos`  

ACT node type.

---

## P

### platform_settings

**Type**: List, items: Dictionary  
**Path**: `platform_settings`  
**Default**: `See documentation`  

Platform settings. The first entry found where the `platform` node setting is fully matched by any regex in the `platforms` list will be chosen. If no matches are found, the first entry containing a platform `default` will be chosen. The default values will be overridden if `platform_settings` is defined. If you need to replace all the default platforms, it is recommended to copy the defaults and modify them. If you need to add custom platforms, create them under `custom_platform_settings`. Entries under `custom_platform_settings` will be matched before the equivalent entries from `platform_settings`.

---
