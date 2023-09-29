=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>cv_tags_enabled</samp>](## "cv_tags_enabled") | Boolean |  | `False` |  | Enable the generation of CloudVision tags that can be applied using the `cloudvision` role. If not defined, the value is assumed to be False and no tags are generated.<br> |
    | [<samp>cv_tags_topology_type</samp>](## "cv_tags_topology_type") | String |  |  | Valid Values:<br>- leaf<br>- spine<br>- core<br>- edge | Device type that CloudVision should use when generating the Topology.<br> |
    | [<samp>cv_tags_generate_interface</samp>](## "cv_tags_generate_interface") | List, items: Dictionary |  |  |  | List of interface tags that should be generated from<br>structured configuration.<br> |
    | [<samp>&nbsp;&nbsp;- name</samp>](## "cv_tags_generate_interface.[].name") | String | Required |  | Value is converted to lower case | Tag name to be assigned to generated tags.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;field</samp>](## "cv_tags_generate_interface.[].field") | String | Required |  |  | Sturctured config field/key path to be used to find the value for the tag. Dot notation is supported to reference values inside dictionaries.<br> |
    | [<samp>cv_tags_generate_device</samp>](## "cv_tags_generate_device") | List, items: Dictionary |  |  |  | List of device tags that should be generated from<br>structured configuration.<br> |
    | [<samp>&nbsp;&nbsp;- name</samp>](## "cv_tags_generate_device.[].name") | String | Required |  | Value is converted to lower case | Tag name to be assigned to generated tags.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;field</samp>](## "cv_tags_generate_device.[].field") | String | Required |  |  | Sturctured config field/key path to be used to find the value for the tag. Dot notation is supported to reference values inside dictionaries.<br> |
    | [<samp>cv_tags_device_custom</samp>](## "cv_tags_device_custom") | List, items: Dictionary |  |  |  | List of user defined tags and their values to be applied to this<br>device on CVP.<br> |
    | [<samp>&nbsp;&nbsp;- name</samp>](## "cv_tags_device_custom.[].name") | String | Required |  | Value is converted to lower case | Tag name to be assigned to generated tag.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;value</samp>](## "cv_tags_device_custom.[].value") | String | Required |  |  | Value to be assigned to the tag.<br> |

=== "YAML"

    ```yaml
    cv_tags_enabled: <bool>
    cv_tags_topology_type: <str>
    cv_tags_generate_interface:
      - name: <str>
        field: <str>
    cv_tags_generate_device:
      - name: <str>
        field: <str>
    cv_tags_device_custom:
      - name: <str>
        value: <str>
    ```
