<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>ipv6_router_ospf</samp>](## "ipv6_router_ospf") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;process_ids</samp>](## "ipv6_router_ospf.process_ids") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;id</samp>](## "ipv6_router_ospf.process_ids.[].id") | Integer | Required, Unique |  |  | OSPF process ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "ipv6_router_ospf.process_ids.[].vrf") | String |  |  |  | VRF name for OSPF process. Must be unique across all OSPFv3 instances. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;router_id</samp>](## "ipv6_router_ospf.process_ids.[].router_id") | String |  |  |  | IPv4 Address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;redistribute</samp>](## "ipv6_router_ospf.process_ids.[].redistribute") | Dictionary |  |  |  | Redistribute routes with OSPFv3. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "ipv6_router_ospf.process_ids.[].redistribute.bgp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "ipv6_router_ospf.process_ids.[].redistribute.bgp.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "ipv6_router_ospf.process_ids.[].redistribute.bgp.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "ipv6_router_ospf.process_ids.[].redistribute.bgp.include_leaked") | Boolean |  |  |  | Include leaked routes while redistributing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;connected</samp>](## "ipv6_router_ospf.process_ids.[].redistribute.connected") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "ipv6_router_ospf.process_ids.[].redistribute.connected.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "ipv6_router_ospf.process_ids.[].redistribute.connected.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "ipv6_router_ospf.process_ids.[].redistribute.connected.include_leaked") | Boolean |  |  |  | Include leaked routes while redistributing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis</samp>](## "ipv6_router_ospf.process_ids.[].redistribute.isis") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "ipv6_router_ospf.process_ids.[].redistribute.isis.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_level</samp>](## "ipv6_router_ospf.process_ids.[].redistribute.isis.isis_level") | String |  |  | Valid Values:<br>- <code>level-1</code><br>- <code>level-2</code><br>- <code>level-1-2</code> | Redistribute IS-IS route level. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "ipv6_router_ospf.process_ids.[].redistribute.isis.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "ipv6_router_ospf.process_ids.[].redistribute.isis.include_leaked") | Boolean |  |  |  | Include leaked routes while redistributing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ospfv3</samp>](## "ipv6_router_ospf.process_ids.[].redistribute.ospfv3") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "ipv6_router_ospf.process_ids.[].redistribute.ospfv3.enabled") | Boolean |  |  |  | Redistribute OSPFv3 routes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_external</samp>](## "ipv6_router_ospf.process_ids.[].redistribute.ospfv3.match_external") | Dictionary |  |  |  | Redistribute OSPFv3 routes learned from external sources. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "ipv6_router_ospf.process_ids.[].redistribute.ospfv3.match_external.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "ipv6_router_ospf.process_ids.[].redistribute.ospfv3.match_external.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "ipv6_router_ospf.process_ids.[].redistribute.ospfv3.match_external.include_leaked") | Boolean |  |  |  | Include leaked routes while redistributing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_internal</samp>](## "ipv6_router_ospf.process_ids.[].redistribute.ospfv3.match_internal") | Dictionary |  |  |  | Redistribute OSPFv3 routes learned from internal sources. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "ipv6_router_ospf.process_ids.[].redistribute.ospfv3.match_internal.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "ipv6_router_ospf.process_ids.[].redistribute.ospfv3.match_internal.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_nssa_external</samp>](## "ipv6_router_ospf.process_ids.[].redistribute.ospfv3.match_nssa_external") | Dictionary |  |  |  | Redistribute OSPFv3 routes learned from external NSSA sources. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "ipv6_router_ospf.process_ids.[].redistribute.ospfv3.match_nssa_external.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "ipv6_router_ospf.process_ids.[].redistribute.ospfv3.match_nssa_external.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "ipv6_router_ospf.process_ids.[].redistribute.ospfv3.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;static</samp>](## "ipv6_router_ospf.process_ids.[].redistribute.static") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "ipv6_router_ospf.process_ids.[].redistribute.static.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "ipv6_router_ospf.process_ids.[].redistribute.static.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "ipv6_router_ospf.process_ids.[].redistribute.static.include_leaked") | Boolean |  |  |  | Include leaked routes while redistributing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dhcp</samp>](## "ipv6_router_ospf.process_ids.[].redistribute.dhcp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "ipv6_router_ospf.process_ids.[].redistribute.dhcp.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "ipv6_router_ospf.process_ids.[].redistribute.dhcp.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;auto_cost_reference_bandwidth</samp>](## "ipv6_router_ospf.process_ids.[].auto_cost_reference_bandwidth") | Integer |  |  | Min: 1<br>Max: 4294967 | Bandwidth in mbps. |

=== "YAML"

    ```yaml
    ipv6_router_ospf:
      process_ids:

          # OSPF process ID.
        - id: <int; required; unique>

          # VRF name for OSPF process. Must be unique across all OSPFv3 instances.
          vrf: <str>

          # IPv4 Address.
          router_id: <str>

          # Redistribute routes with OSPFv3.
          redistribute:
            bgp:
              enabled: <bool; required>
              route_map: <str>

              # Include leaked routes while redistributing.
              include_leaked: <bool>
            connected:
              enabled: <bool; required>
              route_map: <str>

              # Include leaked routes while redistributing.
              include_leaked: <bool>
            isis:
              enabled: <bool; required>

              # Redistribute IS-IS route level.
              isis_level: <str; "level-1" | "level-2" | "level-1-2">
              route_map: <str>

              # Include leaked routes while redistributing.
              include_leaked: <bool>
            ospfv3:

              # Redistribute OSPFv3 routes.
              enabled: <bool>

              # Redistribute OSPFv3 routes learned from external sources.
              match_external:
                enabled: <bool; required>
                route_map: <str>

                # Include leaked routes while redistributing.
                include_leaked: <bool>

              # Redistribute OSPFv3 routes learned from internal sources.
              match_internal:
                enabled: <bool; required>
                route_map: <str>

              # Redistribute OSPFv3 routes learned from external NSSA sources.
              match_nssa_external:
                enabled: <bool; required>
                route_map: <str>
              route_map: <str>
            static:
              enabled: <bool; required>
              route_map: <str>

              # Include leaked routes while redistributing.
              include_leaked: <bool>
            dhcp:
              enabled: <bool; required>
              route_map: <str>

          # Bandwidth in mbps.
          auto_cost_reference_bandwidth: <int; 1-4294967>
    ```
