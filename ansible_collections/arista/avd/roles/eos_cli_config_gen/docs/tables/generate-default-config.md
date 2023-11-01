<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>generate_default_config</samp>](## "generate_default_config") | Boolean |  | `True` |  | The `generate_default_config` knob allows to omit default EOS configuration.<br>This can be useful when leveraging `eos_cli_config_gen` to generate configlets with CloudVision.<br><br>The following commands will be omitted when `generate_default_config` is set to `false`:<br><br>- RANCID Content Type<br>- Hostname<br>- Default configuration for `aaa`<br>- Default configuration for `enable password`<br>- Transceiver qsfp default mode<br>- End of configuration delimiter |

=== "YAML"

    ```yaml
    # The `generate_default_config` knob allows to omit default EOS configuration.
    # This can be useful when leveraging `eos_cli_config_gen` to generate configlets with CloudVision.

    # The following commands will be omitted when `generate_default_config` is set to `false`:

    # - RANCID Content Type
    # - Hostname
    # - Default configuration for `aaa`
    # - Default configuration for `enable password`
    # - Transceiver qsfp default mode
    # - End of configuration delimiter
    generate_default_config: <bool; default=True>
    ```
