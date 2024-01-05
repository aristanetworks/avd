<!--
  ~ Copyright (c) 2023-2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>metadata</samp>](## "metadata") | Dictionary |  |  |  | The data under `metadata` is used for documentation, validation or integration purposes.<br>It will not affect the generated EOS configuration. |
    | [<samp>&nbsp;&nbsp;platform</samp>](## "metadata.platform") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;cv_tags</samp>](## "metadata.cv_tags") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;device_tags</samp>](## "metadata.cv_tags.device_tags") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "metadata.cv_tags.device_tags.[].name") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;value</samp>](## "metadata.cv_tags.device_tags.[].value") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;interface_tags</samp>](## "metadata.cv_tags.interface_tags") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;interface</samp>](## "metadata.cv_tags.interface_tags.[].interface") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tags</samp>](## "metadata.cv_tags.interface_tags.[].tags") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "metadata.cv_tags.interface_tags.[].tags.[].name") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;value</samp>](## "metadata.cv_tags.interface_tags.[].tags.[].value") | String | Required |  |  |  |

=== "YAML"

    ```yaml
    # The data under `metadata` is used for documentation, validation or integration purposes.
    # It will not affect the generated EOS configuration.
    metadata:
      platform: <str>
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
