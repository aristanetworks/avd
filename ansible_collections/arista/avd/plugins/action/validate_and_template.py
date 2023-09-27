# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible.errors import AnsibleActionFail
from ansible.plugins.action import ActionBase, display

from ansible_collections.arista.avd.plugins.filter.add_md_toc import add_md_toc
from ansible_collections.arista.avd.plugins.plugin_utils.schema.avdschematools import AvdSchemaTools
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get_templar, template


class ActionModule(ActionBase):
    def run(self, tmp=None, task_vars=None):
        if task_vars is None:
            task_vars = {}

        result = super().run(tmp, task_vars)
        del tmp  # tmp no longer has any effect

        # Validate Arguments
        self.templatefile = self._task.args.get("template")
        if not isinstance(self.templatefile, str):
            raise AnsibleActionFail("The argument 'template' must be a string")

        schema = self._task.args.get("schema")
        schema_id = self._task.args.get("schema_id")
        conversion_mode = self._task.args.get("conversion_mode")
        validation_mode = self._task.args.get("validation_mode")

        dest = self._task.args.get("dest")
        if dest is not None and not isinstance(dest, str):
            raise AnsibleActionFail("The argument 'dest' must be a string if set")

        self.add_md_toc = self._task.args.get("add_md_toc", False)
        if not isinstance(self.add_md_toc, bool):
            raise AnsibleActionFail("The argument 'add_md_toc' must be a boolean")

        self.md_toc_skip_lines = self._task.args.get("md_toc_skip_lines", 0)
        if not isinstance(self.md_toc_skip_lines, int):
            raise AnsibleActionFail("The argument 'md_toc_skip_lines' must be an integer")

        # Build data from hostvars and role default vars
        hostname = task_vars["inventory_hostname"]

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

        if not isinstance(task_vars, dict):
            # Corner case for ansible-test where the passed task_vars is a nested chain-map
            task_vars = dict(task_vars)

        # Load schema tools and perform conversion and validation
        avdschematools = AvdSchemaTools(
            hostname=hostname,
            ansible_display=display,
            schema=schema,
            schema_id=schema_id,
            conversion_mode=conversion_mode,
            validation_mode=validation_mode,
            plugin_name=task_vars["ansible_role_name"],
        )
        result.update(avdschematools.convert_and_validate_data(task_vars))

        # Template to file
        # Update result from Ansible "copy" operation (setting 'changed' flag accordingly)
        if not result.get("failed"):
            result.update(self.template(task_vars, dest))

        return result

    def template(self, task_vars, dest):
        # Get updated templar instance to be passed along to our simplified "templater"
        templar = get_templar(self, task_vars)

        output = template(self.templatefile, task_vars, templar)
        if self.add_md_toc:
            output = add_md_toc(output, skip_lines=self.md_toc_skip_lines)

        if dest is None:
            # Return dict with template output in 'output' key for fileless operation
            return {"output": output}

        write_file_result = self.write_file(output, dest, task_vars)

        # Return result with the result from the copy operation
        return write_file_result

    def write_file(self, content, dest, task_vars):
        """
        This function implements the Ansible 'copy' action_module, to benefit from Ansible builtin functionality like 'changed'.
        Reuse task data
        """
        new_task = self._task.copy()
        new_task.args = {
            "dest": dest,
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
