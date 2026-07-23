# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import json
from collections import ChainMap
from pathlib import Path
from typing import TYPE_CHECKING, Any

from ansible.parsing.yaml.dumper import AnsibleDumper

from ansible_collections.arista.avd.plugins.plugin_utils.constants import ANSIBLE_ABOVE_2_19
from ansible_collections.arista.avd.plugins.plugin_utils.utils import (
    AVDFileHandler,
    AVDVaultHandler,
    cprofile,
    get_eos_designs_facts_path,
    get_templar,
    get_tmp_paths,
)
from ansible_collections.arista.avd.plugins.plugin_utils.utils.avd_action_plugin import AVDActionPlugin, AVDLoggingConfig

if TYPE_CHECKING:
    from ansible.playbook.task import Task
    from ansible.template import Templar

    from pyavd._eos_designs.eos_designs_facts.get_facts import get_facts
    from pyavd.api.pool_manager import PoolManager
    from pyavd.api.schemas import AVDDesign
    from pyavd.j2filters import natural_sort

try:
    from pyavd._eos_designs.eos_designs_facts.get_facts import get_facts
    from pyavd.api.pool_manager import PoolManager
    from pyavd.api.schemas import AVDDesign
    from pyavd.j2filters import natural_sort

    HAS_PYAVD = True
except ImportError:
    HAS_PYAVD = False


PLUGIN_NAME = "arista.avd.eos_designs_facts"

ARGUMENT_SPEC = {
    "tmp_dir": {"type": "str", "required": True},
    "output_dir": {"type": "str", "required": True},
    "template_output": {"type": "bool", "default": False},
    "digital_twin": {"type": "bool", "default": False},
    "cprofile_file": {"type": "str"},
}


