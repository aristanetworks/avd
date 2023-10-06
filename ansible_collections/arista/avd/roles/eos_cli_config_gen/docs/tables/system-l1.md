<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>system_l1</samp>](## "system_l1") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;unsupported_speed_action</samp>](## "system_l1.unsupported_speed_action") | String |  |  | Valid Values:<br>- error<br>- warn |  |
    | [<samp>&nbsp;&nbsp;unsupported_error_correction_action</samp>](## "system_l1.unsupported_error_correction_action") | String |  |  | Valid Values:<br>- error<br>- warn |  |

=== "YAML"

    ```yaml
    system_l1:
      unsupported_speed_action: <str>
      unsupported_error_correction_action: <str>
    ```
