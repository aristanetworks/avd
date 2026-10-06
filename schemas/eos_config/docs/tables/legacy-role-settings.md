<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>custom_templates</samp>](## "custom_templates") | List, items: String |  |  |  | Legacy alias for `eos_cli_config_gen_custom_templates`. |
    | [<samp>&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "custom_templates.[]") | String |  |  |  |  |
    | [<samp>read_structured_config_from_file</samp>](## "read_structured_config_from_file") | Boolean |  |  |  | Legacy alias for `eos_cli_config_gen_read_structured_config_from_file`.<br> |

=== "YAML"

    ```yaml
    # Legacy alias for `eos_cli_config_gen_custom_templates`.
    custom_templates:
      - <str>

    # Legacy alias for `eos_cli_config_gen_read_structured_config_from_file`.
    read_structured_config_from_file: <bool>
    ```
