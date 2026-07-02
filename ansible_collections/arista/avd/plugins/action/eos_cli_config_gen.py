# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import json
import logging
from collections import ChainMap
from contextlib import suppress
from pathlib import Path
from typing import TYPE_CHECKING, Any

from ansible.errors import AnsibleActionFail
from ansible.plugins.action import ActionBase, display

from ansible_collections.arista.avd.plugins.plugin_utils.utils import (
    AVDFileHandler,
    AVDVaultHandler,
    PythonToAnsibleContextFilter,
    PythonToAnsibleHandler,
    cprofile,
    get_templar,
    get_tmp_paths,
    raise_action_fail,
)

if TYPE_CHECKING:
    from pyavd import ConfigRenderConfiguration, DocRenderConfiguration, get_device_config, get_device_doc
    from pyavd._utils import strip_empties_from_dict, template
    from pyavd.j2filters import add_md_toc

try:
    from pyavd import ConfigRenderConfiguration, DocRenderConfiguration, get_device_config, get_device_doc
    from pyavd._utils import strip_empties_from_dict, template
    from pyavd.j2filters import add_md_toc

    HAS_PYAVD = True
except ImportError:
    HAS_PYAVD = False


CUSTOM_TEMPLATES_CFG_TEMPLATE = "eos/custom-templates.j2"
CUSTOM_TEMPLATES_DOC_TEMPLATE = "documentation/custom-templates.j2"

LOGGER = logging.getLogger("ansible_collections.arista.avd")
with suppress(AttributeError):
    # Avoid duplicate logs in debug files
    # Suppressing AttribueError for ansible-lint
    LOGGER.propagate = False

ARGUMENT_SPEC = {
    "tmp_dir": {"type": "str", "required": True},
    "config_filename": {"type": "str"},
    "documentation_filename": {"type": "str"},
    "generate_device_config": {"type": "bool", "default": True},
    "generate_device_doc": {"type": "bool", "default": True},
    "configuration_hide_passwords": {"type": "bool"},
    "documentation_hide_passwords": {"type": "bool"},
    "device_doc_toc": {"type": "bool", "default": True},
    "cprofile_file": {"type": "str"},
}


