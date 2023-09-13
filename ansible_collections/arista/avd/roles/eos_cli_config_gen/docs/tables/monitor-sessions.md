<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>monitor_sessions</samp>](## "monitor_sessions") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- name</samp>](## "monitor_sessions.[].name") | String | Required |  |  | Session Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sources</samp>](## "monitor_sessions.[].sources") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "monitor_sessions.[].sources.[].name") | String |  |  |  | Interface name, range or comma separated list |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction</samp>](## "monitor_sessions.[].sources.[].direction") | String |  |  | Valid Values:<br>- rx<br>- tx<br>- both |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_group</samp>](## "monitor_sessions.[].sources.[].access_group") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "monitor_sessions.[].sources.[].access_group.type") | String |  |  | Valid Values:<br>- ip<br>- ipv6<br>- mac |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "monitor_sessions.[].sources.[].access_group.name") | String |  |  |  | ACL Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "monitor_sessions.[].sources.[].access_group.priority") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;destinations</samp>](## "monitor_sessions.[].destinations") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "monitor_sessions.[].destinations.[].&lt;str&gt;") | String |  |  |  | 'cpu' or interface name, range or comma separated list |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;encapsulation_gre_metadata_tx</samp>](## "monitor_sessions.[].encapsulation_gre_metadata_tx") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;header_remove_size</samp>](## "monitor_sessions.[].header_remove_size") | Integer |  |  |  | Number of bytes to remove from header |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;access_group</samp>](## "monitor_sessions.[].access_group") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "monitor_sessions.[].access_group.type") | String |  |  | Valid Values:<br>- ip<br>- ipv6<br>- mac |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "monitor_sessions.[].access_group.name") | String |  |  |  | ACL Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;rate_limit_per_ingress_chip</samp>](## "monitor_sessions.[].rate_limit_per_ingress_chip") | String |  |  |  | Ratelimit and unit as string.<br>Examples:<br>  "100000 bps"<br>  "100 kbps"<br>  "10 mbps"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;rate_limit_per_egress_chip</samp>](## "monitor_sessions.[].rate_limit_per_egress_chip") | String |  |  |  | Ratelimit and unit as string.<br>Examples:<br>  "100000 bps"<br>  "100 kbps"<br>  "10 mbps"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sample</samp>](## "monitor_sessions.[].sample") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;truncate</samp>](## "monitor_sessions.[].truncate") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "monitor_sessions.[].truncate.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;size</samp>](## "monitor_sessions.[].truncate.size") | Integer |  |  |  | Size in bytes |

=== "YAML"

    ```yaml
    monitor_sessions:
      - name: <str>
        sources:
          - name: <str>
            direction: <str>
            access_group:
              type: <str>
              name: <str>
              priority: <int>
        destinations:
          - <str>
        encapsulation_gre_metadata_tx: <bool>
        header_remove_size: <int>
        access_group:
          type: <str>
          name: <str>
        rate_limit_per_ingress_chip: <str>
        rate_limit_per_egress_chip: <str>
        sample: <int>
        truncate:
          enabled: <bool>
          size: <int>
    ```
