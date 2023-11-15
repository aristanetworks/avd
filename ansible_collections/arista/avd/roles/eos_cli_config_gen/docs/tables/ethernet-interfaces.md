<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>ethernet_interfaces</samp>](## "ethernet_interfaces") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "ethernet_interfaces.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "ethernet_interfaces.[].description") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "ethernet_interfaces.[].shutdown") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;load_interval</samp>](## "ethernet_interfaces.[].load_interval") | Integer |  |  | Min: 0<br>Max: 600 | Interval in seconds for updating interface counters" |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;speed</samp>](## "ethernet_interfaces.[].speed") | String |  |  |  | Speed should be set in the format `<interface_speed>` or `forced <interface_speed>` or `auto <interface_speed>`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp>](## "ethernet_interfaces.[].mtu") | Integer |  |  | Min: 68<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;l2_mtu</samp>](## "ethernet_interfaces.[].l2_mtu") | Integer |  |  | Min: 68<br>Max: 65535 | "l2_mtu" should only be defined for platforms supporting the "l2 mtu" CLI<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;l2_mru</samp>](## "ethernet_interfaces.[].l2_mru") | Integer |  |  | Min: 68<br>Max: 65535 | "l2_mru" should only be defined for platforms supporting the "l2 mru" CLI<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vlans</samp>](## "ethernet_interfaces.[].vlans") | String |  |  |  | List of switchport vlans as string<br>For a trunk port this would be a range like "1-200,300"<br>For an access port this would be a single vlan "123"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;native_vlan</samp>](## "ethernet_interfaces.[].native_vlan") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;native_vlan_tag</samp>](## "ethernet_interfaces.[].native_vlan_tag") | Boolean |  |  |  | If setting both native_vlan and native_vlan_tag, native_vlan_tag takes precedence |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "ethernet_interfaces.[].mode") | String |  |  | Valid Values:<br>- <code>access</code><br>- <code>dot1q-tunnel</code><br>- <code>trunk</code><br>- <code>trunk phone</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;phone</samp>](## "ethernet_interfaces.[].phone") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;trunk</samp>](## "ethernet_interfaces.[].phone.trunk") | String |  |  | Valid Values:<br>- <code>tagged</code><br>- <code>tagged phone</code><br>- <code>untagged</code><br>- <code>untagged phone</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan</samp>](## "ethernet_interfaces.[].phone.vlan") | Integer |  |  | Min: 1<br>Max: 4094 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;l2_protocol</samp>](## "ethernet_interfaces.[].l2_protocol") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;encapsulation_dot1q_vlan</samp>](## "ethernet_interfaces.[].l2_protocol.encapsulation_dot1q_vlan") | Integer |  |  |  | Vlan tag to configure on sub-interface |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;forwarding_profile</samp>](## "ethernet_interfaces.[].l2_protocol.forwarding_profile") | String |  |  |  | L2 protocol forwarding profile |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;trunk_groups</samp>](## "ethernet_interfaces.[].trunk_groups") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "ethernet_interfaces.[].trunk_groups.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "ethernet_interfaces.[].type") | String |  |  | Valid Values:<br>- <code>routed</code><br>- <code>switched</code><br>- <code>l3dot1q</code><br>- <code>l2dot1q</code><br>- <code>port-channel-member</code> | l3dot1q and l2dot1q are used for sub-interfaces. The parent interface should be defined as routed.<br>Interface will not be listed in device documentation, unless "type" is set.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;snmp_trap_link_change</samp>](## "ethernet_interfaces.[].snmp_trap_link_change") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;address_locking</samp>](## "ethernet_interfaces.[].address_locking") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp>](## "ethernet_interfaces.[].address_locking.ipv4") | Boolean |  |  |  | Enable address locking for IPv4 |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6</samp>](## "ethernet_interfaces.[].address_locking.ipv6") | Boolean |  |  |  | Enable address locking for IPv6 |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;flowcontrol</samp>](## "ethernet_interfaces.[].flowcontrol") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;received</samp>](## "ethernet_interfaces.[].flowcontrol.received") | String |  |  | Valid Values:<br>- <code>desired</code><br>- <code>on</code><br>- <code>off</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "ethernet_interfaces.[].vrf") | String |  |  |  | VRF name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;flow_tracker</samp>](## "ethernet_interfaces.[].flow_tracker") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sampled</samp>](## "ethernet_interfaces.[].flow_tracker.sampled") | String |  |  |  | Sampled flow tracker name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hardware</samp>](## "ethernet_interfaces.[].flow_tracker.hardware") | String |  |  |  | Hardware flow tracker name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;error_correction_encoding</samp>](## "ethernet_interfaces.[].error_correction_encoding") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "ethernet_interfaces.[].error_correction_encoding.enabled") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;fire_code</samp>](## "ethernet_interfaces.[].error_correction_encoding.fire_code") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reed_solomon</samp>](## "ethernet_interfaces.[].error_correction_encoding.reed_solomon") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;link_tracking_groups</samp>](## "ethernet_interfaces.[].link_tracking_groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "ethernet_interfaces.[].link_tracking_groups.[].name") | String | Required, Unique |  |  | Group name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction</samp>](## "ethernet_interfaces.[].link_tracking_groups.[].direction") | String |  |  | Valid Values:<br>- <code>upstream</code><br>- <code>downstream</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;evpn_ethernet_segment</samp>](## "ethernet_interfaces.[].evpn_ethernet_segment") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;identifier</samp>](## "ethernet_interfaces.[].evpn_ethernet_segment.identifier") | String |  |  |  | EVPN Ethernet Segment Identifier (Type 1 format) |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;redundancy</samp>](## "ethernet_interfaces.[].evpn_ethernet_segment.redundancy") | String |  |  | Valid Values:<br>- <code>all-active</code><br>- <code>single-active</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;designated_forwarder_election</samp>](## "ethernet_interfaces.[].evpn_ethernet_segment.designated_forwarder_election") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;algorithm</samp>](## "ethernet_interfaces.[].evpn_ethernet_segment.designated_forwarder_election.algorithm") | String |  |  | Valid Values:<br>- <code>modulus</code><br>- <code>preference</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;preference_value</samp>](## "ethernet_interfaces.[].evpn_ethernet_segment.designated_forwarder_election.preference_value") | Integer |  |  | Min: 0<br>Max: 65535 | Preference_value is only used when "algorithm" is "preference" |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dont_preempt</samp>](## "ethernet_interfaces.[].evpn_ethernet_segment.designated_forwarder_election.dont_preempt") | Boolean |  |  |  | Dont_preempt is only used when "algorithm" is "preference" |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hold_time</samp>](## "ethernet_interfaces.[].evpn_ethernet_segment.designated_forwarder_election.hold_time") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;subsequent_hold_time</samp>](## "ethernet_interfaces.[].evpn_ethernet_segment.designated_forwarder_election.subsequent_hold_time") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;candidate_reachability_required</samp>](## "ethernet_interfaces.[].evpn_ethernet_segment.designated_forwarder_election.candidate_reachability_required") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls</samp>](## "ethernet_interfaces.[].evpn_ethernet_segment.mpls") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shared_index</samp>](## "ethernet_interfaces.[].evpn_ethernet_segment.mpls.shared_index") | Integer |  |  | Min: 1<br>Max: 1024 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tunnel_flood_filter_time</samp>](## "ethernet_interfaces.[].evpn_ethernet_segment.mpls.tunnel_flood_filter_time") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_target</samp>](## "ethernet_interfaces.[].evpn_ethernet_segment.route_target") | String |  |  |  | EVPN Route Target for ESI with format xx:xx:xx:xx:xx:xx |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;encapsulation_dot1q_vlan</samp>](## "ethernet_interfaces.[].encapsulation_dot1q_vlan") | Integer |  |  |  | VLAN tag to configure on sub-interface |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;encapsulation_vlan</samp>](## "ethernet_interfaces.[].encapsulation_vlan") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;client</samp>](## "ethernet_interfaces.[].encapsulation_vlan.client") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dot1q</samp>](## "ethernet_interfaces.[].encapsulation_vlan.client.dot1q") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan</samp>](## "ethernet_interfaces.[].encapsulation_vlan.client.dot1q.vlan") | Integer |  |  |  | Client VLAN ID |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;outer</samp>](## "ethernet_interfaces.[].encapsulation_vlan.client.dot1q.outer") | Integer |  |  |  | Client Outer VLAN ID |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inner</samp>](## "ethernet_interfaces.[].encapsulation_vlan.client.dot1q.inner") | Integer |  |  |  | Client Inner VLAN ID |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unmatched</samp>](## "ethernet_interfaces.[].encapsulation_vlan.client.unmatched") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;network</samp>](## "ethernet_interfaces.[].encapsulation_vlan.network") | Dictionary |  |  |  | Network encapsulations are all optional and skipped if using client unmatched |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dot1q</samp>](## "ethernet_interfaces.[].encapsulation_vlan.network.dot1q") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan</samp>](## "ethernet_interfaces.[].encapsulation_vlan.network.dot1q.vlan") | Integer |  |  |  | Network VLAN ID |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;outer</samp>](## "ethernet_interfaces.[].encapsulation_vlan.network.dot1q.outer") | Integer |  |  |  | Network outer VLAN ID |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inner</samp>](## "ethernet_interfaces.[].encapsulation_vlan.network.dot1q.inner") | Integer |  |  |  | Network inner VLAN ID |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;client</samp>](## "ethernet_interfaces.[].encapsulation_vlan.network.client") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vlan_id</samp>](## "ethernet_interfaces.[].vlan_id") | Integer |  |  | Min: 1<br>Max: 4094 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "ethernet_interfaces.[].ip_address") | String |  |  |  | IPv4 address/mask or "dhcp" |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_address_secondaries</samp>](## "ethernet_interfaces.[].ip_address_secondaries") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "ethernet_interfaces.[].ip_address_secondaries.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;dhcp_client_accept_default_route</samp>](## "ethernet_interfaces.[].dhcp_client_accept_default_route") | Boolean |  |  |  | Install default-route obtained via DHCP |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;dhcp_server_ipv4</samp>](## "ethernet_interfaces.[].dhcp_server_ipv4") | Boolean |  |  |  | Enable IPv4 DHCP server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;dhcp_server_ipv6</samp>](## "ethernet_interfaces.[].dhcp_server_ipv6") | Boolean |  |  |  | Enable IPv6 DHCP server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_helpers</samp>](## "ethernet_interfaces.[].ip_helpers") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;ip_helper</samp>](## "ethernet_interfaces.[].ip_helpers.[].ip_helper") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp>](## "ethernet_interfaces.[].ip_helpers.[].source_interface") | String |  |  |  | Source interface name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "ethernet_interfaces.[].ip_helpers.[].vrf") | String |  |  |  | VRF name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_nat</samp>](## "ethernet_interfaces.[].ip_nat") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;service_profile</samp>](## "ethernet_interfaces.[].ip_nat.service_profile") | String |  |  |  | NAT interface profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;destination</samp>](## "ethernet_interfaces.[].ip_nat.destination") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dynamic</samp>](## "ethernet_interfaces.[].ip_nat.destination.dynamic") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;access_list</samp>](## "ethernet_interfaces.[].ip_nat.destination.dynamic.[].access_list") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;comment</samp>](## "ethernet_interfaces.[].ip_nat.destination.dynamic.[].comment") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pool_name</samp>](## "ethernet_interfaces.[].ip_nat.destination.dynamic.[].pool_name") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "ethernet_interfaces.[].ip_nat.destination.dynamic.[].priority") | Integer |  |  | Min: 0<br>Max: 4294967295 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;static</samp>](## "ethernet_interfaces.[].ip_nat.destination.static") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;access_list</samp>](## "ethernet_interfaces.[].ip_nat.destination.static.[].access_list") | String |  |  |  | 'access_list' and 'group' are mutual exclusive |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;comment</samp>](## "ethernet_interfaces.[].ip_nat.destination.static.[].comment") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction</samp>](## "ethernet_interfaces.[].ip_nat.destination.static.[].direction") | String |  |  | Valid Values:<br>- <code>egress</code><br>- <code>ingress</code> | Egress or ingress can be the default. This depends on source/destination, EOS version, and hardware platform.<br>EOS might remove this keyword in the configuration. So, check the configuration on targeted HW/SW.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp>](## "ethernet_interfaces.[].ip_nat.destination.static.[].group") | Integer |  |  | Min: 1<br>Max: 65535 | 'access_list' and 'group' are mutual exclusive |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;original_ip</samp>](## "ethernet_interfaces.[].ip_nat.destination.static.[].original_ip") | String | Required, Unique |  |  | IPv4 address |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;original_port</samp>](## "ethernet_interfaces.[].ip_nat.destination.static.[].original_port") | Integer |  |  | Min: 1<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "ethernet_interfaces.[].ip_nat.destination.static.[].priority") | Integer |  |  | Min: 0<br>Max: 4294967295 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;protocol</samp>](## "ethernet_interfaces.[].ip_nat.destination.static.[].protocol") | String |  |  | Valid Values:<br>- <code>udp</code><br>- <code>tcp</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;translated_ip</samp>](## "ethernet_interfaces.[].ip_nat.destination.static.[].translated_ip") | String | Required |  |  | IPv4 address |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;translated_port</samp>](## "ethernet_interfaces.[].ip_nat.destination.static.[].translated_port") | Integer |  |  | Min: 1<br>Max: 65535 | requires 'original_port' |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source</samp>](## "ethernet_interfaces.[].ip_nat.source") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dynamic</samp>](## "ethernet_interfaces.[].ip_nat.source.dynamic") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;access_list</samp>](## "ethernet_interfaces.[].ip_nat.source.dynamic.[].access_list") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;comment</samp>](## "ethernet_interfaces.[].ip_nat.source.dynamic.[].comment") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nat_type</samp>](## "ethernet_interfaces.[].ip_nat.source.dynamic.[].nat_type") | String | Required |  | Valid Values:<br>- <code>overload</code><br>- <code>pool</code><br>- <code>pool-address-only</code><br>- <code>pool-full-cone</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pool_name</samp>](## "ethernet_interfaces.[].ip_nat.source.dynamic.[].pool_name") | String |  |  |  | required if 'nat_type' is pool, pool-address-only or pool-full-cone<br>ignored if 'nat_type' is overload<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "ethernet_interfaces.[].ip_nat.source.dynamic.[].priority") | Integer |  |  | Min: 0<br>Max: 4294967295 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;static</samp>](## "ethernet_interfaces.[].ip_nat.source.static") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;access_list</samp>](## "ethernet_interfaces.[].ip_nat.source.static.[].access_list") | String |  |  |  | 'access_list' and 'group' are mutual exclusive |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;comment</samp>](## "ethernet_interfaces.[].ip_nat.source.static.[].comment") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction</samp>](## "ethernet_interfaces.[].ip_nat.source.static.[].direction") | String |  |  | Valid Values:<br>- <code>egress</code><br>- <code>ingress</code> | Egress or ingress can be the default. This depends on source/destination, EOS version, and hardware platform.<br>EOS might remove this keyword in the configuration. So, check the configuration on targeted HW/SW.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp>](## "ethernet_interfaces.[].ip_nat.source.static.[].group") | Integer |  |  | Min: 1<br>Max: 65535 | 'access_list' and 'group' are mutual exclusive |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;original_ip</samp>](## "ethernet_interfaces.[].ip_nat.source.static.[].original_ip") | String | Required, Unique |  |  | IPv4 address |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;original_port</samp>](## "ethernet_interfaces.[].ip_nat.source.static.[].original_port") | Integer |  |  | Min: 1<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "ethernet_interfaces.[].ip_nat.source.static.[].priority") | Integer |  |  | Min: 0<br>Max: 4294967295 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;protocol</samp>](## "ethernet_interfaces.[].ip_nat.source.static.[].protocol") | String |  |  | Valid Values:<br>- <code>udp</code><br>- <code>tcp</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;translated_ip</samp>](## "ethernet_interfaces.[].ip_nat.source.static.[].translated_ip") | String | Required |  |  | IPv4 address |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;translated_port</samp>](## "ethernet_interfaces.[].ip_nat.source.static.[].translated_port") | Integer |  |  | Min: 1<br>Max: 65535 | requires 'original_port' |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_enable</samp>](## "ethernet_interfaces.[].ipv6_enable") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address</samp>](## "ethernet_interfaces.[].ipv6_address") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address_link_local</samp>](## "ethernet_interfaces.[].ipv6_address_link_local") | String |  |  |  | Link local IPv6 address/mask |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_nd_ra_disabled</samp>](## "ethernet_interfaces.[].ipv6_nd_ra_disabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_nd_managed_config_flag</samp>](## "ethernet_interfaces.[].ipv6_nd_managed_config_flag") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_nd_prefixes</samp>](## "ethernet_interfaces.[].ipv6_nd_prefixes") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;ipv6_prefix</samp>](## "ethernet_interfaces.[].ipv6_nd_prefixes.[].ipv6_prefix") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;valid_lifetime</samp>](## "ethernet_interfaces.[].ipv6_nd_prefixes.[].valid_lifetime") | String |  |  |  | Infinite or lifetime in seconds |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;preferred_lifetime</samp>](## "ethernet_interfaces.[].ipv6_nd_prefixes.[].preferred_lifetime") | String |  |  |  | Infinite or lifetime in seconds |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;no_autoconfig_flag</samp>](## "ethernet_interfaces.[].ipv6_nd_prefixes.[].no_autoconfig_flag") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_dhcp_relay_destinations</samp>](## "ethernet_interfaces.[].ipv6_dhcp_relay_destinations") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;address</samp>](## "ethernet_interfaces.[].ipv6_dhcp_relay_destinations.[].address") | String | Required, Unique |  |  | DHCP server's IPv6 address |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "ethernet_interfaces.[].ipv6_dhcp_relay_destinations.[].vrf") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_interface</samp>](## "ethernet_interfaces.[].ipv6_dhcp_relay_destinations.[].local_interface") | String |  |  |  | Local interface to communicate with DHCP server - mutually exclusive to source_address |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_address</samp>](## "ethernet_interfaces.[].ipv6_dhcp_relay_destinations.[].source_address") | String |  |  |  | Source IPv6 address to communicate with DHCP server - mutually exclusive to local_interface |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;link_address</samp>](## "ethernet_interfaces.[].ipv6_dhcp_relay_destinations.[].link_address") | String |  |  |  | Override the default link address specified in the relayed DHCP packet |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;access_group_in</samp>](## "ethernet_interfaces.[].access_group_in") | String |  |  |  | Access list name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;access_group_out</samp>](## "ethernet_interfaces.[].access_group_out") | String |  |  |  | Access list name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_access_group_in</samp>](## "ethernet_interfaces.[].ipv6_access_group_in") | String |  |  |  | IPv6 access list name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_access_group_out</samp>](## "ethernet_interfaces.[].ipv6_access_group_out") | String |  |  |  | IPv6 access list name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mac_access_group_in</samp>](## "ethernet_interfaces.[].mac_access_group_in") | String |  |  |  | MAC access list name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mac_access_group_out</samp>](## "ethernet_interfaces.[].mac_access_group_out") | String |  |  |  | MAC access list name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;multicast</samp>](## "ethernet_interfaces.[].multicast") | Dictionary |  |  |  | Boundaries can be either 1 ACL or a list of multicast IP address_range(s)/prefix but not combination of both |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp>](## "ethernet_interfaces.[].multicast.ipv4") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;boundaries</samp>](## "ethernet_interfaces.[].multicast.ipv4.boundaries") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;boundary</samp>](## "ethernet_interfaces.[].multicast.ipv4.boundaries.[].boundary") | String |  |  |  | ACL name or multicast IP subnet |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;out</samp>](## "ethernet_interfaces.[].multicast.ipv4.boundaries.[].out") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;static</samp>](## "ethernet_interfaces.[].multicast.ipv4.static") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6</samp>](## "ethernet_interfaces.[].multicast.ipv6") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;boundaries</samp>](## "ethernet_interfaces.[].multicast.ipv6.boundaries") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;boundary</samp>](## "ethernet_interfaces.[].multicast.ipv6.boundaries.[].boundary") | String |  |  |  | ACL name or multicast IP subnet |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;static</samp>](## "ethernet_interfaces.[].multicast.ipv6.static") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf_network_point_to_point</samp>](## "ethernet_interfaces.[].ospf_network_point_to_point") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf_area</samp>](## "ethernet_interfaces.[].ospf_area") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf_cost</samp>](## "ethernet_interfaces.[].ospf_cost") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf_authentication</samp>](## "ethernet_interfaces.[].ospf_authentication") | String |  |  | Valid Values:<br>- <code>none</code><br>- <code>simple</code><br>- <code>message-digest</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf_authentication_key</samp>](## "ethernet_interfaces.[].ospf_authentication_key") | String |  |  |  | Encrypted password - only type 7 supported |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf_message_digest_keys</samp>](## "ethernet_interfaces.[].ospf_message_digest_keys") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;id</samp>](## "ethernet_interfaces.[].ospf_message_digest_keys.[].id") | Integer | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hash_algorithm</samp>](## "ethernet_interfaces.[].ospf_message_digest_keys.[].hash_algorithm") | String |  |  | Valid Values:<br>- <code>md5</code><br>- <code>sha1</code><br>- <code>sha256</code><br>- <code>sha384</code><br>- <code>sha512</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "ethernet_interfaces.[].ospf_message_digest_keys.[].key") | String |  |  |  | Encrypted password - only type 7 supported |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;pim</samp>](## "ethernet_interfaces.[].pim") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp>](## "ethernet_interfaces.[].pim.ipv4") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dr_priority</samp>](## "ethernet_interfaces.[].pim.ipv4.dr_priority") | Integer |  |  | Min: 0<br>Max: 429467295 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sparse_mode</samp>](## "ethernet_interfaces.[].pim.ipv4.sparse_mode") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mac_security</samp>](## "ethernet_interfaces.[].mac_security") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "ethernet_interfaces.[].mac_security.profile") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;channel_group</samp>](## "ethernet_interfaces.[].channel_group") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id</samp>](## "ethernet_interfaces.[].channel_group.id") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "ethernet_interfaces.[].channel_group.mode") | String |  |  | Valid Values:<br>- <code>on</code><br>- <code>active</code><br>- <code>passive</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_enable</samp>](## "ethernet_interfaces.[].isis_enable") | String |  |  |  | ISIS instance |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_passive</samp>](## "ethernet_interfaces.[].isis_passive") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_metric</samp>](## "ethernet_interfaces.[].isis_metric") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_network_point_to_point</samp>](## "ethernet_interfaces.[].isis_network_point_to_point") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_circuit_type</samp>](## "ethernet_interfaces.[].isis_circuit_type") | String |  |  | Valid Values:<br>- <code>level-1-2</code><br>- <code>level-1</code><br>- <code>level-2</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_hello_padding</samp>](## "ethernet_interfaces.[].isis_hello_padding") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_authentication_mode</samp>](## "ethernet_interfaces.[].isis_authentication_mode") | String |  |  | Valid Values:<br>- <code>text</code><br>- <code>md5</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_authentication_key</samp>](## "ethernet_interfaces.[].isis_authentication_key") | String |  |  |  | Type-7 encrypted password |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;poe</samp>](## "ethernet_interfaces.[].poe") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;disabled</samp>](## "ethernet_interfaces.[].poe.disabled") | Boolean |  | `False` |  | Disable PoE on a POE capable port. PoE is enabled on all ports that support it by default in EOS. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "ethernet_interfaces.[].poe.priority") | String |  |  | Valid Values:<br>- <code>critical</code><br>- <code>high</code><br>- <code>medium</code><br>- <code>low</code> | Prioritize a port's power in the event that one of the switch's power supplies loses power |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reboot</samp>](## "ethernet_interfaces.[].poe.reboot") | Dictionary |  |  |  | Set the PoE power behavior for a PoE port when the system is rebooted |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "ethernet_interfaces.[].poe.reboot.action") | String |  |  | Valid Values:<br>- <code>maintain</code><br>- <code>power-off</code> | PoE action for interface |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;link_down</samp>](## "ethernet_interfaces.[].poe.link_down") | Dictionary |  |  |  | Set the PoE power behavior for a PoE port when the port goes down |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "ethernet_interfaces.[].poe.link_down.action") | String |  |  | Valid Values:<br>- <code>maintain</code><br>- <code>power-off</code> | PoE action for interface |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;power_off_delay</samp>](## "ethernet_interfaces.[].poe.link_down.power_off_delay") | Integer |  |  | Min: 1<br>Max: 86400 | Number of seconds to delay shutting the power off after a link down event occurs. Default value is 5 seconds in EOS. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "ethernet_interfaces.[].poe.shutdown") | Dictionary |  |  |  | Set the PoE power behavior for a PoE port when the port is admin down |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "ethernet_interfaces.[].poe.shutdown.action") | String |  |  | Valid Values:<br>- <code>maintain</code><br>- <code>power-off</code> | PoE action for interface |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;limit</samp>](## "ethernet_interfaces.[].poe.limit") | Dictionary |  |  |  | Override the hardware-negotiated power limit using either wattage or a power class. Note that if using a power class, AVD will automatically convert the class value to the wattage value corresponding to that power class. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;class</samp>](## "ethernet_interfaces.[].poe.limit.class") | Integer |  |  | Min: 0<br>Max: 8 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;watts</samp>](## "ethernet_interfaces.[].poe.limit.watts") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;fixed</samp>](## "ethernet_interfaces.[].poe.limit.fixed") | Boolean |  |  |  | Set to ignore hardware classification |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;negotiation_lldp</samp>](## "ethernet_interfaces.[].poe.negotiation_lldp") | Boolean |  |  |  | Disable to prevent port from negotiating power with powered devices over LLDP. Enabled by default in EOS. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;legacy_detect</samp>](## "ethernet_interfaces.[].poe.legacy_detect") | Boolean |  |  |  | Allow a subset of legacy devices to work with the PoE switch. Disabled by default in EOS because it can cause false positive detections. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ptp</samp>](## "ethernet_interfaces.[].ptp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable</samp>](## "ethernet_interfaces.[].ptp.enable") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;announce</samp>](## "ethernet_interfaces.[].ptp.announce") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "ethernet_interfaces.[].ptp.announce.interval") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timeout</samp>](## "ethernet_interfaces.[].ptp.announce.timeout") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;delay_req</samp>](## "ethernet_interfaces.[].ptp.delay_req") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;delay_mechanism</samp>](## "ethernet_interfaces.[].ptp.delay_mechanism") | String |  |  | Valid Values:<br>- <code>e2e</code><br>- <code>p2p</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sync_message</samp>](## "ethernet_interfaces.[].ptp.sync_message") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "ethernet_interfaces.[].ptp.sync_message.interval") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;role</samp>](## "ethernet_interfaces.[].ptp.role") | String |  |  | Valid Values:<br>- <code>master</code><br>- <code>dynamic</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan</samp>](## "ethernet_interfaces.[].ptp.vlan") | String |  |  |  | VLAN can be 'all' or list of vlans as string |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;transport</samp>](## "ethernet_interfaces.[].ptp.transport") | String |  |  | Valid Values:<br>- <code>ipv4</code><br>- <code>ipv6</code><br>- <code>layer2</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "ethernet_interfaces.[].profile") | String |  |  |  | Interface profile |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;storm_control</samp>](## "ethernet_interfaces.[].storm_control") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;all</samp>](## "ethernet_interfaces.[].storm_control.all") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp>](## "ethernet_interfaces.[].storm_control.all.level") | String |  |  |  | Configure maximum storm-control level |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp>](## "ethernet_interfaces.[].storm_control.all.unit") | String |  | `percent` | Valid Values:<br>- <code>percent</code><br>- <code>pps</code> | Optional field and is hardware dependent |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;broadcast</samp>](## "ethernet_interfaces.[].storm_control.broadcast") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp>](## "ethernet_interfaces.[].storm_control.broadcast.level") | String |  |  |  | Configure maximum storm-control level |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp>](## "ethernet_interfaces.[].storm_control.broadcast.unit") | String |  | `percent` | Valid Values:<br>- <code>percent</code><br>- <code>pps</code> | Optional field and is hardware dependent |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multicast</samp>](## "ethernet_interfaces.[].storm_control.multicast") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp>](## "ethernet_interfaces.[].storm_control.multicast.level") | String |  |  |  | Configure maximum storm-control level |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp>](## "ethernet_interfaces.[].storm_control.multicast.unit") | String |  | `percent` | Valid Values:<br>- <code>percent</code><br>- <code>pps</code> | Optional field and is hardware dependent |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unknown_unicast</samp>](## "ethernet_interfaces.[].storm_control.unknown_unicast") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp>](## "ethernet_interfaces.[].storm_control.unknown_unicast.level") | String |  |  |  | Configure maximum storm-control level |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp>](## "ethernet_interfaces.[].storm_control.unknown_unicast.unit") | String |  | `percent` | Valid Values:<br>- <code>percent</code><br>- <code>pps</code> | Optional field and is hardware dependent |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;logging</samp>](## "ethernet_interfaces.[].logging") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;event</samp>](## "ethernet_interfaces.[].logging.event") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;link_status</samp>](## "ethernet_interfaces.[].logging.event.link_status") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;congestion_drops</samp>](## "ethernet_interfaces.[].logging.event.congestion_drops") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree</samp>](## "ethernet_interfaces.[].logging.event.spanning_tree") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;storm_control_discards</samp>](## "ethernet_interfaces.[].logging.event.storm_control_discards") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;lldp</samp>](## "ethernet_interfaces.[].lldp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;transmit</samp>](## "ethernet_interfaces.[].lldp.transmit") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;receive</samp>](## "ethernet_interfaces.[].lldp.receive") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ztp_vlan</samp>](## "ethernet_interfaces.[].lldp.ztp_vlan") | Integer |  |  |  | ZTP vlan number |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;trunk_private_vlan_secondary</samp>](## "ethernet_interfaces.[].trunk_private_vlan_secondary") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;pvlan_mapping</samp>](## "ethernet_interfaces.[].pvlan_mapping") | String |  |  |  | List of vlans as string |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vlan_translations</samp>](## "ethernet_interfaces.[].vlan_translations") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;from</samp>](## "ethernet_interfaces.[].vlan_translations.[].from") | String |  |  |  | List of vlans as string (only one vlan if direction is "both") |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;to</samp>](## "ethernet_interfaces.[].vlan_translations.[].to") | Integer |  |  |  | VLAN ID |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction</samp>](## "ethernet_interfaces.[].vlan_translations.[].direction") | String |  | `both` | Valid Values:<br>- <code>in</code><br>- <code>out</code><br>- <code>both</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;dot1x</samp>](## "ethernet_interfaces.[].dot1x") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port_control</samp>](## "ethernet_interfaces.[].dot1x.port_control") | String |  |  | Valid Values:<br>- <code>auto</code><br>- <code>force-authorized</code><br>- <code>force-unauthorized</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port_control_force_authorized_phone</samp>](## "ethernet_interfaces.[].dot1x.port_control_force_authorized_phone") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reauthentication</samp>](## "ethernet_interfaces.[].dot1x.reauthentication") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pae</samp>](## "ethernet_interfaces.[].dot1x.pae") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "ethernet_interfaces.[].dot1x.pae.mode") | String |  |  | Valid Values:<br>- <code>authenticator</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;authentication_failure</samp>](## "ethernet_interfaces.[].dot1x.authentication_failure") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "ethernet_interfaces.[].dot1x.authentication_failure.action") | String |  |  | Valid Values:<br>- <code>allow</code><br>- <code>drop</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;allow_vlan</samp>](## "ethernet_interfaces.[].dot1x.authentication_failure.allow_vlan") | Integer |  |  | Min: 1<br>Max: 4094 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;host_mode</samp>](## "ethernet_interfaces.[].dot1x.host_mode") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "ethernet_interfaces.[].dot1x.host_mode.mode") | String |  |  | Valid Values:<br>- <code>multi-host</code><br>- <code>single-host</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multi_host_authenticated</samp>](## "ethernet_interfaces.[].dot1x.host_mode.multi_host_authenticated") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mac_based_authentication</samp>](## "ethernet_interfaces.[].dot1x.mac_based_authentication") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "ethernet_interfaces.[].dot1x.mac_based_authentication.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always</samp>](## "ethernet_interfaces.[].dot1x.mac_based_authentication.always") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;host_mode_common</samp>](## "ethernet_interfaces.[].dot1x.mac_based_authentication.host_mode_common") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timeout</samp>](## "ethernet_interfaces.[].dot1x.timeout") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;idle_host</samp>](## "ethernet_interfaces.[].dot1x.timeout.idle_host") | Integer |  |  | Min: 10<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;quiet_period</samp>](## "ethernet_interfaces.[].dot1x.timeout.quiet_period") | Integer |  |  | Min: 1<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reauth_period</samp>](## "ethernet_interfaces.[].dot1x.timeout.reauth_period") | String |  |  |  | Value can be 60-4294967295 or 'server' |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reauth_timeout_ignore</samp>](## "ethernet_interfaces.[].dot1x.timeout.reauth_timeout_ignore") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tx_period</samp>](## "ethernet_interfaces.[].dot1x.timeout.tx_period") | Integer |  |  | Min: 1<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reauthorization_request_limit</samp>](## "ethernet_interfaces.[].dot1x.reauthorization_request_limit") | Integer |  |  | Min: 1<br>Max: 10 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unauthorized</samp>](## "ethernet_interfaces.[].dot1x.unauthorized") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_vlan_membership_egress</samp>](## "ethernet_interfaces.[].dot1x.unauthorized.access_vlan_membership_egress") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;native_vlan_membership_egress</samp>](## "ethernet_interfaces.[].dot1x.unauthorized.native_vlan_membership_egress") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;eapol</samp>](## "ethernet_interfaces.[].dot1x.eapol") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;disabled</samp>](## "ethernet_interfaces.[].dot1x.eapol.disabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;authentication_failure_fallback_mba</samp>](## "ethernet_interfaces.[].dot1x.eapol.authentication_failure_fallback_mba") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "ethernet_interfaces.[].dot1x.eapol.authentication_failure_fallback_mba.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timeout</samp>](## "ethernet_interfaces.[].dot1x.eapol.authentication_failure_fallback_mba.timeout") | Integer |  |  | Min: 0<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;service_profile</samp>](## "ethernet_interfaces.[].service_profile") | String |  |  |  | QOS profile |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;shape</samp>](## "ethernet_interfaces.[].shape") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rate</samp>](## "ethernet_interfaces.[].shape.rate") | String |  |  |  | Rate in kbps, pps or percent<br>Supported options are platform dependent<br>Examples:<br>- "5000 kbps"<br>- "1000 pps"<br>- "20 percent"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;qos</samp>](## "ethernet_interfaces.[].qos") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;trust</samp>](## "ethernet_interfaces.[].qos.trust") | String |  |  | Valid Values:<br>- <code>dscp</code><br>- <code>cos</code><br>- <code>disabled</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dscp</samp>](## "ethernet_interfaces.[].qos.dscp") | Integer |  |  |  | DSCP value |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cos</samp>](## "ethernet_interfaces.[].qos.cos") | Integer |  |  |  | COS value |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_bpdufilter</samp>](## "ethernet_interfaces.[].spanning_tree_bpdufilter") | String |  |  | Valid Values:<br>- <code>enabled</code><br>- <code>disabled</code><br>- <code>True</code><br>- <code>False</code><br>- <code>true</code><br>- <code>false</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_bpduguard</samp>](## "ethernet_interfaces.[].spanning_tree_bpduguard") | String |  |  | Valid Values:<br>- <code>enabled</code><br>- <code>disabled</code><br>- <code>True</code><br>- <code>False</code><br>- <code>true</code><br>- <code>false</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_guard</samp>](## "ethernet_interfaces.[].spanning_tree_guard") | String |  |  | Valid Values:<br>- <code>loop</code><br>- <code>root</code><br>- <code>disabled</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_portfast</samp>](## "ethernet_interfaces.[].spanning_tree_portfast") | String |  |  | Valid Values:<br>- <code>edge</code><br>- <code>network</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vmtracer</samp>](## "ethernet_interfaces.[].vmtracer") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;priority_flow_control</samp>](## "ethernet_interfaces.[].priority_flow_control") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "ethernet_interfaces.[].priority_flow_control.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priorities</samp>](## "ethernet_interfaces.[].priority_flow_control.priorities") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;priority</samp>](## "ethernet_interfaces.[].priority_flow_control.priorities.[].priority") | Integer | Required, Unique |  | Min: 0<br>Max: 7 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;no_drop</samp>](## "ethernet_interfaces.[].priority_flow_control.priorities.[].no_drop") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp>](## "ethernet_interfaces.[].bfd") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;echo</samp>](## "ethernet_interfaces.[].bfd.echo") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "ethernet_interfaces.[].bfd.interval") | Integer |  |  |  | Interval in milliseconds |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;min_rx</samp>](## "ethernet_interfaces.[].bfd.min_rx") | Integer |  |  |  | Rate in milliseconds |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multiplier</samp>](## "ethernet_interfaces.[].bfd.multiplier") | Integer |  |  | Min: 3<br>Max: 50 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;service_policy</samp>](## "ethernet_interfaces.[].service_policy") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pbr</samp>](## "ethernet_interfaces.[].service_policy.pbr") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;input</samp>](## "ethernet_interfaces.[].service_policy.pbr.input") | String |  |  |  | Policy Based Routing Policy-map name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;qos</samp>](## "ethernet_interfaces.[].service_policy.qos") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;input</samp>](## "ethernet_interfaces.[].service_policy.qos.input") | String | Required |  |  | Quality of Service Policy-map name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mpls</samp>](## "ethernet_interfaces.[].mpls") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip</samp>](## "ethernet_interfaces.[].mpls.ip") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ldp</samp>](## "ethernet_interfaces.[].mpls.ldp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interface</samp>](## "ethernet_interfaces.[].mpls.ldp.interface") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;igp_sync</samp>](## "ethernet_interfaces.[].mpls.ldp.igp_sync") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;lacp_timer</samp>](## "ethernet_interfaces.[].lacp_timer") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "ethernet_interfaces.[].lacp_timer.mode") | String |  |  | Valid Values:<br>- <code>fast</code><br>- <code>normal</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multiplier</samp>](## "ethernet_interfaces.[].lacp_timer.multiplier") | Integer |  |  | Min: 3<br>Max: 3000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;lacp_port_priority</samp>](## "ethernet_interfaces.[].lacp_port_priority") | Integer |  |  | Min: 0<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;transceiver</samp>](## "ethernet_interfaces.[].transceiver") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;media</samp>](## "ethernet_interfaces.[].transceiver.media") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;override</samp>](## "ethernet_interfaces.[].transceiver.media.override") | String |  |  |  | Transceiver type |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_proxy_arp</samp>](## "ethernet_interfaces.[].ip_proxy_arp") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;traffic_policy</samp>](## "ethernet_interfaces.[].traffic_policy") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;input</samp>](## "ethernet_interfaces.[].traffic_policy.input") | String |  |  |  | Ingress traffic policy |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;output</samp>](## "ethernet_interfaces.[].traffic_policy.output") | String |  |  |  | Egress traffic policy |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "ethernet_interfaces.[].bgp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;session_tracker</samp>](## "ethernet_interfaces.[].bgp.session_tracker") | String |  |  |  | Name of session tracker |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;peer</samp>](## "ethernet_interfaces.[].peer") | String |  |  |  | Key only used for documentation or validation purposes |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;peer_interface</samp>](## "ethernet_interfaces.[].peer_interface") | String |  |  |  | Key only used for documentation or validation purposes |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;peer_type</samp>](## "ethernet_interfaces.[].peer_type") | String |  |  |  | Key only used for documentation or validation purposes |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sflow</samp>](## "ethernet_interfaces.[].sflow") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable</samp>](## "ethernet_interfaces.[].sflow.enable") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;egress</samp>](## "ethernet_interfaces.[].sflow.egress") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable</samp>](## "ethernet_interfaces.[].sflow.egress.enable") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unmodified_enable</samp>](## "ethernet_interfaces.[].sflow.egress.unmodified_enable") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;port_profile</samp>](## "ethernet_interfaces.[].port_profile") | String |  |  |  | Key only used for documentation or validation purposes |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;uc_tx_queues</samp>](## "ethernet_interfaces.[].uc_tx_queues") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;id</samp>](## "ethernet_interfaces.[].uc_tx_queues.[].id") | Integer | Required, Unique |  |  | TX-Queue ID |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;random_detect</samp>](## "ethernet_interfaces.[].uc_tx_queues.[].random_detect") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ecn</samp>](## "ethernet_interfaces.[].uc_tx_queues.[].random_detect.ecn") | Dictionary |  |  |  | Explicit Congestion Notification |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;count</samp>](## "ethernet_interfaces.[].uc_tx_queues.[].random_detect.ecn.count") | Boolean |  |  |  | Enable counter for random-detect ECNs |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;threshold</samp>](## "ethernet_interfaces.[].uc_tx_queues.[].random_detect.ecn.threshold") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;units</samp>](## "ethernet_interfaces.[].uc_tx_queues.[].random_detect.ecn.threshold.units") | String | Required |  | Valid Values:<br>- <code>segments</code><br>- <code>bytes</code><br>- <code>kbytes</code><br>- <code>mbytes</code><br>- <code>milliseconds</code> | Indicate the units to be used for the threshold values |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;min</samp>](## "ethernet_interfaces.[].uc_tx_queues.[].random_detect.ecn.threshold.min") | Integer | Required |  | Min: 1<br>Max: 256000000 | Set the random-detect ECN minimum-threshold |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max</samp>](## "ethernet_interfaces.[].uc_tx_queues.[].random_detect.ecn.threshold.max") | Integer | Required |  | Min: 1<br>Max: 256000000 | Set the random-detect ECN maximum-threshold |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_probability</samp>](## "ethernet_interfaces.[].uc_tx_queues.[].random_detect.ecn.threshold.max_probability") | Integer |  |  | Min: 1<br>Max: 100 | Set the random-detect ECN max-mark-probability |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;weight</samp>](## "ethernet_interfaces.[].uc_tx_queues.[].random_detect.ecn.threshold.weight") | Integer |  |  | Min: 0<br>Max: 15 | Set the random-detect ECN weight |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;tx_queues</samp>](## "ethernet_interfaces.[].tx_queues") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;id</samp>](## "ethernet_interfaces.[].tx_queues.[].id") | Integer | Required, Unique |  |  | TX-Queue ID |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;random_detect</samp>](## "ethernet_interfaces.[].tx_queues.[].random_detect") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ecn</samp>](## "ethernet_interfaces.[].tx_queues.[].random_detect.ecn") | Dictionary |  |  |  | Explicit Congestion Notification |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;count</samp>](## "ethernet_interfaces.[].tx_queues.[].random_detect.ecn.count") | Boolean |  |  |  | Enable counter for random-detect ECNs |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;threshold</samp>](## "ethernet_interfaces.[].tx_queues.[].random_detect.ecn.threshold") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;units</samp>](## "ethernet_interfaces.[].tx_queues.[].random_detect.ecn.threshold.units") | String | Required |  | Valid Values:<br>- <code>segments</code><br>- <code>bytes</code><br>- <code>kbytes</code><br>- <code>mbytes</code><br>- <code>milliseconds</code> | Indicate the units to be used for the threshold values |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;min</samp>](## "ethernet_interfaces.[].tx_queues.[].random_detect.ecn.threshold.min") | Integer |  |  | Min: 1<br>Max: 256000000 | Set the random-detect ECN minimum-threshold |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max</samp>](## "ethernet_interfaces.[].tx_queues.[].random_detect.ecn.threshold.max") | Integer | Required |  | Min: 1<br>Max: 256000000 | Set the random-detect ECN maximum-threshold |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_probability</samp>](## "ethernet_interfaces.[].tx_queues.[].random_detect.ecn.threshold.max_probability") | Integer | Required |  | Min: 1<br>Max: 100 | Set the random-detect ECN max-mark-probability |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;weight</samp>](## "ethernet_interfaces.[].tx_queues.[].random_detect.ecn.threshold.weight") | Integer |  |  | Min: 0<br>Max: 15 | Set the random-detect ECN weight |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrrp_ids</samp>](## "ethernet_interfaces.[].vrrp_ids") | List, items: Dictionary |  |  |  | VRRP model. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;id</samp>](## "ethernet_interfaces.[].vrrp_ids.[].id") | Integer | Required, Unique |  |  | VRID |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority_level</samp>](## "ethernet_interfaces.[].vrrp_ids.[].priority_level") | Integer |  |  | Min: 1<br>Max: 254 | Instance priority |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;advertisement</samp>](## "ethernet_interfaces.[].vrrp_ids.[].advertisement") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "ethernet_interfaces.[].vrrp_ids.[].advertisement.interval") | Integer |  |  | Min: 1<br>Max: 255 | Interval in seconds |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;preempt</samp>](## "ethernet_interfaces.[].vrrp_ids.[].preempt") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "ethernet_interfaces.[].vrrp_ids.[].preempt.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;delay</samp>](## "ethernet_interfaces.[].vrrp_ids.[].preempt.delay") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;minimum</samp>](## "ethernet_interfaces.[].vrrp_ids.[].preempt.delay.minimum") | Integer |  |  | Min: 0<br>Max: 3600 | Minimum preempt delay in seconds |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reload</samp>](## "ethernet_interfaces.[].vrrp_ids.[].preempt.delay.reload") | Integer |  |  | Min: 0<br>Max: 3600 | Reload preempt delay in seconds |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timers</samp>](## "ethernet_interfaces.[].vrrp_ids.[].timers") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;delay</samp>](## "ethernet_interfaces.[].vrrp_ids.[].timers.delay") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reload</samp>](## "ethernet_interfaces.[].vrrp_ids.[].timers.delay.reload") | Integer |  |  | Min: 0<br>Max: 3600 | Delay after reload in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tracked_object</samp>](## "ethernet_interfaces.[].vrrp_ids.[].tracked_object") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "ethernet_interfaces.[].vrrp_ids.[].tracked_object.[].name") | String | Required, Unique |  |  | Tracked object name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;decrement</samp>](## "ethernet_interfaces.[].vrrp_ids.[].tracked_object.[].decrement") | Integer |  |  | Min: 1<br>Max: 254 | Decrement VRRP priority by 1-254 |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "ethernet_interfaces.[].vrrp_ids.[].tracked_object.[].shutdown") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp>](## "ethernet_interfaces.[].vrrp_ids.[].ipv4") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address</samp>](## "ethernet_interfaces.[].vrrp_ids.[].ipv4.address") | String | Required |  |  | Virtual IPv4 address |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "ethernet_interfaces.[].vrrp_ids.[].ipv4.version") | Integer |  |  | Valid Values:<br>- <code>2</code><br>- <code>3</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6</samp>](## "ethernet_interfaces.[].vrrp_ids.[].ipv6") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address</samp>](## "ethernet_interfaces.[].vrrp_ids.[].ipv6.address") | String | Required |  |  | Virtual IPv6 address |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;eos_cli</samp>](## "ethernet_interfaces.[].eos_cli") | String |  |  |  | Multiline EOS CLI rendered directly on the ethernet interface in the final EOS configuration |

=== "YAML"

    ```yaml
    ethernet_interfaces:
      - name: <str; required; unique>
        description: <str>
        shutdown: <bool>

        # Interval in seconds for updating interface counters"
        load_interval: <int; 0-600>

        # Speed should be set in the format `<interface_speed>` or `forced <interface_speed>` or `auto <interface_speed>`.
        speed: <str>
        mtu: <int; 68-65535>

        # "l2_mtu" should only be defined for platforms supporting the "l2 mtu" CLI
        l2_mtu: <int; 68-65535>

        # "l2_mru" should only be defined for platforms supporting the "l2 mru" CLI
        l2_mru: <int; 68-65535>

        # List of switchport vlans as string
        # For a trunk port this would be a range like "1-200,300"
        # For an access port this would be a single vlan "123"
        vlans: <str>
        native_vlan: <int>

        # If setting both native_vlan and native_vlan_tag, native_vlan_tag takes precedence
        native_vlan_tag: <bool>
        mode: <str; "access" | "dot1q-tunnel" | "trunk" | "trunk phone">
        phone:
          trunk: <str; "tagged" | "tagged phone" | "untagged" | "untagged phone">
          vlan: <int; 1-4094>
        l2_protocol:

          # Vlan tag to configure on sub-interface
          encapsulation_dot1q_vlan: <int>

          # L2 protocol forwarding profile
          forwarding_profile: <str>
        trunk_groups:
          - <str>

        # l3dot1q and l2dot1q are used for sub-interfaces. The parent interface should be defined as routed.
        # Interface will not be listed in device documentation, unless "type" is set.
        type: <str; "routed" | "switched" | "l3dot1q" | "l2dot1q" | "port-channel-member">
        snmp_trap_link_change: <bool>
        address_locking:

          # Enable address locking for IPv4
          ipv4: <bool>

          # Enable address locking for IPv6
          ipv6: <bool>
        flowcontrol:
          received: <str; "desired" | "on" | "off">

        # VRF name
        vrf: <str>
        flow_tracker:

          # Sampled flow tracker name.
          sampled: <str>

          # Hardware flow tracker name.
          hardware: <str>
        error_correction_encoding:
          enabled: <bool; default=True>
          fire_code: <bool>
          reed_solomon: <bool>
        link_tracking_groups:

            # Group name
          - name: <str; required; unique>
            direction: <str; "upstream" | "downstream">
        evpn_ethernet_segment:

          # EVPN Ethernet Segment Identifier (Type 1 format)
          identifier: <str>
          redundancy: <str; "all-active" | "single-active">
          designated_forwarder_election:
            algorithm: <str; "modulus" | "preference">

            # Preference_value is only used when "algorithm" is "preference"
            preference_value: <int; 0-65535>

            # Dont_preempt is only used when "algorithm" is "preference"
            dont_preempt: <bool>
            hold_time: <int>
            subsequent_hold_time: <int>
            candidate_reachability_required: <bool>
          mpls:
            shared_index: <int; 1-1024>
            tunnel_flood_filter_time: <int>

          # EVPN Route Target for ESI with format xx:xx:xx:xx:xx:xx
          route_target: <str>

        # VLAN tag to configure on sub-interface
        encapsulation_dot1q_vlan: <int>
        encapsulation_vlan:
          client:
            dot1q:

              # Client VLAN ID
              vlan: <int>

              # Client Outer VLAN ID
              outer: <int>

              # Client Inner VLAN ID
              inner: <int>
            unmatched: <bool>

          # Network encapsulations are all optional and skipped if using client unmatched
          network:
            dot1q:

              # Network VLAN ID
              vlan: <int>

              # Network outer VLAN ID
              outer: <int>

              # Network inner VLAN ID
              inner: <int>
            client: <bool>
        vlan_id: <int; 1-4094>

        # IPv4 address/mask or "dhcp"
        ip_address: <str>
        ip_address_secondaries:
          - <str>

        # Install default-route obtained via DHCP
        dhcp_client_accept_default_route: <bool>

        # Enable IPv4 DHCP server.
        dhcp_server_ipv4: <bool>

        # Enable IPv6 DHCP server.
        dhcp_server_ipv6: <bool>
        ip_helpers:
          - ip_helper: <str; required; unique>

            # Source interface name
            source_interface: <str>

            # VRF name
            vrf: <str>
        ip_nat:

          # NAT interface profile.
          service_profile: <str>
          destination:
            dynamic:
              - access_list: <str; required; unique>
                comment: <str>
                pool_name: <str; required>
                priority: <int; 0-4294967295>
            static:

                # 'access_list' and 'group' are mutual exclusive
              - access_list: <str>
                comment: <str>

                # Egress or ingress can be the default. This depends on source/destination, EOS version, and hardware platform.
                # EOS might remove this keyword in the configuration. So, check the configuration on targeted HW/SW.
                direction: <str; "egress" | "ingress">

                # 'access_list' and 'group' are mutual exclusive
                group: <int; 1-65535>

                # IPv4 address
                original_ip: <str; required; unique>
                original_port: <int; 1-65535>
                priority: <int; 0-4294967295>
                protocol: <str; "udp" | "tcp">

                # IPv4 address
                translated_ip: <str; required>

                # requires 'original_port'
                translated_port: <int; 1-65535>
          source:
            dynamic:
              - access_list: <str; required; unique>
                comment: <str>
                nat_type: <str; "overload" | "pool" | "pool-address-only" | "pool-full-cone"; required>

                # required if 'nat_type' is pool, pool-address-only or pool-full-cone
                # ignored if 'nat_type' is overload
                pool_name: <str>
                priority: <int; 0-4294967295>
            static:

                # 'access_list' and 'group' are mutual exclusive
              - access_list: <str>
                comment: <str>

                # Egress or ingress can be the default. This depends on source/destination, EOS version, and hardware platform.
                # EOS might remove this keyword in the configuration. So, check the configuration on targeted HW/SW.
                direction: <str; "egress" | "ingress">

                # 'access_list' and 'group' are mutual exclusive
                group: <int; 1-65535>

                # IPv4 address
                original_ip: <str; required; unique>
                original_port: <int; 1-65535>
                priority: <int; 0-4294967295>
                protocol: <str; "udp" | "tcp">

                # IPv4 address
                translated_ip: <str; required>

                # requires 'original_port'
                translated_port: <int; 1-65535>
        ipv6_enable: <bool>
        ipv6_address: <str>

        # Link local IPv6 address/mask
        ipv6_address_link_local: <str>
        ipv6_nd_ra_disabled: <bool>
        ipv6_nd_managed_config_flag: <bool>
        ipv6_nd_prefixes:
          - ipv6_prefix: <str; required; unique>

            # Infinite or lifetime in seconds
            valid_lifetime: <str>

            # Infinite or lifetime in seconds
            preferred_lifetime: <str>
            no_autoconfig_flag: <bool>
        ipv6_dhcp_relay_destinations:

            # DHCP server's IPv6 address
          - address: <str; required; unique>
            vrf: <str>

            # Local interface to communicate with DHCP server - mutually exclusive to source_address
            local_interface: <str>

            # Source IPv6 address to communicate with DHCP server - mutually exclusive to local_interface
            source_address: <str>

            # Override the default link address specified in the relayed DHCP packet
            link_address: <str>

        # Access list name
        access_group_in: <str>

        # Access list name
        access_group_out: <str>

        # IPv6 access list name
        ipv6_access_group_in: <str>

        # IPv6 access list name
        ipv6_access_group_out: <str>

        # MAC access list name
        mac_access_group_in: <str>

        # MAC access list name
        mac_access_group_out: <str>

        # Boundaries can be either 1 ACL or a list of multicast IP address_range(s)/prefix but not combination of both
        multicast:
          ipv4:
            boundaries:

                # ACL name or multicast IP subnet
              - boundary: <str>
                out: <bool>
            static: <bool>
          ipv6:
            boundaries:

                # ACL name or multicast IP subnet
              - boundary: <str>
            static: <bool>
        ospf_network_point_to_point: <bool>
        ospf_area: <str>
        ospf_cost: <int>
        ospf_authentication: <str; "none" | "simple" | "message-digest">

        # Encrypted password - only type 7 supported
        ospf_authentication_key: <str>
        ospf_message_digest_keys:
          - id: <int; required; unique>
            hash_algorithm: <str; "md5" | "sha1" | "sha256" | "sha384" | "sha512">

            # Encrypted password - only type 7 supported
            key: <str>
        pim:
          ipv4:
            dr_priority: <int; 0-429467295>
            sparse_mode: <bool>
        mac_security:
          profile: <str>
        channel_group:
          id: <int>
          mode: <str; "on" | "active" | "passive">

        # ISIS instance
        isis_enable: <str>
        isis_passive: <bool>
        isis_metric: <int>
        isis_network_point_to_point: <bool>
        isis_circuit_type: <str; "level-1-2" | "level-1" | "level-2">
        isis_hello_padding: <bool>
        isis_authentication_mode: <str; "text" | "md5">

        # Type-7 encrypted password
        isis_authentication_key: <str>
        poe:

          # Disable PoE on a POE capable port. PoE is enabled on all ports that support it by default in EOS.
          disabled: <bool; default=False>

          # Prioritize a port's power in the event that one of the switch's power supplies loses power
          priority: <str; "critical" | "high" | "medium" | "low">

          # Set the PoE power behavior for a PoE port when the system is rebooted
          reboot:

            # PoE action for interface
            action: <str; "maintain" | "power-off">

          # Set the PoE power behavior for a PoE port when the port goes down
          link_down:

            # PoE action for interface
            action: <str; "maintain" | "power-off">

            # Number of seconds to delay shutting the power off after a link down event occurs. Default value is 5 seconds in EOS.
            power_off_delay: <int; 1-86400>

          # Set the PoE power behavior for a PoE port when the port is admin down
          shutdown:

            # PoE action for interface
            action: <str; "maintain" | "power-off">

          # Override the hardware-negotiated power limit using either wattage or a power class. Note that if using a power class, AVD will automatically convert the class value to the wattage value corresponding to that power class.
          limit:
            class: <int; 0-8>
            watts: <str>

            # Set to ignore hardware classification
            fixed: <bool>

          # Disable to prevent port from negotiating power with powered devices over LLDP. Enabled by default in EOS.
          negotiation_lldp: <bool>

          # Allow a subset of legacy devices to work with the PoE switch. Disabled by default in EOS because it can cause false positive detections.
          legacy_detect: <bool>
        ptp:
          enable: <bool>
          announce:
            interval: <int>
            timeout: <int>
          delay_req: <int>
          delay_mechanism: <str; "e2e" | "p2p">
          sync_message:
            interval: <int>
          role: <str; "master" | "dynamic">

          # VLAN can be 'all' or list of vlans as string
          vlan: <str>
          transport: <str; "ipv4" | "ipv6" | "layer2">

        # Interface profile
        profile: <str>
        storm_control:
          all:

            # Configure maximum storm-control level
            level: <str>

            # Optional field and is hardware dependent
            unit: <str; "percent" | "pps"; default="percent">
          broadcast:

            # Configure maximum storm-control level
            level: <str>

            # Optional field and is hardware dependent
            unit: <str; "percent" | "pps"; default="percent">
          multicast:

            # Configure maximum storm-control level
            level: <str>

            # Optional field and is hardware dependent
            unit: <str; "percent" | "pps"; default="percent">
          unknown_unicast:

            # Configure maximum storm-control level
            level: <str>

            # Optional field and is hardware dependent
            unit: <str; "percent" | "pps"; default="percent">
        logging:
          event:
            link_status: <bool>
            congestion_drops: <bool>
            spanning_tree: <bool>
            storm_control_discards: <bool>
        lldp:
          transmit: <bool>
          receive: <bool>

          # ZTP vlan number
          ztp_vlan: <int>
        trunk_private_vlan_secondary: <bool>

        # List of vlans as string
        pvlan_mapping: <str>
        vlan_translations:

            # List of vlans as string (only one vlan if direction is "both")
          - from: <str>

            # VLAN ID
            to: <int>
            direction: <str; "in" | "out" | "both"; default="both">
        dot1x:
          port_control: <str; "auto" | "force-authorized" | "force-unauthorized">
          port_control_force_authorized_phone: <bool>
          reauthentication: <bool>
          pae:
            mode: <str; "authenticator">
          authentication_failure:
            action: <str; "allow" | "drop">
            allow_vlan: <int; 1-4094>
          host_mode:
            mode: <str; "multi-host" | "single-host">
            multi_host_authenticated: <bool>
          mac_based_authentication:
            enabled: <bool>
            always: <bool>
            host_mode_common: <bool>
          timeout:
            idle_host: <int; 10-65535>
            quiet_period: <int; 1-65535>

            # Value can be 60-4294967295 or 'server'
            reauth_period: <str>
            reauth_timeout_ignore: <bool>
            tx_period: <int; 1-65535>
          reauthorization_request_limit: <int; 1-10>
          unauthorized:
            access_vlan_membership_egress: <bool>
            native_vlan_membership_egress: <bool>
          eapol:
            disabled: <bool>
            authentication_failure_fallback_mba:
              enabled: <bool>
              timeout: <int; 0-65535>

        # QOS profile
        service_profile: <str>
        shape:

          # Rate in kbps, pps or percent
          # Supported options are platform dependent
          # Examples:
          # - "5000 kbps"
          # - "1000 pps"
          # - "20 percent"
          rate: <str>
        qos:
          trust: <str; "dscp" | "cos" | "disabled">

          # DSCP value
          dscp: <int>

          # COS value
          cos: <int>
        spanning_tree_bpdufilter: <str; "enabled" | "disabled" | "True" | "False" | "true" | "false">
        spanning_tree_bpduguard: <str; "enabled" | "disabled" | "True" | "False" | "true" | "false">
        spanning_tree_guard: <str; "loop" | "root" | "disabled">
        spanning_tree_portfast: <str; "edge" | "network">
        vmtracer: <bool>
        priority_flow_control:
          enabled: <bool>
          priorities:
            - priority: <int; 0-7; required; unique>
              no_drop: <bool>
        bfd:
          echo: <bool>

          # Interval in milliseconds
          interval: <int>

          # Rate in milliseconds
          min_rx: <int>
          multiplier: <int; 3-50>
        service_policy:
          pbr:

            # Policy Based Routing Policy-map name
            input: <str>
          qos:

            # Quality of Service Policy-map name
            input: <str; required>
        mpls:
          ip: <bool>
          ldp:
            interface: <bool>
            igp_sync: <bool>
        lacp_timer:
          mode: <str; "fast" | "normal">
          multiplier: <int; 3-3000>
        lacp_port_priority: <int; 0-65535>
        transceiver:
          media:

            # Transceiver type
            override: <str>
        ip_proxy_arp: <bool>
        traffic_policy:

          # Ingress traffic policy
          input: <str>

          # Egress traffic policy
          output: <str>
        bgp:

          # Name of session tracker
          session_tracker: <str>

        # Key only used for documentation or validation purposes
        peer: <str>

        # Key only used for documentation or validation purposes
        peer_interface: <str>

        # Key only used for documentation or validation purposes
        peer_type: <str>
        sflow:
          enable: <bool>
          egress:
            enable: <bool>
            unmodified_enable: <bool>

        # Key only used for documentation or validation purposes
        port_profile: <str>
        uc_tx_queues:

            # TX-Queue ID
          - id: <int; required; unique>
            random_detect:

              # Explicit Congestion Notification
              ecn:

                # Enable counter for random-detect ECNs
                count: <bool>
                threshold:

                  # Indicate the units to be used for the threshold values
                  units: <str; "segments" | "bytes" | "kbytes" | "mbytes" | "milliseconds"; required>

                  # Set the random-detect ECN minimum-threshold
                  min: <int; 1-256000000; required>

                  # Set the random-detect ECN maximum-threshold
                  max: <int; 1-256000000; required>

                  # Set the random-detect ECN max-mark-probability
                  max_probability: <int; 1-100>

                  # Set the random-detect ECN weight
                  weight: <int; 0-15>
        tx_queues:

            # TX-Queue ID
          - id: <int; required; unique>
            random_detect:

              # Explicit Congestion Notification
              ecn:

                # Enable counter for random-detect ECNs
                count: <bool>
                threshold:

                  # Indicate the units to be used for the threshold values
                  units: <str; "segments" | "bytes" | "kbytes" | "mbytes" | "milliseconds"; required>

                  # Set the random-detect ECN minimum-threshold
                  min: <int; 1-256000000>

                  # Set the random-detect ECN maximum-threshold
                  max: <int; 1-256000000; required>

                  # Set the random-detect ECN max-mark-probability
                  max_probability: <int; 1-100; required>

                  # Set the random-detect ECN weight
                  weight: <int; 0-15>

        # VRRP model.
        vrrp_ids:

            # VRID
          - id: <int; required; unique>

            # Instance priority
            priority_level: <int; 1-254>
            advertisement:

              # Interval in seconds
              interval: <int; 1-255>
            preempt:
              enabled: <bool; required>
              delay:

                # Minimum preempt delay in seconds
                minimum: <int; 0-3600>

                # Reload preempt delay in seconds
                reload: <int; 0-3600>
            timers:
              delay:

                # Delay after reload in seconds.
                reload: <int; 0-3600>
            tracked_object:

                # Tracked object name
              - name: <str; required; unique>

                # Decrement VRRP priority by 1-254
                decrement: <int; 1-254>
                shutdown: <bool>
            ipv4:

              # Virtual IPv4 address
              address: <str; required>
              version: <int; 2 | 3>
            ipv6:

              # Virtual IPv6 address
              address: <str; required>

        # Multiline EOS CLI rendered directly on the ethernet interface in the final EOS configuration
        eos_cli: <str>
    ```
