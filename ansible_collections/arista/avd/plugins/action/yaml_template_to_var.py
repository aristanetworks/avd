#!/usr/bin/python
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import yaml

from ansible.plugins.action import ActionBase
from ansible.errors import AnsibleAction, AnsibleActionFail
from ansible.utils.vars import isidentifier
from ansible.plugins.filter.core import combine
from ansible.plugins.lookup.template import LookupModule as TemplateLookupModule

ANSIBLE_METADATA = {'metadata_version': '1.0.0',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = r'''
---
module: configlet_build_config
version_added: "1.0.0"
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
# tasks file for configlet_build_config
- name: generate intented variables
  tags: [build, provision]
  configlet_build_config:
    configlet_dir: '/path/to/configlets/folder/'
    configlet_prefix: 'AVD_'
    configlet_extension: 'cfg'
'''

class ActionModule(ActionBase):
    def run(self, tmp=None, task_vars=None):
        if task_vars is None:
            task_vars = dict()

        result = super().run(tmp, task_vars)
        del tmp  # tmp no longer has any effect

        root_key = ""

        if self._task.args:
            if "root_key" in self._task.args:
                n = self._task.args.get("root_key")
                n = self._templar.template(n)
                if not isidentifier(n):
                    raise AnsibleActionFail("The root_key '%s' is not valid. Keys must start with a letter or underscore character, "
                                            "and contain only letters, numbers and underscores." % n)
                root_key = n

            if "yaml_templates" in self._task.args:
                template_list = list(self._task.args.get("yaml_templates"))
            else:
                raise AnsibleActionFail("The variable 'yaml_templates' is missing")
        else:
            raise AnsibleActionFail("The variable 'yaml_templates' is missing")

        output = dict()

        template_lookup_module = TemplateLookupModule(loader=self._loader, templar=self._templar)

        template_vars = task_vars

        for template in template_list:
            if root_key:
                template_vars[root_key] = output
            else:
                template_vars = combine(task_vars, output, recursive=True)

            template_output = template_lookup_module.run([template], template_vars)
            template_output_data = yaml.safe_load(template_output[0])
            if template_output_data:
                output = combine(output, template_output_data, recursive=True, list_merge='append')

        if root_key:
            result['ansible_facts'] = {root_key : output}
        else:
            result['ansible_facts'] = output
        return result
