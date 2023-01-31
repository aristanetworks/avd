---
search:
  boost: 2
---

# Routing

## ARP

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>arp</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;aging</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;timeout_default</samp> | Integer |  |  | Min: 60<br>Max: 65535 | Timeout in seconds |

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
    | <samp>ip_routing</samp> | Boolean |  |  |  |  |

=== "YAML"

    ```yaml
    ip_routing: <bool>
    ```

## IP Routing IPv6 Interfaces

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>ip_routing_ipv6_interfaces</samp> | Boolean |  |  |  |  |

=== "YAML"

    ```yaml
    ip_routing_ipv6_interfaces: <bool>
    ```

## IP Virtual Router MAC Address

MAC address (hh:hh:hh:hh:hh:hh)
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>ip_virtual_router_mac_address</samp> | String |  |  |  |  |

=== "YAML"

    ```yaml
    ip_virtual_router_mac_address: <str>
    ```

## IPv6 Static Routes

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>ipv6_static_routes</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;- vrf</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;destination_address_prefix</samp> | String |  |  |  | IPv6 Network/Mask |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;interface</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;gateway</samp> | String |  |  |  | IPv6 Address |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;track_bfd</samp> | Boolean |  |  |  | Track next-hop using BFD |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;distance</samp> | Integer |  |  | Min: 1<br>Max: 255 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;tag</samp> | Integer |  |  | Min: 0<br>Max: 4294967295 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp> | String |  |  |  | Description |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;metric</samp> | Integer |  |  | Min: 0<br>Max: 4294967295 |  |

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
    | <samp>ipv6_unicast_routing</samp> | Boolean |  |  |  |  |

=== "YAML"

    ```yaml
    ipv6_unicast_routing: <bool>
    ```

