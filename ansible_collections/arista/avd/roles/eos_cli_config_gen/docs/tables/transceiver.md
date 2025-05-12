<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>transceiver</samp>](## "transceiver") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;dom_threshold</samp>](## "transceiver.dom_threshold") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;default</samp>](## "transceiver.dom_threshold.default") | Boolean |  |  |  | Set default Arista-standardized thresholds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;file</samp>](## "transceiver.dom_threshold.file") | String |  |  |  | Set Optics transceiver DOM thresholds with values from specified file.<br>eg. `dom_threshold_file: flash:/Fossil/`<br> |

=== "YAML"

    ```yaml
    transceiver:
      dom_threshold:

        # Set default Arista-standardized thresholds.
        default: <bool>

        # Set Optics transceiver DOM thresholds with values from specified file.
        # eg. `dom_threshold_file: flash:/Fossil/`
        file: <str>
    ```
