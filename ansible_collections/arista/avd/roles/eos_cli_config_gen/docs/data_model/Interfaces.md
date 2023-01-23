---
search:
  boost: 2
---

# Interfaces
## Ethernet Interfaces



=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>ethernet_interfaces</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;description</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;speed</samp> | String |  |  |  | Speed can be interface_speed or forced interface_speed or auto interface_speed |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;l2_mtu</samp> | Integer |  |  |  | "l2_mtu" should only be defined for platforms supporting the "l2 mtu" CLI<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;vlans</samp> | String |  |  |  | List of switchport vlans as string<br>For a trunk port this would be a range like "1-200,300"<br>For an access port this would be a single vlan "123"<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;native_vlan</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;native_vlan_tag</samp> | Boolean |  |  |  | If setting both native_vlan and native_vlan_tag, native_vlan_tag takes precedence |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;mode</samp> | String |  |  | Valid Values:<br>- access<br>- dot1q-tunnel<br>- trunk<br>- trunk phone |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;phone</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;trunk</samp> | String |  |  | Valid Values:<br>- tagged<br>- untagged |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan</samp> | Integer |  |  | Min: 1<br>Max: 4094 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;l2_protocol</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;encapsulation_dot1q_vlan</samp> | Integer |  |  |  | Vlan tag to configure on sub-interface |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;trunk_groups</samp> | List, items: String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;type</samp> | String |  |  | Valid Values:<br>- routed<br>- switched<br>- l3dot1q<br>- l2dot1q | l3dot1q and l2dot1q are used for sub-interfaces<br>The parent interface should be defined as routed<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;snmp_trap_link_change</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;flowcontrol</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;received</samp> | String |  |  | Valid Values:<br>- desired<br>- on<br>- off |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp> | String |  |  |  | VRF name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;flow_tracker</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sampled</samp> | String |  |  |  | Flow tracker name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;error_correction_encoding</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp> | Boolean |  | True |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;fire_code</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reed_solomon</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;link_tracking_groups</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  | Group name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction</samp> | String |  |  | Valid Values:<br>- upstream<br>- downstream |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;evpn_ethernet_segment</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;identifier</samp> | String |  |  |  | EVPN Ethernet Segment Identifier (Type 1 format) |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;redundancy</samp> | String |  |  | Valid Values:<br>- all-active<br>- single-active |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;designated_forwarder_election</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;algorithm</samp> | String |  |  | Valid Values:<br>- modulus<br>- preference |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;preference_value</samp> | Integer |  |  | Min: 0<br>Max: 65535 | Preference_value is only used when "algorithm" is "preference" |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dont_preempt</samp> | Boolean |  |  |  | Dont_preempt is only used when "algorithm" is "preference" |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hold_time</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;subsequent_hold_time</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;candidate_reachability_required</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shared_index</samp> | Integer |  |  | Min: 1<br>Max: 1024 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tunnel_flood_filter_time</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_target</samp> | String |  |  |  | EVPN Route Target for ESI with format xx:xx:xx:xx:xx:xx |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;encapsulation_dot1q_vlan</samp> | Integer |  |  |  | VLAN tag to configure on sub-interface |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;encapsulation_vlan</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;client</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dot1q</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan</samp> | Integer |  |  |  | Client VLAN ID |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;outer</samp> | Integer |  |  |  | Client Outer VLAN ID |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inner</samp> | Integer |  |  |  | Client Inner VLAN ID |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unmatched</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;network</samp> | Dictionary |  |  |  | Network encapsulations are all optional and skipped if using client unmatched |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dot1q</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan</samp> | Integer |  |  |  | Network VLAN ID |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;outer</samp> | Integer |  |  |  | Network outer VLAN ID |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inner</samp> | Integer |  |  |  | Network inner VLAN ID |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;client</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;vlan_id</samp> | Integer |  |  | Min: 1<br>Max: 4094 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp> | String |  |  |  | IPv4 address/mask |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_address_secondaries</samp> | List, items: String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_helpers</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ip_helper</samp> | String | Required, Unique |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp> | String |  |  |  | Source interface name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp> | String |  |  |  | VRF name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_enable</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address_link_local</samp> | String |  |  |  | Link local IPv6 address/mask |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_nd_ra_disabled</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_nd_managed_config_flag</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_nd_prefixes</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ipv6_prefix</samp> | String | Required, Unique |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;valid_lifetime</samp> | String |  |  |  | Infinite or lifetime in seconds |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;preferred_lifetime</samp> | String |  |  |  | Infinite or lifetime in seconds |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;no_autoconfig_flag</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;access_group_in</samp> | String |  |  |  | Access list name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;access_group_out</samp> | String |  |  |  | Access list name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_access_group_in</samp> | String |  |  |  | IPv6 access list name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_access_group_out</samp> | String |  |  |  | IPv6 access list name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;mac_access_group_in</samp> | String |  |  |  | MAC access list name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;mac_access_group_out</samp> | String |  |  |  | MAC access list name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;multicast</samp> | Dictionary |  |  |  | Boundaries can be either 1 ACL or a list of multicast IP address_range(s)/prefix but not combination of both |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;boundaries</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- boundary</samp> | String |  |  |  | ACL name or multicast IP subnet |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;out</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;static</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;boundaries</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- boundary</samp> | String |  |  |  | ACL name or multicast IP subnet |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;static</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf_network_point_to_point</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf_area</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf_cost</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf_authentication</samp> | String |  |  | Valid Values:<br>- none<br>- simple<br>- message-digest |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf_authentication_key</samp> | String |  |  |  | Encrypted password |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf_message_digest_keys</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- id</samp> | Integer | Required, Unique |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hash_algorithm</samp> | String |  |  | Valid Values:<br>- md5<br>- sha1<br>- sha256<br>- sha384<br>- sha512 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp> | String |  |  |  | Encrypted password |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;pim</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dr_priority</samp> | Integer |  |  | Min: 0<br>Max: 429467295 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sparse_mode</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;mac_security</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;channel_group</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp> | String |  |  | Valid Values:<br>- on<br>- active<br>- passive |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_enable</samp> | String |  |  |  | ISIS instance |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_passive</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_metric</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_network_point_to_point</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_circuit_type</samp> | String |  |  | Valid Values:<br>- level-1-2<br>- level-1<br>- level-2 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_hello_padding</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_authentication_mode</samp> | String |  |  | Valid Values:<br>- text<br>- md5 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_authentication_key</samp> | String |  |  |  | Type-7 encrypted password |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ptp</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;announce</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timeout</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;delay_req</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;delay_mechanism</samp> | String |  |  | Valid Values:<br>- e2e<br>- p2p |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sync_message</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;role</samp> | String |  |  | Valid Values:<br>- master<br>- dynamic |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan</samp> | String |  |  |  | VLAN can be 'all' or list of vlans as string |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;transport</samp> | String |  |  | Valid Values:<br>- ipv4<br>- ipv6<br>- layer2 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;profile</samp> | String |  |  |  | Interface profile |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;storm_control</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;all</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp> | Integer |  |  |  | Configure maximum storm-control level |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp> | String |  | percent | Valid Values:<br>- percent<br>- pps | Optional field and is hardware dependant |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;broadcast</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp> | Integer |  |  |  | Configure maximum storm-control level |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp> | String |  | percent | Valid Values:<br>- percent<br>- pps | Optional field and is hardware dependant |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multicast</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp> | Integer |  |  |  | Configure maximum storm-control level |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp> | String |  | percent | Valid Values:<br>- percent<br>- pps | Optional field and is hardware dependant |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unknown_unicast</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp> | Integer |  |  |  | Configure maximum storm-control level |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp> | String |  | percent | Valid Values:<br>- percent<br>- pps | Optional field and is hardware dependant |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;logging</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;event</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;link_status</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;congestion_drops</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;lldp</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;transmit</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;receive</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ztp_vlan</samp> | Integer |  |  |  | ZTP vlan number |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;trunk_private_vlan_secondary</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;pvlan_mapping</samp> | String |  |  |  | List of vlans as string |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;vlan_translations</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- from</samp> | String |  |  |  | List of vlans as string (only one vlan if direction is "both") |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;to</samp> | Integer |  |  |  | VLAN ID |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction</samp> | String |  | both | Valid Values:<br>- in<br>- out<br>- both |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;dot1x</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port_control</samp> | String |  |  | Valid Values:<br>- auto<br>- force-authorized<br>- force-unauthorized |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port_control_force_authorized_phone</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reauthentication</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pae</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp> | String |  |  | Valid Values:<br>- authenticator |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;authentication_failure</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp> | String |  |  | Valid Values:<br>- allow<br>- drop |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;allow_vlan</samp> | Integer |  |  | Min: 1<br>Max: 4094 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;host_mode</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp> | String |  |  | Valid Values:<br>- multi-host<br>- single-host |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multi_host_authenticated</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mac_based_authentication</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;host_mode_common</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timeout</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;idle_host</samp> | Integer |  |  | Min: 10<br>Max: 65535 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;quiet_period</samp> | Integer |  |  | Min: 1<br>Max: 65535 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reauth_period</samp> | String |  |  |  | Value can be 60-4294967295 or 'server' |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reauth_timeout_ignore</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tx_period</samp> | Integer |  |  | Min: 1<br>Max: 65535 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reauthorization_request_limit</samp> | Integer |  |  | Min: 1<br>Max: 10 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;service_profile</samp> | String |  |  |  | QOS profile |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;shape</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rate</samp> | String |  |  |  | Rate in kbps, pps or percent<br>Supported options are platform dependent<br>Examples:<br>- "5000 kbps"<br>- "1000 pps"<br>- "20 percent"<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;qos</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;trust</samp> | String |  |  | Valid Values:<br>- dscp<br>- cos<br>- disabled |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dscp</samp> | Integer |  |  |  | DSCP value |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cos</samp> | Integer |  |  |  | COS value |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_bpdufilter</samp> | String |  |  | Valid Values:<br>- enabled<br>- disabled<br>- True<br>- False<br>- true<br>- false |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_bpduguard</samp> | String |  |  | Valid Values:<br>- enabled<br>- disabled<br>- True<br>- False<br>- true<br>- false |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_guard</samp> | String |  |  | Valid Values:<br>- loop<br>- root<br>- disabled |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_portfast</samp> | String |  |  | Valid Values:<br>- edge<br>- network |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;vmtracer</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;priority_flow_control</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priorities</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- priority</samp> | Integer | Required, Unique |  | Min: 0<br>Max: 7 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;no_drop</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;echo</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp> | Integer |  |  |  | Interval in milliseconds |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;min_rx</samp> | Integer |  |  |  | Rate in milliseconds |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multiplier</samp> | Integer |  |  | Min: 3<br>Max: 50 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;service_policy</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pbr</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;input</samp> | String |  |  |  | Policy-map name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;mpls</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ldp</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interface</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;igp_sync</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;lacp_timer</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp> | String |  |  | Valid Values:<br>- fast<br>- normal |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multiplier</samp> | Integer |  |  | Min: 3<br>Max: 3000 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;lacp_port_priority</samp> | Integer |  |  | Min: 0<br>Max: 65535 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;transceiver</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;media</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;override</samp> | String |  |  |  | Transceiver type |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_proxy_arp</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;traffic_policy</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;input</samp> | String |  |  |  | Ingress traffic policy |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;output</samp> | String |  |  |  | Egress traffic policy |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;peer</samp> | String |  |  |  | Key only used for documentation or validation purposes |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;peer_interface</samp> | String |  |  |  | Key only used for documentation or validation purposes |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;peer_type</samp> | String |  |  |  | Key only used for documentation or validation purposes |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;eos_cli</samp> | String |  |  |  | Multiline EOS CLI rendered directly on the ethernet interface in the final EOS configuration |

