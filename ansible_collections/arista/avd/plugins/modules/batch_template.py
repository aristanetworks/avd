# Copyright (c) 2021-2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

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
