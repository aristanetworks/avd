# Glossary

## Table of Contents

- [D](#d)

## D

### default_connected_endpoints_description

**Type**: String  
**Path**: `default_connected_endpoints_description`  
**Default**: `{endpoint_type?>_!u}{endpoint}{endpoint_port?<_}`  

Default description or description template to be used on all ports to connected endpoints.
This can be a template using the AVD string formatter syntax: https://avd.arista.com/stable/ansible_collections/arista/avd/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.
The available template fields are:
  - `endpoint_type`: The `type` of the connected endpoint either set on the endpoint or taken from `connected_endpoints_keys[].type` like `server`, `router` etc.
  - `endpoint`: The name of the connected endpoint
  - `endpoint_port`: The value from `endpoint_ports` for this switch port if set.
  - `port_channel_id`: The port-channel number for the switch.

By default the description is templated from the type, name and port of the endpoint if set.

---

### default_connected_endpoints_port_channel_description

**Type**: String  
**Path**: `default_connected_endpoints_port_channel_description`  
**Default**: `{endpoint_type?>_!u}{endpoint}{endpoint_port_channel?<_}`  

Default description or description template to be used on all port-channels to connected endpoints.
This can be a template using the AVD string formatter syntax: https://avd.arista.com/stable/ansible_collections/arista/avd/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.
The available template fields are:
  - `endpoint_type` - the `type` of the connected endpoint either set on the endpoint or taken from `connected_endpoints_keys.type` like `server`, `router` etc.
  - `endpoint`: The name of the connected endpoint
  - `endpoint_port_channel`: The value of `endpoint_port_channel` if set.
  - `port_channel_id`: The port-channel number for the switch.
  - `adapter_description`: The adapter's description if set.
  - `adapter_description_or_endpoint`: Helper alias of the adapter_description or endpoint.

By default the description is templated from the type, name and port-channel name of the endpoint if set.

---
