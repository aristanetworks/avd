=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>cloudvision_tags_interface_generate</samp>](## "cloudvision_tags_interface_generate") | List, items: Dictionary |  |  |  | List of device tags that should be generated from<br>structured configuration.<br> |
    | [<samp>&nbsp;&nbsp;- name</samp>](## "cloudvision_tags_interface_generate.[].name") | String | Required |  |  | Tag name to be assigned to generated tags.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;field</samp>](## "cloudvision_tags_interface_generate.[].field") | String | Required |  |  | Sturctured config field/key to be used to find the value for the tag.<br> |

=== "YAML"

    ```yaml
    cloudvision_tags_interface_generate:
      - name: <str>
        field: <str>
    ```
