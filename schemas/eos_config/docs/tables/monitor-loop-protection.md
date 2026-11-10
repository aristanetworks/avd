<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>monitor_loop_protection</samp>](## "monitor_loop_protection") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;enabled</samp>](## "monitor_loop_protection.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;disabled_time</samp>](## "monitor_loop_protection.disabled_time") | Integer |  |  | Min: 0<br>Max: 604800 | Port disable time. EOS default is 604800 seconds (7 days).<br>0 indicates that the disabled device should not automatically come back up. |
    | [<samp>&nbsp;&nbsp;protect_vlan</samp>](## "monitor_loop_protection.protect_vlan") | String |  |  |  | VLAN range as string.<br>"< vlan_id >, < vlan_id >-< vlan_id >"<br>Example: 15,16,17,18 |
    | [<samp>&nbsp;&nbsp;rate_limit</samp>](## "monitor_loop_protection.rate_limit") | Integer |  |  | Min: 0<br>Max: 1000 | Rate limits the loop detection frames. EOS default is 1000/second. |
    | [<samp>&nbsp;&nbsp;transmit_interval</samp>](## "monitor_loop_protection.transmit_interval") | Integer |  |  | Min: 1<br>Max: 10 | Loop protection packet transmit interval. EOS default is 5 seconds. |

=== "YAML"

    ```yaml
    monitor_loop_protection:
      enabled: <bool>

      # Port disable time. EOS default is 604800 seconds (7 days).
      # 0 indicates that the disabled device should not automatically come back up.
      disabled_time: <int; 0-604800>

      # VLAN range as string.
      # "< vlan_id >, < vlan_id >-< vlan_id >"
      # Example: 15,16,17,18
      protect_vlan: <str>

      # Rate limits the loop detection frames. EOS default is 1000/second.
      rate_limit: <int; 0-1000>

      # Loop protection packet transmit interval. EOS default is 5 seconds.
      transmit_interval: <int; 1-10>
    ```
