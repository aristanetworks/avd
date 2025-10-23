<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>cv_topology</samp>](## "cv_topology") | List, items: Dictionary |  |  |  | Generate AVD configurations directly from the given CloudVision topology.<br>Activate this feature by setting `use_cv_topology` to `true`.<br>Interfaces are assigned according to the following rules:<br>  - All interfaces connected to the MLAG peer (only other device in the same node group) will be `mlag_interfaces`.<br>  - For connections between devices with different `cv_topology_levels[type=<type>].level`, the lowest level will be considered the "parent switch"<br>    and the highest level will be considered the "child switch".<br>  - Connections between devices with the same `cv_topology_levels[type=<type>].level` will be ignored and must be created manually.<br>  - The first Management interface is assigned as `mgmt_interface` unless it is set for the node or under platform_settings.<br>Neighbor hostnames must match the inventory hostnames of the AVD inventory to be taken into consideration. |
    | [<samp>&nbsp;&nbsp;-&nbsp;hostname</samp>](## "cv_topology.[].hostname") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;platform</samp>](## "cv_topology.[].platform") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;interfaces</samp>](## "cv_topology.[].interfaces") | List, items: Dictionary | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "cv_topology.[].interfaces.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;neighbor</samp>](## "cv_topology.[].interfaces.[].neighbor") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;neighbor_interface</samp>](## "cv_topology.[].interfaces.[].neighbor_interface") | String |  |  |  |  |
    | [<samp>cv_topology_levels</samp>](## "cv_topology_levels") | List, items: Dictionary |  |  |  | Type to level assignment used for generation of the AVD topology from the CloudVision topology.<br>See `cv_topology` for details. |
    | [<samp>&nbsp;&nbsp;-&nbsp;type</samp>](## "cv_topology_levels.[].type") | String | Required, Unique |  |  | Node type like l3leaf, l2spine etc. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;level</samp>](## "cv_topology_levels.[].level") | Integer | Required |  |  | Level value used to determine the relationship between two devices for a connection.<br>The lower value is the "parent switch" (like Spine).<br>The higher value is the "child switch" (like Leaf). |
    | [<samp>use_cv_topology</samp>](## "use_cv_topology") | Boolean |  |  |  | Generate AVD configurations directly from a given CloudVision topology.<br>See `cv_topology` for details.<br>Requires both `cv_topology` and `cv_topology_levels` to be set. |

=== "YAML"

    ```yaml
    # Generate AVD configurations directly from the given CloudVision topology.
    # Activate this feature by setting `use_cv_topology` to `true`.
    # Interfaces are assigned according to the following rules:
    #   - All interfaces connected to the MLAG peer (only other device in the same node group) will be `mlag_interfaces`.
    #   - For connections between devices with different `cv_topology_levels[type=<type>].level`, the lowest level will be considered the "parent switch"
    #     and the highest level will be considered the "child switch".
    #   - Connections between devices with the same `cv_topology_levels[type=<type>].level` will be ignored and must be created manually.
    #   - The first Management interface is assigned as `mgmt_interface` unless it is set for the node or under platform_settings.
    # Neighbor hostnames must match the inventory hostnames of the AVD inventory to be taken into consideration.
    cv_topology:
      - hostname: <str; required; unique>
        platform: <str; required>
        interfaces: # required
          - name: <str; required; unique>
            neighbor: <str>
            neighbor_interface: <str>

    # Type to level assignment used for generation of the AVD topology from the CloudVision topology.
    # See `cv_topology` for details.
    cv_topology_levels:

        # Node type like l3leaf, l2spine etc.
      - type: <str; required; unique>

        # Level value used to determine the relationship between two devices for a connection.
        # The lower value is the "parent switch" (like Spine).
        # The higher value is the "child switch" (like Leaf).
        level: <int; required>

    # Generate AVD configurations directly from a given CloudVision topology.
    # See `cv_topology` for details.
    # Requires both `cv_topology` and `cv_topology_levels` to be set.
    use_cv_topology: <bool>
    ```
