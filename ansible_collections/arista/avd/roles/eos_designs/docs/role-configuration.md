---
# This title is used for search results
title: Role configuration for eos_designs
---
<!--
  ~ Copyright (c) 2023-2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# Role configuration for eos_designs

Role configuration settings can be set either as regular inventory variables or directly as task_vars on the `import_role` task.

## Collection-wide output directories

Default output directories use the collection-wide `avd_*` variables:

``` yaml
avd_root_dir: "{{ inventory_dir }}"
avd_documentation_dir_name: "documentation"
avd_documentation_dir: "{{ avd_root_dir }}/{{ avd_documentation_dir_name }}"
avd_fabric_dir_name: "fabric"
avd_fabric_dir: "{{ avd_documentation_dir }}/{{ avd_fabric_dir_name }}"
avd_output_dir_name: "intended"
avd_output_dir: "{{ avd_root_dir }}/{{ avd_output_dir_name }}"
avd_structured_dir_name: "structured_configs"
avd_structured_dir: "{{ avd_output_dir }}/{{ avd_structured_dir_name }}"
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

Any data validation issues will trigger errors - blocking further processing.

## Generation of facts, structured configuration and documentation

The following settings can be leveraged to control generation of structured configuration and fabric documentation.

--8<--
schemas/avd_design/docs/tables/role-settings.md
--8<--

## Custom Templates

--8<--
schemas/avd_design/docs/tables/role-custom-templates.md
--8<--

## Legacy input aliases

The previously supported generic inputs remain accepted silently. If both a
generic name and its `avd_*` equivalent are set, the `avd_*` value wins.

--8<--
schemas/avd_design/docs/tables/legacy-role-settings.md
--8<--
