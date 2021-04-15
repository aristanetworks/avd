#!/usr/bin/python
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import os
import yaml

from ansible.module_utils.parsing.convert_bool import boolean
from ansible.plugins.action import ActionBase
from ansible.errors import AnsibleError, AnsibleFileNotFound, AnsibleAction, AnsibleActionFail
from ansible.module_utils._text import to_bytes, to_text, to_native
from ansible.utils.vars import isidentifier
from ansible.plugins.filter.core import combine
from ansible.plugins.lookup.template import LookupModule as TemplateLookupModule

class ActionModule(ActionBase):
    def run(self, tmp=None, task_vars=None):
        if task_vars is None:
            task_vars = dict()

        result = super(ActionModule, self).run(tmp, task_vars)
        del tmp  # tmp no longer has any effect

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

        template_vars = task_vars

        for template in template_list:
            if output_var_name:
                template_vars[output_var_name] = output
            else:
                template_vars = combine(task_vars, output, recursive=True)

            #template_output = self.template_light(task_vars, template, template_vars)
            template_lookup_module = TemplateLookupModule(loader=self._loader, templar=self._templar)
            template_output = template_lookup_module.run(template, task_vars, template_vars=template_vars)

            output = combine(output, template_output, recursive=True)

        if output_var_name:
            result['ansible_facts'] = {output_var_name : output}
        else:
            result['ansible_facts'] = output
        return result

    def template_light(self, task_vars, source, template_vars):

        try:
            source = self._find_needle('templates', source)
        except AnsibleError as e:
            raise AnsibleActionFail(to_text(e))

        # Get vault decrypted tmp file
        try:
            tmp_source = self._loader.get_real_file(source)
        except AnsibleFileNotFound as e:
            raise AnsibleActionFail("could not find src=%s, %s" % (source, to_text(e)))
        b_tmp_source = to_bytes(tmp_source, errors='surrogate_or_strict')

        # template the source data locally & get ready to transfer
        try:
            with open(b_tmp_source, 'rb') as f:
                try:
                    template_data = to_text(f.read(), errors='surrogate_or_strict')
                except UnicodeError:
                    raise AnsibleActionFail("Template source files must be utf-8 encoded")

            # set jinja2 internal search path for includes
            searchpath = task_vars.get('ansible_search_path', [])
            searchpath.extend([self._loader._basedir, os.path.dirname(source)])

            # We want to search into the 'templates' subdir of each search path in
            # addition to our original search paths.
            newsearchpath = []
            for p in searchpath:
                newsearchpath.append(os.path.join(p, 'templates'))
                newsearchpath.append(p)
            searchpath = newsearchpath

            #temp_templar = self._templar.copy_with_new_env(searchpath=searchpath, available_variables=template_vars)
            #result = temp_templar.do_template(template_data, preserve_trailing_newlines=True, escape_backslashes=False)

            self._templar.environment.loader.searchpath = searchpath
            old_vars = self._templar.available_variables
            self._templar.available_variables = template_vars
            result = self._templar.do_template(template_data, preserve_trailing_newlines=True, escape_backslashes=False)
            self._templar.available_variables = old_vars

            return yaml.safe_load(result)

        except AnsibleAction:
            raise
        except Exception as e:
            raise AnsibleActionFail("%s: %s" % (type(e).__name__, to_text(e)))
