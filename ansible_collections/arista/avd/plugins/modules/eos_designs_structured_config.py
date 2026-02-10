# Copyright (c) 2021-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

DOCUMENTATION = r"""
---
module: eos_designs_structured_config
version_added: "4.0.0"
author: Arista Ansible Team (@aristanetworks)
short_description: Generate AVD EOS Designs structured configuration
description: |-
  The `arista.avd.eos_designs_structured_config` module is an Ansible Action Plugin providing the following capabilities:

  - Generates structured configuration
  - Optionally run any custom jinja2 YAML templates and merge result onto structured configuration
  - Optionally run jinja2 templating the generated structured configuration
  - Optionally write structured configuration to a JSON or YAML file
  - Return structured configuration as "ansible_facts"

  Note: Input validation is performed by the `arista.avd.validate_inputs` plugin, which must be run before this plugin.
options:
  tmp_dir:
    description:
      - Path to use as the AVD temporary directory for storing templated and validated data used internally by plugins.
      - Must be the same across all plugins.
    required: true
    type: str
  eos_designs_custom_templates:
    description: List of dicts for Jinja2 templates to be run after generating the structured configuration
    required: false
    type: list
    elements: dict
    suboptions:
      template:
        description: |
          Template file.
        required: true
        type: str
      options:
        description: Template options
        required: false
        type: dict
        suboptions:
          list_merge:
            description: Merge strategy for lists
            required: false
            default: 'append'
            type: str
          strip_empty_keys:
            description:
              - Filter out keys from the generated output if value is null/none/undefined
              - Only applies to templates.
            required: false
            default: true
            type: bool
  dest:
    description:
      - Destination path. If set, the output facts will also be written to this path.
      - Autodetects data format based on file suffix. '.yml', '.yaml' -> YAML, default -> JSON
    required: false
    type: str
  mode:
    description: File mode (ex. "0o664") for dest file. See 'ansible.builtin.copy' module for details.
    required: false
    type: str
  template_output:
    description:
      - If true, the output data will be run through another jinja2 rendering before returning.
      - This is to resolve any input values with inline jinja using variables/facts set by the input templates.
      - Ignored for ansible-core versions >= 2.19, since it is no longer needed.
    required: false
    type: bool
  cprofile_file:
    description:
      - Filename for storing cprofile data used to debug performance issues.
      - Running cprofile will slow down performance in it self, so only set this while troubleshooting.
    required: false
    type: str
  digital_twin:
    description: |-
      PREVIEW: This option is marked as "preview", meaning the data models or generated configuration can change at any time.
      Generate Digital Twin topology information.
    default: false
    type: bool
  return_structured_config:
    description: |-
      Return the structured configuration as "ansible_facts".
    default: false
    type: bool
"""

EXAMPLES = r"""
---
- name: Generate device configuration in structured format
  arista.avd.eos_designs_structured_config:
    tmp_dir: "intended/tmp/eos_designs"
    templates:
      - template: "custom_templates/custom_feature1.j2"
      - template: "custom_templates/custom_feature2.j2"
        options:
          list_merge: replace
          strip_empty_keys: false
  check_mode: false
  changed_when: false
"""
