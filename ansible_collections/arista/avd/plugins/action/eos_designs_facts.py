# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import cProfile
import pstats
from collections import ChainMap
from pathlib import Path
from typing import TYPE_CHECKING, Any

from ansible.errors import AnsibleActionFail
from ansible.parsing.yaml.dumper import AnsibleDumper
from ansible.plugins.action import ActionBase, display

from ansible_collections.arista.avd.plugins.plugin_utils.pyavd_wrappers import RaiseOnUse
from ansible_collections.arista.avd.plugins.plugin_utils.schema.avdschematools import AvdSchemaTools
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get_templar

PLUGIN_NAME = "arista.avd.eos_designs_facts"

if TYPE_CHECKING:
    from ansible.template import Templar
    from ansible.vars.hostvars import HostVars

try:
    from pyavd._eos_designs.eos_designs_facts.get_facts import get_facts
    from pyavd._eos_designs.schema import EosDesigns
    from pyavd._errors import AristaAvdError
    from pyavd.api.pool_manager import PoolManager
except ImportError as e:
    get_facts = EosDesigns = SharedUtils = PoolManager = RaiseOnUse(
        AnsibleActionFail(
            f"The '{PLUGIN_NAME}' plugin requires the 'pyavd' Python library. Got import error",
            orig_exc=e,
        ),
    )


class ActionModule(ActionBase):
    def run(self, tmp: Any = None, task_vars: dict | None = None) -> dict:
        if task_vars is None:
            task_vars = {}

        result = super().run(tmp, task_vars)
        del tmp  # tmp no longer has any effect

        cprofile_file = self._task.args.get("cprofile_file")
        if cprofile_file:
            profiler = cProfile.Profile()
            profiler.enable()

        self.template_output = self._task.args.get("template_output", False)
        self._validation_mode = self._task.args.get("validation_mode")
        output_dir = self._task.args.get("output_dir")

        groups = task_vars.get("groups", {})
        fabric_name = self._templar.template(task_vars.get("fabric_name", ""))
        fabric_hosts = groups.get(fabric_name, [])
        ansible_play_hosts_all = task_vars.get("ansible_play_hosts_all", [])

        # Check if fabric_name is set and that all play hosts are part Ansible group set in "fabric_name"
        if fabric_name is None or not set(ansible_play_hosts_all).issubset(fabric_hosts):
            msg = (
                "Invalid/missing 'fabric_name' variable. "
                "All hosts in the play must have the same 'fabric_name' value "
                "which must point to an Ansible Group containing the hosts."
                f"play_hosts: {ansible_play_hosts_all}"
            )
            raise AnsibleActionFail(msg)

        # This is not all the hostvars, but just the Ansible Hostvars Manager object where we can retrieve hostvars for each host on-demand.
        hostvars: HostVars = task_vars["hostvars"]

        # Get updated templar instance to be passed along to our simplified "templater"
        templar = get_templar(self, task_vars)

        pool_manager = PoolManager(Path(output_dir))

        all_inputs, all_hostvars = self.parse_inputs(fabric_hosts, hostvars, result)
        if result.get("failed"):
            # Stop here if any of the devices failed input data validation
            return result

        avd_switch_facts = self.render_facts(all_inputs=all_inputs, all_hostvars=all_hostvars, pool_manager=pool_manager, templar=templar)

        # Save any updated pools.
        result["changed"] = pool_manager.save_updated_pools(dumper_cls=AnsibleDumper)

        result["ansible_facts"] = {"avd_switch_facts": avd_switch_facts}

        if cprofile_file:
            profiler.disable()
            stats = pstats.Stats(profiler).sort_stats("cumtime")
            stats.dump_stats(cprofile_file)

        return result

    def parse_inputs(self, fabric_hosts: list, hostvars: HostVars, result: dict) -> tuple[dict[str, EosDesigns], dict[str, dict]]:
        """
        Fetch hostvars for all hosts and perform data conversion & validation.

        Load data into EosDesigns class
        Returns

        Args:
            fabric_hosts: List of hostnames
            hostvars: Ansible "hostvars" object
            result: Ansible Action result dict which is inplace updated.

        Returns:
            Tuple of
                Dict with the loaded data keyed by hostnames.
                Dict of the raw hostvars keyed by hostnames.
        """
        # Load schema tools once with empty host.
        avdschematools = AvdSchemaTools(
            hostname="",
            ansible_display=display,
            schema_id="eos_designs",
            validation_mode=self._validation_mode,
            plugin_name="arista.avd.eos_designs",
        )

        all_inputs: dict[str, EosDesigns] = {}
        all_hostvars: dict[str, dict] = {}
        data_validation_errors = 0
        for host in fabric_hosts:
            # Fetch all templated Ansible vars for this host
            host_hostvars = dict(hostvars.get(host))

            # Set correct hostname in schema tools and perform conversion and validation
            avdschematools.hostname = host
            host_result = avdschematools.convert_and_validate_data(host_hostvars, return_counters=True)

            data_validation_errors += host_result["validation_errors"]

            if host_result.get("failed"):
                # Quickly continue if data validation failed
                result["failed"] = True
                continue

            # Load input vars into the EosDesigns data class.
            host_inputs = EosDesigns._from_dict(host_hostvars)

            all_inputs[host] = host_inputs
            all_hostvars[host] = host_hostvars

        # Build result message
        result["msg"] = avdschematools.build_result_message(validation_errors=data_validation_errors)

        return all_inputs, all_hostvars

    def render_facts(self, all_inputs: dict[str, EosDesigns], pool_manager: PoolManager, all_hostvars: dict[str, dict], templar: Templar) -> dict[str, dict]:
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
            all_facts = get_facts(all_inputs=all_inputs, pool_manager=pool_manager, all_hostvars=all_hostvars, templar=templar)
        except AristaAvdError as e:
            raise AnsibleActionFail(message=str(e)) from e

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