=== "YAML"

    ```yaml
    ethernet_interfaces:
      - name: <str>
        description: <str>
        shutdown: <bool>
        speed: <str>
        mtu: <int>
        l2_mtu: <int>
        vlans: <str>
        native_vlan: <int>
        native_vlan_tag: <bool>
        mode: <str>
        phone:
          trunk: <str>
          vlan: <int>
        l2_protocol:
          encapsulation_dot1q_vlan: <int>
        trunk_groups:
          - <str>
        type: <str>
        snmp_trap_link_change: <bool>
        flowcontrol:
          received: <str>
        vrf: <str>
        flow_tracker:
          sampled: <str>
        error_correction_encoding:
          enabled: <bool>
          fire_code: <bool>
          reed_solomon: <bool>
        link_tracking_groups:
          - name: <str>
            direction: <str>
        evpn_ethernet_segment:
          identifier: <str>
          redundancy: <str>
          designated_forwarder_election:
            algorithm: <str>
            preference_value: <int>
            dont_preempt: <bool>
            hold_time: <int>
            subsequent_hold_time: <int>
            candidate_reachability_required: <bool>
          mpls:
            shared_index: <int>
            tunnel_flood_filter_time: <int>
          route_target: <str>
        encapsulation_dot1q_vlan: <int>
        encapsulation_vlan:
          client:
            dot1q:
              vlan: <int>
              outer: <int>
              inner: <int>
            unmatched: <bool>
          network:
            dot1q:
              vlan: <int>
              outer: <int>
              inner: <int>
            client: <bool>
        vlan_id: <int>
        ip_address: <str>
        ip_address_secondaries:
          - <str>
        ip_helpers:
          - ip_helper: <str>
            source_interface: <str>
            vrf: <str>
        ipv6_enable: <bool>
        ipv6_address: <str>
        ipv6_address_link_local: <str>
        ipv6_nd_ra_disabled: <bool>
        ipv6_nd_managed_config_flag: <bool>
        ipv6_nd_prefixes:
          - ipv6_prefix: <str>
            valid_lifetime: <str>
            preferred_lifetime: <str>
            no_autoconfig_flag: <bool>
        access_group_in: <str>
        access_group_out: <str>
        ipv6_access_group_in: <str>
        ipv6_access_group_out: <str>
        mac_access_group_in: <str>
        mac_access_group_out: <str>
        multicast:
          ipv4:
            boundaries:
              - boundary: <str>
                out: <bool>
            static: <bool>
          ipv6:
            boundaries:
              - boundary: <str>
            static: <bool>
        ospf_network_point_to_point: <bool>
        ospf_area: <str>
        ospf_cost: <int>
        ospf_authentication: <str>
        ospf_authentication_key: <str>
        ospf_message_digest_keys:
          - id: <int>
            hash_algorithm: <str>
            key: <str>
        pim:
          ipv4:
            dr_priority: <int>
            sparse_mode: <bool>
        mac_security:
          profile: <str>
        channel_group:
          id: <int>
          mode: <str>
        isis_enable: <str>
        isis_passive: <bool>
        isis_metric: <int>
        isis_network_point_to_point: <bool>
        isis_circuit_type: <str>
        isis_hello_padding: <bool>
        isis_authentication_mode: <str>
        isis_authentication_key: <str>
        ptp:
          enable: <bool>
          announce:
            interval: <int>
            timeout: <int>
          delay_req: <int>
          delay_mechanism: <str>
          sync_message:
            interval: <int>
          role: <str>
          vlan: <str>
          transport: <str>
        profile: <str>
        storm_control:
          all:
            level: <int>
            unit: <str>
          broadcast:
            level: <int>
            unit: <str>
          multicast:
            level: <int>
            unit: <str>
          unknown_unicast:
            level: <int>
            unit: <str>
        logging:
          event:
            link_status: <bool>
            congestion_drops: <bool>
        lldp:
          transmit: <bool>
          receive: <bool>
          ztp_vlan: <int>
        trunk_private_vlan_secondary: <bool>
        pvlan_mapping: <str>
        vlan_translations:
          - from: <str>
            to: <int>
            direction: <str>
        dot1x:
          port_control: <str>
          port_control_force_authorized_phone: <bool>
          reauthentication: <bool>
          pae:
            mode: <str>
          authentication_failure:
            action: <str>
            allow_vlan: <int>
          host_mode:
            mode: <str>
            multi_host_authenticated: <bool>
          mac_based_authentication:
            enabled: <bool>
            always: <bool>
            host_mode_common: <bool>
          timeout:
            idle_host: <int>
            quiet_period: <int>
            reauth_period: <str>
            reauth_timeout_ignore: <bool>
            tx_period: <int>
          reauthorization_request_limit: <int>
        service_profile: <str>
        shape:
          rate: <str>
        qos:
          trust: <str>
          dscp: <int>
          cos: <int>
        spanning_tree_bpdufilter: <str>
        spanning_tree_bpduguard: <str>
        spanning_tree_guard: <str>
        spanning_tree_portfast: <str>
        vmtracer: <bool>
        priority_flow_control:
          enabled: <bool>
          priorities:
            - priority: <int>
              no_drop: <bool>
        bfd:
          echo: <bool>
          interval: <int>
          min_rx: <int>
          multiplier: <int>
        service_policy:
          pbr:
            input: <str>
        mpls:
          ip: <bool>
          ldp:
            interface: <bool>
            igp_sync: <bool>
        lacp_timer:
          mode: <str>
          multiplier: <int>
        lacp_port_priority: <int>
        transceiver:
          media:
            override: <str>
        ip_proxy_arp: <bool>
        traffic_policy:
          input: <str>
          output: <str>
        peer: <str>
        peer_interface: <str>
        peer_type: <str>
        eos_cli: <str>
    ```
