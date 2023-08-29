# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.plugin_utils.eos_designs_shared_utils import SharedUtils
from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError, AristaAvdMissingVariableError
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get


class UtilsMixin:
    """
    Mixin Class with internal functions.
    Class should only be used as Mixin to a AvdStructuredConfig class or other Mixins.
    """

    # Set type hints for Attributes of the main class as needed
    _hostvars: dict
    shared_utils: SharedUtils

    @cached_property
    def _source_interfaces(self) -> dict:
        return get(self._hostvars, "source_interfaces", default={})

    def _build_source_interfaces(self, include_mgmt_interface: bool, include_inband_mgmt_interface: bool, error_context: str) -> list:
        """
        Return list of source interfaces with VRFs.

        Error context should be short and fit in "... configure {error_context} source-interface ..."

        Raises errors for duplicate VRFs or missing interfaces with the given error context.
        """
        source_interfaces = []

        if include_mgmt_interface:
            if (self.shared_utils.mgmt_ip is None) and (self.shared_utils.ipv6_mgmt_ip is None):
                raise AristaAvdMissingVariableError(f"Unable to configure {error_context} source-interface since 'mgmt_ip' or 'ipv6_mgmt_ip' are not set.")

            # mgmt_interface is always set (defaults to "Management1") so no need for error handling missing interface.
            source_interface = {"name": self.shared_utils.mgmt_interface}
            if self.shared_utils.mgmt_interface_vrf not in [None, "default"]:
                source_interface["vrf"] = self.shared_utils.mgmt_interface_vrf
            source_interfaces.append(source_interface)

        if include_inband_mgmt_interface:
            # Check for missing interface
            if self.shared_utils.inband_mgmt_interface is None:
                raise AristaAvdMissingVariableError(f"Unable to configure {error_context} source-interface since 'inband_mgmt_interface' is not set.")

            # Check for duplicate VRF
            # inband_mgmt_vrf returns None in case of VRF "default", but here we want the "default" VRF name to have proper duplicate detection.
            inband_mgmt_vrf = self.shared_utils.inband_mgmt_vrf or "default"
            if [source_interface for source_interface in source_interfaces if source_interface.get("vrf", "default") == inband_mgmt_vrf]:
                raise AristaAvdError(f"Unable to configure multiple {error_context} source-interfaces for the same VRF '{inband_mgmt_vrf}'.")

            source_interface = {"name": self.shared_utils.inband_mgmt_interface}
            if self.shared_utils.inband_mgmt_vrf not in [None, "default"]:
                source_interface["vrf"] = self.shared_utils.inband_mgmt_vrf
            source_interfaces.append(source_interface)

        return source_interfaces
