<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>router_rip</samp>](## "router_rip") | Dictionary |  |  |  | Routing Information Protocol settings. |
    | [<samp>&nbsp;&nbsp;enabled</samp>](## "router_rip.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;vrf</samp>](## "router_rip.vrf") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;metric</samp>](## "router_rip.metric") | Integer |  |  | Min: 0<br>Max: 16 | Set default metric for the routes |
    | [<samp>&nbsp;&nbsp;networks</samp>](## "router_rip.networks") | List, items: String |  |  | Min Length: 1 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "router_rip.networks.[]") | String |  |  |  | Subnet/Mask. e.g. 192.168.10.0/24. |
    | [<samp>&nbsp;&nbsp;distance</samp>](## "router_rip.distance") | Integer |  |  | Min: 1<br>Max: 255 | Administrative distance. |
    | [<samp>&nbsp;&nbsp;access_group</samp>](## "router_rip.access_group") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;timers</samp>](## "router_rip.timers") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;update_interval</samp>](## "router_rip.timers.update_interval") | Integer | Required |  | Min: 5<br>Max: 2147483647 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;expiration_time</samp>](## "router_rip.timers.expiration_time") | Integer | Required |  | Min: 5<br>Max: 2147483647 | Expiration time of a route. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;deletion_time</samp>](## "router_rip.timers.deletion_time") | Integer | Required |  | Min: 5<br>Max: 2147483647 | Deletion time of a route after its expiry. |
    | [<samp>&nbsp;&nbsp;redistribute</samp>](## "router_rip.redistribute") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "router_rip.redistribute.bgp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_rip.redistribute.bgp.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_rip.redistribute.bgp.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;connected</samp>](## "router_rip.redistribute.connected") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_rip.redistribute.connected.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_rip.redistribute.connected.route_map") | String | Required |  |  | Route Map Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf</samp>](## "router_rip.redistribute.ospf") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_rip.redistribute.ospf.enabled") | Boolean |  |  |  | Redistribute OSPF routes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_rip.redistribute.ospf.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_external</samp>](## "router_rip.redistribute.ospf.match_external") | Dictionary |  |  |  | Redistribute OSPF routes learned from external sources. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_rip.redistribute.ospf.match_external.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_rip.redistribute.ospf.match_external.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_internal</samp>](## "router_rip.redistribute.ospf.match_internal") | Dictionary |  |  |  | Redistribute OSPF routes learned from internal sources.<br>This is mutually exclusive with `redistribute.enabled` and `redistribute.route_map`.<br>This key is least preferred.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_rip.redistribute.ospf.match_internal.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_rip.redistribute.ospf.match_internal.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;static</samp>](## "router_rip.redistribute.static") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_rip.redistribute.static.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_rip.redistribute.static.route_map") | String |  |  |  | Route Map Name. |

=== "YAML"

    ```yaml
    # Routing Information Protocol settings.
    router_rip:
      enabled: <bool>
      vrf: <str>

      # Set default metric for the routes
      metric: <int; 0-16>
      networks: # >=1 items

          # Subnet/Mask. e.g. 192.168.10.0/24.
        - <str>

      # Administrative distance.
      distance: <int; 1-255>
      access_group: <str>
      timers:
        update_interval: <int; 5-2147483647; required>

        # Expiration time of a route.
        expiration_time: <int; 5-2147483647; required>

        # Deletion time of a route after its expiry.
        deletion_time: <int; 5-2147483647; required>
      redistribute:
        bgp:
          enabled: <bool>
          route_map: <str>
        connected:
          enabled: <bool; required>

          # Route Map Name.
          route_map: <str; required>
        ospf:

          # Redistribute OSPF routes.
          enabled: <bool>
          route_map: <str>

          # Redistribute OSPF routes learned from external sources.
          match_external:
            enabled: <bool; required>
            route_map: <str>

          # Redistribute OSPF routes learned from internal sources.
          # This is mutually exclusive with `redistribute.enabled` and `redistribute.route_map`.
          # This key is least preferred.
          match_internal:
            enabled: <bool; required>
            route_map: <str>
        static:
          enabled: <bool>

          # Route Map Name.
          route_map: <str>
    ```