## Interface Defaults



=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>interface_defaults</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;ethernet</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;mtu</samp> | Integer |  |  |  |  |

=== "YAML"

    ```yaml
    interface_defaults:
      ethernet:
        shutdown: <bool>
      mtu: <int>
    ```
## Interface Profiles



=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>interface_profiles</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  | Interface-Profile Name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;commands</samp> | List, items: String | Required |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp> | String |  |  |  | EOS CLI interface command<br>Example: "switchport mode access" |

=== "YAML"

    ```yaml
    interface_profiles:
      - name: <str>
        commands:
          - <str>
    ```
## Loopback Interfaces



=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>loopback_interfaces</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  | Loopback interface name e.g. "Loopback0" |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;description</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp> | String |  |  |  | VRF name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp> | String |  |  |  | IPv4_address/Mask |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_address_secondaries</samp> | List, items: String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp> | String |  |  |  | IPv4_address/Mask |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_enable</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address</samp> | String |  |  |  | IPv6_address/Mask |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_proxy_arp</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf_area</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;mpls</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ldp</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interface</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_enable</samp> | String |  |  |  | ISIS instance name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_passive</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_metric</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_network_point_to_point</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;node_segment</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_index</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_index</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;eos_cli</samp> | String |  |  |  | EOS CLI rendered directly on the loopback interface in the final EOS configuration |

