# Copyright 2021 Arista Networks
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

DOCUMENTATION = r"""
---
module: batch_template
version_added: "4.0.0"
author: Arista Ansible Team (@aristanetworks)
short_description: Render Jinja2 template on multiple items and write result to individual files.
description:
  - Render Jinja2 template on multiple items and write result to individual files.
  - Destination file mode is hardcoded to 0o664.
options:
  template:
    description: Path to Jinja2 Template file
    required: true
    type: str
  dest_format_string:
    description: Format string used to specify target file for each item. 'item' is the current item from 'items'. Like "mypath/{item}.md"
    required: true
    type: str
  items:
    description: List of strings. Each list item is passed to 'dest_format_string' as 'item' and passed to templater as 'item'
    required: true
    type: list
    elements: str
"""

EXAMPLES = r"""
- name: Output eos_cli_config_gen Documentation
  tags: [eos_cli_config_gen]
  delegate_to: localhost
  run_once: true
  arista.avd.batch_template:
    template: avd_schema_documentation.j2
    dest_format_str: "{{ role_documentation_dir }}/{item}.md"
    items: "{{ documentation_schema | list }}"
  vars:
    documentation_schema: "{{ role_name | arista.avd.convert_schema(type='documentation') }}"
"""
