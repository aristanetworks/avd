# Glossary

## Table of Contents

- [D](#d)

## D

### default_network_ports_description

**Type**: String  
**Path**: `default_network_ports_description`  
**Default**: `{endpoint?}`  

Default description or description template to be used on all ports defined under `network_ports`.
This can be a template using the AVD string formatter syntax: https://avd.arista.com/stable/ansible_collections/arista/avd/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.
The available template fields are:
  - `endpoint_type`: Always set to `network_port`.
  - `endpoint`: The value of the `endpoint` key if set.
  - `port_channel_id`: The port-channel number for the switch.

By default the description is templated from the `endpoint` key if set.

---

### default_network_ports_port_channel_description

**Type**: String  
**Path**: `default_network_ports_port_channel_description`  
**Default**: `{endpoint?}{endpoint_port_channel?<_}`  

Default description or description template to be used on all port-channels defined under `network_ports`.
This can be a template using the AVD string formatter syntax: https://avd.arista.com/stable/ansible_collections/arista/avd/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.
The available template fields are:
  - `endpoint_type`: Always set to `network_port`.
  - `endpoint`: The value of the `endpoint` key if set.
  - `endpoint_port_channel`: The value of `endpoint_port_channel` if set.
  - `port_channel_id`: The port-channel number for the switch.
  - `adapter_description`: The adapter's description if set.
  - `adapter_description_or_endpoint`: Helper alias of the adapter_description or endpoint.

By default the description is templated from the `endpoint` key if set.

---
