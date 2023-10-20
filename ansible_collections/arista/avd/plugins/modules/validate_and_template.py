# Copyright (c) 2021-2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

DOCUMENTATION = r"""
---
module: validate_and_template
version_added: "3.8.0"
author: Arista Ansible Team (@aristanetworks)
short_description: Validate input data according to Schema, render Jinja2 template and write result to a file.
description:
  - The `arista.avd.validate_and_template` Action Plugin performs data conversions and validation according to the supplied Schema.
  - The converted data is then used to render a Jinja2 template and writing the result to a file.
  - The Action Plugin supports different modes for conversion and validation, to either block the playbook or just warn the user if
    the input data is not valid.
  - For Markdown files the plugin can also run md_toc on the output before writing to the file.
options:
  template:
    description: Path to Jinja2 Template file
    required: true
    type: str
  dest:
    description: Destination path. The rendered template will be written to this file
    required: true
    type: str
  mode:
    description: File mode for dest file.
    required: false
    type: str
  schema:
    description: Schema conforming to "AVD Meta Schema". Either schema or schema_id must be set.
    required: false
    type: dict
  schema_id:
    description: ID of Schema conforming to "AVD Meta Schema".  Either schema or schema_id must be set.
    required: false
    type: str
    choices: [ "eos_cli_config_gen", "eos_designs" ]
  add_md_toc:
    description: Run md_toc on the output before writing to the file.
    required: false
    type: bool
  md_toc_skip_lines:
    description: Pass this value as skip_lines to add_md_toc.
    default: 0
    type: int
    required: false
  conversion_mode:
    description:
      - Run data conversion in either "warning", "info", "debug", "quiet" or "disabled" mode.
      - Conversion will perform type conversion of input variables as defined in the schema.
      - Conversion is intended to help the user to identify minor issues with the input data, while still allowing the data to be validated.
      - During conversion, messages will generated with information about the host(s) and key(s) which required conversion.
      - conversion_mode:disabled means that conversion will not run.
      - conversion_mode:error will produce error messages and fail the task.
      - conversion_mode:warning will produce warning messages.
      - conversion_mode:info will produce regular log messages.
      - conversion_mode:debug will produce hidden messages viewable with -v.
      - conversion_mode:quiet will not produce any messages.
    required: false
    default: "debug"
    type: str
    choices: [ "warning", "info", "debug", "quiet", "disabled" ]
  validation_mode:
    description:
      - Run validation in either "error", "warning", "info", "debug" or "disabled" mode.
      - Validation will validate the input variables according to the schema.
      - During validation, messages will generated with information about the host(s) and key(s) which failed validation.
      - validation_mode:disabled means that validation will not run.
      - validation_mode:error will produce error messages and fail the task.
      - validation_mode:warning will produce warning messages.
      - validation_mode:info will produce regular log messages.
      - validation_mode:debug will produce hidden messages viewable with -v.
    required: false
    default: "warning"
    type: str
    choices: [ "error", "warning", "info", "debug", "disabled" ]
"""

EXAMPLES = r"""
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
"""
