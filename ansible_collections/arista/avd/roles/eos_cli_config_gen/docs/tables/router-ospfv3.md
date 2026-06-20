<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>router_ospfv3</samp>](## "router_ospfv3") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;router_id</samp>](## "router_ospfv3.router_id") | String |  |  |  | IPv4 Address. |
    | [<samp>&nbsp;&nbsp;passive_interface_default</samp>](## "router_ospfv3.passive_interface_default") | Boolean |  |  |  | Set all interfaces to passive by default. |
    | [<samp>&nbsp;&nbsp;auto_cost_reference_bandwidth</samp>](## "router_ospfv3.auto_cost_reference_bandwidth") | Integer |  |  | Min: 1<br>Max: 4294967 | Reference bandwidth in Mbps. |
    | [<samp>&nbsp;&nbsp;address_family_ipv4</samp>](## "router_ospfv3.address_family_ipv4") | Dictionary |  |  |  | Address family IPv4 configuration.<br>Common configurations defined at the router-level and address-family level are mutually exclusive.<br>If both are provided, the address-family level configuration takes precedence. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_ospfv3.address_family_ipv4.enabled") | Boolean | Required |  |  | Activate the address family. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;router_id</samp>](## "router_ospfv3.address_family_ipv4.router_id") | String |  |  |  | IPv4 Address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;passive_interface_default</samp>](## "router_ospfv3.address_family_ipv4.passive_interface_default") | Boolean |  |  |  | Set all interfaces to passive by default. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;auto_cost_reference_bandwidth</samp>](## "router_ospfv3.address_family_ipv4.auto_cost_reference_bandwidth") | Integer |  |  | Min: 1<br>Max: 4294967 | Reference bandwidth in Mbps. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;redistribute</samp>](## "router_ospfv3.address_family_ipv4.redistribute") | Dictionary |  |  |  | Redistribute routes with OSPFv3. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "router_ospfv3.address_family_ipv4.redistribute.bgp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_ospfv3.address_family_ipv4.redistribute.bgp.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_ospfv3.address_family_ipv4.redistribute.bgp.route_map") | String |  |  |  | Specify route map to use. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_ospfv3.address_family_ipv4.redistribute.bgp.include_leaked") | Boolean |  |  |  | Include leaked routes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;connected</samp>](## "router_ospfv3.address_family_ipv4.redistribute.connected") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_ospfv3.address_family_ipv4.redistribute.connected.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_ospfv3.address_family_ipv4.redistribute.connected.route_map") | String |  |  |  | Specify route map to use. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_ospfv3.address_family_ipv4.redistribute.connected.include_leaked") | Boolean |  |  |  | Include leaked routes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;static</samp>](## "router_ospfv3.address_family_ipv4.redistribute.static") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_ospfv3.address_family_ipv4.redistribute.static.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_ospfv3.address_family_ipv4.redistribute.static.route_map") | String |  |  |  | Specify route map to use. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_ospfv3.address_family_ipv4.redistribute.static.include_leaked") | Boolean |  |  |  | Include leaked routes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis</samp>](## "router_ospfv3.address_family_ipv4.redistribute.isis") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_ospfv3.address_family_ipv4.redistribute.isis.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp>](## "router_ospfv3.address_family_ipv4.redistribute.isis.level") | String |  |  | Valid Values:<br>- <code>level-1</code><br>- <code>level-2</code><br>- <code>level-1-2</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_ospfv3.address_family_ipv4.redistribute.isis.route_map") | String |  |  |  | Specify route map to use. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_ospfv3.address_family_ipv4.redistribute.isis.include_leaked") | Boolean |  |  |  | Include leaked routes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ospfv3</samp>](## "router_ospfv3.address_family_ipv4.redistribute.ospfv3") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_ospfv3.address_family_ipv4.redistribute.ospfv3.enabled") | Boolean |  |  |  | Redistribute all OSPFv3 leaked routes.<br>Mutually exclusive with match_internal. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_ospfv3.address_family_ipv4.redistribute.ospfv3.route_map") | String |  |  |  | Specify route map to use. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_internal</samp>](## "router_ospfv3.address_family_ipv4.redistribute.ospfv3.match_internal") | Dictionary |  |  |  | Redistribute only internal OSPFv3 leaked routes.<br>Mutually exclusive with `enabled`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_ospfv3.address_family_ipv4.redistribute.ospfv3.match_internal.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_ospfv3.address_family_ipv4.redistribute.ospfv3.match_internal.route_map") | String |  |  |  | Specify route map to use. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_external</samp>](## "router_ospfv3.address_family_ipv4.redistribute.ospfv3.match_external") | Dictionary |  |  |  | Redistribute external OSPFv3 leaked routes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_ospfv3.address_family_ipv4.redistribute.ospfv3.match_external.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_ospfv3.address_family_ipv4.redistribute.ospfv3.match_external.route_map") | String |  |  |  | Specify route map to use. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_nssa_external</samp>](## "router_ospfv3.address_family_ipv4.redistribute.ospfv3.match_nssa_external") | Dictionary |  |  |  | Redistribute NSSA external OSPFv3 leaked routes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_ospfv3.address_family_ipv4.redistribute.ospfv3.match_nssa_external.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_ospfv3.address_family_ipv4.redistribute.ospfv3.match_nssa_external.route_map") | String |  |  |  | Specify route map to use. |
    | [<samp>&nbsp;&nbsp;address_family_ipv6</samp>](## "router_ospfv3.address_family_ipv6") | Dictionary |  |  |  | Address family IPv6 configuration.<br>Common configurations defined at the router-level and address-family level are mutually exclusive.<br>If both are provided, the address-family level configuration takes precedence. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_ospfv3.address_family_ipv6.enabled") | Boolean | Required |  |  | Activate the address family. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;router_id</samp>](## "router_ospfv3.address_family_ipv6.router_id") | String |  |  |  | IPv4 Address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;passive_interface_default</samp>](## "router_ospfv3.address_family_ipv6.passive_interface_default") | Boolean |  |  |  | Set all interfaces to passive by default. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;auto_cost_reference_bandwidth</samp>](## "router_ospfv3.address_family_ipv6.auto_cost_reference_bandwidth") | Integer |  |  | Min: 1<br>Max: 4294967 | Reference bandwidth in Mbps. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;redistribute</samp>](## "router_ospfv3.address_family_ipv6.redistribute") | Dictionary |  |  |  | Redistribute routes with OSPFv3. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "router_ospfv3.address_family_ipv6.redistribute.bgp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_ospfv3.address_family_ipv6.redistribute.bgp.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_ospfv3.address_family_ipv6.redistribute.bgp.route_map") | String |  |  |  | Specify route map to use. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_ospfv3.address_family_ipv6.redistribute.bgp.include_leaked") | Boolean |  |  |  | Include leaked routes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;connected</samp>](## "router_ospfv3.address_family_ipv6.redistribute.connected") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_ospfv3.address_family_ipv6.redistribute.connected.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_ospfv3.address_family_ipv6.redistribute.connected.route_map") | String |  |  |  | Specify route map to use. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_ospfv3.address_family_ipv6.redistribute.connected.include_leaked") | Boolean |  |  |  | Include leaked routes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;static</samp>](## "router_ospfv3.address_family_ipv6.redistribute.static") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_ospfv3.address_family_ipv6.redistribute.static.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_ospfv3.address_family_ipv6.redistribute.static.route_map") | String |  |  |  | Specify route map to use. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_ospfv3.address_family_ipv6.redistribute.static.include_leaked") | Boolean |  |  |  | Include leaked routes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis</samp>](## "router_ospfv3.address_family_ipv6.redistribute.isis") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_ospfv3.address_family_ipv6.redistribute.isis.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp>](## "router_ospfv3.address_family_ipv6.redistribute.isis.level") | String |  |  | Valid Values:<br>- <code>level-1</code><br>- <code>level-2</code><br>- <code>level-1-2</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_ospfv3.address_family_ipv6.redistribute.isis.route_map") | String |  |  |  | Specify route map to use. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_ospfv3.address_family_ipv6.redistribute.isis.include_leaked") | Boolean |  |  |  | Include leaked routes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ospfv3</samp>](## "router_ospfv3.address_family_ipv6.redistribute.ospfv3") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_ospfv3.address_family_ipv6.redistribute.ospfv3.enabled") | Boolean |  |  |  | Redistribute all OSPFv3 leaked routes.<br>Mutually exclusive with match_internal. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_ospfv3.address_family_ipv6.redistribute.ospfv3.route_map") | String |  |  |  | Specify route map to use. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_internal</samp>](## "router_ospfv3.address_family_ipv6.redistribute.ospfv3.match_internal") | Dictionary |  |  |  | Redistribute only internal OSPFv3 leaked routes.<br>Mutually exclusive with `enabled`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_ospfv3.address_family_ipv6.redistribute.ospfv3.match_internal.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_ospfv3.address_family_ipv6.redistribute.ospfv3.match_internal.route_map") | String |  |  |  | Specify route map to use. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_external</samp>](## "router_ospfv3.address_family_ipv6.redistribute.ospfv3.match_external") | Dictionary |  |  |  | Redistribute external OSPFv3 leaked routes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_ospfv3.address_family_ipv6.redistribute.ospfv3.match_external.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_ospfv3.address_family_ipv6.redistribute.ospfv3.match_external.route_map") | String |  |  |  | Specify route map to use. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_nssa_external</samp>](## "router_ospfv3.address_family_ipv6.redistribute.ospfv3.match_nssa_external") | Dictionary |  |  |  | Redistribute NSSA external OSPFv3 leaked routes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_ospfv3.address_family_ipv6.redistribute.ospfv3.match_nssa_external.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_ospfv3.address_family_ipv6.redistribute.ospfv3.match_nssa_external.route_map") | String |  |  |  | Specify route map to use. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dhcp</samp>](## "router_ospfv3.address_family_ipv6.redistribute.dhcp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_ospfv3.address_family_ipv6.redistribute.dhcp.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_ospfv3.address_family_ipv6.redistribute.dhcp.route_map") | String |  |  |  | Specify route map to use. |
    | [<samp>&nbsp;&nbsp;eos_cli</samp>](## "router_ospfv3.eos_cli") | String |  |  |  | Multiline EOS CLI rendered directly on the default VRF OSPFv3 instance. |
    | [<samp>&nbsp;&nbsp;vrfs</samp>](## "router_ospfv3.vrfs") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "router_ospfv3.vrfs.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;router_id</samp>](## "router_ospfv3.vrfs.[].router_id") | String |  |  |  | IPv4 Address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;passive_interface_default</samp>](## "router_ospfv3.vrfs.[].passive_interface_default") | Boolean |  |  |  | Set all interfaces to passive by default. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;auto_cost_reference_bandwidth</samp>](## "router_ospfv3.vrfs.[].auto_cost_reference_bandwidth") | Integer |  |  | Min: 1<br>Max: 4294967 | Reference bandwidth in Mbps. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_family_ipv4</samp>](## "router_ospfv3.vrfs.[].address_family_ipv4") | Dictionary |  |  |  | Address family IPv4 configuration.<br>Common configurations defined at the router-level and address-family level are mutually exclusive.<br>If both are provided, the address-family level configuration takes precedence. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_ospfv3.vrfs.[].address_family_ipv4.enabled") | Boolean | Required |  |  | Activate the address family. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;router_id</samp>](## "router_ospfv3.vrfs.[].address_family_ipv4.router_id") | String |  |  |  | IPv4 Address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;passive_interface_default</samp>](## "router_ospfv3.vrfs.[].address_family_ipv4.passive_interface_default") | Boolean |  |  |  | Set all interfaces to passive by default. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;auto_cost_reference_bandwidth</samp>](## "router_ospfv3.vrfs.[].address_family_ipv4.auto_cost_reference_bandwidth") | Integer |  |  | Min: 1<br>Max: 4294967 | Reference bandwidth in Mbps. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;redistribute</samp>](## "router_ospfv3.vrfs.[].address_family_ipv4.redistribute") | Dictionary |  |  |  | Redistribute routes with OSPFv3. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "router_ospfv3.vrfs.[].address_family_ipv4.redistribute.bgp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_ospfv3.vrfs.[].address_family_ipv4.redistribute.bgp.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_ospfv3.vrfs.[].address_family_ipv4.redistribute.bgp.route_map") | String |  |  |  | Specify route map to use. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_ospfv3.vrfs.[].address_family_ipv4.redistribute.bgp.include_leaked") | Boolean |  |  |  | Include leaked routes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;connected</samp>](## "router_ospfv3.vrfs.[].address_family_ipv4.redistribute.connected") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_ospfv3.vrfs.[].address_family_ipv4.redistribute.connected.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_ospfv3.vrfs.[].address_family_ipv4.redistribute.connected.route_map") | String |  |  |  | Specify route map to use. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_ospfv3.vrfs.[].address_family_ipv4.redistribute.connected.include_leaked") | Boolean |  |  |  | Include leaked routes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;static</samp>](## "router_ospfv3.vrfs.[].address_family_ipv4.redistribute.static") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_ospfv3.vrfs.[].address_family_ipv4.redistribute.static.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_ospfv3.vrfs.[].address_family_ipv4.redistribute.static.route_map") | String |  |  |  | Specify route map to use. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_ospfv3.vrfs.[].address_family_ipv4.redistribute.static.include_leaked") | Boolean |  |  |  | Include leaked routes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis</samp>](## "router_ospfv3.vrfs.[].address_family_ipv4.redistribute.isis") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_ospfv3.vrfs.[].address_family_ipv4.redistribute.isis.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp>](## "router_ospfv3.vrfs.[].address_family_ipv4.redistribute.isis.level") | String |  |  | Valid Values:<br>- <code>level-1</code><br>- <code>level-2</code><br>- <code>level-1-2</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_ospfv3.vrfs.[].address_family_ipv4.redistribute.isis.route_map") | String |  |  |  | Specify route map to use. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_ospfv3.vrfs.[].address_family_ipv4.redistribute.isis.include_leaked") | Boolean |  |  |  | Include leaked routes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ospfv3</samp>](## "router_ospfv3.vrfs.[].address_family_ipv4.redistribute.ospfv3") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_ospfv3.vrfs.[].address_family_ipv4.redistribute.ospfv3.enabled") | Boolean |  |  |  | Redistribute all OSPFv3 leaked routes.<br>Mutually exclusive with match_internal. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_ospfv3.vrfs.[].address_family_ipv4.redistribute.ospfv3.route_map") | String |  |  |  | Specify route map to use. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_internal</samp>](## "router_ospfv3.vrfs.[].address_family_ipv4.redistribute.ospfv3.match_internal") | Dictionary |  |  |  | Redistribute only internal OSPFv3 leaked routes.<br>Mutually exclusive with `enabled`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_ospfv3.vrfs.[].address_family_ipv4.redistribute.ospfv3.match_internal.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_ospfv3.vrfs.[].address_family_ipv4.redistribute.ospfv3.match_internal.route_map") | String |  |  |  | Specify route map to use. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_external</samp>](## "router_ospfv3.vrfs.[].address_family_ipv4.redistribute.ospfv3.match_external") | Dictionary |  |  |  | Redistribute external OSPFv3 leaked routes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_ospfv3.vrfs.[].address_family_ipv4.redistribute.ospfv3.match_external.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_ospfv3.vrfs.[].address_family_ipv4.redistribute.ospfv3.match_external.route_map") | String |  |  |  | Specify route map to use. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_nssa_external</samp>](## "router_ospfv3.vrfs.[].address_family_ipv4.redistribute.ospfv3.match_nssa_external") | Dictionary |  |  |  | Redistribute NSSA external OSPFv3 leaked routes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_ospfv3.vrfs.[].address_family_ipv4.redistribute.ospfv3.match_nssa_external.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_ospfv3.vrfs.[].address_family_ipv4.redistribute.ospfv3.match_nssa_external.route_map") | String |  |  |  | Specify route map to use. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_family_ipv6</samp>](## "router_ospfv3.vrfs.[].address_family_ipv6") | Dictionary |  |  |  | Address family IPv6 configuration.<br>Common configurations defined at the router-level and address-family level are mutually exclusive.<br>If both are provided, the address-family level configuration takes precedence. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_ospfv3.vrfs.[].address_family_ipv6.enabled") | Boolean | Required |  |  | Activate the address family. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;router_id</samp>](## "router_ospfv3.vrfs.[].address_family_ipv6.router_id") | String |  |  |  | IPv4 Address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;passive_interface_default</samp>](## "router_ospfv3.vrfs.[].address_family_ipv6.passive_interface_default") | Boolean |  |  |  | Set all interfaces to passive by default. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;auto_cost_reference_bandwidth</samp>](## "router_ospfv3.vrfs.[].address_family_ipv6.auto_cost_reference_bandwidth") | Integer |  |  | Min: 1<br>Max: 4294967 | Reference bandwidth in Mbps. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;redistribute</samp>](## "router_ospfv3.vrfs.[].address_family_ipv6.redistribute") | Dictionary |  |  |  | Redistribute routes with OSPFv3. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "router_ospfv3.vrfs.[].address_family_ipv6.redistribute.bgp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_ospfv3.vrfs.[].address_family_ipv6.redistribute.bgp.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_ospfv3.vrfs.[].address_family_ipv6.redistribute.bgp.route_map") | String |  |  |  | Specify route map to use. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_ospfv3.vrfs.[].address_family_ipv6.redistribute.bgp.include_leaked") | Boolean |  |  |  | Include leaked routes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;connected</samp>](## "router_ospfv3.vrfs.[].address_family_ipv6.redistribute.connected") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_ospfv3.vrfs.[].address_family_ipv6.redistribute.connected.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_ospfv3.vrfs.[].address_family_ipv6.redistribute.connected.route_map") | String |  |  |  | Specify route map to use. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_ospfv3.vrfs.[].address_family_ipv6.redistribute.connected.include_leaked") | Boolean |  |  |  | Include leaked routes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;static</samp>](## "router_ospfv3.vrfs.[].address_family_ipv6.redistribute.static") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_ospfv3.vrfs.[].address_family_ipv6.redistribute.static.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_ospfv3.vrfs.[].address_family_ipv6.redistribute.static.route_map") | String |  |  |  | Specify route map to use. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_ospfv3.vrfs.[].address_family_ipv6.redistribute.static.include_leaked") | Boolean |  |  |  | Include leaked routes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis</samp>](## "router_ospfv3.vrfs.[].address_family_ipv6.redistribute.isis") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_ospfv3.vrfs.[].address_family_ipv6.redistribute.isis.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp>](## "router_ospfv3.vrfs.[].address_family_ipv6.redistribute.isis.level") | String |  |  | Valid Values:<br>- <code>level-1</code><br>- <code>level-2</code><br>- <code>level-1-2</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_ospfv3.vrfs.[].address_family_ipv6.redistribute.isis.route_map") | String |  |  |  | Specify route map to use. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_ospfv3.vrfs.[].address_family_ipv6.redistribute.isis.include_leaked") | Boolean |  |  |  | Include leaked routes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ospfv3</samp>](## "router_ospfv3.vrfs.[].address_family_ipv6.redistribute.ospfv3") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_ospfv3.vrfs.[].address_family_ipv6.redistribute.ospfv3.enabled") | Boolean |  |  |  | Redistribute all OSPFv3 leaked routes.<br>Mutually exclusive with match_internal. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_ospfv3.vrfs.[].address_family_ipv6.redistribute.ospfv3.route_map") | String |  |  |  | Specify route map to use. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_internal</samp>](## "router_ospfv3.vrfs.[].address_family_ipv6.redistribute.ospfv3.match_internal") | Dictionary |  |  |  | Redistribute only internal OSPFv3 leaked routes.<br>Mutually exclusive with `enabled`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_ospfv3.vrfs.[].address_family_ipv6.redistribute.ospfv3.match_internal.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_ospfv3.vrfs.[].address_family_ipv6.redistribute.ospfv3.match_internal.route_map") | String |  |  |  | Specify route map to use. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_external</samp>](## "router_ospfv3.vrfs.[].address_family_ipv6.redistribute.ospfv3.match_external") | Dictionary |  |  |  | Redistribute external OSPFv3 leaked routes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_ospfv3.vrfs.[].address_family_ipv6.redistribute.ospfv3.match_external.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_ospfv3.vrfs.[].address_family_ipv6.redistribute.ospfv3.match_external.route_map") | String |  |  |  | Specify route map to use. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_nssa_external</samp>](## "router_ospfv3.vrfs.[].address_family_ipv6.redistribute.ospfv3.match_nssa_external") | Dictionary |  |  |  | Redistribute NSSA external OSPFv3 leaked routes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_ospfv3.vrfs.[].address_family_ipv6.redistribute.ospfv3.match_nssa_external.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_ospfv3.vrfs.[].address_family_ipv6.redistribute.ospfv3.match_nssa_external.route_map") | String |  |  |  | Specify route map to use. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dhcp</samp>](## "router_ospfv3.vrfs.[].address_family_ipv6.redistribute.dhcp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_ospfv3.vrfs.[].address_family_ipv6.redistribute.dhcp.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_ospfv3.vrfs.[].address_family_ipv6.redistribute.dhcp.route_map") | String |  |  |  | Specify route map to use. |

=== "YAML"

    ```yaml
    router_ospfv3:

      # IPv4 Address.
      router_id: <str>

      # Set all interfaces to passive by default.
      passive_interface_default: <bool>

      # Reference bandwidth in Mbps.
      auto_cost_reference_bandwidth: <int; 1-4294967>

      # Address family IPv4 configuration.
      # Common configurations defined at the router-level and address-family level are mutually exclusive.
      # If both are provided, the address-family level configuration takes precedence.
      address_family_ipv4:

        # Activate the address family.
        enabled: <bool; required>

        # IPv4 Address.
        router_id: <str>

        # Set all interfaces to passive by default.
        passive_interface_default: <bool>

        # Reference bandwidth in Mbps.
        auto_cost_reference_bandwidth: <int; 1-4294967>

        # Redistribute routes with OSPFv3.
        redistribute:
          bgp:
            enabled: <bool; required>

            # Specify route map to use.
            route_map: <str>

            # Include leaked routes.
            include_leaked: <bool>
          connected:
            enabled: <bool; required>

            # Specify route map to use.
            route_map: <str>

            # Include leaked routes.
            include_leaked: <bool>
          static:
            enabled: <bool; required>

            # Specify route map to use.
            route_map: <str>

            # Include leaked routes.
            include_leaked: <bool>
          isis:
            enabled: <bool; required>
            level: <str; "level-1" | "level-2" | "level-1-2">

            # Specify route map to use.
            route_map: <str>

            # Include leaked routes.
            include_leaked: <bool>
          ospfv3:

            # Redistribute all OSPFv3 leaked routes.
            # Mutually exclusive with match_internal.
            enabled: <bool>

            # Specify route map to use.
            route_map: <str>

            # Redistribute only internal OSPFv3 leaked routes.
            # Mutually exclusive with `enabled`.
            match_internal:
              enabled: <bool; required>

              # Specify route map to use.
              route_map: <str>

            # Redistribute external OSPFv3 leaked routes.
            match_external:
              enabled: <bool; required>

              # Specify route map to use.
              route_map: <str>

            # Redistribute NSSA external OSPFv3 leaked routes.
            match_nssa_external:
              enabled: <bool; required>

              # Specify route map to use.
              route_map: <str>

      # Address family IPv6 configuration.
      # Common configurations defined at the router-level and address-family level are mutually exclusive.
      # If both are provided, the address-family level configuration takes precedence.
      address_family_ipv6:

        # Activate the address family.
        enabled: <bool; required>

        # IPv4 Address.
        router_id: <str>

        # Set all interfaces to passive by default.
        passive_interface_default: <bool>

        # Reference bandwidth in Mbps.
        auto_cost_reference_bandwidth: <int; 1-4294967>

        # Redistribute routes with OSPFv3.
        redistribute:
          bgp:
            enabled: <bool; required>

            # Specify route map to use.
            route_map: <str>

            # Include leaked routes.
            include_leaked: <bool>
          connected:
            enabled: <bool; required>

            # Specify route map to use.
            route_map: <str>

            # Include leaked routes.
            include_leaked: <bool>
          static:
            enabled: <bool; required>

            # Specify route map to use.
            route_map: <str>

            # Include leaked routes.
            include_leaked: <bool>
          isis:
            enabled: <bool; required>
            level: <str; "level-1" | "level-2" | "level-1-2">

            # Specify route map to use.
            route_map: <str>

            # Include leaked routes.
            include_leaked: <bool>
          ospfv3:

            # Redistribute all OSPFv3 leaked routes.
            # Mutually exclusive with match_internal.
            enabled: <bool>

            # Specify route map to use.
            route_map: <str>

            # Redistribute only internal OSPFv3 leaked routes.
            # Mutually exclusive with `enabled`.
            match_internal:
              enabled: <bool; required>

              # Specify route map to use.
              route_map: <str>

            # Redistribute external OSPFv3 leaked routes.
            match_external:
              enabled: <bool; required>

              # Specify route map to use.
              route_map: <str>

            # Redistribute NSSA external OSPFv3 leaked routes.
            match_nssa_external:
              enabled: <bool; required>

              # Specify route map to use.
              route_map: <str>
          dhcp:
            enabled: <bool; required>

            # Specify route map to use.
            route_map: <str>

      # Multiline EOS CLI rendered directly on the default VRF OSPFv3 instance.
      eos_cli: <str>
      vrfs:
        - name: <str; required; unique>

          # IPv4 Address.
          router_id: <str>

          # Set all interfaces to passive by default.
          passive_interface_default: <bool>

          # Reference bandwidth in Mbps.
          auto_cost_reference_bandwidth: <int; 1-4294967>

          # Address family IPv4 configuration.
          # Common configurations defined at the router-level and address-family level are mutually exclusive.
          # If both are provided, the address-family level configuration takes precedence.
          address_family_ipv4:

            # Activate the address family.
            enabled: <bool; required>

            # IPv4 Address.
            router_id: <str>

            # Set all interfaces to passive by default.
            passive_interface_default: <bool>

            # Reference bandwidth in Mbps.
            auto_cost_reference_bandwidth: <int; 1-4294967>

            # Redistribute routes with OSPFv3.
            redistribute:
              bgp:
                enabled: <bool; required>

                # Specify route map to use.
                route_map: <str>

                # Include leaked routes.
                include_leaked: <bool>
              connected:
                enabled: <bool; required>

                # Specify route map to use.
                route_map: <str>

                # Include leaked routes.
                include_leaked: <bool>
              static:
                enabled: <bool; required>

                # Specify route map to use.
                route_map: <str>

                # Include leaked routes.
                include_leaked: <bool>
              isis:
                enabled: <bool; required>
                level: <str; "level-1" | "level-2" | "level-1-2">

                # Specify route map to use.
                route_map: <str>

                # Include leaked routes.
                include_leaked: <bool>
              ospfv3:

                # Redistribute all OSPFv3 leaked routes.
                # Mutually exclusive with match_internal.
                enabled: <bool>

                # Specify route map to use.
                route_map: <str>

                # Redistribute only internal OSPFv3 leaked routes.
                # Mutually exclusive with `enabled`.
                match_internal:
                  enabled: <bool; required>

                  # Specify route map to use.
                  route_map: <str>

                # Redistribute external OSPFv3 leaked routes.
                match_external:
                  enabled: <bool; required>

                  # Specify route map to use.
                  route_map: <str>

                # Redistribute NSSA external OSPFv3 leaked routes.
                match_nssa_external:
                  enabled: <bool; required>

                  # Specify route map to use.
                  route_map: <str>

          # Address family IPv6 configuration.
          # Common configurations defined at the router-level and address-family level are mutually exclusive.
          # If both are provided, the address-family level configuration takes precedence.
          address_family_ipv6:

            # Activate the address family.
            enabled: <bool; required>

            # IPv4 Address.
            router_id: <str>

            # Set all interfaces to passive by default.
            passive_interface_default: <bool>

            # Reference bandwidth in Mbps.
            auto_cost_reference_bandwidth: <int; 1-4294967>

            # Redistribute routes with OSPFv3.
            redistribute:
              bgp:
                enabled: <bool; required>

                # Specify route map to use.
                route_map: <str>

                # Include leaked routes.
                include_leaked: <bool>
              connected:
                enabled: <bool; required>

                # Specify route map to use.
                route_map: <str>

                # Include leaked routes.
                include_leaked: <bool>
              static:
                enabled: <bool; required>

                # Specify route map to use.
                route_map: <str>

                # Include leaked routes.
                include_leaked: <bool>
              isis:
                enabled: <bool; required>
                level: <str; "level-1" | "level-2" | "level-1-2">

                # Specify route map to use.
                route_map: <str>

                # Include leaked routes.
                include_leaked: <bool>
              ospfv3:

                # Redistribute all OSPFv3 leaked routes.
                # Mutually exclusive with match_internal.
                enabled: <bool>

                # Specify route map to use.
                route_map: <str>

                # Redistribute only internal OSPFv3 leaked routes.
                # Mutually exclusive with `enabled`.
                match_internal:
                  enabled: <bool; required>

                  # Specify route map to use.
                  route_map: <str>

                # Redistribute external OSPFv3 leaked routes.
                match_external:
                  enabled: <bool; required>

                  # Specify route map to use.
                  route_map: <str>

                # Redistribute NSSA external OSPFv3 leaked routes.
                match_nssa_external:
                  enabled: <bool; required>

                  # Specify route map to use.
                  route_map: <str>
              dhcp:
                enabled: <bool; required>

                # Specify route map to use.
                route_map: <str>
    ```
