# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import absolute_import, division, print_function

__metaclass__ = type

import cProfile
import pstats
from collections import ChainMap

import yaml
from ansible.errors import AnsibleActionFail
from ansible.parsing.yaml.dumper import AnsibleDumper
from ansible.plugins.action import ActionBase, display

from ansible_collections.arista.avd.plugins.plugin_utils.merge import merge
from ansible_collections.arista.avd.plugins.plugin_utils.schema.avdschematools import AvdSchemaTools
from ansible_collections.arista.avd.plugins.plugin_utils.strip_empties import strip_null_from_data
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get, get_templar
from ansible_collections.arista.avd.plugins.plugin_utils.utils import template as templater
from ansible_collections.arista.avd.roles.eos_designs.python_modules.get_structured_config import get_structured_config


class ActionModule(ActionBase):
    def run(self, tmp=None, task_vars=None):
        if task_vars is None:
            task_vars = {}

        result = super().run(tmp, task_vars)
        del tmp  # tmp no longer has any effect

        cprofile_file = self._task.args.get("cprofile_file")
        if cprofile_file:
            profiler = cProfile.Profile()
            profiler.enable()

        eos_designs_custom_templates = self._task.args.get("eos_designs_custom_templates", [])
        self.dest = self._task.args.get("dest", False)
        template_output = self._task.args.get("template_output", False)
        conversion_mode = self._task.args.get("conversion_mode")
        validation_mode = self._task.args.get("validation_mode")

        hostname = task_vars["inventory_hostname"]

        task_vars["switch"] = get(task_vars, f"avd_switch_facts..{hostname}..switch", separator="..", default={})

        # Read ansible variables and perform templating to support inline jinja2
        for var in task_vars:
            if str(var).startswith(("ansible", "molecule", "hostvars", "vars", "avd_switch_facts")):
                continue
            if self._templar.is_template(task_vars[var]):
                # Var contains a jinja2 template.
                try:
                    task_vars[var] = self._templar.template(task_vars[var], fail_on_undefined=False)
                except Exception as e:
                    raise AnsibleActionFail(f"Exception during templating of task_var '{var}'") from e

        # Get updated templar instance to be passed along to our simplified "templater"
        self.templar = get_templar(self, task_vars)

        # Load schema tools for input schema
        input_schema_tools = AvdSchemaTools(
            hostname=hostname,
            ansible_display=display,
            schema_id="eos_designs",
            conversion_mode=conversion_mode,
            validation_mode=validation_mode,
            plugin_name="arista.avd.eos_designs",
        )

        # Load schema tools for output schema
        output_schema_tools = AvdSchemaTools(
            hostname=hostname,
            ansible_display=display,
            schema_id="eos_cli_config_gen",
            conversion_mode=conversion_mode,
            validation_mode=validation_mode,
            plugin_name="arista.avd.eos_cli_config_gen",
        )

        # Get Structured Config from builtin eos_designs python_modules
        try:
            output = get_structured_config(
                vars=dict(task_vars),
                input_schema_tools=input_schema_tools,
                output_schema_tools=output_schema_tools,
                result=result,
                templar=self.templar,
            )
        except Exception as error:
            raise AnsibleActionFail(message=str(error)) from error

        if result.get("failed"):
            # Something failed in schema validation or conversion.
            return result

        # We use ChainMap to avoid copying large amounts of data around, mapping in
        #  - output (containing structured_config at this point)
        #  - templated, converted and validated version of all other vars
        # Any var assignments will end up in output, so all other objects are protected.
        template_vars = ChainMap(output, task_vars)

        # eos_designs_custom_templates can contain a list of jinja templates to run after the builtin eos_designs python_modules
        for template_item in eos_designs_custom_templates:
            template_options = template_item.get("options", {})
            list_merge = template_options.get("list_merge", "append_rp")
            strip_empty_keys = template_options.get("strip_empty_keys", True)
            template = template_item["template"]

            # Here we parse the template, expecting the result to be a YAML formatted string
            template_result = templater(template, template_vars, self.templar)

            # Load data from the template result.
            template_result_data = yaml.safe_load(template_result)

            # If the argument 'strip_empty_keys' is set, remove keys with value of null / None from the resulting dict (recursively).
            if strip_empty_keys:
                template_result_data = strip_null_from_data(template_result_data)

            # If there is any data produced by the template, convert and merge it on top of previous output.
            if template_result_data:
                # Some templates return a list of dicts, others only return a dict. Here we normalize to list.
                if not isinstance(template_result_data, list):
                    template_result_data = [template_result_data]

                try:
                    merge(output, *template_result_data, list_merge=list_merge, schema=output_schema_tools.avdschema)
                except Exception as error:
                    raise AnsibleActionFail(message=str(error)) from error

        # If the argument 'template_output' is set, run the output data through another jinja2 rendering.
        # This is to resolve any input values with inline jinja using variables/facts set by the input templates.
        if template_output:
            with self._templar.set_temporary_context(available_variables=template_vars):
                output = self._templar.template(output, fail_on_undefined=False)

        # If the argument 'dest' is set, write the output data to a file.
        if self.dest:
            # Depending on the file suffix of 'dest' (default: 'json') we will format the data to yaml or just write the output data directly.
            # The Copy module used in 'write_file' will convert the output data to json automatically.
            if self.dest.split(".")[-1] in ["yml", "yaml"]:
                write_file_result = self.write_file(yaml.dump(output, Dumper=AnsibleDumper, indent=2, sort_keys=False, width=130), task_vars)
            else:
                write_file_result = self.write_file(output, task_vars)

            # Overwrite result with the result from the copy operation (setting 'changed' flag accordingly)
            result.update(write_file_result)

        # If 'dest' is not set, hardcode 'changed' to true, since we don't know if something changed and later tasks may depend on this.
        else:
            result["changed"] = True

        result["ansible_facts"] = output
        result["ansible_facts"]["switch"] = task_vars.get("switch")

        if cprofile_file:
            profiler.disable()
            stats = pstats.Stats(profiler).sort_stats("cumtime")
            stats.dump_stats(cprofile_file)

        return result

    def write_file(self, content, task_vars):
        """
        This function implements the Ansible 'copy' action_module, to benefit from Ansible builtin functionality like 'changed'.
        Reuse task data
        """
        new_task = self._task.copy()
        new_task.args = {
            "dest": self.dest,
            "mode": self._task.args.get("mode"),
            "content": content,
        }

        copy_action = self._shared_loader_obj.action_loader.get(
            "ansible.legacy.copy",
            task=new_task,
            connection=self._connection,
            play_context=self._play_context,
            loader=self._loader,
            templar=self._templar,
            shared_loader_obj=self._shared_loader_obj,
        )

        return copy_action.run(task_vars=task_vars)