class ActionModule(AVDActionPlugin):
    _task: Task
    _templar: Templar
    _logging_config = AVDLoggingConfig(add_role_context=True)
    tmp_dir: str

    @cprofile()
    def main(self, task_vars: dict[str, Any]) -> None:
        """Load validated eos_designs inputs and render avd_switch_facts."""
        if not HAS_PYAVD:
            msg = "plugin requires the 'pyavd' Python library. Got import error"
            raise ImportError(msg)

        self.logger.debug("Validating task arguments...")
        validated_args = self._validate_args()
        self.logger.debug("Validating task arguments [done].")

        self.tmp_dir = validated_args["tmp_dir"]

        # Only template output on ansible versions < 2.19.
        self.template_output = validated_args["template_output"] and not ANSIBLE_ABOVE_2_19

        self._digital_twin = validated_args["digital_twin"]
        output_dir = validated_args["output_dir"]

        # Get target path and clean any previously generated facts.
        avd_switch_facts_path = get_eos_designs_facts_path(self.tmp_dir, clean=True)

        groups = task_vars.get("groups", {})
        fabric_name = self._templar.template(task_vars.get("fabric_name", ""))
        # Sort for deterministic host ordering as it can change initial pool-manager assignments.
        fabric_hosts = natural_sort(groups.get(fabric_name), ignore_case=False)
        ansible_play_hosts_all = task_vars.get("ansible_play_hosts_all", [])

        # Check if fabric_name is set and that all play hosts are part of the Ansible group set in "fabric_name".
        if fabric_name is None or not set(ansible_play_hosts_all).issubset(fabric_hosts):
            msg = (
                "Invalid/missing 'fabric_name' variable. "
                "All hosts in the play must have the same 'fabric_name' value "
                "which must point to an Ansible Group containing the hosts."
                f"play_hosts: {ansible_play_hosts_all}"
            )
            raise ValueError(msg)

        self.logger.debug("Loading validated inputs...")
        all_inputs, all_hostvars = self.load_validated_inputs(fabric_hosts)
        self.logger.debug("Loading validated inputs [done].")

        # Get updated templar instance to be passed along to our simplified "templater"
        templar = get_templar(self, task_vars)

        self.logger.debug("Rendering eos_designs facts...")
        pool_manager = PoolManager(Path(output_dir))

        avd_switch_facts = self.render_facts(all_inputs=all_inputs, all_hostvars=all_hostvars, pool_manager=pool_manager, templar=templar)
        self.logger.debug("Rendering eos_designs facts [done].")

        # Dump facts to file.
        self.dump_facts(avd_switch_facts, avd_switch_facts_path)

        # Save any updated pools.
        self.result["changed"] = pool_manager.save_updated_pools(dumper_cls=AnsibleDumper)

    def _validate_args(self) -> dict[str, Any]:
        """Get task arguments and validate them."""
        _validation_result, validated_args = self.validate_argument_spec(ARGUMENT_SPEC)

        # Converting to json and back to remove any AnsibleUnsafe types.
        return json.loads(json.dumps(validated_args))

    def load_validated_inputs(self, fabric_hosts: list) -> tuple[dict[str, AVDDesign], dict[str, dict]]:
        """
        Load validated hostvars from temporary files for all hosts and load data into AVDDesign classes.

        Args:
            fabric_hosts: List of inventory hostnames.

        Returns:
            Tuple of one dict with the loaded AVDDesign instances keyed by hostnames
            and one dict of the raw hostvars also keyed by hostnames.

        TODO: Since hostvars are only used for custom templates, we should just give the raw hostvars object instead.
              This will allow us to only serialize and deserialize what is relevant to the schema, and drop everything else.
              As long as we support dynamic keys it would only be possible to drop the keys after validation, where we have
              identified the relevant keys correctly.
        """
        all_inputs: dict[str, AVDDesign] = {}
        all_hostvars: dict[str, dict] = {}

        _templated_path, validated_path = get_tmp_paths(self.tmp_dir)

        for host in fabric_hosts:
            file_path = validated_path / f"{host}.json"
            if not file_path.exists():
                msg = (
                    f"Missing validated inputs for host '{host}'. "
                    "Ensure the 'arista.avd.validate_inputs' task ran successfully for this host and that no validation errors occurred."
                )
                raise FileNotFoundError(msg)

            # Read, unvault, and parse the JSON file
            vault_handler = AVDVaultHandler(self._loader)
            file_handler = AVDFileHandler(vault_handler)
            host_hostvars = file_handler.load_json(file_path)

            # Load host hostvars into the AVDDesign data class.
            all_inputs[host] = AVDDesign._from_dict(host_hostvars)
            all_hostvars[host] = host_hostvars

        return all_inputs, all_hostvars

    def render_facts(self, all_inputs: dict[str, AVDDesign], pool_manager: PoolManager, all_hostvars: dict[str, dict], templar: Templar) -> dict[str, dict]:
        """
        Render facts.

        Args:
            all_inputs: EosDesigns instances for each device.
            pool_manager: Instance of pool_manager to assign from.
            all_hostvars: Validated hostvars for each device.
            templar: Ansible templar to render custom jinja templates.

        Returns:
            Facts as dict for each device.
        """
        all_facts = get_facts(all_inputs=all_inputs, pool_manager=pool_manager, all_hostvars=all_hostvars, templar=templar, digital_twin=self._digital_twin)

        all_facts_as_dicts: dict[str, dict] = {}
        for host, facts in all_facts.items():
            facts._strip_empties()
            facts_dict = facts._as_dict()

            # If the argument 'template_output' is set, run the output data through jinja2 rendering.
            # This is to resolve any input values with inline jinja using variables/facts set by eos_designs_facts.
            if self.template_output:
                available_variables = ChainMap({"switch": facts_dict}, all_hostvars[host])
                with self._templar.set_temporary_context(available_variables=available_variables):
                    facts_dict = self._templar.template(facts_dict, fail_on_undefined=False)

            all_facts_as_dicts[host] = facts_dict

        return all_facts_as_dicts

    def dump_facts(self, avd_switch_facts: dict[str, dict], file_path: Path) -> None:
        """
        Dump facts to the temporary folder.

        Args:
            avd_switch_facts: Facts to dump as dict keyed by hostname.
            file_path: Path to dump facts to.
        """
        with file_path.open(mode="w", encoding="utf-8") as f:
            json.dump(avd_switch_facts, f, indent=4)
