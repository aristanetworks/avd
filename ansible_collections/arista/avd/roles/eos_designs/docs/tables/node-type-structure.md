<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>&lt;node_type_keys.key&gt;</samp>](## "<node_type_keys.key>") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;defaults</samp>](## "<node_type_keys.key>.defaults") | Dictionary |  |  |  | Define variables for all nodes of this type. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_port_id_allocation_port_channel_range</samp>](## "<node_type_keys.key>.defaults.spanning_tree_port_id_allocation_port_channel_range") | Dictionary |  |  |  | Specify range of port-ids to reserve for port-channels. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;minimum</samp>](## "<node_type_keys.key>.defaults.spanning_tree_port_id_allocation_port_channel_range.minimum") | Integer | Required |  | Min: 1<br>Max: 2048 | Specify minimum value for reserved range. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum</samp>](## "<node_type_keys.key>.defaults.spanning_tree_port_id_allocation_port_channel_range.maximum") | Integer | Required |  | Min: 1<br>Max: 2048 | Specify maximum value for reserved range. |
    | [<samp>&nbsp;&nbsp;node_groups</samp>](## "<node_type_keys.key>.node_groups") | List, items: Dictionary |  |  |  | Define variables related to all nodes part of this group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;group</samp>](## "<node_type_keys.key>.node_groups.[].group") | String | Required, Unique |  |  | The Node Group Name is used for MLAG domain unless set with 'mlag_domain_id'.<br>The Node Group Name is also used for peer description on downstream switches' uplinks.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "<node_type_keys.key>.node_groups.[].nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_port_id_allocation_port_channel_range</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].spanning_tree_port_id_allocation_port_channel_range") | Dictionary |  |  |  | Specify range of port-ids to reserve for port-channels. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;minimum</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].spanning_tree_port_id_allocation_port_channel_range.minimum") | Integer | Required |  | Min: 1<br>Max: 2048 | Specify minimum value for reserved range. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].spanning_tree_port_id_allocation_port_channel_range.maximum") | Integer | Required |  | Min: 1<br>Max: 2048 | Specify maximum value for reserved range. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_port_id_allocation_port_channel_range</samp>](## "<node_type_keys.key>.node_groups.[].spanning_tree_port_id_allocation_port_channel_range") | Dictionary |  |  |  | Specify range of port-ids to reserve for port-channels. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;minimum</samp>](## "<node_type_keys.key>.node_groups.[].spanning_tree_port_id_allocation_port_channel_range.minimum") | Integer | Required |  | Min: 1<br>Max: 2048 | Specify minimum value for reserved range. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum</samp>](## "<node_type_keys.key>.node_groups.[].spanning_tree_port_id_allocation_port_channel_range.maximum") | Integer | Required |  | Min: 1<br>Max: 2048 | Specify maximum value for reserved range. |
    | [<samp>&nbsp;&nbsp;nodes</samp>](## "<node_type_keys.key>.nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<node_type_keys.key>.nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_port_id_allocation_port_channel_range</samp>](## "<node_type_keys.key>.nodes.[].spanning_tree_port_id_allocation_port_channel_range") | Dictionary |  |  |  | Specify range of port-ids to reserve for port-channels. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;minimum</samp>](## "<node_type_keys.key>.nodes.[].spanning_tree_port_id_allocation_port_channel_range.minimum") | Integer | Required |  | Min: 1<br>Max: 2048 | Specify minimum value for reserved range. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum</samp>](## "<node_type_keys.key>.nodes.[].spanning_tree_port_id_allocation_port_channel_range.maximum") | Integer | Required |  | Min: 1<br>Max: 2048 | Specify maximum value for reserved range. |

=== "YAML"

    ```yaml
    <node_type_keys.key>:

      # Define variables for all nodes of this type.
      defaults:

        # Specify range of port-ids to reserve for port-channels.
        spanning_tree_port_id_allocation_port_channel_range:

          # Specify minimum value for reserved range.
          minimum: <int; 1-2048; required>

          # Specify maximum value for reserved range.
          maximum: <int; 1-2048; required>

      # Define variables related to all nodes part of this group.
      node_groups:

          # The Node Group Name is used for MLAG domain unless set with 'mlag_domain_id'.
          # The Node Group Name is also used for peer description on downstream switches' uplinks.
        - group: <str; required; unique>

          # Define variables per node.
          nodes:

              # The Node Name is used as "hostname".
            - name: <str; required; unique>

              # Specify range of port-ids to reserve for port-channels.
              spanning_tree_port_id_allocation_port_channel_range:

                # Specify minimum value for reserved range.
                minimum: <int; 1-2048; required>

                # Specify maximum value for reserved range.
                maximum: <int; 1-2048; required>

          # Specify range of port-ids to reserve for port-channels.
          spanning_tree_port_id_allocation_port_channel_range:

            # Specify minimum value for reserved range.
            minimum: <int; 1-2048; required>

            # Specify maximum value for reserved range.
            maximum: <int; 1-2048; required>

      # Define variables per node.
      nodes:

          # The Node Name is used as "hostname".
        - name: <str; required; unique>

          # Specify range of port-ids to reserve for port-channels.
          spanning_tree_port_id_allocation_port_channel_range:

            # Specify minimum value for reserved range.
            minimum: <int; 1-2048; required>

            # Specify maximum value for reserved range.
            maximum: <int; 1-2048; required>
    ```
