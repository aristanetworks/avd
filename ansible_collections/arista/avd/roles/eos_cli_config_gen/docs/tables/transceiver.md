<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>transceiver</samp>](## "transceiver") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;dom_threshold_file</samp>](## "transceiver.dom_threshold_file") | String |  |  |  | CSV file path for DOM threshold values.<br>eg. `dom_threshold_file: flash:/dom_threshold.csv`<br>Note: Set `dom_threshold_file` to `default` for default Arista-standardized thresholds.<br>eg. `dom_threshold_file: default` |

=== "YAML"

    ```yaml
    transceiver:

      # CSV file path for DOM threshold values.
      # eg. `dom_threshold_file: flash:/dom_threshold.csv`
      # Note: Set `dom_threshold_file` to `default` for default Arista-standardized thresholds.
      # eg. `dom_threshold_file: default`
      dom_threshold_file: <str>
    ```
