<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>monitor_layer1</samp>](## "monitor_layer1") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;logging_mac_faults</samp>](## "monitor_layer1.logging_mac_faults") | Boolean |  |  |  |   |
    | [<samp>&nbsp;&nbsp;logging_transciever</samp>](## "monitor_layer1.logging_transciever") | Dictionary |  |  |  |   |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enable</samp>](## "monitor_layer1.logging_transciever.enable") | Boolean | Required |  |  |   |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;dom</samp>](## "monitor_layer1.logging_transciever.dom") | Boolean |  |  |  |   |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;communication</samp>](## "monitor_layer1.logging_transciever.communication") | Boolean |  |  |  |   |

=== "YAML"

    ```yaml
    monitor_layer1:


      logging_mac_faults: <bool>


      logging_transciever:


        enable: <bool; required>


        dom: <bool>


        communication: <bool>
    ```
