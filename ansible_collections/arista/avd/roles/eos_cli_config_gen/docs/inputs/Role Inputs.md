---
search:
  boost: 2
---

# Role Inputs

## Extensibility with Custom Templates

- Custom templates can be added below the playbook directory.
- If a location above the directory is desired, a symbolic link can be used.
- Example under the `playbooks` directory create symbolic link with the following command:

  ```bash
  ln -s ../../shared_repo/custom_avd_templates/ ./custom_avd_templates
  ```

- The output will be rendered at the end of the configuration.
- The order of custom templates in the list can be important if they overlap.
- It is recommended to use a `!` delimiter at the top of each custom template.

Add `custom_templates` to group/host variables:

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>custom_templates</samp>](## "custom_templates") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- &lt;str&gt;</samp>](## "custom_templates.[].&lt;str&gt;") | String |  |  |  | Template relative path below playbook directory |

=== "YAML"

    ```yaml
    custom_templates:
      - <str>
    ```

## EOS CLI Config Gen Configuration

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>eos_cli_config_gen_configuration</samp>](## "eos_cli_config_gen_configuration") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;hide_passwords</samp>](## "eos_cli_config_gen_configuration.hide_passwords") | Boolean |  | False |  | Replace the input data using the `hide_passwords` filter in the Jinja2 templates by '<removed>' in the configruation if true<br> |

=== "YAML"

    ```yaml
    eos_cli_config_gen_configuration:
      hide_passwords: <bool>
    ```

## EOS CLI Config Gen Documentation

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>eos_cli_config_gen_documentation</samp>](## "eos_cli_config_gen_documentation") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;hide_passwords</samp>](## "eos_cli_config_gen_documentation.hide_passwords") | Boolean |  | True |  | Replace the input data using the `hide_passwords` filter in the Jinja2 templates by '<removed>' in the documentation if true<br> |

=== "YAML"

    ```yaml
    eos_cli_config_gen_documentation:
      hide_passwords: <bool>
    ```

## Generate Default Config

The `generate_default_config` knob allows to omit default EOS configuration.
This can be useful when leveraging `eos_cli_config_gen` to generate configlets with CloudVision.

The following commands will be omitted when `generate_default_config` is set to `false`:

- RANCID Content Type
- Hostname
- Default configuration for `aaa`
- Default configuration for `enable password`
- Transceiver qsfp default mode
- End of configuration delimiter

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>generate_default_config</samp>](## "generate_default_config") | Boolean |  | True |  |  |

=== "YAML"

    ```yaml
    generate_default_config: <bool>
    ```

## Generate Device Documentation

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>generate_device_documentation</samp>](## "generate_device_documentation") | Boolean |  | True |  |  |

=== "YAML"

    ```yaml
    generate_device_documentation: <bool>
    ```
