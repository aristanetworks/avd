# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import json
import logging
from contextlib import suppress
from pathlib import Path
from typing import TYPE_CHECKING, Any

import yaml
from ansible.errors import AnsibleActionFail
from ansible.plugins.action import ActionBase, display

from ansible_collections.arista.avd.plugins.plugin_utils.utils import (
    PythonToAnsibleContextFilter,
    PythonToAnsibleHandler,
    YamlLoader,
    cprofile,
    get_templar,
    get_tmp_path,
)

if TYPE_CHECKING:
    from pyavd import get_device_config, get_device_doc
    from pyavd._utils import strip_empties_from_dict, template
    from pyavd.api.schemas import EOSConfig
    from pyavd.j2filters import add_md_toc

try:
    from pyavd import get_device_config, get_device_doc
    from pyavd._utils import strip_empties_from_dict, template
    from pyavd.api.schemas import EOSConfig
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
    "structured_config_filename": {"type": "str"},
    "config_filename": {"type": "str"},
    "documentation_filename": {"type": "str"},
    "read_structured_config_from_file": {"type": "bool", "default": True},
    "generate_device_config": {"type": "bool", "default": True},
    "generate_device_doc": {"type": "bool", "default": True},
    "device_doc_toc": {"type": "bool", "default": True},
    "cprofile_file": {"type": "str"},
}


class ActionModule(ActionBase):
    """Action Module for eos_cli_config_gen."""

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

        return self.main(hostname, result)

    # TODO: Cleanup.
    def main(self, hostname: str, result: dict) -> dict:
        """Main function in charge of validating the input variables and generating the device configuration and documentation."""
        LOGGER.debug("Validating task arguments...")
        validated_args = self.validate_args()
        LOGGER.debug("Validating task arguments [done].")

        eos_config, host_hostvars = self.load_validated_inputs(hostname)

        has_custom_templates = bool(host_hostvars.get("custom_templates"))
        try:
            if validated_args["generate_device_config"]:
                LOGGER.debug("Rendering configuration...")
                device_config = get_device_config(eos_config)

                if has_custom_templates:
                    LOGGER.debug("Rendering config custom templates...")
                    rendered_custom_templates = self.render_template_with_ansible_templar(host_hostvars, CUSTOM_TEMPLATES_CFG_TEMPLATE)
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
                device_doc = get_device_doc(eos_config, add_md_toc=False)

                if has_custom_templates:
                    LOGGER.debug("Rendering documentation custom templates...")
                    device_doc += self.render_template_with_ansible_templar(host_hostvars, CUSTOM_TEMPLATES_DOC_TEMPLATE)
                    LOGGER.debug("Rendering documentation custom templates [done].")

                if validated_args["device_doc_toc"]:
                    device_doc = add_md_toc(device_doc, skip_lines=3)

                file_changed = self.write_file(device_doc, validated_args["documentation_filename"])
                result["changed"] = result.get("changed") or file_changed
                LOGGER.debug("Rendering documentation [done].")

        except Exception as error:
            # Recast errors as AnsibleActionFail
            msg = f"Error during plugin execution: {error}"
            raise AnsibleActionFail(msg) from error

        return result

    def validate_args(self) -> dict:
        """Get task arguments and validate them."""
        _validation_result, validated_args = self.validate_argument_spec(
            ARGUMENT_SPEC,
            required_if=[
                ("read_structured_config_from_file", True, ("structured_config_filename",)),
                ("generate_device_config", True, ("config_filename",)),
                ("generate_device_doc", True, ("documentation_filename",)),
            ],
        )
        validated_args = strip_empties_from_dict(validated_args)

        # Converting to json and back to remove any AnsibeUnsafe types
        return json.loads(json.dumps(validated_args))

    def render_template_with_ansible_templar(self, task_vars: dict, templatefile: str) -> str:
        """Render a template with the Ansible Templar."""
        # Get updated templar instance to be passed along to our simplified "templater"
        if not hasattr(self, "ansible_templar"):
            self.ansible_templar = get_templar(self, task_vars)

        return template(templatefile, task_vars, self.ansible_templar)

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

    def load_validated_inputs(self, host: str) -> tuple[EOSConfig, dict[str, Any]]:
        """
        Read validated hostvars from the temporary file for the host and load data into AVDDesign class.

        Args:
            host: Hostname.
            avd_validated_files: Dictionary mapping hostnames to validated file paths.

        Returns:
            Tuple of an AVDDesign instance loaded from the host hostvars and a dict with the host raw hostvars.
        """
        # TODO: Use constants.
        file_path = get_tmp_path() / "eos_cli_config_gen" / "validated" / f"{host}.json"
        if not file_path.exists():
            msg = (
                f"Missing validated inputs for host '{host}'. "
                "Ensure the 'arista.avd.validate_inputs' task ran successfully for this host and that no validation errors occurred."
            )
            raise AnsibleActionFail(message=msg)

        with file_path.open(mode="r", encoding="utf-8") as f:
            host_hostvars = json.load(f)

        # Load input vars into the AVDDesign data class.
        eos_config = EOSConfig._from_dict(host_hostvars)

        return eos_config, host_hostvars


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


def read_vars(filename: Path | str) -> dict:
    """
    Read the file at filename and return the content as dict.

    The function supports either `json` or `yaml` format.

    Parameters
    ----------
        filename: The path to the file to read as a string or a Path.

    Returns:
    -------
        dict: The content of the file as dict or an empty dict if the file does not exist.

    Raises:
    ------
        NotImplementedError: If the file extension is not json, yml or yaml.
    """
    if not isinstance(filename, Path):
        filename = Path(filename)

    if not filename.exists():
        LOGGER.debug("File %s does not exist, skipping reading variables...", filename)
        return {}

    with filename.open(mode="r", encoding="UTF-8") as stream:
        if filename.suffix in [".yml", ".yaml"]:
            return yaml.load(stream, Loader=YamlLoader)  # noqa: S506 TODO: Figure out if we can move to safeloader everywhere
        if filename.suffix == ".json":
            return json.load(stream)

        msg = f"Unsupported file suffix for file '{filename}'"
        raise NotImplementedError(msg)