## Router BFD

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>router_bfd</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;interval</samp> | Integer |  |  |  | Rate in milliseconds |
    | <samp>&nbsp;&nbsp;min_rx</samp> | Integer |  |  |  | Rate in milliseconds |
    | <samp>&nbsp;&nbsp;multiplier</samp> | Integer |  |  | Min: 3<br>Max: 50 |  |
    | <samp>&nbsp;&nbsp;multihop</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;interval</samp> | Integer |  |  |  | Rate in milliseconds |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;min_rx</samp> | Integer |  |  |  | Rate in milliseconds |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;multiplier</samp> | Integer |  |  | Min: 3<br>Max: 50 |  |
    | <samp>&nbsp;&nbsp;sbfd</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;local_interface</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp> | String |  |  |  | Interface Name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;protocols</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;initiator_interval</samp> | Integer |  |  |  | Rate in milliseconds |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;initiator_multiplier</samp> | Integer |  |  | Min: 3<br>Max: 50 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;reflector</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;min_rx</samp> | Integer |  |  |  | Rate in milliseconds |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_discriminator</samp> | String |  |  |  | IPv4 address or 32 bit integer |

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
    | <samp>router_bgp</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;as</samp> | String |  |  |  | BGP AS <1-4294967295> or AS number in asdot notation <1-65535>.<0-65535> |
    | <samp>&nbsp;&nbsp;router_id</samp> | String |  |  |  | In IP address format A.B.C.D |
    | <samp>&nbsp;&nbsp;distance</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;external_routes</samp> | Integer |  |  | Min: 1<br>Max: 255 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;internal_routes</samp> | Integer |  |  | Min: 1<br>Max: 255 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;local_routes</samp> | Integer |  |  | Min: 1<br>Max: 255 |  |
    | <samp>&nbsp;&nbsp;graceful_restart</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;restart_time</samp> | Integer |  |  | Min: 1<br>Max: 3600 | Number of seconds |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;stalepath_time</samp> | Integer |  |  | Min: 1<br>Max: 3600 | Number of seconds |
    | <samp>&nbsp;&nbsp;graceful_restart_helper</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;restart_time</samp> | Integer |  |  | Min: 1<br>Max: 100000000 | Number of seconds<br>graceful-restart-help long-lived and restart-time are mutually exclusive in CLI.<br>restart-time will take precedence if both are configured.<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;long_lived</samp> | Boolean |  |  |  | graceful-restart-help long-lived and restart-time are mutually exclusive in CLI.<br>restart-time will take precedence if both are configured.<br> |
    | <samp>&nbsp;&nbsp;maximum_paths</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;paths</samp> | Integer |  |  | Min: 1<br>Max: 600 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ecmp</samp> | Integer |  |  | Min: 1<br>Max: 600 |  |
    | <samp>&nbsp;&nbsp;updates</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;wait_for_convergence</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;wait_install</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;bgp_cluster_id</samp> | String |  |  |  | IP Address A.B.C.D |
    | <samp>&nbsp;&nbsp;bgp_defaults</samp> | List, items: String |  |  |  | BGP command as string |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;bgp</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;bestpath</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;d_path</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;listen_ranges</samp> | List, items: Dictionary |  |  |  | Improved "listen_ranges" data model to support multiple listen ranges and additional filter capabilities<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;- prefix</samp> | String |  |  |  | IPv4 prefix "A.B.C.D/E" or IPv6 prefix "A:B:C:D:E:F:G:H/I" |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_id_include_router_id</samp> | Boolean |  |  |  | Include router ID as part of peer filter |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_group</samp> | String |  |  |  | Peer group name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_filter</samp> | String |  |  |  | Peer-filter name<br>note: `peer_filter` or `remote_as` is required but mutually exclusive.<br>If both are defined, `peer_filter` takes precedence<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_as</samp> | String |  |  |  | BGP AS <1-4294967295> or AS number in asdot notation <1-65535>.<0-65535> |
    | <samp>&nbsp;&nbsp;peer_groups</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  | Peer-group name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp> | String |  |  |  | Key only used for documentation or validation purposes |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_as</samp> | String |  |  |  | BGP AS <1-4294967295> or AS number in asdot notation <1-65535>.<0-65535> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_as</samp> | String |  |  |  | BGP AS <1-4294967295> or AS number in asdot notation <1-65535>.<0-65535> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remove_private_as</samp> | Dictionary |  |  |  | Remove private AS numbers in outbound AS path |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;all</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;replace_as</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remove_private_as_ingress</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;replace_as</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_filter</samp> | String |  |  |  | Peer-filter name<br>note: `bgp_listen_range_prefix` and `peer_filter` will be deprecated in AVD v4.0<br>These should not be mixed with the new `listen_ranges` key above to avoid conflicts.<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;next_hop_unchanged</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;update_source</samp> | String |  |  |  | IP address or interface name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_reflector_client</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ebgp_multihop</samp> | Integer |  |  | Min: 1<br>Max: 255 | Time-to-live in range of hops |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;next_hop_self</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;password</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default_originate</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp> | String |  |  |  | Route-map name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send_community</samp> | String |  |  |  | 'all' or a combination of 'standard', 'extended', 'large' and 'link-bandwidth (w/options)' |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes</samp> | Integer |  |  | Min: 0<br>Max: 4294967294 | Maximum number of routes (0 means unlimited) |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes_warning_limit</samp> | String |  |  |  | Maximum number of routes after which a warning is issued (0 means never warn) or<br>Percentage of maximum number of routes at which to warn ("<1-100> percent")<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes_warning_only</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;link_bandwidth</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default</samp> | String |  |  |  | nn.nn(K|M|G) link speed in bits/second |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;allowas_in</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;times</samp> | Integer |  |  | Min: 1<br>Max: 10 | Number of local ASNs allowed in a BGP update |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;weight</samp> | Integer |  |  | Min: 0<br>Max: 65535 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timers</samp> | String |  |  |  | BGP Keepalive and Hold Timer values in seconds as string "<0-3600> <0-3600>" |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rib_in_pre_policy_retain</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;all</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp> | String |  |  |  | Inbound route-map name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp> | String |  |  |  | Outbound route-map name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_listen_range_prefix</samp> | String |  |  |  | IP prefix range<br>note: `bgp_listen_range_prefix` and `peer_filter` will be deprecated in AVD v4.0<br>These should not be mixed with the new `listen_ranges` key above to avoid conflicts.<br> |
    | <samp>&nbsp;&nbsp;neighbors</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;- ip_address</samp> | String | Required, Unique |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_group</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_as</samp> | String |  |  |  | BGP AS <1-4294967295> or AS number in asdot notation <1-65535>.<0-65535> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_as</samp> | String |  |  |  | BGP AS <1-4294967295> or AS number in asdot notation <1-65535>.<0-65535> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_reflector_client</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;update_source</samp> | String |  |  |  | Source Interface |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;weight</samp> | Integer |  |  | Min: 0<br>Max: 65535 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timers</samp> | String |  |  |  | BGP Keepalive and Hold Timer values in seconds as string "<0-3600> <0-3600>" |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp> | String |  |  |  | Inbound route-map name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp> | String |  |  |  | Outbound route-map name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default_originate</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send_community</samp> | String |  |  |  | 'all' or a combination of 'standard', 'extended', 'large' and 'link-bandwidth (w/options)' |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes</samp> | Integer |  |  | Min: 0<br>Max: 4294967294 | Maximum number of routes (0 means unlimited) |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes_warning_limit</samp> | String |  |  |  | Maximum number of routes after which a warning is issued (0 means never warn) or<br>Percentage of maximum number of routes at which to warn ("<1-100> percent")<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes_warning_only</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;allowas_in</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;times</samp> | Integer |  |  | Min: 1<br>Max: 10 | Number of local ASNs allowed in a BGP update |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ebgp_multihop</samp> | Integer |  |  | Min: 1<br>Max: 255 | Time-to-live in range of hops |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;next_hop_self</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;link_bandwidth</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default</samp> | String |  |  |  | nn.nn(K|M|G) link speed in bits/second |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rib_in_pre_policy_retain</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;all</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remove_private_as</samp> | Dictionary |  |  |  | Remove private AS numbers in outbound AS path |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;all</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;replace_as</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remove_private_as_ingress</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;replace_as</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;neighbor_interfaces</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  | Interface name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_as</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_group</samp> | String |  | Peer-group name |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_filter</samp> | String |  |  |  | Peer-filter name |
    | <samp>&nbsp;&nbsp;aggregate_addresses</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;- prefix</samp> | String | Required, Unique |  |  | IPv4 prefix "A.B.C.D/E" or IPv6 prefix "A:B:C:D:E:F:G:H/I" |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;advertise_only</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;as_set</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;summary_only</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;attribute_map</samp> | String |  |  |  | Route-map name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_map</samp> | String |  |  |  | Route-map name |
    | <samp>&nbsp;&nbsp;redistribute_routes</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;- source_protocol</samp> | String | Required, Unique |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;vlan_aware_bundles</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  | VLAN aware bundle name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tenant</samp> | String |  |  |  | Key only used for documentation or validation purposes |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp> | String |  |  |  | Key only used for documentation or validation purposes |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rd</samp> | String |  |  |  | Route distinguisher |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rd_evpn_domain</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;domain</samp> | String |  |  | Valid Values:<br>- remote<br>- all |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rd</samp> | String |  |  |  | Route distinguisher |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_targets</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;both</samp> | List, items: String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;import</samp> | List, items: String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;export</samp> | List, items: String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;import_evpn_domains</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- domain</samp> | String |  |  | Valid Values:<br>- remote<br>- all |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_target</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;export_evpn_domains</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- domain</samp> | String |  |  | Valid Values:<br>- remote<br>- all |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_target</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;import_export_evpn_domains</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- domain</samp> | String |  |  | Valid Values:<br>- remote<br>- all |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_target</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;redistribute_routes</samp> | List, items: String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;no_redistribute_routes</samp> | List, items: String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan</samp> | String |  |  |  | VLAN range as string. Example "100-200,300" |
    | <samp>&nbsp;&nbsp;vlans</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;- id</samp> | Integer | Required, Unique |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tenant</samp> | String |  |  |  | Key only used for documentation or validation purposes |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rd</samp> | String |  |  |  | Route distinguisher |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rd_evpn_domain</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;domain</samp> | String |  |  | Valid Values:<br>- remote<br>- all |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rd</samp> | String |  |  |  | Route distinguisher |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;eos_cli</samp> | String |  |  |  | Multiline EOS CLI rendered directly on the Router BGP, VLAN definition in the final EOS configuration |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_targets</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;both</samp> | List, items: String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;import</samp> | List, items: String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;export</samp> | List, items: String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;import_evpn_domains</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- domain</samp> | String |  |  | Valid Values:<br>- remote<br>- all |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_target</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;export_evpn_domains</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- domain</samp> | String |  |  | Valid Values:<br>- remote<br>- all |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_target</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;import_export_evpn_domains</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- domain</samp> | String |  |  | Valid Values:<br>- remote<br>- all |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_target</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;redistribute_routes</samp> | List, items: String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;no_redistribute_routes</samp> | List, items: String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;vpws</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  | VPWS instance name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rd</samp> | String |  |  |  | Route distinguisher |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_targets</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;import_export</samp> | String |  |  |  | Route Target |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls_control_word</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;label_flow</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pseudowires</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  | Pseudowire name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id_local</samp> | Integer |  |  |  | Must match id_remote on other pe |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id_remote</samp> | Integer |  |  |  | Must match id_local on other pe |
    | <samp>&nbsp;&nbsp;address_family_evpn</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;domain_identifier</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;neighbor_default</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;encapsulation</samp> | String |  |  | Valid Values:<br>- vxlan<br>- mpls |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;next_hop_self_source_interface</samp> | String |  |  |  | Source interface name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;next_hop_self_received_evpn_routes</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inter_domain</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;peer_groups</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  | Peer-group name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp> | String |  |  |  | Inbound route-map name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp> | String |  |  |  | Outbound route-map name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;domain_remote</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;evpn_hostflap_detection</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;window</samp> | Integer |  |  | Min: 0<br>Max: 4294967295 | Time (in seconds) to detect a MAC duplication issue |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;threshold</samp> | Integer |  |  | Min: 0<br>Max: 4294967295 | Minimum number of MAC moves that indicate a MAC Duplication issue |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expiry_timeout</samp> | Integer |  |  | Min: 0<br>Max: 4294967295 | Time (in seconds) to purge a MAC duplication issue |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;route</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;import_match_failure_action</samp> | String |  |  | Valid Values:<br>- discard |  |
    | <samp>&nbsp;&nbsp;address_family_rtc</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;peer_groups</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  | Peer-group name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default_route_target</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;only</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;encoding_origin_as_omit</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;address_family_ipv4</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;networks</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- prefix</samp> | String | Required, Unique |  |  | IPv4 prefix "A.B.C.D/E" or IPv6 prefix "A:B:C:D:E:F:G:H/I" |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp> | String |  |  |  | Route-map name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;peer_groups</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  | Peer-group name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp> | String |  |  |  | Inbound route-map name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp> | String |  |  |  | Outbound route-map name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default_originate</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp> | String |  |  |  | Route-map name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;next_hop</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_family_ipv6_originate</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list_in</samp> | String |  |  |  | Inbound prefix-list name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list_out</samp> | String |  |  |  | Outbound prefix-list name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;neighbors</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ip_address</samp> | String | Required, Unique |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp> | String |  |  |  | Inbound route-map name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp> | String |  |  |  | Outbound route-map name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list_in</samp> | String |  |  |  | Inbound prefix-list name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list_out</samp> | String |  |  |  | Prefix-list name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default_originate</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;address_family_ipv4_multicast</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;peer_groups</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  | Peer-group name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp> | String |  |  |  | Inbound route-map name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp> | String |  |  |  | Outbound route-map name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;neighbors</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ip_address</samp> | String | Required, Unique |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp> | String |  |  |  | Inbound route-map name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp> | String |  |  |  | Outbound route-map name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;redistribute_routes</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- source_protocol</samp> | String | Required, Unique |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;address_family_ipv6</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;networks</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- prefix</samp> | String | Required, Unique |  |  | IPv4 prefix "A.B.C.D/E" or IPv6 prefix "A:B:C:D:E:F:G:H/I" |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp> | String |  |  |  | Route-map name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;peer_groups</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  | Peer-group name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp> | String |  |  |  | Inbound route-map name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp> | String |  |  |  | Outbound route-map name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list_in</samp> | String |  |  |  | Inbound prefix-list name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list_out</samp> | String |  |  |  | Outbound prefix-list name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;neighbors</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ip_address</samp> | String | Required, Unique |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp> | String |  |  |  | Inbound route-map name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp> | String |  |  |  | Outbound route-map name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list_in</samp> | String |  |  |  | Inbound prefix-list name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list_out</samp> | String |  |  |  | Outbound prefix-list name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;redistribute_routes</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- source_protocol</samp> | String | Required, Unique |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;address_family_vpn_ipv4</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;domain_identifier</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;peer_groups</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  | Peer-group name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp> | String |  |  |  | Inbound route-map name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp> | String |  |  |  | Outbound route-map name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;route</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;import_match_failure_action</samp> | String |  |  | Valid Values:<br>- discard |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;neighbors</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ip_address</samp> | String | Required, Unique |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp> | String |  |  |  | Inbound route-map name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp> | String |  |  |  | Outbound route-map name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;neighbor_default_encapsulation_mpls_next_hop_self</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;address_family_vpn_ipv6</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;domain_identifier</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;peer_groups</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  | Peer-group name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp> | String |  |  |  | Inbound route-map name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp> | String |  |  |  | Outbound route-map name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;route</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;import_match_failure_action</samp> | String |  |  | Valid Values:<br>- discard |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;neighbors</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ip_address</samp> | String | Required, Unique |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp> | String |  |  |  | Inbound route-map name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp> | String |  |  |  | Outbound route-map name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;neighbor_default_encapsulation_mpls_next_hop_self</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;vrfs</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  | VRF name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rd</samp> | String |  |  |  | Route distinguisher |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_multicast</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_multicast_address_family</samp> | Dictionary |  |  |  | Enable per-AF EVPN multicast settings |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;transit</samp> | Boolean |  |  |  | Enable EVPN multicast transit mode |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_targets</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;import</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- address_family</samp> | String | Required, Unique |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_targets</samp> | List, items: String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;export</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- address_family</samp> | String | Required, Unique |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_targets</samp> | List, items: String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;router_id</samp> | String |  |  |  | in IP address format A.B.C.D |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timers</samp> | String |  |  |  | BGP Keepalive and Hold Timer values in seconds as string "<0-3600> <0-3600>" |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;networks</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- prefix</samp> | String | Required, Unique |  |  | IPv4 prefix "A.B.C.D/E" or IPv6 prefix "A:B:C:D:E:F:G:H/I" |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;listen_ranges</samp> | List, items: Dictionary |  |  |  | Improved "listen_ranges" data model to support multiple listen ranges and additional filter capabilities<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- prefix</samp> | String |  |  |  | IPv4 prefix "A.B.C.D/E" or IPv6 prefix "A:B:C:D:E:F:G:H/I" |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_id_include_router_id</samp> | Boolean |  |  |  | Include router ID as part of peer filter |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_group</samp> | String |  |  |  | Peer-group name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_filter</samp> | String |  |  |  | Peer-filter name<br>note: `peer_filter`` or `remote_as` is required but mutually exclusive.<br>If both are defined, peer_filter takes precedence<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_as</samp> | String |  |  |  | BGP AS <1-4294967295> or AS number in asdot notation <1-65535>.<0-65535> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;neighbors</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ip_address</samp> | String | Required, Unique |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_group</samp> | String |  |  |  | Peer-group name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_as</samp> | String |  |  |  | BGP AS <1-4294967295> or AS number in asdot notation <1-65535>.<0-65535> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;password</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remove_private_as</samp> | Dictionary |  |  |  | Remove private AS numbers in outbound AS path |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;all</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;replace_as</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remove_private_as_ingress</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;replace_as</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;weight</samp> | Integer |  |  | Min: 0<br>Max: 65535 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_as</samp> | String |  |  |  | BGP AS <1-4294967295> or AS number in asdot notation <1-65535>.<0-65535> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ebgp_multihop</samp> | Integer |  |  | Min: 1<br>Max: 255 | Time-to-live in range of hops |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;next_hop_self</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timers</samp> | String |  |  |  | BGP Keepalive and Hold Timer values in seconds as string "<0-3600> <0-3600>" |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rib_in_pre_policy_retain</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;all</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send_community</samp> | String |  |  |  | 'all' or a combination of 'standard', 'extended', 'large' and 'link-bandwidth (w/options)' |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes_warning_limit</samp> | String |  |  |  | Maximum number of routes after which a warning is issued (0 means never warn) or<br>Percentage of maximum number of routes at which to warn ("<1-100> percent")<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes_warning_only</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;allowas_in</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;times</samp> | Integer |  |  | Min: 1<br>Max: 10 | Number of local ASNs allowed in a BGP update |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default_originate</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;update_source</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp> | String |  |  |  | Inbound route-map name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp> | String |  |  |  | Outbound route-map name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list_in</samp> | String |  |  |  | Inbound prefix-list name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list_out</samp> | String |  |  |  | Outbound prefix-list name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;neighbor_interfaces</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  | Interface name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_as</samp> | String |  |  |  | BGP AS <1-4294967295> or AS number in asdot notation <1-65535>.<0-65535> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_group</samp> | String |  |  |  | Peer-group name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_filter</samp> | String |  |  |  | Peer-filter name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;redistribute_routes</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- source_protocol</samp> | String | Required, Unique |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;aggregate_addresses</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- prefix</samp> | String | Required, Unique |  |  | IPv4 prefix "A.B.C.D/E" or IPv6 prefix "A:B:C:D:E:F:G:H/I" |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;advertise_only</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;as_set</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;summary_only</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;attribute_map</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_map</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_families</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- address_family</samp> | String | Required, Unique |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;missing_policy</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction_in_action</samp> | String |  |  | Valid Values:<br>- deny<br>- deny-in-out<br>- permit |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction_out_action</samp> | String |  |  | Valid Values:<br>- deny<br>- deny-in-out<br>- permit |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;additional_paths</samp> | List, items: String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;neighbors</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ip_address</samp> | String | Required, Unique |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp> | String |  |  |  | Inbound route-map name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp> | String |  |  |  | Outbound route-map name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_groups</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  | Peer-group name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;next_hop</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_family_ipv6_originate</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;networks</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- prefix</samp> | String | Required, Unique |  |  | IPv4 prefix "A.B.C.D/E" or IPv6 prefix "A:B:C:D:E:F:G:H/I" |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;eos_cli</samp> | String |  |  |  | Multiline EOS CLI rendered directly on the Router BGP, VRF definition in the final EOS configuration |

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
      neighbors:
        - ip_address: <str>
          peer_group: <str>
          remote_as: <str>
          local_as: <str>
          description: <str>
          route_reflector_client: <bool>
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
              remove_private_as:
                enabled: <bool>
                all: <bool>
                replace_as: <bool>
              remove_private_as_ingress:
                enabled: <bool>
                replace_as: <bool>
              weight: <int>
              local_as: <str>
              description: <str>
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
    ```

