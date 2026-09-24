<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>environment_fan_speed</samp>](## "environment_fan_speed") | Dictionary |  |  |  | Environment fan-speed settings. |
    | [<samp>&nbsp;&nbsp;minimum</samp>](## "environment_fan_speed.minimum") | Integer |  |  | Min: 30<br>Max: 100 | Set the minimum fan speed in percent. |

=== "YAML"

    ```yaml
    # Environment fan-speed settings.
    environment_fan_speed:

      # Set the minimum fan speed in percent.
      minimum: <int; 30-100>
    ```
