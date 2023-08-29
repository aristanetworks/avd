<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>router_bgp</samp>](## "router_bgp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;as</samp>](## "router_bgp.as") | String |  |  |  | BGP AS <1-4294967295> or AS number in asdot notation <1-65535>.<0-65535> |
    | [<samp>&nbsp;&nbsp;router_id</samp>](## "router_bgp.router_id") | String |  |  |  | In IP address format A.B.C.D |
    | [<samp>&nbsp;&nbsp;distance</samp>](## "router_bgp.distance") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;external_routes</samp>](## "router_bgp.distance.external_routes") | Integer | Required |  | Min: 1<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;internal_routes</samp>](## "router_bgp.distance.internal_routes") | Integer | Required |  | Min: 1<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;local_routes</samp>](## "router_bgp.distance.local_routes") | Integer | Required |  | Min: 1<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;graceful_restart</samp>](## "router_bgp.graceful_restart") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.graceful_restart.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;restart_time</samp>](## "router_bgp.graceful_restart.restart_time") | Integer |  |  | Min: 1<br>Max: 3600 | Number of seconds |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;stalepath_time</samp>](## "router_bgp.graceful_restart.stalepath_time") | Integer |  |  | Min: 1<br>Max: 3600 | Number of seconds |
    | [<samp>&nbsp;&nbsp;graceful_restart_helper</samp>](## "router_bgp.graceful_restart_helper") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.graceful_restart_helper.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;restart_time</samp>](## "router_bgp.graceful_restart_helper.restart_time") | Integer |  |  | Min: 1<br>Max: 100000000 | Number of seconds<br>graceful-restart-help long-lived and restart-time are mutually exclusive in CLI.<br>restart-time will take precedence if both are configured.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;long_lived</samp>](## "router_bgp.graceful_restart_helper.long_lived") | Boolean |  |  |  | graceful-restart-help long-lived and restart-time are mutually exclusive in CLI.<br>restart-time will take precedence if both are configured.<br> |
    | [<samp>&nbsp;&nbsp;maximum_paths</samp>](## "router_bgp.maximum_paths") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;paths</samp>](## "router_bgp.maximum_paths.paths") | Integer | Required |  | Min: 1<br>Max: 600 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ecmp</samp>](## "router_bgp.maximum_paths.ecmp") | Integer |  |  | Min: 1<br>Max: 600 |  |
    | [<samp>&nbsp;&nbsp;updates</samp>](## "router_bgp.updates") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;wait_for_convergence</samp>](## "router_bgp.updates.wait_for_convergence") | Boolean |  |  |  | Disables FIB updates and route advertisement when the BGP instance is initiated until the BGP convergence state is reached.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;wait_install</samp>](## "router_bgp.updates.wait_install") | Boolean |  |  |  | Do not advertise reachability to a prefix until that prefix has been installed in hardware.<br>This will eliminate any temporary black holes due to a BGP speaker advertising reachability to a prefix that may not yet be installed into the forwarding plane.<br> |
    | [<samp>&nbsp;&nbsp;bgp_cluster_id</samp>](## "router_bgp.bgp_cluster_id") | String |  |  |  | IP Address A.B.C.D |
    | [<samp>&nbsp;&nbsp;bgp_defaults</samp>](## "router_bgp.bgp_defaults") | List, items: String |  |  |  | BGP command as string |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "router_bgp.bgp_defaults.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;bgp</samp>](## "router_bgp.bgp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;default</samp>](## "router_bgp.bgp.default") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_unicast</samp>](## "router_bgp.bgp.default.ipv4_unicast") | Boolean |  |  |  | Default activation of IPv4 unicast address-family on all IPv4 neighbors (EOS default = True). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_unicast_transport_ipv6</samp>](## "router_bgp.bgp.default.ipv4_unicast_transport_ipv6") | Boolean |  |  |  | Default activation of IPv4 unicast address-family on all IPv6 neighbors (EOS default == False). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;route_reflector_preserve_attributes</samp>](## "router_bgp.bgp.route_reflector_preserve_attributes") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.bgp.route_reflector_preserve_attributes.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always</samp>](## "router_bgp.bgp.route_reflector_preserve_attributes.always") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bestpath</samp>](## "router_bgp.bgp.bestpath") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;d_path</samp>](## "router_bgp.bgp.bestpath.d_path") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;listen_ranges</samp>](## "router_bgp.listen_ranges") | List, items: Dictionary |  |  |  | Improved "listen_ranges" data model to support multiple listen ranges and additional filter capabilities<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- prefix</samp>](## "router_bgp.listen_ranges.[].prefix") | String |  |  |  | IPv4 prefix "A.B.C.D/E" or IPv6 prefix "A:B:C:D:E:F:G:H/I" |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_id_include_router_id</samp>](## "router_bgp.listen_ranges.[].peer_id_include_router_id") | Boolean |  |  |  | Include router ID as part of peer filter |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_group</samp>](## "router_bgp.listen_ranges.[].peer_group") | String |  |  |  | Peer group name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_filter</samp>](## "router_bgp.listen_ranges.[].peer_filter") | String |  |  |  | Peer-filter name<br>note: `peer_filter` or `remote_as` is required but mutually exclusive.<br>If both are defined, `peer_filter` takes precedence<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_as</samp>](## "router_bgp.listen_ranges.[].remote_as") | String |  |  |  | BGP AS <1-4294967295> or AS number in asdot notation <1-65535>.<0-65535> |
    | [<samp>&nbsp;&nbsp;peer_groups</samp>](## "router_bgp.peer_groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "router_bgp.peer_groups.[].name") | String | Required, Unique |  |  | Peer-group name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "router_bgp.peer_groups.[].type") | String |  |  |  | Key only used for documentation or validation purposes |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_as</samp>](## "router_bgp.peer_groups.[].remote_as") | String |  |  |  | BGP AS <1-4294967295> or AS number in asdot notation <1-65535>.<0-65535> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_as</samp>](## "router_bgp.peer_groups.[].local_as") | String |  |  |  | BGP AS <1-4294967295> or AS number in asdot notation <1-65535>.<0-65535> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "router_bgp.peer_groups.[].description") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "router_bgp.peer_groups.[].shutdown") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;as_path</samp>](## "router_bgp.peer_groups.[].as_path") | Dictionary |  |  |  | BGP AS-PATH options |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_as_replace_out</samp>](## "router_bgp.peer_groups.[].as_path.remote_as_replace_out") | Boolean |  |  |  | Replace AS number with local AS number |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prepend_own_disabled</samp>](## "router_bgp.peer_groups.[].as_path.prepend_own_disabled") | Boolean |  |  |  | Disable prepending own AS number to AS path |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remove_private_as</samp>](## "router_bgp.peer_groups.[].remove_private_as") | Dictionary |  |  |  | Remove private AS numbers in outbound AS path |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.peer_groups.[].remove_private_as.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;all</samp>](## "router_bgp.peer_groups.[].remove_private_as.all") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;replace_as</samp>](## "router_bgp.peer_groups.[].remove_private_as.replace_as") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remove_private_as_ingress</samp>](## "router_bgp.peer_groups.[].remove_private_as_ingress") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.peer_groups.[].remove_private_as_ingress.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;replace_as</samp>](## "router_bgp.peer_groups.[].remove_private_as_ingress.replace_as") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_filter</samp>](## "router_bgp.peer_groups.[].peer_filter") <span style="color:red">deprecated</span> | String |  |  |  | Peer-filter name<br>note: `bgp_listen_range_prefix` and `peer_filter` should not be mixed with<br>the new `listen_ranges` key above to avoid conflicts.<br><span style="color:red">This key is deprecated. Support will be removed in AVD version 5.0.0. Use <samp>listen_ranges</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;next_hop_unchanged</samp>](## "router_bgp.peer_groups.[].next_hop_unchanged") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;update_source</samp>](## "router_bgp.peer_groups.[].update_source") | String |  |  |  | IP address or interface name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_reflector_client</samp>](## "router_bgp.peer_groups.[].route_reflector_client") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp>](## "router_bgp.peer_groups.[].bfd") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ebgp_multihop</samp>](## "router_bgp.peer_groups.[].ebgp_multihop") | Integer |  |  | Min: 1<br>Max: 255 | Time-to-live in range of hops |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;next_hop_self</samp>](## "router_bgp.peer_groups.[].next_hop_self") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "router_bgp.peer_groups.[].password") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;passive</samp>](## "router_bgp.peer_groups.[].passive") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default_originate</samp>](## "router_bgp.peer_groups.[].default_originate") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.peer_groups.[].default_originate.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always</samp>](## "router_bgp.peer_groups.[].default_originate.always") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.peer_groups.[].default_originate.route_map") | String |  |  |  | Route-map name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send_community</samp>](## "router_bgp.peer_groups.[].send_community") | String |  |  |  | 'all' or a combination of 'standard', 'extended', 'large' and 'link-bandwidth (w/options)' |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes</samp>](## "router_bgp.peer_groups.[].maximum_routes") | Integer |  |  | Min: 0<br>Max: 4294967294 | Maximum number of routes (0 means unlimited) |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes_warning_limit</samp>](## "router_bgp.peer_groups.[].maximum_routes_warning_limit") | String |  |  |  | Maximum number of routes after which a warning is issued (0 means never warn) or<br>Percentage of maximum number of routes at which to warn ("<1-100> percent")<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes_warning_only</samp>](## "router_bgp.peer_groups.[].maximum_routes_warning_only") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;link_bandwidth</samp>](## "router_bgp.peer_groups.[].link_bandwidth") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.peer_groups.[].link_bandwidth.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default</samp>](## "router_bgp.peer_groups.[].link_bandwidth.default") | String |  |  |  | nn.nn(K|M|G) link speed in bits/second |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;allowas_in</samp>](## "router_bgp.peer_groups.[].allowas_in") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.peer_groups.[].allowas_in.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;times</samp>](## "router_bgp.peer_groups.[].allowas_in.times") | Integer |  |  | Min: 1<br>Max: 10 | Number of local ASNs allowed in a BGP update |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;weight</samp>](## "router_bgp.peer_groups.[].weight") | Integer |  |  | Min: 0<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timers</samp>](## "router_bgp.peer_groups.[].timers") | String |  |  |  | BGP Keepalive and Hold Timer values in seconds as string "<0-3600> <0-3600>" |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rib_in_pre_policy_retain</samp>](## "router_bgp.peer_groups.[].rib_in_pre_policy_retain") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.peer_groups.[].rib_in_pre_policy_retain.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;all</samp>](## "router_bgp.peer_groups.[].rib_in_pre_policy_retain.all") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp>](## "router_bgp.peer_groups.[].route_map_in") | String |  |  |  | Inbound route-map name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp>](## "router_bgp.peer_groups.[].route_map_out") | String |  |  |  | Outbound route-map name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_listen_range_prefix</samp>](## "router_bgp.peer_groups.[].bgp_listen_range_prefix") <span style="color:red">deprecated</span> | String |  |  |  | IP prefix range<br>note: `bgp_listen_range_prefix` and `peer_filter` should not be mixed with<br>the new `listen_ranges` key above to avoid conflicts.<br><span style="color:red">This key is deprecated. Support will be removed in AVD version 5.0.0. Use <samp>listen_ranges</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;session_tracker</samp>](## "router_bgp.peer_groups.[].session_tracker") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;neighbors</samp>](## "router_bgp.neighbors") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- ip_address</samp>](## "router_bgp.neighbors.[].ip_address") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_group</samp>](## "router_bgp.neighbors.[].peer_group") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_as</samp>](## "router_bgp.neighbors.[].remote_as") | String |  |  |  | BGP AS <1-4294967295> or AS number in asdot notation <1-65535>.<0-65535> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_as</samp>](## "router_bgp.neighbors.[].local_as") | String |  |  |  | BGP AS <1-4294967295> or AS number in asdot notation <1-65535>.<0-65535> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;as_path</samp>](## "router_bgp.neighbors.[].as_path") | Dictionary |  |  |  | BGP AS-PATH options |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_as_replace_out</samp>](## "router_bgp.neighbors.[].as_path.remote_as_replace_out") | Boolean |  |  |  | Replace AS number with local AS number |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prepend_own_disabled</samp>](## "router_bgp.neighbors.[].as_path.prepend_own_disabled") | Boolean |  |  |  | Disable prepending own AS number to AS path |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "router_bgp.neighbors.[].description") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_reflector_client</samp>](## "router_bgp.neighbors.[].route_reflector_client") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;passive</samp>](## "router_bgp.neighbors.[].passive") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "router_bgp.neighbors.[].shutdown") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;update_source</samp>](## "router_bgp.neighbors.[].update_source") | String |  |  |  | Source Interface |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp>](## "router_bgp.neighbors.[].bfd") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;weight</samp>](## "router_bgp.neighbors.[].weight") | Integer |  |  | Min: 0<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timers</samp>](## "router_bgp.neighbors.[].timers") | String |  |  |  | BGP Keepalive and Hold Timer values in seconds as string "<0-3600> <0-3600>" |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp>](## "router_bgp.neighbors.[].route_map_in") | String |  |  |  | Inbound route-map name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp>](## "router_bgp.neighbors.[].route_map_out") | String |  |  |  | Outbound route-map name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default_originate</samp>](## "router_bgp.neighbors.[].default_originate") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.neighbors.[].default_originate.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always</samp>](## "router_bgp.neighbors.[].default_originate.always") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.neighbors.[].default_originate.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send_community</samp>](## "router_bgp.neighbors.[].send_community") | String |  |  |  | 'all' or a combination of 'standard', 'extended', 'large' and 'link-bandwidth (w/options)' |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes</samp>](## "router_bgp.neighbors.[].maximum_routes") | Integer |  |  | Min: 0<br>Max: 4294967294 | Maximum number of routes (0 means unlimited) |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes_warning_limit</samp>](## "router_bgp.neighbors.[].maximum_routes_warning_limit") | String |  |  |  | Maximum number of routes after which a warning is issued (0 means never warn) or<br>Percentage of maximum number of routes at which to warn ("<1-100> percent")<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes_warning_only</samp>](## "router_bgp.neighbors.[].maximum_routes_warning_only") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;allowas_in</samp>](## "router_bgp.neighbors.[].allowas_in") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.neighbors.[].allowas_in.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;times</samp>](## "router_bgp.neighbors.[].allowas_in.times") | Integer |  |  | Min: 1<br>Max: 10 | Number of local ASNs allowed in a BGP update |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ebgp_multihop</samp>](## "router_bgp.neighbors.[].ebgp_multihop") | Integer |  |  | Min: 1<br>Max: 255 | Time-to-live in range of hops |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;next_hop_self</samp>](## "router_bgp.neighbors.[].next_hop_self") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;link_bandwidth</samp>](## "router_bgp.neighbors.[].link_bandwidth") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.neighbors.[].link_bandwidth.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default</samp>](## "router_bgp.neighbors.[].link_bandwidth.default") | String |  |  |  | nn.nn(K|M|G) link speed in bits/second |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rib_in_pre_policy_retain</samp>](## "router_bgp.neighbors.[].rib_in_pre_policy_retain") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.neighbors.[].rib_in_pre_policy_retain.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;all</samp>](## "router_bgp.neighbors.[].rib_in_pre_policy_retain.all") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remove_private_as</samp>](## "router_bgp.neighbors.[].remove_private_as") | Dictionary |  |  |  | Remove private AS numbers in outbound AS path |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.neighbors.[].remove_private_as.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;all</samp>](## "router_bgp.neighbors.[].remove_private_as.all") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;replace_as</samp>](## "router_bgp.neighbors.[].remove_private_as.replace_as") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remove_private_as_ingress</samp>](## "router_bgp.neighbors.[].remove_private_as_ingress") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.neighbors.[].remove_private_as_ingress.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;replace_as</samp>](## "router_bgp.neighbors.[].remove_private_as_ingress.replace_as") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;session_tracker</samp>](## "router_bgp.neighbors.[].session_tracker") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;neighbor_interfaces</samp>](## "router_bgp.neighbor_interfaces") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "router_bgp.neighbor_interfaces.[].name") | String | Required, Unique |  |  | Interface name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_as</samp>](## "router_bgp.neighbor_interfaces.[].remote_as") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_group</samp>](## "router_bgp.neighbor_interfaces.[].peer_group") | String |  | `Peer-group name` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "router_bgp.neighbor_interfaces.[].description") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_filter</samp>](## "router_bgp.neighbor_interfaces.[].peer_filter") | String |  |  |  | Peer-filter name |
    | [<samp>&nbsp;&nbsp;aggregate_addresses</samp>](## "router_bgp.aggregate_addresses") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- prefix</samp>](## "router_bgp.aggregate_addresses.[].prefix") | String | Required, Unique |  |  | IPv4 prefix "A.B.C.D/E" or IPv6 prefix "A:B:C:D:E:F:G:H/I" |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;advertise_only</samp>](## "router_bgp.aggregate_addresses.[].advertise_only") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;as_set</samp>](## "router_bgp.aggregate_addresses.[].as_set") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;summary_only</samp>](## "router_bgp.aggregate_addresses.[].summary_only") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;attribute_map</samp>](## "router_bgp.aggregate_addresses.[].attribute_map") | String |  |  |  | Route-map name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_map</samp>](## "router_bgp.aggregate_addresses.[].match_map") | String |  |  |  | Route-map name |
    | [<samp>&nbsp;&nbsp;redistribute_routes</samp>](## "router_bgp.redistribute_routes") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- source_protocol</samp>](## "router_bgp.redistribute_routes.[].source_protocol") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.redistribute_routes.[].route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_bgp.redistribute_routes.[].include_leaked") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;vlan_aware_bundles</samp>](## "router_bgp.vlan_aware_bundles") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "router_bgp.vlan_aware_bundles.[].name") | String | Required, Unique |  |  | VLAN aware bundle name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tenant</samp>](## "router_bgp.vlan_aware_bundles.[].tenant") | String |  |  |  | Key only used for documentation or validation purposes |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "router_bgp.vlan_aware_bundles.[].description") | String |  |  |  | Key only used for documentation or validation purposes |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rd</samp>](## "router_bgp.vlan_aware_bundles.[].rd") | String |  |  |  | Route distinguisher |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rd_evpn_domain</samp>](## "router_bgp.vlan_aware_bundles.[].rd_evpn_domain") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;domain</samp>](## "router_bgp.vlan_aware_bundles.[].rd_evpn_domain.domain") | String |  |  | Valid Values:<br>- remote<br>- all |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rd</samp>](## "router_bgp.vlan_aware_bundles.[].rd_evpn_domain.rd") | String |  |  |  | Route distinguisher |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_targets</samp>](## "router_bgp.vlan_aware_bundles.[].route_targets") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;both</samp>](## "router_bgp.vlan_aware_bundles.[].route_targets.both") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "router_bgp.vlan_aware_bundles.[].route_targets.both.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;import</samp>](## "router_bgp.vlan_aware_bundles.[].route_targets.import") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "router_bgp.vlan_aware_bundles.[].route_targets.import.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;export</samp>](## "router_bgp.vlan_aware_bundles.[].route_targets.export") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "router_bgp.vlan_aware_bundles.[].route_targets.export.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;import_evpn_domains</samp>](## "router_bgp.vlan_aware_bundles.[].route_targets.import_evpn_domains") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- domain</samp>](## "router_bgp.vlan_aware_bundles.[].route_targets.import_evpn_domains.[].domain") | String |  |  | Valid Values:<br>- remote<br>- all |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_target</samp>](## "router_bgp.vlan_aware_bundles.[].route_targets.import_evpn_domains.[].route_target") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;export_evpn_domains</samp>](## "router_bgp.vlan_aware_bundles.[].route_targets.export_evpn_domains") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- domain</samp>](## "router_bgp.vlan_aware_bundles.[].route_targets.export_evpn_domains.[].domain") | String |  |  | Valid Values:<br>- remote<br>- all |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_target</samp>](## "router_bgp.vlan_aware_bundles.[].route_targets.export_evpn_domains.[].route_target") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;import_export_evpn_domains</samp>](## "router_bgp.vlan_aware_bundles.[].route_targets.import_export_evpn_domains") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- domain</samp>](## "router_bgp.vlan_aware_bundles.[].route_targets.import_export_evpn_domains.[].domain") | String |  |  | Valid Values:<br>- remote<br>- all |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_target</samp>](## "router_bgp.vlan_aware_bundles.[].route_targets.import_export_evpn_domains.[].route_target") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;redistribute_routes</samp>](## "router_bgp.vlan_aware_bundles.[].redistribute_routes") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "router_bgp.vlan_aware_bundles.[].redistribute_routes.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;no_redistribute_routes</samp>](## "router_bgp.vlan_aware_bundles.[].no_redistribute_routes") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "router_bgp.vlan_aware_bundles.[].no_redistribute_routes.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan</samp>](## "router_bgp.vlan_aware_bundles.[].vlan") | String |  |  |  | VLAN range as string. Example "100-200,300" |
    | [<samp>&nbsp;&nbsp;vlans</samp>](## "router_bgp.vlans") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- id</samp>](## "router_bgp.vlans.[].id") | Integer | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tenant</samp>](## "router_bgp.vlans.[].tenant") | String |  |  |  | Key only used for documentation or validation purposes |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rd</samp>](## "router_bgp.vlans.[].rd") | String |  |  |  | Route distinguisher |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rd_evpn_domain</samp>](## "router_bgp.vlans.[].rd_evpn_domain") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;domain</samp>](## "router_bgp.vlans.[].rd_evpn_domain.domain") | String |  |  | Valid Values:<br>- remote<br>- all |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rd</samp>](## "router_bgp.vlans.[].rd_evpn_domain.rd") | String |  |  |  | Route distinguisher |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;eos_cli</samp>](## "router_bgp.vlans.[].eos_cli") | String |  |  |  | Multiline EOS CLI rendered directly on the Router BGP, VLAN definition in the final EOS configuration |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_targets</samp>](## "router_bgp.vlans.[].route_targets") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;both</samp>](## "router_bgp.vlans.[].route_targets.both") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "router_bgp.vlans.[].route_targets.both.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;import</samp>](## "router_bgp.vlans.[].route_targets.import") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "router_bgp.vlans.[].route_targets.import.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;export</samp>](## "router_bgp.vlans.[].route_targets.export") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "router_bgp.vlans.[].route_targets.export.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;import_evpn_domains</samp>](## "router_bgp.vlans.[].route_targets.import_evpn_domains") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- domain</samp>](## "router_bgp.vlans.[].route_targets.import_evpn_domains.[].domain") | String |  |  | Valid Values:<br>- remote<br>- all |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_target</samp>](## "router_bgp.vlans.[].route_targets.import_evpn_domains.[].route_target") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;export_evpn_domains</samp>](## "router_bgp.vlans.[].route_targets.export_evpn_domains") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- domain</samp>](## "router_bgp.vlans.[].route_targets.export_evpn_domains.[].domain") | String |  |  | Valid Values:<br>- remote<br>- all |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_target</samp>](## "router_bgp.vlans.[].route_targets.export_evpn_domains.[].route_target") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;import_export_evpn_domains</samp>](## "router_bgp.vlans.[].route_targets.import_export_evpn_domains") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- domain</samp>](## "router_bgp.vlans.[].route_targets.import_export_evpn_domains.[].domain") | String |  |  | Valid Values:<br>- remote<br>- all |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_target</samp>](## "router_bgp.vlans.[].route_targets.import_export_evpn_domains.[].route_target") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;redistribute_routes</samp>](## "router_bgp.vlans.[].redistribute_routes") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "router_bgp.vlans.[].redistribute_routes.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;no_redistribute_routes</samp>](## "router_bgp.vlans.[].no_redistribute_routes") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "router_bgp.vlans.[].no_redistribute_routes.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;vpws</samp>](## "router_bgp.vpws") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "router_bgp.vpws.[].name") | String | Required, Unique |  |  | VPWS instance name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rd</samp>](## "router_bgp.vpws.[].rd") | String |  |  |  | Route distinguisher |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_targets</samp>](## "router_bgp.vpws.[].route_targets") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;import_export</samp>](## "router_bgp.vpws.[].route_targets.import_export") | String |  |  |  | Route Target |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls_control_word</samp>](## "router_bgp.vpws.[].mpls_control_word") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;label_flow</samp>](## "router_bgp.vpws.[].label_flow") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp>](## "router_bgp.vpws.[].mtu") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pseudowires</samp>](## "router_bgp.vpws.[].pseudowires") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "router_bgp.vpws.[].pseudowires.[].name") | String | Required, Unique |  |  | Pseudowire name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id_local</samp>](## "router_bgp.vpws.[].pseudowires.[].id_local") | Integer |  |  |  | Must match id_remote on other pe |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id_remote</samp>](## "router_bgp.vpws.[].pseudowires.[].id_remote") | Integer |  |  |  | Must match id_local on other pe |
    | [<samp>&nbsp;&nbsp;address_family_evpn</samp>](## "router_bgp.address_family_evpn") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;domain_identifier</samp>](## "router_bgp.address_family_evpn.domain_identifier") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;neighbor_default</samp>](## "router_bgp.address_family_evpn.neighbor_default") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;encapsulation</samp>](## "router_bgp.address_family_evpn.neighbor_default.encapsulation") | String |  |  | Valid Values:<br>- vxlan<br>- mpls |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;next_hop_self_source_interface</samp>](## "router_bgp.address_family_evpn.neighbor_default.next_hop_self_source_interface") | String |  |  |  | Source interface name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;next_hop_self_received_evpn_routes</samp>](## "router_bgp.address_family_evpn.neighbor_default.next_hop_self_received_evpn_routes") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable</samp>](## "router_bgp.address_family_evpn.neighbor_default.next_hop_self_received_evpn_routes.enable") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inter_domain</samp>](## "router_bgp.address_family_evpn.neighbor_default.next_hop_self_received_evpn_routes.inter_domain") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;peer_groups</samp>](## "router_bgp.address_family_evpn.peer_groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "router_bgp.address_family_evpn.peer_groups.[].name") | String | Required, Unique |  |  | Peer-group name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "router_bgp.address_family_evpn.peer_groups.[].activate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp>](## "router_bgp.address_family_evpn.peer_groups.[].route_map_in") | String |  |  |  | Inbound route-map name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp>](## "router_bgp.address_family_evpn.peer_groups.[].route_map_out") | String |  |  |  | Outbound route-map name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;domain_remote</samp>](## "router_bgp.address_family_evpn.peer_groups.[].domain_remote") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;encapsulation</samp>](## "router_bgp.address_family_evpn.peer_groups.[].encapsulation") | String |  |  | Valid Values:<br>- vxlan<br>- mpls |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;evpn_hostflap_detection</samp>](## "router_bgp.address_family_evpn.evpn_hostflap_detection") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.address_family_evpn.evpn_hostflap_detection.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;window</samp>](## "router_bgp.address_family_evpn.evpn_hostflap_detection.window") | Integer |  |  | Min: 0<br>Max: 4294967295 | Time (in seconds) to detect a MAC duplication issue |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;threshold</samp>](## "router_bgp.address_family_evpn.evpn_hostflap_detection.threshold") | Integer |  |  | Min: 0<br>Max: 4294967295 | Minimum number of MAC moves that indicate a MAC Duplication issue |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expiry_timeout</samp>](## "router_bgp.address_family_evpn.evpn_hostflap_detection.expiry_timeout") | Integer |  |  | Min: 0<br>Max: 4294967295 | Time (in seconds) to purge a MAC duplication issue |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;route</samp>](## "router_bgp.address_family_evpn.route") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;import_match_failure_action</samp>](## "router_bgp.address_family_evpn.route.import_match_failure_action") | String |  |  | Valid Values:<br>- discard |  |
    | [<samp>&nbsp;&nbsp;address_family_rtc</samp>](## "router_bgp.address_family_rtc") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;peer_groups</samp>](## "router_bgp.address_family_rtc.peer_groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "router_bgp.address_family_rtc.peer_groups.[].name") | String | Required, Unique |  |  | Peer-group name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "router_bgp.address_family_rtc.peer_groups.[].activate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default_route_target</samp>](## "router_bgp.address_family_rtc.peer_groups.[].default_route_target") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;only</samp>](## "router_bgp.address_family_rtc.peer_groups.[].default_route_target.only") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;encoding_origin_as_omit</samp>](## "router_bgp.address_family_rtc.peer_groups.[].default_route_target.encoding_origin_as_omit") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;address_family_ipv4</samp>](## "router_bgp.address_family_ipv4") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;networks</samp>](## "router_bgp.address_family_ipv4.networks") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- prefix</samp>](## "router_bgp.address_family_ipv4.networks.[].prefix") | String | Required, Unique |  |  | IPv4 prefix "A.B.C.D/E" or IPv6 prefix "A:B:C:D:E:F:G:H/I" |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.address_family_ipv4.networks.[].route_map") | String |  |  |  | Route-map name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;peer_groups</samp>](## "router_bgp.address_family_ipv4.peer_groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "router_bgp.address_family_ipv4.peer_groups.[].name") | String | Required, Unique |  |  | Peer-group name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "router_bgp.address_family_ipv4.peer_groups.[].activate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp>](## "router_bgp.address_family_ipv4.peer_groups.[].route_map_in") | String |  |  |  | Inbound route-map name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp>](## "router_bgp.address_family_ipv4.peer_groups.[].route_map_out") | String |  |  |  | Outbound route-map name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default_originate</samp>](## "router_bgp.address_family_ipv4.peer_groups.[].default_originate") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always</samp>](## "router_bgp.address_family_ipv4.peer_groups.[].default_originate.always") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.address_family_ipv4.peer_groups.[].default_originate.route_map") | String |  |  |  | Route-map name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;next_hop</samp>](## "router_bgp.address_family_ipv4.peer_groups.[].next_hop") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_family_ipv6</samp>](## "router_bgp.address_family_ipv4.peer_groups.[].next_hop.address_family_ipv6") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.address_family_ipv4.peer_groups.[].next_hop.address_family_ipv6.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;originate</samp>](## "router_bgp.address_family_ipv4.peer_groups.[].next_hop.address_family_ipv6.originate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_family_ipv6_originate</samp>](## "router_bgp.address_family_ipv4.peer_groups.[].next_hop.address_family_ipv6_originate") <span style="color:red">deprecated</span> | Boolean |  |  |  | <span style="color:red">This key is deprecated. Support will be removed in AVD version 5.0.0. Use <samp>address_family_ipv6</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list_in</samp>](## "router_bgp.address_family_ipv4.peer_groups.[].prefix_list_in") | String |  |  |  | Inbound prefix-list name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list_out</samp>](## "router_bgp.address_family_ipv4.peer_groups.[].prefix_list_out") | String |  |  |  | Outbound prefix-list name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;neighbors</samp>](## "router_bgp.address_family_ipv4.neighbors") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ip_address</samp>](## "router_bgp.address_family_ipv4.neighbors.[].ip_address") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "router_bgp.address_family_ipv4.neighbors.[].activate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp>](## "router_bgp.address_family_ipv4.neighbors.[].route_map_in") | String |  |  |  | Inbound route-map name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp>](## "router_bgp.address_family_ipv4.neighbors.[].route_map_out") | String |  |  |  | Outbound route-map name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list_in</samp>](## "router_bgp.address_family_ipv4.neighbors.[].prefix_list_in") | String |  |  |  | Inbound prefix-list name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list_out</samp>](## "router_bgp.address_family_ipv4.neighbors.[].prefix_list_out") | String |  |  |  | Prefix-list name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default_originate</samp>](## "router_bgp.address_family_ipv4.neighbors.[].default_originate") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always</samp>](## "router_bgp.address_family_ipv4.neighbors.[].default_originate.always") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.address_family_ipv4.neighbors.[].default_originate.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;address_family_ipv4_multicast</samp>](## "router_bgp.address_family_ipv4_multicast") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;peer_groups</samp>](## "router_bgp.address_family_ipv4_multicast.peer_groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "router_bgp.address_family_ipv4_multicast.peer_groups.[].name") | String | Required, Unique |  |  | Peer-group name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "router_bgp.address_family_ipv4_multicast.peer_groups.[].activate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp>](## "router_bgp.address_family_ipv4_multicast.peer_groups.[].route_map_in") | String |  |  |  | Inbound route-map name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp>](## "router_bgp.address_family_ipv4_multicast.peer_groups.[].route_map_out") | String |  |  |  | Outbound route-map name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;neighbors</samp>](## "router_bgp.address_family_ipv4_multicast.neighbors") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ip_address</samp>](## "router_bgp.address_family_ipv4_multicast.neighbors.[].ip_address") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "router_bgp.address_family_ipv4_multicast.neighbors.[].activate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp>](## "router_bgp.address_family_ipv4_multicast.neighbors.[].route_map_in") | String |  |  |  | Inbound route-map name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp>](## "router_bgp.address_family_ipv4_multicast.neighbors.[].route_map_out") | String |  |  |  | Outbound route-map name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;redistribute_routes</samp>](## "router_bgp.address_family_ipv4_multicast.redistribute_routes") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- source_protocol</samp>](## "router_bgp.address_family_ipv4_multicast.redistribute_routes.[].source_protocol") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.address_family_ipv4_multicast.redistribute_routes.[].route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;address_family_ipv6</samp>](## "router_bgp.address_family_ipv6") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;networks</samp>](## "router_bgp.address_family_ipv6.networks") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- prefix</samp>](## "router_bgp.address_family_ipv6.networks.[].prefix") | String | Required, Unique |  |  | IPv4 prefix "A.B.C.D/E" or IPv6 prefix "A:B:C:D:E:F:G:H/I" |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.address_family_ipv6.networks.[].route_map") | String |  |  |  | Route-map name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;peer_groups</samp>](## "router_bgp.address_family_ipv6.peer_groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "router_bgp.address_family_ipv6.peer_groups.[].name") | String | Required, Unique |  |  | Peer-group name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "router_bgp.address_family_ipv6.peer_groups.[].activate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp>](## "router_bgp.address_family_ipv6.peer_groups.[].route_map_in") | String |  |  |  | Inbound route-map name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp>](## "router_bgp.address_family_ipv6.peer_groups.[].route_map_out") | String |  |  |  | Outbound route-map name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list_in</samp>](## "router_bgp.address_family_ipv6.peer_groups.[].prefix_list_in") | String |  |  |  | Inbound prefix-list name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list_out</samp>](## "router_bgp.address_family_ipv6.peer_groups.[].prefix_list_out") | String |  |  |  | Outbound prefix-list name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;neighbors</samp>](## "router_bgp.address_family_ipv6.neighbors") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ip_address</samp>](## "router_bgp.address_family_ipv6.neighbors.[].ip_address") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "router_bgp.address_family_ipv6.neighbors.[].activate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp>](## "router_bgp.address_family_ipv6.neighbors.[].route_map_in") | String |  |  |  | Inbound route-map name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp>](## "router_bgp.address_family_ipv6.neighbors.[].route_map_out") | String |  |  |  | Outbound route-map name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list_in</samp>](## "router_bgp.address_family_ipv6.neighbors.[].prefix_list_in") | String |  |  |  | Inbound prefix-list name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list_out</samp>](## "router_bgp.address_family_ipv6.neighbors.[].prefix_list_out") | String |  |  |  | Outbound prefix-list name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;redistribute_routes</samp>](## "router_bgp.address_family_ipv6.redistribute_routes") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- source_protocol</samp>](## "router_bgp.address_family_ipv6.redistribute_routes.[].source_protocol") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.address_family_ipv6.redistribute_routes.[].route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_bgp.address_family_ipv6.redistribute_routes.[].include_leaked") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;address_family_ipv6_multicast</samp>](## "router_bgp.address_family_ipv6_multicast") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "router_bgp.address_family_ipv6_multicast.bgp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;missing_policy</samp>](## "router_bgp.address_family_ipv6_multicast.bgp.missing_policy") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction_in_action</samp>](## "router_bgp.address_family_ipv6_multicast.bgp.missing_policy.direction_in_action") | String |  |  | Valid Values:<br>- deny<br>- deny-in-out<br>- permit |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction_out_action</samp>](## "router_bgp.address_family_ipv6_multicast.bgp.missing_policy.direction_out_action") | String |  |  | Valid Values:<br>- deny<br>- deny-in-out<br>- permit |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;additional_paths</samp>](## "router_bgp.address_family_ipv6_multicast.bgp.additional_paths") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;receive</samp>](## "router_bgp.address_family_ipv6_multicast.bgp.additional_paths.receive") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;neighbors</samp>](## "router_bgp.address_family_ipv6_multicast.neighbors") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ip_address</samp>](## "router_bgp.address_family_ipv6_multicast.neighbors.[].ip_address") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "router_bgp.address_family_ipv6_multicast.neighbors.[].activate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp>](## "router_bgp.address_family_ipv6_multicast.neighbors.[].route_map_in") | String |  |  |  | Inbound route-map name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp>](## "router_bgp.address_family_ipv6_multicast.neighbors.[].route_map_out") | String |  |  |  | Outbound route-map name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;peer_groups</samp>](## "router_bgp.address_family_ipv6_multicast.peer_groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "router_bgp.address_family_ipv6_multicast.peer_groups.[].name") | String | Required, Unique |  |  | Peer-group name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "router_bgp.address_family_ipv6_multicast.peer_groups.[].activate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;networks</samp>](## "router_bgp.address_family_ipv6_multicast.networks") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- prefix</samp>](## "router_bgp.address_family_ipv6_multicast.networks.[].prefix") | String | Required, Unique |  |  | IPv6 prefix "A:B:C:D:E:F:G:H/I" |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.address_family_ipv6_multicast.networks.[].route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;address_family_flow_spec_ipv4</samp>](## "router_bgp.address_family_flow_spec_ipv4") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "router_bgp.address_family_flow_spec_ipv4.bgp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;missing_policy</samp>](## "router_bgp.address_family_flow_spec_ipv4.bgp.missing_policy") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction_in_action</samp>](## "router_bgp.address_family_flow_spec_ipv4.bgp.missing_policy.direction_in_action") | String |  |  | Valid Values:<br>- deny<br>- deny-in-out<br>- permit |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction_out_action</samp>](## "router_bgp.address_family_flow_spec_ipv4.bgp.missing_policy.direction_out_action") | String |  |  | Valid Values:<br>- deny<br>- deny-in-out<br>- permit |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;neighbors</samp>](## "router_bgp.address_family_flow_spec_ipv4.neighbors") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ip_address</samp>](## "router_bgp.address_family_flow_spec_ipv4.neighbors.[].ip_address") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "router_bgp.address_family_flow_spec_ipv4.neighbors.[].activate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;peer_groups</samp>](## "router_bgp.address_family_flow_spec_ipv4.peer_groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "router_bgp.address_family_flow_spec_ipv4.peer_groups.[].name") | String | Required, Unique |  |  | Peer-group name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "router_bgp.address_family_flow_spec_ipv4.peer_groups.[].activate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;address_family_flow_spec_ipv6</samp>](## "router_bgp.address_family_flow_spec_ipv6") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "router_bgp.address_family_flow_spec_ipv6.bgp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;missing_policy</samp>](## "router_bgp.address_family_flow_spec_ipv6.bgp.missing_policy") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction_in_action</samp>](## "router_bgp.address_family_flow_spec_ipv6.bgp.missing_policy.direction_in_action") | String |  |  | Valid Values:<br>- deny<br>- deny-in-out<br>- permit |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction_out_action</samp>](## "router_bgp.address_family_flow_spec_ipv6.bgp.missing_policy.direction_out_action") | String |  |  | Valid Values:<br>- deny<br>- deny-in-out<br>- permit |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;neighbors</samp>](## "router_bgp.address_family_flow_spec_ipv6.neighbors") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ip_address</samp>](## "router_bgp.address_family_flow_spec_ipv6.neighbors.[].ip_address") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "router_bgp.address_family_flow_spec_ipv6.neighbors.[].activate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;peer_groups</samp>](## "router_bgp.address_family_flow_spec_ipv6.peer_groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "router_bgp.address_family_flow_spec_ipv6.peer_groups.[].name") | String | Required, Unique |  |  | Peer-group name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "router_bgp.address_family_flow_spec_ipv6.peer_groups.[].activate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;address_family_vpn_ipv4</samp>](## "router_bgp.address_family_vpn_ipv4") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;domain_identifier</samp>](## "router_bgp.address_family_vpn_ipv4.domain_identifier") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;peer_groups</samp>](## "router_bgp.address_family_vpn_ipv4.peer_groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "router_bgp.address_family_vpn_ipv4.peer_groups.[].name") | String | Required, Unique |  |  | Peer-group name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "router_bgp.address_family_vpn_ipv4.peer_groups.[].activate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp>](## "router_bgp.address_family_vpn_ipv4.peer_groups.[].route_map_in") | String |  |  |  | Inbound route-map name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp>](## "router_bgp.address_family_vpn_ipv4.peer_groups.[].route_map_out") | String |  |  |  | Outbound route-map name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;route</samp>](## "router_bgp.address_family_vpn_ipv4.route") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;import_match_failure_action</samp>](## "router_bgp.address_family_vpn_ipv4.route.import_match_failure_action") | String |  |  | Valid Values:<br>- discard |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;neighbors</samp>](## "router_bgp.address_family_vpn_ipv4.neighbors") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ip_address</samp>](## "router_bgp.address_family_vpn_ipv4.neighbors.[].ip_address") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "router_bgp.address_family_vpn_ipv4.neighbors.[].activate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp>](## "router_bgp.address_family_vpn_ipv4.neighbors.[].route_map_in") | String |  |  |  | Inbound route-map name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp>](## "router_bgp.address_family_vpn_ipv4.neighbors.[].route_map_out") | String |  |  |  | Outbound route-map name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;neighbor_default_encapsulation_mpls_next_hop_self</samp>](## "router_bgp.address_family_vpn_ipv4.neighbor_default_encapsulation_mpls_next_hop_self") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp>](## "router_bgp.address_family_vpn_ipv4.neighbor_default_encapsulation_mpls_next_hop_self.source_interface") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;address_family_vpn_ipv6</samp>](## "router_bgp.address_family_vpn_ipv6") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;domain_identifier</samp>](## "router_bgp.address_family_vpn_ipv6.domain_identifier") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;peer_groups</samp>](## "router_bgp.address_family_vpn_ipv6.peer_groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "router_bgp.address_family_vpn_ipv6.peer_groups.[].name") | String | Required, Unique |  |  | Peer-group name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "router_bgp.address_family_vpn_ipv6.peer_groups.[].activate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp>](## "router_bgp.address_family_vpn_ipv6.peer_groups.[].route_map_in") | String |  |  |  | Inbound route-map name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp>](## "router_bgp.address_family_vpn_ipv6.peer_groups.[].route_map_out") | String |  |  |  | Outbound route-map name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;route</samp>](## "router_bgp.address_family_vpn_ipv6.route") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;import_match_failure_action</samp>](## "router_bgp.address_family_vpn_ipv6.route.import_match_failure_action") | String |  |  | Valid Values:<br>- discard |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;neighbors</samp>](## "router_bgp.address_family_vpn_ipv6.neighbors") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ip_address</samp>](## "router_bgp.address_family_vpn_ipv6.neighbors.[].ip_address") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "router_bgp.address_family_vpn_ipv6.neighbors.[].activate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp>](## "router_bgp.address_family_vpn_ipv6.neighbors.[].route_map_in") | String |  |  |  | Inbound route-map name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp>](## "router_bgp.address_family_vpn_ipv6.neighbors.[].route_map_out") | String |  |  |  | Outbound route-map name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;neighbor_default_encapsulation_mpls_next_hop_self</samp>](## "router_bgp.address_family_vpn_ipv6.neighbor_default_encapsulation_mpls_next_hop_self") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp>](## "router_bgp.address_family_vpn_ipv6.neighbor_default_encapsulation_mpls_next_hop_self.source_interface") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;vrfs</samp>](## "router_bgp.vrfs") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "router_bgp.vrfs.[].name") | String | Required, Unique |  |  | VRF name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rd</samp>](## "router_bgp.vrfs.[].rd") | String |  |  |  | Route distinguisher |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_multicast</samp>](## "router_bgp.vrfs.[].evpn_multicast") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_multicast_address_family</samp>](## "router_bgp.vrfs.[].evpn_multicast_address_family") | Dictionary |  |  |  | Enable per-AF EVPN multicast settings |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp>](## "router_bgp.vrfs.[].evpn_multicast_address_family.ipv4") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;transit</samp>](## "router_bgp.vrfs.[].evpn_multicast_address_family.ipv4.transit") | Boolean |  |  |  | Enable EVPN multicast transit mode |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_targets</samp>](## "router_bgp.vrfs.[].route_targets") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;import</samp>](## "router_bgp.vrfs.[].route_targets.import") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- address_family</samp>](## "router_bgp.vrfs.[].route_targets.import.[].address_family") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_targets</samp>](## "router_bgp.vrfs.[].route_targets.import.[].route_targets") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "router_bgp.vrfs.[].route_targets.import.[].route_targets.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;export</samp>](## "router_bgp.vrfs.[].route_targets.export") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- address_family</samp>](## "router_bgp.vrfs.[].route_targets.export.[].address_family") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_targets</samp>](## "router_bgp.vrfs.[].route_targets.export.[].route_targets") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "router_bgp.vrfs.[].route_targets.export.[].route_targets.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;router_id</samp>](## "router_bgp.vrfs.[].router_id") | String |  |  |  | in IP address format A.B.C.D |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timers</samp>](## "router_bgp.vrfs.[].timers") | String |  |  |  | BGP Keepalive and Hold Timer values in seconds as string "<0-3600> <0-3600>" |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;networks</samp>](## "router_bgp.vrfs.[].networks") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- prefix</samp>](## "router_bgp.vrfs.[].networks.[].prefix") | String | Required, Unique |  |  | IPv4 prefix "A.B.C.D/E" or IPv6 prefix "A:B:C:D:E:F:G:H/I" |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].networks.[].route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;updates</samp>](## "router_bgp.vrfs.[].updates") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;wait_for_convergence</samp>](## "router_bgp.vrfs.[].updates.wait_for_convergence") | Boolean |  |  |  | Disables FIB updates and route advertisement when the BGP instance is initiated until the BGP convergence state is reached.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;wait_install</samp>](## "router_bgp.vrfs.[].updates.wait_install") | Boolean |  |  |  | Do not advertise reachability to a prefix until that prefix has been installed in hardware.<br>This will eliminate any temporary black holes due to a BGP speaker advertising reachability to a prefix that may not yet be installed into the forwarding plane.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;listen_ranges</samp>](## "router_bgp.vrfs.[].listen_ranges") | List, items: Dictionary |  |  |  | Improved "listen_ranges" data model to support multiple listen ranges and additional filter capabilities<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- prefix</samp>](## "router_bgp.vrfs.[].listen_ranges.[].prefix") | String |  |  |  | IPv4 prefix "A.B.C.D/E" or IPv6 prefix "A:B:C:D:E:F:G:H/I" |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_id_include_router_id</samp>](## "router_bgp.vrfs.[].listen_ranges.[].peer_id_include_router_id") | Boolean |  |  |  | Include router ID as part of peer filter |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_group</samp>](## "router_bgp.vrfs.[].listen_ranges.[].peer_group") | String |  |  |  | Peer-group name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_filter</samp>](## "router_bgp.vrfs.[].listen_ranges.[].peer_filter") | String |  |  |  | Peer-filter name<br>note: `peer_filter`` or `remote_as` is required but mutually exclusive.<br>If both are defined, peer_filter takes precedence<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_as</samp>](## "router_bgp.vrfs.[].listen_ranges.[].remote_as") | String |  |  |  | BGP AS <1-4294967295> or AS number in asdot notation <1-65535>.<0-65535> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;neighbors</samp>](## "router_bgp.vrfs.[].neighbors") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ip_address</samp>](## "router_bgp.vrfs.[].neighbors.[].ip_address") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_group</samp>](## "router_bgp.vrfs.[].neighbors.[].peer_group") | String |  |  |  | Peer-group name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_as</samp>](## "router_bgp.vrfs.[].neighbors.[].remote_as") | String |  |  |  | BGP AS <1-4294967295> or AS number in asdot notation <1-65535>.<0-65535> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "router_bgp.vrfs.[].neighbors.[].password") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;passive</samp>](## "router_bgp.vrfs.[].neighbors.[].passive") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remove_private_as</samp>](## "router_bgp.vrfs.[].neighbors.[].remove_private_as") | Dictionary |  |  |  | Remove private AS numbers in outbound AS path |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].neighbors.[].remove_private_as.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;all</samp>](## "router_bgp.vrfs.[].neighbors.[].remove_private_as.all") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;replace_as</samp>](## "router_bgp.vrfs.[].neighbors.[].remove_private_as.replace_as") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remove_private_as_ingress</samp>](## "router_bgp.vrfs.[].neighbors.[].remove_private_as_ingress") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].neighbors.[].remove_private_as_ingress.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;replace_as</samp>](## "router_bgp.vrfs.[].neighbors.[].remove_private_as_ingress.replace_as") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;weight</samp>](## "router_bgp.vrfs.[].neighbors.[].weight") | Integer |  |  | Min: 0<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_as</samp>](## "router_bgp.vrfs.[].neighbors.[].local_as") | String |  |  |  | BGP AS <1-4294967295> or AS number in asdot notation <1-65535>.<0-65535> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;as_path</samp>](## "router_bgp.vrfs.[].neighbors.[].as_path") | Dictionary |  |  |  | BGP AS-PATH options |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_as_replace_out</samp>](## "router_bgp.vrfs.[].neighbors.[].as_path.remote_as_replace_out") | Boolean |  |  |  | Replace AS number with local AS number |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prepend_own_disabled</samp>](## "router_bgp.vrfs.[].neighbors.[].as_path.prepend_own_disabled") | Boolean |  |  |  | Disable prepending own AS number to AS path |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "router_bgp.vrfs.[].neighbors.[].description") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_reflector_client</samp>](## "router_bgp.vrfs.[].neighbors.[].route_reflector_client") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ebgp_multihop</samp>](## "router_bgp.vrfs.[].neighbors.[].ebgp_multihop") | Integer |  |  | Min: 1<br>Max: 255 | Time-to-live in range of hops |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;next_hop_self</samp>](## "router_bgp.vrfs.[].neighbors.[].next_hop_self") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "router_bgp.vrfs.[].neighbors.[].shutdown") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp>](## "router_bgp.vrfs.[].neighbors.[].bfd") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timers</samp>](## "router_bgp.vrfs.[].neighbors.[].timers") | String |  |  |  | BGP Keepalive and Hold Timer values in seconds as string "<0-3600> <0-3600>" |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rib_in_pre_policy_retain</samp>](## "router_bgp.vrfs.[].neighbors.[].rib_in_pre_policy_retain") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].neighbors.[].rib_in_pre_policy_retain.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;all</samp>](## "router_bgp.vrfs.[].neighbors.[].rib_in_pre_policy_retain.all") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send_community</samp>](## "router_bgp.vrfs.[].neighbors.[].send_community") | String |  |  |  | 'all' or a combination of 'standard', 'extended', 'large' and 'link-bandwidth (w/options)' |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes</samp>](## "router_bgp.vrfs.[].neighbors.[].maximum_routes") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes_warning_limit</samp>](## "router_bgp.vrfs.[].neighbors.[].maximum_routes_warning_limit") | String |  |  |  | Maximum number of routes after which a warning is issued (0 means never warn) or<br>Percentage of maximum number of routes at which to warn ("<1-100> percent")<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes_warning_only</samp>](## "router_bgp.vrfs.[].neighbors.[].maximum_routes_warning_only") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;allowas_in</samp>](## "router_bgp.vrfs.[].neighbors.[].allowas_in") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].neighbors.[].allowas_in.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;times</samp>](## "router_bgp.vrfs.[].neighbors.[].allowas_in.times") | Integer |  |  | Min: 1<br>Max: 10 | Number of local ASNs allowed in a BGP update |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default_originate</samp>](## "router_bgp.vrfs.[].neighbors.[].default_originate") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].neighbors.[].default_originate.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always</samp>](## "router_bgp.vrfs.[].neighbors.[].default_originate.always") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].neighbors.[].default_originate.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;update_source</samp>](## "router_bgp.vrfs.[].neighbors.[].update_source") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp>](## "router_bgp.vrfs.[].neighbors.[].route_map_in") | String |  |  |  | Inbound route-map name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp>](## "router_bgp.vrfs.[].neighbors.[].route_map_out") | String |  |  |  | Outbound route-map name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list_in</samp>](## "router_bgp.vrfs.[].neighbors.[].prefix_list_in") | String |  |  |  | Inbound prefix-list name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list_out</samp>](## "router_bgp.vrfs.[].neighbors.[].prefix_list_out") | String |  |  |  | Outbound prefix-list name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;neighbor_interfaces</samp>](## "router_bgp.vrfs.[].neighbor_interfaces") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "router_bgp.vrfs.[].neighbor_interfaces.[].name") | String | Required, Unique |  |  | Interface name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_as</samp>](## "router_bgp.vrfs.[].neighbor_interfaces.[].remote_as") | String |  |  |  | BGP AS <1-4294967295> or AS number in asdot notation <1-65535>.<0-65535> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_group</samp>](## "router_bgp.vrfs.[].neighbor_interfaces.[].peer_group") | String |  |  |  | Peer-group name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_filter</samp>](## "router_bgp.vrfs.[].neighbor_interfaces.[].peer_filter") | String |  |  |  | Peer-filter name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "router_bgp.vrfs.[].neighbor_interfaces.[].description") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;redistribute_routes</samp>](## "router_bgp.vrfs.[].redistribute_routes") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- source_protocol</samp>](## "router_bgp.vrfs.[].redistribute_routes.[].source_protocol") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].redistribute_routes.[].route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_bgp.vrfs.[].redistribute_routes.[].include_leaked") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;aggregate_addresses</samp>](## "router_bgp.vrfs.[].aggregate_addresses") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- prefix</samp>](## "router_bgp.vrfs.[].aggregate_addresses.[].prefix") | String | Required, Unique |  |  | IPv4 prefix "A.B.C.D/E" or IPv6 prefix "A:B:C:D:E:F:G:H/I" |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;advertise_only</samp>](## "router_bgp.vrfs.[].aggregate_addresses.[].advertise_only") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;as_set</samp>](## "router_bgp.vrfs.[].aggregate_addresses.[].as_set") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;summary_only</samp>](## "router_bgp.vrfs.[].aggregate_addresses.[].summary_only") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;attribute_map</samp>](## "router_bgp.vrfs.[].aggregate_addresses.[].attribute_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_map</samp>](## "router_bgp.vrfs.[].aggregate_addresses.[].match_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_family_ipv4</samp>](## "router_bgp.vrfs.[].address_family_ipv4") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "router_bgp.vrfs.[].address_family_ipv4.bgp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;missing_policy</samp>](## "router_bgp.vrfs.[].address_family_ipv4.bgp.missing_policy") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction_in_action</samp>](## "router_bgp.vrfs.[].address_family_ipv4.bgp.missing_policy.direction_in_action") | String |  |  | Valid Values:<br>- deny<br>- deny-in-out<br>- permit |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction_out_action</samp>](## "router_bgp.vrfs.[].address_family_ipv4.bgp.missing_policy.direction_out_action") | String |  |  | Valid Values:<br>- deny<br>- deny-in-out<br>- permit |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;additional_paths</samp>](## "router_bgp.vrfs.[].address_family_ipv4.bgp.additional_paths") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;install</samp>](## "router_bgp.vrfs.[].address_family_ipv4.bgp.additional_paths.install") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;install_ecmp_primary</samp>](## "router_bgp.vrfs.[].address_family_ipv4.bgp.additional_paths.install_ecmp_primary") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;receive</samp>](## "router_bgp.vrfs.[].address_family_ipv4.bgp.additional_paths.receive") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send</samp>](## "router_bgp.vrfs.[].address_family_ipv4.bgp.additional_paths.send") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;any</samp>](## "router_bgp.vrfs.[].address_family_ipv4.bgp.additional_paths.send.any") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;backup</samp>](## "router_bgp.vrfs.[].address_family_ipv4.bgp.additional_paths.send.backup") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ecmp</samp>](## "router_bgp.vrfs.[].address_family_ipv4.bgp.additional_paths.send.ecmp") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ecmp_limit</samp>](## "router_bgp.vrfs.[].address_family_ipv4.bgp.additional_paths.send.ecmp_limit") | Integer |  |  | Min: 2<br>Max: 64 | Amount of ECMP paths to send |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;limit</samp>](## "router_bgp.vrfs.[].address_family_ipv4.bgp.additional_paths.send.limit") | Integer |  |  | Min: 2<br>Max: 64 | Amount of paths to send |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;neighbors</samp>](## "router_bgp.vrfs.[].address_family_ipv4.neighbors") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ip_address</samp>](## "router_bgp.vrfs.[].address_family_ipv4.neighbors.[].ip_address") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "router_bgp.vrfs.[].address_family_ipv4.neighbors.[].activate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp>](## "router_bgp.vrfs.[].address_family_ipv4.neighbors.[].route_map_in") | String |  |  |  | Inbound route-map name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp>](## "router_bgp.vrfs.[].address_family_ipv4.neighbors.[].route_map_out") | String |  |  |  | Outbound route-map name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;next_hop</samp>](## "router_bgp.vrfs.[].address_family_ipv4.neighbors.[].next_hop") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_family_ipv6</samp>](## "router_bgp.vrfs.[].address_family_ipv4.neighbors.[].next_hop.address_family_ipv6") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].address_family_ipv4.neighbors.[].next_hop.address_family_ipv6.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;originate</samp>](## "router_bgp.vrfs.[].address_family_ipv4.neighbors.[].next_hop.address_family_ipv6.originate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;networks</samp>](## "router_bgp.vrfs.[].address_family_ipv4.networks") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- prefix</samp>](## "router_bgp.vrfs.[].address_family_ipv4.networks.[].prefix") | String | Required, Unique |  |  | IPv4 prefix "A.B.C.D/E" |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].address_family_ipv4.networks.[].route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_family_ipv6</samp>](## "router_bgp.vrfs.[].address_family_ipv6") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "router_bgp.vrfs.[].address_family_ipv6.bgp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;missing_policy</samp>](## "router_bgp.vrfs.[].address_family_ipv6.bgp.missing_policy") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction_in_action</samp>](## "router_bgp.vrfs.[].address_family_ipv6.bgp.missing_policy.direction_in_action") | String |  |  | Valid Values:<br>- deny<br>- deny-in-out<br>- permit |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction_out_action</samp>](## "router_bgp.vrfs.[].address_family_ipv6.bgp.missing_policy.direction_out_action") | String |  |  | Valid Values:<br>- deny<br>- deny-in-out<br>- permit |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;additional_paths</samp>](## "router_bgp.vrfs.[].address_family_ipv6.bgp.additional_paths") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;install</samp>](## "router_bgp.vrfs.[].address_family_ipv6.bgp.additional_paths.install") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;install_ecmp_primary</samp>](## "router_bgp.vrfs.[].address_family_ipv6.bgp.additional_paths.install_ecmp_primary") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;receive</samp>](## "router_bgp.vrfs.[].address_family_ipv6.bgp.additional_paths.receive") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send</samp>](## "router_bgp.vrfs.[].address_family_ipv6.bgp.additional_paths.send") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;any</samp>](## "router_bgp.vrfs.[].address_family_ipv6.bgp.additional_paths.send.any") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;backup</samp>](## "router_bgp.vrfs.[].address_family_ipv6.bgp.additional_paths.send.backup") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ecmp</samp>](## "router_bgp.vrfs.[].address_family_ipv6.bgp.additional_paths.send.ecmp") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ecmp_limit</samp>](## "router_bgp.vrfs.[].address_family_ipv6.bgp.additional_paths.send.ecmp_limit") | Integer |  |  | Min: 2<br>Max: 64 | Amount of ECMP paths to send |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;limit</samp>](## "router_bgp.vrfs.[].address_family_ipv6.bgp.additional_paths.send.limit") | Integer |  |  | Min: 2<br>Max: 64 | Amount of paths to send |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;neighbors</samp>](## "router_bgp.vrfs.[].address_family_ipv6.neighbors") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ip_address</samp>](## "router_bgp.vrfs.[].address_family_ipv6.neighbors.[].ip_address") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "router_bgp.vrfs.[].address_family_ipv6.neighbors.[].activate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp>](## "router_bgp.vrfs.[].address_family_ipv6.neighbors.[].route_map_in") | String |  |  |  | Inbound route-map name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp>](## "router_bgp.vrfs.[].address_family_ipv6.neighbors.[].route_map_out") | String |  |  |  | Outbound route-map name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;networks</samp>](## "router_bgp.vrfs.[].address_family_ipv6.networks") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- prefix</samp>](## "router_bgp.vrfs.[].address_family_ipv6.networks.[].prefix") | String | Required, Unique |  |  | IPv6 prefix "A:B:C:D:E:F:G:H/I" |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].address_family_ipv6.networks.[].route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_family_ipv4_multicast</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.bgp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;missing_policy</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.bgp.missing_policy") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction_in_action</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.bgp.missing_policy.direction_in_action") | String |  |  | Valid Values:<br>- deny<br>- deny-in-out<br>- permit |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction_out_action</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.bgp.missing_policy.direction_out_action") | String |  |  | Valid Values:<br>- deny<br>- deny-in-out<br>- permit |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;additional_paths</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.bgp.additional_paths") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;receive</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.bgp.additional_paths.receive") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;neighbors</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.neighbors") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ip_address</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.neighbors.[].ip_address") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.neighbors.[].activate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.neighbors.[].route_map_in") | String |  |  |  | Inbound route-map name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.neighbors.[].route_map_out") | String |  |  |  | Outbound route-map name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;networks</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.networks") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- prefix</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.networks.[].prefix") | String | Required, Unique |  |  | IPv6 prefix "A.B.C.D/E" |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.networks.[].route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_family_ipv6_multicast</samp>](## "router_bgp.vrfs.[].address_family_ipv6_multicast") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "router_bgp.vrfs.[].address_family_ipv6_multicast.bgp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;missing_policy</samp>](## "router_bgp.vrfs.[].address_family_ipv6_multicast.bgp.missing_policy") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction_in_action</samp>](## "router_bgp.vrfs.[].address_family_ipv6_multicast.bgp.missing_policy.direction_in_action") | String |  |  | Valid Values:<br>- deny<br>- deny-in-out<br>- permit |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction_out_action</samp>](## "router_bgp.vrfs.[].address_family_ipv6_multicast.bgp.missing_policy.direction_out_action") | String |  |  | Valid Values:<br>- deny<br>- deny-in-out<br>- permit |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;additional_paths</samp>](## "router_bgp.vrfs.[].address_family_ipv6_multicast.bgp.additional_paths") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;receive</samp>](## "router_bgp.vrfs.[].address_family_ipv6_multicast.bgp.additional_paths.receive") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;neighbors</samp>](## "router_bgp.vrfs.[].address_family_ipv6_multicast.neighbors") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ip_address</samp>](## "router_bgp.vrfs.[].address_family_ipv6_multicast.neighbors.[].ip_address") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "router_bgp.vrfs.[].address_family_ipv6_multicast.neighbors.[].activate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp>](## "router_bgp.vrfs.[].address_family_ipv6_multicast.neighbors.[].route_map_in") | String |  |  |  | Inbound route-map name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp>](## "router_bgp.vrfs.[].address_family_ipv6_multicast.neighbors.[].route_map_out") | String |  |  |  | Outbound route-map name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;networks</samp>](## "router_bgp.vrfs.[].address_family_ipv6_multicast.networks") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- prefix</samp>](## "router_bgp.vrfs.[].address_family_ipv6_multicast.networks.[].prefix") | String | Required, Unique |  |  | IPv6 prefix "A:B:C:D:E:F:G:H/I" |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].address_family_ipv6_multicast.networks.[].route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_family_flow_spec_ipv4</samp>](## "router_bgp.vrfs.[].address_family_flow_spec_ipv4") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "router_bgp.vrfs.[].address_family_flow_spec_ipv4.bgp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;missing_policy</samp>](## "router_bgp.vrfs.[].address_family_flow_spec_ipv4.bgp.missing_policy") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction_in_action</samp>](## "router_bgp.vrfs.[].address_family_flow_spec_ipv4.bgp.missing_policy.direction_in_action") | String |  |  | Valid Values:<br>- deny<br>- deny-in-out<br>- permit |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction_out_action</samp>](## "router_bgp.vrfs.[].address_family_flow_spec_ipv4.bgp.missing_policy.direction_out_action") | String |  |  | Valid Values:<br>- deny<br>- deny-in-out<br>- permit |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;neighbors</samp>](## "router_bgp.vrfs.[].address_family_flow_spec_ipv4.neighbors") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ip_address</samp>](## "router_bgp.vrfs.[].address_family_flow_spec_ipv4.neighbors.[].ip_address") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "router_bgp.vrfs.[].address_family_flow_spec_ipv4.neighbors.[].activate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_family_flow_spec_ipv6</samp>](## "router_bgp.vrfs.[].address_family_flow_spec_ipv6") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "router_bgp.vrfs.[].address_family_flow_spec_ipv6.bgp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;missing_policy</samp>](## "router_bgp.vrfs.[].address_family_flow_spec_ipv6.bgp.missing_policy") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction_in_action</samp>](## "router_bgp.vrfs.[].address_family_flow_spec_ipv6.bgp.missing_policy.direction_in_action") | String |  |  | Valid Values:<br>- deny<br>- deny-in-out<br>- permit |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction_out_action</samp>](## "router_bgp.vrfs.[].address_family_flow_spec_ipv6.bgp.missing_policy.direction_out_action") | String |  |  | Valid Values:<br>- deny<br>- deny-in-out<br>- permit |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;neighbors</samp>](## "router_bgp.vrfs.[].address_family_flow_spec_ipv6.neighbors") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ip_address</samp>](## "router_bgp.vrfs.[].address_family_flow_spec_ipv6.neighbors.[].ip_address") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "router_bgp.vrfs.[].address_family_flow_spec_ipv6.neighbors.[].activate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_families</samp>](## "router_bgp.vrfs.[].address_families") <span style="color:red">deprecated</span> | List, items: Dictionary |  |  |  | <span style="color:red">This key is deprecated. Support will be removed in AVD version v5.0.0. Use <samp>address_family_*</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- address_family</samp>](## "router_bgp.vrfs.[].address_families.[].address_family") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "router_bgp.vrfs.[].address_families.[].bgp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;missing_policy</samp>](## "router_bgp.vrfs.[].address_families.[].bgp.missing_policy") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction_in_action</samp>](## "router_bgp.vrfs.[].address_families.[].bgp.missing_policy.direction_in_action") | String |  |  | Valid Values:<br>- deny<br>- deny-in-out<br>- permit |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction_out_action</samp>](## "router_bgp.vrfs.[].address_families.[].bgp.missing_policy.direction_out_action") | String |  |  | Valid Values:<br>- deny<br>- deny-in-out<br>- permit |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;additional_paths</samp>](## "router_bgp.vrfs.[].address_families.[].bgp.additional_paths") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "router_bgp.vrfs.[].address_families.[].bgp.additional_paths.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;neighbors</samp>](## "router_bgp.vrfs.[].address_families.[].neighbors") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ip_address</samp>](## "router_bgp.vrfs.[].address_families.[].neighbors.[].ip_address") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "router_bgp.vrfs.[].address_families.[].neighbors.[].activate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp>](## "router_bgp.vrfs.[].address_families.[].neighbors.[].route_map_in") | String |  |  |  | Inbound route-map name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp>](## "router_bgp.vrfs.[].address_families.[].neighbors.[].route_map_out") | String |  |  |  | Outbound route-map name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_groups</samp>](## "router_bgp.vrfs.[].address_families.[].peer_groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "router_bgp.vrfs.[].address_families.[].peer_groups.[].name") | String | Required, Unique |  |  | Peer-group name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "router_bgp.vrfs.[].address_families.[].peer_groups.[].activate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;next_hop</samp>](## "router_bgp.vrfs.[].address_families.[].peer_groups.[].next_hop") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_family_ipv6_originate</samp>](## "router_bgp.vrfs.[].address_families.[].peer_groups.[].next_hop.address_family_ipv6_originate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;networks</samp>](## "router_bgp.vrfs.[].address_families.[].networks") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- prefix</samp>](## "router_bgp.vrfs.[].address_families.[].networks.[].prefix") | String | Required, Unique |  |  | IPv4 prefix "A.B.C.D/E" or IPv6 prefix "A:B:C:D:E:F:G:H/I" |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].address_families.[].networks.[].route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;eos_cli</samp>](## "router_bgp.vrfs.[].eos_cli") | String |  |  |  | Multiline EOS CLI rendered directly on the Router BGP, VRF definition in the final EOS configuration<br> |
    | [<samp>&nbsp;&nbsp;session_trackers</samp>](## "router_bgp.session_trackers") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "router_bgp.session_trackers.[].name") | String | Required, Unique |  |  | Name of session tracker |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery_delay</samp>](## "router_bgp.session_trackers.[].recovery_delay") | Integer |  |  | Min: 1<br>Max: 3600 | Recovery delay in seconds |

=== "YAML"

    ```yaml
    router_bgp:
      as: <str>
      router_id: <str>
      distance:
        external_routes: <int>
        internal_routes: <int>
        local_routes: <int>
      graceful_restart:
        enabled: <bool>
        restart_time: <int>
        stalepath_time: <int>
      graceful_restart_helper:
        enabled: <bool>
        restart_time: <int>
        long_lived: <bool>
      maximum_paths:
        paths: <int>
        ecmp: <int>
      updates:
        wait_for_convergence: <bool>
        wait_install: <bool>
      bgp_cluster_id: <str>
      bgp_defaults:
        - <str>
      bgp:
        default:
          ipv4_unicast: <bool>
          ipv4_unicast_transport_ipv6: <bool>
        route_reflector_preserve_attributes:
          enabled: <bool>
          always: <bool>
        bestpath:
          d_path: <bool>
      listen_ranges:
        - prefix: <str>
          peer_id_include_router_id: <bool>
          peer_group: <str>
          peer_filter: <str>
          remote_as: <str>
      peer_groups:
        - name: <str>
          type: <str>
          remote_as: <str>
          local_as: <str>
          description: <str>
          shutdown: <bool>
          as_path:
            remote_as_replace_out: <bool>
            prepend_own_disabled: <bool>
          remove_private_as:
            enabled: <bool>
            all: <bool>
            replace_as: <bool>
          remove_private_as_ingress:
            enabled: <bool>
            replace_as: <bool>
          peer_filter: <str>
          next_hop_unchanged: <bool>
          update_source: <str>
          route_reflector_client: <bool>
          bfd: <bool>
          ebgp_multihop: <int>
          next_hop_self: <bool>
          password: <str>
          passive: <bool>
          default_originate:
            enabled: <bool>
            always: <bool>
            route_map: <str>
          send_community: <str>
          maximum_routes: <int>
          maximum_routes_warning_limit: <str>
          maximum_routes_warning_only: <bool>
          link_bandwidth:
            enabled: <bool>
            default: <str>
          allowas_in:
            enabled: <bool>
            times: <int>
          weight: <int>
          timers: <str>
          rib_in_pre_policy_retain:
            enabled: <bool>
            all: <bool>
          route_map_in: <str>
          route_map_out: <str>
          bgp_listen_range_prefix: <str>
          session_tracker: <str>
      neighbors:
        - ip_address: <str>
          peer_group: <str>
          remote_as: <str>
          local_as: <str>
          as_path:
            remote_as_replace_out: <bool>
            prepend_own_disabled: <bool>
          description: <str>
          route_reflector_client: <bool>
          passive: <bool>
          shutdown: <bool>
          update_source: <str>
          bfd: <bool>
          weight: <int>
          timers: <str>
          route_map_in: <str>
          route_map_out: <str>
          default_originate:
            enabled: <bool>
            always: <bool>
            route_map: <str>
          send_community: <str>
          maximum_routes: <int>
          maximum_routes_warning_limit: <str>
          maximum_routes_warning_only: <bool>
          allowas_in:
            enabled: <bool>
            times: <int>
          ebgp_multihop: <int>
          next_hop_self: <bool>
          link_bandwidth:
            enabled: <bool>
            default: <str>
          rib_in_pre_policy_retain:
            enabled: <bool>
            all: <bool>
          remove_private_as:
            enabled: <bool>
            all: <bool>
            replace_as: <bool>
          remove_private_as_ingress:
            enabled: <bool>
            replace_as: <bool>
          session_tracker: <str>
      neighbor_interfaces:
        - name: <str>
          remote_as: <str>
          peer_group: <str>
          description: <str>
          peer_filter: <str>
      aggregate_addresses:
        - prefix: <str>
          advertise_only: <bool>
          as_set: <bool>
          summary_only: <bool>
          attribute_map: <str>
          match_map: <str>
      redistribute_routes:
        - source_protocol: <str>
          route_map: <str>
          include_leaked: <bool>
      vlan_aware_bundles:
        - name: <str>
          tenant: <str>
          description: <str>
          rd: <str>
          rd_evpn_domain:
            domain: <str>
            rd: <str>
          route_targets:
            both:
              - <str>
            import:
              - <str>
            export:
              - <str>
            import_evpn_domains:
              - domain: <str>
                route_target: <str>
            export_evpn_domains:
              - domain: <str>
                route_target: <str>
            import_export_evpn_domains:
              - domain: <str>
                route_target: <str>
          redistribute_routes:
            - <str>
          no_redistribute_routes:
            - <str>
          vlan: <str>
      vlans:
        - id: <int>
          tenant: <str>
          rd: <str>
          rd_evpn_domain:
            domain: <str>
            rd: <str>
          eos_cli: <str>
          route_targets:
            both:
              - <str>
            import:
              - <str>
            export:
              - <str>
            import_evpn_domains:
              - domain: <str>
                route_target: <str>
            export_evpn_domains:
              - domain: <str>
                route_target: <str>
            import_export_evpn_domains:
              - domain: <str>
                route_target: <str>
          redistribute_routes:
            - <str>
          no_redistribute_routes:
            - <str>
      vpws:
        - name: <str>
          rd: <str>
          route_targets:
            import_export: <str>
          mpls_control_word: <bool>
          label_flow: <bool>
          mtu: <int>
          pseudowires:
            - name: <str>
              id_local: <int>
              id_remote: <int>
      address_family_evpn:
        domain_identifier: <str>
        neighbor_default:
          encapsulation: <str>
          next_hop_self_source_interface: <str>
          next_hop_self_received_evpn_routes:
            enable: <bool>
            inter_domain: <bool>
        peer_groups:
          - name: <str>
            activate: <bool>
            route_map_in: <str>
            route_map_out: <str>
            domain_remote: <bool>
            encapsulation: <str>
        evpn_hostflap_detection:
          enabled: <bool>
          window: <int>
          threshold: <int>
          expiry_timeout: <int>
        route:
          import_match_failure_action: <str>
      address_family_rtc:
        peer_groups:
          - name: <str>
            activate: <bool>
            default_route_target:
              only: <bool>
              encoding_origin_as_omit: <str>
      address_family_ipv4:
        networks:
          - prefix: <str>
            route_map: <str>
        peer_groups:
          - name: <str>
            activate: <bool>
            route_map_in: <str>
            route_map_out: <str>
            default_originate:
              always: <bool>
              route_map: <str>
            next_hop:
              address_family_ipv6:
                enabled: <bool>
                originate: <bool>
              address_family_ipv6_originate: <bool>
            prefix_list_in: <str>
            prefix_list_out: <str>
        neighbors:
          - ip_address: <str>
            activate: <bool>
            route_map_in: <str>
            route_map_out: <str>
            prefix_list_in: <str>
            prefix_list_out: <str>
            default_originate:
              always: <bool>
              route_map: <str>
      address_family_ipv4_multicast:
        peer_groups:
          - name: <str>
            activate: <bool>
            route_map_in: <str>
            route_map_out: <str>
        neighbors:
          - ip_address: <str>
            activate: <bool>
            route_map_in: <str>
            route_map_out: <str>
        redistribute_routes:
          - source_protocol: <str>
            route_map: <str>
      address_family_ipv6:
        networks:
          - prefix: <str>
            route_map: <str>
        peer_groups:
          - name: <str>
            activate: <bool>
            route_map_in: <str>
            route_map_out: <str>
            prefix_list_in: <str>
            prefix_list_out: <str>
        neighbors:
          - ip_address: <str>
            activate: <bool>
            route_map_in: <str>
            route_map_out: <str>
            prefix_list_in: <str>
            prefix_list_out: <str>
        redistribute_routes:
          - source_protocol: <str>
            route_map: <str>
            include_leaked: <bool>
      address_family_ipv6_multicast:
        bgp:
          missing_policy:
            direction_in_action: <str>
            direction_out_action: <str>
          additional_paths:
            receive: <bool>
        neighbors:
          - ip_address: <str>
            activate: <bool>
            route_map_in: <str>
            route_map_out: <str>
        peer_groups:
          - name: <str>
            activate: <bool>
        networks:
          - prefix: <str>
            route_map: <str>
      address_family_flow_spec_ipv4:
        bgp:
          missing_policy:
            direction_in_action: <str>
            direction_out_action: <str>
        neighbors:
          - ip_address: <str>
            activate: <bool>
        peer_groups:
          - name: <str>
            activate: <bool>
      address_family_flow_spec_ipv6:
        bgp:
          missing_policy:
            direction_in_action: <str>
            direction_out_action: <str>
        neighbors:
          - ip_address: <str>
            activate: <bool>
        peer_groups:
          - name: <str>
            activate: <bool>
      address_family_vpn_ipv4:
        domain_identifier: <str>
        peer_groups:
          - name: <str>
            activate: <bool>
            route_map_in: <str>
            route_map_out: <str>
        route:
          import_match_failure_action: <str>
        neighbors:
          - ip_address: <str>
            activate: <bool>
            route_map_in: <str>
            route_map_out: <str>
        neighbor_default_encapsulation_mpls_next_hop_self:
          source_interface: <str>
      address_family_vpn_ipv6:
        domain_identifier: <str>
        peer_groups:
          - name: <str>
            activate: <bool>
            route_map_in: <str>
            route_map_out: <str>
        route:
          import_match_failure_action: <str>
        neighbors:
          - ip_address: <str>
            activate: <bool>
            route_map_in: <str>
            route_map_out: <str>
        neighbor_default_encapsulation_mpls_next_hop_self:
          source_interface: <str>
      vrfs:
        - name: <str>
          rd: <str>
          evpn_multicast: <bool>
          evpn_multicast_address_family:
            ipv4:
              transit: <bool>
          route_targets:
            import:
              - address_family: <str>
                route_targets:
                  - <str>
            export:
              - address_family: <str>
                route_targets:
                  - <str>
          router_id: <str>
          timers: <str>
          networks:
            - prefix: <str>
              route_map: <str>
          updates:
            wait_for_convergence: <bool>
            wait_install: <bool>
          listen_ranges:
            - prefix: <str>
              peer_id_include_router_id: <bool>
              peer_group: <str>
              peer_filter: <str>
              remote_as: <str>
          neighbors:
            - ip_address: <str>
              peer_group: <str>
              remote_as: <str>
              password: <str>
              passive: <bool>
              remove_private_as:
                enabled: <bool>
                all: <bool>
                replace_as: <bool>
              remove_private_as_ingress:
                enabled: <bool>
                replace_as: <bool>
              weight: <int>
              local_as: <str>
              as_path:
                remote_as_replace_out: <bool>
                prepend_own_disabled: <bool>
              description: <str>
              route_reflector_client: <bool>
              ebgp_multihop: <int>
              next_hop_self: <bool>
              shutdown: <bool>
              bfd: <bool>
              timers: <str>
              rib_in_pre_policy_retain:
                enabled: <bool>
                all: <bool>
              send_community: <str>
              maximum_routes: <int>
              maximum_routes_warning_limit: <str>
              maximum_routes_warning_only: <bool>
              allowas_in:
                enabled: <bool>
                times: <int>
              default_originate:
                enabled: <bool>
                always: <bool>
                route_map: <str>
              update_source: <str>
              route_map_in: <str>
              route_map_out: <str>
              prefix_list_in: <str>
              prefix_list_out: <str>
          neighbor_interfaces:
            - name: <str>
              remote_as: <str>
              peer_group: <str>
              peer_filter: <str>
              description: <str>
          redistribute_routes:
            - source_protocol: <str>
              route_map: <str>
              include_leaked: <bool>
          aggregate_addresses:
            - prefix: <str>
              advertise_only: <bool>
              as_set: <bool>
              summary_only: <bool>
              attribute_map: <str>
              match_map: <str>
          address_family_ipv4:
            bgp:
              missing_policy:
                direction_in_action: <str>
                direction_out_action: <str>
              additional_paths:
                install: <bool>
                install_ecmp_primary: <bool>
                receive: <bool>
                send:
                  any: <bool>
                  backup: <bool>
                  ecmp: <bool>
                  ecmp_limit: <int>
                  limit: <int>
            neighbors:
              - ip_address: <str>
                activate: <bool>
                route_map_in: <str>
                route_map_out: <str>
                next_hop:
                  address_family_ipv6:
                    enabled: <bool>
                    originate: <bool>
            networks:
              - prefix: <str>
                route_map: <str>
          address_family_ipv6:
            bgp:
              missing_policy:
                direction_in_action: <str>
                direction_out_action: <str>
              additional_paths:
                install: <bool>
                install_ecmp_primary: <bool>
                receive: <bool>
                send:
                  any: <bool>
                  backup: <bool>
                  ecmp: <bool>
                  ecmp_limit: <int>
                  limit: <int>
            neighbors:
              - ip_address: <str>
                activate: <bool>
                route_map_in: <str>
                route_map_out: <str>
            networks:
              - prefix: <str>
                route_map: <str>
          address_family_ipv4_multicast:
            bgp:
              missing_policy:
                direction_in_action: <str>
                direction_out_action: <str>
              additional_paths:
                receive: <bool>
            neighbors:
              - ip_address: <str>
                activate: <bool>
                route_map_in: <str>
                route_map_out: <str>
            networks:
              - prefix: <str>
                route_map: <str>
          address_family_ipv6_multicast:
            bgp:
              missing_policy:
                direction_in_action: <str>
                direction_out_action: <str>
              additional_paths:
                receive: <bool>
            neighbors:
              - ip_address: <str>
                activate: <bool>
                route_map_in: <str>
                route_map_out: <str>
            networks:
              - prefix: <str>
                route_map: <str>
          address_family_flow_spec_ipv4:
            bgp:
              missing_policy:
                direction_in_action: <str>
                direction_out_action: <str>
            neighbors:
              - ip_address: <str>
                activate: <bool>
          address_family_flow_spec_ipv6:
            bgp:
              missing_policy:
                direction_in_action: <str>
                direction_out_action: <str>
            neighbors:
              - ip_address: <str>
                activate: <bool>
          address_families:
            - address_family: <str>
              bgp:
                missing_policy:
                  direction_in_action: <str>
                  direction_out_action: <str>
                additional_paths:
                  - <str>
              neighbors:
                - ip_address: <str>
                  activate: <bool>
                  route_map_in: <str>
                  route_map_out: <str>
              peer_groups:
                - name: <str>
                  activate: <bool>
                  next_hop:
                    address_family_ipv6_originate: <bool>
              networks:
                - prefix: <str>
                  route_map: <str>
          eos_cli: <str>
      session_trackers:
        - name: <str>
          recovery_delay: <int>
    ```
