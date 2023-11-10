<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>vlans</samp>](## "vlans") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- id</samp>](## "vlans.[].id") | Integer | Required, Unique |  |  | VLAN ID |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "vlans.[].name") | String |  |  |  | VLAN Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;state</samp>](## "vlans.[].state") | String |  |  | Valid Values:<br>- active<br>- suspend |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;trunk_groups</samp>](## "vlans.[].trunk_groups") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "vlans.[].trunk_groups.[].&lt;str&gt;") | String |  |  |  | Trunk Group Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;private_vlan</samp>](## "vlans.[].private_vlan") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "vlans.[].private_vlan.type") | String |  |  | Valid Values:<br>- community<br>- isolated |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;primary_vlan</samp>](## "vlans.[].private_vlan.primary_vlan") | Integer |  |  |  | Primary VLAN ID |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;tenant</samp>](## "vlans.[].tenant") | String |  |  |  | Key only used for documentation or validation purposes |

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
