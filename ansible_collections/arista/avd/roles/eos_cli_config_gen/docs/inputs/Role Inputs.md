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
    | <samp>custom_templates</samp> | List, items: String |  |  |  |  |
    | <samp>&nbsp;&nbsp;- &lt;str&gt;</samp> | String |  |  |  | Template relative path below playbook directory |

=== "YAML"

    ```yaml
    custom_templates:
      - <str>
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
    | <samp>generate_default_config</samp> | Boolean |  | True |  |  |

=== "YAML"

    ```yaml
    generate_default_config: <bool>
    ```
## Generate Device Documentation



=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | <samp>generate_device_documentation</samp> | Boolean |  | True |  |  |

=== "YAML"

    ```yaml
    generate_device_documentation: <bool>
    ```
