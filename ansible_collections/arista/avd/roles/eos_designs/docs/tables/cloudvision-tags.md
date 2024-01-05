<!--
  ~ Copyright (c) 2023-2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>cv_tags_enabled</samp>](## "cv_tags_enabled") | Boolean |  | `False` |  | Enable the generation of CloudVision tags that can be applied using the `cloudvision` role. If not defined, the value is assumed to be False and no tags are generated.<br> |
    | [<samp>cv_tags_topology_type</samp>](## "cv_tags_topology_type") | String |  |  | Valid Values:<br>- <code>leaf</code><br>- <code>spine</code><br>- <code>core</code><br>- <code>edge</code> | Device type that CloudVision should use when generating the Topology.<br> |
    | [<samp>cv_tags_generate_interface</samp>](## "cv_tags_generate_interface") | List, items: Dictionary |  |  |  | List of interface tags that should be generated from<br>structured configuration.<br> |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "cv_tags_generate_interface.[].name") | String | Required |  | Value is converted to lower case. | Tag name to be assigned to generated tags.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;data_path</samp>](## "cv_tags_generate_interface.[].data_path") | String | Required |  |  | Structured config field/key path to be used to find the value for the tag. Dot notation is supported to reference values inside dictionaries.<br>For Example: 'data_path: channel_group.id' would set the tag with the value of the channel id of the interface. If there is no channel id, the tag is not created.<br> |
    | [<samp>cv_tags_generate_device</samp>](## "cv_tags_generate_device") | List, items: Dictionary |  |  |  | List of device tags that should be generated from<br>structured configuration.<br> |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "cv_tags_generate_device.[].name") | String | Required |  | Value is converted to lower case. | Tag name to be assigned to generated tags.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;data_path</samp>](## "cv_tags_generate_device.[].data_path") | String | Required |  |  | Structured config field/key path to be used to find the value for the tag. Dot notation is supported to reference values inside dictionaries.<br>For Example: 'data_path: router_bfd.multihop.interval' would set the tag with the value of the interval for multihop bfd. If this value is not specified in the structured config, the tag is not created.<br> |
    | [<samp>cv_tags_device_custom</samp>](## "cv_tags_device_custom") | List, items: Dictionary |  |  |  | List of user defined tags and their values to be applied to this<br>device on CVP.<br> |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "cv_tags_device_custom.[].name") | String | Required |  | Value is converted to lower case. | Tag name to be assigned to generated tag.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;value</samp>](## "cv_tags_device_custom.[].value") | String | Required |  |  | Value to be assigned to the tag.<br> |

=== "YAML"

    ```yaml
    # Enable the generation of CloudVision tags that can be applied using the `cloudvision` role. If not defined, the value is assumed to be False and no tags are generated.
    cv_tags_enabled: <bool; default=False>

    # Device type that CloudVision should use when generating the Topology.
    cv_tags_topology_type: <str; "leaf" | "spine" | "core" | "edge">

    # List of interface tags that should be generated from
    # structured configuration.
    cv_tags_generate_interface:

        # Tag name to be assigned to generated tags.
      - name: <str; required>

        # Structured config field/key path to be used to find the value for the tag. Dot notation is supported to reference values inside dictionaries.
        # For Example: 'data_path: channel_group.id' would set the tag with the value of the channel id of the interface. If there is no channel id, the tag is not created.
        data_path: <str; required>

    # List of device tags that should be generated from
    # structured configuration.
    cv_tags_generate_device:

        # Tag name to be assigned to generated tags.
      - name: <str; required>

        # Structured config field/key path to be used to find the value for the tag. Dot notation is supported to reference values inside dictionaries.
        # For Example: 'data_path: router_bfd.multihop.interval' would set the tag with the value of the interval for multihop bfd. If this value is not specified in the structured config, the tag is not created.
        data_path: <str; required>

    # List of user defined tags and their values to be applied to this
    # device on CVP.
    cv_tags_device_custom:

        # Tag name to be assigned to generated tag.
      - name: <str; required>

        # Value to be assigned to the tag.
        value: <str; required>
    ```
