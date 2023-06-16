=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>cloudvision_tags_device_generate</samp>](## "cloudvision_tags_device_generate") | List, items: Dictionary |  |  |  | List of device tags that should be generated from<br>structured configuration.<br> |
    | [<samp>&nbsp;&nbsp;- label</samp>](## "cloudvision_tags_device_generate.[].label") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;field</samp>](## "cloudvision_tags_device_generate.[].field") | String | Required |  |  |  |

=== "YAML"

    ```yaml
    cloudvision_tags_device_generate:
      - label: <str>
        field: <str>
    ```
