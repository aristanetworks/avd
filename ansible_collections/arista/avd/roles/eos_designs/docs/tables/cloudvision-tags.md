<!--
  ~ Copyright (c) 2023-2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>cv_tags_topology_type</samp>](## "cv_tags_topology_type") | String |  |  | Valid Values:<br>- <code>leaf</code><br>- <code>spine</code><br>- <code>core</code><br>- <code>edge</code> | Device type that CloudVision should use when generating the Topology. Defaults to the setting under node_type_keys. |
    | [<samp>generate_cv_tags</samp>](## "generate_cv_tags") | Dictionary |  |  |  | Generate CloudVision Tags based on AVD data. |
    | [<samp>&nbsp;&nbsp;topology_hints</samp>](## "generate_cv_tags.topology_hints") | Boolean |  | `False` |  | Enable the generation of CloudVision Topology Tags (hints). |
    | [<samp>&nbsp;&nbsp;interface_tags</samp>](## "generate_cv_tags.interface_tags") | List, items: Dictionary |  |  |  | List of interface tags that should be generated. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "generate_cv_tags.interface_tags.[].name") | String | Required, Unique |  | Value is converted to lower case. | Tag name to be assigned to generated tags. Tag names must be lower case. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;data_path</samp>](## "generate_cv_tags.interface_tags.[].data_path") | String |  |  |  | Structured config field/key path to be used to find the value for the tag. Dot notation is supported to reference values inside dictionaries.<br>For Example: 'data_path: channel_group.id' would set the tag with the value of the channel id of the interface. If there is no channel id, the tag is not created.<br>`data_path` is ignored if `value` is set. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;value</samp>](## "generate_cv_tags.interface_tags.[].value") | String |  |  |  | Value to be assigned to the tag. |
    | [<samp>&nbsp;&nbsp;device_tags</samp>](## "generate_cv_tags.device_tags") | List, items: Dictionary |  |  |  | List of device tags that should be generated. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "generate_cv_tags.device_tags.[].name") | String | Required |  | Value is converted to lower case. | Tag name to be assigned to generated tags. Tag names must be lower case. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;data_path</samp>](## "generate_cv_tags.device_tags.[].data_path") | String |  |  |  | Structured config field/key path to be used to find the value for the tag. Dot notation is supported to reference values inside dictionaries.<br>For Example: 'data_path: router_bfd.multihop.interval' would set the tag with the value of the interval for multihop bfd. If this value is not specified in the structured config, the tag is not created.<br>`data_path` is ignored if `value` is set. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;value</samp>](## "generate_cv_tags.device_tags.[].value") | String |  |  |  | Value to be assigned to the tag. |

=== "YAML"

    ```yaml
    # Device type that CloudVision should use when generating the Topology. Defaults to the setting under node_type_keys.
    cv_tags_topology_type: <str; "leaf" | "spine" | "core" | "edge">

    # Generate CloudVision Tags based on AVD data.
    generate_cv_tags:

      # Enable the generation of CloudVision Topology Tags (hints).
      topology_hints: <bool; default=False>

      # List of interface tags that should be generated.
      interface_tags:

          # Tag name to be assigned to generated tags. Tag names must be lower case.
        - name: <str; required; unique>

          # Structured config field/key path to be used to find the value for the tag. Dot notation is supported to reference values inside dictionaries.
          # For Example: 'data_path: channel_group.id' would set the tag with the value of the channel id of the interface. If there is no channel id, the tag is not created.
          # `data_path` is ignored if `value` is set.
          data_path: <str>

          # Value to be assigned to the tag.
          value: <str>

      # List of device tags that should be generated.
      device_tags:

          # Tag name to be assigned to generated tags. Tag names must be lower case.
        - name: <str; required>

          # Structured config field/key path to be used to find the value for the tag. Dot notation is supported to reference values inside dictionaries.
          # For Example: 'data_path: router_bfd.multihop.interval' would set the tag with the value of the interval for multihop bfd. If this value is not specified in the structured config, the tag is not created.
          # `data_path` is ignored if `value` is set.
          data_path: <str>

          # Value to be assigned to the tag.
          value: <str>
    ```