=== "YAML"

    ```yaml
    loopback_interfaces:
      - name: <str>
        description: <str>
        shutdown: <bool>
        vrf: <str>
        ip_address: <str>
        ip_address_secondaries:
          - <str>
        ipv6_enable: <bool>
        ipv6_address: <str>
        ip_proxy_arp: <bool>
        ospf_area: <str>
        mpls:
          ldp:
            interface: <bool>
        isis_enable: <str>
        isis_passive: <bool>
        isis_metric: <int>
        isis_network_point_to_point: <bool>
        node_segment:
          ipv4_index: <int>
          ipv6_index: <int>
        eos_cli: <str>
    ```
## Port Channel Interfaces



=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>port_channel_interfaces</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;description</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;logging</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;event</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;link_status</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;l2_mtu</samp> | Integer |  |  |  | "l2_mtu" should only be defined for platforms supporting the "l2 mtu" CLI<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;vlans</samp> | String |  |  |  | List of switchport vlans as string<br>For a trunk port this would be a range like "1-200,300"<br>For an access port this would be a single vlan "123"<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;snmp_trap_link_change</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;type</samp> | String |  |  | Valid Values:<br>- routed<br>- switched<br>- l3dot1q<br>- l2dot1q | l3dot1q and l2dot1q are used for sub-interfaces<br>The parent interface should be defined as routed<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;encapsulation_dot1q_vlan</samp> | Integer |  |  |  | VLAN tag to configure on sub-interface |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp> | String |  |  |  | VRF name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;encapsulation_vlan</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;client</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dot1q</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan</samp> | Integer |  |  |  | Client VLAN ID |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;outer</samp> | Integer |  |  |  | Client Outer VLAN ID |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inner</samp> | Integer |  |  |  | Client Inner VLAN ID |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unmatched</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;network</samp> | Dictionary |  |  |  | Network encapsulation are all optional, and skipped if using client unmatched |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dot1q</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan</samp> | Integer |  |  |  | Network VLAN ID |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;outer</samp> | Integer |  |  |  | Network Outer VLAN ID |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inner</samp> | Integer |  |  |  | Network Inner VLAN ID |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;client</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;vlan_id</samp> | Integer |  |  | Min: 1<br>Max: 4094 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;mode</samp> | String |  |  | Valid Values:<br>- access<br>- dot1q-tunnel<br>- trunk<br>- trunk phone |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;native_vlan</samp> | Integer |  |  |  | If setting both native_vlan and native_vlan_tag, native_vlan_tag takes precedence |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;native_vlan_tag</samp> | Boolean |  | False |  | If setting both native_vlan and native_vlan_tag, native_vlan_tag takes precedence |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;link_tracking_groups</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  | Group name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction</samp> | String |  |  | Valid Values:<br>- upstream<br>- downstream |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;phone</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;trunk</samp> | String |  |  | Valid Values:<br>- tagged<br>- untagged |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan</samp> | Integer |  |  | Min: 1<br>Max: 4094 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;l2_protocol</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;encapsulation_dot1q_vlan</samp> | Integer |  |  |  | Vlan tag to configure on sub-interface |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag</samp> | Integer |  |  | Min: 1<br>Max: 2000 | MLAG ID |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;trunk_groups</samp> | List, items: String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;lacp_fallback_timeout</samp> | Integer |  | 90 | Min: 0<br>Max: 300 | Timeout in seconds |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;lacp_fallback_mode</samp> | String |  |  | Valid Values:<br>- individual<br>- static |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;qos</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;trust</samp> | String |  |  | Valid Values:<br>- dscp<br>- cos<br>- disabled |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dscp</samp> | Integer |  |  |  | DSCP value |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cos</samp> | Integer |  |  |  | COS value |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;echo</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp> | Integer |  |  |  | Interval in milliseconds |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;min_rx</samp> | Integer |  |  |  | Rate in milliseconds |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multiplier</samp> | Integer |  |  | Min: 3<br>Max: 50 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;service_policy</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pbr</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;input</samp> | String |  |  |  | Policy-map name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;mpls</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ldp</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interface</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;igp_sync</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;trunk_private_vlan_secondary</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;pvlan_mapping</samp> | String |  |  |  | List of vlans as string |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;vlan_translations</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- from</samp> | String |  |  |  | List of vlans as string (only one vlan if direction is "both") |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;to</samp> | Integer |  |  |  | VLAN ID |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction</samp> | String |  | both | Valid Values:<br>- in<br>- out<br>- both |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;shape</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rate</samp> | String |  |  |  | Rate in kbps, pps or percent<br>Supported options are platform dependent<br>Examples:<br>- "5000 kbps"<br>- "1000 pps"<br>- "20 percent"<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;storm_control</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;all</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp> | Integer |  |  |  | Configure maximum storm-control level |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp> | String |  | percent | Valid Values:<br>- percent<br>- pps | Optional field and is hardware dependant |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;broadcast</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp> | Integer |  |  |  | Configure maximum storm-control level |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp> | String |  | percent | Valid Values:<br>- percent<br>- pps | Optional field and is hardware dependant |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multicast</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp> | Integer |  |  |  | Configure maximum storm-control level |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp> | String |  | percent | Valid Values:<br>- percent<br>- pps | Optional field and is hardware dependant |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unknown_unicast</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp> | Integer |  |  |  | Configure maximum storm-control level |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp> | String |  | percent | Valid Values:<br>- percent<br>- pps | Optional field and is hardware dependant |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_proxy_arp</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_enable</samp> | String |  |  |  | ISIS instance |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_passive</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_metric</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_network_point_to_point</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_circuit_type</samp> | String |  |  | Valid Values:<br>- level-1-2<br>- level-1<br>- level-2 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_hello_padding</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_authentication_mode</samp> | String |  |  | Valid Values:<br>- text<br>- md5 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_authentication_key</samp> | String |  |  |  | Type-7 encrypted password |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;traffic_policy</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;input</samp> | String |  |  |  | Ingress traffic policy |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;output</samp> | String |  |  |  | Egress traffic policy |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;evpn_ethernet_segment</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;identifier</samp> | String |  |  |  | EVPN Ethernet Segment Identifier (Type 1 format) |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;redundancy</samp> | String |  |  | Valid Values:<br>- all-active<br>- single-active |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;designated_forwarder_election</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;algorithm</samp> | String |  |  | Valid Values:<br>- modulus<br>- preference |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;preference_value</samp> | Integer |  |  | Min: 0<br>Max: 65535 | Preference_value is only used when "algorithm" is "preference" |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dont_preempt</samp> | Boolean |  | False |  | Dont_preempt is only used when "algorithm" is "preference" |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hold_time</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;subsequent_hold_time</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;candidate_reachability_required</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shared_index</samp> | Integer |  |  | Min: 1<br>Max: 1024 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tunnel_flood_filter_time</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_target</samp> | String |  |  |  | EVPN Route Target for ESI with format xx:xx:xx:xx:xx:xx |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;esi</samp> | String |  |  |  | EVPN Ethernet Segment Identifier (Type 1 format)<br>Will be deprecated in AVD 4.0 in favor of "evpn_ethernet_segment.identifier"<br>If both "esi" and "evpn_ethernet_segment.identifier" are defined, the new variable takes precedence<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;rt</samp> | String |  |  |  | EVPN Route Target for ESI with format xx:xx:xx:xx:xx:xx<br>Will be deprecated in AVD 4.0 in favor of "evpn_ethernet_segment.route_target"<br>If both "rt" and "evpn_ethernet_segment.route_target" are defined, the new variable takes precedence<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;lacp_id</samp> | String |  |  |  | LACP ID with format xxxx.xxxx.xxxx |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_bpdufilter</samp> | String |  |  | Valid Values:<br>- enabled<br>- disabled<br>- True<br>- False<br>- true<br>- false |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_bpduguard</samp> | String |  |  | Valid Values:<br>- enabled<br>- disabled<br>- True<br>- False<br>- true<br>- false |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_guard</samp> | String |  |  | Valid Values:<br>- loop<br>- root<br>- disabled |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_portfast</samp> | String |  |  | Valid Values:<br>- edge<br>- network |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;vmtracer</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ptp</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;announce</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timeout</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;delay_req</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;delay_mechanism</samp> | String |  |  | Valid Values:<br>- e2e<br>- p2p |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sync_message</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;role</samp> | String |  |  | Valid Values:<br>- master<br>- dynamic |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan</samp> | String |  |  |  | VLAN can be 'all' or list of vlans as string |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;transport</samp> | String |  |  | Valid Values:<br>- ipv4<br>- ipv6<br>- layer2 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp> | String |  |  |  | IPv4 address/mask |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_enable</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address</samp> | String |  |  |  | IPv6 address/mask |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address_link_local</samp> | String |  |  |  | Link local IPv6 address/mask |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_nd_ra_disabled</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_nd_managed_config_flag</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_nd_prefixes</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ipv6_prefix</samp> | String | Required, Unique |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;valid_lifetime</samp> | String |  |  |  | Infinite or lifetime in seconds |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;preferred_lifetime</samp> | String |  |  |  | Infinite or lifetime in seconds |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;no_autoconfig_flag</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;access_group_in</samp> | String |  |  |  | Access list name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;access_group_out</samp> | String |  |  |  | Access list name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_access_group_in</samp> | String |  |  |  | IPv6 access list name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_access_group_out</samp> | String |  |  |  | IPv6 access list name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;mac_access_group_in</samp> | String |  |  |  | MAC access list name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;mac_access_group_out</samp> | String |  |  |  | MAC access list name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;pim</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dr_priority</samp> | Integer |  |  | Min: 0<br>Max: 429467295 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sparse_mode</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;service_profile</samp> | String |  |  |  | QOS profile |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf_network_point_to_point</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf_area</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf_cost</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf_authentication</samp> | String |  |  | Valid Values:<br>- none<br>- simple<br>- message-digest |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf_authentication_key</samp> | String |  |  |  | Encrypted password |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf_message_digest_keys</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- id</samp> | Integer | Required, Unique |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hash_algorithm</samp> | String |  |  | Valid Values:<br>- md5<br>- sha1<br>- sha256<br>- sha384<br>- sha512 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp> | String |  |  |  | Encrypted password |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;flow_tracker</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sampled</samp> | String |  |  |  | Flow tracker name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;peer</samp> | String |  |  |  | Key only used for documentation or validation purposes |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;peer_interface</samp> | String |  |  |  | Key only used for documentation or validation purposes |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;peer_type</samp> | String |  |  |  | Key only used for documentation or validation purposes |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;eos_cli</samp> | String |  |  |  | Multiline EOS CLI rendered directly on the port-channel interface in the final EOS configuration |

