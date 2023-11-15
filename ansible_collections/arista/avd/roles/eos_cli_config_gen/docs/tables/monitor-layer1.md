<!--
  ~ Copyright (c) 2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>monitor_layer1</samp>](## "monitor_layer1") | Dictionary |  |  |  | Enable SYSLOG messages on transceiver SMBus communication failures |
    | [<samp>&nbsp;&nbsp;logging_mac_fault</samp>](## "monitor_layer1.logging_mac_fault") | Boolean |  |  |  | Enable mac fault loggin. |
    | [<samp>&nbsp;&nbsp;logging_transceiver</samp>](## "monitor_layer1.logging_transceiver") | Dictionary |  |  |  | Configure transceiver monitoring logging. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enable</samp>](## "monitor_layer1.logging_transceiver.enable") | Boolean | Required |  |  | Enable transcieve monitoring logging. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;dom</samp>](## "monitor_layer1.logging_transceiver.dom") | Boolean |  |  |  | Enable transceiver digital optical monitoring (DOM) logging. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;communication</samp>](## "monitor_layer1.logging_transceiver.communication") | Boolean |  |  |  | Enable transceiver SMBus fail and reset logging. |

=== "YAML"

    ```yaml
    # Enable SYSLOG messages on transceiver SMBus communication failures
    monitor_layer1:

      # Enable mac fault loggin.
      logging_mac_fault: <bool>

      # Configure transceiver monitoring logging.
      logging_transceiver:

        # Enable transcieve monitoring logging.
        enable: <bool; required>

        # Enable transceiver digital optical monitoring (DOM) logging.
        dom: <bool>

        # Enable transceiver SMBus fail and reset logging.
        communication: <bool>
    ```
