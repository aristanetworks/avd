---
search:
  boost: 2
---

# Routing

## ARP

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>arp</samp>](## "arp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;aging</samp>](## "arp.aging") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;timeout_default</samp>](## "arp.aging.timeout_default") | Integer |  |  | Min: 60<br>Max: 65535 | Timeout in seconds |

=== "YAML"

    ```yaml
    arp:
      aging:
        timeout_default: <int>
    ```

## IP Routing

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>ip_routing</samp>](## "ip_routing") | Boolean |  |  |  |  |

=== "YAML"

    ```yaml
    ip_routing: <bool>
    ```

## IP Routing IPv6 Interfaces

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>ip_routing_ipv6_interfaces</samp>](## "ip_routing_ipv6_interfaces") | Boolean |  |  |  |  |

=== "YAML"

    ```yaml
    ip_routing_ipv6_interfaces: <bool>
    ```

## IP Virtual Router MAC Address

MAC address (hh:hh:hh:hh:hh:hh)

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>ip_virtual_router_mac_address</samp>](## "ip_virtual_router_mac_address") | String |  |  |  |  |

=== "YAML"

    ```yaml
    ip_virtual_router_mac_address: <str>
    ```

## IPv6 Static Routes

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>ipv6_static_routes</samp>](## "ipv6_static_routes") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- vrf</samp>](## "ipv6_static_routes.[].vrf") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;destination_address_prefix</samp>](## "ipv6_static_routes.[].destination_address_prefix") | String |  |  |  | IPv6 Network/Mask |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;interface</samp>](## "ipv6_static_routes.[].interface") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;gateway</samp>](## "ipv6_static_routes.[].gateway") | String |  |  |  | IPv6 Address |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;track_bfd</samp>](## "ipv6_static_routes.[].track_bfd") | Boolean |  |  |  | Track next-hop using BFD |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;distance</samp>](## "ipv6_static_routes.[].distance") | Integer |  |  | Min: 1<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;tag</samp>](## "ipv6_static_routes.[].tag") | Integer |  |  | Min: 0<br>Max: 4294967295 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "ipv6_static_routes.[].name") | String |  |  |  | Description |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;metric</samp>](## "ipv6_static_routes.[].metric") | Integer |  |  | Min: 0<br>Max: 4294967295 |  |

=== "YAML"

    ```yaml
    ipv6_static_routes:
      - vrf: <str>
        destination_address_prefix: <str>
        interface: <str>
        gateway: <str>
        track_bfd: <bool>
        distance: <int>
        tag: <int>
        name: <str>
        metric: <int>
    ```

## IPv6 Unicast Routing

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>ipv6_unicast_routing</samp>](## "ipv6_unicast_routing") | Boolean |  |  |  |  |

=== "YAML"

    ```yaml
    ipv6_unicast_routing: <bool>
    ```

## Router BFD

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>router_bfd</samp>](## "router_bfd") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;interval</samp>](## "router_bfd.interval") | Integer |  |  |  | Rate in milliseconds |
    | [<samp>&nbsp;&nbsp;min_rx</samp>](## "router_bfd.min_rx") | Integer |  |  |  | Rate in milliseconds |
    | [<samp>&nbsp;&nbsp;multiplier</samp>](## "router_bfd.multiplier") | Integer |  |  | Min: 3<br>Max: 50 |  |
    | [<samp>&nbsp;&nbsp;multihop</samp>](## "router_bfd.multihop") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "router_bfd.multihop.interval") | Integer |  |  |  | Rate in milliseconds |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;min_rx</samp>](## "router_bfd.multihop.min_rx") | Integer |  |  |  | Rate in milliseconds |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;multiplier</samp>](## "router_bfd.multihop.multiplier") | Integer |  |  | Min: 3<br>Max: 50 |  |
    | [<samp>&nbsp;&nbsp;sbfd</samp>](## "router_bfd.sbfd") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;local_interface</samp>](## "router_bfd.sbfd.local_interface") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "router_bfd.sbfd.local_interface.name") | String |  |  |  | Interface Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;protocols</samp>](## "router_bfd.sbfd.local_interface.protocols") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp>](## "router_bfd.sbfd.local_interface.protocols.ipv4") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6</samp>](## "router_bfd.sbfd.local_interface.protocols.ipv6") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;initiator_interval</samp>](## "router_bfd.sbfd.initiator_interval") | Integer |  |  |  | Rate in milliseconds |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;initiator_multiplier</samp>](## "router_bfd.sbfd.initiator_multiplier") | Integer |  |  | Min: 3<br>Max: 50 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;reflector</samp>](## "router_bfd.sbfd.reflector") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;min_rx</samp>](## "router_bfd.sbfd.reflector.min_rx") | Integer |  |  |  | Rate in milliseconds |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_discriminator</samp>](## "router_bfd.sbfd.reflector.local_discriminator") | String |  |  |  | IPv4 address or 32 bit integer |

=== "YAML"

    ```yaml
    router_bfd:
      interval: <int>
      min_rx: <int>
      multiplier: <int>
      multihop:
        interval: <int>
        min_rx: <int>
        multiplier: <int>
      sbfd:
        local_interface:
          name: <str>
          protocols:
            ipv4: <bool>
            ipv6: <bool>
        initiator_interval: <int>
        initiator_multiplier: <int>
        reflector:
          min_rx: <int>
          local_discriminator: <str>
    ```

## Router BGP

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>router_bgp</samp>](## "router_bgp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;as</samp>](## "router_bgp.as") | String |  |  |  | BGP AS <1-4294967295> or AS number in asdot notation <1-65535>.<0-65535> |
    | [<samp>&nbsp;&nbsp;router_id</samp>](## "router_bgp.router_id") | String |  |  |  | In IP address format A.B.C.D |
    | [<samp>&nbsp;&nbsp;distance</samp>](## "router_bgp.distance") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;external_routes</samp>](## "router_bgp.distance.external_routes") | Integer |  |  | Min: 1<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;internal_routes</samp>](## "router_bgp.distance.internal_routes") | Integer |  |  | Min: 1<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;local_routes</samp>](## "router_bgp.distance.local_routes") | Integer |  |  | Min: 1<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;graceful_restart</samp>](## "router_bgp.graceful_restart") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.graceful_restart.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;restart_time</samp>](## "router_bgp.graceful_restart.restart_time") | Integer |  |  | Min: 1<br>Max: 3600 | Number of seconds |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;stalepath_time</samp>](## "router_bgp.graceful_restart.stalepath_time") | Integer |  |  | Min: 1<br>Max: 3600 | Number of seconds |
    | [<samp>&nbsp;&nbsp;graceful_restart_helper</samp>](## "router_bgp.graceful_restart_helper") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.graceful_restart_helper.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;restart_time</samp>](## "router_bgp.graceful_restart_helper.restart_time") | Integer |  |  | Min: 1<br>Max: 100000000 | Number of seconds<br>graceful-restart-help long-lived and restart-time are mutually exclusive in CLI.<br>restart-time will take precedence if both are configured.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;long_lived</samp>](## "router_bgp.graceful_restart_helper.long_lived") | Boolean |  |  |  | graceful-restart-help long-lived and restart-time are mutually exclusive in CLI.<br>restart-time will take precedence if both are configured.<br> |
    | [<samp>&nbsp;&nbsp;maximum_paths</samp>](## "router_bgp.maximum_paths") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;paths</samp>](## "router_bgp.maximum_paths.paths") | Integer |  |  | Min: 1<br>Max: 600 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ecmp</samp>](## "router_bgp.maximum_paths.ecmp") | Integer |  |  | Min: 1<br>Max: 600 |  |
    | [<samp>&nbsp;&nbsp;updates</samp>](## "router_bgp.updates") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;wait_for_convergence</samp>](## "router_bgp.updates.wait_for_convergence") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;wait_install</samp>](## "router_bgp.updates.wait_install") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;bgp_cluster_id</samp>](## "router_bgp.bgp_cluster_id") | String |  |  |  | IP Address A.B.C.D |
    | [<samp>&nbsp;&nbsp;bgp_defaults</samp>](## "router_bgp.bgp_defaults") | List, items: String |  |  |  | BGP command as string |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "router_bgp.bgp_defaults.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;bgp</samp>](## "router_bgp.bgp") | Dictionary |  |  |  |  |
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
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_filter</samp>](## "router_bgp.peer_groups.[].peer_filter") | String |  |  |  | Peer-filter name<br>note: `bgp_listen_range_prefix` and `peer_filter` will be deprecated in AVD v4.0<br>These should not be mixed with the new `listen_ranges` key above to avoid conflicts.<br> |
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
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_listen_range_prefix</samp>](## "router_bgp.peer_groups.[].bgp_listen_range_prefix") | String |  |  |  | IP prefix range<br>note: `bgp_listen_range_prefix` and `peer_filter` will be deprecated in AVD v4.0<br>These should not be mixed with the new `listen_ranges` key above to avoid conflicts.<br> |
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
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_group</samp>](## "router_bgp.neighbor_interfaces.[].peer_group") | String |  | Peer-group name |  |  |
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
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_family_ipv6_originate</samp>](## "router_bgp.address_family_ipv4.peer_groups.[].next_hop.address_family_ipv6_originate") | Boolean |  |  |  |  |
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
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;aggregate_addresses</samp>](## "router_bgp.vrfs.[].aggregate_addresses") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- prefix</samp>](## "router_bgp.vrfs.[].aggregate_addresses.[].prefix") | String | Required, Unique |  |  | IPv4 prefix "A.B.C.D/E" or IPv6 prefix "A:B:C:D:E:F:G:H/I" |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;advertise_only</samp>](## "router_bgp.vrfs.[].aggregate_addresses.[].advertise_only") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;as_set</samp>](## "router_bgp.vrfs.[].aggregate_addresses.[].as_set") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;summary_only</samp>](## "router_bgp.vrfs.[].aggregate_addresses.[].summary_only") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;attribute_map</samp>](## "router_bgp.vrfs.[].aggregate_addresses.[].attribute_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_map</samp>](## "router_bgp.vrfs.[].aggregate_addresses.[].match_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_families</samp>](## "router_bgp.vrfs.[].address_families") | List, items: Dictionary |  |  |  |  |
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
          aggregate_addresses:
            - prefix: <str>
              advertise_only: <bool>
              as_set: <bool>
              summary_only: <bool>
              attribute_map: <str>
              match_map: <str>
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

## Router General configuration

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>router_general</samp>](## "router_general") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;router_id</samp>](## "router_general.router_id") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp>](## "router_general.router_id.ipv4") | String |  |  |  | IPv4 Address |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6</samp>](## "router_general.router_id.ipv6") | String |  |  |  | IPv6 Address |
    | [<samp>&nbsp;&nbsp;nexthop_fast_failover</samp>](## "router_general.nexthop_fast_failover") | Boolean |  | False |  |  |
    | [<samp>&nbsp;&nbsp;vrfs</samp>](## "router_general.vrfs") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "router_general.vrfs.[].name") | String | Required, Unique |  |  | Destination-VRF |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;leak_routes</samp>](## "router_general.vrfs.[].leak_routes") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- source_vrf</samp>](## "router_general.vrfs.[].leak_routes.[].source_vrf") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;subscribe_policy</samp>](## "router_general.vrfs.[].leak_routes.[].subscribe_policy") | String |  |  |  | Route-Map Policy |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;routes</samp>](## "router_general.vrfs.[].routes") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dynamic_prefix_lists</samp>](## "router_general.vrfs.[].routes.dynamic_prefix_lists") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "router_general.vrfs.[].routes.dynamic_prefix_lists.[].name") | String |  |  |  | Dynamic Prefix List Name |

=== "YAML"

    ```yaml
    router_general:
      router_id:
        ipv4: <str>
        ipv6: <str>
      nexthop_fast_failover: <bool>
      vrfs:
        - name: <str>
          leak_routes:
            - source_vrf: <str>
              subscribe_policy: <str>
          routes:
            dynamic_prefix_lists:
              - name: <str>
    ```

## Router IGMP Configuration

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>router_igmp</samp>](## "router_igmp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;ssm_aware</samp>](## "router_igmp.ssm_aware") | Boolean |  |  |  |  |

=== "YAML"

    ```yaml
    router_igmp:
      ssm_aware: <bool>
    ```

## Router ISIS

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>router_isis</samp>](## "router_isis") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;instance</samp>](## "router_isis.instance") | String |  |  |  | ISIS Instance Name |
    | [<samp>&nbsp;&nbsp;net</samp>](## "router_isis.net") | String |  |  |  | CLNS Address like "49.0001.0001.0000.0001.00" |
    | [<samp>&nbsp;&nbsp;router_id</samp>](## "router_isis.router_id") | String |  |  |  | IPv4 Address |
    | [<samp>&nbsp;&nbsp;is_type</samp>](## "router_isis.is_type") | String |  |  | Valid Values:<br>- level-1<br>- level-1-2<br>- level-2 |  |
    | [<samp>&nbsp;&nbsp;log_adjacency_changes</samp>](## "router_isis.log_adjacency_changes") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;mpls_ldp_sync_default</samp>](## "router_isis.mpls_ldp_sync_default") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;timers</samp>](## "router_isis.timers") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;local_convergence</samp>](## "router_isis.timers.local_convergence") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;protected_prefixes</samp>](## "router_isis.timers.local_convergence.protected_prefixes") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;delay</samp>](## "router_isis.timers.local_convergence.delay") | Integer |  | 10000 |  | Delay in milliseconds. |
    | [<samp>&nbsp;&nbsp;advertise</samp>](## "router_isis.advertise") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;passive_only</samp>](## "router_isis.advertise.passive_only") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;address_family</samp>](## "router_isis.address_family") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "router_isis.address_family.[].&lt;str&gt;") | String |  |  | Valid Values:<br>- ipv4<br>- ipv6<br>- ipv4 unicast<br>- ipv6 unicast | Address Family |
    | [<samp>&nbsp;&nbsp;isis_af_defaults</samp>](## "router_isis.isis_af_defaults") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "router_isis.isis_af_defaults.[].&lt;str&gt;") | String |  |  |  | EOS CLI rendered under the address families<br>Example "maximum-paths 64"<br> |
    | [<samp>&nbsp;&nbsp;redistribute_routes</samp>](## "router_isis.redistribute_routes") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- source_protocol</samp>](## "router_isis.redistribute_routes.[].source_protocol") | String | Required |  | Valid Values:<br>- bgp<br>- connected<br>- isis<br>- ospf<br>- ospfv3<br>- static |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_isis.redistribute_routes.[].route_map") | String |  |  |  | Route-map name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_isis.redistribute_routes.[].include_leaked") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ospf_route_type</samp>](## "router_isis.redistribute_routes.[].ospf_route_type") | String |  |  | Valid Values:<br>- external<br>- internal<br>- nssa-external | ospf_route_type is required with source_protocols 'ospf' and 'ospfv3' |
    | [<samp>&nbsp;&nbsp;address_family_ipv4</samp>](## "router_isis.address_family_ipv4") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;maximum_paths</samp>](## "router_isis.address_family_ipv4.maximum_paths") | Integer |  |  | Min: 1<br>Max: 128 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;fast_reroute_ti_lfa</samp>](## "router_isis.address_family_ipv4.fast_reroute_ti_lfa") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "router_isis.address_family_ipv4.fast_reroute_ti_lfa.mode") | String |  |  | Valid Values:<br>- link-protection<br>- node-protection |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp>](## "router_isis.address_family_ipv4.fast_reroute_ti_lfa.level") | String |  |  | Valid Values:<br>- level-1<br>- level-2 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;srlg</samp>](## "router_isis.address_family_ipv4.fast_reroute_ti_lfa.srlg") | Dictionary |  |  |  | Shared Risk Link Group |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable</samp>](## "router_isis.address_family_ipv4.fast_reroute_ti_lfa.srlg.enable") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;strict</samp>](## "router_isis.address_family_ipv4.fast_reroute_ti_lfa.srlg.strict") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;tunnel_source_labeled_unicast</samp>](## "router_isis.address_family_ipv4.tunnel_source_labeled_unicast") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_isis.address_family_ipv4.tunnel_source_labeled_unicast.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf</samp>](## "router_isis.address_family_ipv4.tunnel_source_labeled_unicast.rcf") | String |  |  |  | Route Control Function |
    | [<samp>&nbsp;&nbsp;address_family_ipv6</samp>](## "router_isis.address_family_ipv6") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;maximum_paths</samp>](## "router_isis.address_family_ipv6.maximum_paths") | Integer |  |  | Min: 1<br>Max: 128 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;fast_reroute_ti_lfa</samp>](## "router_isis.address_family_ipv6.fast_reroute_ti_lfa") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "router_isis.address_family_ipv6.fast_reroute_ti_lfa.mode") | String |  |  | Valid Values:<br>- link-protection<br>- node-protection |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp>](## "router_isis.address_family_ipv6.fast_reroute_ti_lfa.level") | String |  |  | Valid Values:<br>- level-1<br>- level-2 | Optional, default is to protect all levels |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;srlg</samp>](## "router_isis.address_family_ipv6.fast_reroute_ti_lfa.srlg") | Dictionary |  |  |  | Shared Risk Link Group |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable</samp>](## "router_isis.address_family_ipv6.fast_reroute_ti_lfa.srlg.enable") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;strict</samp>](## "router_isis.address_family_ipv6.fast_reroute_ti_lfa.srlg.strict") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;segment_routing_mpls</samp>](## "router_isis.segment_routing_mpls") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_isis.segment_routing_mpls.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;router_id</samp>](## "router_isis.segment_routing_mpls.router_id") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;prefix_segments</samp>](## "router_isis.segment_routing_mpls.prefix_segments") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- prefix</samp>](## "router_isis.segment_routing_mpls.prefix_segments.[].prefix") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;index</samp>](## "router_isis.segment_routing_mpls.prefix_segments.[].index") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;no_passive_interfaces</samp>](## "router_isis.no_passive_interfaces") | List |  |  |  | Unused key - to be removed from eos_designs. |

=== "YAML"

    ```yaml
    router_isis:
      instance: <str>
      net: <str>
      router_id: <str>
      is_type: <str>
      log_adjacency_changes: <bool>
      mpls_ldp_sync_default: <bool>
      timers:
        local_convergence:
          protected_prefixes: <bool>
          delay: <int>
      advertise:
        passive_only: <bool>
      address_family:
        - <str>
      isis_af_defaults:
        - <str>
      redistribute_routes:
        - source_protocol: <str>
          route_map: <str>
          include_leaked: <bool>
          ospf_route_type: <str>
      address_family_ipv4:
        maximum_paths: <int>
        fast_reroute_ti_lfa:
          mode: <str>
          level: <str>
          srlg:
            enable: <bool>
            strict: <bool>
        tunnel_source_labeled_unicast:
          enabled: <bool>
          rcf: <str>
      address_family_ipv6:
        maximum_paths: <int>
        fast_reroute_ti_lfa:
          mode: <str>
          level: <str>
          srlg:
            enable: <bool>
            strict: <bool>
      segment_routing_mpls:
        enabled: <bool>
        router_id: <str>
        prefix_segments:
          - prefix: <str>
            index: <int>
      no_passive_interfaces:
    ```

## Router L2 VPN

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>router_l2_vpn</samp>](## "router_l2_vpn") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;arp_learning_bridged</samp>](## "router_l2_vpn.arp_learning_bridged") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;arp_proxy</samp>](## "router_l2_vpn.arp_proxy") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;prefix_list</samp>](## "router_l2_vpn.arp_proxy.prefix_list") | String |  |  |  | Prefix-list name. ARP Proxying is disabled for IPv4 addresses defined in the prefix-list. |
    | [<samp>&nbsp;&nbsp;arp_selective_install</samp>](## "router_l2_vpn.arp_selective_install") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;nd_learning_bridged</samp>](## "router_l2_vpn.nd_learning_bridged") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;nd_proxy</samp>](## "router_l2_vpn.nd_proxy") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;prefix_list</samp>](## "router_l2_vpn.nd_proxy.prefix_list") | String |  |  |  | Prefix-list name. ND Proxying is disabled for IPv6 addresses defined in the prefix-list. |
    | [<samp>&nbsp;&nbsp;nd_rs_flooding_disabled</samp>](## "router_l2_vpn.nd_rs_flooding_disabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;virtual_router_nd_ra_flooding_disabled</samp>](## "router_l2_vpn.virtual_router_nd_ra_flooding_disabled") | Boolean |  |  |  |  |

=== "YAML"

    ```yaml
    router_l2_vpn:
      arp_learning_bridged: <bool>
      arp_proxy:
        prefix_list: <str>
      arp_selective_install: <bool>
      nd_learning_bridged: <bool>
      nd_proxy:
        prefix_list: <str>
      nd_rs_flooding_disabled: <bool>
      virtual_router_nd_ra_flooding_disabled: <bool>
    ```

## Router Msdp

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>router_msdp</samp>](## "router_msdp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;originator_id_local_interface</samp>](## "router_msdp.originator_id_local_interface") | String |  |  |  | Interface to use for originator ID |
    | [<samp>&nbsp;&nbsp;rejected_limit</samp>](## "router_msdp.rejected_limit") | Integer |  |  | Min: 0<br>Max: 40000 | Maximum number of rejected SA messages allowed in cache |
    | [<samp>&nbsp;&nbsp;forward_register_packets</samp>](## "router_msdp.forward_register_packets") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;connection_retry_interval</samp>](## "router_msdp.connection_retry_interval") | Integer |  |  | Min: 1<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;group_limits</samp>](## "router_msdp.group_limits") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- source_prefix</samp>](## "router_msdp.group_limits.[].source_prefix") | String | Required, Unique |  |  | Source address prefix |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;limit</samp>](## "router_msdp.group_limits.[].limit") | Integer | Required |  | Min: 0<br>Max: 40000 | Limit for SAs matching the source address prefix |
    | [<samp>&nbsp;&nbsp;peers</samp>](## "router_msdp.peers") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- ipv4_address</samp>](## "router_msdp.peers.[].ipv4_address") | String | Required, Unique |  |  | Peer IP Address |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default_peer</samp>](## "router_msdp.peers.[].default_peer") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_msdp.peers.[].default_peer.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list</samp>](## "router_msdp.peers.[].default_peer.prefix_list") | String |  |  |  | Prefix list to filter source of SA messages |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_interface</samp>](## "router_msdp.peers.[].local_interface") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "router_msdp.peers.[].description") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;disabled</samp>](## "router_msdp.peers.[].disabled") | Boolean |  |  |  | Disable the MSDP peer |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sa_limit</samp>](## "router_msdp.peers.[].sa_limit") | Integer |  |  | Min: 0<br>Max: 40000 | Maximum number of SA messages allowed in cache |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mesh_groups</samp>](## "router_msdp.peers.[].mesh_groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "router_msdp.peers.[].mesh_groups.[].name") | String | Required, Unique |  |  | Mesh group name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;keepalive</samp>](## "router_msdp.peers.[].keepalive") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;keepalive_timer</samp>](## "router_msdp.peers.[].keepalive.keepalive_timer") | Integer | Required |  | Min: 1<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hold_timer</samp>](## "router_msdp.peers.[].keepalive.hold_timer") | Integer | Required |  | Min: 1<br>Max: 65535 | Must be greater than keepalive timer |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sa_filter</samp>](## "router_msdp.peers.[].sa_filter") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;in_list</samp>](## "router_msdp.peers.[].sa_filter.in_list") | String |  |  |  | ACL to filter inbound SA messages |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;out_list</samp>](## "router_msdp.peers.[].sa_filter.out_list") | String |  |  |  | ACL to filter outbound SA messages |
    | [<samp>&nbsp;&nbsp;vrfs</samp>](## "router_msdp.vrfs") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "router_msdp.vrfs.[].name") | String | Required, Unique |  |  | VRF name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;originator_id_local_interface</samp>](## "router_msdp.vrfs.[].originator_id_local_interface") | String |  |  |  | Interface to use for originator ID |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rejected_limit</samp>](## "router_msdp.vrfs.[].rejected_limit") | Integer |  |  | Min: 0<br>Max: 40000 | Maximum number of rejected SA messages allowed in cache |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;forward_register_packets</samp>](## "router_msdp.vrfs.[].forward_register_packets") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;connection_retry_interval</samp>](## "router_msdp.vrfs.[].connection_retry_interval") | Integer |  |  | Min: 1<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group_limits</samp>](## "router_msdp.vrfs.[].group_limits") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- source_prefix</samp>](## "router_msdp.vrfs.[].group_limits.[].source_prefix") | String | Required, Unique |  |  | Source address prefix |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;limit</samp>](## "router_msdp.vrfs.[].group_limits.[].limit") | Integer | Required |  | Min: 0<br>Max: 40000 | Limit for SAs matching the source address prefix |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peers</samp>](## "router_msdp.vrfs.[].peers") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ipv4_address</samp>](## "router_msdp.vrfs.[].peers.[].ipv4_address") | String | Required, Unique |  |  | Peer IP Address |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default_peer</samp>](## "router_msdp.vrfs.[].peers.[].default_peer") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_msdp.vrfs.[].peers.[].default_peer.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list</samp>](## "router_msdp.vrfs.[].peers.[].default_peer.prefix_list") | String |  |  |  | Prefix list to filter source of SA messages |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_interface</samp>](## "router_msdp.vrfs.[].peers.[].local_interface") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "router_msdp.vrfs.[].peers.[].description") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;disabled</samp>](## "router_msdp.vrfs.[].peers.[].disabled") | Boolean |  |  |  | Disable the MSDP peer |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sa_limit</samp>](## "router_msdp.vrfs.[].peers.[].sa_limit") | Integer |  |  | Min: 0<br>Max: 40000 | Maximum number of SA messages allowed in cache |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mesh_groups</samp>](## "router_msdp.vrfs.[].peers.[].mesh_groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "router_msdp.vrfs.[].peers.[].mesh_groups.[].name") | String | Required, Unique |  |  | Mesh group name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;keepalive</samp>](## "router_msdp.vrfs.[].peers.[].keepalive") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;keepalive_timer</samp>](## "router_msdp.vrfs.[].peers.[].keepalive.keepalive_timer") | Integer | Required |  | Min: 1<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hold_timer</samp>](## "router_msdp.vrfs.[].peers.[].keepalive.hold_timer") | Integer | Required |  | Min: 1<br>Max: 65535 | Must be greater than keepalive timer |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sa_filter</samp>](## "router_msdp.vrfs.[].peers.[].sa_filter") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;in_list</samp>](## "router_msdp.vrfs.[].peers.[].sa_filter.in_list") | String |  |  |  | ACL to filter inbound SA messages |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;out_list</samp>](## "router_msdp.vrfs.[].peers.[].sa_filter.out_list") | String |  |  |  | ACL to filter outbound SA messages |

=== "YAML"

    ```yaml
    router_msdp:
      originator_id_local_interface: <str>
      rejected_limit: <int>
      forward_register_packets: <bool>
      connection_retry_interval: <int>
      group_limits:
        - source_prefix: <str>
          limit: <int>
      peers:
        - ipv4_address: <str>
          default_peer:
            enabled: <bool>
            prefix_list: <str>
          local_interface: <str>
          description: <str>
          disabled: <bool>
          sa_limit: <int>
          mesh_groups:
            - name: <str>
          keepalive:
            keepalive_timer: <int>
            hold_timer: <int>
          sa_filter:
            in_list: <str>
            out_list: <str>
      vrfs:
        - name: <str>
          originator_id_local_interface: <str>
          rejected_limit: <int>
          forward_register_packets: <bool>
          connection_retry_interval: <int>
          group_limits:
            - source_prefix: <str>
              limit: <int>
          peers:
            - ipv4_address: <str>
              default_peer:
                enabled: <bool>
                prefix_list: <str>
              local_interface: <str>
              description: <str>
              disabled: <bool>
              sa_limit: <int>
              mesh_groups:
                - name: <str>
              keepalive:
                keepalive_timer: <int>
                hold_timer: <int>
              sa_filter:
                in_list: <str>
                out_list: <str>
    ```

## Router OSPF Configuration

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>router_ospf</samp>](## "router_ospf") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;process_ids</samp>](## "router_ospf.process_ids") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- id</samp>](## "router_ospf.process_ids.[].id") | Integer | Required, Unique |  |  | OSPF Process ID |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "router_ospf.process_ids.[].vrf") | String |  |  |  | VRF Name for OSPF Process |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;passive_interface_default</samp>](## "router_ospf.process_ids.[].passive_interface_default") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;router_id</samp>](## "router_ospf.process_ids.[].router_id") | String |  |  |  | IPv4 Address |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;distance</samp>](## "router_ospf.process_ids.[].distance") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;external</samp>](## "router_ospf.process_ids.[].distance.external") | Integer |  |  | Min: 1<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inter_area</samp>](## "router_ospf.process_ids.[].distance.inter_area") | Integer |  |  | Min: 1<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;intra_area</samp>](## "router_ospf.process_ids.[].distance.intra_area") | Integer |  |  | Min: 1<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;log_adjacency_changes_detail</samp>](## "router_ospf.process_ids.[].log_adjacency_changes_detail") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;network_prefixes</samp>](## "router_ospf.process_ids.[].network_prefixes") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ipv4_prefix</samp>](## "router_ospf.process_ids.[].network_prefixes.[].ipv4_prefix") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;area</samp>](## "router_ospf.process_ids.[].network_prefixes.[].area") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bfd_enable</samp>](## "router_ospf.process_ids.[].bfd_enable") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bfd_adjacency_state_any</samp>](## "router_ospf.process_ids.[].bfd_adjacency_state_any") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;no_passive_interfaces</samp>](## "router_ospf.process_ids.[].no_passive_interfaces") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "router_ospf.process_ids.[].no_passive_interfaces.[].&lt;str&gt;") | String |  |  |  | Interface Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;distribute_list_in</samp>](## "router_ospf.process_ids.[].distribute_list_in") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_ospf.process_ids.[].distribute_list_in.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_lsa</samp>](## "router_ospf.process_ids.[].max_lsa") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timers</samp>](## "router_ospf.process_ids.[].timers") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lsa</samp>](## "router_ospf.process_ids.[].timers.lsa") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rx_min_interval</samp>](## "router_ospf.process_ids.[].timers.lsa.rx_min_interval") | Integer |  |  | Min: 0<br>Max: 600000 | Min interval in msecs between accepting the same LSA |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tx_delay</samp>](## "router_ospf.process_ids.[].timers.lsa.tx_delay") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;initial</samp>](## "router_ospf.process_ids.[].timers.lsa.tx_delay.initial") | Integer |  |  | Min: 0<br>Max: 600000 | Delay to generate first occurrence of LSA in msecs |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;min</samp>](## "router_ospf.process_ids.[].timers.lsa.tx_delay.min") | Integer |  |  | Min: 1<br>Max: 600000 | Min delay between originating the same LSA in msecs |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max</samp>](## "router_ospf.process_ids.[].timers.lsa.tx_delay.max") | Integer |  |  | Min: 1<br>Max: 600000 | 1-600000 Maximum delay between originating the same LSA in msec |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;spf_delay</samp>](## "router_ospf.process_ids.[].timers.spf_delay") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;initial</samp>](## "router_ospf.process_ids.[].timers.spf_delay.initial") | Integer |  |  | Min: 0<br>Max: 600000 | Initial SPF schedule delay in msecs |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;min</samp>](## "router_ospf.process_ids.[].timers.spf_delay.min") | Integer |  |  | Min: 0<br>Max: 65535000 | Min Hold time between two SPFs in msecs |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max</samp>](## "router_ospf.process_ids.[].timers.spf_delay.max") | Integer |  |  | Min: 0<br>Max: 65535000 | Max wait time between two SPFs in msecs |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default_information_originate</samp>](## "router_ospf.process_ids.[].default_information_originate") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always</samp>](## "router_ospf.process_ids.[].default_information_originate.always") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;summary_addresses</samp>](## "router_ospf.process_ids.[].summary_addresses") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- prefix</samp>](## "router_ospf.process_ids.[].summary_addresses.[].prefix") | String | Required, Unique |  |  | Summary Prefix Address |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tag</samp>](## "router_ospf.process_ids.[].summary_addresses.[].tag") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;attribute_map</samp>](## "router_ospf.process_ids.[].summary_addresses.[].attribute_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;not_advertise</samp>](## "router_ospf.process_ids.[].summary_addresses.[].not_advertise") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;redistribute</samp>](## "router_ospf.process_ids.[].redistribute") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;static</samp>](## "router_ospf.process_ids.[].redistribute.static") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_ospf.process_ids.[].redistribute.static.route_map") | String |  |  |  | Route Map Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_ospf.process_ids.[].redistribute.static.include_leaked") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;connected</samp>](## "router_ospf.process_ids.[].redistribute.connected") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_ospf.process_ids.[].redistribute.connected.route_map") | String |  |  |  | Route Map Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_ospf.process_ids.[].redistribute.connected.include_leaked") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "router_ospf.process_ids.[].redistribute.bgp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_ospf.process_ids.[].redistribute.bgp.route_map") | String |  |  |  | Route Map Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_ospf.process_ids.[].redistribute.bgp.include_leaked") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;auto_cost_reference_bandwidth</samp>](## "router_ospf.process_ids.[].auto_cost_reference_bandwidth") | Integer |  |  |  | Bandwidth in mbps |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;areas</samp>](## "router_ospf.process_ids.[].areas") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- id</samp>](## "router_ospf.process_ids.[].areas.[].id") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;filter</samp>](## "router_ospf.process_ids.[].areas.[].filter") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;networks</samp>](## "router_ospf.process_ids.[].areas.[].filter.networks") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "router_ospf.process_ids.[].areas.[].filter.networks.[].&lt;str&gt;") | String |  |  |  | IPv4 Prefix |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list</samp>](## "router_ospf.process_ids.[].areas.[].filter.prefix_list") | String |  |  |  | Prefix-List Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "router_ospf.process_ids.[].areas.[].type") | String |  | normal | Valid Values:<br>- normal<br>- stub<br>- nssa |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;no_summary</samp>](## "router_ospf.process_ids.[].areas.[].no_summary") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nssa_only</samp>](## "router_ospf.process_ids.[].areas.[].nssa_only") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default_information_originate</samp>](## "router_ospf.process_ids.[].areas.[].default_information_originate") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;metric</samp>](## "router_ospf.process_ids.[].areas.[].default_information_originate.metric") | Integer |  |  | Min: 1<br>Max: 65535 | Metric for default route |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;metric_type</samp>](## "router_ospf.process_ids.[].areas.[].default_information_originate.metric_type") | Integer |  |  | Valid Values:<br>- 1<br>- 2 | OSPF metric type for default route |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_paths</samp>](## "router_ospf.process_ids.[].maximum_paths") | Integer |  |  | Min: 1<br>Max: 128 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_metric</samp>](## "router_ospf.process_ids.[].max_metric") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;router_lsa</samp>](## "router_ospf.process_ids.[].max_metric.router_lsa") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;external_lsa</samp>](## "router_ospf.process_ids.[].max_metric.router_lsa.external_lsa") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;override_metric</samp>](## "router_ospf.process_ids.[].max_metric.router_lsa.external_lsa.override_metric") | Integer |  |  | Min: 1<br>Max: 16777215 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_stub</samp>](## "router_ospf.process_ids.[].max_metric.router_lsa.include_stub") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;on_startup</samp>](## "router_ospf.process_ids.[].max_metric.router_lsa.on_startup") | String |  |  |  | "wait-for-bgp" or Integer 5-86400<br>Example: "wait-for-bgp" Or "222"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;summary_lsa</samp>](## "router_ospf.process_ids.[].max_metric.router_lsa.summary_lsa") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;override_metric</samp>](## "router_ospf.process_ids.[].max_metric.router_lsa.summary_lsa.override_metric") | Integer |  |  | Min: 1<br>Max: 16777215 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls_ldp_sync_default</samp>](## "router_ospf.process_ids.[].mpls_ldp_sync_default") | Boolean |  |  |  |  |

=== "YAML"

    ```yaml
    router_ospf:
      process_ids:
        - id: <int>
          vrf: <str>
          passive_interface_default: <bool>
          router_id: <str>
          distance:
            external: <int>
            inter_area: <int>
            intra_area: <int>
          log_adjacency_changes_detail: <bool>
          network_prefixes:
            - ipv4_prefix: <str>
              area: <str>
          bfd_enable: <bool>
          bfd_adjacency_state_any: <bool>
          no_passive_interfaces:
            - <str>
          distribute_list_in:
            route_map: <str>
          max_lsa: <int>
          timers:
            lsa:
              rx_min_interval: <int>
              tx_delay:
                initial: <int>
                min: <int>
                max: <int>
            spf_delay:
              initial: <int>
              min: <int>
              max: <int>
          default_information_originate:
            always: <bool>
          summary_addresses:
            - prefix: <str>
              tag: <int>
              attribute_map: <str>
              not_advertise: <bool>
          redistribute:
            static:
              route_map: <str>
              include_leaked: <bool>
            connected:
              route_map: <str>
              include_leaked: <bool>
            bgp:
              route_map: <str>
              include_leaked: <bool>
          auto_cost_reference_bandwidth: <int>
          areas:
            - id: <str>
              filter:
                networks:
                  - <str>
                prefix_list: <str>
              type: <str>
              no_summary: <bool>
              nssa_only: <bool>
              default_information_originate:
                metric: <int>
                metric_type: <int>
          maximum_paths: <int>
          max_metric:
            router_lsa:
              external_lsa:
                override_metric: <int>
              include_stub: <bool>
              on_startup: <str>
              summary_lsa:
                override_metric: <int>
          mpls_ldp_sync_default: <bool>
    ```

## Router Traffic Engineering

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>router_traffic_engineering</samp>](## "router_traffic_engineering") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;router_id</samp>](## "router_traffic_engineering.router_id") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp>](## "router_traffic_engineering.router_id.ipv4") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6</samp>](## "router_traffic_engineering.router_id.ipv6") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;segment_routing</samp>](## "router_traffic_engineering.segment_routing") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;colored_tunnel_rib</samp>](## "router_traffic_engineering.segment_routing.colored_tunnel_rib") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;policy_endpoints</samp>](## "router_traffic_engineering.segment_routing.policy_endpoints") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- address</samp>](## "router_traffic_engineering.segment_routing.policy_endpoints.[].address") | String |  |  |  | IPv4 or IPv6 address |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;colors</samp>](## "router_traffic_engineering.segment_routing.policy_endpoints.[].colors") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- value</samp>](## "router_traffic_engineering.segment_routing.policy_endpoints.[].colors.[].value") | Integer | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;binding_sid</samp>](## "router_traffic_engineering.segment_routing.policy_endpoints.[].colors.[].binding_sid") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "router_traffic_engineering.segment_routing.policy_endpoints.[].colors.[].description") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "router_traffic_engineering.segment_routing.policy_endpoints.[].colors.[].name") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sbfd_remote_discriminator</samp>](## "router_traffic_engineering.segment_routing.policy_endpoints.[].colors.[].sbfd_remote_discriminator") | String |  |  |  | IPv4 address or 32 bit integer |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;path_group</samp>](## "router_traffic_engineering.segment_routing.policy_endpoints.[].colors.[].path_group") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- preference</samp>](## "router_traffic_engineering.segment_routing.policy_endpoints.[].colors.[].path_group.[].preference") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;explicit_null</samp>](## "router_traffic_engineering.segment_routing.policy_endpoints.[].colors.[].path_group.[].explicit_null") | String |  |  | Valid Values:<br>- ipv4<br>- ipv6<br>- ipv4 ipv6<br>- none |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;segment_list</samp>](## "router_traffic_engineering.segment_routing.policy_endpoints.[].colors.[].path_group.[].segment_list") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- label_stack</samp>](## "router_traffic_engineering.segment_routing.policy_endpoints.[].colors.[].path_group.[].segment_list.[].label_stack") | String |  |  |  | Label Stack as string.<br>Example: "100 2000 30"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;weight</samp>](## "router_traffic_engineering.segment_routing.policy_endpoints.[].colors.[].path_group.[].segment_list.[].weight") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;index</samp>](## "router_traffic_engineering.segment_routing.policy_endpoints.[].colors.[].path_group.[].segment_list.[].index") | Integer |  |  |  |  |

=== "YAML"

    ```yaml
    router_traffic_engineering:
      router_id:
        ipv4: <str>
        ipv6: <str>
      segment_routing:
        colored_tunnel_rib: <bool>
        policy_endpoints:
          - address: <str>
            colors:
              - value: <int>
                binding_sid: <int>
                description: <str>
                name: <str>
                sbfd_remote_discriminator: <str>
                path_group:
                  - preference: <int>
                    explicit_null: <str>
                    segment_list:
                      - label_stack: <str>
                        weight: <int>
                        index: <int>
    ```

## Service Routing Configuration BGP

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>service_routing_configuration_bgp</samp>](## "service_routing_configuration_bgp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;no_equals_default</samp>](## "service_routing_configuration_bgp.no_equals_default") | Boolean |  |  |  |  |

=== "YAML"

    ```yaml
    service_routing_configuration_bgp:
      no_equals_default: <bool>
    ```

## Service Routing Protocols Model

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>service_routing_protocols_model</samp>](## "service_routing_protocols_model") | String |  |  | Valid Values:<br>- multi-agent<br>- ribd |  |

=== "YAML"

    ```yaml
    service_routing_protocols_model: <str>
    ```

## Static Routes

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>static_routes</samp>](## "static_routes") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- vrf</samp>](## "static_routes.[].vrf") | String |  |  |  | VRF Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;destination_address_prefix</samp>](## "static_routes.[].destination_address_prefix") | String |  |  |  | IPv4_network/Mask |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;interface</samp>](## "static_routes.[].interface") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;gateway</samp>](## "static_routes.[].gateway") | String |  |  |  | IPv4 Address |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;track_bfd</samp>](## "static_routes.[].track_bfd") | Boolean |  |  |  | Track next-hop using BFD |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;distance</samp>](## "static_routes.[].distance") | Integer |  |  | Min: 1<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;tag</samp>](## "static_routes.[].tag") | Integer |  |  | Min: 0<br>Max: 4294967295 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "static_routes.[].name") | String |  |  |  | Description |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;metric</samp>](## "static_routes.[].metric") | Integer |  |  | Min: 0<br>Max: 4294967295 |  |

=== "YAML"

    ```yaml
    static_routes:
      - vrf: <str>
        destination_address_prefix: <str>
        interface: <str>
        gateway: <str>
        track_bfd: <bool>
        distance: <int>
        tag: <int>
        name: <str>
        metric: <int>
    ```

## VRFs

These keys are ignored if the name of the vrf is 'default'

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>vrfs</samp>](## "vrfs") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- name</samp>](## "vrfs.[].name") | String | Required, Unique |  |  | VRF Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "vrfs.[].description") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_routing</samp>](## "vrfs.[].ip_routing") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_routing</samp>](## "vrfs.[].ipv6_routing") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_routing_ipv6_interfaces</samp>](## "vrfs.[].ip_routing_ipv6_interfaces") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;tenant</samp>](## "vrfs.[].tenant") | String |  |  |  | Key only used for documentation or validation purposes |

=== "YAML"

    ```yaml
    vrfs:
      - name: <str>
        description: <str>
        ip_routing: <bool>
        ipv6_routing: <bool>
        ip_routing_ipv6_interfaces: <bool>
        tenant: <str>
    ```
