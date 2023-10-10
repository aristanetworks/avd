<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>lldp_topology</samp>](## "lldp_topology") | List, items: Dictionary |  |  |  | Generate AVD configurations directly from the given Topology.<br>Activate this feature by setting `use_lldp_topology` to `true`.<br>Requires `default_interfaces` to be set for the relevant platforms and node types to detect the proper interface roles automatically.<br>Neighbor hostnames must match the inventory hostnames of the AVD inventory to be taken into consideration. |
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
