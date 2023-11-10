<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>avd_data_conversion_mode</samp>](## "avd_data_conversion_mode") | String |  | `debug` | Valid Values:<br>- <code>disabled</code><br>- <code>error</code><br>- <code>warning</code><br>- <code>info</code><br>- <code>debug</code><br>- <code>quiet</code> | Conversion Mode for AVD input data conversion.<br>Input data conversion will perform type conversion of input variables as defined in the schema.<br>The type conversion is intended to help the user to identify minor issues with the input data, while still allowing the data to be validated.<br>During conversion, messages will generated with information about the host(s) and key(s) which required conversion.<br>"disabled" means that conversion will not run - avoid this since conversion is also handling data deprecation and upgrade.<br>"error" will produce error messages and fail the task.<br>"warning" will produce warning messages.<br>"info" will produce regular log messages.<br>"debug" will produce hidden debug messages viewable with -v.<br>"quiet" will not produce any messages |
    | [<samp>avd_data_validation_mode</samp>](## "avd_data_validation_mode") | String |  | `warning` | Valid Values:<br>- <code>disabled</code><br>- <code>error</code><br>- <code>warning</code><br>- <code>info</code><br>- <code>debug</code> | Validation Mode for AVD input data validation.<br>Input data validation will validate the input variables according to the schema.<br>During validation, messages will generated with information about the host(s) and key(s) which failed validation.<br>"disabled" means that validation will not run.<br>"error" will produce error messages and fail the task.<br>"warning" will produce warning messages.<br>"info" will produce regular log messages.<br>"debug" will produce hidden debug messages viewable with -v. |

=== "YAML"

    ```yaml
    # Conversion Mode for AVD input data conversion.
    # Input data conversion will perform type conversion of input variables as defined in the schema.
    # The type conversion is intended to help the user to identify minor issues with the input data, while still allowing the data to be validated.
    # During conversion, messages will generated with information about the host(s) and key(s) which required conversion.
    # "disabled" means that conversion will not run - avoid this since conversion is also handling data deprecation and upgrade.
    # "error" will produce error messages and fail the task.
    # "warning" will produce warning messages.
    # "info" will produce regular log messages.
    # "debug" will produce hidden debug messages viewable with -v.
    # "quiet" will not produce any messages
    avd_data_conversion_mode: <str; "disabled" | "error" | "warning" | "info" | "debug" | "quiet"; default="debug">

    # Validation Mode for AVD input data validation.
    # Input data validation will validate the input variables according to the schema.
    # During validation, messages will generated with information about the host(s) and key(s) which failed validation.
    # "disabled" means that validation will not run.
    # "error" will produce error messages and fail the task.
    # "warning" will produce warning messages.
    # "info" will produce regular log messages.
    # "debug" will produce hidden debug messages viewable with -v.
    avd_data_validation_mode: <str; "disabled" | "error" | "warning" | "info" | "debug"; default="warning">
    ```
