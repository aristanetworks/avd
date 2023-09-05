<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>queue_monitor_length</samp>](## "queue_monitor_length") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;enabled</samp>](## "queue_monitor_length.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;default_thresholds</samp>](## "queue_monitor_length.default_thresholds") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;high</samp>](## "queue_monitor_length.default_thresholds.high") | Integer | Required |  |  | Default high threshold for Ethernet Interfaces.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;low</samp>](## "queue_monitor_length.default_thresholds.low") | Integer |  |  |  | Default low threshold for Ethernet Interfaces.<br>Low threshold support is platform dependent.<br> |
    | [<samp>&nbsp;&nbsp;log</samp>](## "queue_monitor_length.log") | Integer |  |  |  | Logging interval in seconds |
    | [<samp>&nbsp;&nbsp;notifying</samp>](## "queue_monitor_length.notifying") | Boolean |  |  |  | Should only be used for platforms supporting the "queue-monitor length notifying" CLI |
    | [<samp>&nbsp;&nbsp;cpu</samp>](## "queue_monitor_length.cpu") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;thresholds</samp>](## "queue_monitor_length.cpu.thresholds") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;high</samp>](## "queue_monitor_length.cpu.thresholds.high") | Integer | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;low</samp>](## "queue_monitor_length.cpu.thresholds.low") | Integer |  |  |  |  |

=== "YAML"

    ```yaml
    queue_monitor_length:
      enabled: <bool>
      default_thresholds:
        high: <int>
        low: <int>
      log: <int>
      notifying: <bool>
      cpu:
        thresholds:
          high: <int>
          low: <int>
    ```
