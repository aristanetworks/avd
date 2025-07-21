# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING, Protocol

from pyavd._eos_designs.schema import EosDesigns
import re

if TYPE_CHECKING:
    from collections.abc import Iterable

    from . import SharedUtilsProtocol


class FilteredNetworkPortsMixin(Protocol):
    @cached_property
    def _filtered_network_ports(self: SharedUtilsProtocol) -> EosDesigns.NetworkPorts:
        """Return list of endpoints defined under "network_ports" which are connected to this switch."""
        filtered_network_ports = EosDesigns.NetworkPorts()
        for index, network_port in enumerate(self.inputs.network_ports):
            network_port._internal_data.context = f"network_ports[{index}]"
            network_port_settings = self.get_merged_adapter_settings(network_port)

            if not network_port_settings.switches and not network_port_settings.platforms:
                continue
            if network_port_settings.switches and not self.match_regexes(network_port_settings.switches, self.hostname):
                continue
            if network_port_settings.platforms and (
                not self.platform or not self.match_regexes(network_port_settings.platforms, self.platform)
            ):
                continue

            filtered_network_ports.append(network_port_settings)

        return filtered_network_ports

    def match_regexes(self: SharedUtilsProtocol, regexes: Iterable[str], value: str) -> bool:
        """
        Match a list of regexes with the supplied value.

        Regex must match the full value to pass.
        """
        return any(re.fullmatch(regex, value) for regex in regexes)