=== "YAML"

    ```yaml
    port_channel_interfaces:
      - name: <str>
        description: <str>
        logging:
          event:
            link_status: <bool>
        shutdown: <bool>
        l2_mtu: <int>
        vlans: <str>
        snmp_trap_link_change: <bool>
        type: <str>
        encapsulation_dot1q_vlan: <int>
        vrf: <str>
        encapsulation_vlan:
          client:
            dot1q:
              vlan: <int>
              outer: <int>
              inner: <int>
            unmatched: <bool>
          network:
            dot1q:
              vlan: <int>
              outer: <int>
              inner: <int>
            client: <bool>
        vlan_id: <int>
        mode: <str>
        native_vlan: <int>
        native_vlan_tag: <bool>
        link_tracking_groups:
          - name: <str>
            direction: <str>
        phone:
          trunk: <str>
          vlan: <int>
        l2_protocol:
          encapsulation_dot1q_vlan: <int>
        mtu: <int>
        mlag: <int>
        trunk_groups:
          - <str>
        lacp_fallback_timeout: <int>
        lacp_fallback_mode: <str>
        qos:
          trust: <str>
          dscp: <int>
          cos: <int>
        bfd:
          echo: <bool>
          interval: <int>
          min_rx: <int>
          multiplier: <int>
        service_policy:
          pbr:
            input: <str>
        mpls:
          ip: <bool>
          ldp:
            interface: <bool>
            igp_sync: <bool>
        trunk_private_vlan_secondary: <bool>
        pvlan_mapping: <str>
        vlan_translations:
          - from: <str>
            to: <int>
            direction: <str>
        shape:
          rate: <str>
        storm_control:
          all:
            level: <int>
            unit: <str>
          broadcast:
            level: <int>
            unit: <str>
          multicast:
            level: <int>
            unit: <str>
          unknown_unicast:
            level: <int>
            unit: <str>
        ip_proxy_arp: <bool>
        isis_enable: <str>
        isis_passive: <bool>
        isis_metric: <int>
        isis_network_point_to_point: <bool>
        isis_circuit_type: <str>
        isis_hello_padding: <bool>
        isis_authentication_mode: <str>
        isis_authentication_key: <str>
        traffic_policy:
          input: <str>
          output: <str>
        evpn_ethernet_segment:
          identifier: <str>
          redundancy: <str>
          designated_forwarder_election:
            algorithm: <str>
            preference_value: <int>
            dont_preempt: <bool>
            hold_time: <int>
            subsequent_hold_time: <int>
            candidate_reachability_required: <bool>
          mpls:
            shared_index: <int>
            tunnel_flood_filter_time: <int>
          route_target: <str>
        esi: <str>
        rt: <str>
        lacp_id: <str>
        spanning_tree_bpdufilter: <str>
        spanning_tree_bpduguard: <str>
        spanning_tree_guard: <str>
        spanning_tree_portfast: <str>
        vmtracer: <bool>
        ptp:
          enable: <bool>
          announce:
            interval: <int>
            timeout: <int>
          delay_req: <int>
          delay_mechanism: <str>
          sync_message:
            interval: <int>
          role: <str>
          vlan: <str>
          transport: <str>
        ip_address: <str>
        ipv6_enable: <bool>
        ipv6_address: <str>
        ipv6_address_link_local: <str>
        ipv6_nd_ra_disabled: <bool>
        ipv6_nd_managed_config_flag: <bool>
        ipv6_nd_prefixes:
          - ipv6_prefix: <str>
            valid_lifetime: <str>
            preferred_lifetime: <str>
            no_autoconfig_flag: <bool>
        access_group_in: <str>
        access_group_out: <str>
        ipv6_access_group_in: <str>
        ipv6_access_group_out: <str>
        mac_access_group_in: <str>
        mac_access_group_out: <str>
        pim:
          ipv4:
            dr_priority: <int>
            sparse_mode: <bool>
        service_profile: <str>
        ospf_network_point_to_point: <bool>
        ospf_area: <str>
        ospf_cost: <int>
        ospf_authentication: <str>
        ospf_authentication_key: <str>
        ospf_message_digest_keys:
          - id: <int>
            hash_algorithm: <str>
            key: <str>
        flow_tracker:
          sampled: <str>
        peer: <str>
        peer_interface: <str>
        peer_type: <str>
        eos_cli: <str>
    ```
