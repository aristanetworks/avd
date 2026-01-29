# Glossary

## Table of Contents

- [A](#a)
- [B](#b)
- [C](#c)
- [D](#d)
- [E](#e)
- [F](#f)
- [G](#g)
- [H](#h)
- [I](#i)
- [K](#k)
- [L](#l)
- [M](#m)
- [N](#n)
- [O](#o)
- [P](#p)
- [R](#r)
- [S](#s)
- [T](#t)
- [U](#u)
- [V](#v)
- [W](#w)
- [Z](#z)

## A

### access

**Type**: String  
**Path**: `snmp_settings.communities.[].access`  
**Valid Values**: `ro`, `rw`  
---

### act_node_type

**Type**: String  
**Path**: `custom_platform_settings.[].digital_twin.act_node_type`  
**Valid Values**: `cloudeos`, `cvp`, `generic`, `third-party`, `tools-server`, `veos`  

ACT node type.

---

### act_node_type

**Type**: String  
**Path**: `platform_settings.[].digital_twin.act_node_type`  
**Valid Values**: `cloudeos`, `cvp`, `generic`, `third-party`, `tools-server`, `veos`  

ACT node type.

---

### action

**Type**: String  
**Path**: `<connected_endpoints_keys.key>.[].adapters.[].dot1x.authentication_failure.action`  
**Valid Values**: `allow`, `drop`  
---

### action

**Type**: String  
**Path**: `<connected_endpoints_keys.key>.[].adapters.[].poe.reboot.action`  
**Valid Values**: `maintain`, `power-off`  

PoE action for interface.

---

### action

**Type**: String  
**Path**: `<connected_endpoints_keys.key>.[].adapters.[].poe.link_down.action`  
**Valid Values**: `maintain`, `power-off`  

PoE action for interface.

---

### action

**Type**: String  
**Path**: `<connected_endpoints_keys.key>.[].adapters.[].poe.shutdown.action`  
**Valid Values**: `maintain`, `power-off`  

PoE action for interface.

---

### action

**Type**: String  
**Path**: `<custom_connected_endpoints_keys.key>.[].adapters.[].dot1x.authentication_failure.action`  
**Valid Values**: `allow`, `drop`  
---

### action

**Type**: String  
**Path**: `<custom_connected_endpoints_keys.key>.[].adapters.[].poe.reboot.action`  
**Valid Values**: `maintain`, `power-off`  

PoE action for interface.

---

### action

**Type**: String  
**Path**: `<custom_connected_endpoints_keys.key>.[].adapters.[].poe.link_down.action`  
**Valid Values**: `maintain`, `power-off`  

PoE action for interface.

---

### action

**Type**: String  
**Path**: `<custom_connected_endpoints_keys.key>.[].adapters.[].poe.shutdown.action`  
**Valid Values**: `maintain`, `power-off`  

PoE action for interface.

---

### action

**Type**: String  
**Path**: `<network_services_keys.name>.[].bgp_peer_groups.[].missing_policy.direction_in.action`  
**Valid Values**: `deny`, `permit`, `deny-in-out`  

Missing policy action.

---

### action

**Type**: String  
**Path**: `<network_services_keys.name>.[].bgp_peer_groups.[].missing_policy.direction_out.action`  
**Valid Values**: `deny`, `permit`, `deny-in-out`  

Missing policy action.

---

### action

**Type**: String  
**Path**: `<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].missing_policy.direction_in.action`  
**Valid Values**: `deny`, `permit`, `deny-in-out`  

Missing policy action.

---

### action

**Type**: String  
**Path**: `<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].missing_policy.direction_out.action`  
**Valid Values**: `deny`, `permit`, `deny-in-out`  

Missing policy action.

---

### action

**Type**: String  
**Path**: `connected_endpoints.[].adapters.[].dot1x.authentication_failure.action`  
**Valid Values**: `allow`, `drop`  
---

### action

**Type**: String  
**Path**: `connected_endpoints.[].adapters.[].poe.reboot.action`  
**Valid Values**: `maintain`, `power-off`  

PoE action for interface.

---

### action

**Type**: String  
**Path**: `connected_endpoints.[].adapters.[].poe.link_down.action`  
**Valid Values**: `maintain`, `power-off`  

PoE action for interface.

---

### action

**Type**: String  
**Path**: `connected_endpoints.[].adapters.[].poe.shutdown.action`  
**Valid Values**: `maintain`, `power-off`  

PoE action for interface.

---

### action

**Type**: String  
**Path**: `event_handlers.[].trigger_on_maintenance.action`  
**Valid Values**: `after`, `before`, `all`, `begin`, `end`  

Action for maintenance operation.

---

### action

**Type**: String  
**Path**: `ipv4_acls.[].entries.[].action`  
**Valid Values**: `permit`, `deny`  

ACL action.
Required except for remarks.

---

### action

**Type**: String  
**Path**: `logging_settings.policy.match.match_lists.[].action`  
**Valid Values**: `discard`  
---

### action

**Type**: String  
**Path**: `network_ports.[].dot1x.authentication_failure.action`  
**Valid Values**: `allow`, `drop`  
---

### action

**Type**: String  
**Path**: `network_ports.[].poe.reboot.action`  
**Valid Values**: `maintain`, `power-off`  

PoE action for interface.

---

### action

**Type**: String  
**Path**: `network_ports.[].poe.link_down.action`  
**Valid Values**: `maintain`, `power-off`  

PoE action for interface.

---

### action

**Type**: String  
**Path**: `network_ports.[].poe.shutdown.action`  
**Valid Values**: `maintain`, `power-off`  

PoE action for interface.

---

### action

**Type**: String  
**Path**: `port_profiles.[].dot1x.authentication_failure.action`  
**Valid Values**: `allow`, `drop`  
---

### action

**Type**: String  
**Path**: `port_profiles.[].poe.reboot.action`  
**Valid Values**: `maintain`, `power-off`  

PoE action for interface.

---

### action

**Type**: String  
**Path**: `port_profiles.[].poe.link_down.action`  
**Valid Values**: `maintain`, `power-off`  

PoE action for interface.

---

### action

**Type**: String  
**Path**: `port_profiles.[].poe.shutdown.action`  
**Valid Values**: `maintain`, `power-off`  

PoE action for interface.

---

### address_type

**Type**: String  
**Path**: `hardware_counters.features.[].address_type`  
**Valid Values**: `ipv4`, `ipv6`, `mac`  

Supported only for the following features:
- acl: [ipv4, ipv6, mac] if direction is 'out'
- multicast: [ipv4, ipv6]
- route: [ipv4, ipv6]
This validation IS NOT made by the schemas.


---

### algorithm

**Type**: String  
**Path**: `fabric_ip_addressing.mlag.algorithm`  
**Default**: `first_id`  
**Valid Values**: `first_id`, `odd_id`, `same_subnet`  

This variable defines the Multi-chassis Link Aggregation (MLAG) algorithm used.
Each MLAG link will have a /31¹ subnet with each subnet allocated from the relevant MLAG pool via a calculated offset.
The offset is calculated using one of the following algorithms:
  - first_id: `(mlag_primary_id - 1) * 2` where `mlag_primary_id` is the ID of the first node defined under the node_group.
    This allocation method will skip every other /31¹ subnet making it less space efficient than `odd_id`.
  - odd_id: `(odd_id - 1) / 2`. Requires the node_group to have a node with an odd ID and a node with an even ID.
  - same_subnet: the offset will always be zero.
    This allocation method will use the first /31¹ subnet from the pool for all MLAG links.
¹ The prefix length is configurable with a default of /31.

---

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

### allocation

**Type**: String  
**Path**: `internal_vlan_order.allocation`  
**Valid Values**: `ascending`, `descending`  
---

### application_classification

**Type**: Dictionary  
**Path**: `application_classification`  

Application traffic recognition configuration.

---

### auth

**Type**: String  
**Path**: `snmp_settings.users.[].auth`  
**Valid Values**: `md5`, `sha`, `sha256`, `sha384`, `sha512`  
---

### authentication

**Type**: String  
**Path**: `<network_services_keys.name>.[].vrfs.[].ospf.authentication`  
**Valid Values**: `simple`, `message-digest`  

Configure OSPF authentication for all interfaces under the VRF.
Can be overridden at the interface level under `l3_interfaces`, `l3_port_channels` or `svis`.

---

### authentication

**Type**: String  
**Path**: `<network_services_keys.name>.[].vrfs.[].svis.[].nodes.[].ospf.authentication`  
**Valid Values**: `simple`, `message-digest`  
---

### authentication

**Type**: String  
**Path**: `<network_services_keys.name>.[].vrfs.[].svis.[].ospf.authentication`  
**Valid Values**: `simple`, `message-digest`  
---

### authentication

**Type**: String  
**Path**: `<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].ospf.authentication`  
**Valid Values**: `simple`, `message-digest`  
---

### authentication

**Type**: String  
**Path**: `<network_services_keys.name>.[].vrfs.[].l3_port_channels.[].ospf.authentication`  
**Valid Values**: `simple`, `message-digest`  
---

### authentication

**Type**: String  
**Path**: `snmp_settings.groups.[].authentication`  
**Valid Values**: `auth`, `noauth`, `priv`  
---

### authentication

**Type**: String  
**Path**: `svi_profiles.[].nodes.[].ospf.authentication`  
**Valid Values**: `simple`, `message-digest`  
---

### authentication

**Type**: String  
**Path**: `svi_profiles.[].ospf.authentication`  
**Valid Values**: `simple`, `message-digest`  
---

### authentication_level

**Type**: String  
**Path**: `snmp_settings.hosts.[].users.[].authentication_level`  
**Valid Values**: `auth`, `noauth`, `priv`  
---

### avd_data_validation_mode

**Type**: String  
**Path**: `avd_data_validation_mode`  
**Default**: `error`  
**Valid Values**: `error`, `warning`  

Validation Mode for AVD input data validation.
Input data validation will validate the input variables according to the schema.
During validation, messages will generated with information about the host(s) and key(s) which failed validation.
"error" will produce error messages and fail the task.
"warning" will produce warning messages.


---

### avd_digital_twin_mode

**Type**: Boolean  
**Path**: `avd_digital_twin_mode`  
**Default**: `False`  

PREVIEW: This option is marked as "preview", meaning the data models or generated configuration can change at any time.
Enable generation of the Digital Twin version of the fabric (Digital Twin topology, adjusted configuration, etc.).
By default, Digital Twin artifacts (such as the topology file, adjusted structured and EOS configuration, device and fabric documentation) will replace original fabric artifacts.
To keep Digital Twin artifacts separate, adjust the `output_dir_name` and `documentation_dir_name` variables for both `eos_designs` and `eos_cli_config_gen` to point to a dedicated output location.

---

### avd_eos_designs_return_structured_config

**Type**: Boolean  
**Path**: `avd_eos_designs_return_structured_config`  
**Default**: `False`  

Return structured configuration as ansible_facts per device.

---

### avd_eos_designs_structured_config

**Type**: Boolean  
**Path**: `avd_eos_designs_structured_config`  
**Default**: `True`  

Generate structured configuration per device.

---

### avd_eos_designs_validate_inputs_batch_size

**Type**: Integer  
**Path**: `avd_eos_designs_validate_inputs_batch_size`  
**Default**: `10`  

The number of hosts to process in each batch when validating inputs.
Depending on your inventory size and the available resources, you may want to adjust this number.

---

### avd_structured_config_file_format

**Type**: String  
**Path**: `avd_structured_config_file_format`  
**Default**: `yml`  
**Valid Values**: `yml`, `yaml`, `json`  

The file format to use when dumping structured configuration files.


---

## B

### bfd_multihop

**Type**: Dictionary  
**Path**: `bfd_multihop`  
**Default**: `See documentation`  

BFD Multihop tuning.

---

### bgp_as

**Type**: String  
**Path**: `bgp_as`  

BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>" to use to configure overlay when "overlay_routing_protocol" == ibgp.
For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number.

---

### bgp_as_notation

**Type**: String  
**Path**: `bgp_as_notation`  
**Default**: `auto`  
**Valid Values**: `auto`, `asdot`, `asplain`  

AS number representation.
asdot - AS number representation in asdot format (Ex. 123.12).
asplain - AS number representation in asplain format (Ex. 12312).
auto - Will look at the configured ASN and if there is a dot in it,
       it will use asdot otherwise asplain.

---

### bgp_default_ipv4_unicast

**Type**: Boolean  
**Path**: `bgp_default_ipv4_unicast`  
**Default**: `False`  

Default activation of IPv4 unicast address-family on all IPv4 neighbors.
It is best practice to disable activation.


---

### bgp_ecmp

**Type**: Integer  
**Path**: `bgp_ecmp`  

Maximum ECMP for BGP multi-path.

---

### bgp_graceful_restart

**Type**: Dictionary  
**Path**: `bgp_graceful_restart`  

BGP graceful-restart allows a BGP speaker with separate control plane and data plane processing to continue forwarding traffic during a BGP restart.
Its neighbors (receiving speakers) may retain routing information from the restarting speaker while a BGP session with it is being re-established, reducing route flapping.


---

### bgp_maximum_paths

**Type**: Integer  
**Path**: `bgp_maximum_paths`  

Maximum Paths for BGP multi-path.
The default value is 4 except for WAN Routers where the default value is 16.

---

### bgp_mesh_pes

**Type**: Boolean  
**Path**: `bgp_mesh_pes`  
**Default**: `False`  

Configure an iBGP full mesh between PEs, either because there is no RR used or other reasons.
Only supported in combination with MPLS overlay.


---

### bgp_peer_groups

**Type**: Dictionary  
**Path**: `bgp_peer_groups`  

Leverage an Arista EOS switch to generate the encrypted password using the correct peer group name.
Note that the name of the peer groups use '-' instead of '_' in EOS configuration.


---

### bgp_update_wait_for_convergence

**Type**: Boolean  
**Path**: `bgp_update_wait_for_convergence`  
**Default**: `False`  

Disables FIB updates and route advertisement when the BGP instance is initiated until the BGP convergence state is reached.


---

### bgp_update_wait_install

**Type**: Boolean  
**Path**: `bgp_update_wait_install`  
**Default**: `True`  

Do not advertise reachability to a prefix until that prefix has been installed in hardware.
This will eliminate any temporary black holes due to a BGP speaker advertising reachability to a prefix that may not yet be installed into the forwarding plane.


---

## C

### campus

**Type**: String  
**Path**: `campus`  

PREVIEW: This option is marked as "preview", meaning the data models or generated configuration can change at any time.
Name of the Campus fabric.
Used to generate CloudVision device tags with the `generate_cv_tags.campus_fabric` feature.

---

### campus_access_pod

**Type**: String  
**Path**: `campus_access_pod`  

PREVIEW: This option is marked as "preview", meaning the data models or generated configuration can change at any time.
Name of the Campus access pod.
Used to generate CloudVision device tags with the `generate_cv_tags.campus_fabric` feature.

---

### campus_pod

**Type**: String  
**Path**: `campus_pod`  

PREVIEW: This option is marked as "preview", meaning the data models or generated configuration can change at any time.
Name of the Campus pod.
Used to generate CloudVision device tags with the `generate_cv_tags.campus_fabric` feature.

---

### channel_id_algorithm

**Type**: String  
**Path**: `core_interfaces.p2p_links_profiles.[].port_channel.channel_id_algorithm`  
**Default**: `first_port`  
**Valid Values**: `first_port`, `p2p_link_id`  

Configures how to derive the Port-Channel ID when not set.
By default the ID is derived from the first switch port in node_child_interfaces[].interfaces.
The `p2p_link_id` setting will use the `id` for each link plus the `channel_id_offset` to derive the Port-Channel ID.

---

### channel_id_algorithm

**Type**: String  
**Path**: `core_interfaces.p2p_links.[].port_channel.channel_id_algorithm`  
**Default**: `first_port`  
**Valid Values**: `first_port`, `p2p_link_id`  

Configures how to derive the Port-Channel ID when not set.
By default the ID is derived from the first switch port in node_child_interfaces[].interfaces.
The `p2p_link_id` setting will use the `id` for each link plus the `channel_id_offset` to derive the Port-Channel ID.

---

### channel_id_algorithm

**Type**: String  
**Path**: `l3_edge.p2p_links_profiles.[].port_channel.channel_id_algorithm`  
**Default**: `first_port`  
**Valid Values**: `first_port`, `p2p_link_id`  

Configures how to derive the Port-Channel ID when not set.
By default the ID is derived from the first switch port in node_child_interfaces[].interfaces.
The `p2p_link_id` setting will use the `id` for each link plus the `channel_id_offset` to derive the Port-Channel ID.

---

### channel_id_algorithm

**Type**: String  
**Path**: `l3_edge.p2p_links.[].port_channel.channel_id_algorithm`  
**Default**: `first_port`  
**Valid Values**: `first_port`, `p2p_link_id`  

Configures how to derive the Port-Channel ID when not set.
By default the ID is derived from the first switch port in node_child_interfaces[].interfaces.
The `p2p_link_id` setting will use the `id` for each link plus the `channel_id_offset` to derive the Port-Channel ID.

---

### compute_local_engineid_source

**Type**: String  
**Path**: `snmp_settings.compute_local_engineid_source`  
**Default**: `rfc3411_type5`  
**Valid Values**: `rfc3411_type5`, `rfc3411_type3`, `system_mac`, `hostname_and_ip`  

`compute_local_engineid_source` supports:
- `rfc3411_type5` use the value of `local_engineid_ip` to find the mgmt ip and calculate an RFC3411 compliant Engine ID based on 8000757105 + sha1(hostname + local_engineid_ip)
- `rfc3411_type3` generate an RFC3411 type 3 compliant Engine ID.
  To use this, `system_mac_address` MUST be set for the device.
  The formula is 8000757103 + system_mac_address.
- `system_mac` generate the Engine ID similar to the default EOS behavior.
  To use this, `system_mac_address` MUST be set for the device.
  The formula is f5717f + system_mac_address + 00.
- `hostname_and_ip` generate a local engineId for SNMP by hashing via SHA1 the string generated via the concatenation of the hostname plus the out-of-band management IP.
    sha1(hostname + mgmt_ip)
  `local_engineid_ip` does not have any effect when using `compute_local_engineid_source: hostname_and_ip`.
  Note that this is a legacy method kept for backward compatibility; it does not follow RFC 3411 and does not properly support in-band management.

---

### Connected Endpoints

**Type**: List, items: Dictionary  
**Path**: `<connected_endpoints_keys.key>`  

List of endpoint connected to the fabric.
This should be applied to group_vars or host_vars where endpoints are connecting.
`connected_endpoints_keys.key` is one of the keys under "connected_endpoints_keys".

---

### connected_endpoints

**Type**: List, items: Dictionary  
**Path**: `connected_endpoints`  

List of endpoint connected to the fabric.
This should be applied to group_vars or host_vars where endpoints are connecting.

---

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

### console

**Type**: String  
**Path**: `logging_settings.console`  
**Valid Values**: `debugging`, `informational`, `notifications`, `warnings`, `errors`, `critical`, `alerts`, `emergencies`, `disabled`  

Console logging severity level.

---

### Custom Connected Endpoints

**Type**: List, items: Dictionary  
**Path**: `<custom_connected_endpoints_keys.key>`  

List of endpoint connected to the fabric.
This should be applied to group_vars or host_vars where endpoints are connecting.
`connected_endpoints_keys.key` is one of the keys under "connected_endpoints_keys".

---

### Custom Node Types

**Type**: Dictionary  
**Path**: `<custom_node_type_keys.key>`  
---

### custom_connected_endpoints_keys

**Type**: List, items: Dictionary  
**Path**: `custom_connected_endpoints_keys`  

`custom_connected_endpoints_keys` offers a flexible way to extend endpoint definitions without altering the `connected_endpoints_keys`.
The values defined in `custom_connected_endpoints_keys`, are prepended to the ones in `connected_endpoint_keys`, taking precedence over any values in `connected_endpoint_keys`.
This approach helps preserving the default `connected_endpoints_keys`, unlike directly overriding it.

---

### custom_node_type_keys

**Type**: List, items: Dictionary  
**Path**: `custom_node_type_keys`  

Define Custom Node Type Keys, to specify the properties of each node type in the fabric.
This allows for complete customization of the fabric layout and functionality.
`custom_node_type_keys` should be defined in top level group_var for the fabric.
These values will be combined with the defaults; custom node type keys named the same as a
default node_type_key will replace the default.

---

### custom_platform_settings

**Type**: List, items: Dictionary  
**Path**: `custom_platform_settings`  

Custom Platform settings to override the default `platform_settings`. This list will be prepended to the list of `platform_settings`. The first entry found where the `platform` node setting is fully matched by any regex in the `platforms` list will be chosen. If no matches are found, the first entry containing a platform `default` will be chosen.

---

### custom_structured_configuration_list_merge

**Type**: String  
**Path**: `custom_structured_configuration_list_merge`  
**Default**: `append_rp`  
**Valid Values**: `replace`, `append`, `keep`, `prepend`, `append_rp`, `prepend_rp`  

The List-merge strategy used when merging custom structured configurations.

This applies to all vars prefixed by prefixes in `custom_structured_configuration_prefix`
and all data under the various `structured_config` options.

The available list merge strategies:
- `replace`:
  - Any list will be replaced with the list defined in custom structured configurations.
- `append`:
  - Existing list items with the same "Primary key"-value will be updated.
  - New items will be appended to the existing list (including duplicates).
- `keep`:
  - Only set list if there is no existing list or existing list is `None`.
- `prepend`:
  - Existing list items with the same "Primary key"-value will be updated.
  - New items will be prepended to the existing list (including duplicates).
- `append_rp`:
  - Existing list items with the same "Primary key"-value will be updated.
  - New unique items will be appended to the existing list.
- `prepend_rp`:
  - Existing list items with the same "Primary key"-value will be updated.
  - New unique items will be prepended to the existing list.


---

### custom_structured_configuration_prefix

**Type**: List, items: String  
**Path**: `custom_structured_configuration_prefix`  
**Default**: `See documentation`  

Custom EOS Structured Configuration keys can be set on any group or host_var level using the name
of the corresponding `eos_cli_config_gen` key prefixed with content of `custom_structured_configuration_prefix`.

The content of Custom Structured Configuration variables will be merged with the structured config generated by the eos_designs role.

The merge is done recursively, so it is possible to update a sub-key of a variable set by Arista AVD already.

The merge follow these recursive merge strategies:
- New keys will be added for all types.
- Existing keys of type "List" with a "Primary key" set in the schema:
  - Strategy can be changed with `custom_structured_configuration_list_merge`. Default strategy:
    - Existing list items with the same "Primary key"-value will be updated.
    - New unique items will be appended to the existing list
- Other keys of type "List" will have new unique items appended the the existing list.
- Existing keys of type "Dictionary" will recursively merge
- Other existing keys will be replaced.


---

### cv_pathfinder_global_sites

**Type**: List, items: Dictionary  
**Path**: `cv_pathfinder_global_sites`  

Define sites that are outside of the CV Pathfinder hierarchy.
This is used to arrange pathfinders in the CloudVision topology layout.

---

### cv_pathfinder_internet_exit_policies

**Type**: List, items: Dictionary  
**Path**: `cv_pathfinder_internet_exit_policies`  

PREVIEW: These keys are in preview mode.

List of internet-exit policies used for the WAN configuration.

---

### cv_pathfinder_regions

**Type**: List, items: Dictionary  
**Path**: `cv_pathfinder_regions`  

Define the CV Pathfinder hierarchy.

---

### cv_pathfinder_transit_mode

**Type**: String  
**Path**: `<node_type_keys.key>.defaults.cv_pathfinder_transit_mode`  
**Valid Values**: `region`, `zone`  

Configure the transit mode for a WAN client for CV Pathfinder designs
only when the `wan_mode` root key is set to `cv_pathfinder`.

'zone' is currently not supported.

---

### cv_pathfinder_transit_mode

**Type**: String  
**Path**: `<node_type_keys.key>.node_groups.[].nodes.[].cv_pathfinder_transit_mode`  
**Valid Values**: `region`, `zone`  

Configure the transit mode for a WAN client for CV Pathfinder designs
only when the `wan_mode` root key is set to `cv_pathfinder`.

'zone' is currently not supported.

---

### cv_pathfinder_transit_mode

**Type**: String  
**Path**: `<node_type_keys.key>.node_groups.[].cv_pathfinder_transit_mode`  
**Valid Values**: `region`, `zone`  

Configure the transit mode for a WAN client for CV Pathfinder designs
only when the `wan_mode` root key is set to `cv_pathfinder`.

'zone' is currently not supported.

---

### cv_pathfinder_transit_mode

**Type**: String  
**Path**: `<node_type_keys.key>.nodes.[].cv_pathfinder_transit_mode`  
**Valid Values**: `region`, `zone`  

Configure the transit mode for a WAN client for CV Pathfinder designs
only when the `wan_mode` root key is set to `cv_pathfinder`.

'zone' is currently not supported.

---

### cv_pathfinder_transit_mode

**Type**: String  
**Path**: `device_profiles.[].cv_pathfinder_transit_mode`  
**Valid Values**: `region`, `zone`  

Configure the transit mode for a WAN client for CV Pathfinder designs
only when the `wan_mode` root key is set to `cv_pathfinder`.

'zone' is currently not supported.

---

### cv_pathfinder_transit_mode

**Type**: String  
**Path**: `devices.[].cv_pathfinder_transit_mode`  
**Valid Values**: `region`, `zone`  

Configure the transit mode for a WAN client for CV Pathfinder designs
only when the `wan_mode` root key is set to `cv_pathfinder`.

'zone' is currently not supported.

---

### cv_server

**Type**: String  
**Path**: `cv_server`  

PREVIEW: These keys are in preview mode.

Hostname or IP address of CloudVision host. Ex. "www.arista.io" for CVaaS.
For AVD Design data models this variable is only used for the WAN Internet-exit integration with Zscaler.
The same variable name is also used by the `cv_deploy` role, and will override the value of `ansible_host` on inventory 'cloudvision' host.
Make sure to set it in a common group_vars file.

---

### cv_settings

**Type**: Dictionary  
**Path**: `cv_settings`  

Settings for CloudVision telemetry streaming and provisioning.

---

### cv_tags_topology_type

**Type**: String  
**Path**: `cv_tags_topology_type`  

Device type that CloudVision should use when generating the Topology like "leaf", "spine", "core", "edge" or "member-leaf". Defaults to the setting under node_type_keys.

---

### cv_token

**Type**: String  
**Path**: `cv_token`  

PREVIEW: These keys are in preview mode.

Service account token as defined on CloudVision. This value should be using Ansible Vault.
For AVD Design data models this variable is only used for the WAN Internet-exit integration with Zscaler.
The same variable name is also used by the `cv_deploy` role, and will override the value of `ansible_password` on inventory 'cloudvision' host.
Make sure to set it in a common group_vars file.

---

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

## D

### dc_name

**Type**: String  
**Path**: `dc_name`  

DC Name is used in:
- Fabric Documentation (Optional, falls back to fabric_name)
- SNMP Location: `snmp_settings.location` (Optional)
- HER Overlay DC scoped flood lists: `overlay_her_flood_list_scope: dc` (Required)


---

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

### default_evpn_encapsulation

**Type**: String  
**Path**: `custom_node_type_keys.[].default_evpn_encapsulation`  
**Default**: `vxlan`  
**Valid Values**: `mpls`, `vxlan`  

Set the default evpn encapsulation.


---

### default_evpn_encapsulation

**Type**: String  
**Path**: `node_type_keys.[].default_evpn_encapsulation`  
**Default**: `vxlan`  
**Valid Values**: `mpls`, `vxlan`  

Set the default evpn encapsulation.


---

### default_evpn_role

**Type**: String  
**Path**: `custom_node_type_keys.[].default_evpn_role`  
**Default**: `none`  
**Valid Values**: `none`, `client`, `server`  

Default evpn_role. Can be overridden in topology vars.

---

### default_evpn_role

**Type**: String  
**Path**: `node_type_keys.[].default_evpn_role`  
**Default**: `none`  
**Valid Values**: `none`, `client`, `server`  

Default evpn_role. Can be overridden in topology vars.

---

### default_flow_tracker_type

**Type**: String  
**Path**: `custom_node_type_keys.[].default_flow_tracker_type`  
**Default**: `sampled`  
**Valid Values**: `sampled`, `hardware`  

Set the default flow tracker type.

---

### default_flow_tracker_type

**Type**: String  
**Path**: `node_type_keys.[].default_flow_tracker_type`  
**Default**: `sampled`  
**Valid Values**: `sampled`, `hardware`  

Set the default flow tracker type.

---

### default_igmp_snooping_enabled

**Type**: Boolean  
**Path**: `default_igmp_snooping_enabled`  
**Default**: `True`  

When set to false, disables IGMP snooping at fabric level and overrides per vlan settings.


---

### default_interface_mtu

**Type**: Integer  
**Path**: `default_interface_mtu`  

Default interface MTU configured on EOS under "interface defaults".
Can be overridden per platform under platform settings.


---

### default_interfaces

**Type**: List, items: Dictionary  
**Path**: `default_interfaces`  

Default uplink, downlink, and MLAG interfaces, which will be used if these interfaces are not defined on a device (either directly or through inheritance).


---

### default_mgmt_method

**Type**: String  
**Path**: `default_mgmt_method`  
**Default**: `oob`  
**Valid Values**: `oob`, `inband`, `none`  

`default_mgmt_method` controls the default VRF and source interface used for the following management and monitoring protocols configured with AVD Design:
  - `aaa_settings`
  - `cv_settings`
  - `logging_settings`
  - `management_eapi`
  - `ntp_settings`
  - `sflow_settings`
  - `snmp_settings`
  - `ssh_settings`

`oob` means the protocols will be configured with the VRF set by `mgmt_interface_vrf` and `mgmt_interface` as the source interface.
`inband` means the protocols will be configured with the VRF set by `inband_mgmt_vrf` and `inband_mgmt_interface` as the source interface.
`none` means the VRF and or interface must be manually set for each protocol.
This can be overridden under the settings for each protocol.


---

### default_mpls_overlay_role

**Type**: String  
**Path**: `custom_node_type_keys.[].default_mpls_overlay_role`  
**Valid Values**: `client`, `server`, `none`  

Set the default mpls overlay role.
Acting role in overlay control plane.


---

### default_mpls_overlay_role

**Type**: String  
**Path**: `node_type_keys.[].default_mpls_overlay_role`  
**Valid Values**: `client`, `server`, `none`  

Set the default mpls overlay role.
Acting role in overlay control plane.


---

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

### default_node_types

**Type**: List, items: Dictionary  
**Path**: `default_node_types`  

Uses hostname matches against a regular expression to determine the node type.

---

### default_overlay_routing_protocol

**Type**: String  
**Path**: `custom_node_type_keys.[].default_overlay_routing_protocol`  
**Default**: `ebgp`  
**Valid Values**: `ebgp`, `ibgp`, `her`, `cvx`, `none`  

Set the default overlay routing_protocol.
Can be overridden by setting "overlay_routing_protocol" host/group_vars.


---

### default_overlay_routing_protocol

**Type**: String  
**Path**: `node_type_keys.[].default_overlay_routing_protocol`  
**Default**: `ebgp`  
**Valid Values**: `ebgp`, `ibgp`, `her`, `cvx`, `none`  

Set the default overlay routing_protocol.
Can be overridden by setting "overlay_routing_protocol" host/group_vars.


---

### default_underlay_p2p_ethernet_description

**Type**: String  
**Path**: `default_underlay_p2p_ethernet_description`  
**Default**: `P2P_{peer}_{peer_interface}{vrf?<_VRF_}`  

The default description or description template to be used on L3 point-to-point ethernet interfaces.
The interfaces using this are the routed uplinks and `p2p_links` defined under `l3_edge` or `core_interfaces`.
This can be a template using the AVD string formatter syntax: https://avd.arista.com/stable/ansible_collections/arista/avd/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.
The available template fields are:
  - `peer`: The name of the peer.
  - `interface`: The local interface name.
  - `peer_interface`: The interface on the peer.
  - `vrf`: The name of the VRF if set (Only applicable for `uplink_type: p2p-vrfs`).

By default the description is templated from the name and interface of the peer.

---

### default_underlay_p2p_port_channel_description

**Type**: String  
**Path**: `default_underlay_p2p_port_channel_description`  
**Default**: `P2P_{peer}_{peer_interface}`  

The default description or description template to be used on L3 point-to-point port-channel interfaces.
The port-channels using this are `p2p_links` defined under `l3_edge` or `core_interfaces`.
This can be a template using the AVD string formatter syntax: https://avd.arista.com/stable/ansible_collections/arista/avd/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.
The available template fields are:
  - `peer`: The name of the peer.
  - `interface`: The local interface name.
  - `peer_interface`: The interface on the peer.
  - `port_channel_id`: The local port-channel ID.
  - `peer_port_channel_id`: The ID of the port-channel on the peer.

By default the description is templated from the name and interface of the peer.

---

### default_underlay_routing_protocol

**Type**: String  
**Path**: `custom_node_type_keys.[].default_underlay_routing_protocol`  
**Default**: `ebgp`  
**Valid Values**: `ebgp`, `ospf`, `ospf-ldp`, `isis`, `isis-sr`, `isis-ldp`, `isis-sr-ldp`, `none`  

Set the default underlay routing_protocol.
Can be overridden by setting "underlay_routing_protocol" host/group_vars.


---

### default_underlay_routing_protocol

**Type**: String  
**Path**: `node_type_keys.[].default_underlay_routing_protocol`  
**Default**: `ebgp`  
**Valid Values**: `ebgp`, `ospf`, `ospf-ldp`, `isis`, `isis-sr`, `isis-ldp`, `isis-sr-ldp`, `none`  

Set the default underlay routing_protocol.
Can be overridden by setting "underlay_routing_protocol" host/group_vars.


---

### default_vrf_diag_loopback_description

**Type**: String  
**Path**: `default_vrf_diag_loopback_description`  
**Default**: `DIAG_VRF_{vrf}`  

The default description or description template to be used on VRF diagnostic loopback interfaces.
This can be a template using the AVD string formatter syntax: https://avd.arista.com/stable/ansible_collections/arista/avd/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.
The available template fields are:
  - `interface`: The Loopback interface name.
  - `vrf`: The VRF name.
  - `tenant`: The tenant name.

By default the description is templated from the VRF name.

---

### default_wan_role

**Type**: String  
**Path**: `custom_node_type_keys.[].default_wan_role`  
**Valid Values**: `client`, `server`  

Set the default WAN role.

This is used both for AutoVPN and Pathfinder designs.
That means if `wan_mode` root key is set to `legacy-autovpn` or `cv-pathfinder`.
`server` indicates that the router is a route-reflector.


---

### default_wan_role

**Type**: String  
**Path**: `node_type_keys.[].default_wan_role`  
**Valid Values**: `client`, `server`  

Set the default WAN role.

This is used both for AutoVPN and Pathfinder designs.
That means if `wan_mode` root key is set to `legacy-autovpn` or `cv-pathfinder`.
`server` indicates that the router is a route-reflector.


---

### delimiter

**Type**: String  
**Path**: `dot1x_settings.mac_based_authentication.username_format.delimiter`  
**Valid Values**: `colon`, `hyphen`, `none`, `period`  

RADIUS User-Name attribute delimiter to use on the MAC address.

---

### designated_forwarder_algorithm

**Type**: String  
**Path**: `<connected_endpoints_keys.key>.[].adapters.[].ethernet_segment.designated_forwarder_algorithm`  
**Valid Values**: `auto`, `modulus`, `preference`  

Configure DF algorithm and preferences.
- auto: Use preference-based algorithm and assign preference based on position of device in the 'switches' list,
  e.g., assuming a list of three switches, this would assign a preference of 200 to the first switch, 100 to the 2nd, and 0 to the third.
- preference: Set preference for each switch manually using designated_forwarder_preferences key.
- modulus: Use the default modulus-based algorithm.
If omitted, Port-Channels use the EOS default of modulus.
If omitted, Ethernet interfaces default to the 'auto' mechanism detailed above.


---

### designated_forwarder_algorithm

**Type**: String  
**Path**: `<custom_connected_endpoints_keys.key>.[].adapters.[].ethernet_segment.designated_forwarder_algorithm`  
**Valid Values**: `auto`, `modulus`, `preference`  

Configure DF algorithm and preferences.
- auto: Use preference-based algorithm and assign preference based on position of device in the 'switches' list,
  e.g., assuming a list of three switches, this would assign a preference of 200 to the first switch, 100 to the 2nd, and 0 to the third.
- preference: Set preference for each switch manually using designated_forwarder_preferences key.
- modulus: Use the default modulus-based algorithm.
If omitted, Port-Channels use the EOS default of modulus.
If omitted, Ethernet interfaces default to the 'auto' mechanism detailed above.


---

### designated_forwarder_algorithm

**Type**: String  
**Path**: `connected_endpoints.[].adapters.[].ethernet_segment.designated_forwarder_algorithm`  
**Valid Values**: `auto`, `modulus`, `preference`  

Configure DF algorithm and preferences.
- auto: Use preference-based algorithm and assign preference based on position of device in the 'switches' list,
  e.g., assuming a list of three switches, this would assign a preference of 200 to the first switch, 100 to the 2nd, and 0 to the third.
- preference: Set preference for each switch manually using designated_forwarder_preferences key.
- modulus: Use the default modulus-based algorithm.
If omitted, Port-Channels use the EOS default of modulus.
If omitted, Ethernet interfaces default to the 'auto' mechanism detailed above.


---

### designated_forwarder_algorithm

**Type**: String  
**Path**: `network_ports.[].ethernet_segment.designated_forwarder_algorithm`  
**Valid Values**: `auto`, `modulus`, `preference`  

Configure DF algorithm and preferences.
- auto: Use preference-based algorithm and assign preference based on position of device in the 'switches' list,
  e.g., assuming a list of three switches, this would assign a preference of 200 to the first switch, 100 to the 2nd, and 0 to the third.
- preference: Set preference for each switch manually using designated_forwarder_preferences key.
- modulus: Use the default modulus-based algorithm.
If omitted, Port-Channels use the EOS default of modulus.
If omitted, Ethernet interfaces default to the 'auto' mechanism detailed above.


---

### designated_forwarder_algorithm

**Type**: String  
**Path**: `port_profiles.[].ethernet_segment.designated_forwarder_algorithm`  
**Valid Values**: `auto`, `modulus`, `preference`  

Configure DF algorithm and preferences.
- auto: Use preference-based algorithm and assign preference based on position of device in the 'switches' list,
  e.g., assuming a list of three switches, this would assign a preference of 200 to the first switch, 100 to the 2nd, and 0 to the third.
- preference: Set preference for each switch manually using designated_forwarder_preferences key.
- modulus: Use the default modulus-based algorithm.
If omitted, Port-Channels use the EOS default of modulus.
If omitted, Ethernet interfaces default to the 'auto' mechanism detailed above.


---

### destination_ports_match

**Type**: String  
**Path**: `ipv4_acls.[].entries.[].destination_ports_match`  
**Default**: `eq`  
**Valid Values**: `eq`, `gt`, `lt`, `neq`, `range`  
---

### device_profile

**Type**: String  
**Path**: `device_profile`  

PREVIEW - This datamodel is still under development and may change or get removed at any time.
Inherit settings from a device profile defined under `device_profiles`.
If the device is defined under `devices` it is recommended to set the `profile` there instead.
Max two levels of profile inheritance: device -> profile -> parent_profile

---

### device_profiles

**Type**: List, items: Dictionary  
**Path**: `device_profiles`  

PREVIEW - This datamodel is still under development and may change or get removed at any time.

---

### devices

**Type**: List, items: Dictionary  
**Path**: `devices`  

PREVIEW - This datamodel is still under development and may change or get removed at any time.

---

### digital_twin

**Type**: Dictionary  
**Path**: `digital_twin`  

PREVIEW: This option is marked as "preview", meaning the data models or generated configuration can change at any time.
Global settings to configure the Digital Twin of the Fabric.

---

### direction

**Type**: String  
**Path**: `<connected_endpoints_keys.key>.[].adapters.[].monitor_sessions.[].source_settings.direction`  
**Valid Values**: `rx`, `tx`, `both`  
---

### direction

**Type**: String  
**Path**: `<custom_connected_endpoints_keys.key>.[].adapters.[].monitor_sessions.[].source_settings.direction`  
**Valid Values**: `rx`, `tx`, `both`  
---

### direction

**Type**: String  
**Path**: `<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].monitor_sessions.[].source_settings.direction`  
**Valid Values**: `rx`, `tx`, `both`  
---

### direction

**Type**: String  
**Path**: `connected_endpoints.[].adapters.[].monitor_sessions.[].source_settings.direction`  
**Valid Values**: `rx`, `tx`, `both`  
---

### direction

**Type**: String  
**Path**: `hardware_counters.features.[].direction`  
**Valid Values**: `in`, `out`, `cpu`  

Most features support only 'in' and 'out'. Some like traffic-policy support 'cpu'.
Some features DO NOT have any direction.
This validation IS NOT made by the schemas.


---

### direction

**Type**: String  
**Path**: `network_ports.[].monitor_sessions.[].source_settings.direction`  
**Valid Values**: `rx`, `tx`, `both`  
---

### direction

**Type**: String  
**Path**: `port_profiles.[].monitor_sessions.[].source_settings.direction`  
**Valid Values**: `rx`, `tx`, `both`  
---

### dns_settings

**Type**: Dictionary  
**Path**: `dns_settings`  

DNS settings

---

### dot1x_settings

**Type**: Dictionary  
**Path**: `dot1x_settings`  

Settings for 802.1X deployments.

---

## E

### eap_response

**Type**: String  
**Path**: `<connected_endpoints_keys.key>.[].adapters.[].dot1x.aaa.unresponsive.eap_response`  
**Valid Values**: `success`, `disabled`  

EAP response to send. EOS default is `success`.

---

### eap_response

**Type**: String  
**Path**: `<custom_connected_endpoints_keys.key>.[].adapters.[].dot1x.aaa.unresponsive.eap_response`  
**Valid Values**: `success`, `disabled`  

EAP response to send. EOS default is `success`.

---

### eap_response

**Type**: String  
**Path**: `connected_endpoints.[].adapters.[].dot1x.aaa.unresponsive.eap_response`  
**Valid Values**: `success`, `disabled`  

EAP response to send. EOS default is `success`.

---

### eap_response

**Type**: String  
**Path**: `network_ports.[].dot1x.aaa.unresponsive.eap_response`  
**Valid Values**: `success`, `disabled`  

EAP response to send. EOS default is `success`.

---

### eap_response

**Type**: String  
**Path**: `port_profiles.[].dot1x.aaa.unresponsive.eap_response`  
**Valid Values**: `success`, `disabled`  

EAP response to send. EOS default is `success`.

---

### enable_trunk_groups

**Type**: Boolean  
**Path**: `enable_trunk_groups`  
**Default**: `False`  

Enable Trunk Group support across eos_designs.
Warning: Because of the nature of the EOS Trunk Group feature, enabling this is "all or nothing".
*All* vlans and *all* trunks towards connected endpoints must be using trunk groups as well.
If trunk groups are not assigned to a trunk, no vlans will be enabled on that trunk.
See "Details on enable_trunk_groups" below before enabling this feature.


---

### endpoint_role

**Type**: String  
**Path**: `<connected_endpoints_keys.key>.[].adapters.[].ptp.endpoint_role`  
**Default**: `follower`  
**Valid Values**: `follower`, `dynamic`, `bmca`, `default`  

PTP role of the endpoint.
`follower` will configure the switch port as `ptp role master`.
`dynamic` will use BMCA.
`default` is deprecated in favor of `follower`.
`bmca` is deprecated in favor of `dynamic`.

---

### endpoint_role

**Type**: String  
**Path**: `<custom_connected_endpoints_keys.key>.[].adapters.[].ptp.endpoint_role`  
**Default**: `follower`  
**Valid Values**: `follower`, `dynamic`, `bmca`, `default`  

PTP role of the endpoint.
`follower` will configure the switch port as `ptp role master`.
`dynamic` will use BMCA.
`default` is deprecated in favor of `follower`.
`bmca` is deprecated in favor of `dynamic`.

---

### endpoint_role

**Type**: String  
**Path**: `connected_endpoints.[].adapters.[].ptp.endpoint_role`  
**Default**: `follower`  
**Valid Values**: `follower`, `dynamic`, `bmca`, `default`  

PTP role of the endpoint.
`follower` will configure the switch port as `ptp role master`.
`dynamic` will use BMCA.
`default` is deprecated in favor of `follower`.
`bmca` is deprecated in favor of `dynamic`.

---

### endpoint_role

**Type**: String  
**Path**: `network_ports.[].ptp.endpoint_role`  
**Default**: `follower`  
**Valid Values**: `follower`, `dynamic`, `bmca`, `default`  

PTP role of the endpoint.
`follower` will configure the switch port as `ptp role master`.
`dynamic` will use BMCA.
`default` is deprecated in favor of `follower`.
`bmca` is deprecated in favor of `dynamic`.

---

### endpoint_role

**Type**: String  
**Path**: `port_profiles.[].ptp.endpoint_role`  
**Default**: `follower`  
**Valid Values**: `follower`, `dynamic`, `bmca`, `default`  

PTP role of the endpoint.
`follower` will configure the switch port as `ptp role master`.
`dynamic` will use BMCA.
`default` is deprecated in favor of `follower`.
`bmca` is deprecated in favor of `dynamic`.

---

### environment

**Type**: String  
**Path**: `digital_twin.environment`  
**Default**: `act`  
**Valid Values**: `act`  

Targeted Digital Twin environment.

---

### eos_designs_documentation

**Type**: Dictionary  
**Path**: `eos_designs_documentation`  

Control fabric documentation generation.


---

### event_handlers

**Type**: List, items: Dictionary  
**Path**: `event_handlers`  

Gives the ability to monitor and react to Syslog messages.
Event Handlers provide a powerful and flexible tool that can be used to apply self-healing actions,
customize the system behavior, and implement workarounds to problems discovered in the field.


---

### evpn_ebgp_gateway_multihop

**Type**: Integer  
**Path**: `evpn_ebgp_gateway_multihop`  
**Default**: `15`  

Default of 15, considering a large value to avoid BGP reachability issues in very complex DCI networks.
Adapt the value for your specific topology.


---

### evpn_ebgp_multihop

**Type**: Integer  
**Path**: `evpn_ebgp_multihop`  
**Default**: `3`  

Default of 3, the recommended value for a 3 stage spine and leaf topology.
Set to a higher value to allow for very large and complex topologies.


---

### evpn_import_pruning

**Type**: Boolean  
**Path**: `evpn_import_pruning`  
**Default**: `False`  

Enable VPN import pruning (Min. EOS 4.24.2F).
The Route Target extended communities carried by incoming VPN paths will be examined.
If none of those Route Targets have been configured for import, the path will be immediately discarded.


---

### evpn_multicast

**Type**: Boolean  
**Path**: `evpn_multicast`  
**Default**: `False`  

General Configuration required for EVPN Multicast. "evpn_l2_multicast" or "evpn_l3_multicast" must also be configured under the Network Services (tenants).
Requires `underlay_multicast_pim_sm: true` and IGMP snooping enabled globally (default).
For MLAG devices Route Distinguisher must be unique since this feature will create multi-vtep configuration.
Warning !!! For Trident3 based platforms i.e 7050X3, 7300X3, 720XP.
  The Following default platform setting will be configured on 7050X3 and 7300X3: "platform trident forwarding-table partition flexible exact-match 16384 l2-shared 98304 l3-shared 131072"
  The Following default platform setting will be configured on 720XP: "flexible exact-match 16000 l2-shared 18000 l3-shared 22000"
  All forwarding agents will be restarted when this configuration is applied.
  You can tune the settings by overriding the default variable: "platform_settings[platforms].trident_forwarding_table_partition:"
  Please contact an Arista representative for help with determining the appropriate values for your environment.

---

### evpn_overlay_bgp_rtc

**Type**: Boolean  
**Path**: `evpn_overlay_bgp_rtc`  
**Default**: `False`  

Enable Route Target Membership Constraint Address Family on EVPN overlay BGP peerings (Min. EOS 4.25.1F).
Requires use eBGP as overlay protocol.


---

### evpn_prevent_readvertise_to_server

**Type**: Boolean  
**Path**: `evpn_prevent_readvertise_to_server`  
**Default**: `False`  

Prevent sending EVPN BGP updates to the route-server if they came from or passed through the route-server already.
Refer to `evpn_prevent_readvertise_to_server_mode` to control which configuration style to use.
This is very useful in large-scale networks, where convergence will be quicker by not returning all updates received
from Route-server-1 to Router-server-2 just for Route-server-2 to throw them away because of AS Path loop detection.


---

### evpn_prevent_readvertise_to_server_mode

**Type**: String  
**Path**: `evpn_prevent_readvertise_to_server_mode`  
**Default**: `as_path_acl`  
**Valid Values**: `source_peer_asn`, `as_path_acl`  

`evpn_prevent_readvertise_to_server_mode` controls the method of identifying EVPN routes that should not be advertised to the EVPN route-servers.
Only used when `evpn_prevent_readvertise_to_server` is set to `true`.
`source_peer_asn` mode configures an outbound route-map towards EVPN route-servers which filter out BGP updates learned directly from the ASN of the route-server. This mode will still allow routes learned via any other peer, even if they have the route-server's ASN in the AS-path.
`as_path_acl` mode configures an outbound route-map and as-path access-list which filters out BGP updates with the route-server ASN anywhere in the AS-path.


---

### evpn_role

**Type**: String  
**Path**: `<node_type_keys.key>.defaults.evpn_role`  
**Valid Values**: `client`, `server`, `none`  

Acting role in EVPN control plane.
Default is set in node_type definition from node_type_keys.


---

### evpn_role

**Type**: String  
**Path**: `<node_type_keys.key>.node_groups.[].nodes.[].evpn_role`  
**Valid Values**: `client`, `server`, `none`  

Acting role in EVPN control plane.
Default is set in node_type definition from node_type_keys.


---

### evpn_role

**Type**: String  
**Path**: `<node_type_keys.key>.node_groups.[].evpn_role`  
**Valid Values**: `client`, `server`, `none`  

Acting role in EVPN control plane.
Default is set in node_type definition from node_type_keys.


---

### evpn_role

**Type**: String  
**Path**: `<node_type_keys.key>.nodes.[].evpn_role`  
**Valid Values**: `client`, `server`, `none`  

Acting role in EVPN control plane.
Default is set in node_type definition from node_type_keys.


---

### evpn_role

**Type**: String  
**Path**: `device_profiles.[].evpn_role`  
**Valid Values**: `client`, `server`, `none`  

Acting role in EVPN control plane.
Default is set in node_type definition from node_type_keys.


---

### evpn_role

**Type**: String  
**Path**: `devices.[].evpn_role`  
**Valid Values**: `client`, `server`, `none`  

Acting role in EVPN control plane.
Default is set in node_type definition from node_type_keys.


---

### evpn_short_esi_prefix

**Type**: String  
**Path**: `evpn_short_esi_prefix`  
**Default**: `0000:0000:`  

Configure prefix for "short_esi" values.

---

### evpn_vlan_aware_bundles

**Type**: Boolean  
**Path**: `evpn_vlan_aware_bundles`  
**Default**: `False`  

Enable VLAN aware bundles for every EVPN MAC-VRF.
If set to `true` all SVIs in a VRF are configured in a vlan-aware-bundle using the VRF name as the bundle name. `l2vlans` are bundled in vlan-aware-bundles using the VLAN name as the bundle name.

The `evpn_vlan_bundle` option under SVI, L2VLAN, VRF or tenant level takes precedence and overrides this behavior. Per SVI/L2VLAN `evpn_vlan_bundle` also works when this setting is disabled which allow mixing vlan-aware-bundles with regular MAC-VRFs.

---

## F

### fabric_evpn_encapsulation

**Type**: String  
**Path**: `fabric_evpn_encapsulation`  
**Valid Values**: `vxlan`, `mpls`  

Should be set to mpls for evpn-mpls scenario. This overrides the evpn_encapsulation setting under node_type_keys.

---

### fabric_flow_tracking

**Type**: Dictionary  
**Path**: `fabric_flow_tracking`  

Default enabling of flow-tracking(IPFIX) for various interface types across the fabric.
Flow Tracking can also be enabled/disabled under each of the specific data models.
For general flow-tracking settings see `flow_tracking_settings`.

---

### fabric_name

**Type**: String  
**Path**: `fabric_name`  

Fabric Name, required to match Ansible Group name covering all devices in the Fabric, **must** be an inventory group name.

---

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

### fabric_sflow

**Type**: Dictionary  
**Path**: `fabric_sflow`  

Default enabling of sFlow for various interface types across the fabric.
sFlow can also be enabled/disabled under each of the specific data models.
For general sFlow settings see `sflow_settings`.

---

### facility

**Type**: String  
**Path**: `logging_settings.facility`  
**Valid Values**: `auth`, `cron`, `daemon`, `kern`, `local0`, `local1`, `local2`, `local3`, `local4`, `local5`, `local6`, `local7`, `lpr`, `mail`, `news`, `sys9`, `sys10`, `sys11`, `sys12`, `sys13`, `sys14`, `syslog`, `user`, `uucp`  
---

### flow_tracker_type

**Type**: String  
**Path**: `<node_type_keys.key>.defaults.flow_tracker_type`  
**Valid Values**: `sampled`, `hardware`  

Set the flow tracker type.
Override the `default_flow_tracker_type` set at the `node_type_key` level.
`default_flow_tracker_type` default value is `sampled`.

---

### flow_tracker_type

**Type**: String  
**Path**: `<node_type_keys.key>.node_groups.[].nodes.[].flow_tracker_type`  
**Valid Values**: `sampled`, `hardware`  

Set the flow tracker type.
Override the `default_flow_tracker_type` set at the `node_type_key` level.
`default_flow_tracker_type` default value is `sampled`.

---

### flow_tracker_type

**Type**: String  
**Path**: `<node_type_keys.key>.node_groups.[].flow_tracker_type`  
**Valid Values**: `sampled`, `hardware`  

Set the flow tracker type.
Override the `default_flow_tracker_type` set at the `node_type_key` level.
`default_flow_tracker_type` default value is `sampled`.

---

### flow_tracker_type

**Type**: String  
**Path**: `<node_type_keys.key>.nodes.[].flow_tracker_type`  
**Valid Values**: `sampled`, `hardware`  

Set the flow tracker type.
Override the `default_flow_tracker_type` set at the `node_type_key` level.
`default_flow_tracker_type` default value is `sampled`.

---

### flow_tracker_type

**Type**: String  
**Path**: `device_profiles.[].flow_tracker_type`  
**Valid Values**: `sampled`, `hardware`  

Set the flow tracker type.
Override the `default_flow_tracker_type` set at the `node_type_key` level.
`default_flow_tracker_type` default value is `sampled`.

---

### flow_tracker_type

**Type**: String  
**Path**: `devices.[].flow_tracker_type`  
**Valid Values**: `sampled`, `hardware`  

Set the flow tracker type.
Override the `default_flow_tracker_type` set at the `node_type_key` level.
`default_flow_tracker_type` default value is `sampled`.

---

### flow_tracking_settings

**Type**: Dictionary  
**Path**: `flow_tracking_settings`  

Define the flow tracking parameters for this topology.

---

## G

### generate_cv_tags

**Type**: Dictionary  
**Path**: `generate_cv_tags`  

Generate CloudVision Tags based on AVD data.

---

## H

### hash_algorithm

**Type**: String  
**Path**: `<network_services_keys.name>.[].bgp_peer_groups.[].shared_secret.hash_algorithm`  
**Valid Values**: `aes-128-cmac-96`, `hmac-sha-256`, `hmac-sha1-96`  

Note: Algorithm hmac-sha-256 requires EOS version 4.31.1F and above.

---

### hash_algorithm

**Type**: String  
**Path**: `<network_services_keys.name>.[].vrfs.[].ospf.message_digest_keys.[].hash_algorithm`  
**Default**: `sha512`  
**Valid Values**: `md5`, `sha1`, `sha256`, `sha384`, `sha512`  
---

### hash_algorithm

**Type**: String  
**Path**: `<network_services_keys.name>.[].vrfs.[].svis.[].nodes.[].ospf.message_digest_keys.[].hash_algorithm`  
**Default**: `sha512`  
**Valid Values**: `md5`, `sha1`, `sha256`, `sha384`, `sha512`  
---

### hash_algorithm

**Type**: String  
**Path**: `<network_services_keys.name>.[].vrfs.[].svis.[].ospf.message_digest_keys.[].hash_algorithm`  
**Default**: `sha512`  
**Valid Values**: `md5`, `sha1`, `sha256`, `sha384`, `sha512`  
---

### hash_algorithm

**Type**: String  
**Path**: `<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].ospf.message_digest_keys.[].hash_algorithm`  
**Default**: `sha512`  
**Valid Values**: `md5`, `sha1`, `sha256`, `sha384`, `sha512`  
---

### hash_algorithm

**Type**: String  
**Path**: `<network_services_keys.name>.[].vrfs.[].l3_port_channels.[].ospf.message_digest_keys.[].hash_algorithm`  
**Default**: `sha512`  
**Valid Values**: `md5`, `sha1`, `sha256`, `sha384`, `sha512`  
---

### hash_algorithm

**Type**: String  
**Path**: `<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].shared_secret.hash_algorithm`  
**Valid Values**: `aes-128-cmac-96`, `hmac-sha-256`, `hmac-sha1-96`  

Note: Algorithm hmac-sha-256 requires EOS version 4.31.1F and above.

---

### hash_algorithm

**Type**: String  
**Path**: `ntp_settings.authentication_keys.[].hash_algorithm`  
**Valid Values**: `md5`, `sha1`  
---

### hash_algorithm

**Type**: String  
**Path**: `svi_profiles.[].nodes.[].ospf.message_digest_keys.[].hash_algorithm`  
**Default**: `sha512`  
**Valid Values**: `md5`, `sha1`, `sha256`, `sha384`, `sha512`  
---

### hash_algorithm

**Type**: String  
**Path**: `svi_profiles.[].ospf.message_digest_keys.[].hash_algorithm`  
**Default**: `sha512`  
**Valid Values**: `md5`, `sha1`, `sha256`, `sha384`, `sha512`  
---

### hash_algorithm

**Type**: String  
**Path**: `underlay_ospf_authentication.message_digest_keys.[].hash_algorithm`  
**Default**: `sha512`  
**Valid Values**: `md5`, `sha1`, `sha256`, `sha384`, `sha512`  
---

### hostname

**Type**: String  
**Path**: `logging_settings.format.hostname`  
**Valid Values**: `fqdn`, `ipv4`  

Hostname format in syslogs. For hostname _only_, remove the line. (default EOS CLI behaviour).

---

## I

### inband_ztp_bootstrap_file

**Type**: String  
**Path**: `inband_ztp_bootstrap_file`  

Bootstrap URL configured in DHCP to use for inband ZTP.
By default the URL will be `https://<first cv server>/ztp/bootstrap` if `cv_settings` are used.
Otherwise no value will be configured.

---

### internal_vlan_order

**Type**: Dictionary  
**Path**: `internal_vlan_order`  
**Default**: `See documentation`  

Internal vlan allocation order and range.

---

### ipsec_settings

**Type**: Dictionary  
**Path**: `ipsec_settings`  

Settings applicable to all IPsec connections.

---

### ipv4_acls

**Type**: List, items: Dictionary  
**Path**: `ipv4_acls`  

IPv4 extended access-lists supporting substitution on certain fields.
These access-lists can be referenced under node settings `l3_interfaces`, and will only be configured on devices where they are in use.

The substitution is useful when assigning the same access-list on multiple interfaces,
but where certain fields require unique values like the "interface_ip" or "peer_ip".
When using substitution, the interface name will be appended to the ACL name.

---

### ipv4_prefix_list_catalog

**Type**: List, items: Dictionary  
**Path**: `ipv4_prefix_list_catalog`  

IPv4 prefix-list catalog.
Note: Entries defined in `ipv4_prefix_list_catalog` are only rendered in the configuration when
they are explicitly referenced in one of the following node config keys:
- `l3_interfaces.[].bgp.ipv4_prefix_list_in`
- `l3_interfaces.[].bgp.ipv4_prefix_list_out`
- `l3_port_channels.[].bgp.ipv4_prefix_list_in`
- `l3_port_channels.[].bgp.ipv4_prefix_list_out`.

---

### ipv6_mgmt_destination_networks

**Type**: List, items: String  
**Path**: `ipv6_mgmt_destination_networks`  

List of IPv6 prefixes to configure as static routes towards the OOB IPv6 Management interface gateway.
Replaces the default route.


---

### ipv6_mgmt_gateway

**Type**: String  
**Path**: `ipv6_mgmt_gateway`  

OOB Management interface gateway in IPv6 format.
Used as next-hop for default gateway or static routes defined under 'ipv6_mgmt_destination_networks'.


---

### ipv6_prefix_length

**Type**: Integer  
**Path**: `fabric_ip_addressing.loopback.ipv6_prefix_length`  
**Default**: `128`  
**Valid Values**: `64`, `128`  

IPv6 prefix length used for Router ID, VTEP and diagnostic loopbacks.

---

### is_deployed

**Type**: Boolean  
**Path**: `is_deployed`  
**Default**: `True`  

If the device is already deployed in the fabric.
When set to false:
  - The `cv_deploy` role will not apply configurations to this device.
  - Peer interfaces toward this device may be shutdown based on the `shutdown_interfaces_towards_undeployed_peers` setting.
  - BGP peerings toward this device may be shutdown based on the `shutdown_bgp_towards_undeployed_peers` setting.
  - Validation tests by the `anta_runner` role are automatically skipped for this device.

---

### is_type

**Type**: String  
**Path**: `<node_type_keys.key>.defaults.is_type`  
**Valid Values**: `level-1-2`, `level-1`, `level-2`  

Overrides `isis_default_is_type`.

---

### is_type

**Type**: String  
**Path**: `<node_type_keys.key>.node_groups.[].nodes.[].is_type`  
**Valid Values**: `level-1-2`, `level-1`, `level-2`  

Overrides `isis_default_is_type`.

---

### is_type

**Type**: String  
**Path**: `<node_type_keys.key>.node_groups.[].is_type`  
**Valid Values**: `level-1-2`, `level-1`, `level-2`  

Overrides `isis_default_is_type`.

---

### is_type

**Type**: String  
**Path**: `<node_type_keys.key>.nodes.[].is_type`  
**Valid Values**: `level-1-2`, `level-1`, `level-2`  

Overrides `isis_default_is_type`.

---

### is_type

**Type**: String  
**Path**: `device_profiles.[].is_type`  
**Valid Values**: `level-1-2`, `level-1`, `level-2`  

Overrides `isis_default_is_type`.

---

### is_type

**Type**: String  
**Path**: `devices.[].is_type`  
**Valid Values**: `level-1-2`, `level-1`, `level-2`  

Overrides `isis_default_is_type`.

---

### ISIS Default IS System-ID format

**Type**: String  
**Path**: `isis_system_id_format`  
**Default**: `underlay_loopback`  
**Valid Values**: `node_id`, `underlay_loopback`  

Configures source for the system-id within the ISIS net id.
If this key is set to `node_id`, the fields `id` and `isis_system_id_prefix` configured under the node attributes are used to generate the system-id.
If `underlay_loopback` is selected then all node `isis_system_id_prefix` settings will be ignored and the loopback address will be used to generate the system-id.

---

### ISIS Default IS Type

**Type**: String  
**Path**: `isis_default_is_type`  
**Default**: `level-2`  
**Valid Values**: `level-1-2`, `level-1`, `level-2`  
---

### isis_authentication_mode

**Type**: String  
**Path**: `core_interfaces.p2p_links_profiles.[].isis_authentication_mode`  
**Valid Values**: `md5`, `text`  
---

### isis_authentication_mode

**Type**: String  
**Path**: `core_interfaces.p2p_links.[].isis_authentication_mode`  
**Valid Values**: `md5`, `text`  
---

### isis_authentication_mode

**Type**: String  
**Path**: `l3_edge.p2p_links_profiles.[].isis_authentication_mode`  
**Valid Values**: `md5`, `text`  
---

### isis_authentication_mode

**Type**: String  
**Path**: `l3_edge.p2p_links.[].isis_authentication_mode`  
**Valid Values**: `md5`, `text`  
---

### isis_circuit_type

**Type**: String  
**Path**: `core_interfaces.p2p_links_profiles.[].isis_circuit_type`  
**Valid Values**: `level-1`, `level-2`, `level-1-2`  
---

### isis_circuit_type

**Type**: String  
**Path**: `core_interfaces.p2p_links.[].isis_circuit_type`  
**Valid Values**: `level-1`, `level-2`, `level-1-2`  
---

### isis_circuit_type

**Type**: String  
**Path**: `l3_edge.p2p_links_profiles.[].isis_circuit_type`  
**Valid Values**: `level-1`, `level-2`, `level-1-2`  
---

### isis_circuit_type

**Type**: String  
**Path**: `l3_edge.p2p_links.[].isis_circuit_type`  
**Valid Values**: `level-1`, `level-2`, `level-1-2`  
---

### isis_default_circuit_type

**Type**: String  
**Path**: `isis_default_circuit_type`  
**Default**: `level-2`  
**Valid Values**: `level-1-2`, `level-1`, `level-2`  

These fabric level parameters can be used with core_interfaces running ISIS, and may be overridden on link profile or link level.


---

### isis_default_metric

**Type**: Integer  
**Path**: `isis_default_metric`  
**Default**: `50`  

These fabric level parameters can be used with core_interfaces running ISIS, and may be overridden at link profile or link level.


---

### isis_maximum_paths

**Type**: Integer  
**Path**: `isis_maximum_paths`  
**Default**: `4`  

Number of path to configure in ECMP for ISIS.

---

### isis_network_type

**Type**: String  
**Path**: `core_interfaces.p2p_links_profiles.[].isis_network_type`  
**Default**: `point-to-point`  
**Valid Values**: `point-to-point`, `broadcast`  
---

### isis_network_type

**Type**: String  
**Path**: `core_interfaces.p2p_links.[].isis_network_type`  
**Default**: `point-to-point`  
**Valid Values**: `point-to-point`, `broadcast`  
---

### isis_network_type

**Type**: String  
**Path**: `l3_edge.p2p_links_profiles.[].isis_network_type`  
**Default**: `point-to-point`  
**Valid Values**: `point-to-point`, `broadcast`  
---

### isis_network_type

**Type**: String  
**Path**: `l3_edge.p2p_links.[].isis_network_type`  
**Default**: `point-to-point`  
**Valid Values**: `point-to-point`, `broadcast`  
---

## K

### key_type

**Type**: String  
**Path**: `ntp_settings.authentication_keys.[].key_type`  
**Valid Values**: `0`, `7`, `8a`  

Key type of the `key`.
Does not have any influence on `cleartext_key`.

---

## L

### l2vlan_profiles

**Type**: List, items: Dictionary  
**Path**: `l2vlan_profiles`  

Profiles to inherit common settings for l2vlans defined under the network_services key.

---

### l3_interface_profiles

**Type**: List, items: Dictionary  
**Path**: `l3_interface_profiles`  

Profiles to inherit common settings for l3_interfaces defined under the node type key.
These profiles will *not* work for `l3_interfaces` defined under `vrfs`.

---

### letter_case

**Type**: String  
**Path**: `dot1x_settings.mac_based_authentication.username_format.letter_case`  
**Valid Values**: `lowercase`, `uppercase`  

RADIUS User-Name attribute letter case to use on the MAC address.

---

### level

**Type**: String  
**Path**: `logging_settings.buffered.level`  
**Valid Values**: `alerts`, `critical`, `debugging`, `emergencies`, `errors`, `informational`, `notifications`, `warnings`, `disabled`  

Buffer logging severity level.

---

### level

**Type**: String  
**Path**: `logging_settings.synchronous.level`  
**Default**: `critical`  
**Valid Values**: `alerts`, `all`, `critical`, `debugging`, `emergencies`, `errors`, `informational`, `notifications`, `warnings`, `disabled`  

Synchronous logging severity level.

---

### logging_settings

**Type**: Dictionary  
**Path**: `logging_settings`  

Logging settings

---

## M

### management_eapi

**Type**: Dictionary  
**Path**: `management_eapi`  

Default is HTTPS management eAPI enabled.


---

### method

**Type**: String  
**Path**: `aaa_settings.accounting.exec.console.methods.[].method`  
**Valid Values**: `logging`, `group`  
---

### method

**Type**: String  
**Path**: `aaa_settings.accounting.exec.default.methods.[].method`  
**Valid Values**: `logging`, `group`  
---

### method

**Type**: String  
**Path**: `aaa_settings.accounting.system.default.methods.[].method`  
**Valid Values**: `logging`, `group`  
---

### method

**Type**: String  
**Path**: `aaa_settings.accounting.commands.console.[].methods.[].method`  
**Valid Values**: `logging`, `group`  
---

### method

**Type**: String  
**Path**: `aaa_settings.accounting.commands.default.[].methods.[].method`  
**Valid Values**: `logging`, `group`  
---

### mgmt_destination_networks

**Type**: List, items: String  
**Path**: `mgmt_destination_networks`  

List of IPv4 prefixes to configure as static routes towards the OOB Management interface gateway.
Replaces the default route.

---

### mgmt_gateway

**Type**: String  
**Path**: `mgmt_gateway`  

OOB Management interface gateway in IPv4 format.
Used as next-hop for default gateway or static routes defined under 'mgmt_destination_networks'.


---

### mgmt_interface

**Type**: String  
**Path**: `mgmt_interface`  
**Default**: `Management1`  

OOB Management interface.

---

### mgmt_interface_description

**Type**: String  
**Path**: `mgmt_interface_description`  
**Default**: `OOB_MANAGEMENT`  

Management interface description.


---

### mgmt_interface_vrf

**Type**: String  
**Path**: `mgmt_interface_vrf`  
**Default**: `MGMT`  

OOB Management VRF.

---

### mgmt_vrf_routing

**Type**: Boolean  
**Path**: `mgmt_vrf_routing`  
**Default**: `False`  

Configure IP routing for the OOB Management VRF.

---

### mlag_bgp_peer_description

**Type**: String  
**Path**: `mlag_bgp_peer_description`  
**Default**: `{mlag_peer}_{peer_interface}`  

Description or description template to be used on the MLAG BGP peers including those in VRFs.
This can be a template using the AVD string formatter syntax: https://avd.arista.com/stable/ansible_collections/arista/avd/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.
The available template fields are:
  - `mlag_peer`: The name of the MLAG peer.
  - `interface`: The local MLAG L3 VLAN interface.
  - `peer_interface`: The MLAG L3 VLAN interface on the MLAG peer.
  - `vrf`: The name of the VRF. Not available for the underlay peering.

The default description is built from the name and interface of the MLAG peer and optionally the VRF.

---

### mlag_bgp_peer_group_description

**Type**: String  
**Path**: `mlag_bgp_peer_group_description`  
**Default**: `{mlag_peer}`  

Description or description template to be used on the MLAG BGP peer-group.
This can be a template using the AVD string formatter syntax: https://avd.arista.com/stable/ansible_collections/arista/avd/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.
The available template fields are:
  - `mlag_peer`: The name of the MLAG peer.

The default description is the name of the MLAG peers.

---

### mlag_ibgp_peering_vrfs

**Type**: Dictionary  
**Path**: `mlag_ibgp_peering_vrfs`  

On mlag leafs, an SVI interface is defined per vrf, to establish iBGP peering (required when there are MLAG leafs in topology).
The SVI id will be derived from the base vlan defined: mlag_ibgp_peering_vrfs.base_vlan + (vrf_id or vrf_vni) - 1.
Depending on the values of vrf_id / vrf_vni it may be required to adjust the base_vlan to avoid overlaps or invalid vlan ids.
The SVI ip address derived from mlag_l3_peer_ipv4_pool is reused across all iBGP peerings.


---

### mlag_interfaces_speed

**Type**: String  
**Path**: `<node_type_keys.key>.defaults.mlag_interfaces_speed`  
**Valid Values**: `100full`, `100g`, `100g-1`, `100g-2`, `100g-4`, `100half`, `10full`, `10g`, `10half`, `1g`, `200g`, `200g-2`, `200g-4`, `25g`, `400g`, `400g-4`, `400g-8`, `40g`, `50g`, `50g-1`, `50g-2`, `800g-8`, `sfp-1000baset auto 100full`, `1.6t-8`, `100mfull`, `100mhalf`, `10mfull`, `10mhalf`, `200g-1`, `400g-2`, `40g-4`, `800g-4`, `auto`, `auto 10000full`, `auto 1000full`, `auto 100full`, `auto 100g-1`, `auto 100g-2`, `auto 100g-4`, `auto 100gfull`, `auto 100half`, `auto 10full`, `auto 10gfull`, `auto 10half`, `auto 1gfull`, `auto 2.5gfull`, `auto 200g-2`, `auto 200g-4`, `auto 25gfull`, `auto 400g-4`, `auto 400g-8`, `auto 40gfull`, `auto 50g-1`, `auto 50g-2`, `auto 50gfull`, `auto 5gfull`, `auto 800g-8`, `auto 1.6t-8`, `auto 100mfull`, `auto 100mhalf`, `auto 10g`, `auto 10mfull`, `auto 10mhalf`, `auto 1g`, `auto 2.5g`, `auto 200g-1`, `auto 25g`, `auto 400g-2`, `auto 40g-4`, `auto 5g`, `auto 800g-4`, `forced 10000full`, `forced 1000full`, `forced 1000half`, `forced 100full`, `forced 100gfull`, `forced 100half`, `forced 10full`, `forced 10half`, `forced 25gfull`, `forced 40gfull`, `forced 50gfull`  

Set MLAG interface speed.


---

### mlag_interfaces_speed

**Type**: String  
**Path**: `<node_type_keys.key>.node_groups.[].nodes.[].mlag_interfaces_speed`  
**Valid Values**: `100full`, `100g`, `100g-1`, `100g-2`, `100g-4`, `100half`, `10full`, `10g`, `10half`, `1g`, `200g`, `200g-2`, `200g-4`, `25g`, `400g`, `400g-4`, `400g-8`, `40g`, `50g`, `50g-1`, `50g-2`, `800g-8`, `sfp-1000baset auto 100full`, `1.6t-8`, `100mfull`, `100mhalf`, `10mfull`, `10mhalf`, `200g-1`, `400g-2`, `40g-4`, `800g-4`, `auto`, `auto 10000full`, `auto 1000full`, `auto 100full`, `auto 100g-1`, `auto 100g-2`, `auto 100g-4`, `auto 100gfull`, `auto 100half`, `auto 10full`, `auto 10gfull`, `auto 10half`, `auto 1gfull`, `auto 2.5gfull`, `auto 200g-2`, `auto 200g-4`, `auto 25gfull`, `auto 400g-4`, `auto 400g-8`, `auto 40gfull`, `auto 50g-1`, `auto 50g-2`, `auto 50gfull`, `auto 5gfull`, `auto 800g-8`, `auto 1.6t-8`, `auto 100mfull`, `auto 100mhalf`, `auto 10g`, `auto 10mfull`, `auto 10mhalf`, `auto 1g`, `auto 2.5g`, `auto 200g-1`, `auto 25g`, `auto 400g-2`, `auto 40g-4`, `auto 5g`, `auto 800g-4`, `forced 10000full`, `forced 1000full`, `forced 1000half`, `forced 100full`, `forced 100gfull`, `forced 100half`, `forced 10full`, `forced 10half`, `forced 25gfull`, `forced 40gfull`, `forced 50gfull`  

Set MLAG interface speed.


---

### mlag_interfaces_speed

**Type**: String  
**Path**: `<node_type_keys.key>.node_groups.[].mlag_interfaces_speed`  
**Valid Values**: `100full`, `100g`, `100g-1`, `100g-2`, `100g-4`, `100half`, `10full`, `10g`, `10half`, `1g`, `200g`, `200g-2`, `200g-4`, `25g`, `400g`, `400g-4`, `400g-8`, `40g`, `50g`, `50g-1`, `50g-2`, `800g-8`, `sfp-1000baset auto 100full`, `1.6t-8`, `100mfull`, `100mhalf`, `10mfull`, `10mhalf`, `200g-1`, `400g-2`, `40g-4`, `800g-4`, `auto`, `auto 10000full`, `auto 1000full`, `auto 100full`, `auto 100g-1`, `auto 100g-2`, `auto 100g-4`, `auto 100gfull`, `auto 100half`, `auto 10full`, `auto 10gfull`, `auto 10half`, `auto 1gfull`, `auto 2.5gfull`, `auto 200g-2`, `auto 200g-4`, `auto 25gfull`, `auto 400g-4`, `auto 400g-8`, `auto 40gfull`, `auto 50g-1`, `auto 50g-2`, `auto 50gfull`, `auto 5gfull`, `auto 800g-8`, `auto 1.6t-8`, `auto 100mfull`, `auto 100mhalf`, `auto 10g`, `auto 10mfull`, `auto 10mhalf`, `auto 1g`, `auto 2.5g`, `auto 200g-1`, `auto 25g`, `auto 400g-2`, `auto 40g-4`, `auto 5g`, `auto 800g-4`, `forced 10000full`, `forced 1000full`, `forced 1000half`, `forced 100full`, `forced 100gfull`, `forced 100half`, `forced 10full`, `forced 10half`, `forced 25gfull`, `forced 40gfull`, `forced 50gfull`  

Set MLAG interface speed.


---

### mlag_interfaces_speed

**Type**: String  
**Path**: `<node_type_keys.key>.nodes.[].mlag_interfaces_speed`  
**Valid Values**: `100full`, `100g`, `100g-1`, `100g-2`, `100g-4`, `100half`, `10full`, `10g`, `10half`, `1g`, `200g`, `200g-2`, `200g-4`, `25g`, `400g`, `400g-4`, `400g-8`, `40g`, `50g`, `50g-1`, `50g-2`, `800g-8`, `sfp-1000baset auto 100full`, `1.6t-8`, `100mfull`, `100mhalf`, `10mfull`, `10mhalf`, `200g-1`, `400g-2`, `40g-4`, `800g-4`, `auto`, `auto 10000full`, `auto 1000full`, `auto 100full`, `auto 100g-1`, `auto 100g-2`, `auto 100g-4`, `auto 100gfull`, `auto 100half`, `auto 10full`, `auto 10gfull`, `auto 10half`, `auto 1gfull`, `auto 2.5gfull`, `auto 200g-2`, `auto 200g-4`, `auto 25gfull`, `auto 400g-4`, `auto 400g-8`, `auto 40gfull`, `auto 50g-1`, `auto 50g-2`, `auto 50gfull`, `auto 5gfull`, `auto 800g-8`, `auto 1.6t-8`, `auto 100mfull`, `auto 100mhalf`, `auto 10g`, `auto 10mfull`, `auto 10mhalf`, `auto 1g`, `auto 2.5g`, `auto 200g-1`, `auto 25g`, `auto 400g-2`, `auto 40g-4`, `auto 5g`, `auto 800g-4`, `forced 10000full`, `forced 1000full`, `forced 1000half`, `forced 100full`, `forced 100gfull`, `forced 100half`, `forced 10full`, `forced 10half`, `forced 25gfull`, `forced 40gfull`, `forced 50gfull`  

Set MLAG interface speed.


---

### mlag_interfaces_speed

**Type**: String  
**Path**: `default_interfaces.[].mlag_interfaces_speed`  
**Valid Values**: `100full`, `100g`, `100g-1`, `100g-2`, `100g-4`, `100half`, `10full`, `10g`, `10half`, `1g`, `200g`, `200g-2`, `200g-4`, `25g`, `400g`, `400g-4`, `400g-8`, `40g`, `50g`, `50g-1`, `50g-2`, `800g-8`, `sfp-1000baset auto 100full`, `1.6t-8`, `100mfull`, `100mhalf`, `10mfull`, `10mhalf`, `200g-1`, `400g-2`, `40g-4`, `800g-4`, `auto`, `auto 10000full`, `auto 1000full`, `auto 100full`, `auto 100g-1`, `auto 100g-2`, `auto 100g-4`, `auto 100gfull`, `auto 100half`, `auto 10full`, `auto 10gfull`, `auto 10half`, `auto 1gfull`, `auto 2.5gfull`, `auto 200g-2`, `auto 200g-4`, `auto 25gfull`, `auto 400g-4`, `auto 400g-8`, `auto 40gfull`, `auto 50g-1`, `auto 50g-2`, `auto 50gfull`, `auto 5gfull`, `auto 800g-8`, `auto 1.6t-8`, `auto 100mfull`, `auto 100mhalf`, `auto 10g`, `auto 10mfull`, `auto 10mhalf`, `auto 1g`, `auto 2.5g`, `auto 200g-1`, `auto 25g`, `auto 400g-2`, `auto 40g-4`, `auto 5g`, `auto 800g-4`, `forced 10000full`, `forced 1000full`, `forced 1000half`, `forced 100full`, `forced 100gfull`, `forced 100half`, `forced 10full`, `forced 10half`, `forced 25gfull`, `forced 40gfull`, `forced 50gfull`  

Set MLAG interfaces speed.


---

### mlag_interfaces_speed

**Type**: String  
**Path**: `device_profiles.[].mlag_interfaces_speed`  
**Valid Values**: `100full`, `100g`, `100g-1`, `100g-2`, `100g-4`, `100half`, `10full`, `10g`, `10half`, `1g`, `200g`, `200g-2`, `200g-4`, `25g`, `400g`, `400g-4`, `400g-8`, `40g`, `50g`, `50g-1`, `50g-2`, `800g-8`, `sfp-1000baset auto 100full`, `1.6t-8`, `100mfull`, `100mhalf`, `10mfull`, `10mhalf`, `200g-1`, `400g-2`, `40g-4`, `800g-4`, `auto`, `auto 10000full`, `auto 1000full`, `auto 100full`, `auto 100g-1`, `auto 100g-2`, `auto 100g-4`, `auto 100gfull`, `auto 100half`, `auto 10full`, `auto 10gfull`, `auto 10half`, `auto 1gfull`, `auto 2.5gfull`, `auto 200g-2`, `auto 200g-4`, `auto 25gfull`, `auto 400g-4`, `auto 400g-8`, `auto 40gfull`, `auto 50g-1`, `auto 50g-2`, `auto 50gfull`, `auto 5gfull`, `auto 800g-8`, `auto 1.6t-8`, `auto 100mfull`, `auto 100mhalf`, `auto 10g`, `auto 10mfull`, `auto 10mhalf`, `auto 1g`, `auto 2.5g`, `auto 200g-1`, `auto 25g`, `auto 400g-2`, `auto 40g-4`, `auto 5g`, `auto 800g-4`, `forced 10000full`, `forced 1000full`, `forced 1000half`, `forced 100full`, `forced 100gfull`, `forced 100half`, `forced 10full`, `forced 10half`, `forced 25gfull`, `forced 40gfull`, `forced 50gfull`  

Set MLAG interface speed.


---

### mlag_interfaces_speed

**Type**: String  
**Path**: `devices.[].mlag_interfaces_speed`  
**Valid Values**: `100full`, `100g`, `100g-1`, `100g-2`, `100g-4`, `100half`, `10full`, `10g`, `10half`, `1g`, `200g`, `200g-2`, `200g-4`, `25g`, `400g`, `400g-4`, `400g-8`, `40g`, `50g`, `50g-1`, `50g-2`, `800g-8`, `sfp-1000baset auto 100full`, `1.6t-8`, `100mfull`, `100mhalf`, `10mfull`, `10mhalf`, `200g-1`, `400g-2`, `40g-4`, `800g-4`, `auto`, `auto 10000full`, `auto 1000full`, `auto 100full`, `auto 100g-1`, `auto 100g-2`, `auto 100g-4`, `auto 100gfull`, `auto 100half`, `auto 10full`, `auto 10gfull`, `auto 10half`, `auto 1gfull`, `auto 2.5gfull`, `auto 200g-2`, `auto 200g-4`, `auto 25gfull`, `auto 400g-4`, `auto 400g-8`, `auto 40gfull`, `auto 50g-1`, `auto 50g-2`, `auto 50gfull`, `auto 5gfull`, `auto 800g-8`, `auto 1.6t-8`, `auto 100mfull`, `auto 100mhalf`, `auto 10g`, `auto 10mfull`, `auto 10mhalf`, `auto 1g`, `auto 2.5g`, `auto 200g-1`, `auto 25g`, `auto 400g-2`, `auto 40g-4`, `auto 5g`, `auto 800g-4`, `forced 10000full`, `forced 1000full`, `forced 1000half`, `forced 100full`, `forced 100gfull`, `forced 100half`, `forced 10full`, `forced 10half`, `forced 25gfull`, `forced 40gfull`, `forced 50gfull`  

Set MLAG interface speed.


---

### mlag_member_description

**Type**: String  
**Path**: `mlag_member_description`  
**Default**: `MLAG_{mlag_peer}_{peer_interface}`  

Description or description template to be used on MLAG peer-link ethernet interfaces.
This can be a template using the AVD string formatter syntax: https://avd.arista.com/stable/ansible_collections/arista/avd/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.
The available template fields are:
  - `mlag_peer`: The name of the MLAG peer.
  - `interface`: The local MLAG port-channel interface.
  - `peer_interface`: The port-channel interface on the MLAG peer.
  - `mlag_port_channel_id`: The local MLAG port-channel ID.
  - `mlag_peer_port_channel_id`: The port-channel ID on the MLAG peer.

By default the description is templated from the name and interface of the MLAG peer.

---

### mlag_on_orphan_port_channel_downlink

**Type**: Boolean  
**Path**: `mlag_on_orphan_port_channel_downlink`  
**Default**: `False`  

If `true` an MLAG ID will always be configured on a Port-Channel downlink even if the downlink is only on one node in the MLAG pair.
If `false` (default) an MLAG ID will only be configured on Port-Channel downlinks dual-homed to two MLAG switches.

---

### mlag_peer_address_family

**Type**: String  
**Path**: `<node_type_keys.key>.defaults.mlag_peer_address_family`  
**Default**: `ipv4`  
**Valid Values**: `ipv4`, `ipv6`  

IP address family used to establish MLAG Peer Link (control link).
`ipv6` requires EOS version 4.31.1F or higher.
Note: `ipv6` is not supported in combination with a common MLAG peer link VLAN (ex. `mlag_peer_l3_vlan` set to 4094).

---

### mlag_peer_address_family

**Type**: String  
**Path**: `<node_type_keys.key>.node_groups.[].nodes.[].mlag_peer_address_family`  
**Default**: `ipv4`  
**Valid Values**: `ipv4`, `ipv6`  

IP address family used to establish MLAG Peer Link (control link).
`ipv6` requires EOS version 4.31.1F or higher.
Note: `ipv6` is not supported in combination with a common MLAG peer link VLAN (ex. `mlag_peer_l3_vlan` set to 4094).

---

### mlag_peer_address_family

**Type**: String  
**Path**: `<node_type_keys.key>.node_groups.[].mlag_peer_address_family`  
**Default**: `ipv4`  
**Valid Values**: `ipv4`, `ipv6`  

IP address family used to establish MLAG Peer Link (control link).
`ipv6` requires EOS version 4.31.1F or higher.
Note: `ipv6` is not supported in combination with a common MLAG peer link VLAN (ex. `mlag_peer_l3_vlan` set to 4094).

---

### mlag_peer_address_family

**Type**: String  
**Path**: `<node_type_keys.key>.nodes.[].mlag_peer_address_family`  
**Default**: `ipv4`  
**Valid Values**: `ipv4`, `ipv6`  

IP address family used to establish MLAG Peer Link (control link).
`ipv6` requires EOS version 4.31.1F or higher.
Note: `ipv6` is not supported in combination with a common MLAG peer link VLAN (ex. `mlag_peer_l3_vlan` set to 4094).

---

### mlag_peer_address_family

**Type**: String  
**Path**: `device_profiles.[].mlag_peer_address_family`  
**Default**: `ipv4`  
**Valid Values**: `ipv4`, `ipv6`  

IP address family used to establish MLAG Peer Link (control link).
`ipv6` requires EOS version 4.31.1F or higher.
Note: `ipv6` is not supported in combination with a common MLAG peer link VLAN (ex. `mlag_peer_l3_vlan` set to 4094).

---

### mlag_peer_address_family

**Type**: String  
**Path**: `devices.[].mlag_peer_address_family`  
**Default**: `ipv4`  
**Valid Values**: `ipv4`, `ipv6`  

IP address family used to establish MLAG Peer Link (control link).
`ipv6` requires EOS version 4.31.1F or higher.
Note: `ipv6` is not supported in combination with a common MLAG peer link VLAN (ex. `mlag_peer_l3_vlan` set to 4094).

---

### mlag_peer_l3_svi_description

**Type**: String  
**Path**: `mlag_peer_l3_svi_description`  
**Default**: `MLAG_L3`  

Description or description template to be used on MLAG L3 peering SVI (Interface Vlan4093 by default).
This can be a template using the AVD string formatter syntax: https://avd.arista.com/stable/ansible_collections/arista/avd/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.
The available template fields are:
  - `mlag_peer`: The name of the MLAG peer.
  - `interface`: The MLAG L3 peering SVI name.
  - `mlag_peer_l3_vlan`: The MLAG L3 peering VLAN ID.

---

### mlag_peer_l3_vlan_name

**Type**: String  
**Path**: `mlag_peer_l3_vlan_name`  
**Default**: `MLAG_L3`  

Name or name template to be used on MLAG L3 VLAN (VLAN 4093 by default).
This can be a template using the AVD string formatter syntax: https://avd.arista.com/stable/ansible_collections/arista/avd/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.
The available template fields are:
  - `mlag_peer`: The name of the MLAG peer.
  - `mlag_peer_l3_vlan`: The MLAG L3 peering VLAN ID.

---

### mlag_peer_l3_vrf_svi_description

**Type**: String  
**Path**: `mlag_peer_l3_vrf_svi_description`  
**Default**: `MLAG_L3_VRF_{vrf}`  

Description or description template to be used on MLAG L3 peering SVI for VRFs.
This can be a template using the AVD string formatter syntax: https://avd.arista.com/stable/ansible_collections/arista/avd/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.
The available template fields are:
  - `mlag_peer`: The name of the MLAG peer.
  - `interface`: The MLAG L3 VRF peering SVI name.
  - `vlan`: The MLAG L3 VRF peering VLAN ID.
  - `vrf`: The VRF name.

---

### mlag_peer_l3_vrf_vlan_name

**Type**: String  
**Path**: `mlag_peer_l3_vrf_vlan_name`  
**Default**: `MLAG_L3_VRF_{vrf}`  

Name or name template to be used on MLAG L3 peering VLAN for VRFs.
This can be a template using the AVD string formatter syntax: https://avd.arista.com/stable/ansible_collections/arista/avd/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.
The available template fields are:
  - `mlag_peer`: The name of the MLAG peer.
  - `vlan`: The MLAG L3 VRF peering VLAN ID.
  - `vrf`: The VRF name.

---

### mlag_peer_svi_description

**Type**: String  
**Path**: `mlag_peer_svi_description`  
**Default**: `MLAG`  

Description or description template to be used on MLAG peering SVI (Interface Vlan4094 by default).
This can be a template using the AVD string formatter syntax: https://avd.arista.com/stable/ansible_collections/arista/avd/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.
The available template fields are:
  - `mlag_peer`: The name of the MLAG peer.
  - `interface`: The MLAG peering SVI name.
  - `mlag_peer_vlan`: The MLAG peering VLAN ID.

---

### mlag_peer_vlan_name

**Type**: String  
**Path**: `mlag_peer_vlan_name`  
**Default**: `MLAG`  

Name or name template to be used on MLAG peering VLAN (VLAN 4094 by default).
This can be a template using the AVD string formatter syntax: https://avd.arista.com/stable/ansible_collections/arista/avd/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.
The available template fields are:
  - `mlag_peer`: The name of the MLAG peer.
  - `mlag_peer_vlan`: The MLAG peering VLAN ID.

---

### mlag_port_channel_description

**Type**: String  
**Path**: `mlag_port_channel_description`  
**Default**: `MLAG_{mlag_peer}_{peer_interface}`  

Description or description template to be used on MLAG peer-link port-channel interfaces.
This can be a template using the AVD string formatter syntax: https://avd.arista.com/stable/ansible_collections/arista/avd/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.
The available template fields are:
  - `mlag_peer`: The name of the MLAG peer.
  - `interface`: The local MLAG port-channel interface.
  - `peer_interface`: The port-channel interface on the MLAG peer.
  - `mlag_port_channel_id`: The local MLAG port-channel ID.
  - `mlag_peer_port_channel_id`: The port-channel ID on the MLAG peer.

By default the description is templated from the name and port-channel interface of the MLAG peer.

---

### mode

**Type**: String  
**Path**: `<connected_endpoints_keys.key>.[].adapters.[].mode`  
**Valid Values**: `access`, `dot1q-tunnel`, `trunk`, `trunk phone`  

Interface mode.

---

### mode

**Type**: String  
**Path**: `<connected_endpoints_keys.key>.[].adapters.[].dot1x.pae.mode`  
**Valid Values**: `authenticator`, `supplicant`  
---

### mode

**Type**: String  
**Path**: `<connected_endpoints_keys.key>.[].adapters.[].dot1x.host_mode.mode`  
**Valid Values**: `multi-host`, `single-host`  
---

### mode

**Type**: String  
**Path**: `<connected_endpoints_keys.key>.[].adapters.[].port_channel.mode`  
**Valid Values**: `active`, `passive`, `on`  

Port-Channel Mode.

---

### mode

**Type**: String  
**Path**: `<connected_endpoints_keys.key>.[].adapters.[].port_channel.lacp_fallback.mode`  
**Valid Values**: `static`, `individual`  

Either static or individual mode is supported.
If the mode is set to "individual" either 'profile' or ('mode' and 'vlans')  must be set under 'port_channel.lacp_fallback.individual'.


---

### mode

**Type**: String  
**Path**: `<connected_endpoints_keys.key>.[].adapters.[].port_channel.lacp_fallback.individual.mode`  
**Valid Values**: `access`, `dot1q-tunnel`, `trunk`, `trunk phone`  

Interface mode on the port-channel member interfaces when in fallback individual.

---

### mode

**Type**: String  
**Path**: `<connected_endpoints_keys.key>.[].adapters.[].port_channel.lacp_timer.mode`  
**Valid Values**: `normal`, `fast`  

LACP mode for interface members.

---

### mode

**Type**: String  
**Path**: `<custom_connected_endpoints_keys.key>.[].adapters.[].mode`  
**Valid Values**: `access`, `dot1q-tunnel`, `trunk`, `trunk phone`  

Interface mode.

---

### mode

**Type**: String  
**Path**: `<custom_connected_endpoints_keys.key>.[].adapters.[].dot1x.pae.mode`  
**Valid Values**: `authenticator`, `supplicant`  
---

### mode

**Type**: String  
**Path**: `<custom_connected_endpoints_keys.key>.[].adapters.[].dot1x.host_mode.mode`  
**Valid Values**: `multi-host`, `single-host`  
---

### mode

**Type**: String  
**Path**: `<custom_connected_endpoints_keys.key>.[].adapters.[].port_channel.mode`  
**Valid Values**: `active`, `passive`, `on`  

Port-Channel Mode.

---

### mode

**Type**: String  
**Path**: `<custom_connected_endpoints_keys.key>.[].adapters.[].port_channel.lacp_fallback.mode`  
**Valid Values**: `static`, `individual`  

Either static or individual mode is supported.
If the mode is set to "individual" either 'profile' or ('mode' and 'vlans')  must be set under 'port_channel.lacp_fallback.individual'.


---

### mode

**Type**: String  
**Path**: `<custom_connected_endpoints_keys.key>.[].adapters.[].port_channel.lacp_fallback.individual.mode`  
**Valid Values**: `access`, `dot1q-tunnel`, `trunk`, `trunk phone`  

Interface mode on the port-channel member interfaces when in fallback individual.

---

### mode

**Type**: String  
**Path**: `<custom_connected_endpoints_keys.key>.[].adapters.[].port_channel.lacp_timer.mode`  
**Valid Values**: `normal`, `fast`  

LACP mode for interface members.

---

### mode

**Type**: String  
**Path**: `<network_services_keys.name>.[].vrfs.[].l3_port_channels.[].mode`  
**Default**: `active`  
**Valid Values**: `active`, `passive`, `on`  

Port-Channel mode.
Should not be set on Port-Channel subinterfaces.

---

### mode

**Type**: String  
**Path**: `<network_services_keys.name>.[].point_to_point_services.[].endpoints.[].port_channel.mode`  
**Valid Values**: `active`, `on`  
---

### mode

**Type**: String  
**Path**: `<node_type_keys.key>.defaults.ptp.mode`  
**Default**: `boundary`  
**Valid Values**: `boundary`  
---

### mode

**Type**: String  
**Path**: `<node_type_keys.key>.defaults.l3_interfaces.[].rx_queue.mode`  
**Valid Values**: `shared`, `exclusive`  

Mode applicable to the workers.

---

### mode

**Type**: String  
**Path**: `<node_type_keys.key>.defaults.l3_port_channels.[].mode`  
**Default**: `active`  
**Valid Values**: `active`, `passive`, `on`  

Port-Channel mode.
Should not be set on Port-Channel subinterfaces.

---

### mode

**Type**: String  
**Path**: `<node_type_keys.key>.defaults.l3_port_channels.[].member_interfaces.[].rx_queue.mode`  
**Valid Values**: `shared`, `exclusive`  

Mode applicable to the workers.

---

### mode

**Type**: String  
**Path**: `<node_type_keys.key>.node_groups.[].nodes.[].ptp.mode`  
**Default**: `boundary`  
**Valid Values**: `boundary`  
---

### mode

**Type**: String  
**Path**: `<node_type_keys.key>.node_groups.[].nodes.[].l3_interfaces.[].rx_queue.mode`  
**Valid Values**: `shared`, `exclusive`  

Mode applicable to the workers.

---

### mode

**Type**: String  
**Path**: `<node_type_keys.key>.node_groups.[].nodes.[].l3_port_channels.[].mode`  
**Default**: `active`  
**Valid Values**: `active`, `passive`, `on`  

Port-Channel mode.
Should not be set on Port-Channel subinterfaces.

---

### mode

**Type**: String  
**Path**: `<node_type_keys.key>.node_groups.[].nodes.[].l3_port_channels.[].member_interfaces.[].rx_queue.mode`  
**Valid Values**: `shared`, `exclusive`  

Mode applicable to the workers.

---

### mode

**Type**: String  
**Path**: `<node_type_keys.key>.node_groups.[].ptp.mode`  
**Default**: `boundary`  
**Valid Values**: `boundary`  
---

### mode

**Type**: String  
**Path**: `<node_type_keys.key>.node_groups.[].l3_interfaces.[].rx_queue.mode`  
**Valid Values**: `shared`, `exclusive`  

Mode applicable to the workers.

---

### mode

**Type**: String  
**Path**: `<node_type_keys.key>.node_groups.[].l3_port_channels.[].mode`  
**Default**: `active`  
**Valid Values**: `active`, `passive`, `on`  

Port-Channel mode.
Should not be set on Port-Channel subinterfaces.

---

### mode

**Type**: String  
**Path**: `<node_type_keys.key>.node_groups.[].l3_port_channels.[].member_interfaces.[].rx_queue.mode`  
**Valid Values**: `shared`, `exclusive`  

Mode applicable to the workers.

---

### mode

**Type**: String  
**Path**: `<node_type_keys.key>.nodes.[].ptp.mode`  
**Default**: `boundary`  
**Valid Values**: `boundary`  
---

### mode

**Type**: String  
**Path**: `<node_type_keys.key>.nodes.[].l3_interfaces.[].rx_queue.mode`  
**Valid Values**: `shared`, `exclusive`  

Mode applicable to the workers.

---

### mode

**Type**: String  
**Path**: `<node_type_keys.key>.nodes.[].l3_port_channels.[].mode`  
**Default**: `active`  
**Valid Values**: `active`, `passive`, `on`  

Port-Channel mode.
Should not be set on Port-Channel subinterfaces.

---

### mode

**Type**: String  
**Path**: `<node_type_keys.key>.nodes.[].l3_port_channels.[].member_interfaces.[].rx_queue.mode`  
**Valid Values**: `shared`, `exclusive`  

Mode applicable to the workers.

---

### mode

**Type**: String  
**Path**: `connected_endpoints.[].adapters.[].mode`  
**Valid Values**: `access`, `dot1q-tunnel`, `trunk`, `trunk phone`  

Interface mode.

---

### mode

**Type**: String  
**Path**: `connected_endpoints.[].adapters.[].dot1x.pae.mode`  
**Valid Values**: `authenticator`, `supplicant`  
---

### mode

**Type**: String  
**Path**: `connected_endpoints.[].adapters.[].dot1x.host_mode.mode`  
**Valid Values**: `multi-host`, `single-host`  
---

### mode

**Type**: String  
**Path**: `connected_endpoints.[].adapters.[].port_channel.mode`  
**Valid Values**: `active`, `passive`, `on`  

Port-Channel Mode.

---

### mode

**Type**: String  
**Path**: `connected_endpoints.[].adapters.[].port_channel.lacp_fallback.mode`  
**Valid Values**: `static`, `individual`  

Either static or individual mode is supported.
If the mode is set to "individual" either 'profile' or ('mode' and 'vlans')  must be set under 'port_channel.lacp_fallback.individual'.


---

### mode

**Type**: String  
**Path**: `connected_endpoints.[].adapters.[].port_channel.lacp_fallback.individual.mode`  
**Valid Values**: `access`, `dot1q-tunnel`, `trunk`, `trunk phone`  

Interface mode on the port-channel member interfaces when in fallback individual.

---

### mode

**Type**: String  
**Path**: `connected_endpoints.[].adapters.[].port_channel.lacp_timer.mode`  
**Valid Values**: `normal`, `fast`  

LACP mode for interface members.

---

### mode

**Type**: String  
**Path**: `core_interfaces.p2p_links_profiles.[].port_channel.mode`  
**Default**: `active`  
**Valid Values**: `on`, `active`, `passive`  
---

### mode

**Type**: String  
**Path**: `core_interfaces.p2p_links.[].port_channel.mode`  
**Default**: `active`  
**Valid Values**: `on`, `active`, `passive`  
---

### mode

**Type**: String  
**Path**: `device_profiles.[].ptp.mode`  
**Default**: `boundary`  
**Valid Values**: `boundary`  
---

### mode

**Type**: String  
**Path**: `device_profiles.[].l3_interfaces.[].rx_queue.mode`  
**Valid Values**: `shared`, `exclusive`  

Mode applicable to the workers.

---

### mode

**Type**: String  
**Path**: `device_profiles.[].l3_port_channels.[].mode`  
**Default**: `active`  
**Valid Values**: `active`, `passive`, `on`  

Port-Channel mode.
Should not be set on Port-Channel subinterfaces.

---

### mode

**Type**: String  
**Path**: `device_profiles.[].l3_port_channels.[].member_interfaces.[].rx_queue.mode`  
**Valid Values**: `shared`, `exclusive`  

Mode applicable to the workers.

---

### mode

**Type**: String  
**Path**: `devices.[].ptp.mode`  
**Default**: `boundary`  
**Valid Values**: `boundary`  
---

### mode

**Type**: String  
**Path**: `devices.[].l3_interfaces.[].rx_queue.mode`  
**Valid Values**: `shared`, `exclusive`  

Mode applicable to the workers.

---

### mode

**Type**: String  
**Path**: `devices.[].l3_port_channels.[].mode`  
**Default**: `active`  
**Valid Values**: `active`, `passive`, `on`  

Port-Channel mode.
Should not be set on Port-Channel subinterfaces.

---

### mode

**Type**: String  
**Path**: `devices.[].l3_port_channels.[].member_interfaces.[].rx_queue.mode`  
**Valid Values**: `shared`, `exclusive`  

Mode applicable to the workers.

---

### mode

**Type**: String  
**Path**: `dot1x_settings.accounting.mode`  
**Default**: `start-stop`  
**Valid Values**: `start-stop`, `stop-only`  

Determines whether to send accounting records when a session is established and
when it ends (`start-stop`), or only when the session ends (`stop-only`).

---

### mode

**Type**: String  
**Path**: `l3_edge.p2p_links_profiles.[].port_channel.mode`  
**Default**: `active`  
**Valid Values**: `on`, `active`, `passive`  
---

### mode

**Type**: String  
**Path**: `l3_edge.p2p_links.[].port_channel.mode`  
**Default**: `active`  
**Valid Values**: `on`, `active`, `passive`  
---

### mode

**Type**: String  
**Path**: `l3_interface_profiles.[].rx_queue.mode`  
**Valid Values**: `shared`, `exclusive`  

Mode applicable to the workers.

---

### mode

**Type**: String  
**Path**: `network_ports.[].mode`  
**Valid Values**: `access`, `dot1q-tunnel`, `trunk`, `trunk phone`  

Interface mode.

---

### mode

**Type**: String  
**Path**: `network_ports.[].dot1x.pae.mode`  
**Valid Values**: `authenticator`, `supplicant`  
---

### mode

**Type**: String  
**Path**: `network_ports.[].dot1x.host_mode.mode`  
**Valid Values**: `multi-host`, `single-host`  
---

### mode

**Type**: String  
**Path**: `network_ports.[].port_channel.mode`  
**Valid Values**: `active`, `passive`, `on`  

Port-Channel Mode.

---

### mode

**Type**: String  
**Path**: `network_ports.[].port_channel.lacp_fallback.mode`  
**Valid Values**: `static`, `individual`  

Either static or individual mode is supported.
If the mode is set to "individual" either 'profile' or ('mode' and 'vlans')  must be set under 'port_channel.lacp_fallback.individual'.


---

### mode

**Type**: String  
**Path**: `network_ports.[].port_channel.lacp_fallback.individual.mode`  
**Valid Values**: `access`, `dot1q-tunnel`, `trunk`, `trunk phone`  

Interface mode on the port-channel member interfaces when in fallback individual.

---

### mode

**Type**: String  
**Path**: `network_ports.[].port_channel.lacp_timer.mode`  
**Valid Values**: `normal`, `fast`  

LACP mode for interface members.

---

### mode

**Type**: String  
**Path**: `port_profiles.[].mode`  
**Valid Values**: `access`, `dot1q-tunnel`, `trunk`, `trunk phone`  

Interface mode.

---

### mode

**Type**: String  
**Path**: `port_profiles.[].dot1x.pae.mode`  
**Valid Values**: `authenticator`, `supplicant`  
---

### mode

**Type**: String  
**Path**: `port_profiles.[].dot1x.host_mode.mode`  
**Valid Values**: `multi-host`, `single-host`  
---

### mode

**Type**: String  
**Path**: `port_profiles.[].port_channel.mode`  
**Valid Values**: `active`, `passive`, `on`  

Port-Channel Mode.

---

### mode

**Type**: String  
**Path**: `port_profiles.[].port_channel.lacp_fallback.mode`  
**Valid Values**: `static`, `individual`  

Either static or individual mode is supported.
If the mode is set to "individual" either 'profile' or ('mode' and 'vlans')  must be set under 'port_channel.lacp_fallback.individual'.


---

### mode

**Type**: String  
**Path**: `port_profiles.[].port_channel.lacp_fallback.individual.mode`  
**Valid Values**: `access`, `dot1q-tunnel`, `trunk`, `trunk phone`  

Interface mode on the port-channel member interfaces when in fallback individual.

---

### mode

**Type**: String  
**Path**: `port_profiles.[].port_channel.lacp_timer.mode`  
**Valid Values**: `normal`, `fast`  

LACP mode for interface members.

---

### mode

**Type**: String  
**Path**: `underlay_multicast_anycast_rp.mode`  
**Default**: `pim`  
**Valid Values**: `pim`, `msdp`  
---

### monitor

**Type**: String  
**Path**: `logging_settings.monitor`  
**Valid Values**: `debugging`, `informational`, `notifications`, `warnings`, `errors`, `critical`, `alerts`, `emergencies`, `disabled`  

Monitor logging severity level.

---

### mpls_overlay_role

**Type**: String  
**Path**: `<node_type_keys.key>.defaults.mpls_overlay_role`  
**Valid Values**: `client`, `server`, `none`  

Set the default mpls overlay role.
Acting role in overlay control plane.


---

### mpls_overlay_role

**Type**: String  
**Path**: `<node_type_keys.key>.node_groups.[].nodes.[].mpls_overlay_role`  
**Valid Values**: `client`, `server`, `none`  

Set the default mpls overlay role.
Acting role in overlay control plane.


---

### mpls_overlay_role

**Type**: String  
**Path**: `<node_type_keys.key>.node_groups.[].mpls_overlay_role`  
**Valid Values**: `client`, `server`, `none`  

Set the default mpls overlay role.
Acting role in overlay control plane.


---

### mpls_overlay_role

**Type**: String  
**Path**: `<node_type_keys.key>.nodes.[].mpls_overlay_role`  
**Valid Values**: `client`, `server`, `none`  

Set the default mpls overlay role.
Acting role in overlay control plane.


---

### mpls_overlay_role

**Type**: String  
**Path**: `device_profiles.[].mpls_overlay_role`  
**Valid Values**: `client`, `server`, `none`  

Set the default mpls overlay role.
Acting role in overlay control plane.


---

### mpls_overlay_role

**Type**: String  
**Path**: `devices.[].mpls_overlay_role`  
**Valid Values**: `client`, `server`, `none`  

Set the default mpls overlay role.
Acting role in overlay control plane.


---

## N

### name

**Type**: String  
**Path**: `hardware_counters.features.[].name`  
**Valid Values**: `acl`, `decap-group`, `directflow`, `ecn`, `flow-spec`, `gre tunnel interface`, `ip`, `mpls interface`, `mpls lfib`, `mpls tunnel`, `multicast`, `nexthop`, `pbr`, `pdp`, `policing interface`, `qos`, `qos dual-rate-policer`, `route`, `routed-port`, `segment-security`, `subinterface`, `tapagg`, `traffic-class`, `traffic-policy`, `traffic-policy vlan-interface`, `vlan`, `vlan-interface`, `vni decap`, `vni encap`, `vtep decap`, `vtep encap`  
---

### Network Services

**Type**: List, items: Dictionary  
**Path**: `<network_services_keys.name>`  
---

### network_services_keys

**Type**: List, items: Dictionary  
**Path**: `network_services_keys`  
**Default**: `See documentation`  

Network Services can be grouped by using separate keys.
The keys can be customized to provide a better better organization or grouping of your data.
`network_services_keys` should be defined in the top level group_vars for the fabric.
The default values will be overridden if defining this key, so it is recommended to copy the defaults and modify them.


---

### Node Types

**Type**: Dictionary  
**Path**: `<node_type_keys.key>`  
---

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

### ntp_settings

**Type**: Dictionary  
**Path**: `ntp_settings`  

NTP settings

---

## O

### only_local_vlan_trunk_groups

**Type**: Boolean  
**Path**: `only_local_vlan_trunk_groups`  
**Default**: `False`  

A vlan can have many trunk_groups assigned.
To avoid unneeded configuration changes on all leaf switches when a new trunk group is added,
this feature will only configure the vlan trunk groups matched with local connected_endpoints.
See "Details on only_local_vlan_trunk_groups" below.
Requires "enable_trunk_groups: true".


---

### operation

**Type**: String  
**Path**: `event_handlers.[].trigger_on_maintenance.operation`  
**Valid Values**: `enter`, `exit`  
---

### overlay_bgp_peer_description

**Type**: String  
**Path**: `overlay_bgp_peer_description`  
**Default**: `{peer}{peer_interface?<_}`  

Description or description template to be used on the overlay BGP peers.
This can be a template using the AVD string formatter syntax: https://avd.arista.com/stable/ansible_collections/arista/avd/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.
The available template fields are:
  - `peer`: The name of the BGP peer.
  - `peer_interface`: The interface on the BGP peer if available.

The default description is built from the name and interface of the BGP peer.

---

### overlay_cvx_servers

**Type**: List, items: String  
**Path**: `overlay_cvx_servers`  

List of CVX vxlan overlay controllers.
Required if overlay_routing_protocol == CVX.
CVX servers (VMs) are peering using their management interface, so mgmt_ip must be set for all CVX servers.


---

### overlay_her_flood_list_per_vni

**Type**: Boolean  
**Path**: `overlay_her_flood_list_per_vni`  
**Default**: `False`  

When using Head-End Replication, configure flood-lists per VNI.
By default HER will be configured with a common flood-list containing all VTEPs.
This behavior can be changed to per-VNI flood-lists by setting `overlay_her_flood_list_per_vni: true`.
This will make Arista AVD consider configured VLANs per VTEP, and only include the relevant VTEPs to each VNI's flood-list.


---

### overlay_her_flood_list_scope

**Type**: String  
**Path**: `overlay_her_flood_list_scope`  
**Default**: `fabric`  
**Valid Values**: `fabric`, `dc`  

When using Head-End Replication, set the scope of flood-lists to Fabric or DC.
By default all VTEPs in the Fabric (part of the inventory group referenced by "fabric_name") are added to the flood-lists.
This can be changed to all VTEPs in the DC (sharing the same "dc_name" value).
This is useful if Border Leaf switches are dividing the VXLAN overlay into separate domains.


---

### overlay_mlag_rfc5549

**Type**: Boolean  
**Path**: `overlay_mlag_rfc5549`  
**Default**: `False`  

IPv6 Unnumbered for MLAG iBGP connections.
Requires "underlay_rfc5549: true".


---

### overlay_rd_type

**Type**: Dictionary  
**Path**: `overlay_rd_type`  

Configuration options for the Administrator subfield (first part of RD) and the Assigned Number subfield (second part of RD).

By default Route Distinguishers (RD) are set to:
- `<overlay_loopback>:<mac_vrf_id_base + vlan_id or mac_vrf_vni_base + vlan_id>` for VLANs and VLAN-Aware Bundles with L2 vlans.
- `<overlay_loopback>:<vlan_aware_bundle_number_base + vrf_id>` for VLAN-Aware Bundles with SVIs.
- `<overlay_loopback>:<vlan_aware_bundle_number_base + id>` for VLAN-Aware Bundles defined under 'evpn_vlan_bundles'.
- `<overlay_loopback>:<vrf_id>` for VRFs.

Note:
RD is a 48-bit value which is split into <16-bit>:<32-bit> or <32-bit>:<16-bit>.
When using loopback or 32-bit ASN/number the assigned number can only be a 16-bit number. This may be a problem with large VNIs.
For 16-bit ASN/number the assigned number can be a 32-bit number.


---

### overlay_routing_protocol

**Type**: String  
**Path**: `overlay_routing_protocol`  
**Valid Values**: `ebgp`, `ibgp`, `cvx`, `her`, `none`  

- The following overlay routing protocols are supported:
  - ebgp: Configures fabric with eBGP, default for l3ls-evpn design.
  - ibgp: Configured fabric with iBGP, only supported with OSPF or ISIS variants in underlay, default for mpls design.
  - cvx: Configures fabric to leverage CloudVision eXchange as the overlay controller.
  - her: Configures fabric with Head-End Replication, configures static VXLAN flood-lists instead of using a dynamic overlay protocol.
  - none: No overlay configuration will be generated, default for l2ls design.

  If not set, the default_overlay_routing_protocol defined under the node_type_keys will be used (default is "ebgp").


---

### overlay_routing_protocol_address_family

**Type**: String  
**Path**: `overlay_routing_protocol_address_family`  
**Default**: `ipv4`  
**Valid Values**: `ipv4`, `ipv6`  

When set to `ipv6`, enable overlay EVPN peering with IPv6 addresses.
This feature depends on underlay_ipv6 variable. As of today, only RFC5549 is capable to transport IPv6 in the underlay.


---

### overlay_rt_type

**Type**: Dictionary  
**Path**: `overlay_rt_type`  

Configuration options for the Administrator subfield (first part of RT) and the Assigned Number subfield (second part of RT).

By default Route Targets (RT) are set to:
- `<(mac_vrf_id_base or mac_vrf_vni_base) + vlan_id>:<(mac_vrf_id_base or mac_vrf_vni_base) + vlan_id>` for VLANs and VLAN-Aware Bundles with L2 vlans.
- `<vlan_aware_bundle_number_base + vrf_id>:<vlan_aware_bundle_number_base + vrf_id>` for VLAN-Aware Bundles with SVIs.
- `<vlan_aware_bundle_number_base + id>:<vlan_aware_bundle_number_base + id>` for VLAN-Aware Bundles defined under 'evpn_vlan_bundles'.
- `<vrf_id>:<vrf_id>` for VRFs.

Notes:
RT is a 48-bit value which is split into <16-bit>:<32-bit> or <32-bit>:<16-bit>.
When using 32-bit ASN/number the VNI can only be a 16-bit number. Alternatively use vlan_id/vrf_id as assigned number.
For 16-bit ASN/number the assigned number can be a 32-bit number.


---

## P

### p2p_uplinks_mtu

**Type**: Integer  
**Path**: `p2p_uplinks_mtu`  
**Default**: `9214`  

Point to Point Links MTU.
Precedence: <node_type>.uplink_mtu -> platform_settings.p2p_uplinks_mtu -> p2p_uplinks_mtu -> 9214

---

### p2p_uplinks_qos_profile

**Type**: String  
**Path**: `p2p_uplinks_qos_profile`  

QOS Profile assigned on all infrastructure links.

---

### password_type

**Type**: String  
**Path**: `<network_services_keys.name>.[].bgp_peer_groups.[].password_type`  
**Default**: `7`  
**Valid Values**: `7`, `8a`  
---

### password_type

**Type**: String  
**Path**: `<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].password_type`  
**Default**: `7`  
**Valid Values**: `7`, `8a`  
---

### password_type

**Type**: String  
**Path**: `aaa_settings.enable_password.password_type`  
**Default**: `sha512`  
**Valid Values**: `sha512`  
---

### password_type

**Type**: String  
**Path**: `aaa_settings.local_users.[].password_type`  
**Default**: `sha512`  
**Valid Values**: `sha512`  
---

### permit_response_traffic

**Type**: String  
**Path**: `ipv4_acls.[].permit_response_traffic`  
**Valid Values**: `nat`  

Permit response traffic automatically based on NAT translations.
Minimum EOS version requirement 4.32.2F.

---

### phone_trunk_mode

**Type**: String  
**Path**: `<connected_endpoints_keys.key>.[].adapters.[].phone_trunk_mode`  
**Valid Values**: `tagged`, `untagged`, `tagged phone`, `untagged phone`  

Specify if the phone traffic is tagged or untagged.
If both data and phone traffic are untagged, MAC-Based VLAN Assignment (MBVA) is used, if supported by the model of switch.

---

### phone_trunk_mode

**Type**: String  
**Path**: `<custom_connected_endpoints_keys.key>.[].adapters.[].phone_trunk_mode`  
**Valid Values**: `tagged`, `untagged`, `tagged phone`, `untagged phone`  

Specify if the phone traffic is tagged or untagged.
If both data and phone traffic are untagged, MAC-Based VLAN Assignment (MBVA) is used, if supported by the model of switch.

---

### phone_trunk_mode

**Type**: String  
**Path**: `connected_endpoints.[].adapters.[].phone_trunk_mode`  
**Valid Values**: `tagged`, `untagged`, `tagged phone`, `untagged phone`  

Specify if the phone traffic is tagged or untagged.
If both data and phone traffic are untagged, MAC-Based VLAN Assignment (MBVA) is used, if supported by the model of switch.

---

### phone_trunk_mode

**Type**: String  
**Path**: `network_ports.[].phone_trunk_mode`  
**Valid Values**: `tagged`, `untagged`, `tagged phone`, `untagged phone`  

Specify if the phone traffic is tagged or untagged.
If both data and phone traffic are untagged, MAC-Based VLAN Assignment (MBVA) is used, if supported by the model of switch.

---

### phone_trunk_mode

**Type**: String  
**Path**: `port_profiles.[].phone_trunk_mode`  
**Valid Values**: `tagged`, `untagged`, `tagged phone`, `untagged phone`  

Specify if the phone traffic is tagged or untagged.
If both data and phone traffic are untagged, MAC-Based VLAN Assignment (MBVA) is used, if supported by the model of switch.

---

### platform_settings

**Type**: List, items: Dictionary  
**Path**: `platform_settings`  
**Default**: `See documentation`  

Platform settings. The first entry found where the `platform` node setting is fully matched by any regex in the `platforms` list will be chosen. If no matches are found, the first entry containing a platform `default` will be chosen. The default values will be overridden if `platform_settings` is defined. If you need to replace all the default platforms, it is recommended to copy the defaults and modify them. If you need to add custom platforms, create them under `custom_platform_settings`. Entries under `custom_platform_settings` will be matched before the equivalent entries from `platform_settings`.

---

### platform_speed_groups

**Type**: List, items: Dictionary  
**Path**: `platform_speed_groups`  

Set Hardware Speed Groups per Platform.

---

### pod_name

**Type**: String  
**Path**: `pod_name`  

POD Name is used in:
- Fabric Documentation (Optional, falls back to dc_name and then to fabric_name)
- SNMP Location: `snmp_settings.location` (Optional)
- VRF Loopbacks: `vtep_diagnostic.loopback_ip_pools.pod` (Required)

Recommended to be common between Spines and Leafs within a POD (One l3ls topology).


---

### port_control

**Type**: String  
**Path**: `<connected_endpoints_keys.key>.[].adapters.[].dot1x.port_control`  
**Valid Values**: `auto`, `force-authorized`, `force-unauthorized`  
---

### port_control

**Type**: String  
**Path**: `<custom_connected_endpoints_keys.key>.[].adapters.[].dot1x.port_control`  
**Valid Values**: `auto`, `force-authorized`, `force-unauthorized`  
---

### port_control

**Type**: String  
**Path**: `connected_endpoints.[].adapters.[].dot1x.port_control`  
**Valid Values**: `auto`, `force-authorized`, `force-unauthorized`  
---

### port_control

**Type**: String  
**Path**: `network_ports.[].dot1x.port_control`  
**Valid Values**: `auto`, `force-authorized`, `force-unauthorized`  
---

### port_control

**Type**: String  
**Path**: `port_profiles.[].dot1x.port_control`  
**Valid Values**: `auto`, `force-authorized`, `force-unauthorized`  
---

### port_profiles

**Type**: List, items: Dictionary  
**Path**: `port_profiles`  

Optional profiles to share common settings for connected_endpoints and/or network_ports.
Keys are the same used under endpoints adapters. Keys defined under endpoints adapters take precedence.


---

### preferred_metric

**Type**: String  
**Path**: `wan_virtual_topologies.control_plane_virtual_topology.metric_order.preferred_metric`  
**Valid Values**: `jitter`, `latency`, `load`, `loss-rate`  
---

### preferred_metric

**Type**: String  
**Path**: `wan_virtual_topologies.policies.[].application_virtual_topologies.[].metric_order.preferred_metric`  
**Valid Values**: `jitter`, `latency`, `load`, `loss-rate`  
---

### preferred_metric

**Type**: String  
**Path**: `wan_virtual_topologies.policies.[].default_virtual_topology.metric_order.preferred_metric`  
**Valid Values**: `jitter`, `latency`, `load`, `loss-rate`  
---

### priority

**Type**: String  
**Path**: `<connected_endpoints_keys.key>.[].adapters.[].poe.priority`  
**Valid Values**: `critical`, `high`, `medium`, `low`  

Prioritize a port's power in the event that one of the switch's power supplies loses power.

---

### priority

**Type**: String  
**Path**: `<custom_connected_endpoints_keys.key>.[].adapters.[].poe.priority`  
**Valid Values**: `critical`, `high`, `medium`, `low`  

Prioritize a port's power in the event that one of the switch's power supplies loses power.

---

### priority

**Type**: String  
**Path**: `connected_endpoints.[].adapters.[].poe.priority`  
**Valid Values**: `critical`, `high`, `medium`, `low`  

Prioritize a port's power in the event that one of the switch's power supplies loses power.

---

### priority

**Type**: String  
**Path**: `network_ports.[].poe.priority`  
**Valid Values**: `critical`, `high`, `medium`, `low`  

Prioritize a port's power in the event that one of the switch's power supplies loses power.

---

### priority

**Type**: String  
**Path**: `port_profiles.[].poe.priority`  
**Valid Values**: `critical`, `high`, `medium`, `low`  

Prioritize a port's power in the event that one of the switch's power supplies loses power.

---

### priv

**Type**: String  
**Path**: `snmp_settings.users.[].priv`  
**Valid Values**: `des`, `aes`, `aes192`, `aes256`  
---

### protection

**Type**: String  
**Path**: `isis_ti_lfa.protection`  
**Valid Values**: `link`, `node`  
---

### protocol

**Type**: String  
**Path**: `logging_settings.hosts.[].protocol`  
**Default**: `udp`  
**Valid Values**: `tcp`, `udp`, `tls`  
---

### protocol

**Type**: String  
**Path**: `redundancy.protocol`  
**Valid Values**: `sso`, `rpr`  
---

### ptp_settings

**Type**: Dictionary  
**Path**: `ptp_settings`  

Common PTP settings.

---

## R

### received

**Type**: String  
**Path**: `<connected_endpoints_keys.key>.[].adapters.[].flowcontrol.received`  
**Valid Values**: `desired`, `on`, `off`  
---

### received

**Type**: String  
**Path**: `<custom_connected_endpoints_keys.key>.[].adapters.[].flowcontrol.received`  
**Valid Values**: `desired`, `on`, `off`  
---

### received

**Type**: String  
**Path**: `connected_endpoints.[].adapters.[].flowcontrol.received`  
**Valid Values**: `desired`, `on`, `off`  
---

### received

**Type**: String  
**Path**: `network_ports.[].flowcontrol.received`  
**Valid Values**: `desired`, `on`, `off`  
---

### received

**Type**: String  
**Path**: `port_profiles.[].flowcontrol.received`  
**Valid Values**: `desired`, `on`, `off`  
---

### redundancy

**Type**: String  
**Path**: `<connected_endpoints_keys.key>.[].adapters.[].ethernet_segment.redundancy`  
**Valid Values**: `all-active`, `single-active`  

If omitted, Port-Channels use the EOS default of all-active.
If omitted, Ethernet interfaces are configured as single-active.


---

### redundancy

**Type**: String  
**Path**: `<custom_connected_endpoints_keys.key>.[].adapters.[].ethernet_segment.redundancy`  
**Valid Values**: `all-active`, `single-active`  

If omitted, Port-Channels use the EOS default of all-active.
If omitted, Ethernet interfaces are configured as single-active.


---

### redundancy

**Type**: String  
**Path**: `connected_endpoints.[].adapters.[].ethernet_segment.redundancy`  
**Valid Values**: `all-active`, `single-active`  

If omitted, Port-Channels use the EOS default of all-active.
If omitted, Ethernet interfaces are configured as single-active.


---

### redundancy

**Type**: String  
**Path**: `network_ports.[].ethernet_segment.redundancy`  
**Valid Values**: `all-active`, `single-active`  

If omitted, Port-Channels use the EOS default of all-active.
If omitted, Ethernet interfaces are configured as single-active.


---

### redundancy

**Type**: String  
**Path**: `port_profiles.[].ethernet_segment.redundancy`  
**Valid Values**: `all-active`, `single-active`  

If omitted, Port-Channels use the EOS default of all-active.
If omitted, Ethernet interfaces are configured as single-active.


---

### redundancy

**Type**: Dictionary  
**Path**: `redundancy`  

Redundancy for chassis platforms with dual supervisors | Optional.

---

### region

**Type**: String  
**Path**: `cv_settings.cvaas.clusters.[].region`  
**Default**: `auto`  
**Valid Values**: `auto`, `us-central1-a`, `us-central1-b`, `us-central1-c`, `apnortheast-1`, `euwest-2`, `ausoutheast-1`, `na-northeast1-b`, `uk-1`, `india-1`, `staging`, `dev`, `play`  

Optionally set the region to stream to.
The "auto" region will use 'apiserver.arista.io:443' which will redirect to the correct region based on the device's serial number.
"staging", "dev" and "play" are for internal Arista use.

---

### role

**Type**: String  
**Path**: `<connected_endpoints_keys.key>.[].adapters.[].monitor_sessions.[].role`  
**Valid Values**: `source`, `destination`  
---

### role

**Type**: String  
**Path**: `<custom_connected_endpoints_keys.key>.[].adapters.[].monitor_sessions.[].role`  
**Valid Values**: `source`, `destination`  
---

### role

**Type**: String  
**Path**: `<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].monitor_sessions.[].role`  
**Valid Values**: `source`, `destination`  
---

### role

**Type**: String  
**Path**: `connected_endpoints.[].adapters.[].monitor_sessions.[].role`  
**Valid Values**: `source`, `destination`  
---

### role

**Type**: String  
**Path**: `network_ports.[].monitor_sessions.[].role`  
**Valid Values**: `source`, `destination`  
---

### role

**Type**: String  
**Path**: `port_profiles.[].monitor_sessions.[].role`  
**Valid Values**: `source`, `destination`  
---

### router_id_loopback_description

**Type**: String  
**Path**: `router_id_loopback_description`  
**Default**: `ROUTER_ID`  

Customize the description on Router ID interface Loopback0.

---

### routing_protocol

**Type**: String  
**Path**: `core_interfaces.p2p_links_profiles.[].routing_protocol`  
**Valid Values**: `ebgp`  

Enables deviation of the routing protocol used on this link from the fabric underlay default.
- ebgp: Enforce plain IPv4 BGP peering and exempt the neighbor from the RFC5549 underlay if configured.

---

### routing_protocol

**Type**: String  
**Path**: `core_interfaces.p2p_links.[].routing_protocol`  
**Valid Values**: `ebgp`  

Enables deviation of the routing protocol used on this link from the fabric underlay default.
- ebgp: Enforce plain IPv4 BGP peering and exempt the neighbor from the RFC5549 underlay if configured.

---

### routing_protocol

**Type**: String  
**Path**: `l3_edge.p2p_links_profiles.[].routing_protocol`  
**Valid Values**: `ebgp`  

Enables deviation of the routing protocol used on this link from the fabric underlay default.
- ebgp: Enforce plain IPv4 BGP peering and exempt the neighbor from the RFC5549 underlay if configured.

---

### routing_protocol

**Type**: String  
**Path**: `l3_edge.p2p_links.[].routing_protocol`  
**Valid Values**: `ebgp`  

Enables deviation of the routing protocol used on this link from the fabric underlay default.
- ebgp: Enforce plain IPv4 BGP peering and exempt the neighbor from the RFC5549 underlay if configured.

---

## S

### serial_number

**Type**: String  
**Path**: `serial_number`  

Serial Number of the device.
Used for documentation purpose in the fabric documentation as can also be used by the 'cv_deploy' role.
"serial_number" can also be set directly under node type settings.
If both are set, the value under node type settings takes precedence.


---

### service

**Type**: String  
**Path**: `application_classification.categories.[].applications.[].service`  
**Valid Values**: `audio-video`, `chat`, `default`, `file-transfer`, `networking-protocols`, `peer-to-peer`, `software-update`  

Service Name.
Specific service to target for this application.
If no service is specified, all supported services of the application are matched.
Not all valid values are valid for all applications, check on EOS CLI.

---

### service

**Type**: String  
**Path**: `application_classification.application_profiles.[].applications.[].service`  
**Valid Values**: `audio-video`, `chat`, `default`, `file-transfer`, `networking-protocols`, `peer-to-peer`, `software-update`  

Service Name.
Specific service to target for this application.
If no service is specified, all supported services of the application are matched.
Not all valid values are valid for all applications, check on EOS CLI.

---

### service

**Type**: String  
**Path**: `application_classification.application_profiles.[].categories.[].service`  
**Valid Values**: `audio-video`, `chat`, `default`, `file-transfer`, `networking-protocols`, `peer-to-peer`, `software-update`  

Service Name.
Specific service to target for this application.
If no service is specified, all supported services of the application are matched.
Not all valid values are valid for all applications, check on EOS CLI.

---

### severity

**Type**: String  
**Path**: `logging_settings.level.[].severity`  
**Valid Values**: `alerts`, `critical`, `debugging`, `emergencies`, `errors`, `informational`, `notifications`, `warnings`, `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`  

Severity of facility. Below are the supported severities.
emergencies    System is unusable                (severity=0)
alerts         Immediate action needed           (severity=1)
critical       Critical conditions               (severity=2)
errors         Error conditions                  (severity=3)
warnings       Warning conditions                (severity=4)
notifications  Normal but significant conditions (severity=5)
informational  Informational messages            (severity=6)
debugging      Debugging messages                (severity=7)
<0-7>          Severity level value

---

### sflow_settings

**Type**: Dictionary  
**Path**: `sflow_settings`  

sFlow settings.
The sFlow process will only be configured if any interface is enabled for sFlow.
For default enabling of sFlow for various interface types across the fabric see `fabric_sflow`.

---

### shell

**Type**: String  
**Path**: `aaa_settings.local_users.[].shell`  
**Valid Values**: `/bin/bash`, `/bin/sh`, `/sbin/nologin`  

Specify shell for the user.


---

### shutdown_bgp_towards_undeployed_peers

**Type**: Boolean  
**Path**: `shutdown_bgp_towards_undeployed_peers`  
**Default**: `True`  

Administratively shuts down BGP peerings towards devices marked with `is_deployed: false`.

---

### shutdown_interfaces_towards_undeployed_peers

**Type**: Boolean  
**Path**: `shutdown_interfaces_towards_undeployed_peers`  
**Default**: `True`  

Administratively shuts down interfaces on deployed devices that connect to a peer marked with `is_deployed: false`.

---

### snmp_settings

**Type**: Dictionary  
**Path**: `snmp_settings`  

SNMP settings.
Configuration of remote SNMP engine IDs are currently only possible using `structured_config`.

---

### source_interfaces

**Type**: Dictionary  
**Path**: `source_interfaces`  

Configure source-interfaces based on the management interfaces set for other AVD Design data models.
By default, no source-interfaces will be configured. They can still be configured manually using `eos_cli_config_gen` and custom structured configuration.
EOS supports a single source-interface per VRF, so an error will be raised in case of conflicts.
Errors will also be raised if an interface is not found for a device.

---

### source_ports_match

**Type**: String  
**Path**: `ipv4_acls.[].entries.[].source_ports_match`  
**Default**: `eq`  
**Valid Values**: `eq`, `gt`, `lt`, `neq`, `range`  
---

### spanning_tree_bpdufilter

**Type**: String  
**Path**: `<connected_endpoints_keys.key>.[].adapters.[].spanning_tree_bpdufilter`  
**Valid Values**: `enabled`, `disabled`, `True`, `False`, `true`, `false`  
---

### spanning_tree_bpdufilter

**Type**: String  
**Path**: `<custom_connected_endpoints_keys.key>.[].adapters.[].spanning_tree_bpdufilter`  
**Valid Values**: `enabled`, `disabled`, `True`, `False`, `true`, `false`  
---

### spanning_tree_bpdufilter

**Type**: String  
**Path**: `connected_endpoints.[].adapters.[].spanning_tree_bpdufilter`  
**Valid Values**: `enabled`, `disabled`, `True`, `False`, `true`, `false`  
---

### spanning_tree_bpdufilter

**Type**: String  
**Path**: `network_ports.[].spanning_tree_bpdufilter`  
**Valid Values**: `enabled`, `disabled`, `True`, `False`, `true`, `false`  
---

### spanning_tree_bpdufilter

**Type**: String  
**Path**: `port_profiles.[].spanning_tree_bpdufilter`  
**Valid Values**: `enabled`, `disabled`, `True`, `False`, `true`, `false`  
---

### spanning_tree_bpduguard

**Type**: String  
**Path**: `<connected_endpoints_keys.key>.[].adapters.[].spanning_tree_bpduguard`  
**Valid Values**: `enabled`, `disabled`, `True`, `False`, `true`, `false`  
---

### spanning_tree_bpduguard

**Type**: String  
**Path**: `<custom_connected_endpoints_keys.key>.[].adapters.[].spanning_tree_bpduguard`  
**Valid Values**: `enabled`, `disabled`, `True`, `False`, `true`, `false`  
---

### spanning_tree_bpduguard

**Type**: String  
**Path**: `connected_endpoints.[].adapters.[].spanning_tree_bpduguard`  
**Valid Values**: `enabled`, `disabled`, `True`, `False`, `true`, `false`  
---

### spanning_tree_bpduguard

**Type**: String  
**Path**: `network_ports.[].spanning_tree_bpduguard`  
**Valid Values**: `enabled`, `disabled`, `True`, `False`, `true`, `false`  
---

### spanning_tree_bpduguard

**Type**: String  
**Path**: `port_profiles.[].spanning_tree_bpduguard`  
**Valid Values**: `enabled`, `disabled`, `True`, `False`, `true`, `false`  
---

### spanning_tree_mode

**Type**: String  
**Path**: `<node_type_keys.key>.defaults.spanning_tree_mode`  
**Valid Values**: `mstp`, `rstp`, `rapid-pvst`, `none`  
---

### spanning_tree_mode

**Type**: String  
**Path**: `<node_type_keys.key>.node_groups.[].nodes.[].spanning_tree_mode`  
**Valid Values**: `mstp`, `rstp`, `rapid-pvst`, `none`  
---

### spanning_tree_mode

**Type**: String  
**Path**: `<node_type_keys.key>.node_groups.[].spanning_tree_mode`  
**Valid Values**: `mstp`, `rstp`, `rapid-pvst`, `none`  
---

### spanning_tree_mode

**Type**: String  
**Path**: `<node_type_keys.key>.nodes.[].spanning_tree_mode`  
**Valid Values**: `mstp`, `rstp`, `rapid-pvst`, `none`  
---

### spanning_tree_mode

**Type**: String  
**Path**: `device_profiles.[].spanning_tree_mode`  
**Valid Values**: `mstp`, `rstp`, `rapid-pvst`, `none`  
---

### spanning_tree_mode

**Type**: String  
**Path**: `devices.[].spanning_tree_mode`  
**Valid Values**: `mstp`, `rstp`, `rapid-pvst`, `none`  
---

### spanning_tree_portfast

**Type**: String  
**Path**: `<connected_endpoints_keys.key>.[].adapters.[].spanning_tree_portfast`  
**Valid Values**: `edge`, `network`  
---

### spanning_tree_portfast

**Type**: String  
**Path**: `<custom_connected_endpoints_keys.key>.[].adapters.[].spanning_tree_portfast`  
**Valid Values**: `edge`, `network`  
---

### spanning_tree_portfast

**Type**: String  
**Path**: `connected_endpoints.[].adapters.[].spanning_tree_portfast`  
**Valid Values**: `edge`, `network`  
---

### spanning_tree_portfast

**Type**: String  
**Path**: `network_ports.[].spanning_tree_portfast`  
**Valid Values**: `edge`, `network`  
---

### spanning_tree_portfast

**Type**: String  
**Path**: `port_profiles.[].spanning_tree_portfast`  
**Valid Values**: `edge`, `network`  
---

### speed

**Type**: String  
**Path**: `<connected_endpoints_keys.key>.[].adapters.[].speed`  
**Valid Values**: `100full`, `100g`, `100g-1`, `100g-2`, `100g-4`, `100half`, `10full`, `10g`, `10half`, `1g`, `200g`, `200g-2`, `200g-4`, `25g`, `400g`, `400g-4`, `400g-8`, `40g`, `50g`, `50g-1`, `50g-2`, `800g-8`, `sfp-1000baset auto 100full`, `1.6t-8`, `100mfull`, `100mhalf`, `10mfull`, `10mhalf`, `200g-1`, `400g-2`, `40g-4`, `800g-4`, `auto`, `auto 10000full`, `auto 1000full`, `auto 100full`, `auto 100g-1`, `auto 100g-2`, `auto 100g-4`, `auto 100gfull`, `auto 100half`, `auto 10full`, `auto 10gfull`, `auto 10half`, `auto 1gfull`, `auto 2.5gfull`, `auto 200g-2`, `auto 200g-4`, `auto 25gfull`, `auto 400g-4`, `auto 400g-8`, `auto 40gfull`, `auto 50g-1`, `auto 50g-2`, `auto 50gfull`, `auto 5gfull`, `auto 800g-8`, `auto 1.6t-8`, `auto 100mfull`, `auto 100mhalf`, `auto 10g`, `auto 10mfull`, `auto 10mhalf`, `auto 1g`, `auto 2.5g`, `auto 200g-1`, `auto 25g`, `auto 400g-2`, `auto 40g-4`, `auto 5g`, `auto 800g-4`, `forced 10000full`, `forced 1000full`, `forced 1000half`, `forced 100full`, `forced 100gfull`, `forced 100half`, `forced 10full`, `forced 10half`, `forced 25gfull`, `forced 40gfull`, `forced 50gfull`  

Set adapter speed.
If not specified speed will be auto.


---

### speed

**Type**: String  
**Path**: `<custom_connected_endpoints_keys.key>.[].adapters.[].speed`  
**Valid Values**: `100full`, `100g`, `100g-1`, `100g-2`, `100g-4`, `100half`, `10full`, `10g`, `10half`, `1g`, `200g`, `200g-2`, `200g-4`, `25g`, `400g`, `400g-4`, `400g-8`, `40g`, `50g`, `50g-1`, `50g-2`, `800g-8`, `sfp-1000baset auto 100full`, `1.6t-8`, `100mfull`, `100mhalf`, `10mfull`, `10mhalf`, `200g-1`, `400g-2`, `40g-4`, `800g-4`, `auto`, `auto 10000full`, `auto 1000full`, `auto 100full`, `auto 100g-1`, `auto 100g-2`, `auto 100g-4`, `auto 100gfull`, `auto 100half`, `auto 10full`, `auto 10gfull`, `auto 10half`, `auto 1gfull`, `auto 2.5gfull`, `auto 200g-2`, `auto 200g-4`, `auto 25gfull`, `auto 400g-4`, `auto 400g-8`, `auto 40gfull`, `auto 50g-1`, `auto 50g-2`, `auto 50gfull`, `auto 5gfull`, `auto 800g-8`, `auto 1.6t-8`, `auto 100mfull`, `auto 100mhalf`, `auto 10g`, `auto 10mfull`, `auto 10mhalf`, `auto 1g`, `auto 2.5g`, `auto 200g-1`, `auto 25g`, `auto 400g-2`, `auto 40g-4`, `auto 5g`, `auto 800g-4`, `forced 10000full`, `forced 1000full`, `forced 1000half`, `forced 100full`, `forced 100gfull`, `forced 100half`, `forced 10full`, `forced 10half`, `forced 25gfull`, `forced 40gfull`, `forced 50gfull`  

Set adapter speed.
If not specified speed will be auto.


---

### speed

**Type**: String  
**Path**: `<network_services_keys.name>.[].vrfs.[].l3_port_channels.[].member_interfaces.[].speed`  
**Valid Values**: `100full`, `100g`, `100g-1`, `100g-2`, `100g-4`, `100half`, `10full`, `10g`, `10half`, `1g`, `200g`, `200g-2`, `200g-4`, `25g`, `400g`, `400g-4`, `400g-8`, `40g`, `50g`, `50g-1`, `50g-2`, `800g-8`, `sfp-1000baset auto 100full`, `1.6t-8`, `100mfull`, `100mhalf`, `10mfull`, `10mhalf`, `200g-1`, `400g-2`, `40g-4`, `800g-4`, `auto`, `auto 10000full`, `auto 1000full`, `auto 100full`, `auto 100g-1`, `auto 100g-2`, `auto 100g-4`, `auto 100gfull`, `auto 100half`, `auto 10full`, `auto 10gfull`, `auto 10half`, `auto 1gfull`, `auto 2.5gfull`, `auto 200g-2`, `auto 200g-4`, `auto 25gfull`, `auto 400g-4`, `auto 400g-8`, `auto 40gfull`, `auto 50g-1`, `auto 50g-2`, `auto 50gfull`, `auto 5gfull`, `auto 800g-8`, `auto 1.6t-8`, `auto 100mfull`, `auto 100mhalf`, `auto 10g`, `auto 10mfull`, `auto 10mhalf`, `auto 1g`, `auto 2.5g`, `auto 200g-1`, `auto 25g`, `auto 400g-2`, `auto 40g-4`, `auto 5g`, `auto 800g-4`, `forced 10000full`, `forced 1000full`, `forced 1000half`, `forced 100full`, `forced 100gfull`, `forced 100half`, `forced 10full`, `forced 10half`, `forced 25gfull`, `forced 40gfull`, `forced 50gfull`  

Interface Speed.

---

### speed

**Type**: String  
**Path**: `<node_type_keys.key>.defaults.l3_interfaces.[].speed`  
**Valid Values**: `100full`, `100g`, `100g-1`, `100g-2`, `100g-4`, `100half`, `10full`, `10g`, `10half`, `1g`, `200g`, `200g-2`, `200g-4`, `25g`, `400g`, `400g-4`, `400g-8`, `40g`, `50g`, `50g-1`, `50g-2`, `800g-8`, `sfp-1000baset auto 100full`, `1.6t-8`, `100mfull`, `100mhalf`, `10mfull`, `10mhalf`, `200g-1`, `400g-2`, `40g-4`, `800g-4`, `auto`, `auto 10000full`, `auto 1000full`, `auto 100full`, `auto 100g-1`, `auto 100g-2`, `auto 100g-4`, `auto 100gfull`, `auto 100half`, `auto 10full`, `auto 10gfull`, `auto 10half`, `auto 1gfull`, `auto 2.5gfull`, `auto 200g-2`, `auto 200g-4`, `auto 25gfull`, `auto 400g-4`, `auto 400g-8`, `auto 40gfull`, `auto 50g-1`, `auto 50g-2`, `auto 50gfull`, `auto 5gfull`, `auto 800g-8`, `auto 1.6t-8`, `auto 100mfull`, `auto 100mhalf`, `auto 10g`, `auto 10mfull`, `auto 10mhalf`, `auto 1g`, `auto 2.5g`, `auto 200g-1`, `auto 25g`, `auto 400g-2`, `auto 40g-4`, `auto 5g`, `auto 800g-4`, `forced 10000full`, `forced 1000full`, `forced 1000half`, `forced 100full`, `forced 100gfull`, `forced 100half`, `forced 10full`, `forced 10half`, `forced 25gfull`, `forced 40gfull`, `forced 50gfull`  

Interface Speed.

---

### speed

**Type**: String  
**Path**: `<node_type_keys.key>.defaults.l3_port_channels.[].member_interfaces.[].speed`  
**Valid Values**: `100full`, `100g`, `100g-1`, `100g-2`, `100g-4`, `100half`, `10full`, `10g`, `10half`, `1g`, `200g`, `200g-2`, `200g-4`, `25g`, `400g`, `400g-4`, `400g-8`, `40g`, `50g`, `50g-1`, `50g-2`, `800g-8`, `sfp-1000baset auto 100full`, `1.6t-8`, `100mfull`, `100mhalf`, `10mfull`, `10mhalf`, `200g-1`, `400g-2`, `40g-4`, `800g-4`, `auto`, `auto 10000full`, `auto 1000full`, `auto 100full`, `auto 100g-1`, `auto 100g-2`, `auto 100g-4`, `auto 100gfull`, `auto 100half`, `auto 10full`, `auto 10gfull`, `auto 10half`, `auto 1gfull`, `auto 2.5gfull`, `auto 200g-2`, `auto 200g-4`, `auto 25gfull`, `auto 400g-4`, `auto 400g-8`, `auto 40gfull`, `auto 50g-1`, `auto 50g-2`, `auto 50gfull`, `auto 5gfull`, `auto 800g-8`, `auto 1.6t-8`, `auto 100mfull`, `auto 100mhalf`, `auto 10g`, `auto 10mfull`, `auto 10mhalf`, `auto 1g`, `auto 2.5g`, `auto 200g-1`, `auto 25g`, `auto 400g-2`, `auto 40g-4`, `auto 5g`, `auto 800g-4`, `forced 10000full`, `forced 1000full`, `forced 1000half`, `forced 100full`, `forced 100gfull`, `forced 100half`, `forced 10full`, `forced 10half`, `forced 25gfull`, `forced 40gfull`, `forced 50gfull`  

Interface Speed.

---

### speed

**Type**: String  
**Path**: `<node_type_keys.key>.node_groups.[].nodes.[].l3_interfaces.[].speed`  
**Valid Values**: `100full`, `100g`, `100g-1`, `100g-2`, `100g-4`, `100half`, `10full`, `10g`, `10half`, `1g`, `200g`, `200g-2`, `200g-4`, `25g`, `400g`, `400g-4`, `400g-8`, `40g`, `50g`, `50g-1`, `50g-2`, `800g-8`, `sfp-1000baset auto 100full`, `1.6t-8`, `100mfull`, `100mhalf`, `10mfull`, `10mhalf`, `200g-1`, `400g-2`, `40g-4`, `800g-4`, `auto`, `auto 10000full`, `auto 1000full`, `auto 100full`, `auto 100g-1`, `auto 100g-2`, `auto 100g-4`, `auto 100gfull`, `auto 100half`, `auto 10full`, `auto 10gfull`, `auto 10half`, `auto 1gfull`, `auto 2.5gfull`, `auto 200g-2`, `auto 200g-4`, `auto 25gfull`, `auto 400g-4`, `auto 400g-8`, `auto 40gfull`, `auto 50g-1`, `auto 50g-2`, `auto 50gfull`, `auto 5gfull`, `auto 800g-8`, `auto 1.6t-8`, `auto 100mfull`, `auto 100mhalf`, `auto 10g`, `auto 10mfull`, `auto 10mhalf`, `auto 1g`, `auto 2.5g`, `auto 200g-1`, `auto 25g`, `auto 400g-2`, `auto 40g-4`, `auto 5g`, `auto 800g-4`, `forced 10000full`, `forced 1000full`, `forced 1000half`, `forced 100full`, `forced 100gfull`, `forced 100half`, `forced 10full`, `forced 10half`, `forced 25gfull`, `forced 40gfull`, `forced 50gfull`  

Interface Speed.

---

### speed

**Type**: String  
**Path**: `<node_type_keys.key>.node_groups.[].nodes.[].l3_port_channels.[].member_interfaces.[].speed`  
**Valid Values**: `100full`, `100g`, `100g-1`, `100g-2`, `100g-4`, `100half`, `10full`, `10g`, `10half`, `1g`, `200g`, `200g-2`, `200g-4`, `25g`, `400g`, `400g-4`, `400g-8`, `40g`, `50g`, `50g-1`, `50g-2`, `800g-8`, `sfp-1000baset auto 100full`, `1.6t-8`, `100mfull`, `100mhalf`, `10mfull`, `10mhalf`, `200g-1`, `400g-2`, `40g-4`, `800g-4`, `auto`, `auto 10000full`, `auto 1000full`, `auto 100full`, `auto 100g-1`, `auto 100g-2`, `auto 100g-4`, `auto 100gfull`, `auto 100half`, `auto 10full`, `auto 10gfull`, `auto 10half`, `auto 1gfull`, `auto 2.5gfull`, `auto 200g-2`, `auto 200g-4`, `auto 25gfull`, `auto 400g-4`, `auto 400g-8`, `auto 40gfull`, `auto 50g-1`, `auto 50g-2`, `auto 50gfull`, `auto 5gfull`, `auto 800g-8`, `auto 1.6t-8`, `auto 100mfull`, `auto 100mhalf`, `auto 10g`, `auto 10mfull`, `auto 10mhalf`, `auto 1g`, `auto 2.5g`, `auto 200g-1`, `auto 25g`, `auto 400g-2`, `auto 40g-4`, `auto 5g`, `auto 800g-4`, `forced 10000full`, `forced 1000full`, `forced 1000half`, `forced 100full`, `forced 100gfull`, `forced 100half`, `forced 10full`, `forced 10half`, `forced 25gfull`, `forced 40gfull`, `forced 50gfull`  

Interface Speed.

---

### speed

**Type**: String  
**Path**: `<node_type_keys.key>.node_groups.[].l3_interfaces.[].speed`  
**Valid Values**: `100full`, `100g`, `100g-1`, `100g-2`, `100g-4`, `100half`, `10full`, `10g`, `10half`, `1g`, `200g`, `200g-2`, `200g-4`, `25g`, `400g`, `400g-4`, `400g-8`, `40g`, `50g`, `50g-1`, `50g-2`, `800g-8`, `sfp-1000baset auto 100full`, `1.6t-8`, `100mfull`, `100mhalf`, `10mfull`, `10mhalf`, `200g-1`, `400g-2`, `40g-4`, `800g-4`, `auto`, `auto 10000full`, `auto 1000full`, `auto 100full`, `auto 100g-1`, `auto 100g-2`, `auto 100g-4`, `auto 100gfull`, `auto 100half`, `auto 10full`, `auto 10gfull`, `auto 10half`, `auto 1gfull`, `auto 2.5gfull`, `auto 200g-2`, `auto 200g-4`, `auto 25gfull`, `auto 400g-4`, `auto 400g-8`, `auto 40gfull`, `auto 50g-1`, `auto 50g-2`, `auto 50gfull`, `auto 5gfull`, `auto 800g-8`, `auto 1.6t-8`, `auto 100mfull`, `auto 100mhalf`, `auto 10g`, `auto 10mfull`, `auto 10mhalf`, `auto 1g`, `auto 2.5g`, `auto 200g-1`, `auto 25g`, `auto 400g-2`, `auto 40g-4`, `auto 5g`, `auto 800g-4`, `forced 10000full`, `forced 1000full`, `forced 1000half`, `forced 100full`, `forced 100gfull`, `forced 100half`, `forced 10full`, `forced 10half`, `forced 25gfull`, `forced 40gfull`, `forced 50gfull`  

Interface Speed.

---

### speed

**Type**: String  
**Path**: `<node_type_keys.key>.node_groups.[].l3_port_channels.[].member_interfaces.[].speed`  
**Valid Values**: `100full`, `100g`, `100g-1`, `100g-2`, `100g-4`, `100half`, `10full`, `10g`, `10half`, `1g`, `200g`, `200g-2`, `200g-4`, `25g`, `400g`, `400g-4`, `400g-8`, `40g`, `50g`, `50g-1`, `50g-2`, `800g-8`, `sfp-1000baset auto 100full`, `1.6t-8`, `100mfull`, `100mhalf`, `10mfull`, `10mhalf`, `200g-1`, `400g-2`, `40g-4`, `800g-4`, `auto`, `auto 10000full`, `auto 1000full`, `auto 100full`, `auto 100g-1`, `auto 100g-2`, `auto 100g-4`, `auto 100gfull`, `auto 100half`, `auto 10full`, `auto 10gfull`, `auto 10half`, `auto 1gfull`, `auto 2.5gfull`, `auto 200g-2`, `auto 200g-4`, `auto 25gfull`, `auto 400g-4`, `auto 400g-8`, `auto 40gfull`, `auto 50g-1`, `auto 50g-2`, `auto 50gfull`, `auto 5gfull`, `auto 800g-8`, `auto 1.6t-8`, `auto 100mfull`, `auto 100mhalf`, `auto 10g`, `auto 10mfull`, `auto 10mhalf`, `auto 1g`, `auto 2.5g`, `auto 200g-1`, `auto 25g`, `auto 400g-2`, `auto 40g-4`, `auto 5g`, `auto 800g-4`, `forced 10000full`, `forced 1000full`, `forced 1000half`, `forced 100full`, `forced 100gfull`, `forced 100half`, `forced 10full`, `forced 10half`, `forced 25gfull`, `forced 40gfull`, `forced 50gfull`  

Interface Speed.

---

### speed

**Type**: String  
**Path**: `<node_type_keys.key>.nodes.[].l3_interfaces.[].speed`  
**Valid Values**: `100full`, `100g`, `100g-1`, `100g-2`, `100g-4`, `100half`, `10full`, `10g`, `10half`, `1g`, `200g`, `200g-2`, `200g-4`, `25g`, `400g`, `400g-4`, `400g-8`, `40g`, `50g`, `50g-1`, `50g-2`, `800g-8`, `sfp-1000baset auto 100full`, `1.6t-8`, `100mfull`, `100mhalf`, `10mfull`, `10mhalf`, `200g-1`, `400g-2`, `40g-4`, `800g-4`, `auto`, `auto 10000full`, `auto 1000full`, `auto 100full`, `auto 100g-1`, `auto 100g-2`, `auto 100g-4`, `auto 100gfull`, `auto 100half`, `auto 10full`, `auto 10gfull`, `auto 10half`, `auto 1gfull`, `auto 2.5gfull`, `auto 200g-2`, `auto 200g-4`, `auto 25gfull`, `auto 400g-4`, `auto 400g-8`, `auto 40gfull`, `auto 50g-1`, `auto 50g-2`, `auto 50gfull`, `auto 5gfull`, `auto 800g-8`, `auto 1.6t-8`, `auto 100mfull`, `auto 100mhalf`, `auto 10g`, `auto 10mfull`, `auto 10mhalf`, `auto 1g`, `auto 2.5g`, `auto 200g-1`, `auto 25g`, `auto 400g-2`, `auto 40g-4`, `auto 5g`, `auto 800g-4`, `forced 10000full`, `forced 1000full`, `forced 1000half`, `forced 100full`, `forced 100gfull`, `forced 100half`, `forced 10full`, `forced 10half`, `forced 25gfull`, `forced 40gfull`, `forced 50gfull`  

Interface Speed.

---

### speed

**Type**: String  
**Path**: `<node_type_keys.key>.nodes.[].l3_port_channels.[].member_interfaces.[].speed`  
**Valid Values**: `100full`, `100g`, `100g-1`, `100g-2`, `100g-4`, `100half`, `10full`, `10g`, `10half`, `1g`, `200g`, `200g-2`, `200g-4`, `25g`, `400g`, `400g-4`, `400g-8`, `40g`, `50g`, `50g-1`, `50g-2`, `800g-8`, `sfp-1000baset auto 100full`, `1.6t-8`, `100mfull`, `100mhalf`, `10mfull`, `10mhalf`, `200g-1`, `400g-2`, `40g-4`, `800g-4`, `auto`, `auto 10000full`, `auto 1000full`, `auto 100full`, `auto 100g-1`, `auto 100g-2`, `auto 100g-4`, `auto 100gfull`, `auto 100half`, `auto 10full`, `auto 10gfull`, `auto 10half`, `auto 1gfull`, `auto 2.5gfull`, `auto 200g-2`, `auto 200g-4`, `auto 25gfull`, `auto 400g-4`, `auto 400g-8`, `auto 40gfull`, `auto 50g-1`, `auto 50g-2`, `auto 50gfull`, `auto 5gfull`, `auto 800g-8`, `auto 1.6t-8`, `auto 100mfull`, `auto 100mhalf`, `auto 10g`, `auto 10mfull`, `auto 10mhalf`, `auto 1g`, `auto 2.5g`, `auto 200g-1`, `auto 25g`, `auto 400g-2`, `auto 40g-4`, `auto 5g`, `auto 800g-4`, `forced 10000full`, `forced 1000full`, `forced 1000half`, `forced 100full`, `forced 100gfull`, `forced 100half`, `forced 10full`, `forced 10half`, `forced 25gfull`, `forced 40gfull`, `forced 50gfull`  

Interface Speed.

---

### speed

**Type**: String  
**Path**: `connected_endpoints.[].adapters.[].speed`  
**Valid Values**: `100full`, `100g`, `100g-1`, `100g-2`, `100g-4`, `100half`, `10full`, `10g`, `10half`, `1g`, `200g`, `200g-2`, `200g-4`, `25g`, `400g`, `400g-4`, `400g-8`, `40g`, `50g`, `50g-1`, `50g-2`, `800g-8`, `sfp-1000baset auto 100full`, `1.6t-8`, `100mfull`, `100mhalf`, `10mfull`, `10mhalf`, `200g-1`, `400g-2`, `40g-4`, `800g-4`, `auto`, `auto 10000full`, `auto 1000full`, `auto 100full`, `auto 100g-1`, `auto 100g-2`, `auto 100g-4`, `auto 100gfull`, `auto 100half`, `auto 10full`, `auto 10gfull`, `auto 10half`, `auto 1gfull`, `auto 2.5gfull`, `auto 200g-2`, `auto 200g-4`, `auto 25gfull`, `auto 400g-4`, `auto 400g-8`, `auto 40gfull`, `auto 50g-1`, `auto 50g-2`, `auto 50gfull`, `auto 5gfull`, `auto 800g-8`, `auto 1.6t-8`, `auto 100mfull`, `auto 100mhalf`, `auto 10g`, `auto 10mfull`, `auto 10mhalf`, `auto 1g`, `auto 2.5g`, `auto 200g-1`, `auto 25g`, `auto 400g-2`, `auto 40g-4`, `auto 5g`, `auto 800g-4`, `forced 10000full`, `forced 1000full`, `forced 1000half`, `forced 100full`, `forced 100gfull`, `forced 100half`, `forced 10full`, `forced 10half`, `forced 25gfull`, `forced 40gfull`, `forced 50gfull`  

Set adapter speed.
If not specified speed will be auto.


---

### speed

**Type**: String  
**Path**: `core_interfaces.p2p_links_profiles.[].speed`  
**Valid Values**: `100full`, `100g`, `100g-1`, `100g-2`, `100g-4`, `100half`, `10full`, `10g`, `10half`, `1g`, `200g`, `200g-2`, `200g-4`, `25g`, `400g`, `400g-4`, `400g-8`, `40g`, `50g`, `50g-1`, `50g-2`, `800g-8`, `sfp-1000baset auto 100full`, `1.6t-8`, `100mfull`, `100mhalf`, `10mfull`, `10mhalf`, `200g-1`, `400g-2`, `40g-4`, `800g-4`, `auto`, `auto 10000full`, `auto 1000full`, `auto 100full`, `auto 100g-1`, `auto 100g-2`, `auto 100g-4`, `auto 100gfull`, `auto 100half`, `auto 10full`, `auto 10gfull`, `auto 10half`, `auto 1gfull`, `auto 2.5gfull`, `auto 200g-2`, `auto 200g-4`, `auto 25gfull`, `auto 400g-4`, `auto 400g-8`, `auto 40gfull`, `auto 50g-1`, `auto 50g-2`, `auto 50gfull`, `auto 5gfull`, `auto 800g-8`, `auto 1.6t-8`, `auto 100mfull`, `auto 100mhalf`, `auto 10g`, `auto 10mfull`, `auto 10mhalf`, `auto 1g`, `auto 2.5g`, `auto 200g-1`, `auto 25g`, `auto 400g-2`, `auto 40g-4`, `auto 5g`, `auto 800g-4`, `forced 10000full`, `forced 1000full`, `forced 1000half`, `forced 100full`, `forced 100gfull`, `forced 100half`, `forced 10full`, `forced 10half`, `forced 25gfull`, `forced 40gfull`, `forced 50gfull`  

Interface Speed.

---

### speed

**Type**: String  
**Path**: `core_interfaces.p2p_links.[].speed`  
**Valid Values**: `100full`, `100g`, `100g-1`, `100g-2`, `100g-4`, `100half`, `10full`, `10g`, `10half`, `1g`, `200g`, `200g-2`, `200g-4`, `25g`, `400g`, `400g-4`, `400g-8`, `40g`, `50g`, `50g-1`, `50g-2`, `800g-8`, `sfp-1000baset auto 100full`, `1.6t-8`, `100mfull`, `100mhalf`, `10mfull`, `10mhalf`, `200g-1`, `400g-2`, `40g-4`, `800g-4`, `auto`, `auto 10000full`, `auto 1000full`, `auto 100full`, `auto 100g-1`, `auto 100g-2`, `auto 100g-4`, `auto 100gfull`, `auto 100half`, `auto 10full`, `auto 10gfull`, `auto 10half`, `auto 1gfull`, `auto 2.5gfull`, `auto 200g-2`, `auto 200g-4`, `auto 25gfull`, `auto 400g-4`, `auto 400g-8`, `auto 40gfull`, `auto 50g-1`, `auto 50g-2`, `auto 50gfull`, `auto 5gfull`, `auto 800g-8`, `auto 1.6t-8`, `auto 100mfull`, `auto 100mhalf`, `auto 10g`, `auto 10mfull`, `auto 10mhalf`, `auto 1g`, `auto 2.5g`, `auto 200g-1`, `auto 25g`, `auto 400g-2`, `auto 40g-4`, `auto 5g`, `auto 800g-4`, `forced 10000full`, `forced 1000full`, `forced 1000half`, `forced 100full`, `forced 100gfull`, `forced 100half`, `forced 10full`, `forced 10half`, `forced 25gfull`, `forced 40gfull`, `forced 50gfull`  

Interface Speed.

---

### speed

**Type**: String  
**Path**: `device_profiles.[].l3_interfaces.[].speed`  
**Valid Values**: `100full`, `100g`, `100g-1`, `100g-2`, `100g-4`, `100half`, `10full`, `10g`, `10half`, `1g`, `200g`, `200g-2`, `200g-4`, `25g`, `400g`, `400g-4`, `400g-8`, `40g`, `50g`, `50g-1`, `50g-2`, `800g-8`, `sfp-1000baset auto 100full`, `1.6t-8`, `100mfull`, `100mhalf`, `10mfull`, `10mhalf`, `200g-1`, `400g-2`, `40g-4`, `800g-4`, `auto`, `auto 10000full`, `auto 1000full`, `auto 100full`, `auto 100g-1`, `auto 100g-2`, `auto 100g-4`, `auto 100gfull`, `auto 100half`, `auto 10full`, `auto 10gfull`, `auto 10half`, `auto 1gfull`, `auto 2.5gfull`, `auto 200g-2`, `auto 200g-4`, `auto 25gfull`, `auto 400g-4`, `auto 400g-8`, `auto 40gfull`, `auto 50g-1`, `auto 50g-2`, `auto 50gfull`, `auto 5gfull`, `auto 800g-8`, `auto 1.6t-8`, `auto 100mfull`, `auto 100mhalf`, `auto 10g`, `auto 10mfull`, `auto 10mhalf`, `auto 1g`, `auto 2.5g`, `auto 200g-1`, `auto 25g`, `auto 400g-2`, `auto 40g-4`, `auto 5g`, `auto 800g-4`, `forced 10000full`, `forced 1000full`, `forced 1000half`, `forced 100full`, `forced 100gfull`, `forced 100half`, `forced 10full`, `forced 10half`, `forced 25gfull`, `forced 40gfull`, `forced 50gfull`  

Interface Speed.

---

### speed

**Type**: String  
**Path**: `device_profiles.[].l3_port_channels.[].member_interfaces.[].speed`  
**Valid Values**: `100full`, `100g`, `100g-1`, `100g-2`, `100g-4`, `100half`, `10full`, `10g`, `10half`, `1g`, `200g`, `200g-2`, `200g-4`, `25g`, `400g`, `400g-4`, `400g-8`, `40g`, `50g`, `50g-1`, `50g-2`, `800g-8`, `sfp-1000baset auto 100full`, `1.6t-8`, `100mfull`, `100mhalf`, `10mfull`, `10mhalf`, `200g-1`, `400g-2`, `40g-4`, `800g-4`, `auto`, `auto 10000full`, `auto 1000full`, `auto 100full`, `auto 100g-1`, `auto 100g-2`, `auto 100g-4`, `auto 100gfull`, `auto 100half`, `auto 10full`, `auto 10gfull`, `auto 10half`, `auto 1gfull`, `auto 2.5gfull`, `auto 200g-2`, `auto 200g-4`, `auto 25gfull`, `auto 400g-4`, `auto 400g-8`, `auto 40gfull`, `auto 50g-1`, `auto 50g-2`, `auto 50gfull`, `auto 5gfull`, `auto 800g-8`, `auto 1.6t-8`, `auto 100mfull`, `auto 100mhalf`, `auto 10g`, `auto 10mfull`, `auto 10mhalf`, `auto 1g`, `auto 2.5g`, `auto 200g-1`, `auto 25g`, `auto 400g-2`, `auto 40g-4`, `auto 5g`, `auto 800g-4`, `forced 10000full`, `forced 1000full`, `forced 1000half`, `forced 100full`, `forced 100gfull`, `forced 100half`, `forced 10full`, `forced 10half`, `forced 25gfull`, `forced 40gfull`, `forced 50gfull`  

Interface Speed.

---

### speed

**Type**: String  
**Path**: `devices.[].l3_interfaces.[].speed`  
**Valid Values**: `100full`, `100g`, `100g-1`, `100g-2`, `100g-4`, `100half`, `10full`, `10g`, `10half`, `1g`, `200g`, `200g-2`, `200g-4`, `25g`, `400g`, `400g-4`, `400g-8`, `40g`, `50g`, `50g-1`, `50g-2`, `800g-8`, `sfp-1000baset auto 100full`, `1.6t-8`, `100mfull`, `100mhalf`, `10mfull`, `10mhalf`, `200g-1`, `400g-2`, `40g-4`, `800g-4`, `auto`, `auto 10000full`, `auto 1000full`, `auto 100full`, `auto 100g-1`, `auto 100g-2`, `auto 100g-4`, `auto 100gfull`, `auto 100half`, `auto 10full`, `auto 10gfull`, `auto 10half`, `auto 1gfull`, `auto 2.5gfull`, `auto 200g-2`, `auto 200g-4`, `auto 25gfull`, `auto 400g-4`, `auto 400g-8`, `auto 40gfull`, `auto 50g-1`, `auto 50g-2`, `auto 50gfull`, `auto 5gfull`, `auto 800g-8`, `auto 1.6t-8`, `auto 100mfull`, `auto 100mhalf`, `auto 10g`, `auto 10mfull`, `auto 10mhalf`, `auto 1g`, `auto 2.5g`, `auto 200g-1`, `auto 25g`, `auto 400g-2`, `auto 40g-4`, `auto 5g`, `auto 800g-4`, `forced 10000full`, `forced 1000full`, `forced 1000half`, `forced 100full`, `forced 100gfull`, `forced 100half`, `forced 10full`, `forced 10half`, `forced 25gfull`, `forced 40gfull`, `forced 50gfull`  

Interface Speed.

---

### speed

**Type**: String  
**Path**: `devices.[].l3_port_channels.[].member_interfaces.[].speed`  
**Valid Values**: `100full`, `100g`, `100g-1`, `100g-2`, `100g-4`, `100half`, `10full`, `10g`, `10half`, `1g`, `200g`, `200g-2`, `200g-4`, `25g`, `400g`, `400g-4`, `400g-8`, `40g`, `50g`, `50g-1`, `50g-2`, `800g-8`, `sfp-1000baset auto 100full`, `1.6t-8`, `100mfull`, `100mhalf`, `10mfull`, `10mhalf`, `200g-1`, `400g-2`, `40g-4`, `800g-4`, `auto`, `auto 10000full`, `auto 1000full`, `auto 100full`, `auto 100g-1`, `auto 100g-2`, `auto 100g-4`, `auto 100gfull`, `auto 100half`, `auto 10full`, `auto 10gfull`, `auto 10half`, `auto 1gfull`, `auto 2.5gfull`, `auto 200g-2`, `auto 200g-4`, `auto 25gfull`, `auto 400g-4`, `auto 400g-8`, `auto 40gfull`, `auto 50g-1`, `auto 50g-2`, `auto 50gfull`, `auto 5gfull`, `auto 800g-8`, `auto 1.6t-8`, `auto 100mfull`, `auto 100mhalf`, `auto 10g`, `auto 10mfull`, `auto 10mhalf`, `auto 1g`, `auto 2.5g`, `auto 200g-1`, `auto 25g`, `auto 400g-2`, `auto 40g-4`, `auto 5g`, `auto 800g-4`, `forced 10000full`, `forced 1000full`, `forced 1000half`, `forced 100full`, `forced 100gfull`, `forced 100half`, `forced 10full`, `forced 10half`, `forced 25gfull`, `forced 40gfull`, `forced 50gfull`  

Interface Speed.

---

### speed

**Type**: String  
**Path**: `l3_edge.p2p_links_profiles.[].speed`  
**Valid Values**: `100full`, `100g`, `100g-1`, `100g-2`, `100g-4`, `100half`, `10full`, `10g`, `10half`, `1g`, `200g`, `200g-2`, `200g-4`, `25g`, `400g`, `400g-4`, `400g-8`, `40g`, `50g`, `50g-1`, `50g-2`, `800g-8`, `sfp-1000baset auto 100full`, `1.6t-8`, `100mfull`, `100mhalf`, `10mfull`, `10mhalf`, `200g-1`, `400g-2`, `40g-4`, `800g-4`, `auto`, `auto 10000full`, `auto 1000full`, `auto 100full`, `auto 100g-1`, `auto 100g-2`, `auto 100g-4`, `auto 100gfull`, `auto 100half`, `auto 10full`, `auto 10gfull`, `auto 10half`, `auto 1gfull`, `auto 2.5gfull`, `auto 200g-2`, `auto 200g-4`, `auto 25gfull`, `auto 400g-4`, `auto 400g-8`, `auto 40gfull`, `auto 50g-1`, `auto 50g-2`, `auto 50gfull`, `auto 5gfull`, `auto 800g-8`, `auto 1.6t-8`, `auto 100mfull`, `auto 100mhalf`, `auto 10g`, `auto 10mfull`, `auto 10mhalf`, `auto 1g`, `auto 2.5g`, `auto 200g-1`, `auto 25g`, `auto 400g-2`, `auto 40g-4`, `auto 5g`, `auto 800g-4`, `forced 10000full`, `forced 1000full`, `forced 1000half`, `forced 100full`, `forced 100gfull`, `forced 100half`, `forced 10full`, `forced 10half`, `forced 25gfull`, `forced 40gfull`, `forced 50gfull`  

Interface Speed.

---

### speed

**Type**: String  
**Path**: `l3_edge.p2p_links.[].speed`  
**Valid Values**: `100full`, `100g`, `100g-1`, `100g-2`, `100g-4`, `100half`, `10full`, `10g`, `10half`, `1g`, `200g`, `200g-2`, `200g-4`, `25g`, `400g`, `400g-4`, `400g-8`, `40g`, `50g`, `50g-1`, `50g-2`, `800g-8`, `sfp-1000baset auto 100full`, `1.6t-8`, `100mfull`, `100mhalf`, `10mfull`, `10mhalf`, `200g-1`, `400g-2`, `40g-4`, `800g-4`, `auto`, `auto 10000full`, `auto 1000full`, `auto 100full`, `auto 100g-1`, `auto 100g-2`, `auto 100g-4`, `auto 100gfull`, `auto 100half`, `auto 10full`, `auto 10gfull`, `auto 10half`, `auto 1gfull`, `auto 2.5gfull`, `auto 200g-2`, `auto 200g-4`, `auto 25gfull`, `auto 400g-4`, `auto 400g-8`, `auto 40gfull`, `auto 50g-1`, `auto 50g-2`, `auto 50gfull`, `auto 5gfull`, `auto 800g-8`, `auto 1.6t-8`, `auto 100mfull`, `auto 100mhalf`, `auto 10g`, `auto 10mfull`, `auto 10mhalf`, `auto 1g`, `auto 2.5g`, `auto 200g-1`, `auto 25g`, `auto 400g-2`, `auto 40g-4`, `auto 5g`, `auto 800g-4`, `forced 10000full`, `forced 1000full`, `forced 1000half`, `forced 100full`, `forced 100gfull`, `forced 100half`, `forced 10full`, `forced 10half`, `forced 25gfull`, `forced 40gfull`, `forced 50gfull`  

Interface Speed.

---

### speed

**Type**: String  
**Path**: `l3_interface_profiles.[].speed`  
**Valid Values**: `100full`, `100g`, `100g-1`, `100g-2`, `100g-4`, `100half`, `10full`, `10g`, `10half`, `1g`, `200g`, `200g-2`, `200g-4`, `25g`, `400g`, `400g-4`, `400g-8`, `40g`, `50g`, `50g-1`, `50g-2`, `800g-8`, `sfp-1000baset auto 100full`, `1.6t-8`, `100mfull`, `100mhalf`, `10mfull`, `10mhalf`, `200g-1`, `400g-2`, `40g-4`, `800g-4`, `auto`, `auto 10000full`, `auto 1000full`, `auto 100full`, `auto 100g-1`, `auto 100g-2`, `auto 100g-4`, `auto 100gfull`, `auto 100half`, `auto 10full`, `auto 10gfull`, `auto 10half`, `auto 1gfull`, `auto 2.5gfull`, `auto 200g-2`, `auto 200g-4`, `auto 25gfull`, `auto 400g-4`, `auto 400g-8`, `auto 40gfull`, `auto 50g-1`, `auto 50g-2`, `auto 50gfull`, `auto 5gfull`, `auto 800g-8`, `auto 1.6t-8`, `auto 100mfull`, `auto 100mhalf`, `auto 10g`, `auto 10mfull`, `auto 10mhalf`, `auto 1g`, `auto 2.5g`, `auto 200g-1`, `auto 25g`, `auto 400g-2`, `auto 40g-4`, `auto 5g`, `auto 800g-4`, `forced 10000full`, `forced 1000full`, `forced 1000half`, `forced 100full`, `forced 100gfull`, `forced 100half`, `forced 10full`, `forced 10half`, `forced 25gfull`, `forced 40gfull`, `forced 50gfull`  

Interface Speed.

---

### speed

**Type**: String  
**Path**: `network_ports.[].speed`  
**Valid Values**: `100full`, `100g`, `100g-1`, `100g-2`, `100g-4`, `100half`, `10full`, `10g`, `10half`, `1g`, `200g`, `200g-2`, `200g-4`, `25g`, `400g`, `400g-4`, `400g-8`, `40g`, `50g`, `50g-1`, `50g-2`, `800g-8`, `sfp-1000baset auto 100full`, `1.6t-8`, `100mfull`, `100mhalf`, `10mfull`, `10mhalf`, `200g-1`, `400g-2`, `40g-4`, `800g-4`, `auto`, `auto 10000full`, `auto 1000full`, `auto 100full`, `auto 100g-1`, `auto 100g-2`, `auto 100g-4`, `auto 100gfull`, `auto 100half`, `auto 10full`, `auto 10gfull`, `auto 10half`, `auto 1gfull`, `auto 2.5gfull`, `auto 200g-2`, `auto 200g-4`, `auto 25gfull`, `auto 400g-4`, `auto 400g-8`, `auto 40gfull`, `auto 50g-1`, `auto 50g-2`, `auto 50gfull`, `auto 5gfull`, `auto 800g-8`, `auto 1.6t-8`, `auto 100mfull`, `auto 100mhalf`, `auto 10g`, `auto 10mfull`, `auto 10mhalf`, `auto 1g`, `auto 2.5g`, `auto 200g-1`, `auto 25g`, `auto 400g-2`, `auto 40g-4`, `auto 5g`, `auto 800g-4`, `forced 10000full`, `forced 1000full`, `forced 1000half`, `forced 100full`, `forced 100gfull`, `forced 100half`, `forced 10full`, `forced 10half`, `forced 25gfull`, `forced 40gfull`, `forced 50gfull`  

Set adapter speed.
If not specified speed will be auto.


---

### speed

**Type**: String  
**Path**: `port_profiles.[].speed`  
**Valid Values**: `100full`, `100g`, `100g-1`, `100g-2`, `100g-4`, `100half`, `10full`, `10g`, `10half`, `1g`, `200g`, `200g-2`, `200g-4`, `25g`, `400g`, `400g-4`, `400g-8`, `40g`, `50g`, `50g-1`, `50g-2`, `800g-8`, `sfp-1000baset auto 100full`, `1.6t-8`, `100mfull`, `100mhalf`, `10mfull`, `10mhalf`, `200g-1`, `400g-2`, `40g-4`, `800g-4`, `auto`, `auto 10000full`, `auto 1000full`, `auto 100full`, `auto 100g-1`, `auto 100g-2`, `auto 100g-4`, `auto 100gfull`, `auto 100half`, `auto 10full`, `auto 10gfull`, `auto 10half`, `auto 1gfull`, `auto 2.5gfull`, `auto 200g-2`, `auto 200g-4`, `auto 25gfull`, `auto 400g-4`, `auto 400g-8`, `auto 40gfull`, `auto 50g-1`, `auto 50g-2`, `auto 50gfull`, `auto 5gfull`, `auto 800g-8`, `auto 1.6t-8`, `auto 100mfull`, `auto 100mhalf`, `auto 10g`, `auto 10mfull`, `auto 10mhalf`, `auto 1g`, `auto 2.5g`, `auto 200g-1`, `auto 25g`, `auto 400g-2`, `auto 40g-4`, `auto 5g`, `auto 800g-4`, `forced 10000full`, `forced 1000full`, `forced 1000half`, `forced 100full`, `forced 100gfull`, `forced 100half`, `forced 10full`, `forced 10half`, `forced 25gfull`, `forced 40gfull`, `forced 50gfull`  

Set adapter speed.
If not specified speed will be auto.


---

### stage

**Type**: String  
**Path**: `event_handlers.[].trigger_on_maintenance.stage`  
**Valid Values**: `bgp`, `linkdown`, `mlag`, `ratemon`  

Action is triggered after/before specified stage.

---

### svi_profiles

**Type**: List, items: Dictionary  
**Path**: `svi_profiles`  

Profiles to share common settings for SVIs under `<network_services_key>.[].vrfs.svis`.
Keys are the same used under SVIs. Keys defined under SVIs take precedence.
Note: structured configuration is not merged recursively and will be taken directly from the most specific level in the following order:
1. svi.nodes[inventory_hostname].structured_config
2. svi_profile.nodes[inventory_hostname].structured_config
3. svi_parent_profile.nodes[inventory_hostname].structured_config
4. svi.structured_config
5. svi_profile.structured_config
6. svi_parent_profile.structured_config


---

### system_mac_address

**Type**: String  
**Path**: `system_mac_address`  

Set to the same MAC address as available in "show version" on the device.
"system_mac_address" can also be set under node type settings.
If both are set, the value under node type settings takes precedence.


---

## T

### time_duration_unit

**Type**: String  
**Path**: `<connected_endpoints_keys.key>.[].adapters.[].dot1x.aaa.unresponsive.action.cached_results_timeout.time_duration_unit`  
**Valid Values**: `days`, `hours`, `minutes`, `seconds`  
---

### time_duration_unit

**Type**: String  
**Path**: `<connected_endpoints_keys.key>.[].adapters.[].dot1x.aaa.unresponsive.phone_action.cached_results_timeout.time_duration_unit`  
**Valid Values**: `days`, `hours`, `minutes`, `seconds`  
---

### time_duration_unit

**Type**: String  
**Path**: `<custom_connected_endpoints_keys.key>.[].adapters.[].dot1x.aaa.unresponsive.action.cached_results_timeout.time_duration_unit`  
**Valid Values**: `days`, `hours`, `minutes`, `seconds`  
---

### time_duration_unit

**Type**: String  
**Path**: `<custom_connected_endpoints_keys.key>.[].adapters.[].dot1x.aaa.unresponsive.phone_action.cached_results_timeout.time_duration_unit`  
**Valid Values**: `days`, `hours`, `minutes`, `seconds`  
---

### time_duration_unit

**Type**: String  
**Path**: `connected_endpoints.[].adapters.[].dot1x.aaa.unresponsive.action.cached_results_timeout.time_duration_unit`  
**Valid Values**: `days`, `hours`, `minutes`, `seconds`  
---

### time_duration_unit

**Type**: String  
**Path**: `connected_endpoints.[].adapters.[].dot1x.aaa.unresponsive.phone_action.cached_results_timeout.time_duration_unit`  
**Valid Values**: `days`, `hours`, `minutes`, `seconds`  
---

### time_duration_unit

**Type**: String  
**Path**: `network_ports.[].dot1x.aaa.unresponsive.action.cached_results_timeout.time_duration_unit`  
**Valid Values**: `days`, `hours`, `minutes`, `seconds`  
---

### time_duration_unit

**Type**: String  
**Path**: `network_ports.[].dot1x.aaa.unresponsive.phone_action.cached_results_timeout.time_duration_unit`  
**Valid Values**: `days`, `hours`, `minutes`, `seconds`  
---

### time_duration_unit

**Type**: String  
**Path**: `port_profiles.[].dot1x.aaa.unresponsive.action.cached_results_timeout.time_duration_unit`  
**Valid Values**: `days`, `hours`, `minutes`, `seconds`  
---

### time_duration_unit

**Type**: String  
**Path**: `port_profiles.[].dot1x.aaa.unresponsive.phone_action.cached_results_timeout.time_duration_unit`  
**Valid Values**: `days`, `hours`, `minutes`, `seconds`  
---

### timestamp

**Type**: String  
**Path**: `logging_settings.format.timestamp`  
**Valid Values**: `high-resolution`, `traditional`, `traditional timezone`, `traditional year`, `traditional timezone year`, `traditional year timezone`  

Timestamp format.

---

### timezone

**Type**: String  
**Path**: `timezone`  

Clock timezone like "CET" or "US/Pacific".

---

### transport

**Type**: String  
**Path**: `ptp_profiles.[].transport`  
**Valid Values**: `ipv4`  
---

### trap

**Type**: String  
**Path**: `logging_settings.trap`  
**Valid Values**: `alerts`, `critical`, `debugging`, `emergencies`, `errors`, `informational`, `notifications`, `system`, `warnings`, `disabled`  

Trap logging severity level.

---

### trigger

**Type**: String  
**Path**: `event_handlers.[].trigger`  
**Valid Values**: `on-boot`, `on-counters`, `on-intf`, `on-logging`, `on-maintenance`, `on-startup-config`, `vm-tracer vm`  

Configure event trigger condition.


---

### ttl_match

**Type**: String  
**Path**: `ipv4_acls.[].entries.[].ttl_match`  
**Default**: `eq`  
**Valid Values**: `eq`, `gt`, `lt`, `neq`  
---

### type

**Type**: String  
**Path**: `<connected_endpoints_keys.key>.[].adapters.[].monitor_sessions.[].source_settings.access_group.type`  
**Valid Values**: `ip`, `ipv6`, `mac`  
---

### type

**Type**: String  
**Path**: `<connected_endpoints_keys.key>.[].adapters.[].monitor_sessions.[].session_settings.access_group.type`  
**Valid Values**: `ip`, `ipv6`, `mac`  
---

### type

**Type**: String  
**Path**: `<custom_connected_endpoints_keys.key>.[].adapters.[].monitor_sessions.[].source_settings.access_group.type`  
**Valid Values**: `ip`, `ipv6`, `mac`  
---

### type

**Type**: String  
**Path**: `<custom_connected_endpoints_keys.key>.[].adapters.[].monitor_sessions.[].session_settings.access_group.type`  
**Valid Values**: `ip`, `ipv6`, `mac`  
---

### type

**Type**: String  
**Path**: `<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].monitor_sessions.[].source_settings.access_group.type`  
**Valid Values**: `ip`, `ipv6`, `mac`  
---

### type

**Type**: String  
**Path**: `<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].monitor_sessions.[].session_settings.access_group.type`  
**Valid Values**: `ip`, `ipv6`, `mac`  
---

### type

**Type**: String  
**Path**: `<network_services_keys.name>.[].vrfs.[].additional_route_targets.[].type`  
**Valid Values**: `import`, `export`  
---

### type

**Type**: String  
**Path**: `<network_services_keys.name>.[].l2vlans.[].private_vlan.type`  
**Valid Values**: `community`, `isolated`  
---

### type

**Type**: String  
**Path**: `<network_services_keys.name>.[].point_to_point_services.[].type`  
**Default**: `vpws-pseudowire`  
**Valid Values**: `vpws-pseudowire`  
---

### type

**Type**: String  
**Path**: `aaa_settings.accounting.exec.console.type`  
**Valid Values**: `none`, `start-stop`, `stop-only`  
---

### type

**Type**: String  
**Path**: `aaa_settings.accounting.exec.default.type`  
**Valid Values**: `none`, `start-stop`, `stop-only`  
---

### type

**Type**: String  
**Path**: `aaa_settings.accounting.system.default.type`  
**Valid Values**: `none`, `start-stop`, `stop-only`  
---

### type

**Type**: String  
**Path**: `aaa_settings.accounting.commands.console.[].type`  
**Valid Values**: `none`, `start-stop`, `stop-only`  
---

### type

**Type**: String  
**Path**: `aaa_settings.accounting.commands.default.[].type`  
**Valid Values**: `none`, `start-stop`, `stop-only`  
---

### type

**Type**: String  
**Path**: `connected_endpoints.[].adapters.[].monitor_sessions.[].source_settings.access_group.type`  
**Valid Values**: `ip`, `ipv6`, `mac`  
---

### type

**Type**: String  
**Path**: `connected_endpoints.[].adapters.[].monitor_sessions.[].session_settings.access_group.type`  
**Valid Values**: `ip`, `ipv6`, `mac`  
---

### type

**Type**: String  
**Path**: `cv_pathfinder_internet_exit_policies.[].type`  
**Valid Values**: `direct`, `zscaler`  

Internet-exit policy type.
direct: Exit directly over wan interfaces
zscaler: Exit using Zscaler secure web gateway service

---

### type

**Type**: String  
**Path**: `l2vlan_profiles.[].private_vlan.type`  
**Valid Values**: `community`, `isolated`  
---

### type

**Type**: String  
**Path**: `network_ports.[].monitor_sessions.[].source_settings.access_group.type`  
**Valid Values**: `ip`, `ipv6`, `mac`  
---

### type

**Type**: String  
**Path**: `network_ports.[].monitor_sessions.[].session_settings.access_group.type`  
**Valid Values**: `ip`, `ipv6`, `mac`  
---

### type

**Type**: String  
**Path**: `port_profiles.[].monitor_sessions.[].source_settings.access_group.type`  
**Valid Values**: `ip`, `ipv6`, `mac`  
---

### type

**Type**: String  
**Path**: `port_profiles.[].monitor_sessions.[].session_settings.access_group.type`  
**Valid Values**: `ip`, `ipv6`, `mac`  
---

### type

**Type**: String  
**Path**: `type`  

The `type:` variable needs to be defined for each device in the fabric.
This is leveraged to load the appropriate template to generate the configuration.


---

## U

### underlay_filter_peer_as

**Type**: Boolean  
**Path**: `underlay_filter_peer_as`  
**Default**: `False`  

Configure route-map on eBGP sessions towards underlay peers, where prefixes with the peer's ASN in the AS Path are filtered away.
This is very useful in very large scale networks not using EVPN overlays, where convergence will be quicker by not having to return
all updates received from Spine-1 to Spine-2 just for Spine-2 to throw them away because of AS Path loop detection.
Note that this setting cannot be used while there are EVPN services present in the default VRF.


---

### underlay_filter_redistribute_connected

**Type**: Boolean  
**Path**: `underlay_filter_redistribute_connected`  
**Default**: `True`  

Filter redistribution of connected into the underlay routing protocol.
Only applicable when overlay_routing_protocol != 'none' and underlay_routing_protocol == BGP.
Creates a route-map and prefix-list assigned to redistribute connected permitting only loopbacks and inband management subnets.


---

### underlay_ipv6

**Type**: Boolean  
**Path**: `underlay_ipv6`  
**Default**: `False`  

This feature allows IPv6 underlay routing protocol with RFC5549 addresses to be used along with IPv4 advertisements as VXLAN tunnel endpoints.
Requires "underlay_rfc5549: true" and "loopback_ipv6_pool" under the node type settings.


---

### underlay_ipv6_numbered

**Type**: Boolean  
**Path**: `underlay_ipv6_numbered`  
**Default**: `False`  

This feature allows pure IPv6 underlay routing protocol with numbered addresses.
Currently sets both underlay and overlay, including MLAG, to use IPv6 addresses.
Currently BGP peer-groups are named with IPv4 by default. This can be modified under `bgp_peer_groups`.
Requires:
  - "underlay_ipv6: true"
  - "loopback_ipv6_pool"
  - "underlay_routing_protocol: ebgp"
Some settings are not yet supported with IPv6 underlay:
  - underlay_multicast_pim_sm
  - underlay_multicast_rp_interfaces
  - underlay_rfc5549
  - wan_role
  - vtep_vvtep_ip
  - inband_ztp


---

### underlay_isis_authentication_cleartext_key

**Type**: String  
**Path**: `underlay_isis_authentication_cleartext_key`  

Cleartext password.
Encrypted to Type 7 by AVD.
To protect the password at rest it is strongly recommended to make use of a vault or similar.

---

### underlay_isis_authentication_key

**Type**: String  
**Path**: `underlay_isis_authentication_key`  

Type-7 encrypted password.
Takes precedence over `underlay_isis_authentication_cleartext_key`.
To protect the password at rest it is strongly recommended to make use of a vault or similar.

---

### underlay_isis_authentication_mode

**Type**: String  
**Path**: `underlay_isis_authentication_mode`  
**Valid Values**: `md5`, `text`  

Underlay ISIS authentication mode.

---

### underlay_isis_bfd

**Type**: Boolean  
**Path**: `underlay_isis_bfd`  
**Default**: `False`  

Enable BFD for ISIS on all underlay links.

---

### underlay_isis_instance_name

**Type**: String  
**Path**: `underlay_isis_instance_name`  

Default -> "EVPN_UNDERLAY" for l3ls, "CORE" for mpls.

---

### underlay_l2_ethernet_description

**Type**: String  
**Path**: `underlay_l2_ethernet_description`  
**Default**: `L2_{peer}_{peer_interface}`  

The description or description template to be used on L2 ethernet interfaces.
The interfaces using this are the member interfaces of port-channel uplinks.
This can be a template using the AVD string formatter syntax: https://avd.arista.com/stable/ansible_collections/arista/avd/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.
The available template fields are:
  - `peer`: The name of the peer.
  - `interface`: The local interface name.
  - `peer_interface`: The interface on the peer.

By default the description is templated from the hostname and interface of the peer.

---

### underlay_l2_port_channel_description

**Type**: String  
**Path**: `underlay_l2_port_channel_description`  
**Default**: `L2_{peer_node_group_or_peer}_{peer_interface}`  

The description or description template to be used on L2 port-channel interfaces.
The interfaces using this are port-channel uplinks.
This can be a template using the AVD string formatter syntax: https://avd.arista.com/stable/ansible_collections/arista/avd/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.
The available template fields are:
  - `peer`: The name of the peer.
  - `interface`: The local interface name.
  - `peer_interface`: The interface on the peer.
  - `port_channel_id`: The local port-channel ID.
  - `peer_port_channel_id`: The ID of the port-channel on the peer.
  - `peer_node_group`: The node group of the peer if the peer is an MLAG member or running EVPN A/A.
  - `peer_node_group_or_peer`: Helper alias of the peer_node_group or peer.
  - `peer_node_group_or_uppercase_peer`: Helper alias of the peer_node_group or peer hostname in uppercase.

By default the description is templated from the peer's node group (for MLAG or EVPN A/A) or hostname and port-channel interface of the peer.

---

### underlay_multicast_anycast_rp

**Type**: Dictionary  
**Path**: `underlay_multicast_anycast_rp`  

If multiple nodes are configured under 'underlay_multicast_rps.[].nodes' for the same RP address, they will be configured
with one of the following methods:
- Anycast RP using PIM (RFC4610).
- Anycast RP using MSDP (RFC4611).

NOTE: When using MSDP, all nodes across all MSDP enabled RPs will be added to a single MSDP mesh group named "ANYCAST-RP".


---

### underlay_multicast_pim_sm

**Type**: Boolean  
**Path**: `underlay_multicast_pim_sm`  
**Default**: `False`  

When enabled, configures multicast routing and by default configures PIM sparse-mode in the underlay on all:
  - P2P uplink interfaces if enabled on uplink peer
  - MLAG L3 peer interface if also enabled on MLAG peer
  - l3_edge and core interfaces

Note: This changes the default behavior for l3_edge / core_interfaces to automatically include the interfaces
in multicast, unless `include_in_underlay_protocol: false` or `multicast_pim_sm: false`.

---

### underlay_multicast_rps

**Type**: List, items: Dictionary  
**Path**: `underlay_multicast_rps`  

List of PIM Sparse-Mode Rendevouz Points configured for underlay multicast on all devices.
The device(s) listed under 'nodes', will be configured as the Rendevouz point router(s).
If multiple nodes are configured under 'nodes' for the same RP address, they will be configured
according to the 'underlay_multicast_anycast_rp.mode' setting.

Requires 'underlay_multicast_pim_sm: true'.


---

### underlay_multicast_static

**Type**: Boolean  
**Path**: `underlay_multicast_static`  
**Default**: `False`  

When enabled, configures multicast routing and by default configures static multicast in the underlay on all:
  - P2P uplink interfaces if enabled on uplink peer
  - MLAG L3 peer interface if also enabled on MLAG peer
  - l3_edge and core interfaces

---

### underlay_ospf_graceful_restart

**Type**: Boolean  
**Path**: `underlay_ospf_graceful_restart`  
**Default**: `True`  

Enable graceful restart for OSPF underlay.

---

### underlay_ospf_maximum_paths

**Type**: Integer  
**Path**: `underlay_ospf_maximum_paths`  
**Default**: `128`  

Maximum number of next-hops in an ECMP route.

---

### underlay_rfc5549

**Type**: Boolean  
**Path**: `underlay_rfc5549`  
**Default**: `False`  

Point to Point Underlay with RFC 5549(eBGP), i.e. IPv6 Unnumbered.
Requires "underlay_routing_protocol: ebgp".


---

### underlay_routing_protocol

**Type**: String  
**Path**: `underlay_routing_protocol`  
**Valid Values**: `ebgp`, `ospf`, `ospf-ldp`, `isis`, `isis-sr`, `isis-ldp`, `isis-sr-ldp`, `none`  

- The following underlay routing protocols are supported:
  - EBGP (default for l3ls-evpn)
  - OSPF.
  - OSPF-LDP*.
  - ISIS.
  - ISIS-SR*.
  - ISIS-LDP*.
  - ISIS-SR-LDP*.
  - No underlay routing protocol (none)
- The variables should be applied to all devices in the fabric.
*Only supported with core_interfaces data model.


---

### unit

**Type**: String  
**Path**: `<connected_endpoints_keys.key>.[].adapters.[].storm_control.all.unit`  
**Default**: `percent`  
**Valid Values**: `percent`, `pps`  

Optional variable and is hardware dependent.

---

### unit

**Type**: String  
**Path**: `<connected_endpoints_keys.key>.[].adapters.[].storm_control.broadcast.unit`  
**Default**: `percent`  
**Valid Values**: `percent`, `pps`  

Optional variable and is hardware dependent.

---

### unit

**Type**: String  
**Path**: `<connected_endpoints_keys.key>.[].adapters.[].storm_control.multicast.unit`  
**Default**: `percent`  
**Valid Values**: `percent`, `pps`  

Optional variable and is hardware dependent.

---

### unit

**Type**: String  
**Path**: `<connected_endpoints_keys.key>.[].adapters.[].storm_control.unknown_unicast.unit`  
**Default**: `percent`  
**Valid Values**: `percent`, `pps`  

Optional variable and is hardware dependent.

---

### unit

**Type**: String  
**Path**: `<custom_connected_endpoints_keys.key>.[].adapters.[].storm_control.all.unit`  
**Default**: `percent`  
**Valid Values**: `percent`, `pps`  

Optional variable and is hardware dependent.

---

### unit

**Type**: String  
**Path**: `<custom_connected_endpoints_keys.key>.[].adapters.[].storm_control.broadcast.unit`  
**Default**: `percent`  
**Valid Values**: `percent`, `pps`  

Optional variable and is hardware dependent.

---

### unit

**Type**: String  
**Path**: `<custom_connected_endpoints_keys.key>.[].adapters.[].storm_control.multicast.unit`  
**Default**: `percent`  
**Valid Values**: `percent`, `pps`  

Optional variable and is hardware dependent.

---

### unit

**Type**: String  
**Path**: `<custom_connected_endpoints_keys.key>.[].adapters.[].storm_control.unknown_unicast.unit`  
**Default**: `percent`  
**Valid Values**: `percent`, `pps`  

Optional variable and is hardware dependent.

---

### unit

**Type**: String  
**Path**: `connected_endpoints.[].adapters.[].storm_control.all.unit`  
**Default**: `percent`  
**Valid Values**: `percent`, `pps`  

Optional variable and is hardware dependent.

---

### unit

**Type**: String  
**Path**: `connected_endpoints.[].adapters.[].storm_control.broadcast.unit`  
**Default**: `percent`  
**Valid Values**: `percent`, `pps`  

Optional variable and is hardware dependent.

---

### unit

**Type**: String  
**Path**: `connected_endpoints.[].adapters.[].storm_control.multicast.unit`  
**Default**: `percent`  
**Valid Values**: `percent`, `pps`  

Optional variable and is hardware dependent.

---

### unit

**Type**: String  
**Path**: `connected_endpoints.[].adapters.[].storm_control.unknown_unicast.unit`  
**Default**: `percent`  
**Valid Values**: `percent`, `pps`  

Optional variable and is hardware dependent.

---

### unit

**Type**: String  
**Path**: `network_ports.[].storm_control.all.unit`  
**Default**: `percent`  
**Valid Values**: `percent`, `pps`  

Optional variable and is hardware dependent.

---

### unit

**Type**: String  
**Path**: `network_ports.[].storm_control.broadcast.unit`  
**Default**: `percent`  
**Valid Values**: `percent`, `pps`  

Optional variable and is hardware dependent.

---

### unit

**Type**: String  
**Path**: `network_ports.[].storm_control.multicast.unit`  
**Default**: `percent`  
**Valid Values**: `percent`, `pps`  

Optional variable and is hardware dependent.

---

### unit

**Type**: String  
**Path**: `network_ports.[].storm_control.unknown_unicast.unit`  
**Default**: `percent`  
**Valid Values**: `percent`, `pps`  

Optional variable and is hardware dependent.

---

### unit

**Type**: String  
**Path**: `port_profiles.[].storm_control.all.unit`  
**Default**: `percent`  
**Valid Values**: `percent`, `pps`  

Optional variable and is hardware dependent.

---

### unit

**Type**: String  
**Path**: `port_profiles.[].storm_control.broadcast.unit`  
**Default**: `percent`  
**Valid Values**: `percent`, `pps`  

Optional variable and is hardware dependent.

---

### unit

**Type**: String  
**Path**: `port_profiles.[].storm_control.multicast.unit`  
**Default**: `percent`  
**Valid Values**: `percent`, `pps`  

Optional variable and is hardware dependent.

---

### unit

**Type**: String  
**Path**: `port_profiles.[].storm_control.unknown_unicast.unit`  
**Default**: `percent`  
**Valid Values**: `percent`, `pps`  

Optional variable and is hardware dependent.

---

### uplink_interface_speed

**Type**: String  
**Path**: `<node_type_keys.key>.defaults.uplink_interface_speed`  
**Valid Values**: `100full`, `100g`, `100g-1`, `100g-2`, `100g-4`, `100half`, `10full`, `10g`, `10half`, `1g`, `200g`, `200g-2`, `200g-4`, `25g`, `400g`, `400g-4`, `400g-8`, `40g`, `50g`, `50g-1`, `50g-2`, `800g-8`, `sfp-1000baset auto 100full`, `1.6t-8`, `100mfull`, `100mhalf`, `10mfull`, `10mhalf`, `200g-1`, `400g-2`, `40g-4`, `800g-4`, `auto`, `auto 10000full`, `auto 1000full`, `auto 100full`, `auto 100g-1`, `auto 100g-2`, `auto 100g-4`, `auto 100gfull`, `auto 100half`, `auto 10full`, `auto 10gfull`, `auto 10half`, `auto 1gfull`, `auto 2.5gfull`, `auto 200g-2`, `auto 200g-4`, `auto 25gfull`, `auto 400g-4`, `auto 400g-8`, `auto 40gfull`, `auto 50g-1`, `auto 50g-2`, `auto 50gfull`, `auto 5gfull`, `auto 800g-8`, `auto 1.6t-8`, `auto 100mfull`, `auto 100mhalf`, `auto 10g`, `auto 10mfull`, `auto 10mhalf`, `auto 1g`, `auto 2.5g`, `auto 200g-1`, `auto 25g`, `auto 400g-2`, `auto 40g-4`, `auto 5g`, `auto 800g-4`, `forced 10000full`, `forced 1000full`, `forced 1000half`, `forced 100full`, `forced 100gfull`, `forced 100half`, `forced 10full`, `forced 10half`, `forced 25gfull`, `forced 40gfull`, `forced 50gfull`  

Set point-to-Point interface speed and will apply to uplink interfaces on both ends.
(Uplink switch interface speed can be overridden with `uplink_switch_interface_speed`).
Speed should be set in the format `<interface_speed>` or `forced <interface_speed>` or `auto <interface_speed>`.


---

### uplink_interface_speed

**Type**: String  
**Path**: `<node_type_keys.key>.node_groups.[].nodes.[].uplink_interface_speed`  
**Valid Values**: `100full`, `100g`, `100g-1`, `100g-2`, `100g-4`, `100half`, `10full`, `10g`, `10half`, `1g`, `200g`, `200g-2`, `200g-4`, `25g`, `400g`, `400g-4`, `400g-8`, `40g`, `50g`, `50g-1`, `50g-2`, `800g-8`, `sfp-1000baset auto 100full`, `1.6t-8`, `100mfull`, `100mhalf`, `10mfull`, `10mhalf`, `200g-1`, `400g-2`, `40g-4`, `800g-4`, `auto`, `auto 10000full`, `auto 1000full`, `auto 100full`, `auto 100g-1`, `auto 100g-2`, `auto 100g-4`, `auto 100gfull`, `auto 100half`, `auto 10full`, `auto 10gfull`, `auto 10half`, `auto 1gfull`, `auto 2.5gfull`, `auto 200g-2`, `auto 200g-4`, `auto 25gfull`, `auto 400g-4`, `auto 400g-8`, `auto 40gfull`, `auto 50g-1`, `auto 50g-2`, `auto 50gfull`, `auto 5gfull`, `auto 800g-8`, `auto 1.6t-8`, `auto 100mfull`, `auto 100mhalf`, `auto 10g`, `auto 10mfull`, `auto 10mhalf`, `auto 1g`, `auto 2.5g`, `auto 200g-1`, `auto 25g`, `auto 400g-2`, `auto 40g-4`, `auto 5g`, `auto 800g-4`, `forced 10000full`, `forced 1000full`, `forced 1000half`, `forced 100full`, `forced 100gfull`, `forced 100half`, `forced 10full`, `forced 10half`, `forced 25gfull`, `forced 40gfull`, `forced 50gfull`  

Set point-to-Point interface speed and will apply to uplink interfaces on both ends.
(Uplink switch interface speed can be overridden with `uplink_switch_interface_speed`).
Speed should be set in the format `<interface_speed>` or `forced <interface_speed>` or `auto <interface_speed>`.


---

### uplink_interface_speed

**Type**: String  
**Path**: `<node_type_keys.key>.node_groups.[].uplink_interface_speed`  
**Valid Values**: `100full`, `100g`, `100g-1`, `100g-2`, `100g-4`, `100half`, `10full`, `10g`, `10half`, `1g`, `200g`, `200g-2`, `200g-4`, `25g`, `400g`, `400g-4`, `400g-8`, `40g`, `50g`, `50g-1`, `50g-2`, `800g-8`, `sfp-1000baset auto 100full`, `1.6t-8`, `100mfull`, `100mhalf`, `10mfull`, `10mhalf`, `200g-1`, `400g-2`, `40g-4`, `800g-4`, `auto`, `auto 10000full`, `auto 1000full`, `auto 100full`, `auto 100g-1`, `auto 100g-2`, `auto 100g-4`, `auto 100gfull`, `auto 100half`, `auto 10full`, `auto 10gfull`, `auto 10half`, `auto 1gfull`, `auto 2.5gfull`, `auto 200g-2`, `auto 200g-4`, `auto 25gfull`, `auto 400g-4`, `auto 400g-8`, `auto 40gfull`, `auto 50g-1`, `auto 50g-2`, `auto 50gfull`, `auto 5gfull`, `auto 800g-8`, `auto 1.6t-8`, `auto 100mfull`, `auto 100mhalf`, `auto 10g`, `auto 10mfull`, `auto 10mhalf`, `auto 1g`, `auto 2.5g`, `auto 200g-1`, `auto 25g`, `auto 400g-2`, `auto 40g-4`, `auto 5g`, `auto 800g-4`, `forced 10000full`, `forced 1000full`, `forced 1000half`, `forced 100full`, `forced 100gfull`, `forced 100half`, `forced 10full`, `forced 10half`, `forced 25gfull`, `forced 40gfull`, `forced 50gfull`  

Set point-to-Point interface speed and will apply to uplink interfaces on both ends.
(Uplink switch interface speed can be overridden with `uplink_switch_interface_speed`).
Speed should be set in the format `<interface_speed>` or `forced <interface_speed>` or `auto <interface_speed>`.


---

### uplink_interface_speed

**Type**: String  
**Path**: `<node_type_keys.key>.nodes.[].uplink_interface_speed`  
**Valid Values**: `100full`, `100g`, `100g-1`, `100g-2`, `100g-4`, `100half`, `10full`, `10g`, `10half`, `1g`, `200g`, `200g-2`, `200g-4`, `25g`, `400g`, `400g-4`, `400g-8`, `40g`, `50g`, `50g-1`, `50g-2`, `800g-8`, `sfp-1000baset auto 100full`, `1.6t-8`, `100mfull`, `100mhalf`, `10mfull`, `10mhalf`, `200g-1`, `400g-2`, `40g-4`, `800g-4`, `auto`, `auto 10000full`, `auto 1000full`, `auto 100full`, `auto 100g-1`, `auto 100g-2`, `auto 100g-4`, `auto 100gfull`, `auto 100half`, `auto 10full`, `auto 10gfull`, `auto 10half`, `auto 1gfull`, `auto 2.5gfull`, `auto 200g-2`, `auto 200g-4`, `auto 25gfull`, `auto 400g-4`, `auto 400g-8`, `auto 40gfull`, `auto 50g-1`, `auto 50g-2`, `auto 50gfull`, `auto 5gfull`, `auto 800g-8`, `auto 1.6t-8`, `auto 100mfull`, `auto 100mhalf`, `auto 10g`, `auto 10mfull`, `auto 10mhalf`, `auto 1g`, `auto 2.5g`, `auto 200g-1`, `auto 25g`, `auto 400g-2`, `auto 40g-4`, `auto 5g`, `auto 800g-4`, `forced 10000full`, `forced 1000full`, `forced 1000half`, `forced 100full`, `forced 100gfull`, `forced 100half`, `forced 10full`, `forced 10half`, `forced 25gfull`, `forced 40gfull`, `forced 50gfull`  

Set point-to-Point interface speed and will apply to uplink interfaces on both ends.
(Uplink switch interface speed can be overridden with `uplink_switch_interface_speed`).
Speed should be set in the format `<interface_speed>` or `forced <interface_speed>` or `auto <interface_speed>`.


---

### uplink_interface_speed

**Type**: String  
**Path**: `default_interfaces.[].uplink_interface_speed`  
**Valid Values**: `100full`, `100g`, `100g-1`, `100g-2`, `100g-4`, `100half`, `10full`, `10g`, `10half`, `1g`, `200g`, `200g-2`, `200g-4`, `25g`, `400g`, `400g-4`, `400g-8`, `40g`, `50g`, `50g-1`, `50g-2`, `800g-8`, `sfp-1000baset auto 100full`, `1.6t-8`, `100mfull`, `100mhalf`, `10mfull`, `10mhalf`, `200g-1`, `400g-2`, `40g-4`, `800g-4`, `auto`, `auto 10000full`, `auto 1000full`, `auto 100full`, `auto 100g-1`, `auto 100g-2`, `auto 100g-4`, `auto 100gfull`, `auto 100half`, `auto 10full`, `auto 10gfull`, `auto 10half`, `auto 1gfull`, `auto 2.5gfull`, `auto 200g-2`, `auto 200g-4`, `auto 25gfull`, `auto 400g-4`, `auto 400g-8`, `auto 40gfull`, `auto 50g-1`, `auto 50g-2`, `auto 50gfull`, `auto 5gfull`, `auto 800g-8`, `auto 1.6t-8`, `auto 100mfull`, `auto 100mhalf`, `auto 10g`, `auto 10mfull`, `auto 10mhalf`, `auto 1g`, `auto 2.5g`, `auto 200g-1`, `auto 25g`, `auto 400g-2`, `auto 40g-4`, `auto 5g`, `auto 800g-4`, `forced 10000full`, `forced 1000full`, `forced 1000half`, `forced 100full`, `forced 100gfull`, `forced 100half`, `forced 10full`, `forced 10half`, `forced 25gfull`, `forced 40gfull`, `forced 50gfull`  

Set point-to-Point uplink interface speed.

---

### uplink_interface_speed

**Type**: String  
**Path**: `device_profiles.[].uplink_interface_speed`  
**Valid Values**: `100full`, `100g`, `100g-1`, `100g-2`, `100g-4`, `100half`, `10full`, `10g`, `10half`, `1g`, `200g`, `200g-2`, `200g-4`, `25g`, `400g`, `400g-4`, `400g-8`, `40g`, `50g`, `50g-1`, `50g-2`, `800g-8`, `sfp-1000baset auto 100full`, `1.6t-8`, `100mfull`, `100mhalf`, `10mfull`, `10mhalf`, `200g-1`, `400g-2`, `40g-4`, `800g-4`, `auto`, `auto 10000full`, `auto 1000full`, `auto 100full`, `auto 100g-1`, `auto 100g-2`, `auto 100g-4`, `auto 100gfull`, `auto 100half`, `auto 10full`, `auto 10gfull`, `auto 10half`, `auto 1gfull`, `auto 2.5gfull`, `auto 200g-2`, `auto 200g-4`, `auto 25gfull`, `auto 400g-4`, `auto 400g-8`, `auto 40gfull`, `auto 50g-1`, `auto 50g-2`, `auto 50gfull`, `auto 5gfull`, `auto 800g-8`, `auto 1.6t-8`, `auto 100mfull`, `auto 100mhalf`, `auto 10g`, `auto 10mfull`, `auto 10mhalf`, `auto 1g`, `auto 2.5g`, `auto 200g-1`, `auto 25g`, `auto 400g-2`, `auto 40g-4`, `auto 5g`, `auto 800g-4`, `forced 10000full`, `forced 1000full`, `forced 1000half`, `forced 100full`, `forced 100gfull`, `forced 100half`, `forced 10full`, `forced 10half`, `forced 25gfull`, `forced 40gfull`, `forced 50gfull`  

Set point-to-Point interface speed and will apply to uplink interfaces on both ends.
(Uplink switch interface speed can be overridden with `uplink_switch_interface_speed`).
Speed should be set in the format `<interface_speed>` or `forced <interface_speed>` or `auto <interface_speed>`.


---

### uplink_interface_speed

**Type**: String  
**Path**: `devices.[].uplink_interface_speed`  
**Valid Values**: `100full`, `100g`, `100g-1`, `100g-2`, `100g-4`, `100half`, `10full`, `10g`, `10half`, `1g`, `200g`, `200g-2`, `200g-4`, `25g`, `400g`, `400g-4`, `400g-8`, `40g`, `50g`, `50g-1`, `50g-2`, `800g-8`, `sfp-1000baset auto 100full`, `1.6t-8`, `100mfull`, `100mhalf`, `10mfull`, `10mhalf`, `200g-1`, `400g-2`, `40g-4`, `800g-4`, `auto`, `auto 10000full`, `auto 1000full`, `auto 100full`, `auto 100g-1`, `auto 100g-2`, `auto 100g-4`, `auto 100gfull`, `auto 100half`, `auto 10full`, `auto 10gfull`, `auto 10half`, `auto 1gfull`, `auto 2.5gfull`, `auto 200g-2`, `auto 200g-4`, `auto 25gfull`, `auto 400g-4`, `auto 400g-8`, `auto 40gfull`, `auto 50g-1`, `auto 50g-2`, `auto 50gfull`, `auto 5gfull`, `auto 800g-8`, `auto 1.6t-8`, `auto 100mfull`, `auto 100mhalf`, `auto 10g`, `auto 10mfull`, `auto 10mhalf`, `auto 1g`, `auto 2.5g`, `auto 200g-1`, `auto 25g`, `auto 400g-2`, `auto 40g-4`, `auto 5g`, `auto 800g-4`, `forced 10000full`, `forced 1000full`, `forced 1000half`, `forced 100full`, `forced 100gfull`, `forced 100half`, `forced 10full`, `forced 10half`, `forced 25gfull`, `forced 40gfull`, `forced 50gfull`  

Set point-to-Point interface speed and will apply to uplink interfaces on both ends.
(Uplink switch interface speed can be overridden with `uplink_switch_interface_speed`).
Speed should be set in the format `<interface_speed>` or `forced <interface_speed>` or `auto <interface_speed>`.


---

### uplink_ptp

**Type**: Dictionary  
**Path**: `uplink_ptp`  

Enable PTP on all infrastructure links.

---

### uplink_switch_interface_speed

**Type**: String  
**Path**: `<node_type_keys.key>.defaults.uplink_switch_interface_speed`  
**Valid Values**: `100full`, `100g`, `100g-1`, `100g-2`, `100g-4`, `100half`, `10full`, `10g`, `10half`, `1g`, `200g`, `200g-2`, `200g-4`, `25g`, `400g`, `400g-4`, `400g-8`, `40g`, `50g`, `50g-1`, `50g-2`, `800g-8`, `sfp-1000baset auto 100full`, `1.6t-8`, `100mfull`, `100mhalf`, `10mfull`, `10mhalf`, `200g-1`, `400g-2`, `40g-4`, `800g-4`, `auto`, `auto 10000full`, `auto 1000full`, `auto 100full`, `auto 100g-1`, `auto 100g-2`, `auto 100g-4`, `auto 100gfull`, `auto 100half`, `auto 10full`, `auto 10gfull`, `auto 10half`, `auto 1gfull`, `auto 2.5gfull`, `auto 200g-2`, `auto 200g-4`, `auto 25gfull`, `auto 400g-4`, `auto 400g-8`, `auto 40gfull`, `auto 50g-1`, `auto 50g-2`, `auto 50gfull`, `auto 5gfull`, `auto 800g-8`, `auto 1.6t-8`, `auto 100mfull`, `auto 100mhalf`, `auto 10g`, `auto 10mfull`, `auto 10mhalf`, `auto 1g`, `auto 2.5g`, `auto 200g-1`, `auto 25g`, `auto 400g-2`, `auto 40g-4`, `auto 5g`, `auto 800g-4`, `forced 10000full`, `forced 1000full`, `forced 1000half`, `forced 100full`, `forced 100gfull`, `forced 100half`, `forced 10full`, `forced 10half`, `forced 25gfull`, `forced 40gfull`, `forced 50gfull`  

Set point-to-Point interface speed for the uplink switch interface only.


---

### uplink_switch_interface_speed

**Type**: String  
**Path**: `<node_type_keys.key>.node_groups.[].nodes.[].uplink_switch_interface_speed`  
**Valid Values**: `100full`, `100g`, `100g-1`, `100g-2`, `100g-4`, `100half`, `10full`, `10g`, `10half`, `1g`, `200g`, `200g-2`, `200g-4`, `25g`, `400g`, `400g-4`, `400g-8`, `40g`, `50g`, `50g-1`, `50g-2`, `800g-8`, `sfp-1000baset auto 100full`, `1.6t-8`, `100mfull`, `100mhalf`, `10mfull`, `10mhalf`, `200g-1`, `400g-2`, `40g-4`, `800g-4`, `auto`, `auto 10000full`, `auto 1000full`, `auto 100full`, `auto 100g-1`, `auto 100g-2`, `auto 100g-4`, `auto 100gfull`, `auto 100half`, `auto 10full`, `auto 10gfull`, `auto 10half`, `auto 1gfull`, `auto 2.5gfull`, `auto 200g-2`, `auto 200g-4`, `auto 25gfull`, `auto 400g-4`, `auto 400g-8`, `auto 40gfull`, `auto 50g-1`, `auto 50g-2`, `auto 50gfull`, `auto 5gfull`, `auto 800g-8`, `auto 1.6t-8`, `auto 100mfull`, `auto 100mhalf`, `auto 10g`, `auto 10mfull`, `auto 10mhalf`, `auto 1g`, `auto 2.5g`, `auto 200g-1`, `auto 25g`, `auto 400g-2`, `auto 40g-4`, `auto 5g`, `auto 800g-4`, `forced 10000full`, `forced 1000full`, `forced 1000half`, `forced 100full`, `forced 100gfull`, `forced 100half`, `forced 10full`, `forced 10half`, `forced 25gfull`, `forced 40gfull`, `forced 50gfull`  

Set point-to-Point interface speed for the uplink switch interface only.


---

### uplink_switch_interface_speed

**Type**: String  
**Path**: `<node_type_keys.key>.node_groups.[].uplink_switch_interface_speed`  
**Valid Values**: `100full`, `100g`, `100g-1`, `100g-2`, `100g-4`, `100half`, `10full`, `10g`, `10half`, `1g`, `200g`, `200g-2`, `200g-4`, `25g`, `400g`, `400g-4`, `400g-8`, `40g`, `50g`, `50g-1`, `50g-2`, `800g-8`, `sfp-1000baset auto 100full`, `1.6t-8`, `100mfull`, `100mhalf`, `10mfull`, `10mhalf`, `200g-1`, `400g-2`, `40g-4`, `800g-4`, `auto`, `auto 10000full`, `auto 1000full`, `auto 100full`, `auto 100g-1`, `auto 100g-2`, `auto 100g-4`, `auto 100gfull`, `auto 100half`, `auto 10full`, `auto 10gfull`, `auto 10half`, `auto 1gfull`, `auto 2.5gfull`, `auto 200g-2`, `auto 200g-4`, `auto 25gfull`, `auto 400g-4`, `auto 400g-8`, `auto 40gfull`, `auto 50g-1`, `auto 50g-2`, `auto 50gfull`, `auto 5gfull`, `auto 800g-8`, `auto 1.6t-8`, `auto 100mfull`, `auto 100mhalf`, `auto 10g`, `auto 10mfull`, `auto 10mhalf`, `auto 1g`, `auto 2.5g`, `auto 200g-1`, `auto 25g`, `auto 400g-2`, `auto 40g-4`, `auto 5g`, `auto 800g-4`, `forced 10000full`, `forced 1000full`, `forced 1000half`, `forced 100full`, `forced 100gfull`, `forced 100half`, `forced 10full`, `forced 10half`, `forced 25gfull`, `forced 40gfull`, `forced 50gfull`  

Set point-to-Point interface speed for the uplink switch interface only.


---

### uplink_switch_interface_speed

**Type**: String  
**Path**: `<node_type_keys.key>.nodes.[].uplink_switch_interface_speed`  
**Valid Values**: `100full`, `100g`, `100g-1`, `100g-2`, `100g-4`, `100half`, `10full`, `10g`, `10half`, `1g`, `200g`, `200g-2`, `200g-4`, `25g`, `400g`, `400g-4`, `400g-8`, `40g`, `50g`, `50g-1`, `50g-2`, `800g-8`, `sfp-1000baset auto 100full`, `1.6t-8`, `100mfull`, `100mhalf`, `10mfull`, `10mhalf`, `200g-1`, `400g-2`, `40g-4`, `800g-4`, `auto`, `auto 10000full`, `auto 1000full`, `auto 100full`, `auto 100g-1`, `auto 100g-2`, `auto 100g-4`, `auto 100gfull`, `auto 100half`, `auto 10full`, `auto 10gfull`, `auto 10half`, `auto 1gfull`, `auto 2.5gfull`, `auto 200g-2`, `auto 200g-4`, `auto 25gfull`, `auto 400g-4`, `auto 400g-8`, `auto 40gfull`, `auto 50g-1`, `auto 50g-2`, `auto 50gfull`, `auto 5gfull`, `auto 800g-8`, `auto 1.6t-8`, `auto 100mfull`, `auto 100mhalf`, `auto 10g`, `auto 10mfull`, `auto 10mhalf`, `auto 1g`, `auto 2.5g`, `auto 200g-1`, `auto 25g`, `auto 400g-2`, `auto 40g-4`, `auto 5g`, `auto 800g-4`, `forced 10000full`, `forced 1000full`, `forced 1000half`, `forced 100full`, `forced 100gfull`, `forced 100half`, `forced 10full`, `forced 10half`, `forced 25gfull`, `forced 40gfull`, `forced 50gfull`  

Set point-to-Point interface speed for the uplink switch interface only.


---

### uplink_switch_interface_speed

**Type**: String  
**Path**: `device_profiles.[].uplink_switch_interface_speed`  
**Valid Values**: `100full`, `100g`, `100g-1`, `100g-2`, `100g-4`, `100half`, `10full`, `10g`, `10half`, `1g`, `200g`, `200g-2`, `200g-4`, `25g`, `400g`, `400g-4`, `400g-8`, `40g`, `50g`, `50g-1`, `50g-2`, `800g-8`, `sfp-1000baset auto 100full`, `1.6t-8`, `100mfull`, `100mhalf`, `10mfull`, `10mhalf`, `200g-1`, `400g-2`, `40g-4`, `800g-4`, `auto`, `auto 10000full`, `auto 1000full`, `auto 100full`, `auto 100g-1`, `auto 100g-2`, `auto 100g-4`, `auto 100gfull`, `auto 100half`, `auto 10full`, `auto 10gfull`, `auto 10half`, `auto 1gfull`, `auto 2.5gfull`, `auto 200g-2`, `auto 200g-4`, `auto 25gfull`, `auto 400g-4`, `auto 400g-8`, `auto 40gfull`, `auto 50g-1`, `auto 50g-2`, `auto 50gfull`, `auto 5gfull`, `auto 800g-8`, `auto 1.6t-8`, `auto 100mfull`, `auto 100mhalf`, `auto 10g`, `auto 10mfull`, `auto 10mhalf`, `auto 1g`, `auto 2.5g`, `auto 200g-1`, `auto 25g`, `auto 400g-2`, `auto 40g-4`, `auto 5g`, `auto 800g-4`, `forced 10000full`, `forced 1000full`, `forced 1000half`, `forced 100full`, `forced 100gfull`, `forced 100half`, `forced 10full`, `forced 10half`, `forced 25gfull`, `forced 40gfull`, `forced 50gfull`  

Set point-to-Point interface speed for the uplink switch interface only.


---

### uplink_switch_interface_speed

**Type**: String  
**Path**: `devices.[].uplink_switch_interface_speed`  
**Valid Values**: `100full`, `100g`, `100g-1`, `100g-2`, `100g-4`, `100half`, `10full`, `10g`, `10half`, `1g`, `200g`, `200g-2`, `200g-4`, `25g`, `400g`, `400g-4`, `400g-8`, `40g`, `50g`, `50g-1`, `50g-2`, `800g-8`, `sfp-1000baset auto 100full`, `1.6t-8`, `100mfull`, `100mhalf`, `10mfull`, `10mhalf`, `200g-1`, `400g-2`, `40g-4`, `800g-4`, `auto`, `auto 10000full`, `auto 1000full`, `auto 100full`, `auto 100g-1`, `auto 100g-2`, `auto 100g-4`, `auto 100gfull`, `auto 100half`, `auto 10full`, `auto 10gfull`, `auto 10half`, `auto 1gfull`, `auto 2.5gfull`, `auto 200g-2`, `auto 200g-4`, `auto 25gfull`, `auto 400g-4`, `auto 400g-8`, `auto 40gfull`, `auto 50g-1`, `auto 50g-2`, `auto 50gfull`, `auto 5gfull`, `auto 800g-8`, `auto 1.6t-8`, `auto 100mfull`, `auto 100mhalf`, `auto 10g`, `auto 10mfull`, `auto 10mhalf`, `auto 1g`, `auto 2.5g`, `auto 200g-1`, `auto 25g`, `auto 400g-2`, `auto 40g-4`, `auto 5g`, `auto 800g-4`, `forced 10000full`, `forced 1000full`, `forced 1000half`, `forced 100full`, `forced 100gfull`, `forced 100half`, `forced 10full`, `forced 10half`, `forced 25gfull`, `forced 40gfull`, `forced 50gfull`  

Set point-to-Point interface speed for the uplink switch interface only.


---

### uplink_type

**Type**: String  
**Path**: `<node_type_keys.key>.defaults.uplink_type`  
**Valid Values**: `p2p`, `port-channel`, `p2p-vrfs`, `lan`  

Override the default `uplink_type` set at the `node_type_key` level.
`uplink_type` must be "p2p" if `vtep` or `underlay_router` is true for the `node_type_key` definition.

---

### uplink_type

**Type**: String  
**Path**: `<node_type_keys.key>.node_groups.[].nodes.[].uplink_type`  
**Valid Values**: `p2p`, `port-channel`, `p2p-vrfs`, `lan`  

Override the default `uplink_type` set at the `node_type_key` level.
`uplink_type` must be "p2p" if `vtep` or `underlay_router` is true for the `node_type_key` definition.

---

### uplink_type

**Type**: String  
**Path**: `<node_type_keys.key>.node_groups.[].uplink_type`  
**Valid Values**: `p2p`, `port-channel`, `p2p-vrfs`, `lan`  

Override the default `uplink_type` set at the `node_type_key` level.
`uplink_type` must be "p2p" if `vtep` or `underlay_router` is true for the `node_type_key` definition.

---

### uplink_type

**Type**: String  
**Path**: `<node_type_keys.key>.nodes.[].uplink_type`  
**Valid Values**: `p2p`, `port-channel`, `p2p-vrfs`, `lan`  

Override the default `uplink_type` set at the `node_type_key` level.
`uplink_type` must be "p2p" if `vtep` or `underlay_router` is true for the `node_type_key` definition.

---

### uplink_type

**Type**: String  
**Path**: `device_profiles.[].uplink_type`  
**Valid Values**: `p2p`, `port-channel`, `p2p-vrfs`, `lan`  

Override the default `uplink_type` set at the `node_type_key` level.
`uplink_type` must be "p2p" if `vtep` or `underlay_router` is true for the `node_type_key` definition.

---

### uplink_type

**Type**: String  
**Path**: `devices.[].uplink_type`  
**Valid Values**: `p2p`, `port-channel`, `p2p-vrfs`, `lan`  

Override the default `uplink_type` set at the `node_type_key` level.
`uplink_type` must be "p2p" if `vtep` or `underlay_router` is true for the `node_type_key` definition.

---

### uplink_type

**Type**: String  
**Path**: `custom_node_type_keys.[].uplink_type`  
**Default**: `p2p`  
**Valid Values**: `p2p`, `port-channel`, `p2p-vrfs`, `lan`  

`uplink_type` must be `p2p`, `p2p-vrfs` or `lan` if `vtep` or `underlay_router` is true.

For `p2p-vrfs`, the uplinks are configured as L3 interfaces with a subinterface for each VRF
in `network_services` present on both the uplink and the downlink switch.
The subinterface ID is the `vrf_id`.
'underlay_router' and 'network_services.l3' must be set to true.
VRF `default` is always configured on the physical interface using the underlay routing protocol.
All subinterfaces use the same IP address as the physical interface.
Multicast is not supported.
Only BGP is supported for subinterfaces.

For `lan`, a single uplink interface is supported and will be configured as an L3 Interface with
subinterfaces for each SVI defined under the VRFs in `network_services` as long as the uplink switch also
has the VLAN permitted by tag/tenant filtering.

---

### uplink_type

**Type**: String  
**Path**: `node_type_keys.[].uplink_type`  
**Default**: `p2p`  
**Valid Values**: `p2p`, `port-channel`, `p2p-vrfs`, `lan`  

`uplink_type` must be `p2p`, `p2p-vrfs` or `lan` if `vtep` or `underlay_router` is true.

For `p2p-vrfs`, the uplinks are configured as L3 interfaces with a subinterface for each VRF
in `network_services` present on both the uplink and the downlink switch.
The subinterface ID is the `vrf_id`.
'underlay_router' and 'network_services.l3' must be set to true.
VRF `default` is always configured on the physical interface using the underlay routing protocol.
All subinterfaces use the same IP address as the physical interface.
Multicast is not supported.
Only BGP is supported for subinterfaces.

For `lan`, a single uplink interface is supported and will be configured as an L3 Interface with
subinterfaces for each SVI defined under the VRFs in `network_services` as long as the uplink switch also
has the VLAN permitted by tag/tenant filtering.

---

### use_cv_topology

**Type**: Boolean  
**Path**: `use_cv_topology`  

Generate AVD configurations directly from a given CloudVision topology.
See `cv_topology` for details.
Requires both `cv_topology` and `cv_topology_levels` to be set.

---

### use_router_general_for_router_id

**Type**: Boolean  
**Path**: `use_router_general_for_router_id`  
**Default**: `False`  

Use `router general` to set router ID for all routing protocols and VRFs.

---

## V

### validation_profiles

**Type**: List, items: Dictionary  
**Path**: `validation_profiles`  

List of validation profiles defining hardware, logging, and fabric-related validation rules.
Validation profiles can be referenced from node definitions (for example under `l3leaf.nodes[].validation_profile`) and support single-level inheritance using `parent_profile`.

---

### version

**Type**: Integer  
**Path**: `<network_services_keys.name>.[].igmp_snooping_querier.version`  
**Valid Values**: `1`, `2`, `3`  

IGMP Version (By default EOS uses IGMP version 2 for IGMP querier).

---

### version

**Type**: Integer  
**Path**: `<network_services_keys.name>.[].vrfs.[].svis.[].nodes.[].igmp_snooping_querier.version`  
**Valid Values**: `1`, `2`, `3`  

IGMP Version (By default EOS uses IGMP version 2 for IGMP querier).

---

### version

**Type**: Integer  
**Path**: `<network_services_keys.name>.[].vrfs.[].svis.[].igmp_snooping_querier.version`  
**Valid Values**: `1`, `2`, `3`  

IGMP Version (By default EOS uses IGMP version 2 for IGMP querier).

---

### version

**Type**: Integer  
**Path**: `<network_services_keys.name>.[].l2vlans.[].igmp_snooping_querier.version`  
**Valid Values**: `1`, `2`, `3`  

IGMP Version (By default EOS uses IGMP version 2 for IGMP querier).

---

### version

**Type**: Integer  
**Path**: `l2vlan_profiles.[].igmp_snooping_querier.version`  
**Valid Values**: `1`, `2`, `3`  

IGMP Version (By default EOS uses IGMP version 2 for IGMP querier).

---

### version

**Type**: String  
**Path**: `snmp_settings.users.[].version`  
**Valid Values**: `v1`, `v2c`, `v3`  
---

### version

**Type**: String  
**Path**: `snmp_settings.hosts.[].version`  
**Valid Values**: `1`, `2c`, `3`  
---

### version

**Type**: String  
**Path**: `snmp_settings.groups.[].version`  
**Valid Values**: `v1`, `v2c`, `v3`  
---

### version

**Type**: Integer  
**Path**: `svi_profiles.[].nodes.[].igmp_snooping_querier.version`  
**Valid Values**: `1`, `2`, `3`  

IGMP Version (By default EOS uses IGMP version 2 for IGMP querier).

---

### version

**Type**: Integer  
**Path**: `svi_profiles.[].igmp_snooping_querier.version`  
**Valid Values**: `1`, `2`, `3`  

IGMP Version (By default EOS uses IGMP version 2 for IGMP querier).

---

### vlan_assigned_number_subfield

**Type**: String  
**Path**: `overlay_rd_type.vlan_assigned_number_subfield`  
**Default**: `mac_vrf_id`  
**Valid Values**: `mac_vrf_id`, `mac_vrf_vni`, `vlan_id`  

The method for deriving RD Assigned Number subfield for VLAN services (second part of RD):
- 'mac_vrf_id' means `(mac_vrf_id_base or mac_vrf_vni_base) + vlan_id`.
- 'mac_vrf_vni' means `(mac_vrf_vni_base or mac_vrf_id_base) + vlan_id`.
- 'vlan_id' will only use the 'vlan_id' and ignores all base values.

These methods can be overridden per VLAN if either 'rd_override', 'rt_override' or 'vni_override' is set (preferred in this order).


---

### vlan_assigned_number_subfield

**Type**: String  
**Path**: `overlay_rt_type.vlan_assigned_number_subfield`  
**Default**: `mac_vrf_id`  
**Valid Values**: `mac_vrf_id`, `mac_vrf_vni`, `vlan_id`  

The method for deriving RT Assigned Number subfield for VLAN services (second part of RT):
- 'mac_vrf_id' means `(mac_vrf_id_base or mac_vrf_vni_base) + vlan_id`.
- 'mac_vrf_vni' means `(mac_vrf_vni_base or mac_vrf_id_base) + vlan_id`.
- 'vlan_id' will only use the 'vlan_id' and ignores all base values.

These methods can be overridden per VLAN if either 'rt_override' or 'vni_override' is set (preferred in this order).


---

### vtep_loopback_description

**Type**: String  
**Path**: `vtep_loopback_description`  
**Default**: `VXLAN_TUNNEL_SOURCE`  

Customize the description on the VTEP interface, typically Loopback1.

---

### vtep_vvtep_ip

**Type**: String  
**Path**: `vtep_vvtep_ip`  

IP Address used as Virtual VTEP. Will be configured as secondary IP on Loopback1.
This is only needed for centralized routing designs.


---

## W

### wan_carriers

**Type**: List, items: Dictionary  
**Path**: `wan_carriers`  

List of carriers used for the WAN configuration and their mapping to path-groups.

---

### wan_encapsulation

**Type**: String  
**Path**: `wan_encapsulation`  
**Default**: `path-selection`  
**Valid Values**: `path-selection`, `vxlan`  

Select the encapsulation to use for EVPN peerings for WAN BGP peers.

---

### wan_ipsec_profiles

**Type**: Dictionary  
**Path**: `wan_ipsec_profiles`  

Define IPsec profiles parameters for WAN configuration.

---

### wan_mode

**Type**: String  
**Path**: `wan_mode`  
**Default**: `cv-pathfinder`  
**Valid Values**: `cv-pathfinder`, `legacy-autovpn`  

Select if the WAN should be run using CV Pathfinder or AutoVPN only.

---

### wan_path_groups

**Type**: List, items: Dictionary  
**Path**: `wan_path_groups`  

List of path-groups used for the WAN configuration.

---

### wan_role

**Type**: String  
**Path**: `<node_type_keys.key>.defaults.wan_role`  
**Valid Values**: `client`, `server`  

Override the default WAN role.

This is used both for AutoVPN and Pathfinder designs.
That means if `wan_mode` root key is set to `legacy-autovpn` or `cv-pathfinder`.
`server` indicates that the router is a route-reflector.

---

### wan_role

**Type**: String  
**Path**: `<node_type_keys.key>.node_groups.[].nodes.[].wan_role`  
**Valid Values**: `client`, `server`  

Override the default WAN role.

This is used both for AutoVPN and Pathfinder designs.
That means if `wan_mode` root key is set to `legacy-autovpn` or `cv-pathfinder`.
`server` indicates that the router is a route-reflector.

---

### wan_role

**Type**: String  
**Path**: `<node_type_keys.key>.node_groups.[].wan_role`  
**Valid Values**: `client`, `server`  

Override the default WAN role.

This is used both for AutoVPN and Pathfinder designs.
That means if `wan_mode` root key is set to `legacy-autovpn` or `cv-pathfinder`.
`server` indicates that the router is a route-reflector.

---

### wan_role

**Type**: String  
**Path**: `<node_type_keys.key>.nodes.[].wan_role`  
**Valid Values**: `client`, `server`  

Override the default WAN role.

This is used both for AutoVPN and Pathfinder designs.
That means if `wan_mode` root key is set to `legacy-autovpn` or `cv-pathfinder`.
`server` indicates that the router is a route-reflector.

---

### wan_role

**Type**: String  
**Path**: `device_profiles.[].wan_role`  
**Valid Values**: `client`, `server`  

Override the default WAN role.

This is used both for AutoVPN and Pathfinder designs.
That means if `wan_mode` root key is set to `legacy-autovpn` or `cv-pathfinder`.
`server` indicates that the router is a route-reflector.

---

### wan_role

**Type**: String  
**Path**: `devices.[].wan_role`  
**Valid Values**: `client`, `server`  

Override the default WAN role.

This is used both for AutoVPN and Pathfinder designs.
That means if `wan_mode` root key is set to `legacy-autovpn` or `cv-pathfinder`.
`server` indicates that the router is a route-reflector.

---

### wan_route_servers

**Type**: List, items: Dictionary  
**Path**: `wan_route_servers`  

List of the AutoVPN RRs when using `wan_mode: legacy-autovpn`, or the Pathfinders
when using `wan_mode: cv-pathfinder`, to which the device should connect to.
This is also used to establish iBGP sessions between WAN route servers.

When the route server is part of the same inventory as the WAN routers,
only the name is required.

---

### wan_stun_dtls_disable

**Type**: Boolean  
**Path**: `wan_stun_dtls_disable`  
**Default**: `False`  

WAN STUN connections are authenticated and secured with DTLS by default.
For CV Pathfinder deployments CloudVision will automatically deploy certificates on the devices.
In case of AutoVPN the certificates must be deployed manually to all devices.

For LAB environments this can be disabled, if there are no certificates available.
This should NOT be disabled for a WAN network connected to the internet, since it will leave the STUN service exposed with no authentication.

---

### wan_stun_dtls_profile_name

**Type**: String  
**Path**: `wan_stun_dtls_profile_name`  
**Default**: `STUN-DTLS`  

Name of the SSL profile used for DTLS on WAN STUN connections.
When using automatic ceritficate deployment via CloudVision this name must be the same on all WAN routers.

---

### wan_use_agent_env_var_for_kernel_software_forwarding_ecmp

**Type**: Boolean  
**Path**: `wan_use_agent_env_var_for_kernel_software_forwarding_ecmp`  
**Default**: `False`  

For EOS kernel forwarding, ECMP programming can be enabled in two different ways depending on the EOS version.

- `true`: For older EOS versions use an agent environment variable. Changing this requires a restart of the KernelFib agent.
- `false`: For newer EOS versions (starting 4.33.2) use the proper CLI.

---

### wan_virtual_topologies

**Type**: Dictionary  
**Path**: `wan_virtual_topologies`  

Configure Virtual Topologies for CV Pathfinder and AutoVPN.
Auto create a control plane profile/policy/application and enforce it being first in the default VRF.

---

## Z

### zscaler_endpoints

**Type**: Dictionary  
**Path**: `zscaler_endpoints`  

PREVIEW: These keys are in preview mode.

Special data model used for testing the WAN internet-exit integration with Zscaler.
The model is supposed to be autofilled per-device by Arista AVD.
Manually setting this model will take precedence and prevent Arista AVD from trying to contact CloudVision.
This can be useful for offline testing or if CloudVision is not available or not configured for Zscaler integration.

---
