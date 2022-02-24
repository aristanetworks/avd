# GNU General Public License v3.0+
#
# Copyright 2021 Arista Networks AS-EMEA
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

DOCUMENTATION = r'''
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
  templates:
    description: List of dicts for Jinja templates to be run.
    required: true
    type: list
    elements: dict
    suboptions:
      template:
        description: Template file
        required: true
        type: str
      options:
        description: Template options
        required: false
        type: dict
        suboptions:
          list_merge:
            description: Merge strategy for lists for Ansible Combine filter
            required: false
            default: 'append'
            type: str
          strip_empty_keys:
            description: "Filter out keys from the generated output if value is null/none/undefined"
            required: false
            default: true
            type: bool
  debug:
    description: Output list 'avd_yaml_templates_to_facts_debug' with timestamps of each performed action.
    required: false
    type: bool
  dest:
    description: |
      Destination path. If set, the output facts will also be written to this path.
      Autodetects data format based on file suffix. '.yml', '.yaml' -> YAML, default -> JSON
    required: false
    type: str
  template_output:
    description: |
      If true the output data will be run through another jinja2 rendering before returning.
      This is to resolve any input values with inline jinja using variables/facts set by the input templates.
    required: false
    type: bool
'''

EXAMPLES = r'''
# tasks file for configlet_build_config
- name: Generate device configuration in structured format
  yaml_templates_to_facts:
    root_key: structured_config
    templates:
      - template: "base/main.j2"
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
  check_mode: no
  changed_when: False
'''
