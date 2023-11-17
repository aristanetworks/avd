---
# This title is used for search results
title: arista.avd.validate_and_template
---
<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# validate_and_template

!!! note
    Always use the FQCN (Fully Qualified Collection Name) `arista.avd.validate_and_template` when using this plugin.

Validate input data according to Schema, render Jinja2 template and write result to a file.

## Synopsis

The \`arista.avd.validate\_and\_template\` Action Plugin performs data conversions and validation according to the supplied Schema.

The converted data is then used to render a Jinja2 template and writing the result to a file.

The Action Plugin supports different modes for conversion and validation, to either block the playbook or just warn the user if the input data is not valid.

For Markdown files the plugin can also run md\_toc on the output before writing to the file.

## Parameters

| Argument | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| template | str | True | None |  | Path to Jinja2 Template file |
| dest | str | True | None |  | Destination path. The rendered template will be written to this file |
| mode | str | False | None |  | File mode for dest file. |
| schema | dict | False | None |  | Schema conforming to \"AVD Meta Schema\". Either schema or schema\_id must be set. |
| schema_id | str | False | None | Valid values:<br>- <code>eos_cli_config_gen</code><br>- <code>eos_designs</code> | ID of Schema conforming to \"AVD Meta Schema\".  Either schema or schema\_id must be set. |
| add_md_toc | bool | False | None |  | Run md\_toc on the output before writing to the file. |
| md_toc_skip_lines | int | False | 0 |  | Pass this value as skip\_lines to add\_md\_toc. |
| conversion_mode | str | False | debug | Valid values:<br>- <code>warning</code><br>- <code>info</code><br>- <code>debug</code><br>- <code>quiet</code><br>- <code>disabled</code> | Run data conversion in either \"warning\", \"info\", \"debug\", \"quiet\" or \"disabled\" mode.<br>Conversion will perform type conversion of input variables as defined in the schema.<br>Conversion is intended to help the user to identify minor issues with the input data, while still allowing the data to be validated.<br>During conversion, messages will generated with information about the host\(s\) and key\(s\) which required conversion.<br>conversion\_mode\:disabled means that conversion will not run.<br>conversion\_mode\:error will produce error messages and fail the task.<br>conversion\_mode\:warning will produce warning messages.<br>conversion\_mode\:info will produce regular log messages.<br>conversion\_mode\:debug will produce hidden messages viewable with \-v.<br>conversion\_mode\:quiet will not produce any messages. |
| validation_mode | str | False | warning | Valid values:<br>- <code>error</code><br>- <code>warning</code><br>- <code>info</code><br>- <code>debug</code><br>- <code>disabled</code> | Run validation in either \"error\", \"warning\", \"info\", \"debug\" or \"disabled\" mode.<br>Validation will validate the input variables according to the schema.<br>During validation, messages will generated with information about the host\(s\) and key\(s\) which failed validation.<br>validation\_mode\:disabled means that validation will not run.<br>validation\_mode\:error will produce error messages and fail the task.<br>validation\_mode\:warning will produce warning messages.<br>validation\_mode\:info will produce regular log messages.<br>validation\_mode\:debug will produce hidden messages viewable with \-v. |

## Examples

```yaml
- name: Generate device documentation
  tags: [build, provision, documentation]
  arista.avd.validate_and_template:
    template: "eos-device-documentation.j2"
    dest: "{{ devices_dir }}/{{ inventory_hostname }}.md"
    mode: 0664
    schema: "{{ lookup('ansible.builtin.file', role_schema_path) | from_yaml }}"
    conversion_mode: "{{ avd_data_conversion_mode }}"
    validation_mode: "{{ avd_data_validation_mode }}"
    add_md_toc: true
    md_toc_skip_lines: 3
  delegate_to: localhost
  when: generate_device_documentation | arista.avd.default(true)
```

## Authors

- Arista Ansible Team (@aristanetworks)
