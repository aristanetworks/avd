=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>cloudvision_tags_device_custom</samp>](## "cloudvision_tags_device_custom") | List, items: Dictionary |  |  |  | List of user defined tags and their values to be applied to this<br>device on CVP.<br> |
    | [<samp>&nbsp;&nbsp;- label</samp>](## "cloudvision_tags_device_custom.[].label") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;value</samp>](## "cloudvision_tags_device_custom.[].value") | String | Required |  |  |  |

=== "YAML"

    ```yaml
    cloudvision_tags_device_custom:
      - label: <str>
        value: <str>
    ```
