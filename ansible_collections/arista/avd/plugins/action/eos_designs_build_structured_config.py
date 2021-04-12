#!/usr/bin/python
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.plugins.action import ActionBase

class ActionModule(ActionBase):
    def run(self, tmp=None, task_vars=None):
        if task_vars is None:
            task_vars = dict()

        result = super(ActionModule, self).run(tmp, task_vars)
        del tmp  # tmp no longer has any effect

        sc = dict() #short for structured_config
        sc['dc_name'] = task_vars.get('dc_name', '') + "test"
        result['ansible_facts'] = dict(structured_config=sc)
        return result
