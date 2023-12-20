<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>core_interfaces</samp>](## "core_interfaces") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;l3_interfaces_profiles</samp>](## "core_interfaces.l3_interfaces_profiles") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;profile</samp>](## "core_interfaces.l3_interfaces_profiles.[].profile") | String | Required, Unique |  |  | L3 interface profile name. Any variable supported under `l3_interfaces` can be inherited from a profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;wan_path_group</samp>](## "core_interfaces.l3_interfaces_profiles.[].wan_path_group") | String |  |  |  | PREVIEW: This key is currently not supported<br><br>The WAN path-group this interface is connected to. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;wan_carrier</samp>](## "core_interfaces.l3_interfaces_profiles.[].wan_carrier") | String |  |  |  | PREVIEW: This key is currently not supported<br><br>The WAN Carrier this interface is connected to.<br>This is not rendered in the configuration but used for WAN designs. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;wan_circuit_id</samp>](## "core_interfaces.l3_interfaces_profiles.[].wan_circuit_id") | String |  |  |  | PREVIEW: This key is currently not supported<br><br>The WAN Circuit ID for this interface.<br>This is not rendered in the configuration but used for WAN designs. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cv_pathfinder_connected_to_pathfinder</samp>](## "core_interfaces.l3_interfaces_profiles.[].cv_pathfinder_connected_to_pathfinder") | Boolean |  |  |  | PREVIEW: This key is currently not supported<br><br>For a WAN interface (`wan_path_group` is set), allow to disable the static tunnel towards Pathfinders.<br>Default True. |
    | [<samp>&nbsp;&nbsp;l3_interfaces</samp>](## "core_interfaces.l3_interfaces") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;wan_path_group</samp>](## "core_interfaces.l3_interfaces.[].wan_path_group") | String |  |  |  | PREVIEW: This key is currently not supported<br><br>The WAN path-group this interface is connected to. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;wan_carrier</samp>](## "core_interfaces.l3_interfaces.[].wan_carrier") | String |  |  |  | PREVIEW: This key is currently not supported<br><br>The WAN Carrier this interface is connected to.<br>This is not rendered in the configuration but used for WAN designs. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;wan_circuit_id</samp>](## "core_interfaces.l3_interfaces.[].wan_circuit_id") | String |  |  |  | PREVIEW: This key is currently not supported<br><br>The WAN Circuit ID for this interface.<br>This is not rendered in the configuration but used for WAN designs. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cv_pathfinder_connected_to_pathfinder</samp>](## "core_interfaces.l3_interfaces.[].cv_pathfinder_connected_to_pathfinder") | Boolean |  |  |  | PREVIEW: This key is currently not supported<br><br>For a WAN interface (`wan_path_group` is set), allow to disable the static tunnel towards Pathfinders.<br>Default True. |
    | [<samp>l3_edge</samp>](## "l3_edge") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;l3_interfaces_profiles</samp>](## "l3_edge.l3_interfaces_profiles") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;profile</samp>](## "l3_edge.l3_interfaces_profiles.[].profile") | String | Required, Unique |  |  | L3 interface profile name. Any variable supported under `l3_interfaces` can be inherited from a profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;wan_path_group</samp>](## "l3_edge.l3_interfaces_profiles.[].wan_path_group") | String |  |  |  | PREVIEW: This key is currently not supported<br><br>The WAN path-group this interface is connected to. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;wan_carrier</samp>](## "l3_edge.l3_interfaces_profiles.[].wan_carrier") | String |  |  |  | PREVIEW: This key is currently not supported<br><br>The WAN Carrier this interface is connected to.<br>This is not rendered in the configuration but used for WAN designs. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;wan_circuit_id</samp>](## "l3_edge.l3_interfaces_profiles.[].wan_circuit_id") | String |  |  |  | PREVIEW: This key is currently not supported<br><br>The WAN Circuit ID for this interface.<br>This is not rendered in the configuration but used for WAN designs. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cv_pathfinder_connected_to_pathfinder</samp>](## "l3_edge.l3_interfaces_profiles.[].cv_pathfinder_connected_to_pathfinder") | Boolean |  |  |  | PREVIEW: This key is currently not supported<br><br>For a WAN interface (`wan_path_group` is set), allow to disable the static tunnel towards Pathfinders.<br>Default True. |
    | [<samp>&nbsp;&nbsp;l3_interfaces</samp>](## "l3_edge.l3_interfaces") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;wan_path_group</samp>](## "l3_edge.l3_interfaces.[].wan_path_group") | String |  |  |  | PREVIEW: This key is currently not supported<br><br>The WAN path-group this interface is connected to. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;wan_carrier</samp>](## "l3_edge.l3_interfaces.[].wan_carrier") | String |  |  |  | PREVIEW: This key is currently not supported<br><br>The WAN Carrier this interface is connected to.<br>This is not rendered in the configuration but used for WAN designs. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;wan_circuit_id</samp>](## "l3_edge.l3_interfaces.[].wan_circuit_id") | String |  |  |  | PREVIEW: This key is currently not supported<br><br>The WAN Circuit ID for this interface.<br>This is not rendered in the configuration but used for WAN designs. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cv_pathfinder_connected_to_pathfinder</samp>](## "l3_edge.l3_interfaces.[].cv_pathfinder_connected_to_pathfinder") | Boolean |  |  |  | PREVIEW: This key is currently not supported<br><br>For a WAN interface (`wan_path_group` is set), allow to disable the static tunnel towards Pathfinders.<br>Default True. |

=== "YAML"

    ```yaml
    core_interfaces:
      l3_interfaces_profiles:

          # L3 interface profile name. Any variable supported under `l3_interfaces` can be inherited from a profile.
        - profile: <str; required; unique>

          # PREVIEW: This key is currently not supported

          # The WAN path-group this interface is connected to.
          wan_path_group: <str>

          # PREVIEW: This key is currently not supported

          # The WAN Carrier this interface is connected to.
          # This is not rendered in the configuration but used for WAN designs.
          wan_carrier: <str>

          # PREVIEW: This key is currently not supported

          # The WAN Circuit ID for this interface.
          # This is not rendered in the configuration but used for WAN designs.
          wan_circuit_id: <str>

          # PREVIEW: This key is currently not supported

          # For a WAN interface (`wan_path_group` is set), allow to disable the static tunnel towards Pathfinders.
          # Default True.
          cv_pathfinder_connected_to_pathfinder: <bool>
      l3_interfaces:

          # PREVIEW: This key is currently not supported

          # The WAN path-group this interface is connected to.
          wan_path_group: <str>

          # PREVIEW: This key is currently not supported

          # The WAN Carrier this interface is connected to.
          # This is not rendered in the configuration but used for WAN designs.
          wan_carrier: <str>

          # PREVIEW: This key is currently not supported

          # The WAN Circuit ID for this interface.
          # This is not rendered in the configuration but used for WAN designs.
          wan_circuit_id: <str>

          # PREVIEW: This key is currently not supported

          # For a WAN interface (`wan_path_group` is set), allow to disable the static tunnel towards Pathfinders.
          # Default True.
          cv_pathfinder_connected_to_pathfinder: <bool>
    l3_edge:
      l3_interfaces_profiles:

          # L3 interface profile name. Any variable supported under `l3_interfaces` can be inherited from a profile.
        - profile: <str; required; unique>

          # PREVIEW: This key is currently not supported

          # The WAN path-group this interface is connected to.
          wan_path_group: <str>

          # PREVIEW: This key is currently not supported

          # The WAN Carrier this interface is connected to.
          # This is not rendered in the configuration but used for WAN designs.
          wan_carrier: <str>

          # PREVIEW: This key is currently not supported

          # The WAN Circuit ID for this interface.
          # This is not rendered in the configuration but used for WAN designs.
          wan_circuit_id: <str>

          # PREVIEW: This key is currently not supported

          # For a WAN interface (`wan_path_group` is set), allow to disable the static tunnel towards Pathfinders.
          # Default True.
          cv_pathfinder_connected_to_pathfinder: <bool>
      l3_interfaces:

          # PREVIEW: This key is currently not supported

          # The WAN path-group this interface is connected to.
          wan_path_group: <str>

          # PREVIEW: This key is currently not supported

          # The WAN Carrier this interface is connected to.
          # This is not rendered in the configuration but used for WAN designs.
          wan_carrier: <str>

          # PREVIEW: This key is currently not supported

          # The WAN Circuit ID for this interface.
          # This is not rendered in the configuration but used for WAN designs.
          wan_circuit_id: <str>

          # PREVIEW: This key is currently not supported

          # For a WAN interface (`wan_path_group` is set), allow to disable the static tunnel towards Pathfinders.
          # Default True.
          cv_pathfinder_connected_to_pathfinder: <bool>
    ```
