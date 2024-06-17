# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import absolute_import, division, print_function

__metaclass__ = type

import json
import logging
from functools import partial
from pathlib import Path

import yaml
from ansible.errors import AnsibleActionFail
from ansible.plugins.action import ActionBase, display

from ansible_collections.arista.avd.plugins.plugin_utils.strip_empties import strip_empties_from_dict
from ansible_collections.arista.avd.plugins.plugin_utils.utils import PythonToAnsibleContextFilter, PythonToAnsibleHandler, cprofile, get_templar, template

try:
    from yaml import CLoader as YamlLoader
except ImportError:
    from yaml import YamlLoader

try:
    from pyavd import get_device_config, get_device_doc, validate_structured_config
    from pyavd.j2filters.add_md_toc import add_md_toc

    HAS_PYAVD = True
except ImportError:
    HAS_PYAVD = False


CUSTOM_TEMPLATES_CFG_TEMPLATE = "eos/custom-templates.j2"
CUSTOM_TEMPLATES_DOC_TEMPLATE = "documentation/custom-templates.j2"

LOGGER = logging.getLogger("ansible_collections.arista.avd")
# Avoid duplicate logs in debug files
LOGGER.propagate = False

# Trying stuff - probably need to go in another PR
setattr(LOGGER, "vv", partial(LOGGER.log, 19))
setattr(LOGGER, "vvv", partial(LOGGER.log, 18))
setattr(LOGGER, "vvvv", partial(LOGGER.log, 17))
setattr(LOGGER, "vvvvv", partial(LOGGER.log, 16))
setattr(LOGGER, "vvvvvv", partial(LOGGER.log, 15))

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
    """Action Module for eos_cli_config_gen."""

    @cprofile()
    def run(self, tmp=None, task_vars=None):
        """Ansible Action entry point."""
        if task_vars is None:
            task_vars = {}

        if not HAS_PYAVD:
            raise AnsibleActionFail("The Python library 'pyavd' was not found. Install using 'pip3 install'.")

        result = super().run(tmp, task_vars)
        del tmp  # tmp no longer has any effect

        # Setup module logging
        hostname = task_vars["inventory_hostname"]
        setup_module_logging(hostname, result)

        result = self.main(task_vars, result)

        return result

    def main(self, task_vars: dict, result: dict) -> dict:
        """Main function in charge of validating the input variables and generating the device configuration and documentation."""
        LOGGER.vvvv("Validating task arguments...")
        validated_args = self.validate_args()
        LOGGER.vvvv("Validating task arguments [done].")

        try:
            # Read structured config from file or task_vars and run templating to handle inline jinja.
            LOGGER.info("Preparing task vars...")
            task_vars = self.prepare_task_vars(
                task_vars, validated_args["structured_config_filename"], read_structured_config_from_file=validated_args["read_structured_config_from_file"]
            )
            LOGGER.info("Preparing task vars [done].")

            LOGGER.info("Validating structured configuration...")
            validation_result = validate_structured_config(task_vars)
            LOGGER.info("Validating structured configuration [done].")
        except Exception as e:
            LOGGER.error(e)
            return result

        if validation_result.failed:
            # TODO nicer logging for validation_errors and probably can be written in a better way.
            validation_mode = validated_args.get("validation_mode", "warning")
            for validation_error in validation_result.validation_errors:
                if validation_mode == "error":
                    LOGGER.error(validation_error)
                elif validation_mode == "warning":
                    LOGGER.warning(validation_error)
                elif validation_mode == "info":
                    LOGGER.info(validation_error)
                elif validation_mode == "debug":
                    LOGGER.debug(validation_error)
                elif validation_mode == "disabled":
                    pass
            return result

        try:
            has_custom_templates = bool(task_vars.get("custom_templates"))
            LOGGER.info("Rendering configuration...")
            device_config = get_device_config(task_vars)
            LOGGER.info("Rendering configuration [done].")

            if has_custom_templates:
                LOGGER.info("Rendering config custom templates...")
                rendered_custom_templates = self.render_template_with_ansible_templar(task_vars, CUSTOM_TEMPLATES_CFG_TEMPLATE)
                LOGGER.info("Rendering config custom templates [done].")
                # Need to handle if `end` has been rendered already
                if device_config.endswith("!\nend\n"):
                    device_config = device_config[:-6] + rendered_custom_templates + "!\nend\n"
                else:
                    device_config += rendered_custom_templates

            result["changed"] = self.write_file(device_config, validated_args["config_filename"])

            if validated_args["generate_device_doc"]:
                LOGGER.info("Rendering documentation...")
                device_doc = get_device_doc(task_vars, add_md_toc=False)

                if has_custom_templates:
                    LOGGER.info("Rendering documentation custom templates...")
                    device_doc += self.render_template_with_ansible_templar(task_vars, CUSTOM_TEMPLATES_DOC_TEMPLATE)
                    LOGGER.info("Rendering documentation custom templates [done].")

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
        """Get task arguments and validate them."""
        validation_result, validated_args = self.validate_argument_spec(ARGUMENT_SPEC)
        validated_args = strip_empties_from_dict(validated_args)

        # Converting to json and back to remove any AnsibeUnsafe types
        return json.loads(json.dumps(validated_args))

    def prepare_task_vars(self, task_vars: dict, structured_config_filename: str, *, read_structured_config_from_file: bool) -> dict:
        """Read the structured_config and render inline Jinja.

        Parameters
        ----------
          task_vars: Dictionary of task variables
          structured_config_filename: The filename where the structured_config for the device is stored.
          read_structured_config_from_file: Flag to indicate whether or not the structured_config_filname should be read.

        Returns
        -------
          dict: Task vars updated with the structured_config content if read and all inline Jinja rendered.

        """

        if read_structured_config_from_file:
            task_vars.update(read_vars(structured_config_filename))

        # Read ansible variables and perform templating to support inline jinja2
        for var in task_vars:
            # TODO - reevaluate these variables
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
        """Render a template with the Ansible Templar."""

        # Get updated templar instance to be passed along to our simplified "templater"
        if not hasattr(self, "ansible_templar"):
            self.ansible_templar = get_templar(self, task_vars)

        return template(templatefile, task_vars, self.ansible_templar)

    def write_file(self, content: str, filename: str) -> bool:
        """
        This function writes the file only if the content has changed.

        Returns
        -------
          bool: to indicate if file was changed.
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


def setup_module_logging(hostname: str, result: dict) -> None:
    """
    Add a Handler to copy the logs from the plugin into Ansible output based on their level

    Parameters
    ----------
        hostname: Current Inventory device being used to augment the logs with <hostname>
        result: The dictionary used for the ansible module results
    """
    python_to_ansible_filter = PythonToAnsibleContextFilter(hostname)
    python_to_ansible_handler = PythonToAnsibleHandler(result, display)
    python_to_ansible_handler.addFilter(python_to_ansible_filter)
    LOGGER.addHandler(python_to_ansible_handler)
    # TODO mechanism to manipulate the logger globally for pyavd
    # NOTE: level is kept at INFO to avoid security disclosures caused by certain libraries when using DEBUG
    # well here 15 is vvvvvv to get them all
    LOGGER.setLevel(15)


def read_vars(filename: Path | str) -> dict:
    if not isinstance(filename, Path):
        filename = Path(filename)

    with filename.open(mode="r", encoding="UTF-8") as stream:
        if filename.suffix in [".yml", ".yaml"]:
            return yaml.load(stream, Loader=YamlLoader)
        elif filename.suffix == ".json":
            return json.load(stream)
        else:
            raise NotImplementedError(f"Unsupported file suffix for file '{filename}'")
