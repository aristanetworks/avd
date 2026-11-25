<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>avd_data_validation_mode</samp>](## "avd_data_validation_mode") <span style="color:red">removed</span> | String |  | `error` | Valid Values:<br>- <code>error</code><br>- <code>warning</code> | Validation Mode for AVD input data validation.<br>Input data validation will validate the input variables according to the schema.<br>During validation, messages will generated with information about the host(s) and key(s) which failed validation.<br>"error" will produce error messages and fail the task.<br>"warning" will produce warning messages.<br><span style="color:red">This key was removed. Support was removed in AVD version 6.0.0.</span> |

=== "YAML"

    ```yaml

    ```
