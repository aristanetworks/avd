# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor

if TYPE_CHECKING:
    from . import AvdStructuredConfigNetworkServicesProtocol


class RouterInternetExitMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @structured_config_contributor
    def router_internet_exit(self: AvdStructuredConfigNetworkServicesProtocol) -> None:
        """
        Set the structured config for router_internet_exit.

        Only used for CV Pathfinder edge routers today
        """
        if not self._filtered_internet_exit_policies_and_connections:
            return

        policies = EosCliConfigGen.RouterInternetExit.Policies()
        exit_groups = EosCliConfigGen.RouterInternetExit.ExitGroups()
        for policy, connections in self._filtered_internet_exit_policies_and_connections:
            # TODO: Today we use the order of the connection list to order the exit-groups inside the policy.
            #       This works for zscaler but later we may need to use some sorting intelligence as order matters.
            for connection in connections:
                exit_group_name = connection["exit_group"]
                exit_groups.obtain(exit_group_name).local_connections.append_new(name=connection["name"])
                # Recording the exit_group in the policy
                policies.obtain(policy.name).exit_groups.append_new(name=exit_group_name)

            if policy.fallback_to_system_default:
                policies.obtain(policy.name).exit_groups.append_new(name="system-default-exit-group")

        self.structured_config.router_internet_exit._update(policies=policies, exit_groups=exit_groups)
