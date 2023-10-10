<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>lldp_topology</samp>](## "lldp_topology") | List, items: Dictionary |  |  |  | LLDP Topology.<br>Used to generate AVD configurations directly from the given topology if `use_lldp_topology` is set to `true`.<br>Neighbor hostnames must match the inventory hostnames of the AVD inventory to be taken into consideration.<br>Requires `default_interfaces` to be set, to detect the proper interface roles automatically.<br>Currently providing the following configurations based on the given LLDP topology and `default_interfaces`:<br>- `uplink_switches`.<br>- `uplink_interfaces`<br>- `uplink_switch_interfaces`<br>- `mlag_interfaces`<br>- `# mlag_peer` (future)<br>- `platform`<br>- `mgmt_interface`<br>NOTES:<br>- Any derived configuration can be overridden by setting the key manually.<br>  Even keys set under node type `defaults` will take precedence over these derived configurations.<br>- when using parallel links between the same devices for L3 uplinks it is important to set<br>  `max_uplink_switches` and `max_parallel_uplinks` to ensure consistent IP addressing. |
    | [<samp>&nbsp;&nbsp;- hostname</samp>](## "lldp_topology.[].hostname") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;platform</samp>](## "lldp_topology.[].platform") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;interfaces</samp>](## "lldp_topology.[].interfaces") | List, items: Dictionary | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "lldp_topology.[].interfaces.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;neighbor</samp>](## "lldp_topology.[].interfaces.[].neighbor") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;neighbor_interface</samp>](## "lldp_topology.[].interfaces.[].neighbor_interface") | String |  |  |  |  |
    | [<samp>use_lldp_topology</samp>](## "use_lldp_topology") | Boolean |  |  |  | Generate AVD configurations directly from a given LLDP Topology.<br>See `lldp_topology` for details. |

=== "YAML"

    ```yaml
    lldp_topology:
      - hostname: <str>
        platform: <str>
        interfaces:
          - name: <str>
            neighbor: <str>
            neighbor_interface: <str>
    use_lldp_topology: <bool>
    ```