class ActionModule(ActionBase):
    """Action Module for eos_cli_config_gen."""

    tmp_dir: str

    @cprofile()
    def run(self, tmp: Any = None, task_vars: dict | None = None) -> dict:
        """Ansible Action entry point."""
        if task_vars is None:
            task_vars = {}

        if not HAS_PYAVD:
            msg = "The arista.avd.eos_cli_config_gen' plugin requires the 'pyavd' Python library. Got import error"
            raise AnsibleActionFail(msg)

        result = super().run(tmp, task_vars)
        del tmp  # tmp no longer has any effect

        # Setup module logging
        hostname = task_vars["inventory_hostname"]
        setup_module_logging(hostname, result)

        return self.main(hostname, task_vars, result)

    def main(self, hostname: str, task_vars: dict, result: dict) -> dict:
        """Main function in charge of loading the structured config and generating the device configuration and documentation."""
        LOGGER.debug("Validating task arguments...")
        validated_args = self.validate_args()
        self.tmp_dir = validated_args.get("tmp_dir")
        LOGGER.debug("Validating task arguments [done].")

        LOGGER.debug("Loading structured config...")
        structured_config = self.load_structured_config(hostname)
        LOGGER.debug("Loading structured config [done].")

        if has_custom_templates := bool(task_vars.get("custom_templates")):
            template_vars = ChainMap(structured_config, task_vars)
        try:
            if validated_args["generate_device_config"]:
                LOGGER.debug("Rendering configuration...")
                device_config = get_device_config(
                    structured_config, configuration=ConfigRenderConfiguration(hide_passwords=validated_args.get("configuration_hide_passwords"))
                )

                if has_custom_templates:
                    LOGGER.debug("Rendering config custom templates...")
                    rendered_custom_templates = self.render_template_with_ansible_templar(template_vars, CUSTOM_TEMPLATES_CFG_TEMPLATE)
                    # Need to handle if `end` has been rendered already
                    if device_config.endswith("!\nend\n"):
                        device_config = device_config[:-6] + rendered_custom_templates + "!\nend\n"
                    else:
                        device_config += rendered_custom_templates
                    LOGGER.debug("Rendering config custom templates [done].")

                result["changed"] = self.write_file(device_config, validated_args["config_filename"])
                LOGGER.debug("Rendering configuration [done].")

            if validated_args["generate_device_doc"]:
                LOGGER.debug("Rendering documentation...")
                device_doc = get_device_doc(
                    structured_config,
                    add_md_toc=False,
                    configuration=DocRenderConfiguration(hide_passwords=validated_args.get("documentation_hide_passwords")),
                )

                if has_custom_templates:
                    LOGGER.debug("Rendering documentation custom templates...")
                    device_doc += self.render_template_with_ansible_templar(template_vars, CUSTOM_TEMPLATES_DOC_TEMPLATE)
                    LOGGER.debug("Rendering documentation custom templates [done].")

                if validated_args["device_doc_toc"]:
                    device_doc = add_md_toc(device_doc, skip_lines=3)

                file_changed = self.write_file(device_doc, validated_args["documentation_filename"])
                result["changed"] = result.get("changed") or file_changed
                LOGGER.debug("Rendering documentation [done].")

        except Exception as error:
            raise_action_fail(f"Error during plugin execution: {error}", error)

        return result

    def validate_args(self) -> dict:
        """Get task arguments and validate them."""
        _validation_result, validated_args = self.validate_argument_spec(
            ARGUMENT_SPEC,
            required_if=[
                ("generate_device_config", True, ("config_filename",)),
                ("generate_device_doc", True, ("documentation_filename",)),
            ],
        )
        validated_args = strip_empties_from_dict(validated_args)

        # Converting to json and back to remove any AnsibeUnsafe types
        return json.loads(json.dumps(validated_args))

    def render_template_with_ansible_templar(self, template_vars: dict | ChainMap, templatefile: str) -> str:
        """Render a template with the Ansible Templar."""
        # Get updated templar instance to be passed along to our simplified "templater"
        if not hasattr(self, "ansible_templar"):
            self.ansible_templar = get_templar(self, template_vars)  # pyright: ignore[reportArgumentType]

        return template(templatefile, template_vars, self.ansible_templar)

    def write_file(self, content: str, filename: str) -> bool:
        """
        This function writes the file only if the content has changed.

        Parameters
        ----------
            content: The content to write
            filename: Target filename

        Returns:
        -------
            bool: Indicate if the content of filename has changed.
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

    def load_structured_config(self, hostname: str) -> dict[str, Any]:
        """
        Load the validated structured config from the temporary file for the host.

        Args:
            hostname: Inventory hostname.

        Returns:
            Dict containing the validated structured config for the host.
        """
        _templated_path, validated_path = get_tmp_paths(self.tmp_dir)
        file_path = validated_path / f"{hostname}.json"
        if not file_path.exists():
            msg = (
                f"Missing the validated structured config for host '{hostname}'. "
                "Ensure the 'arista.avd.validate_inputs' task ran successfully for this host and that no validation errors occurred."
            )
            raise AnsibleActionFail(message=msg)

        # Read, unvault, and parse the JSON file
        vault_handler = AVDVaultHandler(self._loader)
        file_handler = AVDFileHandler(vault_handler)
        return file_handler.load_json(file_path)


def setup_module_logging(hostname: str, result: dict) -> None:
    """
    Add a Handler to copy the logs from the plugin into Ansible output based on their level.

    Parameters
    ----------
        hostname: Current Inventory device being used to augment the logs with <hostname>
        result: The dictionary used for the ansible module results
    """
    python_to_ansible_filter = PythonToAnsibleContextFilter(hostname)
    python_to_ansible_handler = PythonToAnsibleHandler(result, display)
    python_to_ansible_handler.addFilter(python_to_ansible_filter)
    LOGGER.addHandler(python_to_ansible_handler)
    # TODO: mechanism to manipulate the logger globally for pyavd
    LOGGER.setLevel(logging.DEBUG)
