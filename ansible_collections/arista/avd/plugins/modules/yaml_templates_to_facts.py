# Copyright (c) 2021-2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

DOCUMENTATION = r"""
---
module: yaml_templates_to_facts
version_added: "1.0.0"
author: EMEA AS Team (@aristanetworks)
short_description: Set facts from YAML via Jinja2 templates
description:
  - Set facts from YAML produced by Jinja2 templates
options:
  root_key:
    description: Root key under which the facts will be defined. If not set the facts well be set directly on root level.
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
  templates:
    description: List of dicts for Jinja templates to be run.
    required: true
    type: list
    elements: dict
    suboptions:
      template:
        description: Template file. Either template or python_module must be set.
        required: false
        type: str
      python_module:
        description: Python module to import. Either template or python_module must be set.
        required: false
        type: str
      python_class_name:
        description: Name of Python Class to import.
        required: false
        type: str
        default: "AvdStructuredConfig"
      options:
        description: Template options.
        required: false
        type: dict
        suboptions:
          list_merge:
            description: Merge strategy for lists
            required: false
            default: 'append'
            type: str
          strip_empty_keys:
            description: Filter out keys from the generated output if value is null/none/undefined. Only applies to templates.
            required: false
            default: true
            type: bool
  debug:
    description: Output list 'avd_yaml_templates_to_facts_debug' with timestamps of each performed action.
    required: false
    type: bool
  dest:
    description:
      - Destination path. If set, the output facts will also be written to this path.
      - Autodetects data format based on file suffix. '.yml', '.yaml' -> YAML, default -> JSON
    required: false
    type: str
  mode:
    description: File mode (ex. 0664) for dest file. See 'ansible.builtin.copy' module for details.
    required: false
    type: str
  template_output:
    description:
      - If true, the output data will be run through another jinja2 rendering before returning.
      - This is to resolve any input values with inline jinja using variables/facts set by the input templates.
    required: false
    type: bool
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
  output_schema:
    description: AVD Schema for output data. Used for automatic merge of data.
    required: false
    type: dict
  output_schema_id:
    description: ID of AVD Schema for output data. Used for automatic merge of data.
    required: false
    type: str
    choices: [ "eos_cli_config_gen", "eos_designs" ]
  set_switch_fact:
    description:
      - Set "switch" fact from on "avd_switch_facts.<inventory_hostname>.switch"
    required: false
    type: bool
    default: true
"""

EXAMPLES = r"""
---
- name: Generate device configuration in structured format
  arista.avd.yaml_templates_to_facts:
    root_key: structured_config
    templates:
      - python_module: "ansible_collections.arista.avd.roles.eos_designs.python_modules.base"
        python_class_name: "AvdStructuredConfig"
      - template: "mlag/main.j2"
      - template: "designs/underlay/main.j2"
      - template: "designs/overlay/main.j2"
      - template: "l3_edge/main.j2"
      - template: "designs/network_services/main.j2"
      - template: "connected_endpoints/main.j2"
      - template: "custom-structured-configuration-from-var.j2"
        options:
          list_merge: "{{ custom_structured_configuration_list_merge }}"
          strip_empty_keys: false
    schema_id: eos_designs
    output_schema_id: eos_cli_config_gen
  check_mode: no
  changed_when: False
"""
