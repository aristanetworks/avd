# Glossary

## Table of Contents

- [A](#a)
- [F](#f)

## A

### algorithm

**Type**: String  
**Path**: `fabric_numbering.node_id.algorithm`  
**Default**: `static`  
**Valid Values**: `static`, `pool_manager`  

IDs will be automatically assigned according to the configured algorithm.
- `static` will use the statically set IDs under node setting.
- `pool_manager` will activate the pool manager for ID pools.
  Any statically set ID under node settings will be reserved in the pool if possible.
  Otherwise an error will be raised.

---

## F

### fabric_numbering

**Type**: Dictionary  
**Path**: `fabric_numbering`  

PREVIEW: This feature is in marked as "preview", which means it is subject to change at any time.

Assignment policies for numbers like Node ID.

---

### fabric_numbering_node_id_pool

**Type**: String  
**Path**: `fabric_numbering_node_id_pool`  
**Default**: `fabric_name={fabric_name}{dc_name?</dc_name=}{pod_name?</pod_name=}{type?</type=}`  

Name of Node ID pool or template used to render the name of each Node ID pool.
For each device the Node ID is assigned from a pool shared by all devices rendering the same pool name.
This can be modified to include fewer or more fields to keep separate pools or to use the same pool across areas.
This can be a template using the AVD string formatter syntax: https://avd.arista.com/stable/ansible_collections/arista/avd/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.
The available template fields are:
  - `fabric_name`: The `fabric_name` assigned to the device.
  - `dc_name`: The `dc_name` assigned to the device.
  - `pod_name`: The `pod_name` assigned to the device.
  - `type`: The `type` assigned to the device.
  - `rack`: The `rack` assigned to the device.

By default the Node ID pool key is templated from `fabric_name`, `dc_name`, `pod_name` and `type`.

---
