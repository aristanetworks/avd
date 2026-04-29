# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import json
import logging
from dataclasses import fields, is_dataclass
from pathlib import Path
from typing import Any

import yaml
from ansible.errors import AnsibleActionFail
from ansible.parsing.yaml.dumper import AnsibleDumper
from ansible.plugins.action import ActionBase, display

from ansible_collections.arista.avd.plugins.plugin_utils.pyavd_wrappers import RaiseOnUse
from ansible_collections.arista.avd.plugins.plugin_utils.utils import PythonToAnsibleHandler, YamlLoader, get_eos_designs_facts_path, write_file

PLUGIN_NAME = "arista.avd.eos_designs_documentation"
try:
    from pyavd._eos_designs.eos_designs_facts.schema import EosDesignsFacts
    from pyavd._utils import get, strip_empties_from_dict
    from pyavd.get_fabric_documentation import get_fabric_documentation
except ImportError as e:
    EosDesignsFacts = get = strip_empties_from_dict = get_fabric_documentation = RaiseOnUse(
        AnsibleActionFail(
            f"The '{PLUGIN_NAME}' plugin requires the 'pyavd' Python library. Got import error",
            orig_exc=e,
        ),
    )


LOGGER = logging.getLogger("ansible_collections.arista.avd")
LOGGING_LEVELS = ["DEBUG", "INFO", "ERROR", "WARNING", "CRITICAL"]

ARGUMENT_SPEC = {
    "tmp_dir": {"type": "str", "required": True},
    "structured_config_dir": {"type": "str", "required": True},
    "structured_config_suffix": {"type": "str", "default": "yml"},
    "fabric_documentation_file": {"type": "str", "required": True},
    "mode": {"type": "str", "default": "0o664"},
    "fabric_documentation": {"type": "bool", "default": True},
    "include_connected_endpoints": {"type": "bool", "default": False},
    "topology_csv_file": {"type": "str", "required": True},
    "topology_csv": {"type": "bool", "default": False},
    "p2p_links_csv_file": {"type": "str", "required": True},
    "p2p_links_csv": {"type": "bool", "default": False},
    "toc": {"type": "bool", "default": True},
    "digital_twin_file": {"type": "str", "default": "DIGITAL-TWIN-TOPOLOGY.yml"},
    "digital_twin": {"type": "bool", "default": False},
}


def _normalize_yaml_data(data: Any) -> Any:
    """Recursively normalize data for YAML output while honoring per-field YAML key aliases on dataclasses."""
    if is_dataclass(data):
        return {
            str(dataclass_field.metadata.get("yaml_key", dataclass_field.name)): _normalize_yaml_data(getattr(data, dataclass_field.name))
            for dataclass_field in fields(data)
        }
    if isinstance(data, dict):
        return {str(key): _normalize_yaml_data(value) for key, value in data.items()}
    if isinstance(data, tuple | list):
        return [_normalize_yaml_data(value) for value in data]
    return data


