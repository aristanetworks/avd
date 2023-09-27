<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>&lt;node_type_keys.key&gt;</samp>](## "&lt;node_type_keys.key&gt;") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;defaults</samp>](## "&lt;node_type_keys.key&gt;.defaults") | Dictionary |  |  |  | Define variables for all nodes of this type. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;link_tracking</samp>](## "&lt;node_type_keys.key&gt;.defaults.link_tracking") | Dictionary |  |  |  | This configures the Link Tracking Group on a switch as well as adds the p2p-uplinks of the switch as the upstream interfaces.<br>Useful in EVPN multhoming designs.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.defaults.link_tracking.enabled") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;groups</samp>](## "&lt;node_type_keys.key&gt;.defaults.link_tracking.groups") | List, items: Dictionary |  | `[{'name': 'LT_GROUP1'}]` |  | Link Tracking Groups.<br>By default a single group named "LT_GROUP1" is defined with default values.<br>Any groups defined under "groups" will replace the default.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "&lt;node_type_keys.key&gt;.defaults.link_tracking.groups.[].name") | String |  |  |  | Tracking group name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery_delay</samp>](## "&lt;node_type_keys.key&gt;.defaults.link_tracking.groups.[].recovery_delay") | Integer |  |  | Min: 0<br>Max: 3600 | default -> platform_settings_mlag_reload_delay -> 300. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;links_minimum</samp>](## "&lt;node_type_keys.key&gt;.defaults.link_tracking.groups.[].links_minimum") | Integer |  |  | Min: 1<br>Max: 100000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;uplink_ipv4_pool</samp>](## "&lt;node_type_keys.key&gt;.defaults.uplink_ipv4_pool") | String |  |  | Format: ipv4_cidr | IPv4 subnet to use to connect to uplink switches. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;uplink_interfaces</samp>](## "&lt;node_type_keys.key&gt;.defaults.uplink_interfaces") | List, items: String |  |  |  | Local uplink interfaces<br>Each list item supports range syntax that can be expanded into a list of interfaces.<br>If uplink_interfaces is not defined, platform-specific defaults (defined under default_interfaces) will be used instead.<br>Please note that default_interfaces are not defined by default, you should define these yourself.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.defaults.uplink_interfaces.[].&lt;str&gt;") | String |  |  | Pattern: Ethernet[\d/]+ |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;uplink_switch_interfaces</samp>](## "&lt;node_type_keys.key&gt;.defaults.uplink_switch_interfaces") | List, items: String |  |  |  | Interfaces located on uplink switches. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.defaults.uplink_switch_interfaces.[].&lt;str&gt;") | String |  |  | Pattern: Ethernet[\d/]+ |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;uplink_switches</samp>](## "&lt;node_type_keys.key&gt;.defaults.uplink_switches") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.defaults.uplink_switches.[].&lt;str&gt;") | String | Required |  |  | Hostname of uplink switch.<br>If parallel uplinks are in use, update max_parallel_uplinks below and specify each uplink switch multiple times.<br>e.g. uplink_switches: [ 'DC1-SPINE1', 'DC1-SPINE1', 'DC1-SPINE2', 'DC1-SPINE2' ].<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;uplink_interface_speed</samp>](## "&lt;node_type_keys.key&gt;.defaults.uplink_interface_speed") | String |  |  |  | Set point-to-Point interface speed and will apply to uplink interfaces on both ends.<br>interface_speed or forced interface_speed or auto interface_speed.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;max_uplink_switches</samp>](## "&lt;node_type_keys.key&gt;.defaults.max_uplink_switches") | Integer |  |  |  | Maximum number of uplink switches.<br>Changing this value may change IP Addressing on uplinks.<br>Can be used to reserve IP space for future expansions.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;max_parallel_uplinks</samp>](## "&lt;node_type_keys.key&gt;.defaults.max_parallel_uplinks") | Integer |  |  |  | Number of parallel links towards uplink switches.<br>Changing this value may change interface naming on uplinks (and corresponding downlinks).<br>Can be used to reserve interfaces for future parallel uplinks.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;uplink_bfd</samp>](## "&lt;node_type_keys.key&gt;.defaults.uplink_bfd") | Boolean |  | `False` |  | Enable bfd on uplink interfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;uplink_native_vlan</samp>](## "&lt;node_type_keys.key&gt;.defaults.uplink_native_vlan") | Integer |  |  | Min: 1<br>Max: 4094 | Only applicable to switches with layer-2 port-channel uplinks.<br>A suspended (disabled) vlan will be created in both ends of the link unless the vlan is defined under network services.<br>By default the uplink will not have a native_vlan configured, so EOS defaults to vlan 1.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;uplink_ptp</samp>](## "&lt;node_type_keys.key&gt;.defaults.uplink_ptp") | Dictionary |  |  |  | Enable PTP on all infrastructure links. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable</samp>](## "&lt;node_type_keys.key&gt;.defaults.uplink_ptp.enable") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;uplink_macsec</samp>](## "&lt;node_type_keys.key&gt;.defaults.uplink_macsec") | Dictionary |  |  |  | Enable MacSec on all uplinks. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "&lt;node_type_keys.key&gt;.defaults.uplink_macsec.profile") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;uplink_structured_config</samp>](## "&lt;node_type_keys.key&gt;.defaults.uplink_structured_config") | Dictionary |  |  |  | Custom structured config applied to "uplink_interfaces", and "uplink_switch_interfaces".<br>When uplink_type == "p2p", custom structured config added under ethernet_interfaces.[name=<interface>] for eos_cli_config_gen overrides the settings on the ethernet interface level.<br>When uplink_type == "port-channel", custom structured config added under port_channel_interfaces.[name=<interface>] for eos_cli_config_gen overrides the settings on the port-channel interface level.<br>"uplink_structured_config" is applied after "structured_config", so it can override "structured_config" defined on node-level.<br>Note! The content of this dictionary is _not_ validated by the schema, since it can be either ethernet_interfaces or port_channel_interfaces.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;short_esi</samp>](## "&lt;node_type_keys.key&gt;.defaults.short_esi") | String |  |  |  | short_esi only valid for l2leaf devices using port-channel uplink.<br>Setting short_esi to "auto" generates the short_esi automatically using a hash of configuration elements.<br>< 0000:0000:0000 | auto >.<br> |
    | [<samp>&nbsp;&nbsp;node_groups</samp>](## "&lt;node_type_keys.key&gt;.node_groups") | List, items: Dictionary |  |  |  | Define variables related to all nodes part of this group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- group</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].group") | String | Required, Unique |  |  | The Node Group Name is used for MLAG domain unless set with 'mlag_domain_id'.<br>The Node Group Name is also used for peer description on downstream switches' uplinks.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;link_tracking</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].link_tracking") | Dictionary |  |  |  | This configures the Link Tracking Group on a switch as well as adds the p2p-uplinks of the switch as the upstream interfaces.<br>Useful in EVPN multhoming designs.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].link_tracking.enabled") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;groups</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].link_tracking.groups") | List, items: Dictionary |  | `[{'name': 'LT_GROUP1'}]` |  | Link Tracking Groups.<br>By default a single group named "LT_GROUP1" is defined with default values.<br>Any groups defined under "groups" will replace the default.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].link_tracking.groups.[].name") | String |  |  |  | Tracking group name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery_delay</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].link_tracking.groups.[].recovery_delay") | Integer |  |  | Min: 0<br>Max: 3600 | default -> platform_settings_mlag_reload_delay -> 300. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;links_minimum</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].link_tracking.groups.[].links_minimum") | Integer |  |  | Min: 1<br>Max: 100000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_ipv4_pool</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].uplink_ipv4_pool") | String |  |  | Format: ipv4_cidr | IPv4 subnet to use to connect to uplink switches. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_interfaces</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].uplink_interfaces") | List, items: String |  |  |  | Local uplink interfaces<br>Each list item supports range syntax that can be expanded into a list of interfaces.<br>If uplink_interfaces is not defined, platform-specific defaults (defined under default_interfaces) will be used instead.<br>Please note that default_interfaces are not defined by default, you should define these yourself.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].uplink_interfaces.[].&lt;str&gt;") | String |  |  | Pattern: Ethernet[\d/]+ |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_switch_interfaces</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].uplink_switch_interfaces") | List, items: String |  |  |  | Interfaces located on uplink switches. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].uplink_switch_interfaces.[].&lt;str&gt;") | String |  |  | Pattern: Ethernet[\d/]+ |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_switches</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].uplink_switches") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].uplink_switches.[].&lt;str&gt;") | String | Required |  |  | Hostname of uplink switch.<br>If parallel uplinks are in use, update max_parallel_uplinks below and specify each uplink switch multiple times.<br>e.g. uplink_switches: [ 'DC1-SPINE1', 'DC1-SPINE1', 'DC1-SPINE2', 'DC1-SPINE2' ].<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_interface_speed</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].uplink_interface_speed") | String |  |  |  | Set point-to-Point interface speed and will apply to uplink interfaces on both ends.<br>interface_speed or forced interface_speed or auto interface_speed.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_uplink_switches</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].max_uplink_switches") | Integer |  |  |  | Maximum number of uplink switches.<br>Changing this value may change IP Addressing on uplinks.<br>Can be used to reserve IP space for future expansions.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_parallel_uplinks</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].max_parallel_uplinks") | Integer |  |  |  | Number of parallel links towards uplink switches.<br>Changing this value may change interface naming on uplinks (and corresponding downlinks).<br>Can be used to reserve interfaces for future parallel uplinks.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_bfd</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].uplink_bfd") | Boolean |  | `False` |  | Enable bfd on uplink interfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_native_vlan</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].uplink_native_vlan") | Integer |  |  | Min: 1<br>Max: 4094 | Only applicable to switches with layer-2 port-channel uplinks.<br>A suspended (disabled) vlan will be created in both ends of the link unless the vlan is defined under network services.<br>By default the uplink will not have a native_vlan configured, so EOS defaults to vlan 1.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_ptp</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].uplink_ptp") | Dictionary |  |  |  | Enable PTP on all infrastructure links. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].uplink_ptp.enable") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_macsec</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].uplink_macsec") | Dictionary |  |  |  | Enable MacSec on all uplinks. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].uplink_macsec.profile") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_structured_config</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].uplink_structured_config") | Dictionary |  |  |  | Custom structured config applied to "uplink_interfaces", and "uplink_switch_interfaces".<br>When uplink_type == "p2p", custom structured config added under ethernet_interfaces.[name=<interface>] for eos_cli_config_gen overrides the settings on the ethernet interface level.<br>When uplink_type == "port-channel", custom structured config added under port_channel_interfaces.[name=<interface>] for eos_cli_config_gen overrides the settings on the port-channel interface level.<br>"uplink_structured_config" is applied after "structured_config", so it can override "structured_config" defined on node-level.<br>Note! The content of this dictionary is _not_ validated by the schema, since it can be either ethernet_interfaces or port_channel_interfaces.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;short_esi</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].nodes.[].short_esi") | String |  |  |  | short_esi only valid for l2leaf devices using port-channel uplink.<br>Setting short_esi to "auto" generates the short_esi automatically using a hash of configuration elements.<br>< 0000:0000:0000 | auto >.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;link_tracking</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].link_tracking") | Dictionary |  |  |  | This configures the Link Tracking Group on a switch as well as adds the p2p-uplinks of the switch as the upstream interfaces.<br>Useful in EVPN multhoming designs.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].link_tracking.enabled") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;groups</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].link_tracking.groups") | List, items: Dictionary |  | `[{'name': 'LT_GROUP1'}]` |  | Link Tracking Groups.<br>By default a single group named "LT_GROUP1" is defined with default values.<br>Any groups defined under "groups" will replace the default.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].link_tracking.groups.[].name") | String |  |  |  | Tracking group name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery_delay</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].link_tracking.groups.[].recovery_delay") | Integer |  |  | Min: 0<br>Max: 3600 | default -> platform_settings_mlag_reload_delay -> 300. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;links_minimum</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].link_tracking.groups.[].links_minimum") | Integer |  |  | Min: 1<br>Max: 100000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_ipv4_pool</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].uplink_ipv4_pool") | String |  |  | Format: ipv4_cidr | IPv4 subnet to use to connect to uplink switches. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_interfaces</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].uplink_interfaces") | List, items: String |  |  |  | Local uplink interfaces<br>Each list item supports range syntax that can be expanded into a list of interfaces.<br>If uplink_interfaces is not defined, platform-specific defaults (defined under default_interfaces) will be used instead.<br>Please note that default_interfaces are not defined by default, you should define these yourself.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].uplink_interfaces.[].&lt;str&gt;") | String |  |  | Pattern: Ethernet[\d/]+ |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_switch_interfaces</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].uplink_switch_interfaces") | List, items: String |  |  |  | Interfaces located on uplink switches. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].uplink_switch_interfaces.[].&lt;str&gt;") | String |  |  | Pattern: Ethernet[\d/]+ |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_switches</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].uplink_switches") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].uplink_switches.[].&lt;str&gt;") | String | Required |  |  | Hostname of uplink switch.<br>If parallel uplinks are in use, update max_parallel_uplinks below and specify each uplink switch multiple times.<br>e.g. uplink_switches: [ 'DC1-SPINE1', 'DC1-SPINE1', 'DC1-SPINE2', 'DC1-SPINE2' ].<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_interface_speed</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].uplink_interface_speed") | String |  |  |  | Set point-to-Point interface speed and will apply to uplink interfaces on both ends.<br>interface_speed or forced interface_speed or auto interface_speed.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_uplink_switches</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].max_uplink_switches") | Integer |  |  |  | Maximum number of uplink switches.<br>Changing this value may change IP Addressing on uplinks.<br>Can be used to reserve IP space for future expansions.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_parallel_uplinks</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].max_parallel_uplinks") | Integer |  |  |  | Number of parallel links towards uplink switches.<br>Changing this value may change interface naming on uplinks (and corresponding downlinks).<br>Can be used to reserve interfaces for future parallel uplinks.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_bfd</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].uplink_bfd") | Boolean |  | `False` |  | Enable bfd on uplink interfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_native_vlan</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].uplink_native_vlan") | Integer |  |  | Min: 1<br>Max: 4094 | Only applicable to switches with layer-2 port-channel uplinks.<br>A suspended (disabled) vlan will be created in both ends of the link unless the vlan is defined under network services.<br>By default the uplink will not have a native_vlan configured, so EOS defaults to vlan 1.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_ptp</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].uplink_ptp") | Dictionary |  |  |  | Enable PTP on all infrastructure links. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].uplink_ptp.enable") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_macsec</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].uplink_macsec") | Dictionary |  |  |  | Enable MacSec on all uplinks. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].uplink_macsec.profile") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_structured_config</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].uplink_structured_config") | Dictionary |  |  |  | Custom structured config applied to "uplink_interfaces", and "uplink_switch_interfaces".<br>When uplink_type == "p2p", custom structured config added under ethernet_interfaces.[name=<interface>] for eos_cli_config_gen overrides the settings on the ethernet interface level.<br>When uplink_type == "port-channel", custom structured config added under port_channel_interfaces.[name=<interface>] for eos_cli_config_gen overrides the settings on the port-channel interface level.<br>"uplink_structured_config" is applied after "structured_config", so it can override "structured_config" defined on node-level.<br>Note! The content of this dictionary is _not_ validated by the schema, since it can be either ethernet_interfaces or port_channel_interfaces.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;short_esi</samp>](## "&lt;node_type_keys.key&gt;.node_groups.[].short_esi") | String |  |  |  | short_esi only valid for l2leaf devices using port-channel uplink.<br>Setting short_esi to "auto" generates the short_esi automatically using a hash of configuration elements.<br>< 0000:0000:0000 | auto >.<br> |
    | [<samp>&nbsp;&nbsp;nodes</samp>](## "&lt;node_type_keys.key&gt;.nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;link_tracking</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].link_tracking") | Dictionary |  |  |  | This configures the Link Tracking Group on a switch as well as adds the p2p-uplinks of the switch as the upstream interfaces.<br>Useful in EVPN multhoming designs.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].link_tracking.enabled") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;groups</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].link_tracking.groups") | List, items: Dictionary |  | `[{'name': 'LT_GROUP1'}]` |  | Link Tracking Groups.<br>By default a single group named "LT_GROUP1" is defined with default values.<br>Any groups defined under "groups" will replace the default.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].link_tracking.groups.[].name") | String |  |  |  | Tracking group name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery_delay</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].link_tracking.groups.[].recovery_delay") | Integer |  |  | Min: 0<br>Max: 3600 | default -> platform_settings_mlag_reload_delay -> 300. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;links_minimum</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].link_tracking.groups.[].links_minimum") | Integer |  |  | Min: 1<br>Max: 100000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_ipv4_pool</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].uplink_ipv4_pool") | String |  |  | Format: ipv4_cidr | IPv4 subnet to use to connect to uplink switches. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_interfaces</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].uplink_interfaces") | List, items: String |  |  |  | Local uplink interfaces<br>Each list item supports range syntax that can be expanded into a list of interfaces.<br>If uplink_interfaces is not defined, platform-specific defaults (defined under default_interfaces) will be used instead.<br>Please note that default_interfaces are not defined by default, you should define these yourself.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].uplink_interfaces.[].&lt;str&gt;") | String |  |  | Pattern: Ethernet[\d/]+ |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_switch_interfaces</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].uplink_switch_interfaces") | List, items: String |  |  |  | Interfaces located on uplink switches. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].uplink_switch_interfaces.[].&lt;str&gt;") | String |  |  | Pattern: Ethernet[\d/]+ |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_switches</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].uplink_switches") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].uplink_switches.[].&lt;str&gt;") | String | Required |  |  | Hostname of uplink switch.<br>If parallel uplinks are in use, update max_parallel_uplinks below and specify each uplink switch multiple times.<br>e.g. uplink_switches: [ 'DC1-SPINE1', 'DC1-SPINE1', 'DC1-SPINE2', 'DC1-SPINE2' ].<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_interface_speed</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].uplink_interface_speed") | String |  |  |  | Set point-to-Point interface speed and will apply to uplink interfaces on both ends.<br>interface_speed or forced interface_speed or auto interface_speed.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_uplink_switches</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].max_uplink_switches") | Integer |  |  |  | Maximum number of uplink switches.<br>Changing this value may change IP Addressing on uplinks.<br>Can be used to reserve IP space for future expansions.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_parallel_uplinks</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].max_parallel_uplinks") | Integer |  |  |  | Number of parallel links towards uplink switches.<br>Changing this value may change interface naming on uplinks (and corresponding downlinks).<br>Can be used to reserve interfaces for future parallel uplinks.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_bfd</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].uplink_bfd") | Boolean |  | `False` |  | Enable bfd on uplink interfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_native_vlan</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].uplink_native_vlan") | Integer |  |  | Min: 1<br>Max: 4094 | Only applicable to switches with layer-2 port-channel uplinks.<br>A suspended (disabled) vlan will be created in both ends of the link unless the vlan is defined under network services.<br>By default the uplink will not have a native_vlan configured, so EOS defaults to vlan 1.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_ptp</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].uplink_ptp") | Dictionary |  |  |  | Enable PTP on all infrastructure links. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].uplink_ptp.enable") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_macsec</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].uplink_macsec") | Dictionary |  |  |  | Enable MacSec on all uplinks. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].uplink_macsec.profile") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uplink_structured_config</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].uplink_structured_config") | Dictionary |  |  |  | Custom structured config applied to "uplink_interfaces", and "uplink_switch_interfaces".<br>When uplink_type == "p2p", custom structured config added under ethernet_interfaces.[name=<interface>] for eos_cli_config_gen overrides the settings on the ethernet interface level.<br>When uplink_type == "port-channel", custom structured config added under port_channel_interfaces.[name=<interface>] for eos_cli_config_gen overrides the settings on the port-channel interface level.<br>"uplink_structured_config" is applied after "structured_config", so it can override "structured_config" defined on node-level.<br>Note! The content of this dictionary is _not_ validated by the schema, since it can be either ethernet_interfaces or port_channel_interfaces.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;short_esi</samp>](## "&lt;node_type_keys.key&gt;.nodes.[].short_esi") | String |  |  |  | short_esi only valid for l2leaf devices using port-channel uplink.<br>Setting short_esi to "auto" generates the short_esi automatically using a hash of configuration elements.<br>< 0000:0000:0000 | auto >.<br> |

=== "YAML"

    ```yaml
    <node_type_keys.key>:
      defaults:
        link_tracking:
          enabled: <bool>
          groups:
            - name: <str>
              recovery_delay: <int>
              links_minimum: <int>
        uplink_ipv4_pool: <str>
        uplink_interfaces:
          - <str>
        uplink_switch_interfaces:
          - <str>
        uplink_switches:
          - <str>
        uplink_interface_speed: <str>
        max_uplink_switches: <int>
        max_parallel_uplinks: <int>
        uplink_bfd: <bool>
        uplink_native_vlan: <int>
        uplink_ptp:
          enable: <bool>
        uplink_macsec:
          profile: <str>
        uplink_structured_config: <dict>
        short_esi: <str>
      node_groups:
        - group: <str>
          nodes:
            - name: <str>
              link_tracking:
                enabled: <bool>
                groups:
                  - name: <str>
                    recovery_delay: <int>
                    links_minimum: <int>
              uplink_ipv4_pool: <str>
              uplink_interfaces:
                - <str>
              uplink_switch_interfaces:
                - <str>
              uplink_switches:
                - <str>
              uplink_interface_speed: <str>
              max_uplink_switches: <int>
              max_parallel_uplinks: <int>
              uplink_bfd: <bool>
              uplink_native_vlan: <int>
              uplink_ptp:
                enable: <bool>
              uplink_macsec:
                profile: <str>
              uplink_structured_config: <dict>
              short_esi: <str>
          link_tracking:
            enabled: <bool>
            groups:
              - name: <str>
                recovery_delay: <int>
                links_minimum: <int>
          uplink_ipv4_pool: <str>
          uplink_interfaces:
            - <str>
          uplink_switch_interfaces:
            - <str>
          uplink_switches:
            - <str>
          uplink_interface_speed: <str>
          max_uplink_switches: <int>
          max_parallel_uplinks: <int>
          uplink_bfd: <bool>
          uplink_native_vlan: <int>
          uplink_ptp:
            enable: <bool>
          uplink_macsec:
            profile: <str>
          uplink_structured_config: <dict>
          short_esi: <str>
      nodes:
        - name: <str>
          link_tracking:
            enabled: <bool>
            groups:
              - name: <str>
                recovery_delay: <int>
                links_minimum: <int>
          uplink_ipv4_pool: <str>
          uplink_interfaces:
            - <str>
          uplink_switch_interfaces:
            - <str>
          uplink_switches:
            - <str>
          uplink_interface_speed: <str>
          max_uplink_switches: <int>
          max_parallel_uplinks: <int>
          uplink_bfd: <bool>
          uplink_native_vlan: <int>
          uplink_ptp:
            enable: <bool>
          uplink_macsec:
            profile: <str>
          uplink_structured_config: <dict>
          short_esi: <str>
    ```