## Router General configuration

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>router_general</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;router_id</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp> | String |  |  |  | IPv4 Address |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6</samp> | String |  |  |  | IPv6 Address |
    | <samp>&nbsp;&nbsp;nexthop_fast_failover</samp> | Boolean |  | False |  |  |
    | <samp>&nbsp;&nbsp;vrfs</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  | Destination-VRF |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;leak_routes</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- source_vrf</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;subscribe_policy</samp> | String |  |  |  | Route-Map Policy |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;routes</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dynamic_prefix_lists</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp> | String |  |  |  | Dynamic Prefix List Name |

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
    | <samp>router_igmp</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;ssm_aware</samp> | Boolean |  |  |  |  |

=== "YAML"

    ```yaml
    router_igmp:
      ssm_aware: <bool>
    ```

## Router ISIS

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>router_isis</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;instance</samp> | String |  |  |  | ISIS Instance Name |
    | <samp>&nbsp;&nbsp;net</samp> | String |  |  |  | CLNS Address like "49.0001.0001.0000.0001.00" |
    | <samp>&nbsp;&nbsp;router_id</samp> | String |  |  |  | IPv4 Address |
    | <samp>&nbsp;&nbsp;is_type</samp> | String |  |  | Valid Values:<br>- level-1<br>- level-1-2<br>- level-2 |  |
    | <samp>&nbsp;&nbsp;log_adjacency_changes</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;mpls_ldp_sync_default</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;timers</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;local_convergence</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;protected_prefixes</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;delay</samp> | Integer |  | 10000 |  | Delay in milliseconds. |
    | <samp>&nbsp;&nbsp;advertise</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;passive_only</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;address_family</samp> | List, items: String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp> | String |  |  | Valid Values:<br>- ipv4<br>- ipv6<br>- ipv4 unicast<br>- ipv6 unicast | Address Family |
    | <samp>&nbsp;&nbsp;isis_af_defaults</samp> | List, items: String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp> | String |  |  |  | EOS CLI rendered under the address families<br>Example "maximum-paths 64"<br> |
    | <samp>&nbsp;&nbsp;redistribute_routes</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;- source_protocol</samp> | String | Required |  | Valid Values:<br>- bgp<br>- connected<br>- isis<br>- ospf<br>- ospfv3<br>- static |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp> | String |  |  |  | Route-map name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ospf_route_type</samp> | String |  |  | Valid Values:<br>- external<br>- internal<br>- nssa-external | ospf_route_type is required with source_protocols 'ospf' and 'ospfv3' |
    | <samp>&nbsp;&nbsp;address_family_ipv4</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;maximum_paths</samp> | Integer |  |  | Min: 1<br>Max: 128 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;fast_reroute_ti_lfa</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp> | String |  |  | Valid Values:<br>- link-protection<br>- node-protection |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp> | String |  |  | Valid Values:<br>- level-1<br>- level-2 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;srlg</samp> | Dictionary |  |  |  | Shared Risk Link Group |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;strict</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;tunnel_source_labeled_unicast</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf</samp> | String |  |  |  | Route Control Function |
    | <samp>&nbsp;&nbsp;address_family_ipv6</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;maximum_paths</samp> | Integer |  |  | Min: 1<br>Max: 128 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;fast_reroute_ti_lfa</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp> | String |  |  | Valid Values:<br>- link-protection<br>- node-protection |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp> | String |  |  | Valid Values:<br>- level-1<br>- level-2 | Optional, default is to protect all levels |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;srlg</samp> | Dictionary |  |  |  | Shared Risk Link Group |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;strict</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;segment_routing_mpls</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;router_id</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;prefix_segments</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- prefix</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;index</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;no_passive_interfaces</samp> | List |  |  |  | Unused key - to be removed from eos_designs. |

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
    | <samp>router_l2_vpn</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;arp_learning_bridged</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;arp_proxy</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;prefix_list</samp> | String |  |  |  | Prefix-list Name |
    | <samp>&nbsp;&nbsp;arp_selective_install</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;nd_rs_flooding_disabled</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;virtual_router_nd_ra_flooding_disabled</samp> | Boolean |  |  |  |  |

