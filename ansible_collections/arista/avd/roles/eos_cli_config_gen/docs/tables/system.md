<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>system</samp>](## "system") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;control_plane</samp>](## "system.control_plane") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;tcp_mss</samp>](## "system.control_plane.tcp_mss") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp>](## "system.control_plane.tcp_mss.ipv4") | Integer |  |  |  | Segment size |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6</samp>](## "system.control_plane.tcp_mss.ipv6") | Integer |  |  |  | Segment size |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv4_access_groups</samp>](## "system.control_plane.ipv4_access_groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- acl_name</samp>](## "system.control_plane.ipv4_access_groups.[].acl_name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "system.control_plane.ipv4_access_groups.[].vrf") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_access_groups</samp>](## "system.control_plane.ipv6_access_groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- acl_name</samp>](## "system.control_plane.ipv6_access_groups.[].acl_name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "system.control_plane.ipv6_access_groups.[].vrf") | String |  |  |  |  |

=== "YAML"

    ```yaml
    system:
      control_plane:
        tcp_mss:
          ipv4: <int>
          ipv6: <int>
        ipv4_access_groups:
          - acl_name: <str>
            vrf: <str>
        ipv6_access_groups:
          - acl_name: <str>
            vrf: <str>
    ```
