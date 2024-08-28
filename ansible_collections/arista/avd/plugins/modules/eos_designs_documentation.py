# Copyright (c) 2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

DOCUMENTATION = r"""
---
module: eos_designs_documentation
version_added: "5.0.0"
author: Arista Ansible Team (@aristanetworks)
short_description: Generate AVD Fabric Documentation
description: |-
  The `arista.avd.eos_designs_documentation` module is an Ansible Action Plugin providing the following capabilities:

  - Generate fabric documentation using AVD facts and structured configuration files.
  - Optionally include connected endpoints documentation.
options:
  structured_config_dir:
    description: Path to directory containing files with AVD structured configurations.
    required: true
    type: str
  structured_config_suffix:
    description: File suffix for AVD structured configuration files.
    default: "yml"
    type: str
  fabric_documentation_file:
    description: Path to output Markdown file.
    required: true
    type: str
  mode:
    description: Mode of output files.
    default: "0o664"
    type: str
  fabric_documentation:
    description: Generate fabric documentation.
    default: true
    type: bool
  include_connected_endpoints:
    description: Include connected endpoints in fabric documentation.
    default: false
    type: bool
  topology_csv_file:
    description: Path to output topology CSV file.
    required: true
    type: str
  topology_csv:
    description: Generate Topology CSV with all interfaces towards other devices. Contains both ends of a link.
    default: false
    type: bool
"""

EXAMPLES = r"""
---
- name: Generate fabric documentation
  tags: [build, provision, documentation]
  arista.avd.eos_designs_documentation:
    device_list: "{{ ansible_play_hosts }}"
    structured_config_dir: "{{ structured_dir }}"
    structured_config_suffix: "{{ avd_structured_config_file_format }}"
    fabric_documentation_file: "{{ fabric_dir }}/{{ fabric_name }}-documentation.md"
    fabric_documentation: true
    include_connected_endpoints: "{{ eos_designs_documentation.connected_endpoints | arista.avd.default(false) }}"
    mode: "0o664"
"""

# TODO: RETURN