## Switchport Default



=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>switchport_default</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;mode</samp> | String |  |  | Valid Values:<br>- routed<br>- access |  |
    | <samp>&nbsp;&nbsp;phone</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;cos</samp> | Integer |  |  | Min: 0<br>Max: 7 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;trunk</samp> | String |  |  | Valid Values:<br>- tagged<br>- untagged |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;vlan</samp> | Integer |  |  | Min: 1<br>Max: 4094 | VLAN ID |

=== "YAML"

    ```yaml
    switchport_default:
      mode: <str>
      phone:
        cos: <int>
        trunk: <str>
        vlan: <int>
    ```
## Tunnel Interfaces



=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>tunnel_interfaces</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  | Tunnel Interface Name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;description</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp> | Integer |  |  | Min: 68<br>Max: 65535 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp> | String |  |  |  | VRF Name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp> | String |  |  | Format: ipv4_cidr | IPv4_address/Mask |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_enable</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address</samp> | String |  |  | Format: ipv6_cidr | IPv6_address/Mask |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;access_group_in</samp> | String |  |  |  | IPv4 ACL Name for ingress |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;access_group_out</samp> | String |  |  |  | IPv4 ACL Name for egress |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_access_group_in</samp> | String |  |  |  | IPv6 ACL Name for ingress |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_access_group_out</samp> | String |  |  |  | IPv6 ACL Name for egress |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;tcp_mss_ceiling</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp> | Integer |  |  | Min: 64<br>Max: 65495 | Segment Size for IPv4 |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6</samp> | Integer |  |  | Min: 64<br>Max: 65475 | Segment Size for IPv6 |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction</samp> | String |  |  | Valid Values:<br>- ingress<br>- egress | Optional direction ('ingress', 'egress')  for tcp mss ceiling<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp> | String |  |  |  | Tunnel Source Interface Name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;destination</samp> | String |  |  |  | IPv4 or IPv6 Address Tunnel Destination |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;path_mtu_discovery</samp> | Boolean |  |  |  | Enable Path MTU Discovery On Tunnel |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;eos_cli</samp> | String |  |  |  | Multiline String with EOS CLI rendered directly on the Tunnel interface in the final EOS configuration. |

=== "YAML"

    ```yaml
    tunnel_interfaces:
      - name: <str>
        description: <str>
        shutdown: <bool>
        mtu: <int>
        vrf: <str>
        ip_address: <str>
        ipv6_enable: <bool>
        ipv6_address: <str>
        access_group_in: <str>
        access_group_out: <str>
        ipv6_access_group_in: <str>
        ipv6_access_group_out: <str>
        tcp_mss_ceiling:
          ipv4: <int>
          ipv6: <int>
          direction: <str>
        source_interface: <str>
        destination: <str>
        path_mtu_discovery: <bool>
        eos_cli: <str>
    ```
## VLAN Interfaces



