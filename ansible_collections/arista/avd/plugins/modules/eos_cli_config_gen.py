# Copyright (c) 2021-2026 Arista Networks, Inc.
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

  - Generates device configuration and saves it to file
  - Optionally generates device documentation and saves it to file

  Note: Input validation is performed by the `arista.avd.validate_inputs` plugin, which must be run before this plugin.
options:
  tmp_dir:
    description:
      - Path to use as the AVD temporary directory for storing templated and validated data used internally by plugins.
      - Must be the same across all plugins.
    required: true
    type: str
  config_filename:
    description: The path to save the generated config to. Required if generate_device_config is true.
    type: str
  documentation_filename:
    description: The path to save the generated documentation. Required if generate_device_doc is true.
    type: str
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
  cprofile_file:
    description:
      - Filename for storing cprofile data used to debug performance issues.
      - Running cprofile will slow down performance in it self, so only set this while troubleshooting.
    required: false
    type: str
"""

EXAMPLES = r"""
---
- name: Generate EOS intended configuration and device documentation
  arista.avd.eos_cli_config_gen:
    config_filename: "{{ eos_config_dir }}/{{ inventory_hostname }}.cfg"
    documentation_filename: "{{ devices_dir }}/{{ inventory_hostname }}.md"
  delegate_to: localhost

- name: Generate device documentation only
  arista.avd.eos_cli_config_gen:
    config_filename: "{{ eos_config_dir }}/{{ inventory_hostname }}.cfg"
    documentation_filename: "{{ devices_dir }}/{{ inventory_hostname }}.md"
    generate_device_config: false
    device_doc_toc: true
  delegate_to: localhost
"""
