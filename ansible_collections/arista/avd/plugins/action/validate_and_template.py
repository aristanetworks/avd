from __future__ import absolute_import, division, print_function

__metaclass__ = type

from cProfile import Profile
from pstats import Stats

from ansible.errors import AnsibleActionFail
from ansible.plugins.action import ActionBase, display

from ansible_collections.arista.avd.plugins.filter.add_md_toc import add_md_toc
from ansible_collections.arista.avd.plugins.plugin_utils.schema.avdschematools import AvdSchemaTools
from ansible_collections.arista.avd.plugins.plugin_utils.utils import compile_searchpath, template


class ActionModule(ActionBase):
    def run(self, tmp=None, task_vars=None):
        if task_vars is None:
            task_vars = {}

        result = super().run(tmp, task_vars)
        del tmp  # tmp no longer has any effect

        cprofile_file = self._task.args.get("cprofile_file")
        if cprofile_file:
            profiler = Profile()
            profiler.enable()

        # Validate Arguments
        if self._task.args and "schema" in self._task.args and "template" in self._task.args:
            self.templatefile = self._task.args["template"]
            if not isinstance(self.templatefile, str):
                raise AnsibleActionFail("The argument 'template' must be a string")
            self.dest = self._task.args["dest"]
            if not isinstance(self.dest, str):
                raise AnsibleActionFail("The argument 'dest' must be a string")
            schema = self._task.args["schema"]
            if not isinstance(schema, dict):
                raise AnsibleActionFail("The argument 'schema' must be a dict")
        else:
            raise AnsibleActionFail("The arguments 'template', 'dest' and 'schema' must be set")

        conversion_mode = self._task.args.get("conversion_mode")
        validation_mode = self._task.args.get("validation_mode")

        self.add_md_toc = self._task.args.get("add_md_toc", False)
        if not isinstance(self.add_md_toc, bool):
            raise AnsibleActionFail("The argument 'add_md_toc' must be a boolean")

        self.md_toc_skip_lines = self._task.args.get("md_toc_skip_lines", 0)
        if not isinstance(self.md_toc_skip_lines, int):
            raise AnsibleActionFail("The argument 'md_toc_skip_lines' must be an integer")

        # Build data from hostvars and role default vars
        hostname = task_vars["inventory_hostname"]
        self.data = self._templar.template(self._task._role.get_default_vars())
        self.data.update(task_vars["hostvars"].get(hostname))

        # Load schema tools
        avdschematools = AvdSchemaTools(schema, hostname, display, conversion_mode, validation_mode)

        result_messages = []

        # Perform data conversions
        result_messages.extend(avdschematools.convert_data(self.data))

        # Perform validation
        validation_messages = avdschematools.validate_data(self.data)
        if validation_messages:
            result_messages.extend(validation_messages)
            if validation_mode == "error":
                result["failed"] = True

        if result_messages:
            result["msg"] = " ".join(result_messages)

        # Template to file
        # Update result from Ansible "copy" operation (setting 'changed' flag accordingly)
        if not result.get("failed"):
            result.update(self.template(task_vars))

        if cprofile_file:
            profiler.disable()
            stats = Stats(profiler).sort_stats("cumtime")
            stats.dump_stats(cprofile_file)

        return result

    def template(self, task_vars):
        searchpath = compile_searchpath(task_vars.get("ansible_search_path"))
        templar = self._templar.copy_with_new_env(searchpath=searchpath, available_variables={})
        output = template(self.templatefile, self.data, templar, searchpath)
        if self.add_md_toc:
            output = add_md_toc(output, skip_lines=self.md_toc_skip_lines)

        write_file_result = self.write_file(output, task_vars)

        # Return result with the result from the copy operation
        return write_file_result

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
