---
# This title is used for search results
title: Role configuration for eos_cli_config_gen
---
<!--
  ~ Copyright (c) 2023-2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# Role configuration for eos_cli_config_gen

Role configuration settings can be set either as regular inventory variables or directly as task_vars on the `import_role` task.

## Collection-wide output directories

Default output directories use the collection-wide `avd_*` variables:

``` yaml
avd_root_dir: "{{ inventory_dir }}"
avd_documentation_dir_name: "documentation"
avd_documentation_dir: "{{ avd_root_dir }}/{{ avd_documentation_dir_name }}"
avd_devices_dir_name: "devices"
avd_devices_dir: "{{ avd_documentation_dir }}/{{ avd_devices_dir_name }}"
avd_output_dir_name: "intended"
avd_output_dir: "{{ avd_root_dir }}/{{ avd_output_dir_name }}"
avd_structured_dir_name: "structured_configs"
avd_structured_dir: "{{ avd_output_dir }}/{{ avd_structured_dir_name }}"
avd_eos_config_dir_name: "configs"
avd_eos_config_dir: "{{ avd_output_dir }}/{{ avd_eos_config_dir_name }}"
```

!!! tip
    To place the outputs outside the inventory directory, use a path relative to `inventory_dir`, for example
    `avd_root_dir: "{{ inventory_dir }}/../outputs"`.

The previous unprefixed inputs (`root_dir`, `output_dir`, and related names) remain
accepted silently. If both names are set, the `avd_*` value wins. Use `avd_*` when
sharing output paths with another role; an unconfigured generic `output_dir` is not
guaranteed to be exported after the role completes.

## Input Variables Validation

Schema validation is performed by the `validate_inputs` action plugin which is called automatically by the role.
The plugin performs variable type conversion and validation of the converted data against the AVD schema.

Any data validation issue will trigger errors - blocking further processing.

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

!!! tip
    The templates will have any host or group variable available to it.
    If adding custom keys to an existing AVD data model, start the key with an underscore `_`, so it will be ignored by schema validation.

--8<--
schemas/eos_config/docs/tables/custom-templates.md
--8<--

## Generation of device configuration and documentation

The following settings can be leveraged to control generation of device configuration and documentation.

The `eos_cli_config_gen_configuration.hide_passwords` and `eos_cli_config_gen_documentation.hide_passwords` settings are role render settings and can be set as inventory variables or directly under `vars` on the `import_role` task. When `eos_cli_config_gen_read_structured_config_from_file` is enabled, they do not need to be present in the structured configuration files.

--8<--
schemas/eos_config/docs/tables/role-settings.md
--8<--

## Legacy input aliases

The previously supported generic inputs remain accepted silently. If both a
generic name and its `avd_*` equivalent are set, the `avd_*` value wins.

--8<--
schemas/eos_config/docs/tables/legacy-role-settings.md
--8<--