class ActionModule(ActionBase):
    tmp_dir: str

    def run(self, tmp: Any = None, task_vars: dict | None = None) -> dict:
        self._supports_check_mode = False

        if task_vars is None:
            task_vars = {}

        result = super().run(tmp, task_vars)
        del tmp  # tmp no longer has any effect

        # Setup module logging
        setup_module_logging(result)

        # Get task arguments and validate them
        _validation_result, validated_args = self.validate_argument_spec(ARGUMENT_SPEC)
        validated_args = strip_empties_from_dict(validated_args)

        # Converting to json and back to remove any AnsibeUnsafe types
        validated_args = json.loads(json.dumps(validated_args))

        self.tmp_dir = validated_args.get("tmp_dir")

        return self.main(validated_args, task_vars, result)

    def main(self, validated_args: dict, task_vars: dict, result: dict) -> dict:
        avd_switch_facts = self.load_facts()
        device_list = list(avd_switch_facts.keys())

        # Create dict of all facts.
        all_facts = {host: EosDesignsFacts._from_dict(facts_as_dict) for host, facts_as_dict in avd_switch_facts.items()}

        structured_configs = self.read_structured_configs(
            device_list=device_list,
            structured_config_dir=validated_args["structured_config_dir"],
            structured_config_suffix=validated_args["structured_config_suffix"],
        )
        fabric_name = get(task_vars, "fabric_name", required=True)
        output = get_fabric_documentation(
            avd_facts=all_facts,
            structured_configs=structured_configs,
            fabric_name=fabric_name,
            fabric_documentation=validated_args["fabric_documentation"],
            include_connected_endpoints=validated_args["include_connected_endpoints"],
            topology_csv=validated_args["topology_csv"],
            p2p_links_csv=validated_args["p2p_links_csv"],
            toc=validated_args["toc"],
            digital_twin=validated_args["digital_twin"],
        )
        if output.fabric_documentation:
            result["changed"] = write_file(
                content=output.fabric_documentation,
                filename=validated_args["fabric_documentation_file"],
                file_mode=validated_args["mode"],
            )
        if output.topology_csv:
            changed = write_file(
                content=output.topology_csv,
                filename=validated_args["topology_csv_file"],
                file_mode=validated_args["mode"],
            )
            result["changed"] = result.get("changed") or changed

        if output.p2p_links_csv:
            changed = write_file(
                content=output.p2p_links_csv,
                filename=validated_args["p2p_links_csv_file"],
                file_mode=validated_args["mode"],
            )
            result["changed"] = result.get("changed") or changed

        if output.digital_twin:
            content = strip_empties_from_dict(_normalize_yaml_data(output.digital_twin))
            changed = write_file(
                content=yaml.dump(content, Dumper=AnsibleDumper, sort_keys=False, indent=2, width=130, explicit_start=True),
                filename=validated_args["digital_twin_file"],
                file_mode=validated_args["mode"],
            )
            result["changed"] = result.get("changed") or changed

        return result

    def read_structured_configs(self, device_list: list[str], structured_config_dir: str, structured_config_suffix: str) -> dict[str, dict]:
        missing = set()
        structured_configs = {}
        for device in device_list:
            if structured_config := self.read_one_structured_config(device, structured_config_dir, structured_config_suffix):
                structured_configs[device] = structured_config
            else:
                missing.add(device)
        if missing:
            LOGGER.warning("Could not find structured config files for '%s'. The documentation may be incomplete.", ",".join(missing))

        return structured_configs

    def read_one_structured_config(self, device: str, structured_config_dir: str, structured_config_suffix: str) -> dict:
        path = Path(structured_config_dir, f"{device}.{structured_config_suffix}")
        if not path.exists():
            return {}

        with path.open(encoding="UTF-8") as stream:
            if structured_config_suffix in ["yml", "yaml"]:
                return yaml.load(stream, Loader=YamlLoader)  # noqa: S506

            # JSON
            return json.load(stream)

    def load_facts(self) -> dict[str, dict]:
        """
        Load facts from the temporary file.

        Returns:
            Dict of facts keyed by hostname.
        """
        file_path = get_eos_designs_facts_path(self.tmp_dir)

        if not file_path.exists():
            msg = f"Missing AVD eos_designs facts to generate documentation ({file_path}). Ensure the 'arista.avd.eos_designs_facts' task ran successfully."
            raise AnsibleActionFail(message=msg)

        with file_path.open(mode="r", encoding="utf-8") as f:
            return json.load(f)


def setup_module_logging(result: dict) -> None:
    """
    Add a Handler to copy the logs from the plugin into Ansible output based on their level.

    Parameters:
        result: The dictionary used for the ansible module results
    """
    python_to_ansible_handler = PythonToAnsibleHandler(result, display)
    LOGGER.addHandler(python_to_ansible_handler)
    # TODO: mechanism to manipulate the logger globally for pyavd
    # Keep debug to be able to see logs with `-v` and `-vvv`
    LOGGER.setLevel(logging.DEBUG)