=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>vlan_interfaces</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  | VLAN interface name like "Vlan123" |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;description</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp> | String |  |  |  | VRF name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;arp_aging_timeout</samp> | Integer |  |  | Min: 1<br>Max: 65535 | In seconds |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;arp_cache_dynamic_capacity</samp> | Integer |  |  | Min: 0<br>Max: 4294967295 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;arp_gratuitous_accept</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;arp_monitor_mac_address</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_proxy_arp</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_directed_broadcast</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp> | String |  |  |  | IPv4_address/Mask |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_address_secondaries</samp> | List, items: String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp> | String |  |  |  | IPv4_address/Mask |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_virtual_router_addresses</samp> | List, items: String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp> | String |  |  |  | IPv4 address or IPv4_address/Mask |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_address_virtual</samp> | String |  |  |  | IPv4_address/Mask |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_address_virtual_secondaries</samp> | List, items: String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp> | String |  |  |  | IPv4_address/Mask |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_igmp</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_helpers</samp> | List, items: Dictionary |  |  |  | List of DHCP servers |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ip_helper</samp> | String | Required, Unique |  |  | IP address or hostname of DHCP server |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp> | String |  |  |  | Interface used as source for forwarded DHCP packets |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp> | String |  |  |  | VRF where DHCP server can be reached |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_enable</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address</samp> | String |  |  |  | IPv6_address/Mask |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address_virtual</samp> | String |  |  |  | IPv6_address/Mask<br>"ipv6_address_virtual" key will be deprecated in AVD v4.0 in favor of the new "ipv6_address_virtuals"<br>If both "ipv6_address_virtual" and "ipv6_address_virtuals" are set, all addresses will be configured<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address_virtuals</samp> | List, items: String |  |  |  | The new "ipv6_address_virtuals" key support multiple virtual ipv6 addresses. |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp> | String |  |  |  | IPv6_address/Mask |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address_link_local</samp> | String |  |  |  | IPv6_address/Mask |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_virtual_router_address</samp> | String |  |  |  | "ipv6_virtual_router_address" key will be deprecated in AVD v4.0<br>This should not be mixed with the new "ipv6_virtual_router_addresses" key below to avoid conflicts.<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_virtual_router_addresses</samp> | List, items: String |  |  |  | Improved "VARPv6" data model to support multiple VARPv6 addresses. |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp> | String |  |  |  | IPv6 address or IPv6_address/Mask |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_nd_ra_disabled</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_nd_managed_config_flag</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_nd_prefixes</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ipv6_prefix</samp> | String | Required, Unique |  |  | IPv6_address/Mask |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;valid_lifetime</samp> | String |  |  |  | In seconds <0-4294967295> or infinite |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;preferred_lifetime</samp> | String |  |  |  | In seconds <0-4294967295> or infinite |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;no_autoconfig_flag</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;access_group_in</samp> | String |  |  |  | IPv4 access-list name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;access_group_out</samp> | String |  |  |  | IPv4 access-list name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_access_group_in</samp> | String |  |  |  | IPv6 access-list name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_access_group_out</samp> | String |  |  |  | IPv6 access-list name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;multicast</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;boundaries</samp> | List, items: Dictionary |  |  |  | Boundaries can be either 1 ACL or a list of multicast IP address_range(s)/prefix but not combination of both |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- boundary</samp> | String | Required, Unique |  |  | IPv4 access-list name or IPv4 multicast group prefix with mask |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;out</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_route_export</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp> | Boolean | Required |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;administrative_distance</samp> | Integer |  |  | Min: 1<br>Max: 255 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;static</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;boundaries</samp> | List, items: Dictionary |  |  |  | Boundaries can be either 1 ACL or a list of multicast IP address_range(s)/prefix but not combination of both |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- boundary</samp> | String | Required, Unique |  |  | IPv6 access-list name or IPv6 multicast group prefix with mask |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_route_export</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp> | Boolean | Required |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;administrative_distance</samp> | Integer |  |  | Min: 1<br>Max: 255 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;static</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf_network_point_to_point</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf_area</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf_cost</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf_authentication</samp> | String |  |  | Valid Values:<br>- none<br>- simple<br>- message-digest |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf_authentication_key</samp> | String |  |  |  | Encrypted password used for simple authentication |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf_message_digest_keys</samp> | List, items: Dictionary |  |  |  | Keys used for message-digest authentication |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- id</samp> | Integer | Required, Unique |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hash_algorithm</samp> | String |  |  | Valid Values:<br>- md5<br>- sha1<br>- sha256<br>- sha384<br>- sha512 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp> | String |  |  |  | Encrypted password |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;pim</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dr_priority</samp> | Integer |  |  | Min: 0<br>Max: 429467295 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sparse_mode</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_interface</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_enable</samp> | String |  |  |  | ISIS instance name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_passive</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_metric</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_network_point_to_point</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;no_autostate</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;vrrp_ids</samp> | List, items: Dictionary |  |  |  | Improved "vrrp" data model to support multiple VRRP IDs |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- id</samp> | Integer | Required, Unique |  |  | VRID |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority_level</samp> | Integer |  |  |  | Instance priority |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;advertisement</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp> | Integer |  |  |  | Interval in seconds |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;preempt</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp> | Boolean | Required |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;delay</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;minimum</samp> | Integer |  |  |  | Minimum preempt delay in seconds |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reload</samp> | Integer |  |  |  | Reload preempt delay in seconds |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timers</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;delay</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reload</samp> | Integer |  |  |  | Delay after reload in seconds. |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tracked_object</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  | Tracked object name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;decrement</samp> | Integer |  |  | Min: 1<br>Max: 254 | Decrement VRRP priority by 1-254 |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address</samp> | String | Required |  |  | Virtual IPv4 address |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp> | Integer |  |  | Valid Values:<br>- 2<br>- 3 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address</samp> | String | Required |  |  | Virtual IPv6 address |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;vrrp</samp> | Dictionary |  |  |  | "vrrp" key will be deprecated in AVD v4.0<br>This should not be mixed with the new "vrrp_ids" key above to avoid conflicts.<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;virtual_router</samp> | String |  |  |  | Virtual Router ID |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp> | Integer |  |  |  | Instance priority |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;advertisement_interval</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;preempt_delay_minimum</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp> | String |  |  |  | Virtual IPv4 address |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6</samp> | String |  |  |  | Virtual IPv6 address |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_attached_host_route_export</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;distance</samp> | Integer |  |  | Min: 1<br>Max: 255 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;echo</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp> | Integer |  |  |  | Rate in milliseconds |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;min_rx</samp> | Integer |  |  |  | Minimum RX hold time in milliseconds |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multiplier</samp> | Integer |  |  | Min: 3<br>Max: 50 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;service_policy</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pbr</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;input</samp> | String |  |  |  | Name of policy-map used for policy based routing |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;pvlan_mapping</samp> | String |  |  |  | List of VLANs as string |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;tenant</samp> | String |  |  |  | Key only used for documentation or validation purposes |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;tags</samp> | List, items: String |  |  |  | Key only used for documentation or validation purposes |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;type</samp> | String |  |  |  | Key only used for documentation or validation purposes |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;eos_cli</samp> | String |  |  |  | Multiline EOS CLI rendered directly on the VLAN interface in the final EOS configuration |

