# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from logging import getLogger
from typing import TYPE_CHECKING, Protocol

from pyavd._errors import AristaAvdInvalidInputsError
from pyavd._utils import default

if TYPE_CHECKING:
    from . import SharedUtilsProtocol

LOGGER = getLogger(__name__)


class MgmtMixin(Protocol):
    """
    Mixin Class providing a subset of SharedUtils.

    Class should only be used as Mixin to the SharedUtils class.
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def mgmt_interface(self: SharedUtilsProtocol) -> str:
        """
        mgmt_interface.

        mgmt_interface is inherited from
        Global var mgmt_interface ->
          Platform Settings management_interface ->
            Fabric Topology data model mgmt_interface.
        If in Digital Twin mode, the returned value is modified to meet the requirements of the target environment:
            ACT: Management1.
        """
        mgmt_interface = default(
            self.node_config.mgmt_interface,
            # Notice that we actually have a default value for the next two, but the precedence order would break if we use it.
            # TODO: Evaluate if we should remove the default values from either or both.
            self.platform_settings._get("management_interface", None),
            self.inputs._get("mgmt_interface", None),
            self.cv_topology_config.mgmt_interface,
            "Management1",
        )

        # Adjust OOB management interface for ACT Digital Twin "veos" and "cloudeos" node types
        if self.digital_twin and self.inputs.digital_twin.environment == "act" and self.platform_settings.digital_twin.act_node_type in ["veos", "cloudeos"]:
            act_mgmt_interface = "Management1"
            if mgmt_interface != act_mgmt_interface:
                LOGGER.info(
                    "OOB management interface for node '%s' changed from '%s' to '%s' for its ACT Digital Twin copy.",
                    self.hostname,
                    mgmt_interface,
                    act_mgmt_interface,
                )
            return act_mgmt_interface

        return mgmt_interface

    @cached_property
    def mgmt_gateway(self: SharedUtilsProtocol) -> str | None:
        return default(self.node_config.mgmt_gateway, self.inputs.mgmt_gateway)

    @cached_property
    def ipv6_mgmt_gateway(self: SharedUtilsProtocol) -> str | None:
        return default(self.node_config.ipv6_mgmt_gateway, self.inputs.ipv6_mgmt_gateway)

    @cached_property
    def default_mgmt_method(self: SharedUtilsProtocol) -> str | None:
        """
        This is only executed if some protocol looks for the default value, so we can raise here to ensure a working config.

        The check for 'inband_mgmt_interface' relies on other indirect checks done in that code.
        """
        default_mgmt_method = self.inputs.default_mgmt_method
        if default_mgmt_method == "oob":
            if self.node_config.mgmt_ip is None and self.node_config.ipv6_mgmt_ip is None:
                msg = "'default_mgmt_method: oob' requires either 'mgmt_ip' or 'ipv6_mgmt_ip' to be set."
                raise AristaAvdInvalidInputsError(msg)

            return default_mgmt_method

        if default_mgmt_method == "inband":
            # Check for missing interface
            if self.inband_mgmt_interface is None:
                msg = "'default_mgmt_method: inband' requires 'inband_mgmt_interface' to be set."
                raise AristaAvdInvalidInputsError(msg)

            return default_mgmt_method

        return None

    @cached_property
    def default_mgmt_protocol_vrf(self: SharedUtilsProtocol) -> str | None:
        if self.default_mgmt_method == "oob":
            return self.inputs.mgmt_interface_vrf
        if self.default_mgmt_method == "inband":
            # inband_mgmt_vrf returns None for vrf default.
            return self.inband_mgmt_vrf or "default"

        return None

    @cached_property
    def default_mgmt_protocol_interface(self: SharedUtilsProtocol) -> str | None:
        if self.default_mgmt_method == "oob":
            return self.mgmt_interface
        if self.default_mgmt_method == "inband":
            return self.inband_mgmt_interface

        return None
