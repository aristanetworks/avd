# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import cProfile
import pstats
from collections import ChainMap
from pathlib import Path
from typing import TYPE_CHECKING, Any, cast

from ansible.errors import AnsibleActionFail
from ansible.parsing.yaml.dumper import AnsibleDumper
from ansible.plugins.action import ActionBase, display

from ansible_collections.arista.avd.plugins.plugin_utils.utils import (
    ANSIBLE_ABOVE_2_19,
    ActionPluginVars,
    build_result_message,
    get_templar,
    parse_validation_result,
    raise_action_fail,
)

if TYPE_CHECKING:
    from ansible.playbook.task import Task
    from ansible.template import Templar

    from pyavd import validate_inputs
    from pyavd._eos_designs.eos_designs_facts.get_facts import get_facts
    from pyavd._errors import AristaAvdError
    from pyavd.api.pool_manager import PoolManager
    from pyavd.api.schemas import AVDDesign

try:
    from pyavd import validate_inputs
    from pyavd._eos_designs.eos_designs_facts.get_facts import get_facts
    from pyavd._errors import AristaAvdError
    from pyavd.api.pool_manager import PoolManager
    from pyavd.api.schemas import AVDDesign

    HAS_PYAVD = True
except ImportError:
    HAS_PYAVD = False


class ActionModule(ActionBase):
    _task: Task
    _templar: Templar

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

        # This is an "Ansible Hostvars Manager"-like object where we can retrieve hostvars for each host on-demand.
        # This is special because it contains role, play and task vars as well.
        hostvars = ActionPluginVars(self)

        # Get updated templar instance to be passed along to our simplified "templater"
        templar = get_templar(self, task_vars)

        pool_manager = PoolManager(Path(output_dir))

        all_inputs, all_hostvars = self.parse_inputs(fabric_hosts, hostvars, result)
        if result.get("failed"):
            # Stop here if any of the devices failed input data validation
            if cprofile_file:
                profiler.disable()
                stats = pstats.Stats(profiler).sort_stats("cumtime")
                stats.dump_stats(cprofile_file)

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

    def parse_inputs(self, fabric_hosts: list, hostvars: ActionPluginVars, result: dict) -> tuple[dict[str, AVDDesign], dict[str, dict]]:
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
        all_inputs: dict[str, AVDDesign] = {}
        all_hostvars: dict[str, dict] = {}
        data_validation_errors = 0

        for host in fabric_hosts:
            # Fetch all templated Ansible vars for this host
            # In Ansible versions <2.19 the vars will be templated best-effort. Ignoring failures.
            # From Ansible version 2.19 the vars will be templated on access and errors will be raised for any undefined vars.
            # NOTE: We need the dict() for conversion to work below, since it is inplace updating stuff. Otherwise it looses the updates.
            host_hostvars = dict(hostvars[host])

            # Load input vars into the EosDesigns data class.
            validated_data_result = validate_inputs(host_hostvars)

            data_validation_errors += parse_validation_result(validation_result=validated_data_result.validation_result, hostname=host, ansible_display=display)

            if data_validation_errors or validated_data_result.validated_data is None:
                # Quickly continue if data validation failed
                result["failed"] = True
                continue

            all_inputs[host] = AVDDesign._from_dict(validated_data_result.validated_data)
            all_hostvars[host] = host_hostvars

        # Build result message
        result["msg"] = build_result_message(data_validation_errors)

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
