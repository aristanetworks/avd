# arista.avd.validate_and_template

Validate input data according to Schema\, render Jinja2 template and write result to a file\.

## Synopsis

The \`arista\.avd\.validate\_and\_template\` Action Plugin performs data conversions and validation according to the supplied Schema\.

The converted data is then used to render a Jinja2 template and writing the result to a file\.

The Action Plugin supports different modes for conversion and validation\, to either block the playbook or just warn the user if

the input data is not valid\.

For Markdown files the plugin can also run md\_toc on the output before writing to the file\.

## Parameters

  template (True, str, None)
    Path to Jinja2 Template file

  dest (True, str, None)
    Destination path\. The rendered template will be written to this file

  mode (False, str, None)
    File mode for dest file\.

  schema (False, dict, None)
    Schema conforming to \"AVD Meta Schema\"\. Either schema or schema\_id must be set\.

  schema_id (False, str, None)
    ID of Schema conforming to \"AVD Meta Schema\"\.  Either schema or schema\_id must be set\.

  add_md_toc (False, bool, None)
    Run md\_toc on the output before writing to the file\.

  md_toc_skip_lines (False, int, 0)
    Pass this value as skip\_lines to add\_md\_toc\.

  conversion_mode (False, str, debug)
    Run data conversion in either \"warning\"\, \"info\"\, \"debug\"\, \"quiet\" or \"disabled\" mode\.
    Conversion will perform type conversion of input variables as defined in the schema\.
    Conversion is intended to help the user to identify minor issues with the input data\, while still allowing the data to be validated\.
    During conversion\, messages will generated with information about the host\(s\) and key\(s\) which required conversion\.
    conversion\_mode\:disabled means that conversion will not run\.
    conversion\_mode\:error will produce error messages and fail the task\.
    conversion\_mode\:warning will produce warning messages\.
    conversion\_mode\:info will produce regular log messages\.
    conversion\_mode\:debug will produce hidden messages viewable with \-v\.
    conversion\_mode\:quiet will not produce any messages\.

  validation_mode (False, str, warning)
    Run validation in either \"error\"\, \"warning\"\, \"info\"\, \"debug\" or \"disabled\" mode\.
    Validation will validate the input variables according to the schema\.
    During validation\, messages will generated with information about the host\(s\) and key\(s\) which failed validation\.
    validation\_mode\:disabled means that validation will not run\.
    validation\_mode\:error will produce error messages and fail the task\.
    validation\_mode\:warning will produce warning messages\.
    validation\_mode\:info will produce regular log messages\.
    validation\_mode\:debug will produce hidden messages viewable with \-v\.

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

## Status

## Authors

- Arista Ansible Team (@aristanetworks)
