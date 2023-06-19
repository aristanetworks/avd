=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>cloudvision_tags_topology_type</samp>](## "cloudvision_tags_topology_type") | String |  |  | Valid Values:<br>- leaf<br>- spine<br>- core<br>- edge | Device type that CloudVision should use when generating the Topology.<br> |
    | [<samp>cloudvision_tags_interface_generate</samp>](## "cloudvision_tags_interface_generate") | List, items: Dictionary |  |  |  | List of device tags that should be generated from<br>structured configuration.<br> |
    | [<samp>&nbsp;&nbsp;- name</samp>](## "cloudvision_tags_interface_generate.[].name") | String | Required |  | Value is converted to lower case | Tag name to be assigned to generated tags.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;field</samp>](## "cloudvision_tags_interface_generate.[].field") | String | Required |  |  | Sturctured config field/key to be used to find the value for the tag.<br> |
    | [<samp>cloudvision_tags_device_generate</samp>](## "cloudvision_tags_device_generate") | List, items: Dictionary |  |  |  | List of device tags that should be generated from<br>structured configuration.<br> |
    | [<samp>&nbsp;&nbsp;- name</samp>](## "cloudvision_tags_device_generate.[].name") | String | Required |  | Value is converted to lower case | Tag name to be assigned to generated tags.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;field</samp>](## "cloudvision_tags_device_generate.[].field") | String | Required |  |  | Sturctured config field/key to be used to find the value for the tag.<br> |
    | [<samp>cloudvision_tags_device_custom</samp>](## "cloudvision_tags_device_custom") | List, items: Dictionary |  |  |  | List of user defined tags and their values to be applied to this<br>device on CVP.<br> |
    | [<samp>&nbsp;&nbsp;- name</samp>](## "cloudvision_tags_device_custom.[].name") | String | Required |  | Value is converted to lower case | Tag name to be assigned to generated tag.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;value</samp>](## "cloudvision_tags_device_custom.[].value") | String | Required |  |  | Value to be assigned to the tag.<br> |

=== "YAML"

    ```yaml
    cloudvision_tags_topology_type: <str>
    cloudvision_tags_interface_generate:
      - name: <str>
        field: <str>
    cloudvision_tags_device_generate:
      - name: <str>
        field: <str>
    cloudvision_tags_device_custom:
      - name: <str>
        value: <str>
    ```
