# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import json
from dataclasses import fields, is_dataclass
from pathlib import Path
from typing import TYPE_CHECKING, Any

import yaml
from ansible.parsing.yaml.dumper import AnsibleDumper

from ansible_collections.arista.avd.plugins.plugin_utils.utils import YamlLoader, get_eos_designs_facts_path, write_file
from ansible_collections.arista.avd.plugins.plugin_utils.utils.avd_action_plugin import AVDActionPlugin

# Remove once we drop ansible-core <2.20; ansible-test then pins coverage >=7.10.1.
if TYPE_CHECKING:  # pragma: no cover
    from pyavd._eos_designs.eos_designs_facts.schema import EosDesignsFacts
    from pyavd._utils import get, strip_empties_from_dict
    from pyavd.get_fabric_documentation import get_fabric_documentation
    from pyavd.j2filters import natural_sort

try:
    from pyavd._eos_designs.eos_designs_facts.schema import EosDesignsFacts
    from pyavd._utils import get, strip_empties_from_dict
    from pyavd.get_fabric_documentation import get_fabric_documentation
    from pyavd.j2filters import natural_sort

    HAS_PYAVD = True
except ImportError:
    HAS_PYAVD = False

PLUGIN_NAME = "arista.avd.eos_designs_documentation"

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


class ActionModule(AVDActionPlugin):
    """Action Module for eos_designs_documentation."""

    tmp_dir: str

    def main(self, task_vars: dict[str, Any]) -> None:
        """Load facts and structured configs, and render fabric documentation artifacts."""
        if not HAS_PYAVD:
            msg = f"The '{PLUGIN_NAME}' plugin requires the 'pyavd' Python library. Got import error."
            raise ImportError(msg)

        validated_args = self._validate_args()
        self.tmp_dir = validated_args["tmp_dir"]

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

        self.result["changed"] = False

        if output.fabric_documentation:
            self.result["changed"] = write_file(
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
            self.result["changed"] = self.result["changed"] or changed

        if output.p2p_links_csv:
            changed = write_file(
                content=output.p2p_links_csv,
                filename=validated_args["p2p_links_csv_file"],
                file_mode=validated_args["mode"],
            )
            self.result["changed"] = self.result["changed"] or changed

        if output.digital_twin:
            content = strip_empties_from_dict(_normalize_yaml_data(output.digital_twin))
            # for cLab we want empty `prefix` at all times in the topology to avoid modifying hostnames
            if get(task_vars, "digital_twin.environment") == "containerlab" and hasattr(output.digital_twin, "prefix"):
                interface_mapping = content.pop("interface_mapping", None)
                if interface_mapping:
                    changed = write_file(
                        content=json.dumps(interface_mapping, indent=4) + "\n",
                        filename=str(Path(validated_args["digital_twin_file"]).parent / "interface_mapping.json"),
                        file_mode=validated_args["mode"],
                    )
                    self.result["changed"] = self.result["changed"] or changed

                content["topology"]["nodes"] = {
                    node_name: {
                        "mgmt-ipv4": node_settings["mgmt-ipv4"],
                        "startup-config": f"intended/configs/{node_name}.cfg",
                    }
                    for node_name, node_settings in content["topology"]["nodes"].items()
                }
                # add keys in a very specific order - name, prefix, everything else
                content = {"name": content["name"], "prefix": output.digital_twin.prefix, **{key: value for key, value in content.items() if key != "name"}}
            changed = write_file(
                content=yaml.dump(content, Dumper=AnsibleDumper, sort_keys=False, indent=2, width=130, explicit_start=True),
                filename=validated_args["digital_twin_file"],
                file_mode=validated_args["mode"],
            )
            self.result["changed"] = self.result["changed"] or changed

    def _validate_args(self) -> dict:
        """Get task arguments and validate them."""
        _validation_result, validated_args = self.validate_argument_spec(ARGUMENT_SPEC)
        validated_args = strip_empties_from_dict(validated_args)

        # Converting to json and back to remove any AnsibeUnsafe types
        return json.loads(json.dumps(validated_args))

    def read_structured_configs(self, device_list: list[str], structured_config_dir: str, structured_config_suffix: str) -> dict[str, dict]:
        missing = set()
        structured_configs = {}
        for device in device_list:
            if structured_config := self.read_one_structured_config(device, structured_config_dir, structured_config_suffix):
                structured_configs[device] = structured_config
            else:
                missing.add(device)
        if missing:
            self.logger.warning("Could not find structured config files for '%s'. The documentation may be incomplete.", ",".join(natural_sort(missing)))

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
            raise FileNotFoundError(msg)

        with file_path.open(mode="r", encoding="utf-8") as f:
            return json.load(f)
