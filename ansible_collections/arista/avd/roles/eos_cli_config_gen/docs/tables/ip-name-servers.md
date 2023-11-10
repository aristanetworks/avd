<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>ip_name_servers</samp>](## "ip_name_servers") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;-&nbsp;ip_address</samp>](## "ip_name_servers.[].ip_address") | String |  |  |  | IPv4 or IPv6 address for DNS server |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "ip_name_servers.[].vrf") | String |  |  |  | VRF Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "ip_name_servers.[].priority") | Integer |  |  | Min: 0<br>Max: 4 | Priority value (lower is first) |

=== "YAML"

    ```yaml
    ip_name_servers:

        # IPv4 or IPv6 address for DNS server
      - ip_address: <str>

        # VRF Name
        vrf: <str>

        # Priority value (lower is first)
        priority: <int; 0-4>
    ```
