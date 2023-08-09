<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>port_channel_interfaces</samp>](## "port_channel_interfaces") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- name</samp>](## "port_channel_interfaces.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "port_channel_interfaces.[].description") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;logging</samp>](## "port_channel_interfaces.[].logging") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;event</samp>](## "port_channel_interfaces.[].logging.event") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;link_status</samp>](## "port_channel_interfaces.[].logging.event.link_status") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "port_channel_interfaces.[].shutdown") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;l2_mtu</samp>](## "port_channel_interfaces.[].l2_mtu") | Integer |  |  |  | "l2_mtu" should only be defined for platforms supporting the "l2 mtu" CLI<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vlans</samp>](## "port_channel_interfaces.[].vlans") | String |  |  |  | List of switchport vlans as string<br>For a trunk port this would be a range like "1-200,300"<br>For an access port this would be a single vlan "123"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;snmp_trap_link_change</samp>](## "port_channel_interfaces.[].snmp_trap_link_change") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "port_channel_interfaces.[].type") | String |  |  | Valid Values:<br>- routed<br>- switched<br>- l3dot1q<br>- l2dot1q | l3dot1q and l2dot1q are used for sub-interfaces. The parent interface should be defined as routed.<br>Interface will not be listed in device documentation, unless "type" is set.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;encapsulation_dot1q_vlan</samp>](## "port_channel_interfaces.[].encapsulation_dot1q_vlan") | Integer |  |  |  | VLAN tag to configure on sub-interface |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "port_channel_interfaces.[].vrf") | String |  |  |  | VRF name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;encapsulation_vlan</samp>](## "port_channel_interfaces.[].encapsulation_vlan") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;client</samp>](## "port_channel_interfaces.[].encapsulation_vlan.client") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dot1q</samp>](## "port_channel_interfaces.[].encapsulation_vlan.client.dot1q") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan</samp>](## "port_channel_interfaces.[].encapsulation_vlan.client.dot1q.vlan") | Integer |  |  |  | Client VLAN ID |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;outer</samp>](## "port_channel_interfaces.[].encapsulation_vlan.client.dot1q.outer") | Integer |  |  |  | Client Outer VLAN ID |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inner</samp>](## "port_channel_interfaces.[].encapsulation_vlan.client.dot1q.inner") | Integer |  |  |  | Client Inner VLAN ID |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unmatched</samp>](## "port_channel_interfaces.[].encapsulation_vlan.client.unmatched") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;network</samp>](## "port_channel_interfaces.[].encapsulation_vlan.network") | Dictionary |  |  |  | Network encapsulation are all optional, and skipped if using client unmatched |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dot1q</samp>](## "port_channel_interfaces.[].encapsulation_vlan.network.dot1q") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan</samp>](## "port_channel_interfaces.[].encapsulation_vlan.network.dot1q.vlan") | Integer |  |  |  | Network VLAN ID |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;outer</samp>](## "port_channel_interfaces.[].encapsulation_vlan.network.dot1q.outer") | Integer |  |  |  | Network Outer VLAN ID |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inner</samp>](## "port_channel_interfaces.[].encapsulation_vlan.network.dot1q.inner") | Integer |  |  |  | Network Inner VLAN ID |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;client</samp>](## "port_channel_interfaces.[].encapsulation_vlan.network.client") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vlan_id</samp>](## "port_channel_interfaces.[].vlan_id") | Integer |  |  | Min: 1<br>Max: 4094 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "port_channel_interfaces.[].mode") | String |  |  | Valid Values:<br>- access<br>- dot1q-tunnel<br>- trunk<br>- trunk phone |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;native_vlan</samp>](## "port_channel_interfaces.[].native_vlan") | Integer |  |  |  | If setting both native_vlan and native_vlan_tag, native_vlan_tag takes precedence |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;native_vlan_tag</samp>](## "port_channel_interfaces.[].native_vlan_tag") | Boolean |  | `False` |  | If setting both native_vlan and native_vlan_tag, native_vlan_tag takes precedence |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;link_tracking_groups</samp>](## "port_channel_interfaces.[].link_tracking_groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "port_channel_interfaces.[].link_tracking_groups.[].name") | String | Required, Unique |  |  | Group name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction</samp>](## "port_channel_interfaces.[].link_tracking_groups.[].direction") | String |  |  | Valid Values:<br>- upstream<br>- downstream |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;phone</samp>](## "port_channel_interfaces.[].phone") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;trunk</samp>](## "port_channel_interfaces.[].phone.trunk") | String |  |  | Valid Values:<br>- tagged<br>- untagged |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan</samp>](## "port_channel_interfaces.[].phone.vlan") | Integer |  |  | Min: 1<br>Max: 4094 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;l2_protocol</samp>](## "port_channel_interfaces.[].l2_protocol") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;encapsulation_dot1q_vlan</samp>](## "port_channel_interfaces.[].l2_protocol.encapsulation_dot1q_vlan") | Integer |  |  |  | Vlan tag to configure on sub-interface |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;forwarding_profile</samp>](## "port_channel_interfaces.[].l2_protocol.forwarding_profile") | String |  |  |  | L2 protocol forwarding profile |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp>](## "port_channel_interfaces.[].mtu") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag</samp>](## "port_channel_interfaces.[].mlag") | Integer |  |  | Min: 1<br>Max: 2000 | MLAG ID |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;trunk_groups</samp>](## "port_channel_interfaces.[].trunk_groups") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "port_channel_interfaces.[].trunk_groups.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;lacp_fallback_timeout</samp>](## "port_channel_interfaces.[].lacp_fallback_timeout") | Integer |  | `90` | Min: 0<br>Max: 300 | Timeout in seconds |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;lacp_fallback_mode</samp>](## "port_channel_interfaces.[].lacp_fallback_mode") | String |  |  | Valid Values:<br>- individual<br>- static |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;qos</samp>](## "port_channel_interfaces.[].qos") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;trust</samp>](## "port_channel_interfaces.[].qos.trust") | String |  |  | Valid Values:<br>- dscp<br>- cos<br>- disabled |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dscp</samp>](## "port_channel_interfaces.[].qos.dscp") | Integer |  |  |  | DSCP value |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cos</samp>](## "port_channel_interfaces.[].qos.cos") | Integer |  |  |  | COS value |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp>](## "port_channel_interfaces.[].bfd") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;echo</samp>](## "port_channel_interfaces.[].bfd.echo") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "port_channel_interfaces.[].bfd.interval") | Integer |  |  |  | Interval in milliseconds |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;min_rx</samp>](## "port_channel_interfaces.[].bfd.min_rx") | Integer |  |  |  | Rate in milliseconds |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multiplier</samp>](## "port_channel_interfaces.[].bfd.multiplier") | Integer |  |  | Min: 3<br>Max: 50 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;service_policy</samp>](## "port_channel_interfaces.[].service_policy") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pbr</samp>](## "port_channel_interfaces.[].service_policy.pbr") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;input</samp>](## "port_channel_interfaces.[].service_policy.pbr.input") | String |  |  |  | Policy Based Routing Policy-map name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;qos</samp>](## "port_channel_interfaces.[].service_policy.qos") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;input</samp>](## "port_channel_interfaces.[].service_policy.qos.input") | String | Required |  |  | Quality of Service Policy-map name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mpls</samp>](## "port_channel_interfaces.[].mpls") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip</samp>](## "port_channel_interfaces.[].mpls.ip") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ldp</samp>](## "port_channel_interfaces.[].mpls.ldp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interface</samp>](## "port_channel_interfaces.[].mpls.ldp.interface") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;igp_sync</samp>](## "port_channel_interfaces.[].mpls.ldp.igp_sync") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;trunk_private_vlan_secondary</samp>](## "port_channel_interfaces.[].trunk_private_vlan_secondary") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;pvlan_mapping</samp>](## "port_channel_interfaces.[].pvlan_mapping") | String |  |  |  | List of vlans as string |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vlan_translations</samp>](## "port_channel_interfaces.[].vlan_translations") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- from</samp>](## "port_channel_interfaces.[].vlan_translations.[].from") | String |  |  |  | List of vlans as string (only one vlan if direction is "both") |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;to</samp>](## "port_channel_interfaces.[].vlan_translations.[].to") | Integer |  |  |  | VLAN ID |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction</samp>](## "port_channel_interfaces.[].vlan_translations.[].direction") | String |  | `both` | Valid Values:<br>- in<br>- out<br>- both |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;shape</samp>](## "port_channel_interfaces.[].shape") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rate</samp>](## "port_channel_interfaces.[].shape.rate") | String |  |  |  | Rate in kbps, pps or percent<br>Supported options are platform dependent<br>Examples:<br>- "5000 kbps"<br>- "1000 pps"<br>- "20 percent"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;storm_control</samp>](## "port_channel_interfaces.[].storm_control") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;all</samp>](## "port_channel_interfaces.[].storm_control.all") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp>](## "port_channel_interfaces.[].storm_control.all.level") | String |  |  |  | Configure maximum storm-control level |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp>](## "port_channel_interfaces.[].storm_control.all.unit") | String |  | `percent` | Valid Values:<br>- percent<br>- pps | Optional field and is hardware dependant |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;broadcast</samp>](## "port_channel_interfaces.[].storm_control.broadcast") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp>](## "port_channel_interfaces.[].storm_control.broadcast.level") | String |  |  |  | Configure maximum storm-control level |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp>](## "port_channel_interfaces.[].storm_control.broadcast.unit") | String |  | `percent` | Valid Values:<br>- percent<br>- pps | Optional field and is hardware dependant |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multicast</samp>](## "port_channel_interfaces.[].storm_control.multicast") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp>](## "port_channel_interfaces.[].storm_control.multicast.level") | String |  |  |  | Configure maximum storm-control level |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp>](## "port_channel_interfaces.[].storm_control.multicast.unit") | String |  | `percent` | Valid Values:<br>- percent<br>- pps | Optional field and is hardware dependant |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unknown_unicast</samp>](## "port_channel_interfaces.[].storm_control.unknown_unicast") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp>](## "port_channel_interfaces.[].storm_control.unknown_unicast.level") | String |  |  |  | Configure maximum storm-control level |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp>](## "port_channel_interfaces.[].storm_control.unknown_unicast.unit") | String |  | `percent` | Valid Values:<br>- percent<br>- pps | Optional field and is hardware dependant |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_proxy_arp</samp>](## "port_channel_interfaces.[].ip_proxy_arp") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_enable</samp>](## "port_channel_interfaces.[].isis_enable") | String |  |  |  | ISIS instance |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_passive</samp>](## "port_channel_interfaces.[].isis_passive") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_metric</samp>](## "port_channel_interfaces.[].isis_metric") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_network_point_to_point</samp>](## "port_channel_interfaces.[].isis_network_point_to_point") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_circuit_type</samp>](## "port_channel_interfaces.[].isis_circuit_type") | String |  |  | Valid Values:<br>- level-1-2<br>- level-1<br>- level-2 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_hello_padding</samp>](## "port_channel_interfaces.[].isis_hello_padding") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_authentication_mode</samp>](## "port_channel_interfaces.[].isis_authentication_mode") | String |  |  | Valid Values:<br>- text<br>- md5 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_authentication_key</samp>](## "port_channel_interfaces.[].isis_authentication_key") | String |  |  |  | Type-7 encrypted password |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;traffic_policy</samp>](## "port_channel_interfaces.[].traffic_policy") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;input</samp>](## "port_channel_interfaces.[].traffic_policy.input") | String |  |  |  | Ingress traffic policy |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;output</samp>](## "port_channel_interfaces.[].traffic_policy.output") | String |  |  |  | Egress traffic policy |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;evpn_ethernet_segment</samp>](## "port_channel_interfaces.[].evpn_ethernet_segment") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;identifier</samp>](## "port_channel_interfaces.[].evpn_ethernet_segment.identifier") | String |  |  |  | EVPN Ethernet Segment Identifier (Type 1 format) |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;redundancy</samp>](## "port_channel_interfaces.[].evpn_ethernet_segment.redundancy") | String |  |  | Valid Values:<br>- all-active<br>- single-active |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;designated_forwarder_election</samp>](## "port_channel_interfaces.[].evpn_ethernet_segment.designated_forwarder_election") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;algorithm</samp>](## "port_channel_interfaces.[].evpn_ethernet_segment.designated_forwarder_election.algorithm") | String |  |  | Valid Values:<br>- modulus<br>- preference |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;preference_value</samp>](## "port_channel_interfaces.[].evpn_ethernet_segment.designated_forwarder_election.preference_value") | Integer |  |  | Min: 0<br>Max: 65535 | Preference_value is only used when "algorithm" is "preference" |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dont_preempt</samp>](## "port_channel_interfaces.[].evpn_ethernet_segment.designated_forwarder_election.dont_preempt") | Boolean |  | `False` |  | Dont_preempt is only used when "algorithm" is "preference" |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hold_time</samp>](## "port_channel_interfaces.[].evpn_ethernet_segment.designated_forwarder_election.hold_time") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;subsequent_hold_time</samp>](## "port_channel_interfaces.[].evpn_ethernet_segment.designated_forwarder_election.subsequent_hold_time") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;candidate_reachability_required</samp>](## "port_channel_interfaces.[].evpn_ethernet_segment.designated_forwarder_election.candidate_reachability_required") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls</samp>](## "port_channel_interfaces.[].evpn_ethernet_segment.mpls") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shared_index</samp>](## "port_channel_interfaces.[].evpn_ethernet_segment.mpls.shared_index") | Integer |  |  | Min: 1<br>Max: 1024 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tunnel_flood_filter_time</samp>](## "port_channel_interfaces.[].evpn_ethernet_segment.mpls.tunnel_flood_filter_time") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_target</samp>](## "port_channel_interfaces.[].evpn_ethernet_segment.route_target") | String |  |  |  | EVPN Route Target for ESI with format xx:xx:xx:xx:xx:xx |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;esi</samp>](## "port_channel_interfaces.[].esi") <span style="color:red">deprecated</span> | String |  |  |  | EVPN Ethernet Segment Identifier (Type 1 format)<br>If both "esi" and "evpn_ethernet_segment.identifier" are defined, the new variable takes precedence<br><span style="color:red">This key is deprecated. Support will be removed in AVD version 5.0.0. Use <samp>evpn_ethernet_segment.identifier</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;rt</samp>](## "port_channel_interfaces.[].rt") <span style="color:red">deprecated</span> | String |  |  |  | EVPN Route Target for ESI with format xx:xx:xx:xx:xx:xx<br>If both "rt" and "evpn_ethernet_segment.route_target" are defined, the new variable takes precedence<br><span style="color:red">This key is deprecated. Support will be removed in AVD version 5.0.0. Use <samp>evpn_ethernet_segment.route_target</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;lacp_id</samp>](## "port_channel_interfaces.[].lacp_id") | String |  |  |  | LACP ID with format xxxx.xxxx.xxxx |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_bpdufilter</samp>](## "port_channel_interfaces.[].spanning_tree_bpdufilter") | String |  |  | Valid Values:<br>- enabled<br>- disabled<br>- True<br>- False<br>- true<br>- false |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_bpduguard</samp>](## "port_channel_interfaces.[].spanning_tree_bpduguard") | String |  |  | Valid Values:<br>- enabled<br>- disabled<br>- True<br>- False<br>- true<br>- false |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_guard</samp>](## "port_channel_interfaces.[].spanning_tree_guard") | String |  |  | Valid Values:<br>- loop<br>- root<br>- disabled |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_portfast</samp>](## "port_channel_interfaces.[].spanning_tree_portfast") | String |  |  | Valid Values:<br>- edge<br>- network |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vmtracer</samp>](## "port_channel_interfaces.[].vmtracer") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ptp</samp>](## "port_channel_interfaces.[].ptp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable</samp>](## "port_channel_interfaces.[].ptp.enable") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;announce</samp>](## "port_channel_interfaces.[].ptp.announce") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "port_channel_interfaces.[].ptp.announce.interval") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timeout</samp>](## "port_channel_interfaces.[].ptp.announce.timeout") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;delay_req</samp>](## "port_channel_interfaces.[].ptp.delay_req") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;delay_mechanism</samp>](## "port_channel_interfaces.[].ptp.delay_mechanism") | String |  |  | Valid Values:<br>- e2e<br>- p2p |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sync_message</samp>](## "port_channel_interfaces.[].ptp.sync_message") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "port_channel_interfaces.[].ptp.sync_message.interval") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;role</samp>](## "port_channel_interfaces.[].ptp.role") | String |  |  | Valid Values:<br>- master<br>- dynamic |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan</samp>](## "port_channel_interfaces.[].ptp.vlan") | String |  |  |  | VLAN can be 'all' or list of vlans as string |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;transport</samp>](## "port_channel_interfaces.[].ptp.transport") | String |  |  | Valid Values:<br>- ipv4<br>- ipv6<br>- layer2 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "port_channel_interfaces.[].ip_address") | String |  |  |  | IPv4 address/mask |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_nat</samp>](## "port_channel_interfaces.[].ip_nat") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;destination</samp>](## "port_channel_interfaces.[].ip_nat.destination") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dynamic</samp>](## "port_channel_interfaces.[].ip_nat.destination.dynamic") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- access_list</samp>](## "port_channel_interfaces.[].ip_nat.destination.dynamic.[].access_list") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;comment</samp>](## "port_channel_interfaces.[].ip_nat.destination.dynamic.[].comment") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pool_name</samp>](## "port_channel_interfaces.[].ip_nat.destination.dynamic.[].pool_name") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "port_channel_interfaces.[].ip_nat.destination.dynamic.[].priority") | Integer |  |  | Min: 0<br>Max: 4294967295 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;static</samp>](## "port_channel_interfaces.[].ip_nat.destination.static") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- access_list</samp>](## "port_channel_interfaces.[].ip_nat.destination.static.[].access_list") | String |  |  |  | 'access_list' and 'group' are mutual exclusive |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;comment</samp>](## "port_channel_interfaces.[].ip_nat.destination.static.[].comment") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction</samp>](## "port_channel_interfaces.[].ip_nat.destination.static.[].direction") | String |  |  | Valid Values:<br>- egress<br>- ingress | Egress or ingress can be the default. This depends on source/destination, EOS version, and hardware platform.<br>EOS might remove this keyword in the configuration. So, check the configuration on targeted HW/SW.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp>](## "port_channel_interfaces.[].ip_nat.destination.static.[].group") | Integer |  |  | Min: 1<br>Max: 65535 | 'access_list' and 'group' are mutual exclusive |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;original_ip</samp>](## "port_channel_interfaces.[].ip_nat.destination.static.[].original_ip") | String | Required, Unique |  |  | IPv4 address |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;original_port</samp>](## "port_channel_interfaces.[].ip_nat.destination.static.[].original_port") | Integer |  |  | Min: 1<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "port_channel_interfaces.[].ip_nat.destination.static.[].priority") | Integer |  |  | Min: 0<br>Max: 4294967295 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;protocol</samp>](## "port_channel_interfaces.[].ip_nat.destination.static.[].protocol") | String |  |  | Valid Values:<br>- udp<br>- tcp |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;translated_ip</samp>](## "port_channel_interfaces.[].ip_nat.destination.static.[].translated_ip") | String | Required |  |  | IPv4 address |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;translated_port</samp>](## "port_channel_interfaces.[].ip_nat.destination.static.[].translated_port") | Integer |  |  | Min: 1<br>Max: 65535 | requires 'original_port' |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source</samp>](## "port_channel_interfaces.[].ip_nat.source") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dynamic</samp>](## "port_channel_interfaces.[].ip_nat.source.dynamic") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- access_list</samp>](## "port_channel_interfaces.[].ip_nat.source.dynamic.[].access_list") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;comment</samp>](## "port_channel_interfaces.[].ip_nat.source.dynamic.[].comment") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nat_type</samp>](## "port_channel_interfaces.[].ip_nat.source.dynamic.[].nat_type") | String | Required |  | Valid Values:<br>- overload<br>- pool<br>- pool-address-only<br>- pool-full-cone |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pool_name</samp>](## "port_channel_interfaces.[].ip_nat.source.dynamic.[].pool_name") | String |  |  |  | required if 'nat_type' is pool, pool-address-only or pool-full-cone<br>ignored if 'nat_type' is overload<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "port_channel_interfaces.[].ip_nat.source.dynamic.[].priority") | Integer |  |  | Min: 0<br>Max: 4294967295 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;static</samp>](## "port_channel_interfaces.[].ip_nat.source.static") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- access_list</samp>](## "port_channel_interfaces.[].ip_nat.source.static.[].access_list") | String |  |  |  | 'access_list' and 'group' are mutual exclusive |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;comment</samp>](## "port_channel_interfaces.[].ip_nat.source.static.[].comment") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction</samp>](## "port_channel_interfaces.[].ip_nat.source.static.[].direction") | String |  |  | Valid Values:<br>- egress<br>- ingress | Egress or ingress can be the default. This depends on source/destination, EOS version, and hardware platform.<br>EOS might remove this keyword in the configuration. So, check the configuration on targeted HW/SW.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp>](## "port_channel_interfaces.[].ip_nat.source.static.[].group") | Integer |  |  | Min: 1<br>Max: 65535 | 'access_list' and 'group' are mutual exclusive |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;original_ip</samp>](## "port_channel_interfaces.[].ip_nat.source.static.[].original_ip") | String | Required, Unique |  |  | IPv4 address |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;original_port</samp>](## "port_channel_interfaces.[].ip_nat.source.static.[].original_port") | Integer |  |  | Min: 1<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "port_channel_interfaces.[].ip_nat.source.static.[].priority") | Integer |  |  | Min: 0<br>Max: 4294967295 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;protocol</samp>](## "port_channel_interfaces.[].ip_nat.source.static.[].protocol") | String |  |  | Valid Values:<br>- udp<br>- tcp |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;translated_ip</samp>](## "port_channel_interfaces.[].ip_nat.source.static.[].translated_ip") | String | Required |  |  | IPv4 address |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;translated_port</samp>](## "port_channel_interfaces.[].ip_nat.source.static.[].translated_port") | Integer |  |  | Min: 1<br>Max: 65535 | requires 'original_port' |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_enable</samp>](## "port_channel_interfaces.[].ipv6_enable") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address</samp>](## "port_channel_interfaces.[].ipv6_address") | String |  |  |  | IPv6 address/mask |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address_link_local</samp>](## "port_channel_interfaces.[].ipv6_address_link_local") | String |  |  |  | Link local IPv6 address/mask |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_nd_ra_disabled</samp>](## "port_channel_interfaces.[].ipv6_nd_ra_disabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_nd_managed_config_flag</samp>](## "port_channel_interfaces.[].ipv6_nd_managed_config_flag") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_nd_prefixes</samp>](## "port_channel_interfaces.[].ipv6_nd_prefixes") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ipv6_prefix</samp>](## "port_channel_interfaces.[].ipv6_nd_prefixes.[].ipv6_prefix") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;valid_lifetime</samp>](## "port_channel_interfaces.[].ipv6_nd_prefixes.[].valid_lifetime") | String |  |  |  | Infinite or lifetime in seconds |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;preferred_lifetime</samp>](## "port_channel_interfaces.[].ipv6_nd_prefixes.[].preferred_lifetime") | String |  |  |  | Infinite or lifetime in seconds |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;no_autoconfig_flag</samp>](## "port_channel_interfaces.[].ipv6_nd_prefixes.[].no_autoconfig_flag") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;access_group_in</samp>](## "port_channel_interfaces.[].access_group_in") | String |  |  |  | Access list name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;access_group_out</samp>](## "port_channel_interfaces.[].access_group_out") | String |  |  |  | Access list name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_access_group_in</samp>](## "port_channel_interfaces.[].ipv6_access_group_in") | String |  |  |  | IPv6 access list name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_access_group_out</samp>](## "port_channel_interfaces.[].ipv6_access_group_out") | String |  |  |  | IPv6 access list name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mac_access_group_in</samp>](## "port_channel_interfaces.[].mac_access_group_in") | String |  |  |  | MAC access list name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mac_access_group_out</samp>](## "port_channel_interfaces.[].mac_access_group_out") | String |  |  |  | MAC access list name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;pim</samp>](## "port_channel_interfaces.[].pim") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp>](## "port_channel_interfaces.[].pim.ipv4") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dr_priority</samp>](## "port_channel_interfaces.[].pim.ipv4.dr_priority") | Integer |  |  | Min: 0<br>Max: 429467295 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sparse_mode</samp>](## "port_channel_interfaces.[].pim.ipv4.sparse_mode") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;service_profile</samp>](## "port_channel_interfaces.[].service_profile") | String |  |  |  | QOS profile |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf_network_point_to_point</samp>](## "port_channel_interfaces.[].ospf_network_point_to_point") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf_area</samp>](## "port_channel_interfaces.[].ospf_area") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf_cost</samp>](## "port_channel_interfaces.[].ospf_cost") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf_authentication</samp>](## "port_channel_interfaces.[].ospf_authentication") | String |  |  | Valid Values:<br>- none<br>- simple<br>- message-digest |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf_authentication_key</samp>](## "port_channel_interfaces.[].ospf_authentication_key") | String |  |  |  | Encrypted password |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf_message_digest_keys</samp>](## "port_channel_interfaces.[].ospf_message_digest_keys") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- id</samp>](## "port_channel_interfaces.[].ospf_message_digest_keys.[].id") | Integer | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hash_algorithm</samp>](## "port_channel_interfaces.[].ospf_message_digest_keys.[].hash_algorithm") | String |  |  | Valid Values:<br>- md5<br>- sha1<br>- sha256<br>- sha384<br>- sha512 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "port_channel_interfaces.[].ospf_message_digest_keys.[].key") | String |  |  |  | Encrypted password |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;flow_tracker</samp>](## "port_channel_interfaces.[].flow_tracker") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sampled</samp>](## "port_channel_interfaces.[].flow_tracker.sampled") | String |  |  |  | Flow tracker name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "port_channel_interfaces.[].bgp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;session_tracker</samp>](## "port_channel_interfaces.[].bgp.session_tracker") | String |  |  |  | Name of session tracker |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;peer</samp>](## "port_channel_interfaces.[].peer") | String |  |  |  | Key only used for documentation or validation purposes |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;peer_interface</samp>](## "port_channel_interfaces.[].peer_interface") | String |  |  |  | Key only used for documentation or validation purposes |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;peer_type</samp>](## "port_channel_interfaces.[].peer_type") | String |  |  |  | Key only used for documentation or validation purposes |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sflow</samp>](## "port_channel_interfaces.[].sflow") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable</samp>](## "port_channel_interfaces.[].sflow.enable") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;egress</samp>](## "port_channel_interfaces.[].sflow.egress") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable</samp>](## "port_channel_interfaces.[].sflow.egress.enable") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unmodified_enable</samp>](## "port_channel_interfaces.[].sflow.egress.unmodified_enable") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;eos_cli</samp>](## "port_channel_interfaces.[].eos_cli") | String |  |  |  | Multiline EOS CLI rendered directly on the port-channel interface in the final EOS configuration |

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
          forwarding_profile: <str>
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
          qos:
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
            level: <str>
            unit: <str>
          broadcast:
            level: <str>
            unit: <str>
          multicast:
            level: <str>
            unit: <str>
          unknown_unicast:
            level: <str>
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
        ip_nat:
          destination:
            dynamic:
              - access_list: <str>
                comment: <str>
                pool_name: <str>
                priority: <int>
            static:
              - access_list: <str>
                comment: <str>
                direction: <str>
                group: <int>
                original_ip: <str>
                original_port: <int>
                priority: <int>
                protocol: <str>
                translated_ip: <str>
                translated_port: <int>
          source:
            dynamic:
              - access_list: <str>
                comment: <str>
                nat_type: <str>
                pool_name: <str>
                priority: <int>
            static:
              - access_list: <str>
                comment: <str>
                direction: <str>
                group: <int>
                original_ip: <str>
                original_port: <int>
                priority: <int>
                protocol: <str>
                translated_ip: <str>
                translated_port: <int>
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
        bgp:
          session_tracker: <str>
        peer: <str>
        peer_interface: <str>
        peer_type: <str>
        sflow:
          enable: <bool>
          egress:
            enable: <bool>
            unmodified_enable: <bool>
        eos_cli: <str>
    ```
