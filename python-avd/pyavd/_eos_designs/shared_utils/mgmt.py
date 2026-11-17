# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from logging import getLogger
from typing import TYPE_CHECKING, Protocol

from pyavd._errors import AristaAvdInvalidInputsError
from pyavd._utils.default import default

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
            self.inputs.mgmt_interface_settings._get("interface", None),
            self.inputs._get("mgmt_interface", None),
            self.cv_topology_config.mgmt_interface,
            "Management1",
        )

        # Adjust OOB management interface for ACT Digital Twin "veos" and "cloudeos" node types
        if self.is_act_digital_twin and self.platform_settings.digital_twin.act_node_type in ["veos", "cloudeos"]:
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
    def mgmt_interface_description(self: SharedUtilsProtocol) -> str:
        if self.inputs.mgmt_interface_settings._get_defined_attr("description"):
            return self.inputs.mgmt_interface_settings.description
        return self.inputs.mgmt_interface_description

    @cached_property
    def mgmt_interface_vrf(self: SharedUtilsProtocol) -> str:
        if self.inputs.mgmt_interface_settings._get_defined_attr("vrf"):
            return self.inputs.mgmt_interface_settings.vrf
        return self.inputs.mgmt_interface_vrf

    @cached_property
    def mgmt_ip(self: SharedUtilsProtocol) -> str | None:
        """
        Management IPv4 address.

        Returns an IPv4 address, or "dhcp", or None if not configured
        """
        # TODO: There's inconsistent behaviour in terms of validating `mgmt_ip`
        #       Ideally it should be `if self.node_config.mgmt_ip`, but it would break
        #       `digital_twin_containerlab_negative_tests` due to it setting `mgmt_ip: ''`, which
        #       existing code handles as a valid IP in multiple places, resulting in the different
        #       error assertions. That should be fixed separately
        if self.node_config.mgmt_ip is not None:
            return self.node_config.mgmt_ip

        if self.inputs.mgmt_interface_settings.ipv4.dhcp is True:
            return "dhcp"

        return None

    @cached_property
    def oob_mgmt_ip(self: SharedUtilsProtocol) -> str | None:
        """
        Management IPv4 address used for the generated OOB management interface.

        In ACT Digital Twin mode, `digital_twin.mgmt_ip` takes precedence over the regular node `mgmt_ip`.
        """
        if self.is_act_digital_twin and self.mgmt_ip is not None:
            return default(self.node_config.digital_twin.mgmt_ip, self.mgmt_ip)

        return self.mgmt_ip

    @cached_property
    def ipv6_mgmt_ip(self: SharedUtilsProtocol) -> str | None:
        """
        Management IPv6 address.

        Returns an IPv6 address, or "auto-config", or None if not configured
        """
        if self.node_config.ipv6_mgmt_ip:
            return self.node_config.ipv6_mgmt_ip

        if self.inputs.mgmt_interface_settings.ipv6.slaac is True:
            return "auto-config"

        return None

    @cached_property
    def mgmt_ip_dhcp_accept_default_route(self: SharedUtilsProtocol) -> bool | None:
        """
        Whether to accept the DHCP-provided default route for the generated OOB management interface.

        Returns None to leave the legacy node-level behavior unset when the future flag is disabled.
        """
        if self.node_config.mgmt_ip:
            if self.inputs.avd_design_future.accept_dhcp_default_route_for_mgmt_ip_dhcp:
                return True
            return None

        return self.inputs.mgmt_interface_settings.ipv4.accept_default_route

    @cached_property
    def ipv6_mgmt_ip_auto_config_accept_default_route(self: SharedUtilsProtocol) -> bool | None:
        """
        Whether to accept the router advertisement default route for the generated OOB management interface.

        Returns None to leave the legacy node-level behavior unset when the future flag is disabled.
        """
        if self.node_config.ipv6_mgmt_ip:
            if self.inputs.avd_design_future.accept_ra_default_route_for_ipv6_mgmt_ip_auto_config:
                return True
            return None

        return self.inputs.mgmt_interface_settings.ipv6.accept_default_route

    @cached_property
    def mgmt_vrf_routing(self: SharedUtilsProtocol) -> bool:
        if self.inputs.mgmt_interface_settings._get_defined_attr("vrf_routing"):
            return self.inputs.mgmt_interface_settings.vrf_routing
        return self.inputs.mgmt_vrf_routing

    @cached_property
    def oob_mgmt_gateway(self: SharedUtilsProtocol) -> str | None:
        """
        Management IPv4 gateway used for the generated OOB management interface.

        In ACT Digital Twin mode, `digital_twin.mgmt_gateway` takes precedence over the regular management gateway.
        """
        regular_mgmt_gateway = default(self.node_config.mgmt_gateway, self.inputs.mgmt_gateway)

        if self.is_act_digital_twin and self.mgmt_ip is not None:
            return default(self.node_config.digital_twin.mgmt_gateway, regular_mgmt_gateway)

        return regular_mgmt_gateway

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
            if not self.oob_mgmt_ip and not self.ipv6_mgmt_ip:
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
    def default_mgmt_protocol_interface(self: SharedUtilsProtocol) -> str | None:
        if self.default_mgmt_method == "oob":
            return self.mgmt_interface
        if self.default_mgmt_method == "inband":
            return self.inband_mgmt_interface

        return None
