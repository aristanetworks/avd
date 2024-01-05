<!--
  ~ Copyright (c) 2023-2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>cv_tags</samp>](## "cv_tags") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;device_tags</samp>](## "cv_tags.device_tags") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "cv_tags.device_tags.[].name") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;value</samp>](## "cv_tags.device_tags.[].value") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;interface_tags</samp>](## "cv_tags.interface_tags") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;interface</samp>](## "cv_tags.interface_tags.[].interface") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tags</samp>](## "cv_tags.interface_tags.[].tags") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "cv_tags.interface_tags.[].tags.[].name") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;value</samp>](## "cv_tags.interface_tags.[].tags.[].value") | String | Required |  |  |  |

=== "YAML"

    ```yaml
    cv_tags:
      device_tags:
        - name: <str; required>
          value: <str; required>
      interface_tags:
        - interface: <str; required>
          tags:
            - name: <str; required>
              value: <str; required>
    ```
