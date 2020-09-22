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
module: configlet_build_config
version_added: "2.9"
author: EMEA AS Team (@aristanetworks)
short_description: Build arista.cvp.configlet configuration.
description:
  - Build configuration to publish configlets on Cloudvision.
options:
  configlet_dir:
    description: Directory where configlets are located.
    required: true
    type: str
  configlet_prefix:
    description: Prefix to append on configlet.
    required: true
    type: str
  destination:
    description: File where to save information.
    required: false
    type: str
    default: ''
  configlet_extension:
    description: File extensio to look for.
    required: false
    type: str
    default: 'conf'
'''

EXAMPLES = r'''
# tasks file for cvp_configlet_upload
- name: generate intented variables
  tags: [build, provision]
  configlet_build_config:
    configlet_dir: '{{ configlet_dir }}'
    configlet_prefix: '{{ configlets_prefix }}'
    configlet_extension: '{{configlet_extension}}'
'''

import glob
import os
import traceback
from ansible.module_utils.basic import AnsibleModule
YAML_IMP_ERR = None
try:
    import yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False
    YAML_IMP_ERR = traceback.format_exc()


def get_configlet(src_folder=str(), prefix='AVD', extension='cfg'):
    """
    Get available configlets to deploy to CVP.

    Parameters
    ----------
    src_folder : str, optional
        Path where to find configlet, by default str()
    prefix : str, optional
        Prefix to append to configlet name, by default 'AVD'
    extension : str, optional
        File extension to lookup configlet file, by default 'cfg'

    Returns
    -------
    dict
        Dictionary of configlets found in source folder.
    """
    src_configlets = glob.glob(src_folder + '/*.' + extension)
    configlets = dict()
    for file in src_configlets:
        if prefix != 'none':
            name = prefix + '_' + os.path.splitext(os.path.basename(file))[0]
        else:
            name = os.path.splitext(os.path.basename(file))[0]
        with open(file, 'r') as file:
            data = file.read()
        configlets[name] = data
    return configlets


def main():
    """ Main entry point for module execution."""
    argument_spec = dict(
        configlet_dir=dict(type='str', required=True),
        configlet_prefix=dict(type='str', required=True),
        configlet_extension=dict(type='str', required=False, default='conf'),
        destination=dict(type='str', required=False, default=None)
    )

    module = AnsibleModule(argument_spec=argument_spec,
                           supports_check_mode=False)
    result = dict(changed=False)

    # If set, build configlet topology
    if module.params['configlet_dir'] is not None:
        result['CVP_CONFIGLETS'] = get_configlet(src_folder=module.params['configlet_dir'],
                                                 prefix=module.params['configlet_prefix'],
                                                 extension=module.params['configlet_extension'])

    # Write vars to file if set by user
    if module.params['destination'] is not None:
        with open(module.params['destination'], 'w') as file:
            yaml.dump(result, file)

    module.exit_json(**result)


if __name__ == '__main__':
    main()
