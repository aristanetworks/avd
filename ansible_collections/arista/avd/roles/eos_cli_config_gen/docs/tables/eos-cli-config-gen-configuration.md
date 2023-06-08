=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>eos_cli_config_gen_configuration</samp>](## "eos_cli_config_gen_configuration") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;hide_passwords</samp>](## "eos_cli_config_gen_configuration.hide_passwords") | Boolean |  | `False` |  | Replace the input data using the `hide_passwords` filter in the Jinja2 templates by '<removed>' in the configruation if true<br> |

=== "YAML"

    ```yaml
    eos_cli_config_gen_configuration:
      hide_passwords: <bool>
    ```
