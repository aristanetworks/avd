#!/usr/bin/python
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import yaml

from ansible.plugins.action import ActionBase
from ansible.errors import AnsibleAction, AnsibleActionFail
from ansible.utils.vars import isidentifier
from ansible.plugins.filter.core import combine
from ansible.plugins.lookup.template import LookupModule as TemplateLookupModule

class ActionModule(ActionBase):
    def run(self, tmp=None, task_vars=None):
        if task_vars is None:
            task_vars = dict()

        result = super(ActionModule, self).run(tmp, task_vars)
        del tmp  # tmp no longer has any effect

        output_var_name = ""

        if self._task.args:
            if "name" in self._task.args:
                n = self._task.args.get("name")
                n = self._templar.template(n)
                if not isidentifier(n):
                    raise AnsibleActionFail("The variable name '%s' is not valid. Variables must start with a letter or underscore character, "
                                            "and contain only letters, numbers and underscores." % n)
                output_var_name = n

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
            if output_var_name:
                template_vars[output_var_name] = output
            else:
                template_vars = combine(task_vars, output, recursive=True)

            template_output = template_lookup_module.run([template], template_vars)
            template_output_data = yaml.safe_load(template_output[0])
            if template_output_data:
                output = combine(output, template_output_data, recursive=True)

        if output_var_name:
            result['ansible_facts'] = {output_var_name : output}
        else:
            result['ansible_facts'] = output
        return result
