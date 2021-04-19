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
                    raise AnsibleActionFail("The argument 'root_key' value of '%s' is not valid. Keys must start with a letter or underscore character, "
                                            "and contain only letters, numbers and underscores." % n)
                root_key = n

            if "templates" in self._task.args:
                template_list = list(self._task.args.get("templates"))
            else:
                raise AnsibleActionFail("The argument 'templates' must be set")
        else:
            raise AnsibleActionFail("The argument 'templates' must be set")

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
            template_output_data = strip_null_from_output(template_output_data)
            if template_output_data:
                output = combine(output, template_output_data, recursive=True, list_merge='append')

        if root_key:
            result['ansible_facts'] = {root_key: output}
        else:
            result['ansible_facts'] = output
        return result


def strip_null_from_output(data):
    strip_values_tuple = (None,)
    if isinstance(data, dict):
        return strip_empties_from_dict(data, strip_values_tuple)
    elif isinstance(data, list):
        return strip_empties_from_list(data, strip_values_tuple)
    return data


def strip_empties_from_list(data, strip_values_tuple=(None, str(), list(), dict(),)):
    new_data = []
    for v in data:
        if isinstance(v, dict):
            v = strip_empties_from_dict(v, strip_values_tuple)
        elif isinstance(v, list):
            v = strip_empties_from_list(v, strip_values_tuple)
        if v not in strip_values_tuple:
            new_data.append(v)
    return new_data


def strip_empties_from_dict(data, strip_values_tuple=(None, str(), list(), dict(),)):
    new_data = {}
    for k, v in data.items():
        if isinstance(v, dict):
            v = strip_empties_from_dict(v, strip_values_tuple)
        elif isinstance(v, list):
            v = strip_empties_from_list(v, strip_values_tuple)
        if v not in strip_values_tuple:
            new_data[k] = v
    return new_data
