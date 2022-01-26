from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import yaml
from ansible.plugins.action import ActionBase
from ansible.errors import AnsibleActionFail
from ansible.utils.vars import isidentifier
from ansible.plugins.filter.core import combine
from ansible.plugins.loader import lookup_loader
from ansible_collections.arista.avd.plugins.module_utils.strip_empties import strip_null_from_data
from datetime import datetime
import yaml


class ActionModule(ActionBase):
    def run(self, tmp=None, task_vars=None):
        if task_vars is None:
            task_vars = {}

        result = super().run(tmp, task_vars)
        del tmp  # tmp no longer has any effect

        root_key = ""

        if self._task.args:
            if "root_key" in self._task.args:
                n = self._task.args.get("root_key")
                n = self._templar.template(n)
                if not isidentifier(n):
                    raise AnsibleActionFail(f"The argument 'root_key' value of '{n}' is not valid. Keys must start with a letter or underscore character, "
                                            "and contain only letters, numbers and underscores.")
                root_key = n

            if "templates" in self._task.args:
                t = self._task.args.get("templates")
                if isinstance(t, list):
                    template_list = t
                else:
                    raise AnsibleActionFail("The argument 'templates' is not a list")
            else:
                raise AnsibleActionFail("The argument 'templates' must be set")

            output_filename = self._task.args.get("output_filename",False)
            output_format = self._task.args.get("output_format","json")
            template_output = self._task.args.get("template_output",False)
            debug = self._task.args.get("debug",False)

        else:
            raise AnsibleActionFail("The argument 'templates' must be set")

        output = {}

        template_lookup_module = lookup_loader.get('ansible.builtin.template', loader=self._loader, templar=self._templar)

        template_vars = task_vars

        if debug:
            avd_yaml_templates_to_facts_debug = template_vars.get('avd_yaml_templates_to_facts_debug',[])

        for template_item in template_list:
            if debug:
                debug_item = template_item
                debug_item['timestamps'] = { "starting": datetime.now() }

            template = template_item.get('template')
            if not template:
                raise AnsibleActionFail("Invalid template data")

            template_options = template_item.get('options', {})
            list_merge = template_options.get('list_merge', 'append')

            strip_empty_keys = template_options.get('strip_empty_keys', True)

            if root_key:
                template_vars[root_key] = output
            else:
                template_vars = combine(task_vars, output, recursive=True)

            if debug:
                debug_item['timestamps']['run_template'] = datetime.now()

            template_result = template_lookup_module.run([template], template_vars)
            if debug:
                debug_item['timestamps']['load_yaml'] = datetime.now()

            template_result_data = yaml.safe_load(template_result[0])

            if strip_empty_keys:
                if debug:
                    debug_item['timestamps']['strip_empty_keys'] = datetime.now()

                template_result_data = strip_null_from_data(template_result_data)

            if template_result_data:
                if debug:
                    debug_item['timestamps']['combine_data'] = datetime.now()

                output = combine(output, template_result_data, recursive=True, list_merge=list_merge)

            if debug:
                debug_item['timestamps']['done'] = datetime.now()
                avd_yaml_templates_to_facts_debug.append(debug_item)

        if template_output:
            if debug:
                debug_item = { 'action': 'template_output', 'timestamps': { 'combine_data': datetime.now() } }

            if root_key:
                template_vars[root_key] = output
            else:
                template_vars = combine(task_vars, output, recursive=True)

            if debug:
                debug_item['timestamps']['templating'] = datetime.now()

            self._templar.available_variables = template_vars
            output = self._templar.template(output)

            if debug:
                debug_item['timestamps']['done'] = datetime.now()
                avd_yaml_templates_to_facts_debug.append(debug_item)

        if output_filename:
            if debug:
                debug_item = {
                    'action': 'output_filename',
                    'output_filename': output_filename,
                    'output_format': output_format,
                    'timestamps': {
                        'write_file': datetime.now()
                    }
                }

            if output_format in ["yml", "yaml"] :
                write_file_result = self.write_file(yaml.dump(output, indent=2, sort_keys=False, width=130), output_filename, task_vars)
            else:
                write_file_result = self.write_file(output, output_filename, task_vars)

            result.update(write_file_result)

            if debug:
                debug_item['timestamps']['done'] = datetime.now()
                avd_yaml_templates_to_facts_debug.append(debug_item)

        if debug:
            output['avd_yaml_templates_to_facts_debug'] = avd_yaml_templates_to_facts_debug

        if root_key:
            result['ansible_facts'] = {root_key: output}
        else:
            result['ansible_facts'] = output
        return result

    def write_file(self, content, filename, task_vars):
        new_task = self._task.copy()
        # remove 'yaml_templates_to_facts' options:
        for remove in ('root_key', 'templates', 'output_filename', 'output_format', 'template_output', 'debug'):
            new_task.args.pop(remove, None)

        new_task.args['content'] = content
        new_task.args['dest'] = filename

        copy_action = self._shared_loader_obj.action_loader.get('ansible.legacy.copy',
                                                                task=new_task,
                                                                connection=self._connection,
                                                                play_context=self._play_context,
                                                                loader=self._loader,
                                                                templar=self._templar,
                                                                shared_loader_obj=self._shared_loader_obj)

        return copy_action.run(task_vars=task_vars)
