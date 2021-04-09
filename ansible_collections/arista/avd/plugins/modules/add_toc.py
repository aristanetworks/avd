#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# GNU General Public License v3.0+
#
# Copyright 2019 Arista Networks AS-EMEA
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

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '1.0.0',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = r'''
---
module: add_toc
version_added: "2.0.0"
author: Ansible Arista Team (@aristanetworks)
short_description: Add Table Of Contents to existing MarkDown file
description:
  - Wrapper of md_toc python library
  - Produce Table of Content and add to MD file between markers
options:
  md_file:
    description: MD file to be updated
    required: true
    type: str
  skip_lines:
    description: Skip first x lines when parsing MD file
    required: false
    default: 0
    type: int
  toc_levels:
    description: How many levels of headings will be included in the TOC (Default:2)
    required: false
    default: 2
    type: int
  toc_marker:
    description: TOC will be inserted or updated between two of these markers in the MD file
    required: false
    default: '<!-- toc -->'
    type: str
'''

EXAMPLES = r'''
- name: Generate TOC for device documentation
  add_toc:
    md_file: '{{ root_dir }}/documentation/devices/{{ inventory_hostname }}.md'
    skip_lines: 3
    #toc_levels: 2
    #toc_marker: '<!-- toc -->'
'''

import hashlib
from ansible.module_utils.basic import AnsibleModule
try:
    import md_toc
    HAS_MD_TOC = True
except ImportError:
    HAS_MD_TOC = False


def main():
    """ Main entry point for module execution."""
    argument_spec = dict(
        md_file=dict(type='str', required=True),
        skip_lines=dict(type='int', required=False, default=0),
        toc_levels=dict(type='int', required=False, default=2),
        toc_marker=dict(type='str', required=False, default='<!-- toc -->')
    )

    module = AnsibleModule(argument_spec=argument_spec,
                           supports_check_mode=False)
    result = dict(changed=False)

    # Test if md_toc is installed
    if HAS_MD_TOC is False:
        module.fail_json(msg='Error md_toc is not installed. Please install using pip')

    # If set, parse MD file and store generated TOC
    if (module.params['md_file'] is not None):
        md_file = module.params['md_file']
        skip_lines = module.params['skip_lines'] or 0
        toc_levels = module.params['toc_levels'] or 2
        toc_marker = module.params['toc_marker'] or '<!-- toc -->'

        hash_origin = hashlib.sha224(open(md_file, 'rb').read()).hexdigest()

        toc = md_toc.build_toc(
            filename=md_file, keep_header_levels=toc_levels, skip_lines=skip_lines)
        md_toc.write_string_on_file_between_markers(
            filename=md_file, string=toc, marker=toc_marker)

        hash_final = hashlib.sha224(open(md_file, 'rb').read()).hexdigest()

        result['checksum'] = hash_final
        if hash_final != hash_origin:
            result['changed'] = True

    module.exit_json(**result)


if __name__ == '__main__':
    main()
