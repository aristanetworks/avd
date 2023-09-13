<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>eos_cli_config_gen_configuration</samp>](## "eos_cli_config_gen_configuration") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;hide_passwords</samp>](## "eos_cli_config_gen_configuration.hide_passwords") | Boolean |  | `False` |  | Replace the input data using the `hide_passwords` filter in the Jinja2 templates by '<removed>' in the configruation if true<br> |

=== "YAML"

    ```yaml
    eos_cli_config_gen_configuration:

      # Replace the input data using the `hide_passwords` filter in the Jinja2 templates by '<removed>' in the configruation if true
      hide_passwords: <bool; default=False>
    ```
