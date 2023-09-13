<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>vlan_internal_order</samp>](## "vlan_internal_order") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;allocation</samp>](## "vlan_internal_order.allocation") | String | Required |  | Valid Values:<br>- ascending<br>- descending |  |
    | [<samp>&nbsp;&nbsp;range</samp>](## "vlan_internal_order.range") | Dictionary | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;beginning</samp>](## "vlan_internal_order.range.beginning") | Integer | Required |  | Min: 2<br>Max: 4094 | First VLAN ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ending</samp>](## "vlan_internal_order.range.ending") | Integer | Required |  | Min: 2<br>Max: 4094 | Last VLAN ID. |

=== "YAML"

    ```yaml
    vlan_internal_order:
      allocation: <str>
      range:
        beginning: <int>
        ending: <int>
    ```
