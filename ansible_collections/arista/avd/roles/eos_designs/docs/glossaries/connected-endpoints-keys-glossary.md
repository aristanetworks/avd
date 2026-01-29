# Glossary

## Table of Contents

- [C](#c)

## C

### connected_endpoints_keys

**Type**: List, items: Dictionary  
**Path**: `connected_endpoints_keys`  
**Default**: `See documentation`  

Endpoints connecting to the fabric can be grouped by using separate keys.
The keys can be customized to provide a better organization or grouping of your data.
`connected_endpoints_keys` should be defined in the top level group_vars for the fabric.
The default values will be overridden if defining this key, so it is recommended to copy the defaults and modify them.
If you need to add custom `connected_endpoints_keys`, create them under `custom_connected_endpoints_keys`.
Entries under `custom_connected_endpoint_keys` will take precedence over entries in `connected_endpoint_keys`.


---

### custom_connected_endpoints_keys

**Type**: List, items: Dictionary  
**Path**: `custom_connected_endpoints_keys`  

`custom_connected_endpoints_keys` offers a flexible way to extend endpoint definitions without altering the `connected_endpoints_keys`.
The values defined in `custom_connected_endpoints_keys`, are prepended to the ones in `connected_endpoint_keys`, taking precedence over any values in `connected_endpoint_keys`.
This approach helps preserving the default `connected_endpoints_keys`, unlike directly overriding it.

---
