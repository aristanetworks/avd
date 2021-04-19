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

ANSIBLE_METADATA = {'metadata_version': '1.0.0',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = r'''
---
module: yaml_template_to_fact
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
    description: List of Jinja templates to be run.
    required: true
    type: list
    elements: str
'''

EXAMPLES = r'''
# tasks file for configlet_build_config
- name: Generate device configuration in structured format
  yaml_template_to_fact:
    root_key: structured_config
    yaml_templates: "{{ templates.structured_config }}"
  check_mode: no
  changed_when: False
'''
