=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>cloudvision_tags</samp>](## "cloudvision_tags") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;device_tags</samp>](## "cloudvision_tags.device_tags") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "cloudvision_tags.device_tags.[].name") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;value</samp>](## "cloudvision_tags.device_tags.[].value") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;interface_tags</samp>](## "cloudvision_tags.interface_tags") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- interface</samp>](## "cloudvision_tags.interface_tags.[].interface") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tags</samp>](## "cloudvision_tags.interface_tags.[].tags") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "cloudvision_tags.interface_tags.[].tags.[].name") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;value</samp>](## "cloudvision_tags.interface_tags.[].tags.[].value") | String | Required |  |  |  |

=== "YAML"

    ```yaml
    cloudvision_tags:
      device_tags:
        - name: <str>
          value: <str>
      interface_tags:
        - interface: <str>
          tags:
            - name: <str>
              value: <str>
    ```
