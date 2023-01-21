---
search:
  boost: 2
---

# VLAN Internal Order
## VLAN Internal Order

=== "Table"


    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>vlan_internal_order</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;allocation</samp> | String | Required |  | Valid Values:<br>- ascending<br>- descending |  |
    | <samp>&nbsp;&nbsp;range</samp> | Dictionary | Required |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;beginning</samp> | Integer | Required |  | Min: 1<br>Max: 4094 | Vlan ID |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;ending</samp> | Integer | Required |  | Min: 1<br>Max: 4094 | Vlan ID |

=== "YAML"

    ```yaml
    vlan_internal_order:
      allocation: <str>
      range:
        beginning: <int>
        ending: <int>
    ```
