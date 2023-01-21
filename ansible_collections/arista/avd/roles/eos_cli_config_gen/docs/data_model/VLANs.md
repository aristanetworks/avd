---
search:
  boost: 2
---

# VLANs
## VLANs

=== "VLANs"


    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>vlans</samp> | List, items: Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;- id</samp> | Integer | Required, Unique |  |  | VLAN ID |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp> | String |  |  |  | VLAN Name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;state</samp> | String |  |  | Valid Values:<br>- active<br>- suspend |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;trunk_groups</samp> | List, items: String |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp> | String |  |  |  | Trunk Group Name |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;private_vlan</samp> | Dictionary |  |  |  |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp> | String |  |  | Valid Values:<br>- community<br>- isolated |  |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;primary_vlan</samp> | Integer |  |  |  | Primary VLAN ID |
    | <samp>&nbsp;&nbsp;&nbsp;&nbsp;tenant</samp> | String |  |  |  | Key only used for documentation or validation purposes |

=== "YAML"

    ```yaml
    vlans:
      - id: <int>
        name: <str>
        state: <str>
        trunk_groups:
          - <str>
        private_vlan:
          type: <str>
          primary_vlan: <int>
        tenant: <str>
    ```
