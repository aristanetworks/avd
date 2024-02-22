<!--
  ~ Copyright (c) 2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>policy_maps</samp>](## "policy_maps") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;pbr</samp>](## "policy_maps.pbr") | List, items: Dictionary |  |  |  | PBR Policy-Maps |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "policy_maps.pbr.[].name") | String | Required, Unique |  |  | Policy-Map Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;classes</samp>](## "policy_maps.pbr.[].classes") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "policy_maps.pbr.[].classes.[].name") | String | Required, Unique |  |  | Class Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;index</samp>](## "policy_maps.pbr.[].classes.[].index") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;drop</samp>](## "policy_maps.pbr.[].classes.[].drop") | Boolean |  |  |  | 'drop' and 'set' are mutually exclusive |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;set</samp>](## "policy_maps.pbr.[].classes.[].set") | Dictionary |  |  |  | Set Nexthop<br>'drop' and 'set' are mutually exclusive<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nexthop</samp>](## "policy_maps.pbr.[].classes.[].set.nexthop") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "policy_maps.pbr.[].classes.[].set.nexthop.ip_address") | String |  |  |  | IPv4 or IPv6 Address |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recursive</samp>](## "policy_maps.pbr.[].classes.[].set.nexthop.recursive") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;qos</samp>](## "policy_maps.qos") | List, items: Dictionary |  |  |  | QOS Policy-Maps |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "policy_maps.qos.[].name") | String | Required, Unique |  |  | Policy-Map Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;classes</samp>](## "policy_maps.qos.[].classes") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "policy_maps.qos.[].classes.[].name") | String | Required, Unique |  |  | Class Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;set</samp>](## "policy_maps.qos.[].classes.[].set") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cos</samp>](## "policy_maps.qos.[].classes.[].set.cos") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dscp</samp>](## "policy_maps.qos.[].classes.[].set.dscp") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;traffic_class</samp>](## "policy_maps.qos.[].classes.[].set.traffic_class") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;drop_precedence</samp>](## "policy_maps.qos.[].classes.[].set.drop_precedence") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;police</samp>](## "policy_maps.qos.[].classes.[].police") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rate</samp>](## "policy_maps.qos.[].classes.[].police.rate") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lower_rate</samp>](## "policy_maps.qos.[].classes.[].police.rate.lower_rate") | Integer |  |  |  | Specify lower rate.<br>Lower rate range in kbps - <8-200000000>. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rate_unit</samp>](## "policy_maps.qos.[].classes.[].police.rate.rate_unit") | String |  | `bps` | Valid Values:<br>- <code>bps</code><br>- <code>kbps</code><br>- <code>mbps</code><br>- <code>pps</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lower_rate_burst_size</samp>](## "policy_maps.qos.[].classes.[].police.rate.lower_rate_burst_size") | Integer |  |  | Min: 256<br>Max: 128000000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;burst_size_unit</samp>](## "policy_maps.qos.[].classes.[].police.rate.burst_size_unit") | String |  | `bytes` | Valid Values:<br>- <code>bytes</code><br>- <code>kbytes</code><br>- <code>mbytes</code><br>- <code>packets</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "policy_maps.qos.[].classes.[].police.rate.action") | String |  |  | Valid Values:<br>- <code>dscp</code><br>- <code>drop-precedence</code> | Set action for policed traffic. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dscp_value</samp>](## "policy_maps.qos.[].classes.[].police.rate.dscp_value") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;higher_rate</samp>](## "policy_maps.qos.[].classes.[].police.rate.higher_rate") | Integer |  |  |  | Specify higher rate. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;higher_rate_burst_size</samp>](## "policy_maps.qos.[].classes.[].police.rate.higher_rate_burst_size") | Integer |  |  | Min: 256<br>Max: 128000000 |  |

=== "YAML"

    ```yaml
    policy_maps:

      # PBR Policy-Maps
      pbr:

          # Policy-Map Name
        - name: <str; required; unique>
          classes:

              # Class Name
            - name: <str; required; unique>
              index: <int>

              # 'drop' and 'set' are mutually exclusive
              drop: <bool>

              # Set Nexthop
              # 'drop' and 'set' are mutually exclusive
              set:
                nexthop:

                  # IPv4 or IPv6 Address
                  ip_address: <str>
                  recursive: <bool>

      # QOS Policy-Maps
      qos:

          # Policy-Map Name
        - name: <str; required; unique>
          classes:

              # Class Name
            - name: <str; required; unique>
              set:
                cos: <int>
                dscp: <str>
                traffic_class: <int>
                drop_precedence: <int>
              police:
                rate:

                  # Specify lower rate.
                  # Lower rate range in kbps - <8-200000000>.
                  lower_rate: <int>
                  rate_unit: <str; "bps" | "kbps" | "mbps" | "pps"; default="bps">
                  lower_rate_burst_size: <int; 256-128000000>
                  burst_size_unit: <str; "bytes" | "kbytes" | "mbytes" | "packets"; default="bytes">

                  # Set action for policed traffic.
                  action: <str; "dscp" | "drop-precedence">
                  dscp_value: <str>

                  # Specify higher rate.
                  higher_rate: <int>
                  higher_rate_burst_size: <int; 256-128000000>
    ```