=== "YAML"

    ```yaml
    vlan_interfaces:
      - name: <str>
        description: <str>
        shutdown: <bool>
        vrf: <str>
        arp_aging_timeout: <int>
        arp_cache_dynamic_capacity: <int>
        arp_gratuitous_accept: <bool>
        arp_monitor_mac_address: <bool>
        ip_proxy_arp: <bool>
        ip_directed_broadcast: <bool>
        ip_address: <str>
        ip_address_secondaries:
          - <str>
        ip_virtual_router_addresses:
          - <str>
        ip_address_virtual: <str>
        ip_address_virtual_secondaries:
          - <str>
        ip_igmp: <bool>
        ip_helpers:
          - ip_helper: <str>
            source_interface: <str>
            vrf: <str>
        ipv6_enable: <bool>
        ipv6_address: <str>
        ipv6_address_virtual: <str>
        ipv6_address_virtuals:
          - <str>
        ipv6_address_link_local: <str>
        ipv6_virtual_router_address: <str>
        ipv6_virtual_router_addresses:
          - <str>
        ipv6_nd_ra_disabled: <bool>
        ipv6_nd_managed_config_flag: <bool>
        ipv6_nd_prefixes:
          - ipv6_prefix: <str>
            valid_lifetime: <str>
            preferred_lifetime: <str>
            no_autoconfig_flag: <bool>
        access_group_in: <str>
        access_group_out: <str>
        ipv6_access_group_in: <str>
        ipv6_access_group_out: <str>
        multicast:
          ipv4:
            boundaries:
              - boundary: <str>
                out: <bool>
            source_route_export:
              enabled: <bool>
              administrative_distance: <int>
            static: <bool>
          ipv6:
            boundaries:
              - boundary: <str>
            source_route_export:
              enabled: <bool>
              administrative_distance: <int>
            static: <bool>
        ospf_network_point_to_point: <bool>
        ospf_area: <str>
        ospf_cost: <int>
        ospf_authentication: <str>
        ospf_authentication_key: <str>
        ospf_message_digest_keys:
          - id: <int>
            hash_algorithm: <str>
            key: <str>
        pim:
          ipv4:
            dr_priority: <int>
            sparse_mode: <bool>
            local_interface: <str>
        isis_enable: <str>
        isis_passive: <bool>
        isis_metric: <int>
        isis_network_point_to_point: <bool>
        mtu: <int>
        no_autostate: <bool>
        vrrp_ids:
          - id: <int>
            priority_level: <int>
            advertisement:
              interval: <int>
            preempt:
              enabled: <bool>
              delay:
                minimum: <int>
                reload: <int>
            timers:
              delay:
                reload: <int>
            tracked_object:
              - name: <str>
                decrement: <int>
                shutdown: <bool>
            ipv4:
              address: <str>
              version: <int>
            ipv6:
              address: <str>
        vrrp:
          virtual_router: <str>
          priority: <int>
          advertisement_interval: <int>
          preempt_delay_minimum: <int>
          ipv4: <str>
          ipv6: <str>
        ip_attached_host_route_export:
          distance: <int>
        bfd:
          echo: <bool>
          interval: <int>
          min_rx: <int>
          multiplier: <int>
        service_policy:
          pbr:
            input: <str>
        pvlan_mapping: <str>
        tenant: <str>
        tags:
          - <str>
        type: <str>
        eos_cli: <str>
    ```
## VxLAN Interface



=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>vxlan_interface</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;Vxlan1</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;description</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;vxlan</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp> | String |  |  |  | Source Interface Name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_source_interface</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;udp_port</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;virtual_router_encapsulation_mac_address</samp> | String |  |  |  | "mlag-system-id" or ethernet_address (H.H.H)<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bfd_vtep_evpn</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;min_rx</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multiplier</samp> | Integer |  |  | Min: 3<br>Max: 50 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;qos</samp> | Dictionary |  |  |  | For the Traffic Class to be derived based on the outer DSCP field of the incoming VxLan packet, the core ports must be in "DSCP Trust" mode.<br>!!!Warning, only few hardware types with software version >= 4.26.0 support the below knobs to configure Vxlan DSCP mapping.<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dscp_propagation_encapsulation</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;map_dscp_to_traffic_class_decapsulation</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlans</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- id</samp> | Integer | Required, Unique |  |  | VLAN ID |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vni</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multicast_group</samp> | String |  |  |  | IP Multicast Group Address |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;flood_vteps</samp> | List, items: String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp> | String |  |  |  | Remote VTEP IP Address |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrfs</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  | VRF Name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vni</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multicast_group</samp> | String |  |  |  | IP Multicast Group Address |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;flood_vteps</samp> | List, items: String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp> | String |  |  |  | Remote VTEP IP Address |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;flood_vtep_learned_data_plane</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;eos_cli</samp> | String |  |  |  | Multiline String with EOS CLI rendered directly on the Vxlan interface in the final EOS configuration. |

=== "YAML"

    ```yaml
    vxlan_interface:
      Vxlan1:
        description: <str>
        vxlan:
          source_interface: <str>
          mlag_source_interface: <str>
          udp_port: <int>
          virtual_router_encapsulation_mac_address: <str>
          bfd_vtep_evpn:
            interval: <int>
            min_rx: <int>
            multiplier: <int>
            prefix_list: <str>
          qos:
            dscp_propagation_encapsulation: <bool>
            map_dscp_to_traffic_class_decapsulation: <bool>
          vlans:
            - id: <int>
              vni: <int>
              multicast_group: <str>
              flood_vteps:
                - <str>
          vrfs:
            - name: <str>
              vni: <int>
              multicast_group: <str>
          flood_vteps:
            - <str>
          flood_vtep_learned_data_plane: <bool>
        eos_cli: <str>
    ```
