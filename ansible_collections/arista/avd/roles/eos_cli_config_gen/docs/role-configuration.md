# Role configuration

Role configuration settings can be set either as regular inventory variables or directly as task_vars on the `import_role` task.

## Input Variables Validation settings

--avdschema--
eos_cli_config_gen:role-input-validation
--avdschema--

## Extensibility with Custom Templates

- Custom templates can be added below the playbook directory.
- If a location above the directory is desired, a symbolic link can be used.
- Example under the `playbooks` directory create symbolic link with the following command:

  ```bash
  ln -s ../../shared_repo/custom_avd_templates/ ./custom_avd_templates
  ```

- The output will be rendered at the end of the configuration.
- The order of custom templates in the list can be important if they overlap.
- It is recommenended to use a `!` delimiter at the top of each custom template.

--avdschema--
eos_cli_config_gen:custom-templates
--avdschema--

### eos_cli_config_gen configuration

--avdschema--
eos_cli_config_gen:eos-cli-config-gen-configuration
--avdschema--

### eos_cli_config_gen documentation

--avdschema--
eos_cli_config_gen:eos-cli-config-gen-documentation
--avdschema--

### Generate default config

The `generate_default_config` knob allows to omit default EOS configuration.
This can be useful when leveraging `eos_cli_config_gen` to generate configlets with CloudVision.

The following commands will be omitted when `generate_default_config` is set to `false`:

- RANCID Content Type
- Hostname
- Default configuration for `aaa`
- Default configuration for `enable password`
- Transceiver qsfp default mode
- End of configuration delimiter

--avdschema--
eos_cli_config_gen:generate-default-config
--avdschema--

### Generate device documentation

--avdschema--
eos_cli_config_gen:generate-device-documentation
--avdschema--
