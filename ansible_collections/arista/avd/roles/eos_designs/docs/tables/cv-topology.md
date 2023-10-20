<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>cv_topology</samp>](## "cv_topology") | List, items: Dictionary |  |  |  | Generate AVD configurations directly from the given CloudVision topology.<br>Activate this feature by setting `use_cv_topology` to `true`.<br>Requires `default_interfaces` to be set for the relevant platforms and node types to detect the proper interface roles automatically.<br>Neighbor hostnames must match the inventory hostnames of the AVD inventory to be taken into consideration. |
    | [<samp>&nbsp;&nbsp;- hostname</samp>](## "cv_topology.[].hostname") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;platform</samp>](## "cv_topology.[].platform") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;interfaces</samp>](## "cv_topology.[].interfaces") | List, items: Dictionary | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "cv_topology.[].interfaces.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;neighbor</samp>](## "cv_topology.[].interfaces.[].neighbor") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;neighbor_interface</samp>](## "cv_topology.[].interfaces.[].neighbor_interface") | String |  |  |  |  |
    | [<samp>use_cv_topology</samp>](## "use_cv_topology") | Boolean |  |  |  | Generate AVD configurations directly from a given CloudVision topology.<br>See `cv_topology` for details. |

=== "YAML"

    ```yaml
    cv_topology:
      - hostname: <str>
        platform: <str>
        interfaces:
          - name: <str>
            neighbor: <str>
            neighbor_interface: <str>
    use_cv_topology: <bool>
    ```
