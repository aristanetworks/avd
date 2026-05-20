<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>&lt;node_type_keys.key&gt;</samp>](## "<node_type_keys.key>") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;defaults</samp>](## "<node_type_keys.key>.defaults") | Dictionary |  |  |  | Define variables for all nodes of this type. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_settings</samp>](## "<node_type_keys.key>.defaults.spanning_tree_settings") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "<node_type_keys.key>.defaults.spanning_tree_settings.mode") | String |  |  | Valid Values:<br>- <code>mstp</code><br>- <code>rstp</code><br>- <code>rapid-pvst</code><br>- <code>none</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "<node_type_keys.key>.defaults.spanning_tree_settings.priority") | Integer |  | `32768` |  | Spanning-tree priority configured for the selected mode.<br>For `rapid-pvst` the priority can also be set per VLAN under network services. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;root_super</samp>](## "<node_type_keys.key>.defaults.spanning_tree_settings.root_super") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mst_pvst_boundary</samp>](## "<node_type_keys.key>.defaults.spanning_tree_settings.mst_pvst_boundary") | Boolean |  |  |  | Enable MST PVST border ports. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port_id_allocation_port_channel_range</samp>](## "<node_type_keys.key>.defaults.spanning_tree_settings.port_id_allocation_port_channel_range") | Dictionary |  |  |  | Specify range of port-ids to reserve for port-channels. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;minimum</samp>](## "<node_type_keys.key>.defaults.spanning_tree_settings.port_id_allocation_port_channel_range.minimum") | Integer | Required |  | Min: 1<br>Max: 2048 | Specify minimum value for reserved range. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum</samp>](## "<node_type_keys.key>.defaults.spanning_tree_settings.port_id_allocation_port_channel_range.maximum") | Integer | Required |  | Min: 1<br>Max: 2048 | Specify maximum value for reserved range. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loop_guard_default</samp>](## "<node_type_keys.key>.defaults.spanning_tree_settings.loop_guard_default") | Boolean |  | `False` |  | Enable loopguard by default on all ports. |
    | [<samp>&nbsp;&nbsp;node_groups</samp>](## "<node_type_keys.key>.node_groups") | List, items: Dictionary |  |  |  | Define variables related to all nodes part of this group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;group</samp>](## "<node_type_keys.key>.node_groups.[].group") | String | Required, Unique |  |  | The Node Group Name is used for MLAG domain unless set with 'mlag_domain_id'.<br>The Node Group Name is also used for peer description on downstream switches' uplinks.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "<node_type_keys.key>.node_groups.[].nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_settings</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].spanning_tree_settings") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].spanning_tree_settings.mode") | String |  |  | Valid Values:<br>- <code>mstp</code><br>- <code>rstp</code><br>- <code>rapid-pvst</code><br>- <code>none</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].spanning_tree_settings.priority") | Integer |  | `32768` |  | Spanning-tree priority configured for the selected mode.<br>For `rapid-pvst` the priority can also be set per VLAN under network services. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;root_super</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].spanning_tree_settings.root_super") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mst_pvst_boundary</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].spanning_tree_settings.mst_pvst_boundary") | Boolean |  |  |  | Enable MST PVST border ports. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port_id_allocation_port_channel_range</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].spanning_tree_settings.port_id_allocation_port_channel_range") | Dictionary |  |  |  | Specify range of port-ids to reserve for port-channels. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;minimum</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].spanning_tree_settings.port_id_allocation_port_channel_range.minimum") | Integer | Required |  | Min: 1<br>Max: 2048 | Specify minimum value for reserved range. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].spanning_tree_settings.port_id_allocation_port_channel_range.maximum") | Integer | Required |  | Min: 1<br>Max: 2048 | Specify maximum value for reserved range. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loop_guard_default</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].spanning_tree_settings.loop_guard_default") | Boolean |  | `False` |  | Enable loopguard by default on all ports. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_settings</samp>](## "<node_type_keys.key>.node_groups.[].spanning_tree_settings") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "<node_type_keys.key>.node_groups.[].spanning_tree_settings.mode") | String |  |  | Valid Values:<br>- <code>mstp</code><br>- <code>rstp</code><br>- <code>rapid-pvst</code><br>- <code>none</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "<node_type_keys.key>.node_groups.[].spanning_tree_settings.priority") | Integer |  | `32768` |  | Spanning-tree priority configured for the selected mode.<br>For `rapid-pvst` the priority can also be set per VLAN under network services. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;root_super</samp>](## "<node_type_keys.key>.node_groups.[].spanning_tree_settings.root_super") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mst_pvst_boundary</samp>](## "<node_type_keys.key>.node_groups.[].spanning_tree_settings.mst_pvst_boundary") | Boolean |  |  |  | Enable MST PVST border ports. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port_id_allocation_port_channel_range</samp>](## "<node_type_keys.key>.node_groups.[].spanning_tree_settings.port_id_allocation_port_channel_range") | Dictionary |  |  |  | Specify range of port-ids to reserve for port-channels. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;minimum</samp>](## "<node_type_keys.key>.node_groups.[].spanning_tree_settings.port_id_allocation_port_channel_range.minimum") | Integer | Required |  | Min: 1<br>Max: 2048 | Specify minimum value for reserved range. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum</samp>](## "<node_type_keys.key>.node_groups.[].spanning_tree_settings.port_id_allocation_port_channel_range.maximum") | Integer | Required |  | Min: 1<br>Max: 2048 | Specify maximum value for reserved range. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loop_guard_default</samp>](## "<node_type_keys.key>.node_groups.[].spanning_tree_settings.loop_guard_default") | Boolean |  | `False` |  | Enable loopguard by default on all ports. |
    | [<samp>&nbsp;&nbsp;nodes</samp>](## "<node_type_keys.key>.nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<node_type_keys.key>.nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_settings</samp>](## "<node_type_keys.key>.nodes.[].spanning_tree_settings") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "<node_type_keys.key>.nodes.[].spanning_tree_settings.mode") | String |  |  | Valid Values:<br>- <code>mstp</code><br>- <code>rstp</code><br>- <code>rapid-pvst</code><br>- <code>none</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "<node_type_keys.key>.nodes.[].spanning_tree_settings.priority") | Integer |  | `32768` |  | Spanning-tree priority configured for the selected mode.<br>For `rapid-pvst` the priority can also be set per VLAN under network services. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;root_super</samp>](## "<node_type_keys.key>.nodes.[].spanning_tree_settings.root_super") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mst_pvst_boundary</samp>](## "<node_type_keys.key>.nodes.[].spanning_tree_settings.mst_pvst_boundary") | Boolean |  |  |  | Enable MST PVST border ports. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port_id_allocation_port_channel_range</samp>](## "<node_type_keys.key>.nodes.[].spanning_tree_settings.port_id_allocation_port_channel_range") | Dictionary |  |  |  | Specify range of port-ids to reserve for port-channels. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;minimum</samp>](## "<node_type_keys.key>.nodes.[].spanning_tree_settings.port_id_allocation_port_channel_range.minimum") | Integer | Required |  | Min: 1<br>Max: 2048 | Specify minimum value for reserved range. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum</samp>](## "<node_type_keys.key>.nodes.[].spanning_tree_settings.port_id_allocation_port_channel_range.maximum") | Integer | Required |  | Min: 1<br>Max: 2048 | Specify maximum value for reserved range. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loop_guard_default</samp>](## "<node_type_keys.key>.nodes.[].spanning_tree_settings.loop_guard_default") | Boolean |  | `False` |  | Enable loopguard by default on all ports. |
    | [<samp>device_profiles</samp>](## "device_profiles") | List, items: Dictionary |  |  |  | PREVIEW - This datamodel is still under development and may change or get removed at any time. |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "device_profiles.[].name") | String | Required, Unique |  |  | Profile Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_settings</samp>](## "device_profiles.[].spanning_tree_settings") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "device_profiles.[].spanning_tree_settings.mode") | String |  |  | Valid Values:<br>- <code>mstp</code><br>- <code>rstp</code><br>- <code>rapid-pvst</code><br>- <code>none</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "device_profiles.[].spanning_tree_settings.priority") | Integer |  | `32768` |  | Spanning-tree priority configured for the selected mode.<br>For `rapid-pvst` the priority can also be set per VLAN under network services. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;root_super</samp>](## "device_profiles.[].spanning_tree_settings.root_super") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mst_pvst_boundary</samp>](## "device_profiles.[].spanning_tree_settings.mst_pvst_boundary") | Boolean |  |  |  | Enable MST PVST border ports. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port_id_allocation_port_channel_range</samp>](## "device_profiles.[].spanning_tree_settings.port_id_allocation_port_channel_range") | Dictionary |  |  |  | Specify range of port-ids to reserve for port-channels. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;minimum</samp>](## "device_profiles.[].spanning_tree_settings.port_id_allocation_port_channel_range.minimum") | Integer | Required |  | Min: 1<br>Max: 2048 | Specify minimum value for reserved range. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum</samp>](## "device_profiles.[].spanning_tree_settings.port_id_allocation_port_channel_range.maximum") | Integer | Required |  | Min: 1<br>Max: 2048 | Specify maximum value for reserved range. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loop_guard_default</samp>](## "device_profiles.[].spanning_tree_settings.loop_guard_default") | Boolean |  | `False` |  | Enable loopguard by default on all ports. |
    | [<samp>devices</samp>](## "devices") | List, items: Dictionary |  |  |  | PREVIEW - This datamodel is still under development and may change or get removed at any time. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "devices.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_settings</samp>](## "devices.[].spanning_tree_settings") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "devices.[].spanning_tree_settings.mode") | String |  |  | Valid Values:<br>- <code>mstp</code><br>- <code>rstp</code><br>- <code>rapid-pvst</code><br>- <code>none</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "devices.[].spanning_tree_settings.priority") | Integer |  | `32768` |  | Spanning-tree priority configured for the selected mode.<br>For `rapid-pvst` the priority can also be set per VLAN under network services. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;root_super</samp>](## "devices.[].spanning_tree_settings.root_super") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mst_pvst_boundary</samp>](## "devices.[].spanning_tree_settings.mst_pvst_boundary") | Boolean |  |  |  | Enable MST PVST border ports. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port_id_allocation_port_channel_range</samp>](## "devices.[].spanning_tree_settings.port_id_allocation_port_channel_range") | Dictionary |  |  |  | Specify range of port-ids to reserve for port-channels. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;minimum</samp>](## "devices.[].spanning_tree_settings.port_id_allocation_port_channel_range.minimum") | Integer | Required |  | Min: 1<br>Max: 2048 | Specify minimum value for reserved range. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum</samp>](## "devices.[].spanning_tree_settings.port_id_allocation_port_channel_range.maximum") | Integer | Required |  | Min: 1<br>Max: 2048 | Specify maximum value for reserved range. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loop_guard_default</samp>](## "devices.[].spanning_tree_settings.loop_guard_default") | Boolean |  | `False` |  | Enable loopguard by default on all ports. |

=== "YAML"

    ```yaml
    <node_type_keys.key>:

      # Define variables for all nodes of this type.
      defaults:
        spanning_tree_settings:
          mode: <str; "mstp" | "rstp" | "rapid-pvst" | "none">

          # Spanning-tree priority configured for the selected mode.
          # For `rapid-pvst` the priority can also be set per VLAN under network services.
          priority: <int; default=32768>
          root_super: <bool; default=False>

          # Enable MST PVST border ports.
          mst_pvst_boundary: <bool>

          # Specify range of port-ids to reserve for port-channels.
          port_id_allocation_port_channel_range:

            # Specify minimum value for reserved range.
            minimum: <int; 1-2048; required>

            # Specify maximum value for reserved range.
            maximum: <int; 1-2048; required>

          # Enable loopguard by default on all ports.
          loop_guard_default: <bool; default=False>

      # Define variables related to all nodes part of this group.
      node_groups:

          # The Node Group Name is used for MLAG domain unless set with 'mlag_domain_id'.
          # The Node Group Name is also used for peer description on downstream switches' uplinks.
        - group: <str; required; unique>

          # Define variables per node.
          nodes:

              # The Node Name is used as "hostname".
            - name: <str; required; unique>
              spanning_tree_settings:
                mode: <str; "mstp" | "rstp" | "rapid-pvst" | "none">

                # Spanning-tree priority configured for the selected mode.
                # For `rapid-pvst` the priority can also be set per VLAN under network services.
                priority: <int; default=32768>
                root_super: <bool; default=False>

                # Enable MST PVST border ports.
                mst_pvst_boundary: <bool>

                # Specify range of port-ids to reserve for port-channels.
                port_id_allocation_port_channel_range:

                  # Specify minimum value for reserved range.
                  minimum: <int; 1-2048; required>

                  # Specify maximum value for reserved range.
                  maximum: <int; 1-2048; required>

                # Enable loopguard by default on all ports.
                loop_guard_default: <bool; default=False>
          spanning_tree_settings:
            mode: <str; "mstp" | "rstp" | "rapid-pvst" | "none">

            # Spanning-tree priority configured for the selected mode.
            # For `rapid-pvst` the priority can also be set per VLAN under network services.
            priority: <int; default=32768>
            root_super: <bool; default=False>

            # Enable MST PVST border ports.
            mst_pvst_boundary: <bool>

            # Specify range of port-ids to reserve for port-channels.
            port_id_allocation_port_channel_range:

              # Specify minimum value for reserved range.
              minimum: <int; 1-2048; required>

              # Specify maximum value for reserved range.
              maximum: <int; 1-2048; required>

            # Enable loopguard by default on all ports.
            loop_guard_default: <bool; default=False>

      # Define variables per node.
      nodes:

          # The Node Name is used as "hostname".
        - name: <str; required; unique>
          spanning_tree_settings:
            mode: <str; "mstp" | "rstp" | "rapid-pvst" | "none">

            # Spanning-tree priority configured for the selected mode.
            # For `rapid-pvst` the priority can also be set per VLAN under network services.
            priority: <int; default=32768>
            root_super: <bool; default=False>

            # Enable MST PVST border ports.
            mst_pvst_boundary: <bool>

            # Specify range of port-ids to reserve for port-channels.
            port_id_allocation_port_channel_range:

              # Specify minimum value for reserved range.
              minimum: <int; 1-2048; required>

              # Specify maximum value for reserved range.
              maximum: <int; 1-2048; required>

            # Enable loopguard by default on all ports.
            loop_guard_default: <bool; default=False>

    # PREVIEW - This datamodel is still under development and may change or get removed at any time.
    device_profiles:

        # Profile Name
      - name: <str; required; unique>
        spanning_tree_settings:
          mode: <str; "mstp" | "rstp" | "rapid-pvst" | "none">

          # Spanning-tree priority configured for the selected mode.
          # For `rapid-pvst` the priority can also be set per VLAN under network services.
          priority: <int; default=32768>
          root_super: <bool; default=False>

          # Enable MST PVST border ports.
          mst_pvst_boundary: <bool>

          # Specify range of port-ids to reserve for port-channels.
          port_id_allocation_port_channel_range:

            # Specify minimum value for reserved range.
            minimum: <int; 1-2048; required>

            # Specify maximum value for reserved range.
            maximum: <int; 1-2048; required>

          # Enable loopguard by default on all ports.
          loop_guard_default: <bool; default=False>

    # PREVIEW - This datamodel is still under development and may change or get removed at any time.
    devices:

        # The Node Name is used as "hostname".
        name: <str; required; unique>
        spanning_tree_settings:
          mode: <str; "mstp" | "rstp" | "rapid-pvst" | "none">

          # Spanning-tree priority configured for the selected mode.
          # For `rapid-pvst` the priority can also be set per VLAN under network services.
          priority: <int; default=32768>
          root_super: <bool; default=False>

          # Enable MST PVST border ports.
          mst_pvst_boundary: <bool>

          # Specify range of port-ids to reserve for port-channels.
          port_id_allocation_port_channel_range:

            # Specify minimum value for reserved range.
            minimum: <int; 1-2048; required>

            # Specify maximum value for reserved range.
            maximum: <int; 1-2048; required>

          # Enable loopguard by default on all ports.
          loop_guard_default: <bool; default=False>
    ```
