<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>router_general</samp>](## "router_general") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;router_id</samp>](## "router_general.router_id") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp>](## "router_general.router_id.ipv4") | String |  |  |  | IPv4 Address |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6</samp>](## "router_general.router_id.ipv6") | String |  |  |  | IPv6 Address |
    | [<samp>&nbsp;&nbsp;nexthop_fast_failover</samp>](## "router_general.nexthop_fast_failover") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;vrfs</samp>](## "router_general.vrfs") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "router_general.vrfs.[].name") | String | Required, Unique |  |  | Destination-VRF |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;leak_routes</samp>](## "router_general.vrfs.[].leak_routes") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;source_vrf</samp>](## "router_general.vrfs.[].leak_routes.[].source_vrf") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;subscribe_policy</samp>](## "router_general.vrfs.[].leak_routes.[].subscribe_policy") | String |  |  |  | Route-Map Policy |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;routes</samp>](## "router_general.vrfs.[].routes") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dynamic_prefix_lists</samp>](## "router_general.vrfs.[].routes.dynamic_prefix_lists") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "router_general.vrfs.[].routes.dynamic_prefix_lists.[].name") | String |  |  |  | Dynamic Prefix List Name |

=== "YAML"

    ```yaml
    router_general:
      router_id:

        # IPv4 Address
        ipv4: <str>

        # IPv6 Address
        ipv6: <str>
      nexthop_fast_failover: <bool; default=False>
      vrfs:

          # Destination-VRF
        - name: <str; required; unique>
          leak_routes:
            - source_vrf: <str>

              # Route-Map Policy
              subscribe_policy: <str>
          routes:
            dynamic_prefix_lists:

                # Dynamic Prefix List Name
              - name: <str>
    ```
