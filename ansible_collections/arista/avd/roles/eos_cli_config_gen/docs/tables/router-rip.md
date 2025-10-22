<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>router_rip</samp>](## "router_rip") | Dictionary |  |  |  | Routing Information Protocol settings. |
    | [<samp>&nbsp;&nbsp;vrfs</samp>](## "router_rip.vrfs") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;enabled</samp>](## "router_rip.vrfs.[].enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "router_rip.vrfs.[].vrf") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;metric_default</samp>](## "router_rip.vrfs.[].metric_default") | Integer |  |  | Min: 0<br>Max: 16 | Set default metric for the routes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;networks</samp>](## "router_rip.vrfs.[].networks") | List, items: String |  |  | Min Length: 1 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "router_rip.vrfs.[].networks.[]") | String |  |  |  | Subnet/Mask. e.g. 192.168.10.0/24. |

=== "YAML"

    ```yaml
    # Routing Information Protocol settings.
    router_rip:
      vrfs:
        - enabled: <bool>
          vrf: <str; required; unique>

          # Set default metric for the routes.
          metric_default: <int; 0-16>
          networks: # >=1 items

              # Subnet/Mask. e.g. 192.168.10.0/24.
            - <str>
    ```
