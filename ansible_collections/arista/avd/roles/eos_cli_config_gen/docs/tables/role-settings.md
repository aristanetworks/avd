<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>avd_eos_cli_config_gen_input_dir</samp>](## "avd_eos_cli_config_gen_input_dir") | String |  |  |  | Specify a directory containing structured configuration files to use as input.<br>Can be set to null or an empty string to force `eos_cli_config_gen` to use hostvars as input.<br>By default, this variable is set to "{{ structured_dir }}" which is the directory where `eos_designs` outputs structured configuration files.<br> |
    | [<samp>avd_eos_cli_config_gen_validate_inputs_batch_size</samp>](## "avd_eos_cli_config_gen_validate_inputs_batch_size") | Integer |  | `10` |  | The number of hosts to process in each batch when validating inputs.<br>Depending on your inventory size and the available resources, you may want to adjust this number. |
    | [<samp>avd_structured_config_file_format</samp>](## "avd_structured_config_file_format") | String |  | `yml` | Valid Values:<br>- <code>yml</code><br>- <code>yaml</code><br>- <code>json</code> | The file format to use when loading structured configuration files.<br> |
    | [<samp>eos_cli_config_gen_configuration</samp>](## "eos_cli_config_gen_configuration") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;enable</samp>](## "eos_cli_config_gen_configuration.enable") | Boolean |  | `True` |  | Generate device EOS configurations. |
    | [<samp>&nbsp;&nbsp;hide_passwords</samp>](## "eos_cli_config_gen_configuration.hide_passwords") | Boolean |  | `False` |  | Replace the input data using the `hide_passwords` filter in the Jinja2 templates by '<removed>' in the configuration if true.<br> |
    | [<samp>eos_cli_config_gen_documentation</samp>](## "eos_cli_config_gen_documentation") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;enable</samp>](## "eos_cli_config_gen_documentation.enable") | Boolean |  | `True` |  | Generate device Markdown documentation. |
    | [<samp>&nbsp;&nbsp;hide_passwords</samp>](## "eos_cli_config_gen_documentation.hide_passwords") | Boolean |  | `True` |  | Replace the input data using the `hide_passwords` filter in the Jinja2 templates by '<removed>' in the documentation if true.<br> |
    | [<samp>&nbsp;&nbsp;toc</samp>](## "eos_cli_config_gen_documentation.toc") | Boolean |  | `True` |  | Generate the table of content(TOC) on device documentation. |
    | [<samp>generate_default_config</samp>](## "generate_default_config") <span style="color:red">removed</span> | Boolean |  | `False` |  | <span style="color:red">This key was removed. Support was removed in AVD version 6.0.0. See [here](https://avd.arista.com/5.x/docs/porting-guides/5.x.x.html#default-eos-configuration-is-no-longer-automatically-generated) for details.</span> |
    | [<samp>generate_device_documentation</samp>](## "generate_device_documentation") <span style="color:red">removed</span> | Boolean |  | `True` |  | <span style="color:red">This key was removed. Support was removed in AVD version 6.0.0. Use <samp>eos_cli_config_gen_documentation.enable</samp> instead.</span> |

=== "YAML"

    ```yaml
    # Specify a directory containing structured configuration files to use as input.
    # Can be set to null or an empty string to force `eos_cli_config_gen` to use hostvars as input.
    # By default, this variable is set to "{{ structured_dir }}" which is the directory where `eos_designs` outputs structured configuration files.
    avd_eos_cli_config_gen_input_dir: <str>

    # The number of hosts to process in each batch when validating inputs.
    # Depending on your inventory size and the available resources, you may want to adjust this number.
    avd_eos_cli_config_gen_validate_inputs_batch_size: <int; default=10>

    # The file format to use when loading structured configuration files.
    avd_structured_config_file_format: <str; "yml" | "yaml" | "json"; default="yml">
    eos_cli_config_gen_configuration:

      # Generate device EOS configurations.
      enable: <bool; default=True>

      # Replace the input data using the `hide_passwords` filter in the Jinja2 templates by '<removed>' in the configuration if true.
      hide_passwords: <bool; default=False>
    eos_cli_config_gen_documentation:

      # Generate device Markdown documentation.
      enable: <bool; default=True>

      # Replace the input data using the `hide_passwords` filter in the Jinja2 templates by '<removed>' in the documentation if true.
      hide_passwords: <bool; default=True>

      # Generate the table of content(TOC) on device documentation.
      toc: <bool; default=True>
    ```