=== "YAML"

    ```yaml
    router_l2_vpn:
      arp_learning_bridged: <bool>
      arp_proxy:
        prefix_list: <str>
      arp_selective_install: <bool>
      nd_rs_flooding_disabled: <bool>
      virtual_router_nd_ra_flooding_disabled: <bool>
    ```

## Router Msdp

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>router_msdp</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;originator_id_local_interface</samp> | String |  |  |  | Interface to use for originator ID |
    | <samp>&nbsp;&nbsp;rejected_limit</samp> | Integer |  |  | Min: 0<br>Max: 40000 | Maximum number of rejected SA messages allowed in cache |
    | <samp>&nbsp;&nbsp;forward_register_packets</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;connection_retry_interval</samp> | Integer |  |  | Min: 1<br>Max: 65535 |  |
    | <samp>&nbsp;&nbsp;group_limits</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;- source_prefix</samp> | String | Required, Unique |  |  | Source address prefix |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;limit</samp> | Integer | Required |  | Min: 0<br>Max: 40000 | Limit for SAs matching the source address prefix |
    | <samp>&nbsp;&nbsp;peers</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;- ipv4_address</samp> | String | Required, Unique |  |  | Peer IP Address |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default_peer</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list</samp> | String |  |  |  | Prefix list to filter source of SA messages |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_interface</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;disabled</samp> | Boolean |  |  |  | Disable the MSDP peer |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sa_limit</samp> | Integer |  |  | Min: 0<br>Max: 40000 | Maximum number of SA messages allowed in cache |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mesh_groups</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  | Mesh group name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;keepalive</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;keepalive_timer</samp> | Integer | Required |  | Min: 1<br>Max: 65535 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hold_timer</samp> | Integer | Required |  | Min: 1<br>Max: 65535 | Must be greater than keepalive timer |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sa_filter</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;in_list</samp> | String |  |  |  | ACL to filter inbound SA messages |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;out_list</samp> | String |  |  |  | ACL to filter outbound SA messages |
    | <samp>&nbsp;&nbsp;vrfs</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  | VRF name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;originator_id_local_interface</samp> | String |  |  |  | Interface to use for originator ID |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rejected_limit</samp> | Integer |  |  | Min: 0<br>Max: 40000 | Maximum number of rejected SA messages allowed in cache |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;forward_register_packets</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;connection_retry_interval</samp> | Integer |  |  | Min: 1<br>Max: 65535 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group_limits</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- source_prefix</samp> | String | Required, Unique |  |  | Source address prefix |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;limit</samp> | Integer | Required |  | Min: 0<br>Max: 40000 | Limit for SAs matching the source address prefix |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peers</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ipv4_address</samp> | String | Required, Unique |  |  | Peer IP Address |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default_peer</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list</samp> | String |  |  |  | Prefix list to filter source of SA messages |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_interface</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;disabled</samp> | Boolean |  |  |  | Disable the MSDP peer |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sa_limit</samp> | Integer |  |  | Min: 0<br>Max: 40000 | Maximum number of SA messages allowed in cache |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mesh_groups</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  | Mesh group name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;keepalive</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;keepalive_timer</samp> | Integer | Required |  | Min: 1<br>Max: 65535 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hold_timer</samp> | Integer | Required |  | Min: 1<br>Max: 65535 | Must be greater than keepalive timer |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sa_filter</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;in_list</samp> | String |  |  |  | ACL to filter inbound SA messages |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;out_list</samp> | String |  |  |  | ACL to filter outbound SA messages |

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
    | <samp>router_ospf</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;process_ids</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;- id</samp> | Integer | Required, Unique |  |  | OSPF Process ID |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp> | String |  |  |  | VRF Name for OSPF Process |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;passive_interface_default</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;router_id</samp> | String |  |  |  | IPv4 Address |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;distance</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;external</samp> | Integer |  |  | Min: 1<br>Max: 255 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inter_area</samp> | Integer |  |  | Min: 1<br>Max: 255 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;intra_area</samp> | Integer |  |  | Min: 1<br>Max: 255 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;log_adjacency_changes_detail</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;network_prefixes</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ipv4_prefix</samp> | String | Required, Unique |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;area</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bfd_enable</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bfd_adjacency_state_any</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;no_passive_interfaces</samp> | List, items: String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp> | String |  |  |  | Interface Name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;distribute_list_in</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_lsa</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timers</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lsa</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rx_min_interval</samp> | Integer |  |  | Min: 0<br>Max: 600000 | Min interval in msecs between accepting the same LSA |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tx_delay</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;initial</samp> | Integer |  |  | Min: 0<br>Max: 600000 | Delay to generate first occurrence of LSA in msecs |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;min</samp> | Integer |  |  | Min: 1<br>Max: 600000 | Min delay between originating the same LSA in msecs |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max</samp> | Integer |  |  | Min: 1<br>Max: 600000 | 1-600000 Maximum delay between originating the same LSA in msec |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;spf_delay</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;initial</samp> | Integer |  |  | Min: 0<br>Max: 600000 | Initial SPF schedule delay in msecs |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;min</samp> | Integer |  |  | Min: 0<br>Max: 65535000 | Min Hold time between two SPFs in msecs |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max</samp> | Integer |  |  | Min: 0<br>Max: 65535000 | Max wait time between two SPFs in msecs |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default_information_originate</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;summary_addresses</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- prefix</samp> | String | Required, Unique |  |  | Summary Prefix Address |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tag</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;attribute_map</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;not_advertise</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;redistribute</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;static</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp> | String |  |  |  | Route Map Name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;connected</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp> | String |  |  |  | Route Map Name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp> | String |  |  |  | Route Map Name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;auto_cost_reference_bandwidth</samp> | Integer |  |  |  | Bandwidth in mbps |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;areas</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- id</samp> | String | Required, Unique |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;filter</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;networks</samp> | List, items: String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp> | String |  |  |  | IPv4 Prefix |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list</samp> | String |  |  |  | Prefix-List Name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp> | String |  | normal | Valid Values:<br>- normal<br>- stub<br>- nssa |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;no_summary</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nssa_only</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default_information_originate</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;metric</samp> | Integer |  |  | Min: 1<br>Max: 65535 | Metric for default route |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;metric_type</samp> | Integer |  |  | Valid Values:<br>- 1<br>- 2 | OSPF metric type for default route |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_paths</samp> | Integer |  |  | Min: 1<br>Max: 128 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_metric</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;router_lsa</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;external_lsa</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;override_metric</samp> | Integer |  |  | Min: 1<br>Max: 16777215 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_stub</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;on_startup</samp> | String |  |  |  | "wait-for-bgp" or Integer 5-86400<br>Example: "wait-for-bgp" Or "222"<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;summary_lsa</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;override_metric</samp> | Integer |  |  | Min: 1<br>Max: 16777215 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls_ldp_sync_default</samp> | Boolean |  |  |  |  |

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
            connected:
              route_map: <str>
            bgp:
              route_map: <str>
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
    | <samp>router_traffic_engineering</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;router_id</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;segment_routing</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;colored_tunnel_rib</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;policy_endpoints</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- address</samp> | String |  |  |  | IPv4 or IPv6 address |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;colors</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- value</samp> | Integer | Required, Unique |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;binding_sid</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sbfd_remote_discriminator</samp> | String |  |  |  | IPv4 address or 32 bit integer |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;path_group</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- preference</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;explicit_null</samp> | String |  |  | Valid Values:<br>- ipv4<br>- ipv6<br>- ipv4 ipv6<br>- none |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;segment_list</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- label_stack</samp> | String |  |  |  | Label Stack as string.<br>Example: "100 2000 30"<br> |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;weight</samp> | Integer |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;index</samp> | Integer |  |  |  |  |

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
    | <samp>service_routing_configuration_bgp</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;no_equals_default</samp> | Boolean |  |  |  |  |

