<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>tunnel_interfaces</samp>](## "tunnel_interfaces") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "tunnel_interfaces.[].name") | String | Required, Unique |  |  | Tunnel Interface Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "tunnel_interfaces.[].description") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "tunnel_interfaces.[].shutdown") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp>](## "tunnel_interfaces.[].mtu") | Integer |  |  | Min: 68<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "tunnel_interfaces.[].vrf") | String |  |  |  | VRF Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;underlay_vrf</samp>](## "tunnel_interfaces.[].underlay_vrf") | String |  |  |  | Underlay VRF Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "tunnel_interfaces.[].ip_address") | String |  |  | Format: ipv4_cidr | IPv4_address/Mask. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_enable</samp>](## "tunnel_interfaces.[].ipv6_enable") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address</samp>](## "tunnel_interfaces.[].ipv6_address") <span style="color:red">deprecated</span> | String |  |  | Format: ipv6_cidr | IPv6_address/Mask.<span style="color:red">This key is deprecated. Support will be removed in AVD version 7.0.0. Use <samp>ipv6_addresses</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_addresses</samp>](## "tunnel_interfaces.[].ipv6_addresses") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "tunnel_interfaces.[].ipv6_addresses.[]") | String |  |  |  | IPv6 address with prefix length.<br>This option is mutually exclusive with `ipv6_address_auto_config` and takes precedence if both are defined. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address_auto_config</samp>](## "tunnel_interfaces.[].ipv6_address_auto_config") | Boolean |  |  |  | Use SLAAC to automatically configure the IPv6 address.<br>This option is mutually exclusive with `ipv6_addresses`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_nd</samp>](## "tunnel_interfaces.[].ipv6_nd") | Dictionary |  |  |  | IPv6 Neighbor Discovery protocol. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cache</samp>](## "tunnel_interfaces.[].ipv6_nd.cache") | Dictionary |  |  |  | Neighbor cache options. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dynamic_capacity</samp>](## "tunnel_interfaces.[].ipv6_nd.cache.dynamic_capacity") | Integer |  |  | Min: 0<br>Max: 4294967295 | Capacity of dynamic cache entries. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expire</samp>](## "tunnel_interfaces.[].ipv6_nd.cache.expire") | Integer |  |  | Min: 1<br>Max: 65535 | Cache entries expiry in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;refresh_always</samp>](## "tunnel_interfaces.[].ipv6_nd.cache.refresh_always") | Boolean |  |  |  | Force refresh on cache expiry. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ra</samp>](## "tunnel_interfaces.[].ipv6_nd.ra") | Dictionary |  |  |  | Router Advertisement. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;disabled</samp>](## "tunnel_interfaces.[].ipv6_nd.ra.disabled") | Boolean |  |  |  | Disable Router Advertisement messages on the interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rx_accept</samp>](## "tunnel_interfaces.[].ipv6_nd.ra.rx_accept") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default_route</samp>](## "tunnel_interfaces.[].ipv6_nd.ra.rx_accept.default_route") | Boolean |  |  |  | Accept default route from received Router Advertisements. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_preference</samp>](## "tunnel_interfaces.[].ipv6_nd.ra.rx_accept.route_preference") | Boolean |  |  |  | Accept route preference from received Router Advertisements. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dns_servers</samp>](## "tunnel_interfaces.[].ipv6_nd.ra.dns_servers") | List, items: Dictionary |  |  | Min Length: 1 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;address</samp>](## "tunnel_interfaces.[].ipv6_nd.ra.dns_servers.[].address") | String | Required, Unique |  |  | IPv6 address of DNS server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lifetime</samp>](## "tunnel_interfaces.[].ipv6_nd.ra.dns_servers.[].lifetime") | Integer |  |  | Min: 0<br>Max: 4294967295 | Specifies the lifetime period for this server in seconds.<br>This value overrides lifetime value set by `dns_servers_lifetime` for this server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dns_servers_lifetime</samp>](## "tunnel_interfaces.[].ipv6_nd.ra.dns_servers_lifetime") | Integer |  |  | Min: 0<br>Max: 4294967295 | Router Advertisement DNS server lifetime value in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;managed_config_flag</samp>](## "tunnel_interfaces.[].ipv6_nd.managed_config_flag") | Boolean |  |  |  | Set the "Managed Address Configuration" (M) flag in Router Advertisements. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefixes</samp>](## "tunnel_interfaces.[].ipv6_nd.prefixes") | List, items: Dictionary |  |  |  | IPv6 prefixes to include in Router Advertisements. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;ipv6_prefix</samp>](## "tunnel_interfaces.[].ipv6_nd.prefixes.[].ipv6_prefix") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;valid_lifetime</samp>](## "tunnel_interfaces.[].ipv6_nd.prefixes.[].valid_lifetime") | String |  |  |  | Valid lifetime in seconds '<0-4294967295>' or 'infinite'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;preferred_lifetime</samp>](## "tunnel_interfaces.[].ipv6_nd.prefixes.[].preferred_lifetime") | String |  |  |  | Preferred lifetime in seconds '<0-4294967295>' or 'infinite'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;no_autoconfig_flag</samp>](## "tunnel_interfaces.[].ipv6_nd.prefixes.[].no_autoconfig_flag") | Boolean |  |  |  | Indicate that the prefix cannot be used for stateless address autoconfiguration (SLAAC). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;other_config_flag</samp>](## "tunnel_interfaces.[].ipv6_nd.other_config_flag") | Boolean |  |  |  | Set the "Other Stateful Configuration" (O) flag in Router Advertisements. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;access_group_in</samp>](## "tunnel_interfaces.[].access_group_in") | String |  |  |  | IPv4 ACL Name for ingress. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;access_group_out</samp>](## "tunnel_interfaces.[].access_group_out") | String |  |  |  | IPv4 ACL Name for egress. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_access_group_in</samp>](## "tunnel_interfaces.[].ipv6_access_group_in") | String |  |  |  | IPv6 ACL Name for ingress. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_access_group_out</samp>](## "tunnel_interfaces.[].ipv6_access_group_out") | String |  |  |  | IPv6 ACL Name for egress. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;tcp_mss_ceiling</samp>](## "tunnel_interfaces.[].tcp_mss_ceiling") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp>](## "tunnel_interfaces.[].tcp_mss_ceiling.ipv4") | Integer |  |  | Min: 64<br>Max: 65495 | Segment Size for IPv4. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6</samp>](## "tunnel_interfaces.[].tcp_mss_ceiling.ipv6") | Integer |  |  | Min: 64<br>Max: 65475 | Segment Size for IPv6. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction</samp>](## "tunnel_interfaces.[].tcp_mss_ceiling.direction") | String |  |  | Valid Values:<br>- <code>ingress</code><br>- <code>egress</code> | Optional direction ('ingress', 'egress')  for tcp mss ceiling.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;tunnel_mode</samp>](## "tunnel_interfaces.[].tunnel_mode") | String |  |  | Valid Values:<br>- <code>gre</code><br>- <code>ipsec</code> | Tunnel encapsulation method.<br>`gre`: Generic route encapsulation protocol,<br>`ipsec`: IPsec-over-IP encapsulation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp>](## "tunnel_interfaces.[].source_interface") | String |  |  |  | Tunnel Source Interface Name.<br>Mutually exclusive with `source`, if both are defined `source_interface` takes precedence. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;source</samp>](## "tunnel_interfaces.[].source") | String |  |  |  | Tunnel Source IPv4/IPv6 address.<br>Mutually exclusive with `source_interface`, if both are defined `source_interface` takes precedence. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;destination</samp>](## "tunnel_interfaces.[].destination") | String |  |  |  | IPv4 or IPv6 Address Tunnel Destination. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;path_mtu_discovery</samp>](## "tunnel_interfaces.[].path_mtu_discovery") | Boolean |  |  |  | Enable Path MTU Discovery On Tunnel. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipsec_profile</samp>](## "tunnel_interfaces.[].ipsec_profile") | String |  |  |  | Used only when `tunnel_mode` is set to `ipsec`.<br>It must target a defined IPsec profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;nat_profile</samp>](## "tunnel_interfaces.[].nat_profile") | String |  |  |  | NAT interface profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mpls</samp>](## "tunnel_interfaces.[].mpls") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip</samp>](## "tunnel_interfaces.[].mpls.ip") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ldp</samp>](## "tunnel_interfaces.[].mpls.ldp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interface</samp>](## "tunnel_interfaces.[].mpls.ldp.interface") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;igp_sync</samp>](## "tunnel_interfaces.[].mpls.ldp.igp_sync") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf_network_point_to_point</samp>](## "tunnel_interfaces.[].ospf_network_point_to_point") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf_area</samp>](## "tunnel_interfaces.[].ospf_area") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf_cost</samp>](## "tunnel_interfaces.[].ospf_cost") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf_authentication</samp>](## "tunnel_interfaces.[].ospf_authentication") | String |  |  | Valid Values:<br>- <code>none</code><br>- <code>simple</code><br>- <code>message-digest</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf_authentication_key</samp>](## "tunnel_interfaces.[].ospf_authentication_key") | String |  |  |  | Encrypted password. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf_authentication_key_type</samp>](## "tunnel_interfaces.[].ospf_authentication_key_type") | String |  | `7` | Valid Values:<br>- <code>7</code><br>- <code>8a</code> | Authentication key type. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf_message_digest_keys</samp>](## "tunnel_interfaces.[].ospf_message_digest_keys") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;id</samp>](## "tunnel_interfaces.[].ospf_message_digest_keys.[].id") | Integer | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hash_algorithm</samp>](## "tunnel_interfaces.[].ospf_message_digest_keys.[].hash_algorithm") | String |  |  | Valid Values:<br>- <code>md5</code><br>- <code>sha1</code><br>- <code>sha256</code><br>- <code>sha384</code><br>- <code>sha512</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "tunnel_interfaces.[].ospf_message_digest_keys.[].key") | String |  |  |  | Encrypted password. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key_type</samp>](## "tunnel_interfaces.[].ospf_message_digest_keys.[].key_type") | String |  | `7` | Valid Values:<br>- <code>7</code><br>- <code>8a</code> | Authentication key type. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_enable</samp>](## "tunnel_interfaces.[].isis_enable") | String |  |  |  | ISIS instance. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_bfd</samp>](## "tunnel_interfaces.[].isis_bfd") | Boolean |  |  |  | Enable BFD for ISIS. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_passive</samp>](## "tunnel_interfaces.[].isis_passive") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_metric</samp>](## "tunnel_interfaces.[].isis_metric") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_network_point_to_point</samp>](## "tunnel_interfaces.[].isis_network_point_to_point") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_circuit_type</samp>](## "tunnel_interfaces.[].isis_circuit_type") | String |  |  | Valid Values:<br>- <code>level-1-2</code><br>- <code>level-1</code><br>- <code>level-2</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_hello_padding</samp>](## "tunnel_interfaces.[].isis_hello_padding") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_authentication</samp>](## "tunnel_interfaces.[].isis_authentication") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;both</samp>](## "tunnel_interfaces.[].isis_authentication.both") | Dictionary |  |  |  | Authentication settings for level-1 and level-2. 'both' takes precedence over 'level_1' and 'level_2' settings. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key_type</samp>](## "tunnel_interfaces.[].isis_authentication.both.key_type") | String |  |  | Valid Values:<br>- <code>0</code><br>- <code>7</code><br>- <code>8a</code> | Configure authentication key type. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "tunnel_interfaces.[].isis_authentication.both.key") | String |  |  |  | Password string. `key_type` is required for this setting. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key_ids</samp>](## "tunnel_interfaces.[].isis_authentication.both.key_ids") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;id</samp>](## "tunnel_interfaces.[].isis_authentication.both.key_ids.[].id") | Integer | Required, Unique |  | Min: 1<br>Max: 65535 | Configure authentication key-id. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;algorithm</samp>](## "tunnel_interfaces.[].isis_authentication.both.key_ids.[].algorithm") | String | Required |  | Valid Values:<br>- <code>sha-1</code><br>- <code>sha-224</code><br>- <code>sha-256</code><br>- <code>sha-384</code><br>- <code>sha-512</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key_type</samp>](## "tunnel_interfaces.[].isis_authentication.both.key_ids.[].key_type") | String | Required |  | Valid Values:<br>- <code>0</code><br>- <code>7</code><br>- <code>8a</code> | Configure authentication key type. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "tunnel_interfaces.[].isis_authentication.both.key_ids.[].key") | String | Required |  |  | Password string. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rfc_5310</samp>](## "tunnel_interfaces.[].isis_authentication.both.key_ids.[].rfc_5310") | Boolean |  |  |  | SHA digest computation according to rfc5310. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "tunnel_interfaces.[].isis_authentication.both.mode") | String |  |  | Valid Values:<br>- <code>md5</code><br>- <code>sha</code><br>- <code>text</code><br>- <code>shared-secret</code> | Authentication mode. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sha</samp>](## "tunnel_interfaces.[].isis_authentication.both.sha") | Dictionary |  |  |  | Required settings for authentication mode 'sha'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key_id</samp>](## "tunnel_interfaces.[].isis_authentication.both.sha.key_id") | Integer | Required |  | Min: 1<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shared_secret</samp>](## "tunnel_interfaces.[].isis_authentication.both.shared_secret") | Dictionary |  |  |  | Required settings for authentication mode 'shared_secret'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "tunnel_interfaces.[].isis_authentication.both.shared_secret.profile") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;algorithm</samp>](## "tunnel_interfaces.[].isis_authentication.both.shared_secret.algorithm") | String | Required |  | Valid Values:<br>- <code>md5</code><br>- <code>sha-1</code><br>- <code>sha-224</code><br>- <code>sha-256</code><br>- <code>sha-384</code><br>- <code>sha-512</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rx_disabled</samp>](## "tunnel_interfaces.[].isis_authentication.both.rx_disabled") | Boolean |  |  |  | Disable authentication check on the receive side. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level_1</samp>](## "tunnel_interfaces.[].isis_authentication.level_1") | Dictionary |  |  |  | Authentication settings for level-1. 'both' takes precedence over 'level_1' and 'level_2' settings. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key_type</samp>](## "tunnel_interfaces.[].isis_authentication.level_1.key_type") | String |  |  | Valid Values:<br>- <code>0</code><br>- <code>7</code><br>- <code>8a</code> | Configure authentication key type. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "tunnel_interfaces.[].isis_authentication.level_1.key") | String |  |  |  | Password string. `key_type` is required for this setting. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key_ids</samp>](## "tunnel_interfaces.[].isis_authentication.level_1.key_ids") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;id</samp>](## "tunnel_interfaces.[].isis_authentication.level_1.key_ids.[].id") | Integer | Required, Unique |  | Min: 1<br>Max: 65535 | Configure authentication key-id. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;algorithm</samp>](## "tunnel_interfaces.[].isis_authentication.level_1.key_ids.[].algorithm") | String | Required |  | Valid Values:<br>- <code>sha-1</code><br>- <code>sha-224</code><br>- <code>sha-256</code><br>- <code>sha-384</code><br>- <code>sha-512</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key_type</samp>](## "tunnel_interfaces.[].isis_authentication.level_1.key_ids.[].key_type") | String | Required |  | Valid Values:<br>- <code>0</code><br>- <code>7</code><br>- <code>8a</code> | Configure authentication key type. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "tunnel_interfaces.[].isis_authentication.level_1.key_ids.[].key") | String | Required |  |  | Password string. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rfc_5310</samp>](## "tunnel_interfaces.[].isis_authentication.level_1.key_ids.[].rfc_5310") | Boolean |  |  |  | SHA digest computation according to rfc5310. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "tunnel_interfaces.[].isis_authentication.level_1.mode") | String |  |  | Valid Values:<br>- <code>md5</code><br>- <code>sha</code><br>- <code>text</code><br>- <code>shared-secret</code> | Authentication mode. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sha</samp>](## "tunnel_interfaces.[].isis_authentication.level_1.sha") | Dictionary |  |  |  | Required settings for authentication mode 'sha'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key_id</samp>](## "tunnel_interfaces.[].isis_authentication.level_1.sha.key_id") | Integer | Required |  | Min: 1<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shared_secret</samp>](## "tunnel_interfaces.[].isis_authentication.level_1.shared_secret") | Dictionary |  |  |  | Required settings for authentication mode 'shared_secret'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "tunnel_interfaces.[].isis_authentication.level_1.shared_secret.profile") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;algorithm</samp>](## "tunnel_interfaces.[].isis_authentication.level_1.shared_secret.algorithm") | String | Required |  | Valid Values:<br>- <code>md5</code><br>- <code>sha-1</code><br>- <code>sha-224</code><br>- <code>sha-256</code><br>- <code>sha-384</code><br>- <code>sha-512</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rx_disabled</samp>](## "tunnel_interfaces.[].isis_authentication.level_1.rx_disabled") | Boolean |  |  |  | Disable authentication check on the receive side. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level_2</samp>](## "tunnel_interfaces.[].isis_authentication.level_2") | Dictionary |  |  |  | Authentication settings for level-2. 'both' takes precedence over 'level_1' and 'level_2' settings. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key_type</samp>](## "tunnel_interfaces.[].isis_authentication.level_2.key_type") | String |  |  | Valid Values:<br>- <code>0</code><br>- <code>7</code><br>- <code>8a</code> | Configure authentication key type. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "tunnel_interfaces.[].isis_authentication.level_2.key") | String |  |  |  | Password string. `key_type` is required for this setting. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key_ids</samp>](## "tunnel_interfaces.[].isis_authentication.level_2.key_ids") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;id</samp>](## "tunnel_interfaces.[].isis_authentication.level_2.key_ids.[].id") | Integer | Required, Unique |  | Min: 1<br>Max: 65535 | Configure authentication key-id. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;algorithm</samp>](## "tunnel_interfaces.[].isis_authentication.level_2.key_ids.[].algorithm") | String | Required |  | Valid Values:<br>- <code>sha-1</code><br>- <code>sha-224</code><br>- <code>sha-256</code><br>- <code>sha-384</code><br>- <code>sha-512</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key_type</samp>](## "tunnel_interfaces.[].isis_authentication.level_2.key_ids.[].key_type") | String | Required |  | Valid Values:<br>- <code>0</code><br>- <code>7</code><br>- <code>8a</code> | Configure authentication key type. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "tunnel_interfaces.[].isis_authentication.level_2.key_ids.[].key") | String | Required |  |  | Password string. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rfc_5310</samp>](## "tunnel_interfaces.[].isis_authentication.level_2.key_ids.[].rfc_5310") | Boolean |  |  |  | SHA digest computation according to rfc5310. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "tunnel_interfaces.[].isis_authentication.level_2.mode") | String |  |  | Valid Values:<br>- <code>md5</code><br>- <code>sha</code><br>- <code>text</code><br>- <code>shared-secret</code> | Authentication mode. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sha</samp>](## "tunnel_interfaces.[].isis_authentication.level_2.sha") | Dictionary |  |  |  | Required settings for authentication mode 'sha'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key_id</samp>](## "tunnel_interfaces.[].isis_authentication.level_2.sha.key_id") | Integer | Required |  | Min: 1<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shared_secret</samp>](## "tunnel_interfaces.[].isis_authentication.level_2.shared_secret") | Dictionary |  |  |  | Required settings for authentication mode 'shared_secret'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "tunnel_interfaces.[].isis_authentication.level_2.shared_secret.profile") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;algorithm</samp>](## "tunnel_interfaces.[].isis_authentication.level_2.shared_secret.algorithm") | String | Required |  | Valid Values:<br>- <code>md5</code><br>- <code>sha-1</code><br>- <code>sha-224</code><br>- <code>sha-256</code><br>- <code>sha-384</code><br>- <code>sha-512</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rx_disabled</samp>](## "tunnel_interfaces.[].isis_authentication.level_2.rx_disabled") | Boolean |  |  |  | Disable authentication check on the receive side. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;eos_cli</samp>](## "tunnel_interfaces.[].eos_cli") | String |  |  |  | Multiline String with EOS CLI rendered directly on the Tunnel interface in the final EOS configuration.<br> |

=== "YAML"

    ```yaml
    tunnel_interfaces:

        # Tunnel Interface Name.
      - name: <str; required; unique>
        description: <str>
        shutdown: <bool>
        mtu: <int; 68-65535>

        # VRF Name.
        vrf: <str>

        # Underlay VRF Name.
        underlay_vrf: <str>

        # IPv4_address/Mask.
        ip_address: <str>
        ipv6_enable: <bool>

        # IPv6_address/Mask.
        # This key is deprecated.
        # Support will be removed in AVD version 7.0.0.
        # Use `ipv6_addresses` instead.
        ipv6_address: <str>
        ipv6_addresses:

            # IPv6 address with prefix length.
            # This option is mutually exclusive with `ipv6_address_auto_config` and takes precedence if both are defined.
          - <str>

        # Use SLAAC to automatically configure the IPv6 address.
        # This option is mutually exclusive with `ipv6_addresses`.
        ipv6_address_auto_config: <bool>

        # IPv6 Neighbor Discovery protocol.
        ipv6_nd:

          # Neighbor cache options.
          cache:

            # Capacity of dynamic cache entries.
            dynamic_capacity: <int; 0-4294967295>

            # Cache entries expiry in seconds.
            expire: <int; 1-65535>

            # Force refresh on cache expiry.
            refresh_always: <bool>

          # Router Advertisement.
          ra:

            # Disable Router Advertisement messages on the interface.
            disabled: <bool>
            rx_accept:

              # Accept default route from received Router Advertisements.
              default_route: <bool>

              # Accept route preference from received Router Advertisements.
              route_preference: <bool>
            dns_servers: # >=1 items

                # IPv6 address of DNS server.
              - address: <str; required; unique>

                # Specifies the lifetime period for this server in seconds.
                # This value overrides lifetime value set by `dns_servers_lifetime` for this server.
                lifetime: <int; 0-4294967295>

            # Router Advertisement DNS server lifetime value in seconds.
            dns_servers_lifetime: <int; 0-4294967295>

          # Set the "Managed Address Configuration" (M) flag in Router Advertisements.
          managed_config_flag: <bool>

          # IPv6 prefixes to include in Router Advertisements.
          prefixes:
            - ipv6_prefix: <str; required; unique>

              # Valid lifetime in seconds '<0-4294967295>' or 'infinite'.
              valid_lifetime: <str>

              # Preferred lifetime in seconds '<0-4294967295>' or 'infinite'.
              preferred_lifetime: <str>

              # Indicate that the prefix cannot be used for stateless address autoconfiguration (SLAAC).
              no_autoconfig_flag: <bool>

          # Set the "Other Stateful Configuration" (O) flag in Router Advertisements.
          other_config_flag: <bool>

        # IPv4 ACL Name for ingress.
        access_group_in: <str>

        # IPv4 ACL Name for egress.
        access_group_out: <str>

        # IPv6 ACL Name for ingress.
        ipv6_access_group_in: <str>

        # IPv6 ACL Name for egress.
        ipv6_access_group_out: <str>
        tcp_mss_ceiling:

          # Segment Size for IPv4.
          ipv4: <int; 64-65495>

          # Segment Size for IPv6.
          ipv6: <int; 64-65475>

          # Optional direction ('ingress', 'egress')  for tcp mss ceiling.
          direction: <str; "ingress" | "egress">

        # Tunnel encapsulation method.
        # `gre`: Generic route encapsulation protocol,
        # `ipsec`: IPsec-over-IP encapsulation.
        tunnel_mode: <str; "gre" | "ipsec">

        # Tunnel Source Interface Name.
        # Mutually exclusive with `source`, if both are defined `source_interface` takes precedence.
        source_interface: <str>

        # Tunnel Source IPv4/IPv6 address.
        # Mutually exclusive with `source_interface`, if both are defined `source_interface` takes precedence.
        source: <str>

        # IPv4 or IPv6 Address Tunnel Destination.
        destination: <str>

        # Enable Path MTU Discovery On Tunnel.
        path_mtu_discovery: <bool>

        # Used only when `tunnel_mode` is set to `ipsec`.
        # It must target a defined IPsec profile.
        ipsec_profile: <str>

        # NAT interface profile.
        nat_profile: <str>
        mpls:
          ip: <bool>
          ldp:
            interface: <bool>
            igp_sync: <bool>
        ospf_network_point_to_point: <bool>
        ospf_area: <str>
        ospf_cost: <int>
        ospf_authentication: <str; "none" | "simple" | "message-digest">

        # Encrypted password.
        ospf_authentication_key: <str>

        # Authentication key type.
        ospf_authentication_key_type: <str; "7" | "8a"; default="7">
        ospf_message_digest_keys:
          - id: <int; required; unique>
            hash_algorithm: <str; "md5" | "sha1" | "sha256" | "sha384" | "sha512">

            # Encrypted password.
            key: <str>

            # Authentication key type.
            key_type: <str; "7" | "8a"; default="7">

        # ISIS instance.
        isis_enable: <str>

        # Enable BFD for ISIS.
        isis_bfd: <bool>
        isis_passive: <bool>
        isis_metric: <int>
        isis_network_point_to_point: <bool>
        isis_circuit_type: <str; "level-1-2" | "level-1" | "level-2">
        isis_hello_padding: <bool>
        isis_authentication:

          # Authentication settings for level-1 and level-2. 'both' takes precedence over 'level_1' and 'level_2' settings.
          both:

            # Configure authentication key type.
            key_type: <str; "0" | "7" | "8a">

            # Password string. `key_type` is required for this setting.
            key: <str>
            key_ids:

                # Configure authentication key-id.
              - id: <int; 1-65535; required; unique>
                algorithm: <str; "sha-1" | "sha-224" | "sha-256" | "sha-384" | "sha-512"; required>

                # Configure authentication key type.
                key_type: <str; "0" | "7" | "8a"; required>

                # Password string.
                key: <str; required>

                # SHA digest computation according to rfc5310.
                rfc_5310: <bool>

            # Authentication mode.
            mode: <str; "md5" | "sha" | "text" | "shared-secret">

            # Required settings for authentication mode 'sha'.
            sha:
              key_id: <int; 1-65535; required>

            # Required settings for authentication mode 'shared_secret'.
            shared_secret:
              profile: <str; required>
              algorithm: <str; "md5" | "sha-1" | "sha-224" | "sha-256" | "sha-384" | "sha-512"; required>

            # Disable authentication check on the receive side.
            rx_disabled: <bool>

          # Authentication settings for level-1. 'both' takes precedence over 'level_1' and 'level_2' settings.
          level_1:

            # Configure authentication key type.
            key_type: <str; "0" | "7" | "8a">

            # Password string. `key_type` is required for this setting.
            key: <str>
            key_ids:

                # Configure authentication key-id.
              - id: <int; 1-65535; required; unique>
                algorithm: <str; "sha-1" | "sha-224" | "sha-256" | "sha-384" | "sha-512"; required>

                # Configure authentication key type.
                key_type: <str; "0" | "7" | "8a"; required>

                # Password string.
                key: <str; required>

                # SHA digest computation according to rfc5310.
                rfc_5310: <bool>

            # Authentication mode.
            mode: <str; "md5" | "sha" | "text" | "shared-secret">

            # Required settings for authentication mode 'sha'.
            sha:
              key_id: <int; 1-65535; required>

            # Required settings for authentication mode 'shared_secret'.
            shared_secret:
              profile: <str; required>
              algorithm: <str; "md5" | "sha-1" | "sha-224" | "sha-256" | "sha-384" | "sha-512"; required>

            # Disable authentication check on the receive side.
            rx_disabled: <bool>

          # Authentication settings for level-2. 'both' takes precedence over 'level_1' and 'level_2' settings.
          level_2:

            # Configure authentication key type.
            key_type: <str; "0" | "7" | "8a">

            # Password string. `key_type` is required for this setting.
            key: <str>
            key_ids:

                # Configure authentication key-id.
              - id: <int; 1-65535; required; unique>
                algorithm: <str; "sha-1" | "sha-224" | "sha-256" | "sha-384" | "sha-512"; required>

                # Configure authentication key type.
                key_type: <str; "0" | "7" | "8a"; required>

                # Password string.
                key: <str; required>

                # SHA digest computation according to rfc5310.
                rfc_5310: <bool>

            # Authentication mode.
            mode: <str; "md5" | "sha" | "text" | "shared-secret">

            # Required settings for authentication mode 'sha'.
            sha:
              key_id: <int; 1-65535; required>

            # Required settings for authentication mode 'shared_secret'.
            shared_secret:
              profile: <str; required>
              algorithm: <str; "md5" | "sha-1" | "sha-224" | "sha-256" | "sha-384" | "sha-512"; required>

            # Disable authentication check on the receive side.
            rx_disabled: <bool>

        # Multiline String with EOS CLI rendered directly on the Tunnel interface in the final EOS configuration.
        eos_cli: <str>
    ```
