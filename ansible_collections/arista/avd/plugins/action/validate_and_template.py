from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible.errors import AnsibleActionFail
from ansible.plugins.action import ActionBase
from ansible.utils.display import Display

from ansible_collections.arista.avd.plugins.filter.add_md_toc import add_md_toc
from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError
from ansible_collections.arista.avd.plugins.plugin_utils.schema.avdschema import AvdSchema
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get_templar, template

VALID_CONVERSION_MODES = ["disabled", "warning", "info", "debug"]
VALID_VALIDATION_MODES = ["disabled", "error", "warning", "info", "debug"]


class ActionModule(ActionBase):
    def run(self, tmp=None, task_vars=None):
        if task_vars is None:
            task_vars = {}

        result = super().run(tmp, task_vars)
        del tmp  # tmp no longer has any effect

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

        self.conversion_mode = self._task.args.get("conversion_mode", "debug")
        if not isinstance(self.conversion_mode, str):
            raise AnsibleActionFail("The argument 'conversion_mode' must be a string")
        if self.conversion_mode not in VALID_CONVERSION_MODES:
            raise AnsibleActionFail(f"Invalid value '{self.conversion_mode}' for the argument 'conversion_mode'. Must be one of {VALID_CONVERSION_MODES}")

        self.validation_mode = self._task.args.get("validation_mode", "warning")
        if not isinstance(self.validation_mode, str):
            raise AnsibleActionFail("The argument 'validation_mode' must be a string")
        if self.validation_mode not in VALID_VALIDATION_MODES:
            raise AnsibleActionFail(f"Invalid value '{self.validation_mode}' for the argument 'validation_mode'. Must be one of {VALID_VALIDATION_MODES}")

        self.add_md_toc = self._task.args.get("add_md_toc", False)
        if not isinstance(self.add_md_toc, bool):
            raise AnsibleActionFail("The argument 'add_md_toc' must be a boolean")

        self.md_toc_skip_lines = self._task.args.get("md_toc_skip_lines", 0)
        if not isinstance(self.md_toc_skip_lines, int):
            raise AnsibleActionFail("The argument 'md_toc_skip_lines' must be an integer")

        # Build data from hostvars and role default vars
        self.hostname = task_vars["inventory_hostname"]
        self.data = self._templar.template(self._task._role.get_default_vars())
        self.data.update(task_vars["hostvars"].get(self.hostname))

        try:
            self.avd_schema = AvdSchema(schema)
        except Exception as e:
            raise AnsibleActionFail("Invalid Schema supplied to the 'arista.avd.validate_and_template' plugin") from e

        result_messages = []

        # Perform data conversions
        if self.conversion_mode != "disabled":
            self.convert_data(result_messages)

        # Perform validation
        if self.validation_mode != "disabled":
            valid = self.validate_data(result_messages)
            if not valid and self.validation_mode == "error":
                result["failed"] = True

        if result_messages:
            result["msg"] = " ".join(result_messages)

        # Template to file
        # Update result from Ansible "copy" operation (setting 'changed' flag accordingly)
        result.update(self.template(task_vars))

        return result

    def convert_data(self, result_messages):
        """
        Convert data according to the schema (convert_types)

        The data conversion is done in-place (updating the original "data" dict).
        """

        # avd_schema.convert returns a generator, which we need to run over to perform the actual conversions.
        # The returned values are a list of conversion errors
        exceptions = list(self.avd_schema.convert(self.data))
        conversion_counter = self.handle_exceptions(exceptions, self.conversion_mode)
        # This is not yet effective, since the converter does not yield on succesful conversion.
        # TODO: Get converter to return the data that was converted, so the user can see what needs to be updated.
        if conversion_counter:
            result_messages.append(f"{conversion_counter} data conversions done to conform to schema.")
        return

    def validate_data(self, result_messages):
        """
        Validate data according to the schema
        """

        # avd_schema.validate returns a generator, which we need to run over to perform the actual validations.
        # The returned values are a list of validation errors
        exceptions = list(self.avd_schema.validate(self.data))
        validation_counter = self.handle_exceptions(exceptions, self.validation_mode)
        if validation_counter:
            result_messages.append(f"{validation_counter} errors found during schema validation of input vars.")
            return False
        return True

    def handle_exceptions(self, exceptions, mode):
        arista_avd_errors = [exception for exception in exceptions if isinstance(exception, AristaAvdError)]
        for exception in arista_avd_errors:
            message = str.encode(f"[{self.hostname}]: {exception}", "UTF-8")
            if mode == "error":
                Display().error(message, False)
            elif mode == "message":
                Display().display(message, False)
            elif mode == "debug":
                Display(verbosity=1).debug(message, False)
            else:
                # mode == "warning"
                Display().warning(message, False)
        return len(arista_avd_errors)

    def template(self, task_vars):
        # Get updated templar instance to be passed along to our simplified "templater"
        templar = get_templar(self, task_vars)

        output = template(self.templatefile, self.data, templar)
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
