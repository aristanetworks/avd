# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._errors import AristaAvdError, AristaAvdInvalidInputsError

if TYPE_CHECKING:
    from typing import TypeVar

    from pyavd._eos_cli_config_gen.schema import EosCliConfigGen

    from . import AvdStructuredConfigBaseProtocol

    T_Source_Interfaces = TypeVar(
        "T_Source_Interfaces",
        EosCliConfigGen.IpHttpClientSourceInterfaces,
        EosCliConfigGen.IpDomainLookup.SourceInterfaces,
        EosCliConfigGen.IpSshClientSourceInterfaces,
        EosCliConfigGen.IpTacacsSourceInterfaces,
        EosCliConfigGen.SnmpServer.LocalInterfaces,
        EosCliConfigGen.IpRadiusSourceInterfaces,
    )


class UtilsMixin(Protocol):
    """
    Mixin Class with internal functions.

    Class should only be used as Mixin to a AvdStructuredConfig class or other Mixins.
    """

    def _build_source_interfaces(
        self: AvdStructuredConfigBaseProtocol,
        include_mgmt_interface: bool,
        include_inband_mgmt_interface: bool,
        error_context: str,
        output_type: type[T_Source_Interfaces],
    ) -> T_Source_Interfaces:
        """
        Return list of source interfaces with VRFs.

        Error context should be short and fit in "... configure {error_context} source-interface ..."

        Raises errors for duplicate VRFs or missing interfaces with the given error context.
        """
        source_interfaces = output_type()
        if include_mgmt_interface:
            if (self.shared_utils.node_config.mgmt_ip is None) and (self.shared_utils.node_config.ipv6_mgmt_ip is None):
                msg = f"Unable to configure {error_context} source-interface since 'mgmt_ip' or 'ipv6_mgmt_ip' are not set."
                raise AristaAvdInvalidInputsError(msg)

            # mgmt_interface is always set (defaults to "Management1") so no need for error handling missing interface.
            source_interfaces.append_new(
                name=self.shared_utils.mgmt_interface, vrf=self.inputs.mgmt_interface_vrf if self.inputs.mgmt_interface_vrf != "default" else None
            )

        if include_inband_mgmt_interface:
            # Check for missing interface
            if self.shared_utils.inband_mgmt_interface is None:
                msg = f"Unable to configure {error_context} source-interface since 'inband_mgmt_interface' is not set."
                raise AristaAvdInvalidInputsError(msg)

            # Check for duplicate VRF
            # inband_mgmt_vrf returns None in case of VRF "default", but here we want the "default" VRF name to have proper duplicate detection.
            inband_mgmt_vrf = self.shared_utils.inband_mgmt_vrf or "default"
            if [source_interface for source_interface in source_interfaces if (source_interface.vrf or "default") == inband_mgmt_vrf]:
                msg = f"Unable to configure multiple {error_context} source-interfaces for the same VRF '{inband_mgmt_vrf}'."
                raise AristaAvdError(msg)

            source_interfaces.append_new(
                name=self.shared_utils.inband_mgmt_interface,
                vrf=self.shared_utils.inband_mgmt_vrf,
            )

        return source_interfaces
