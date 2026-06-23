<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>env</samp>](## "env") | Dictionary |  |  |  | System environment settings. |
    | [<samp>&nbsp;&nbsp;fan_speed</samp>](## "env.fan_speed") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;minimum</samp>](## "env.fan_speed.minimum") | Integer |  |  | Min: 30<br>Max: 100 | Set the minimum fan speed in percent. |

=== "YAML"

    ```yaml
    # System environment settings.
    env:
      fan_speed:

        # Set the minimum fan speed in percent.
        minimum: <int; 30-100>
    ```
