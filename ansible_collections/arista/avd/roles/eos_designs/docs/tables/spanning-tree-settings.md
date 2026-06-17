<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>spanning_tree_settings</samp>](## "spanning_tree_settings") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;mode</samp>](## "spanning_tree_settings.mode") | String |  |  | Valid Values:<br>- <code>mstp</code><br>- <code>rstp</code><br>- <code>rapid-pvst</code><br>- <code>none</code> | Spanning tree operating mode.<br>"spanning_tree_mode" can also be set under node type settings.<br>If both are set, the setting under node type settings takes precedence. |
    | [<samp>&nbsp;&nbsp;priority</samp>](## "spanning_tree_settings.priority") | Integer |  | `32768` |  | Spanning-tree priority configured for the selected mode.<br>For `rapid-pvst` the priority can also be set per VLAN under network services.<br>"spanning_tree_priority" can also be set under node type settings.<br>If both are set, the setting under node type settings takes precedence. |
    | [<samp>&nbsp;&nbsp;port_id_allocation_port_channel_range</samp>](## "spanning_tree_settings.port_id_allocation_port_channel_range") | Dictionary |  |  |  | Specify range of port-ids to reserve for port-channels.<br>"spanning_tree_port_id_allocation_port_channel_range" can also be set under node type settings.<br>If both are set, the setting under node type settings takes precedence. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;minimum</samp>](## "spanning_tree_settings.port_id_allocation_port_channel_range.minimum") | Integer | Required |  | Min: 1<br>Max: 2048 | Specify minimum value for reserved range. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;maximum</samp>](## "spanning_tree_settings.port_id_allocation_port_channel_range.maximum") | Integer | Required |  | Min: 1<br>Max: 2048 | Specify maximum value for reserved range. |
    | [<samp>&nbsp;&nbsp;loop_guard_default</samp>](## "spanning_tree_settings.loop_guard_default") | Boolean |  | `False` |  | Enable loopguard by default on all ports. |

=== "YAML"

    ```yaml
    spanning_tree_settings:

      # Spanning tree operating mode.
      # "spanning_tree_mode" can also be set under node type settings.
      # If both are set, the setting under node type settings takes precedence.
      mode: <str; "mstp" | "rstp" | "rapid-pvst" | "none">

      # Spanning-tree priority configured for the selected mode.
      # For `rapid-pvst` the priority can also be set per VLAN under network services.
      # "spanning_tree_priority" can also be set under node type settings.
      # If both are set, the setting under node type settings takes precedence.
      priority: <int; default=32768>

      # Specify range of port-ids to reserve for port-channels.
      # "spanning_tree_port_id_allocation_port_channel_range" can also be set under node type settings.
      # If both are set, the setting under node type settings takes precedence.
      port_id_allocation_port_channel_range:

        # Specify minimum value for reserved range.
        minimum: <int; 1-2048; required>

        # Specify maximum value for reserved range.
        maximum: <int; 1-2048; required>

      # Enable loopguard by default on all ports.
      loop_guard_default: <bool; default=False>
    ```
