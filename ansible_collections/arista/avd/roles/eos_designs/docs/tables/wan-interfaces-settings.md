<!--
  ~ Copyright (c) 2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>&lt;node_type_keys.key&gt;</samp>](## "<node_type_keys.key>") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;defaults</samp>](## "<node_type_keys.key>.defaults") | Dictionary |  |  |  | Define variables for all nodes of this type. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;l3_interfaces</samp>](## "<node_type_keys.key>.defaults.l3_interfaces") | List, items: Dictionary |  |  |  | PREVIEW: This key is currently not supported<br><br>L3 Interfaces currently only use for WAN interfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;profile</samp>](## "<node_type_keys.key>.defaults.l3_interfaces.[].profile") | String |  |  |  | L3 interface profile name. Profile defined under `l3_interface_profiles`.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "<node_type_keys.key>.defaults.l3_interfaces.[].name") | String | Required, Unique |  | Pattern: Ethernet[\d/]+(.[\d]+)? | Ethernet interface name like 'Ethernet2' or subinterface name like 'Ethernet2.42'<br>For a subinterface, the parent physical interface is automatically created. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "<node_type_keys.key>.defaults.l3_interfaces.[].description") | String |  |  |  | Interface description.<br>If not set a default description will be configured with '[<peer>[ <peer_interface>]]' |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "<node_type_keys.key>.defaults.l3_interfaces.[].ip_address") | String |  |  |  | Node IPv4 address/Mask or 'dhcp'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;encapsulation_dot1q_vlan</samp>](## "<node_type_keys.key>.defaults.l3_interfaces.[].encapsulation_dot1q_vlan") | Integer |  |  | Min: 1<br>Max: 4094 | For subinterfaces the dot1q vlan is derived from the interface name by default, but can also be specified. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dhcp_accept_default_route</samp>](## "<node_type_keys.key>.defaults.l3_interfaces.[].dhcp_accept_default_route") | Boolean |  | `False` |  | Accept a default route from DHCP if `ip` is `dhcp`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<node_type_keys.key>.defaults.l3_interfaces.[].enabled") | Boolean |  | `True` |  | Enable or Shutdown the interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;speed</samp>](## "<node_type_keys.key>.defaults.l3_interfaces.[].speed") | String |  |  |  | Speed should be set in the format `<interface_speed>` or `forced <interface_speed>` or `auto <interface_speed>`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer</samp>](## "<node_type_keys.key>.defaults.l3_interfaces.[].peer") | String |  |  |  | The peer device name. Used for description and documentation |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_interface</samp>](## "<node_type_keys.key>.defaults.l3_interfaces.[].peer_interface") | String |  |  |  | The peer device interface. Used for description and documentation |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_ip</samp>](## "<node_type_keys.key>.defaults.l3_interfaces.[].peer_ip") | String |  |  |  | The peer device IPv4 address (no mask). Used as default route gateway if `set_default_route` is true and `ip` is an IP address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;static_routes</samp>](## "<node_type_keys.key>.defaults.l3_interfaces.[].static_routes") | List, items: Dictionary |  |  | Min Length: 1 | Configure IPv4 static routes pointing to `peer_ip`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;prefix</samp>](## "<node_type_keys.key>.defaults.l3_interfaces.[].static_routes.[].prefix") | String | Required |  |  | IPv4_network/Mask |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;qos_profile</samp>](## "<node_type_keys.key>.defaults.l3_interfaces.[].qos_profile") | String |  |  |  | QOS service profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;wan_carrier</samp>](## "<node_type_keys.key>.defaults.l3_interfaces.[].wan_carrier") | String |  |  |  | The WAN Carrier this interface is connected to.<br>This is used to infer the path-groups in which this interface should be configured. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;wan_circuit_id</samp>](## "<node_type_keys.key>.defaults.l3_interfaces.[].wan_circuit_id") | String |  |  |  | The WAN Circuit ID for this interface.<br>This is not rendered in the configuration but used for WAN designs. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;connected_to_pathfinder</samp>](## "<node_type_keys.key>.defaults.l3_interfaces.[].connected_to_pathfinder") | Boolean |  | `True` |  | For a WAN interface (`wan_path_group` is set), allow to disable the static tunnel towards Pathfinders. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "<node_type_keys.key>.defaults.l3_interfaces.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the interface in the final EOS configuration. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "<node_type_keys.key>.defaults.l3_interfaces.[].structured_config") | Dictionary |  |  |  | Custom structured config for the Ethernet interface. |
    | [<samp>&nbsp;&nbsp;node_groups</samp>](## "<node_type_keys.key>.node_groups") | List, items: Dictionary |  |  |  | Define variables related to all nodes part of this group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;group</samp>](## "<node_type_keys.key>.node_groups.[].group") | String | Required, Unique |  |  | The Node Group Name is used for MLAG domain unless set with 'mlag_domain_id'.<br>The Node Group Name is also used for peer description on downstream switches' uplinks.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "<node_type_keys.key>.node_groups.[].nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;l3_interfaces</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_interfaces") | List, items: Dictionary |  |  |  | PREVIEW: This key is currently not supported<br><br>L3 Interfaces currently only use for WAN interfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;profile</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_interfaces.[].profile") | String |  |  |  | L3 interface profile name. Profile defined under `l3_interface_profiles`.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_interfaces.[].name") | String | Required, Unique |  | Pattern: Ethernet[\d/]+(.[\d]+)? | Ethernet interface name like 'Ethernet2' or subinterface name like 'Ethernet2.42'<br>For a subinterface, the parent physical interface is automatically created. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_interfaces.[].description") | String |  |  |  | Interface description.<br>If not set a default description will be configured with '[<peer>[ <peer_interface>]]' |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_interfaces.[].ip_address") | String |  |  |  | Node IPv4 address/Mask or 'dhcp'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;encapsulation_dot1q_vlan</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_interfaces.[].encapsulation_dot1q_vlan") | Integer |  |  | Min: 1<br>Max: 4094 | For subinterfaces the dot1q vlan is derived from the interface name by default, but can also be specified. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dhcp_accept_default_route</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_interfaces.[].dhcp_accept_default_route") | Boolean |  | `False` |  | Accept a default route from DHCP if `ip` is `dhcp`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_interfaces.[].enabled") | Boolean |  | `True` |  | Enable or Shutdown the interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;speed</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_interfaces.[].speed") | String |  |  |  | Speed should be set in the format `<interface_speed>` or `forced <interface_speed>` or `auto <interface_speed>`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_interfaces.[].peer") | String |  |  |  | The peer device name. Used for description and documentation |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_interface</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_interfaces.[].peer_interface") | String |  |  |  | The peer device interface. Used for description and documentation |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_ip</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_interfaces.[].peer_ip") | String |  |  |  | The peer device IPv4 address (no mask). Used as default route gateway if `set_default_route` is true and `ip` is an IP address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;static_routes</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_interfaces.[].static_routes") | List, items: Dictionary |  |  | Min Length: 1 | Configure IPv4 static routes pointing to `peer_ip`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;prefix</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_interfaces.[].static_routes.[].prefix") | String | Required |  |  | IPv4_network/Mask |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;qos_profile</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_interfaces.[].qos_profile") | String |  |  |  | QOS service profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;wan_carrier</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_interfaces.[].wan_carrier") | String |  |  |  | The WAN Carrier this interface is connected to.<br>This is used to infer the path-groups in which this interface should be configured. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;wan_circuit_id</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_interfaces.[].wan_circuit_id") | String |  |  |  | The WAN Circuit ID for this interface.<br>This is not rendered in the configuration but used for WAN designs. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;connected_to_pathfinder</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_interfaces.[].connected_to_pathfinder") | Boolean |  | `True` |  | For a WAN interface (`wan_path_group` is set), allow to disable the static tunnel towards Pathfinders. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_interfaces.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the interface in the final EOS configuration. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_interfaces.[].structured_config") | Dictionary |  |  |  | Custom structured config for the Ethernet interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;l3_interfaces</samp>](## "<node_type_keys.key>.node_groups.[].l3_interfaces") | List, items: Dictionary |  |  |  | PREVIEW: This key is currently not supported<br><br>L3 Interfaces currently only use for WAN interfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;profile</samp>](## "<node_type_keys.key>.node_groups.[].l3_interfaces.[].profile") | String |  |  |  | L3 interface profile name. Profile defined under `l3_interface_profiles`.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "<node_type_keys.key>.node_groups.[].l3_interfaces.[].name") | String | Required, Unique |  | Pattern: Ethernet[\d/]+(.[\d]+)? | Ethernet interface name like 'Ethernet2' or subinterface name like 'Ethernet2.42'<br>For a subinterface, the parent physical interface is automatically created. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "<node_type_keys.key>.node_groups.[].l3_interfaces.[].description") | String |  |  |  | Interface description.<br>If not set a default description will be configured with '[<peer>[ <peer_interface>]]' |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "<node_type_keys.key>.node_groups.[].l3_interfaces.[].ip_address") | String |  |  |  | Node IPv4 address/Mask or 'dhcp'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;encapsulation_dot1q_vlan</samp>](## "<node_type_keys.key>.node_groups.[].l3_interfaces.[].encapsulation_dot1q_vlan") | Integer |  |  | Min: 1<br>Max: 4094 | For subinterfaces the dot1q vlan is derived from the interface name by default, but can also be specified. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dhcp_accept_default_route</samp>](## "<node_type_keys.key>.node_groups.[].l3_interfaces.[].dhcp_accept_default_route") | Boolean |  | `False` |  | Accept a default route from DHCP if `ip` is `dhcp`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<node_type_keys.key>.node_groups.[].l3_interfaces.[].enabled") | Boolean |  | `True` |  | Enable or Shutdown the interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;speed</samp>](## "<node_type_keys.key>.node_groups.[].l3_interfaces.[].speed") | String |  |  |  | Speed should be set in the format `<interface_speed>` or `forced <interface_speed>` or `auto <interface_speed>`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer</samp>](## "<node_type_keys.key>.node_groups.[].l3_interfaces.[].peer") | String |  |  |  | The peer device name. Used for description and documentation |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_interface</samp>](## "<node_type_keys.key>.node_groups.[].l3_interfaces.[].peer_interface") | String |  |  |  | The peer device interface. Used for description and documentation |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_ip</samp>](## "<node_type_keys.key>.node_groups.[].l3_interfaces.[].peer_ip") | String |  |  |  | The peer device IPv4 address (no mask). Used as default route gateway if `set_default_route` is true and `ip` is an IP address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;static_routes</samp>](## "<node_type_keys.key>.node_groups.[].l3_interfaces.[].static_routes") | List, items: Dictionary |  |  | Min Length: 1 | Configure IPv4 static routes pointing to `peer_ip`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;prefix</samp>](## "<node_type_keys.key>.node_groups.[].l3_interfaces.[].static_routes.[].prefix") | String | Required |  |  | IPv4_network/Mask |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;qos_profile</samp>](## "<node_type_keys.key>.node_groups.[].l3_interfaces.[].qos_profile") | String |  |  |  | QOS service profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;wan_carrier</samp>](## "<node_type_keys.key>.node_groups.[].l3_interfaces.[].wan_carrier") | String |  |  |  | The WAN Carrier this interface is connected to.<br>This is used to infer the path-groups in which this interface should be configured. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;wan_circuit_id</samp>](## "<node_type_keys.key>.node_groups.[].l3_interfaces.[].wan_circuit_id") | String |  |  |  | The WAN Circuit ID for this interface.<br>This is not rendered in the configuration but used for WAN designs. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;connected_to_pathfinder</samp>](## "<node_type_keys.key>.node_groups.[].l3_interfaces.[].connected_to_pathfinder") | Boolean |  | `True` |  | For a WAN interface (`wan_path_group` is set), allow to disable the static tunnel towards Pathfinders. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "<node_type_keys.key>.node_groups.[].l3_interfaces.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the interface in the final EOS configuration. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "<node_type_keys.key>.node_groups.[].l3_interfaces.[].structured_config") | Dictionary |  |  |  | Custom structured config for the Ethernet interface. |
    | [<samp>&nbsp;&nbsp;nodes</samp>](## "<node_type_keys.key>.nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<node_type_keys.key>.nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;l3_interfaces</samp>](## "<node_type_keys.key>.nodes.[].l3_interfaces") | List, items: Dictionary |  |  |  | PREVIEW: This key is currently not supported<br><br>L3 Interfaces currently only use for WAN interfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;profile</samp>](## "<node_type_keys.key>.nodes.[].l3_interfaces.[].profile") | String |  |  |  | L3 interface profile name. Profile defined under `l3_interface_profiles`.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "<node_type_keys.key>.nodes.[].l3_interfaces.[].name") | String | Required, Unique |  | Pattern: Ethernet[\d/]+(.[\d]+)? | Ethernet interface name like 'Ethernet2' or subinterface name like 'Ethernet2.42'<br>For a subinterface, the parent physical interface is automatically created. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "<node_type_keys.key>.nodes.[].l3_interfaces.[].description") | String |  |  |  | Interface description.<br>If not set a default description will be configured with '[<peer>[ <peer_interface>]]' |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "<node_type_keys.key>.nodes.[].l3_interfaces.[].ip_address") | String |  |  |  | Node IPv4 address/Mask or 'dhcp'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;encapsulation_dot1q_vlan</samp>](## "<node_type_keys.key>.nodes.[].l3_interfaces.[].encapsulation_dot1q_vlan") | Integer |  |  | Min: 1<br>Max: 4094 | For subinterfaces the dot1q vlan is derived from the interface name by default, but can also be specified. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dhcp_accept_default_route</samp>](## "<node_type_keys.key>.nodes.[].l3_interfaces.[].dhcp_accept_default_route") | Boolean |  | `False` |  | Accept a default route from DHCP if `ip` is `dhcp`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<node_type_keys.key>.nodes.[].l3_interfaces.[].enabled") | Boolean |  | `True` |  | Enable or Shutdown the interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;speed</samp>](## "<node_type_keys.key>.nodes.[].l3_interfaces.[].speed") | String |  |  |  | Speed should be set in the format `<interface_speed>` or `forced <interface_speed>` or `auto <interface_speed>`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer</samp>](## "<node_type_keys.key>.nodes.[].l3_interfaces.[].peer") | String |  |  |  | The peer device name. Used for description and documentation |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_interface</samp>](## "<node_type_keys.key>.nodes.[].l3_interfaces.[].peer_interface") | String |  |  |  | The peer device interface. Used for description and documentation |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_ip</samp>](## "<node_type_keys.key>.nodes.[].l3_interfaces.[].peer_ip") | String |  |  |  | The peer device IPv4 address (no mask). Used as default route gateway if `set_default_route` is true and `ip` is an IP address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;static_routes</samp>](## "<node_type_keys.key>.nodes.[].l3_interfaces.[].static_routes") | List, items: Dictionary |  |  | Min Length: 1 | Configure IPv4 static routes pointing to `peer_ip`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;prefix</samp>](## "<node_type_keys.key>.nodes.[].l3_interfaces.[].static_routes.[].prefix") | String | Required |  |  | IPv4_network/Mask |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;qos_profile</samp>](## "<node_type_keys.key>.nodes.[].l3_interfaces.[].qos_profile") | String |  |  |  | QOS service profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;wan_carrier</samp>](## "<node_type_keys.key>.nodes.[].l3_interfaces.[].wan_carrier") | String |  |  |  | The WAN Carrier this interface is connected to.<br>This is used to infer the path-groups in which this interface should be configured. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;wan_circuit_id</samp>](## "<node_type_keys.key>.nodes.[].l3_interfaces.[].wan_circuit_id") | String |  |  |  | The WAN Circuit ID for this interface.<br>This is not rendered in the configuration but used for WAN designs. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;connected_to_pathfinder</samp>](## "<node_type_keys.key>.nodes.[].l3_interfaces.[].connected_to_pathfinder") | Boolean |  | `True` |  | For a WAN interface (`wan_path_group` is set), allow to disable the static tunnel towards Pathfinders. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "<node_type_keys.key>.nodes.[].l3_interfaces.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the interface in the final EOS configuration. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "<node_type_keys.key>.nodes.[].l3_interfaces.[].structured_config") | Dictionary |  |  |  | Custom structured config for the Ethernet interface. |
    | [<samp>l3_interface_profiles</samp>](## "l3_interface_profiles") | List, items: Dictionary |  |  |  | PREVIEW: This key is currently not supported<br><br>Profiles to inherit common settings for l3_interfaces defined under the node type key.<br>These profiles will *not* work for `l3_interfaces` defined under `vrfs`. |
    | [<samp>&nbsp;&nbsp;-&nbsp;profile</samp>](## "l3_interface_profiles.[].profile") | String | Required, Unique |  |  | L3 interface profile name. Any variable supported under `l3_interfaces` can be inherited from a profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "l3_interface_profiles.[].name") | String |  |  | Pattern: Ethernet[\d/]+(.[\d]+)? | Ethernet interface name like 'Ethernet2' or subinterface name like 'Ethernet2.42'<br>For a subinterface, the parent physical interface is automatically created. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "l3_interface_profiles.[].description") | String |  |  |  | Interface description.<br>If not set a default description will be configured with '[<peer>[ <peer_interface>]]' |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "l3_interface_profiles.[].ip_address") | String |  |  |  | Node IPv4 address/Mask or 'dhcp'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;encapsulation_dot1q_vlan</samp>](## "l3_interface_profiles.[].encapsulation_dot1q_vlan") | Integer |  |  | Min: 1<br>Max: 4094 | For subinterfaces the dot1q vlan is derived from the interface name by default, but can also be specified. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;dhcp_accept_default_route</samp>](## "l3_interface_profiles.[].dhcp_accept_default_route") | Boolean |  | `False` |  | Accept a default route from DHCP if `ip` is `dhcp`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "l3_interface_profiles.[].enabled") | Boolean |  | `True` |  | Enable or Shutdown the interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;speed</samp>](## "l3_interface_profiles.[].speed") | String |  |  |  | Speed should be set in the format `<interface_speed>` or `forced <interface_speed>` or `auto <interface_speed>`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;peer</samp>](## "l3_interface_profiles.[].peer") | String |  |  |  | The peer device name. Used for description and documentation |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;peer_interface</samp>](## "l3_interface_profiles.[].peer_interface") | String |  |  |  | The peer device interface. Used for description and documentation |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;peer_ip</samp>](## "l3_interface_profiles.[].peer_ip") | String |  |  |  | The peer device IPv4 address (no mask). Used as default route gateway if `set_default_route` is true and `ip` is an IP address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;static_routes</samp>](## "l3_interface_profiles.[].static_routes") | List, items: Dictionary |  |  | Min Length: 1 | Configure IPv4 static routes pointing to `peer_ip`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;prefix</samp>](## "l3_interface_profiles.[].static_routes.[].prefix") | String | Required |  |  | IPv4_network/Mask |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;qos_profile</samp>](## "l3_interface_profiles.[].qos_profile") | String |  |  |  | QOS service profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;wan_carrier</samp>](## "l3_interface_profiles.[].wan_carrier") | String |  |  |  | The WAN Carrier this interface is connected to.<br>This is used to infer the path-groups in which this interface should be configured. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;wan_circuit_id</samp>](## "l3_interface_profiles.[].wan_circuit_id") | String |  |  |  | The WAN Circuit ID for this interface.<br>This is not rendered in the configuration but used for WAN designs. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;connected_to_pathfinder</samp>](## "l3_interface_profiles.[].connected_to_pathfinder") | Boolean |  | `True` |  | For a WAN interface (`wan_path_group` is set), allow to disable the static tunnel towards Pathfinders. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "l3_interface_profiles.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the interface in the final EOS configuration. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "l3_interface_profiles.[].structured_config") | Dictionary |  |  |  | Custom structured config for the Ethernet interface. |

=== "YAML"

    ```yaml
    <node_type_keys.key>:

      # Define variables for all nodes of this type.
      defaults:

        # PREVIEW: This key is currently not supported

        # L3 Interfaces currently only use for WAN interfaces.
        l3_interfaces:

            # L3 interface profile name. Profile defined under `l3_interface_profiles`.
          - profile: <str>

            # Ethernet interface name like 'Ethernet2' or subinterface name like 'Ethernet2.42'
            # For a subinterface, the parent physical interface is automatically created.
            name: <str; required; unique>

            # Interface description.
            # If not set a default description will be configured with '[<peer>[ <peer_interface>]]'
            description: <str>

            # Node IPv4 address/Mask or 'dhcp'.
            ip_address: <str>

            # For subinterfaces the dot1q vlan is derived from the interface name by default, but can also be specified.
            encapsulation_dot1q_vlan: <int; 1-4094>

            # Accept a default route from DHCP if `ip` is `dhcp`.
            dhcp_accept_default_route: <bool; default=False>

            # Enable or Shutdown the interface.
            enabled: <bool; default=True>

            # Speed should be set in the format `<interface_speed>` or `forced <interface_speed>` or `auto <interface_speed>`.
            speed: <str>

            # The peer device name. Used for description and documentation
            peer: <str>

            # The peer device interface. Used for description and documentation
            peer_interface: <str>

            # The peer device IPv4 address (no mask). Used as default route gateway if `set_default_route` is true and `ip` is an IP address.
            peer_ip: <str>

            # Configure IPv4 static routes pointing to `peer_ip`.
            static_routes: # >=1 items

                # IPv4_network/Mask
              - prefix: <str; required>

            # QOS service profile.
            qos_profile: <str>

            # The WAN Carrier this interface is connected to.
            # This is used to infer the path-groups in which this interface should be configured.
            wan_carrier: <str>

            # The WAN Circuit ID for this interface.
            # This is not rendered in the configuration but used for WAN designs.
            wan_circuit_id: <str>

            # For a WAN interface (`wan_path_group` is set), allow to disable the static tunnel towards Pathfinders.
            connected_to_pathfinder: <bool; default=True>

            # EOS CLI rendered directly on the interface in the final EOS configuration.
            raw_eos_cli: <str>

            # Custom structured config for the Ethernet interface.
            structured_config: <dict>

      # Define variables related to all nodes part of this group.
      node_groups:

          # The Node Group Name is used for MLAG domain unless set with 'mlag_domain_id'.
          # The Node Group Name is also used for peer description on downstream switches' uplinks.
        - group: <str; required; unique>

          # Define variables per node.
          nodes:

              # The Node Name is used as "hostname".
            - name: <str; required; unique>

              # PREVIEW: This key is currently not supported

              # L3 Interfaces currently only use for WAN interfaces.
              l3_interfaces:

                  # L3 interface profile name. Profile defined under `l3_interface_profiles`.
                - profile: <str>

                  # Ethernet interface name like 'Ethernet2' or subinterface name like 'Ethernet2.42'
                  # For a subinterface, the parent physical interface is automatically created.
                  name: <str; required; unique>

                  # Interface description.
                  # If not set a default description will be configured with '[<peer>[ <peer_interface>]]'
                  description: <str>

                  # Node IPv4 address/Mask or 'dhcp'.
                  ip_address: <str>

                  # For subinterfaces the dot1q vlan is derived from the interface name by default, but can also be specified.
                  encapsulation_dot1q_vlan: <int; 1-4094>

                  # Accept a default route from DHCP if `ip` is `dhcp`.
                  dhcp_accept_default_route: <bool; default=False>

                  # Enable or Shutdown the interface.
                  enabled: <bool; default=True>

                  # Speed should be set in the format `<interface_speed>` or `forced <interface_speed>` or `auto <interface_speed>`.
                  speed: <str>

                  # The peer device name. Used for description and documentation
                  peer: <str>

                  # The peer device interface. Used for description and documentation
                  peer_interface: <str>

                  # The peer device IPv4 address (no mask). Used as default route gateway if `set_default_route` is true and `ip` is an IP address.
                  peer_ip: <str>

                  # Configure IPv4 static routes pointing to `peer_ip`.
                  static_routes: # >=1 items

                      # IPv4_network/Mask
                    - prefix: <str; required>

                  # QOS service profile.
                  qos_profile: <str>

                  # The WAN Carrier this interface is connected to.
                  # This is used to infer the path-groups in which this interface should be configured.
                  wan_carrier: <str>

                  # The WAN Circuit ID for this interface.
                  # This is not rendered in the configuration but used for WAN designs.
                  wan_circuit_id: <str>

                  # For a WAN interface (`wan_path_group` is set), allow to disable the static tunnel towards Pathfinders.
                  connected_to_pathfinder: <bool; default=True>

                  # EOS CLI rendered directly on the interface in the final EOS configuration.
                  raw_eos_cli: <str>

                  # Custom structured config for the Ethernet interface.
                  structured_config: <dict>

          # PREVIEW: This key is currently not supported

          # L3 Interfaces currently only use for WAN interfaces.
          l3_interfaces:

              # L3 interface profile name. Profile defined under `l3_interface_profiles`.
            - profile: <str>

              # Ethernet interface name like 'Ethernet2' or subinterface name like 'Ethernet2.42'
              # For a subinterface, the parent physical interface is automatically created.
              name: <str; required; unique>

              # Interface description.
              # If not set a default description will be configured with '[<peer>[ <peer_interface>]]'
              description: <str>

              # Node IPv4 address/Mask or 'dhcp'.
              ip_address: <str>

              # For subinterfaces the dot1q vlan is derived from the interface name by default, but can also be specified.
              encapsulation_dot1q_vlan: <int; 1-4094>

              # Accept a default route from DHCP if `ip` is `dhcp`.
              dhcp_accept_default_route: <bool; default=False>

              # Enable or Shutdown the interface.
              enabled: <bool; default=True>

              # Speed should be set in the format `<interface_speed>` or `forced <interface_speed>` or `auto <interface_speed>`.
              speed: <str>

              # The peer device name. Used for description and documentation
              peer: <str>

              # The peer device interface. Used for description and documentation
              peer_interface: <str>

              # The peer device IPv4 address (no mask). Used as default route gateway if `set_default_route` is true and `ip` is an IP address.
              peer_ip: <str>

              # Configure IPv4 static routes pointing to `peer_ip`.
              static_routes: # >=1 items

                  # IPv4_network/Mask
                - prefix: <str; required>

              # QOS service profile.
              qos_profile: <str>

              # The WAN Carrier this interface is connected to.
              # This is used to infer the path-groups in which this interface should be configured.
              wan_carrier: <str>

              # The WAN Circuit ID for this interface.
              # This is not rendered in the configuration but used for WAN designs.
              wan_circuit_id: <str>

              # For a WAN interface (`wan_path_group` is set), allow to disable the static tunnel towards Pathfinders.
              connected_to_pathfinder: <bool; default=True>

              # EOS CLI rendered directly on the interface in the final EOS configuration.
              raw_eos_cli: <str>

              # Custom structured config for the Ethernet interface.
              structured_config: <dict>

      # Define variables per node.
      nodes:

          # The Node Name is used as "hostname".
        - name: <str; required; unique>

          # PREVIEW: This key is currently not supported

          # L3 Interfaces currently only use for WAN interfaces.
          l3_interfaces:

              # L3 interface profile name. Profile defined under `l3_interface_profiles`.
            - profile: <str>

              # Ethernet interface name like 'Ethernet2' or subinterface name like 'Ethernet2.42'
              # For a subinterface, the parent physical interface is automatically created.
              name: <str; required; unique>

              # Interface description.
              # If not set a default description will be configured with '[<peer>[ <peer_interface>]]'
              description: <str>

              # Node IPv4 address/Mask or 'dhcp'.
              ip_address: <str>

              # For subinterfaces the dot1q vlan is derived from the interface name by default, but can also be specified.
              encapsulation_dot1q_vlan: <int; 1-4094>

              # Accept a default route from DHCP if `ip` is `dhcp`.
              dhcp_accept_default_route: <bool; default=False>

              # Enable or Shutdown the interface.
              enabled: <bool; default=True>

              # Speed should be set in the format `<interface_speed>` or `forced <interface_speed>` or `auto <interface_speed>`.
              speed: <str>

              # The peer device name. Used for description and documentation
              peer: <str>

              # The peer device interface. Used for description and documentation
              peer_interface: <str>

              # The peer device IPv4 address (no mask). Used as default route gateway if `set_default_route` is true and `ip` is an IP address.
              peer_ip: <str>

              # Configure IPv4 static routes pointing to `peer_ip`.
              static_routes: # >=1 items

                  # IPv4_network/Mask
                - prefix: <str; required>

              # QOS service profile.
              qos_profile: <str>

              # The WAN Carrier this interface is connected to.
              # This is used to infer the path-groups in which this interface should be configured.
              wan_carrier: <str>

              # The WAN Circuit ID for this interface.
              # This is not rendered in the configuration but used for WAN designs.
              wan_circuit_id: <str>

              # For a WAN interface (`wan_path_group` is set), allow to disable the static tunnel towards Pathfinders.
              connected_to_pathfinder: <bool; default=True>

              # EOS CLI rendered directly on the interface in the final EOS configuration.
              raw_eos_cli: <str>

              # Custom structured config for the Ethernet interface.
              structured_config: <dict>

    # PREVIEW: This key is currently not supported

    # Profiles to inherit common settings for l3_interfaces defined under the node type key.
    # These profiles will *not* work for `l3_interfaces` defined under `vrfs`.
    l3_interface_profiles:

        # L3 interface profile name. Any variable supported under `l3_interfaces` can be inherited from a profile.
      - profile: <str; required; unique>

        # Ethernet interface name like 'Ethernet2' or subinterface name like 'Ethernet2.42'
        # For a subinterface, the parent physical interface is automatically created.
        name: <str>

        # Interface description.
        # If not set a default description will be configured with '[<peer>[ <peer_interface>]]'
        description: <str>

        # Node IPv4 address/Mask or 'dhcp'.
        ip_address: <str>

        # For subinterfaces the dot1q vlan is derived from the interface name by default, but can also be specified.
        encapsulation_dot1q_vlan: <int; 1-4094>

        # Accept a default route from DHCP if `ip` is `dhcp`.
        dhcp_accept_default_route: <bool; default=False>

        # Enable or Shutdown the interface.
        enabled: <bool; default=True>

        # Speed should be set in the format `<interface_speed>` or `forced <interface_speed>` or `auto <interface_speed>`.
        speed: <str>

        # The peer device name. Used for description and documentation
        peer: <str>

        # The peer device interface. Used for description and documentation
        peer_interface: <str>

        # The peer device IPv4 address (no mask). Used as default route gateway if `set_default_route` is true and `ip` is an IP address.
        peer_ip: <str>

        # Configure IPv4 static routes pointing to `peer_ip`.
        static_routes: # >=1 items

            # IPv4_network/Mask
          - prefix: <str; required>

        # QOS service profile.
        qos_profile: <str>

        # The WAN Carrier this interface is connected to.
        # This is used to infer the path-groups in which this interface should be configured.
        wan_carrier: <str>

        # The WAN Circuit ID for this interface.
        # This is not rendered in the configuration but used for WAN designs.
        wan_circuit_id: <str>

        # For a WAN interface (`wan_path_group` is set), allow to disable the static tunnel towards Pathfinders.
        connected_to_pathfinder: <bool; default=True>

        # EOS CLI rendered directly on the interface in the final EOS configuration.
        raw_eos_cli: <str>

        # Custom structured config for the Ethernet interface.
        structured_config: <dict>
    ```
