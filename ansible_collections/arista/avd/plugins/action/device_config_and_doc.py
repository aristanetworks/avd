# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import absolute_import, division, print_function

from pathlib import Path

from ansible_collections.arista.avd.plugins.filter.add_md_toc import add_md_toc
from ansible_collections.arista.avd.plugins.plugin_utils.utils.get import get

__metaclass__ = type

import cProfile
import json
import logging
import pstats

from ansible.errors import AnsibleActionFail
from ansible.plugins.action import ActionBase, display

from ansible_collections.arista.avd.plugins.plugin_utils.schema.avdschematools import AvdSchemaTools
from ansible_collections.arista.avd.plugins.plugin_utils.strip_empties import strip_empties_from_dict
from ansible_collections.arista.avd.plugins.plugin_utils.utils import PythonToAnsibleHandler, get_templar, template

try:
    from pyavd import get_device_config, get_device_doc
    from pyavd.utils.read_vars import read_vars

    HAS_PYAVD = True
except ImportError:
    HAS_PYAVD = False

CUSTOM_TEMPLATES_CFG_TEMPLATE = "eos/custom-templates.j2"
CUSTOM_TEMPLATES_DOC_TEMPLATE = "documentation/custom-templates.j2"

LOGGER = logging.getLogger("ansible_collections.arista.avd")
LOGGING_LEVELS = ["DEBUG", "INFO", "ERROR", "WARNING", "CRITICAL"]

ARGUMENT_SPEC = {
    "structured_config_filename": {"type": "str", "required": True},
    "config_filename": {"type": "str", "required": True},
    "documentation_filename": {"type": "str", "required": True},
    "read_structured_config_from_file": {"type": "bool", "default": True},
    "conversion_mode": {"type": "str", "default": "debug"},
    "validation_mode": {"type": "str", "default": "warning"},
    "generate_device_doc": {"type": "bool", "default": True},
    "device_doc_toc": {"type": "bool", "default": True},
    "cprofile_file": {"type": "str"},
}


class ActionModule(ActionBase):
    def run(self, tmp=None, task_vars=None):
        if task_vars is None:
            task_vars = {}

        if not HAS_PYAVD:
            raise AnsibleActionFail("The Python library 'pyavd' was not found. Install using 'pip3 install'.")

        result = super().run(tmp, task_vars)
        del tmp  # tmp no longer has any effect

        cprofile_file = self._task.args.get("cprofile_file")
        if cprofile_file:
            profiler = cProfile.Profile()
            profiler.enable()

        # Setup module logging
        setup_module_logging(result)

        result = self.main(task_vars, result)

        if cprofile_file:
            profiler.disable()
            stats = pstats.Stats(profiler).sort_stats("cumtime")
            stats.dump_stats(cprofile_file)

        return result

    def main(self, task_vars: dict, result: dict) -> dict:
        validated_args = self.validate_args()

        try:
            # Read structured config from file or task_vars and run templating to handle inline jinja.
            task_vars = self.prepare_task_vars(task_vars, validated_args["structured_config_filename"], validated_args["read_structured_config_from_file"])

            # Load schema tools and perform conversion and validation
            avdschematools = AvdSchemaTools(
                hostname=task_vars["inventory_hostname"],
                ansible_display=display,
                schema_id="eos_cli_config_gen",
                conversion_mode=validated_args["conversion_mode"],
                validation_mode=validated_args["validation_mode"],
                plugin_name="device_config_and_doc",
            )
            result.update(avdschematools.convert_and_validate_data(task_vars))

            if result.get("failed"):
                return result

            has_custom_templates = bool(task_vars.get("custom_templates"))

            device_config = get_device_config(task_vars)

            if has_custom_templates:
                device_config += self.render_template_with_ansible_templar(task_vars, CUSTOM_TEMPLATES_CFG_TEMPLATE)

            if get(task_vars, "generate_default_config") is not False:
                device_config += "!\nend\n"

            result["changed"] = self.write_file(device_config, validated_args["config_filename"])

            if validated_args["generate_device_doc"]:
                device_doc = get_device_doc(task_vars, add_md_toc=False)

                if has_custom_templates:
                    device_doc += self.render_template_with_ansible_templar(task_vars, CUSTOM_TEMPLATES_DOC_TEMPLATE)

                if validated_args["device_doc_toc"]:
                    device_doc = add_md_toc(device_doc, skip_lines=3)

                file_changed = self.write_file(device_doc, validated_args["documentation_filename"])
                result["changed"] = result["changed"] or file_changed

        except Exception as error:
            # Recast errors as AnsibleActionFail
            msg = f"Error during plugin execution: {error}"
            raise AnsibleActionFail(msg) from error

        return result

    def validate_args(self) -> dict:
        # Get task arguments and validate them
        validated_args = strip_empties_from_dict(self._task.args)
        validation_result, validated_args = self.validate_argument_spec(ARGUMENT_SPEC)
        validated_args = strip_empties_from_dict(validated_args)

        # Converting to json and back to remove any AnsibeUnsafe types
        return json.loads(json.dumps(validated_args))

    def prepare_task_vars(self, task_vars: dict, structured_config_filename: str, read_structured_config_from_file: bool):
        if read_structured_config_from_file:
            task_vars.update(read_vars(structured_config_filename))

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

        return task_vars

    def render_template_with_ansible_templar(self, task_vars: dict, templatefile: str) -> str:
        # Get updated templar instance to be passed along to our simplified "templater"
        if not hasattr(self, "ansible_templar"):
            self.ansible_templar = get_templar(self, task_vars)

        return template(templatefile, task_vars, self.ansible_templar)

    def write_file(self, content: str, filename: str) -> bool:
        """
        This function writes the file only if the content has changed.

        Returns <bool> to indicate if file was changed.
        """
        path = Path(filename)
        if path.exists():
            if path.read_text(encoding="UTF-8") == content:
                return False

        else:
            # Create parent dirs automatically.
            path.parent.mkdir(mode=0o775, parents=True, exist_ok=True)
            # Touch file
            path.touch(mode=0o664)

        path.write_text(content, encoding="UTF-8")
        return True


def setup_module_logging(result: dict) -> None:
    """
    Add a Handler to copy the logs from the plugin into Ansible output based on their level

    Parameters:
        result: The dictionary used for the ansible module results
    """
    python_to_ansible_handler = PythonToAnsibleHandler(result, display)
    LOGGER.addHandler(python_to_ansible_handler)
    # TODO mechanism to manipulate the logger globally for pyavd
    # Keep debug to be able to see logs with `-v` and `-vvv`
    LOGGER.setLevel(logging.DEBUG)
