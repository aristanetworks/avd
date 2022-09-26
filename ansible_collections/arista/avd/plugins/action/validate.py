from __future__ import absolute_import, division, print_function

__metaclass__ = type

import copy

from ansible.errors import AnsibleActionFail
from ansible.plugins.action import ActionBase
from ansible.utils.display import Display

from ansible_collections.arista.avd.plugins.plugin_utils.schema.avdschema import AristaAvdError, AvdSchema

VALID_CONVERSION_MODES = ["disabled", "warning", "info", "debug"]
VALID_VALIDATION_MODES = ["disabled", "error", "warning", "info", "debug"]


class ActionModule(ActionBase):
    def run(self, tmp=None, task_vars=None):
        if task_vars is None:
            task_vars = {}

        result = super().run(tmp, task_vars)
        del tmp  # tmp no longer has any effect

        # ########
        # VALIDATE ARGUMENTS
        if self._task.args and "schema" in self._task.args:
            schema = self._task.args["schema"]
            if not isinstance(schema, dict):
                raise AnsibleActionFail("The argument 'schema' is not a dict")
        else:
            raise AnsibleActionFail("The argument 'schema' must be set")

        conversion_mode = self._task.args.get("conversion_mode", "debug")
        if not isinstance(conversion_mode, str):
            raise AnsibleActionFail("The argument 'conversion_mode' must be a string")
        if conversion_mode not in VALID_CONVERSION_MODES:
            raise AnsibleActionFail(f"Invalid value '{conversion_mode}' for the argument 'conversion_mode'.Must be one of {VALID_CONVERSION_MODES}")

        validation_mode = self._task.args.get("validation_mode", "warning")
        if not isinstance(validation_mode, str):
            raise AnsibleActionFail("The argument 'validation_mode' must be a string")
        if validation_mode not in VALID_VALIDATION_MODES:
            raise AnsibleActionFail(f"Invalid value '{validation_mode}' for the argument 'validation_mode'.Must be one of {VALID_VALIDATION_MODES}")

        # ########
        # BUILD DATA FROM HOSTVARS AND DEFAULT_VARS
        hostname = task_vars["inventory_hostname"]
        data = self._templar.template(self._task._role.get_default_vars())
        data.update(task_vars["hostvars"].get(hostname))

        try:
            avd_schema = AvdSchema(schema)
        except Exception as e:
            raise AnsibleActionFail("Invalid Schema supplied to the arista.avd.validate plugin") from e

        # ########
        # PERFORM CONVERSION
        result_messages = []

        if conversion_mode != "disabled":
            # auto-convert data according to schema (convert_types)
            preconversion_data = copy.deepcopy(data)
            # The convert_data performs in-place updates of the data.
            exceptions = self.convert_data(data, avd_schema)
            conversion_counter = self.handle_exceptions(exceptions, conversion_mode, hostname)
            if data != preconversion_data:
                # Idempotency checks fail when we set the changed flag on auto upgrade.
                # Uncomment this when all data models and molecule tests have been updated.
                # result['changed'] = True
                result.setdefault("ansible_facts", {})
                for key, value in data.items():
                    if key not in preconversion_data or value != preconversion_data[key]:
                        result["ansible_facts"][key] = value
            if conversion_counter:
                result_messages.append(f"{conversion_counter} conversions done. Check converted facts with -v or -vvv.")

        # ########
        # PERFORM VALIDATION
        if validation_mode != "disabled":
            # perform schema validation according to schema
            exceptions = self.validate_data(data, avd_schema)
            validation_counter = self.handle_exceptions(exceptions, validation_mode, hostname)
            if validation_counter and validation_mode == "error":
                result["failed"] = True
            if validation_counter:
                result_messages.append(f"{validation_counter} errors found during schema validation of input vars.")

        # ########
        # RETURN RESULTS
        if result_messages:
            result["msg"] = " ".join(result_messages)

        return result

    def convert_data(self, data, avd_schema):
        # avd_schema.convert returns a generator, which we need to run over to perform the actual conversions.
        # The data conversion is done in-place (updating the original "data" dict).
        # The returned values are a list of validation errors
        return list(avd_schema.convert(data))

    def validate_data(self, data, avd_schema):
        # avd_schema.validate returns a generator, which we need to run over to perform the actual validations.
        # The returned values are a list of validation errors
        return list(avd_schema.validate(data))

    def handle_exceptions(self, exceptions, mode, hostname):
        arista_avd_errors = [exception for exception in exceptions if isinstance(exception, AristaAvdError)]
        for exception in arista_avd_errors:
            message = str.encode(f"[{hostname}]: {exception}", "UTF-8")
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
