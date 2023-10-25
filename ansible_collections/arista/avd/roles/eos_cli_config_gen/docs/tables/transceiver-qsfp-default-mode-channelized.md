<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>transceiver_qsfp_default_mode_channelized</samp>](## "transceiver_qsfp_default_mode_channelized") | Boolean |  |  |  | The `transceiver_qsfp_default_mode_channelized` knob allows to set default qsfp mode to 40G when set to `false`.<br>If not defined, it defaults to the value of `generate_default_config` |

=== "YAML"

    ```yaml
    transceiver_qsfp_default_mode_channelized: <bool>
    ```
