<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
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
