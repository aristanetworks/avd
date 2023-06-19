=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>cloudvision_tags_device_custom</samp>](## "cloudvision_tags_device_custom") | List, items: Dictionary |  |  |  | List of user defined tags and their values to be applied to this<br>device on CVP.<br> |
    | [<samp>&nbsp;&nbsp;- name</samp>](## "cloudvision_tags_device_custom.[].name") | String | Required |  |  | Tag name to be assigned to generated tag.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;value</samp>](## "cloudvision_tags_device_custom.[].value") | String | Required |  |  | Value to be assigned to the tag.<br> |

=== "YAML"

    ```yaml
    cloudvision_tags_device_custom:
      - name: <str>
        value: <str>
    ```
