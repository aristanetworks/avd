<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>wan_carriers</samp>](## "wan_carriers") | List, items: Dictionary |  |  |  | PREVIEW: This key is currently not supported<br><br>List of carriers used for the WAN configuration and their mapping to path-groups. |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "wan_carriers.[].name") | String | Required, Unique |  |  | Carrier name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "wan_carriers.[].description") | String |  |  |  | Additional information about the carrier for documentation purposes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;path_group</samp>](## "wan_carriers.[].path_group") | String | Required |  |  | The path-group to which this carrier belongs. |

=== "YAML"

    ```yaml
    # PREVIEW: This key is currently not supported

    # List of carriers used for the WAN configuration and their mapping to path-groups.
    wan_carriers:

        # Carrier name.
      - name: <str; required; unique>

        # Additional information about the carrier for documentation purposes.
        description: <str>

        # The path-group to which this carrier belongs.
        path_group: <str; required>
    ```
