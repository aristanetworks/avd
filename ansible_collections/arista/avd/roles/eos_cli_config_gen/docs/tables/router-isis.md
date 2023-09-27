<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>router_isis</samp>](## "router_isis") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;instance</samp>](## "router_isis.instance") | String | Required |  |  | ISIS Instance Name |
    | [<samp>&nbsp;&nbsp;net</samp>](## "router_isis.net") | String |  |  |  | CLNS Address like "49.0001.0001.0000.0001.00" |
    | [<samp>&nbsp;&nbsp;router_id</samp>](## "router_isis.router_id") | String |  |  |  | IPv4 Address |
    | [<samp>&nbsp;&nbsp;is_type</samp>](## "router_isis.is_type") | String |  |  | Valid Values:<br>- level-1<br>- level-1-2<br>- level-2 |  |
    | [<samp>&nbsp;&nbsp;log_adjacency_changes</samp>](## "router_isis.log_adjacency_changes") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;mpls_ldp_sync_default</samp>](## "router_isis.mpls_ldp_sync_default") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;timers</samp>](## "router_isis.timers") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;local_convergence</samp>](## "router_isis.timers.local_convergence") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;protected_prefixes</samp>](## "router_isis.timers.local_convergence.protected_prefixes") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;delay</samp>](## "router_isis.timers.local_convergence.delay") | Integer |  | `10000` |  | Delay in milliseconds. |
    | [<samp>&nbsp;&nbsp;advertise</samp>](## "router_isis.advertise") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;passive_only</samp>](## "router_isis.advertise.passive_only") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;address_family</samp>](## "router_isis.address_family") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "router_isis.address_family.[].&lt;str&gt;") <span style="color:red">deprecated</span> | String |  |  | Valid Values:<br>- ipv4<br>- ipv6<br>- ipv4 unicast<br>- ipv6 unicast | Address Family<span style="color:red">This key is deprecated. Support will be removed in AVD version 5.0.0. Use <samp>address_family_ipv4.enabled or address_family_ipv6.enabled</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;isis_af_defaults</samp>](## "router_isis.isis_af_defaults") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "router_isis.isis_af_defaults.[].&lt;str&gt;") <span style="color:red">deprecated</span> | String |  |  |  | EOS CLI rendered under the address families<br>Example "maximum-paths 64"<br><span style="color:red">This key is deprecated. Support will be removed in AVD version 5.0.0. Use <samp>address_family_ipv4/address_family_ipv6</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;redistribute_routes</samp>](## "router_isis.redistribute_routes") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- source_protocol</samp>](## "router_isis.redistribute_routes.[].source_protocol") | String | Required |  | Valid Values:<br>- bgp<br>- connected<br>- isis<br>- ospf<br>- ospfv3<br>- static |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_isis.redistribute_routes.[].route_map") | String |  |  |  | Route-map name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_isis.redistribute_routes.[].include_leaked") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ospf_route_type</samp>](## "router_isis.redistribute_routes.[].ospf_route_type") | String |  |  | Valid Values:<br>- external<br>- internal<br>- nssa-external | ospf_route_type is required with source_protocols 'ospf' and 'ospfv3' |
    | [<samp>&nbsp;&nbsp;address_family_ipv4</samp>](## "router_isis.address_family_ipv4") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_isis.address_family_ipv4.enabled") | Boolean |  |  |  |  |
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
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_isis.address_family_ipv6.enabled") | Boolean |  |  |  |  |
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
        enabled: <bool>
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
        enabled: <bool>
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
    ```
