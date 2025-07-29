<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>router_rip</samp>](## "router_rip") | List, items: Dictionary |  |  |  | Routing Information Protocol settings. |
    | [<samp>&nbsp;&nbsp;-&nbsp;enabled</samp>](## "router_rip.[].enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "router_rip.[].vrf") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;default_metric</samp>](## "router_rip.[].default_metric") | Integer |  |  | Min: 0<br>Max: 16 | Set default metric for the routes |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;networks</samp>](## "router_rip.[].networks") | List, items: String |  |  | Min Length: 1 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "router_rip.[].networks.[]") | String |  |  |  | Subnet/Mask. e.g. 192.168.10.0/24. |

=== "YAML"

    ```yaml
    # Routing Information Protocol settings.
    router_rip:
      - enabled: <bool>
        vrf: <str; required; unique>

        # Set default metric for the routes
        default_metric: <int; 0-16>
        networks: # >=1 items

            # Subnet/Mask. e.g. 192.168.10.0/24.
          - <str>
    ```
