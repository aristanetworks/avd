# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING, Protocol

from pyavd._eos_designs.eos_designs_facts.schema import EosDesignsFactsProtocol
from pyavd._utils import remove_cached_property_type

if TYPE_CHECKING:
    from . import EosDesignsFactsGeneratorProtocol


class OverlayMixin(EosDesignsFactsProtocol, Protocol):
    """
    Mixin Class used to generate some of the EosDesignsFacts.

    Class should only be used as Mixin to the EosDesignsFacts class.
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @remove_cached_property_type
    @cached_property
    def evpn_role(self: EosDesignsFactsGeneratorProtocol) -> str | None:
        """Exposed in avd_switch_facts."""
        return self.shared_utils.evpn_role

    @remove_cached_property_type
    @cached_property
    def mpls_overlay_role(self: EosDesignsFactsGeneratorProtocol) -> str | None:
        """Exposed in avd_switch_facts."""
        return self.shared_utils.mpls_overlay_role

    @remove_cached_property_type
    @cached_property
    def evpn_route_servers(self: EosDesignsFactsGeneratorProtocol) -> EosDesignsFactsProtocol.EvpnRouteServers:
        """
        Exposed in avd_switch_facts.

        For evpn clients the default value for EVPN Route Servers is the content of the uplink_switches variable set elsewhere.
        For all other evpn roles there is no default.
        """
        if self.shared_utils.underlay_router is True:
            if self.evpn_role == "client":
                return EosDesignsFactsProtocol.EvpnRouteServers(self.shared_utils.node_config.evpn_route_servers or self.shared_utils.uplink_switches)
            return EosDesignsFactsProtocol.EvpnRouteServers(self.shared_utils.node_config.evpn_route_servers)
        return EosDesignsFactsProtocol.EvpnRouteServers()

    @remove_cached_property_type
    @cached_property
    def mpls_route_reflectors(self: EosDesignsFactsGeneratorProtocol) -> EosDesignsFactsProtocol.MplsRouteReflectors:
        """Exposed in avd_switch_facts."""
        if self.shared_utils.underlay_router is True and (
            self.mpls_overlay_role in ["client", "server"] or (self.evpn_role in ["client", "server"] and self.shared_utils.overlay_evpn_mpls)
        ):
            return EosDesignsFactsProtocol.MplsRouteReflectors(self.shared_utils.node_config.mpls_route_reflectors)
        return EosDesignsFactsProtocol.MplsRouteReflectors()

    @remove_cached_property_type
    @cached_property
    def overlay(self: EosDesignsFactsGeneratorProtocol) -> EosDesignsFactsProtocol.Overlay:
        """Exposed in avd_switch_facts."""
        if self.shared_utils.underlay_router is True:
            return EosDesignsFactsProtocol.Overlay(
                peering_address=self.shared_utils.overlay_peering_address,
                evpn_mpls=self.shared_utils.overlay_evpn_mpls,
            )
        return EosDesignsFactsProtocol.Overlay()

    @remove_cached_property_type
    @cached_property
    def vtep_ip(self: EosDesignsFactsGeneratorProtocol) -> str | None:
        """Exposed in avd_switch_facts."""
        if self.shared_utils.vtep or self.shared_utils.is_wan_router:
            return self.shared_utils.vtep_ip
        return None
