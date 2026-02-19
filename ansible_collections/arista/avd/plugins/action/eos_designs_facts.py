# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import cProfile
import json
import pstats
from collections import ChainMap
from pathlib import Path
from typing import TYPE_CHECKING, Any, cast

from ansible.errors import AnsibleActionFail
from ansible.parsing.yaml.dumper import AnsibleDumper
from ansible.plugins.action import ActionBase

from ansible_collections.arista.avd.plugins.plugin_utils.utils import (
    ANSIBLE_ABOVE_2_19,
    AVDFileHandler,
    AVDVaultHandler,
    get_eos_designs_facts_path,
    get_templar,
    get_tmp_paths,
    raise_action_fail,
)

if TYPE_CHECKING:
    from ansible.playbook.task import Task
    from ansible.template import Templar

    from pyavd._eos_designs.eos_designs_facts.get_facts import get_facts
    from pyavd._errors import AristaAvdError
    from pyavd.api.pool_manager import PoolManager
    from pyavd.api.schemas import AVDDesign
    from pyavd.j2filters import natural_sort

try:
    from pyavd._eos_designs.eos_designs_facts.get_facts import get_facts
    from pyavd._errors import AristaAvdError
    from pyavd.api.pool_manager import PoolManager
    from pyavd.api.schemas import AVDDesign
    from pyavd.j2filters import natural_sort

    HAS_PYAVD = True
except ImportError:
    HAS_PYAVD = False


class ActionModule(ActionBase):
    _task: Task
    _templar: Templar
    tmp_dir: str

    def run(self, tmp: Any = None, task_vars: dict | None = None) -> dict:
        if task_vars is None:
            task_vars = {}
        result = super().run(tmp, task_vars)
        del tmp  # tmp no longer has any effect
        if not HAS_PYAVD:
            msg = "The arista.avd.eos_designs_facts' plugin requires the 'pyavd' Python library. Got import error"
            raise AnsibleActionFail(msg)

        self._task.args = cast("dict", self._task.args)

        cprofile_file = self._task.args.get("cprofile_file")
        if cprofile_file:
            profiler = cProfile.Profile()
            profiler.enable()

        # Only template output on ansible versions < 2.19.
        self.template_output = bool(self._task.args.get("template_output", False)) and not ANSIBLE_ABOVE_2_19

        self._digital_twin = self._task.args.get("digital_twin", False)
        output_dir = self._task.args.get("output_dir")
        self.tmp_dir = self._task.args.get("tmp_dir")
        # Get target path and clean any previously generated facts.
        avd_switch_facts_path = get_eos_designs_facts_path(self.tmp_dir, clean=True)

        groups = task_vars.get("groups", {})
        fabric_name = self._templar.template(task_vars.get("fabric_name", ""))
        # Sort for deterministic host ordering as it can change initial pool-manager assignments.
        fabric_hosts = natural_sort(groups.get(fabric_name), ignore_case=false)
        ansible_play_hosts_all = task_vars.get("ansible_play_hosts_all", [])

        # Check if fabric_name is set and that all play hosts are part of the Ansible group set in "fabric_name".
        if fabric_name is None or not set(ansible_play_hosts_all).issubset(fabric_hosts):
            msg = (
                "Invalid/missing 'fabric_name' variable. "
                "All hosts in the play must have the same 'fabric_name' value "
                "which must point to an Ansible Group containing the hosts."
                f"play_hosts: {ansible_play_hosts_all}"
            )
            raise AnsibleActionFail(msg)

        all_inputs, all_hostvars = self.load_validated_inputs(fabric_hosts)

        # Get updated templar instance to be passed along to our simplified "templater"
        templar = get_templar(self, task_vars)

        pool_manager = PoolManager(Path(output_dir))

        avd_switch_facts = self.render_facts(all_inputs=all_inputs, all_hostvars=all_hostvars, pool_manager=pool_manager, templar=templar)

        # Dump facts to file.
        self.dump_facts(avd_switch_facts, avd_switch_facts_path)

        # Save any updated pools.
        result["changed"] = pool_manager.save_updated_pools(dumper_cls=AnsibleDumper)

        if cprofile_file:
            profiler.disable()
            stats = pstats.Stats(profiler).sort_stats("cumtime")
            stats.dump_stats(cprofile_file)

        return result

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
                raise AnsibleActionFail(message=msg)

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
        Render facts, reraising errors as AnsibleActionFail.

        Args:
            all_inputs: EosDesigns instances for each device.
            pool_manager: Instance of pool_manager to assign from.
            all_hostvars: Validated hostvars for each device.
            templar: Ansible templar to render custom jinja templates.

        Returns:
            Facts as dict for each device.

        Raises:
            AnsibleActionFail for every AristaAvdError raised by pyavd.
        """
        try:
            all_facts = get_facts(all_inputs=all_inputs, pool_manager=pool_manager, all_hostvars=all_hostvars, templar=templar, digital_twin=self._digital_twin)
        except AristaAvdError as e:
            raise_action_fail(str(e), e)

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
