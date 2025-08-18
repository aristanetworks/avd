<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>&lt;network_services_keys.name&gt;</samp>](## "<network_services_keys.name>") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "<network_services_keys.name>.[].name") | String | Required, Unique |  |  | Specify a tenant name.<br>Tenant provide a construct to group L3 VRFs and L2 VLANs.<br>Networks services can be filtered by tenant name.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrfs</samp>](## "<network_services_keys.name>.[].vrfs") | List, items: Dictionary |  |  |  | VRFs will only be configured on a node if any of the underlying objects like `svis`, `l3_interfaces` or `l3_port_channels` apply to the node.<br><br>It is recommended to only define a VRF in one Tenant. If the same VRF name is used across multiple tenants and those tenants<br>are accepted by `filter.tenants` on the node, any object set under the duplicate VRFs must either be unique or be an exact match.<br><br>VRF "default" is partially supported under network-services. Currently the supported options for "default" vrf are route-target,<br>route-distinguisher settings, structured_config, raw_eos_cli in bgp and SVIs are the only supported interface type.<br>Vlan-aware-bundles are supported as well inside default vrf. OSPF is not supported currently.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<network_services_keys.name>.[].vrfs.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;l3_interfaces</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces") | List, items: Dictionary |  |  |  | List of L3 interfaces.<br>This will create IP routed interface inside VRF. Length of interfaces, nodes and ip_addresses must match.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;interfaces</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].interfaces") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].interfaces.[]") | String |  |  |  | Interface name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;encapsulation_dot1q_vlan</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].encapsulation_dot1q_vlan") | List, items: Integer |  |  |  | For sub-interfaces the dot1q vlan is derived from the interface name by default, but can also be specified. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;int&gt;</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].encapsulation_dot1q_vlan.[]") | Integer |  |  | Min: 1<br>Max: 4094 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_addresses</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].ip_addresses") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].ip_addresses.[]") | String |  |  |  | IPv4_address/Mask. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;static_routes</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].static_routes") | List, items: Dictionary |  |  |  | Static routes to be configured on every device where this interface is configured. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;prefix</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].static_routes.[].prefix") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;next_hop</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].static_routes.[].next_hop") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;track_bfd</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].static_routes.[].track_bfd") | Boolean |  |  |  | Track next-hop using BFD. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;distance</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].static_routes.[].distance") | Integer |  |  | Min: 1<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tag</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].static_routes.[].tag") | Integer |  |  | Min: 0<br>Max: 4294967295 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].static_routes.[].name") | String |  |  |  | description. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;metric</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].static_routes.[].metric") | Integer |  |  | Min: 0<br>Max: 4294967295 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interface</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].static_routes.[].interface") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_static_routes</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].ipv6_static_routes") | List, items: Dictionary |  |  |  | IPv6 static routes to be configured on every device where this interface is configured. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;prefix</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].ipv6_static_routes.[].prefix") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;next_hop</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].ipv6_static_routes.[].next_hop") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;track_bfd</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].ipv6_static_routes.[].track_bfd") | Boolean |  |  |  | Track next-hop using BFD. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;distance</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].ipv6_static_routes.[].distance") | Integer |  |  | Min: 1<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tag</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].ipv6_static_routes.[].tag") | Integer |  |  | Min: 0<br>Max: 4294967295 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].ipv6_static_routes.[].name") | String |  |  |  | description. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;metric</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].ipv6_static_routes.[].metric") | Integer |  |  | Min: 0<br>Max: 4294967295 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interface</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].ipv6_static_routes.[].interface") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].nodes") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].nodes.[]") | String |  |  |  | Node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;arp_gratuitous_accept</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].arp_gratuitous_accept") | Boolean |  |  |  | Accept gratuitous ARP. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].description") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;descriptions</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].descriptions") | List, items: String |  |  |  | "descriptions" has precedence over "description".<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].descriptions.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].enabled") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].mtu") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_acl_in</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].ipv4_acl_in") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_acl_out</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].ipv4_acl_out") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ospf</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].ospf") | Dictionary |  |  |  | OSPF interface configuration. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].ospf.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;point_to_point</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].ospf.point_to_point") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;area</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].ospf.area") | String |  | `0.0.0.0` |  | OSPF area ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cost</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].ospf.cost") | Integer |  |  |  | OSPF link cost. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;authentication</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].ospf.authentication") | String |  |  | Valid Values:<br>- <code>simple</code><br>- <code>message-digest</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;simple_auth_key</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].ospf.simple_auth_key") | String |  |  |  | Type 7 encrypted key for OSPF simple authentication.<br>Takes precedence over `cleartext_simple_auth_key`.<br>NOTE: The l3_interfaces.interfaces list must not be more than 1 interface or they must all be the same<br>(e.g. [Ethernet7, Ethernet7]) as the type7 password depends on the interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cleartext_simple_auth_key</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].ospf.cleartext_simple_auth_key") | String |  |  | Min Length: 1<br>Max Length: 8 | Cleartext key for OSPF simple authentication.<br>To protect the password at rest it is strongly recommended to make use of a vault or similar. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;message_digest_keys</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].ospf.message_digest_keys") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;id</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].ospf.message_digest_keys.[].id") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hash_algorithm</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].ospf.message_digest_keys.[].hash_algorithm") | String |  | `sha512` | Valid Values:<br>- <code>md5</code><br>- <code>sha1</code><br>- <code>sha256</code><br>- <code>sha384</code><br>- <code>sha512</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].ospf.message_digest_keys.[].key") | String |  |  |  | Type 7 encrypted key for OSPF message-digest authentication.<br>Takes precedence over `cleartext_key`<br>NOTE: The l3_interfaces.interfaces list must not be more than 1 interface or they must all be the same<br>(e.g. [Ethernet7, Ethernet7]) as the type7 password depends on the interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cleartext_key</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].ospf.message_digest_keys.[].cleartext_key") | String |  |  | Min Length: 1<br>Max Length: 16 | Cleartext key for OSPF message-digest authentication<br>To protect the password at rest it is strongly recommended to make use of a vault or similar. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pim</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].pim") | Dictionary |  |  |  | Enable PIM sparse-mode on the interface; requires "evpn_l3_multicast" to be enabled on the VRF/Tenant.<br>Enabling this implicitly makes the device a PIM External Gateway (PEG) in EVPN designs only.<br>At least one RP address must be configured for EVPN PEG to be configured.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].pim.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;flow_tracking</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].flow_tracking") | Dictionary |  |  |  | Configures flow-tracking on the interface. Overrides `fabric_flow_tracking.l3_interfaces` setting. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].flow_tracking.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].flow_tracking.name") | String |  |  |  | Flow tracker name as defined in flow_tracking_settings. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;monitor_sessions</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].monitor_sessions") | List, items: Dictionary |  |  |  | Used to define interfaces as source or destination for monitoring sessions. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].monitor_sessions.[].name") | String | Required |  |  | Session name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;role</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].monitor_sessions.[].role") | String |  |  | Valid Values:<br>- <code>source</code><br>- <code>destination</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_settings</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].monitor_sessions.[].source_settings") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].monitor_sessions.[].source_settings.direction") | String |  |  | Valid Values:<br>- <code>rx</code><br>- <code>tx</code><br>- <code>both</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_group</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].monitor_sessions.[].source_settings.access_group") | Dictionary |  |  |  | This can only be set when `session_settings.access_group` is not set. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].monitor_sessions.[].source_settings.access_group.type") | String |  |  | Valid Values:<br>- <code>ip</code><br>- <code>ipv6</code><br>- <code>mac</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].monitor_sessions.[].source_settings.access_group.name") | String |  |  |  | ACL name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].monitor_sessions.[].source_settings.access_group.priority") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;session_settings</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].monitor_sessions.[].session_settings") | Dictionary |  |  |  | Session settings are defined per session name.<br>Different session_settings for the same session name will be combined/merged.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;encapsulation_gre_metadata_tx</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].monitor_sessions.[].session_settings.encapsulation_gre_metadata_tx") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;header_remove_size</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].monitor_sessions.[].session_settings.header_remove_size") | Integer |  |  |  | Number of bytes to remove from header. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_group</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].monitor_sessions.[].session_settings.access_group") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].monitor_sessions.[].session_settings.access_group.type") | String |  |  | Valid Values:<br>- <code>ip</code><br>- <code>ipv6</code><br>- <code>mac</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].monitor_sessions.[].session_settings.access_group.name") | String |  |  |  | ACL name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rate_limit_per_ingress_chip</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].monitor_sessions.[].session_settings.rate_limit_per_ingress_chip") | String |  |  |  | Ratelimit and unit as string.<br>Examples:<br>  "100000 bps"<br>  "100 kbps"<br>  "10 mbps"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rate_limit_per_egress_chip</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].monitor_sessions.[].session_settings.rate_limit_per_egress_chip") | String |  |  |  | Ratelimit and unit as string.<br>Examples:<br>  "100000 bps"<br>  "100 kbps"<br>  "10 mbps"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sample</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].monitor_sessions.[].session_settings.sample") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;truncate</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].monitor_sessions.[].session_settings.truncate") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].monitor_sessions.[].session_settings.truncate.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;size</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].monitor_sessions.[].session_settings.truncate.size") | Integer |  |  |  | Size in bytes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;campus_link_type</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].campus_link_type") | List, items: String |  |  |  | PREVIEW: This option is marked as "preview", meaning the data models or generated configuration can change at any time.<br>Values for the CloudVision `Link-Type` user tags to be associated with an interface.<br>Attempting to associate `Link-Type` user tags with an Ethernet sub-interface will result in the same tags being associated with the parent Ethernet interface instead.<br>Attempting to associate `Link-Type` user tags with a Port-Channel interface will result in the same tags being associated with the member Ethernet interfaces instead. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].campus_link_type.[]") | String |  |  | Valid Values:<br>- <code>downlink</code><br>- <code>egress</code><br>- <code>fabric</code><br>- <code>mlag</code><br>- <code>uplink</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].structured_config") | Dictionary |  |  |  | Custom structured config added under ethernet_interfaces.[name=<interface>] for eos_cli_config_gen. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the Ethernet interface in the final EOS configuration.<br> |

=== "YAML"

    ```yaml
    <network_services_keys.name>:

        # Specify a tenant name.
        # Tenant provide a construct to group L3 VRFs and L2 VLANs.
        # Networks services can be filtered by tenant name.
      - name: <str; required; unique>

        # VRFs will only be configured on a node if any of the underlying objects like `svis`, `l3_interfaces` or `l3_port_channels` apply to the node.
        #
        # It is recommended to only define a VRF in one Tenant. If the same VRF name is used across multiple tenants and those tenants
        # are accepted by `filter.tenants` on the node, any object set under the duplicate VRFs must either be unique or be an exact match.
        #
        # VRF "default" is partially supported under network-services. Currently the supported options for "default" vrf are route-target,
        # route-distinguisher settings, structured_config, raw_eos_cli in bgp and SVIs are the only supported interface type.
        # Vlan-aware-bundles are supported as well inside default vrf. OSPF is not supported currently.
        vrfs:
          - name: <str; required; unique>

            # List of L3 interfaces.
            # This will create IP routed interface inside VRF. Length of interfaces, nodes and ip_addresses must match.
            l3_interfaces:
              - interfaces:

                    # Interface name.
                  - <str>

                # For sub-interfaces the dot1q vlan is derived from the interface name by default, but can also be specified.
                encapsulation_dot1q_vlan:
                  - <int; 1-4094>
                ip_addresses:

                    # IPv4_address/Mask.
                  - <str>

                # Static routes to be configured on every device where this interface is configured.
                static_routes:
                  - prefix: <str>
                    next_hop: <str>

                    # Track next-hop using BFD.
                    track_bfd: <bool>
                    distance: <int; 1-255>
                    tag: <int; 0-4294967295>

                    # description.
                    name: <str>
                    metric: <int; 0-4294967295>
                    interface: <str>

                # IPv6 static routes to be configured on every device where this interface is configured.
                ipv6_static_routes:
                  - prefix: <str>
                    next_hop: <str>

                    # Track next-hop using BFD.
                    track_bfd: <bool>
                    distance: <int; 1-255>
                    tag: <int; 0-4294967295>

                    # description.
                    name: <str>
                    metric: <int; 0-4294967295>
                    interface: <str>
                nodes:

                    # Node.
                  - <str>

                # Accept gratuitous ARP.
                arp_gratuitous_accept: <bool>
                description: <str>

                # "descriptions" has precedence over "description".
                descriptions:
                  - <str>
                enabled: <bool; default=True>
                mtu: <int>
                ipv4_acl_in: <str>
                ipv4_acl_out: <str>

                # OSPF interface configuration.
                ospf:
                  enabled: <bool>
                  point_to_point: <bool; default=False>

                  # OSPF area ID.
                  area: <str; default="0.0.0.0">

                  # OSPF link cost.
                  cost: <int>
                  authentication: <str; "simple" | "message-digest">

                  # Type 7 encrypted key for OSPF simple authentication.
                  # Takes precedence over `cleartext_simple_auth_key`.
                  # NOTE: The l3_interfaces.interfaces list must not be more than 1 interface or they must all be the same
                  # (e.g. [Ethernet7, Ethernet7]) as the type7 password depends on the interface.
                  simple_auth_key: <str>

                  # Cleartext key for OSPF simple authentication.
                  # To protect the password at rest it is strongly recommended to make use of a vault or similar.
                  cleartext_simple_auth_key: <str; length 1-8>
                  message_digest_keys:
                    - id: <int>
                      hash_algorithm: <str; "md5" | "sha1" | "sha256" | "sha384" | "sha512"; default="sha512">

                      # Type 7 encrypted key for OSPF message-digest authentication.
                      # Takes precedence over `cleartext_key`
                      # NOTE: The l3_interfaces.interfaces list must not be more than 1 interface or they must all be the same
                      # (e.g. [Ethernet7, Ethernet7]) as the type7 password depends on the interface.
                      key: <str>

                      # Cleartext key for OSPF message-digest authentication
                      # To protect the password at rest it is strongly recommended to make use of a vault or similar.
                      cleartext_key: <str; length 1-16>

                # Enable PIM sparse-mode on the interface; requires "evpn_l3_multicast" to be enabled on the VRF/Tenant.
                # Enabling this implicitly makes the device a PIM External Gateway (PEG) in EVPN designs only.
                # At least one RP address must be configured for EVPN PEG to be configured.
                pim:
                  enabled: <bool>

                # Configures flow-tracking on the interface. Overrides `fabric_flow_tracking.l3_interfaces` setting.
                flow_tracking:
                  enabled: <bool>

                  # Flow tracker name as defined in flow_tracking_settings.
                  name: <str>

                # Used to define interfaces as source or destination for monitoring sessions.
                monitor_sessions:

                    # Session name.
                  - name: <str; required>
                    role: <str; "source" | "destination">
                    source_settings:
                      direction: <str; "rx" | "tx" | "both">

                      # This can only be set when `session_settings.access_group` is not set.
                      access_group:
                        type: <str; "ip" | "ipv6" | "mac">

                        # ACL name.
                        name: <str>
                        priority: <int>

                    # Session settings are defined per session name.
                    # Different session_settings for the same session name will be combined/merged.
                    session_settings:
                      encapsulation_gre_metadata_tx: <bool>

                      # Number of bytes to remove from header.
                      header_remove_size: <int>
                      access_group:
                        type: <str; "ip" | "ipv6" | "mac">

                        # ACL name.
                        name: <str>

                      # Ratelimit and unit as string.
                      # Examples:
                      #   "100000 bps"
                      #   "100 kbps"
                      #   "10 mbps"
                      rate_limit_per_ingress_chip: <str>

                      # Ratelimit and unit as string.
                      # Examples:
                      #   "100000 bps"
                      #   "100 kbps"
                      #   "10 mbps"
                      rate_limit_per_egress_chip: <str>
                      sample: <int>
                      truncate:
                        enabled: <bool>

                        # Size in bytes.
                        size: <int>

                # PREVIEW: This option is marked as "preview", meaning the data models or generated configuration can change at any time.
                # Values for the CloudVision `Link-Type` user tags to be associated with an interface.
                # Attempting to associate `Link-Type` user tags with an Ethernet sub-interface will result in the same tags being associated with the parent Ethernet interface instead.
                # Attempting to associate `Link-Type` user tags with a Port-Channel interface will result in the same tags being associated with the member Ethernet interfaces instead.
                campus_link_type:
                  - <str; "downlink" | "egress" | "fabric" | "mlag" | "uplink">

                # Custom structured config added under ethernet_interfaces.[name=<interface>] for eos_cli_config_gen.
                structured_config: <dict>

                # EOS CLI rendered directly on the Ethernet interface in the final EOS configuration.
                raw_eos_cli: <str>
    ```
