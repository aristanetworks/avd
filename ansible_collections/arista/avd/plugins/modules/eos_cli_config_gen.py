# Copyright (c) 2021-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

DOCUMENTATION = r"""
---
module: eos_cli_config_gen
version_added: "4.9.0"
author: Arista Ansible Team (@aristanetworks)
short_description: Generate AVD EOS device configurations and documentations
description: |-
  The `arista.avd.eos_cli_config_gen` module is an Ansible Action Plugin providing the following capabilities:

  - Validates input variables according to eos_cli_config_gen schema
  - Generates device configuration and saves it to file
  - Optionallu generates device documentation and saves it to file
options:
  structured_config_filename:
    description: The path of the structured config to load. Required if read_structured_config_from_file is true.
    type: str
  config_filename:
    description: The path to save the generated config to. Required if generate_device_config is true.
    type: str
  documentation_filename:
    description: The path to save the generated documentation. Required if generate_device_doc is true.
    type: str
  read_structured_config_from_file:
    description: Flag to indicate if the structured config should be read from a file or not.
    type: bool
    default: true
  generate_device_config:
    description: Flag to generate the device configuration.
    type: bool
    default: true
  generate_device_doc:
    description: Flag to generate the device documentation.
    type: bool
    default: true
  device_doc_toc:
    description: Flag to generate the table of content for the device documentation.
    type: bool
    default: true
  conversion_mode:
    description:
      - Run data conversion in either "error", "warning", "info", "debug", "quiet" or "disabled" mode.
      - Conversion will perform type conversion of input variables as defined in the schema.
      - Conversion is intended to help the user to identify minor issues with the input data, while still allowing the data to be validated.
      - During conversion, messages will be generated with information about the host(s) and key(s) which required conversion.
      - conversion_mode:disabled means that conversion will not run.
      - conversion_mode:error will produce error messages and fail the task.
      - conversion_mode:warning will produce warning messages.
      - conversion_mode:info will produce regular log messages.
      - conversion_mode:debug will produce hidden messages viewable with -v.
      - conversion_mode:quiet will not produce any messages.
    required: false
    default: "debug"
    type: str
    choices: [ "error", "warning", "info", "debug", "quiet", "disabled" ]
  validation_mode:
    description:
      - Run validation in either "error", "warning", "info", "debug" or "disabled" mode.
      - Validation will validate the input variables according to the schema.
      - During validation, messages will be generated with information about the host(s) and key(s) which failed validation.
      - validation_mode:disabled means that validation will not run.
      - validation_mode:error will produce error messages and fail the task.
      - validation_mode:warning will produce warning messages.
      - validation_mode:info will produce regular log messages.
      - validation_mode:debug will produce hidden messages viewable with -v.
    required: false
    default: "warning"
    type: str
    choices: [ "error", "warning", "info", "debug", "disabled" ]
  cprofile_file:
    description:
      - Filename for storing cprofile data used to debug performance issues.
      - Running cprofile will slow down performance in it self, so only set this while troubleshooting.
    required: false
    type: str
"""

EXAMPLES = r"""
---
- name: Generate eos intended configuration and device documentation
  arista.avd.eos_cli_config_gen:
    structured_config_filename: "{{ structured_config_filename }}"
    config_filename: "{{ eos_config_dir }}/{{ inventory_hostname }}.cfg"
    documentation_filename: "{{ devices_dir }}/{{ inventory_hostname }}.md"
    read_structured_config_from_file: true
  delegate_to: localhost
  vars:
    structured_config_filename: "{{ structured_dir }}/{{ inventory_hostname }}.{{ avd_structured_config_file_format }}"
- name: Generate device documentation only
  arista.avd.eos_cli_config_gen:
    structured_config_filename: "{{ structured_config_filename }}"
    config_filename: "{{ eos_config_dir }}/{{ inventory_hostname }}.cfg"
    documentation_filename: "{{ devices_dir }}/{{ inventory_hostname }}.md"
    read_structured_config_from_file: true
    generate_device_config: false
    device_doc_toc: true
  delegate_to: localhost
  vars:
    structured_config_filename: "{{ structured_dir }}/{{ inventory_hostname }}.{{ avd_structured_config_file_format }}"
"""
