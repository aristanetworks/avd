<!--
  ~ Copyright (c) 2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>internet_exit_policies</samp>](## "internet_exit_policies") | List, items: Dictionary |  |  |  | PREVIEW: These keys are in preview mode.<br><br>List of path-groups used for the WAN configuration. |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "internet_exit_policies.[].name") | String | Required, Unique |  |  | Internet-exit policy name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "internet_exit_policies.[].type") | String | Required |  | Valid Values:<br>- <code>zscaler</code> | Internet-exit policy type.<br>Only Zscaler supported. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;fallback_to_system_default</samp>](## "internet_exit_policies.[].fallback_to_system_default") | Boolean |  | `True` |  | Add system default exit-group at the end of the policy. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;zscaler</samp>](## "internet_exit_policies.[].zscaler") | Dictionary |  |  |  | Zscaler information. Only used if `type` is 'zscaler'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cloud_name</samp>](## "internet_exit_policies.[].zscaler.cloud_name") | String |  | `zscaler` |  | Zscaler Cloud |

=== "YAML"

    ```yaml
    # PREVIEW: These keys are in preview mode.
    #
    # List of path-groups used for the WAN configuration.
    internet_exit_policies:

        # Internet-exit policy name.
      - name: <str; required; unique>

        # Internet-exit policy type.
        # Only Zscaler supported.
        type: <str; "zscaler"; required>

        # Add system default exit-group at the end of the policy.
        fallback_to_system_default: <bool; default=True>

        # Zscaler information. Only used if `type` is 'zscaler'.
        zscaler:

          # Zscaler Cloud
          cloud_name: <str; default="zscaler">
    ```
