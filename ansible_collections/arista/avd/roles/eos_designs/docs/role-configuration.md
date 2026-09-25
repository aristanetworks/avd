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

## Role default output directories

Default output directories can be updated with the role-prefixed variables:

``` yaml
eos_designs_root_dir: "{{ inventory_dir }}"
eos_designs_documentation_dir_name: "documentation"
eos_designs_documentation_dir: "{{ eos_designs_root_dir }}/{{ eos_designs_documentation_dir_name }}"
eos_designs_fabric_dir_name: "fabric"
eos_designs_fabric_dir: "{{ eos_designs_documentation_dir }}/{{ eos_designs_fabric_dir_name }}"
eos_designs_output_dir_name: "intended"
eos_designs_output_dir: "{{ eos_designs_root_dir }}/{{ eos_designs_output_dir_name }}"
eos_designs_structured_dir_name: "structured_configs"
eos_designs_structured_dir: "{{ eos_designs_output_dir }}/{{ eos_designs_structured_dir_name }}"
```

!!! tip
    To place the outputs outside the inventory directory, use a path relative to `inventory_dir`, for example
    `eos_designs_root_dir: "{{ inventory_dir }}/../outputs"`.

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

## Legacy role variable aliases

Legacy unprefixed aliases remain supported. The role-prefixed variable takes precedence when both names are set.

--8<--
schemas/avd_design/docs/tables/legacy-role-settings.md
--8<--
