---
# This title is used for search results
title: arista.avd.validate_and_template
---
<!--
  ~ Copyright (c) 2023-2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# validate_and_template

!!! note
    Always use the FQCN (Fully Qualified Collection Name) `arista.avd.validate_and_template` when using this plugin.

Validate input data according to Schema, render Jinja2 template and write result to a file.

## Synopsis

The `arista.avd.validate_and_template` Action Plugin performs data conversions and validation according to the supplied Schema.

The converted data is then used to render a Jinja2 template and writing the result to a file.

The Action Plugin supports different modes for conversion and validation, to either block the playbook or just warn the user if the input data is not valid.

For Markdown files the plugin can also run md_toc on the output before writing to the file.

## Parameters

| Argument | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| <samp>template</samp> | str | True | None |  | Path to Jinja2 Template file |
| <samp>dest</samp> | str | True | None |  | Destination path. The rendered template will be written to this file |
| <samp>mode</samp> | str | False | None |  | File mode for dest file. |
| <samp>schema</samp> | dict | False | None |  | Schema conforming to &#34;AVD Meta Schema&#34;. Either schema or schema_id must be set. |
| <samp>schema_id</samp> | str | False | None | Valid values:<br>- <code>eos_cli_config_gen</code><br>- <code>eos_designs</code> | ID of Schema conforming to &#34;AVD Meta Schema&#34;.  Either schema or schema_id must be set. |
| <samp>add_md_toc</samp> | bool | False | None |  | Run md_toc on the output before writing to the file. |
| <samp>md_toc_skip_lines</samp> | int | False | 0 |  | Pass this value as skip_lines to add_md_toc. |
| <samp>conversion_mode</samp> | str | False | debug | Valid values:<br>- <code>warning</code><br>- <code>info</code><br>- <code>debug</code><br>- <code>quiet</code><br>- <code>disabled</code> | Run data conversion in either &#34;warning&#34;, &#34;info&#34;, &#34;debug&#34;, &#34;quiet&#34; or &#34;disabled&#34; mode.<br>Conversion will perform type conversion of input variables as defined in the schema.<br>Conversion is intended to help the user to identify minor issues with the input data, while still allowing the data to be validated.<br>During conversion, messages will generated with information about the host(s) and key(s) which required conversion.<br>conversion_mode:disabled means that conversion will not run.<br>conversion_mode:error will produce error messages and fail the task.<br>conversion_mode:warning will produce warning messages.<br>conversion_mode:info will produce regular log messages.<br>conversion_mode:debug will produce hidden messages viewable with -v.<br>conversion_mode:quiet will not produce any messages. |
| <samp>validation_mode</samp> | str | False | warning | Valid values:<br>- <code>error</code><br>- <code>warning</code><br>- <code>info</code><br>- <code>debug</code><br>- <code>disabled</code> | Run validation in either &#34;error&#34;, &#34;warning&#34;, &#34;info&#34;, &#34;debug&#34; or &#34;disabled&#34; mode.<br>Validation will validate the input variables according to the schema.<br>During validation, messages will generated with information about the host(s) and key(s) which failed validation.<br>validation_mode:disabled means that validation will not run.<br>validation_mode:error will produce error messages and fail the task.<br>validation_mode:warning will produce warning messages.<br>validation_mode:info will produce regular log messages.<br>validation_mode:debug will produce hidden messages viewable with -v. |
| <samp>cprofile_file</samp> | str | False | None |  | Filename for storing cprofile data used to debug performance issues.<br>Running cprofile will slow down performance in itself, so only set this while troubleshooting. |

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