=== "YAML"

    ```yaml
    service_routing_configuration_bgp:
      no_equals_default: <bool>
    ```

## Service Routing Protocols Model

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>service_routing_protocols_model</samp> | String |  |  | Valid Values:<br>- multi-agent<br>- ribd |  |

=== "YAML"

    ```yaml
    service_routing_protocols_model: <str>
    ```

## Static Routes

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>static_routes</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;- vrf</samp> | String |  |  |  | VRF Name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;destination_address_prefix</samp> | String |  |  |  | IPv4_network/Mask |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;interface</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;gateway</samp> | String |  |  |  | IPv4 Address |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;track_bfd</samp> | Boolean |  |  |  | Track next-hop using BFD |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;distance</samp> | Integer |  |  | Min: 1<br>Max: 255 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;tag</samp> | Integer |  |  | Min: 0<br>Max: 4294967295 |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp> | String |  |  |  | Description |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;metric</samp> | Integer |  |  | Min: 0<br>Max: 4294967295 |  |

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

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>vrfs</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;- name</samp> | String | Required, Unique |  |  | VRF Name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;description</samp> | String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_routing</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_routing</samp> | Boolean |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;tenant</samp> | String |  |  |  | Key only used for documentation or validation purposes |

=== "YAML"

    ```yaml
    vrfs:
      - name: <str>
        description: <str>
        ip_routing: <bool>
        ipv6_routing: <bool>
        tenant: <str>
    ```
