# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING, Protocol

from pyavd._eos_designs.avdfacts import AvdFacts, AvdFactsProtocol
from pyavd._errors import AristaAvdError
from pyavd._utils import remove_cached_property_type

from .mlag import MlagMixin
from .overlay import OverlayMixin
from .schema import EosDesignsFactsProtocol
from .short_esi import ShortEsiMixin
from .uplinks import UplinksMixin
from .utils import UtilsMixin
from .vlans import VlansMixin
from .wan import WanMixin

if TYPE_CHECKING:
    from collections.abc import Mapping

    from pyavd._eos_designs.schema import EosDesigns
    from pyavd._eos_designs.shared_utils import SharedUtilsProtocol


class EosDesignsFactsGeneratorProtocol(
    MlagMixin, ShortEsiMixin, OverlayMixin, WanMixin, UplinksMixin, UtilsMixin, VlansMixin, EosDesignsFactsProtocol, AvdFactsProtocol, Protocol
):
    """
    This Protocol is only used by EosDesignsFactsGenerator.

    It is implemented as a protocol because of the Mixin layout and to get proper type checking in the Mixin classes.
    Used as type hint on `self` in the Mixin methods.
    """

    peer_generators: dict[str, EosDesignsFactsGenerator]

    # Placeholders that are filled out by the peers' generators.
    _downlink_switches: EosDesignsFactsProtocol.DownlinkSwitches
    _evpn_route_server_clients: EosDesignsFactsProtocol.EvpnRouteServerClients
    _mpls_route_reflector_clients: EosDesignsFactsProtocol.MplsRouteReflectorClients

    @remove_cached_property_type
    @cached_property
    def id(self) -> int | None:
        """Exposed in avd_switch_facts."""
        return self.shared_utils.id

    @remove_cached_property_type
    @cached_property
    def type(self) -> str:
        """
        Exposed in avd_switch_facts.

        switch.type fact set based on type variable
        """
        return self.shared_utils.type

    @remove_cached_property_type
    @cached_property
    def platform(self) -> str | None:
        """Exposed in avd_switch_facts."""
        return self.shared_utils.platform

    @remove_cached_property_type
    @cached_property
    def is_deployed(self) -> bool:
        """Exposed in avd_switch_facts."""
        return self.inputs.is_deployed

    @remove_cached_property_type
    @cached_property
    def serial_number(self) -> str | None:
        """Exposed in avd_switch_facts."""
        return self.shared_utils.serial_number

    @remove_cached_property_type
    @cached_property
    def mgmt_interface(self) -> str | None:
        """Exposed in avd_switch_facts."""
        return self.shared_utils.mgmt_interface

    @remove_cached_property_type
    @cached_property
    def mgmt_ip(self) -> str | None:
        """Exposed in avd_switch_facts."""
        return self.shared_utils.node_config.mgmt_ip

    @remove_cached_property_type
    @cached_property
    def mpls_lsr(self) -> bool:
        """Exposed in avd_switch_facts."""
        return self.shared_utils.mpls_lsr

    @remove_cached_property_type
    @cached_property
    def evpn_multicast(self) -> bool | None:
        """
        Exposed in avd_switch_facts.

        This method _must_ be in EosDesignsFacts and not in SharedUtils, since it reads the SharedUtils instance on the peer.
        This is only possible when running from EosDesignsFacts, since this is the only time where we can access the actual
        python instance of EosDesignsFacts and not the simplified dict.
        """
        if "evpn" not in self.shared_utils.overlay_address_families:
            return None
        if self.inputs.evpn_multicast and self.shared_utils.vtep:
            if not (self.shared_utils.underlay_multicast and self.shared_utils.igmp_snooping_enabled):
                msg = "'evpn_multicast: True' is only supported in combination with 'underlay_multicast: True' and 'igmp_snooping_enabled : True'"
                raise AristaAvdError(msg)

            if (
                self.shared_utils.mlag
                and self.shared_utils.overlay_rd_type_admin_subfield == self._mlag_peer_facts_generator.shared_utils.overlay_rd_type_admin_subfield
            ):
                msg = "For MLAG devices Route Distinguisher must be unique when 'evpn_multicast: True' since it will create a multi-vtep configuration."
                raise AristaAvdError(msg)
            return True
        return None

    @remove_cached_property_type
    @cached_property
    def loopback_ipv4_pool(self) -> str | None:
        """Exposed in avd_switch_facts."""
        if self.shared_utils.underlay_router:
            return self.shared_utils.loopback_ipv4_pool
        return None

    @remove_cached_property_type
    @cached_property
    def uplink_ipv4_pool(self) -> str | None:
        """Exposed in avd_switch_facts."""
        if self.shared_utils.underlay_router:
            return self.shared_utils.node_config.uplink_ipv4_pool
        return None

    @remove_cached_property_type
    @cached_property
    def downlink_pools(self) -> EosDesignsFactsProtocol.DownlinkPools:
        """Exposed in avd_switch_facts."""
        if self.shared_utils.underlay_router:
            return self.shared_utils.node_config.downlink_pools._cast_as(EosDesignsFactsProtocol.DownlinkPools)
        return EosDesignsFactsProtocol.DownlinkPools()

    @remove_cached_property_type
    @cached_property
    def bgp_as(self) -> str | None:
        """Exposed in avd_switch_facts."""
        if self.shared_utils.underlay_router is True:
            return self.shared_utils.bgp_as
        return None

    @remove_cached_property_type
    @cached_property
    def underlay_routing_protocol(self) -> str:
        """Exposed in avd_switch_facts."""
        return self.shared_utils.underlay_routing_protocol

    @remove_cached_property_type
    @cached_property
    def vtep_loopback_ipv4_pool(self) -> str | None:
        """Exposed in avd_switch_facts."""
        if self.shared_utils.vtep is True:
            return self.shared_utils.vtep_loopback_ipv4_pool
        return None

    @remove_cached_property_type
    @cached_property
    def inband_mgmt_subnet(self) -> str | None:
        """Exposed in avd_switch_facts."""
        if self.shared_utils.configure_parent_for_inband_mgmt:
            return self.shared_utils.node_config.inband_mgmt_subnet
        return None

    @remove_cached_property_type
    @cached_property
    def inband_mgmt_ipv6_subnet(self) -> str | None:
        """Exposed in avd_switch_facts."""
        if self.shared_utils.configure_parent_for_inband_mgmt_ipv6:
            return self.shared_utils.node_config.inband_mgmt_ipv6_subnet
        return None

    @remove_cached_property_type
    @cached_property
    def inband_mgmt_vlan(self) -> int | None:
        """Exposed in avd_switch_facts."""
        if self.shared_utils.configure_parent_for_inband_mgmt or self.shared_utils.configure_parent_for_inband_mgmt_ipv6:
            return self.shared_utils.node_config.inband_mgmt_vlan
        return None

    @remove_cached_property_type
    @cached_property
    def inband_ztp(self) -> bool | None:
        """Exposed in avd_switch_facts."""
        return self.shared_utils.node_config.inband_ztp

    @remove_cached_property_type
    @cached_property
    def inband_ztp_vlan(self) -> int | None:
        """Exposed in avd_switch_facts."""
        if self.shared_utils.node_config.inband_ztp:
            return self.shared_utils.node_config.inband_mgmt_vlan
        return None

    @remove_cached_property_type
    @cached_property
    def inband_ztp_lacp_fallback_delay(self) -> int | None:
        """Exposed in avd_switch_facts."""
        if self.shared_utils.node_config.inband_ztp:
            return self.shared_utils.node_config.inband_ztp_lacp_fallback_delay
        return None

    @remove_cached_property_type
    @cached_property
    def dc_name(self) -> str | None:
        """Exposed in avd_switch_facts."""
        return self.inputs.dc_name

    @remove_cached_property_type
    @cached_property
    def group(self) -> str | None:
        """Exposed in avd_switch_facts."""
        return self.shared_utils.group

    @remove_cached_property_type
    @cached_property
    def router_id(self) -> str | None:
        """Exposed in avd_switch_facts."""
        return self.shared_utils.router_id

    @remove_cached_property_type
    @cached_property
    def inband_mgmt_ip(self) -> str | None:
        """
        Exposed in avd_switch_facts.

        Used for fabric docs
        """
        return self.shared_utils.inband_mgmt_ip

    @remove_cached_property_type
    @cached_property
    def inband_mgmt_interface(self) -> str | None:
        """
        Exposed in avd_switch_facts.

        Used for fabric docs
        """
        return self.shared_utils.inband_mgmt_interface

    @remove_cached_property_type
    @cached_property
    def pod(self) -> str:
        """
        Exposed in avd_switch_facts.

        Used for fabric docs
        """
        return self.inputs.pod_name or self.inputs.dc_name or self.shared_utils.fabric_name

    @remove_cached_property_type
    @cached_property
    def connected_endpoints_keys(self) -> EosDesignsFactsProtocol.ConnectedEndpointsKeys:
        """
        List of connected_endpoints_keys in use on this device.

        Exposed in avd_switch_facts.

        Used for fabric docs
        """
        return EosDesignsFactsProtocol.ConnectedEndpointsKeys(
            EosDesignsFactsProtocol.ConnectedEndpointsKeysItem(key=entry.key, type=entry.type, description=entry.description)
            for entry in self.inputs.connected_endpoints_keys
            if entry.key in self.inputs._dynamic_keys.connected_endpoints
        )

    @remove_cached_property_type
    @cached_property
    def port_profile_names(self) -> EosDesignsFactsProtocol.PortProfileNames:
        """
        Exposed in avd_switch_facts.

        Used for fabric docs
        """
        return EosDesignsFactsProtocol.PortProfileNames(
            EosDesignsFactsProtocol.PortProfileNamesItem(profile=profile.profile, parent_profile=profile.parent_profile)
            for profile in self.inputs.port_profiles
        )

    def _populate_downlink_switches_on_peers(self) -> None:
        """
        Walk through uplink_peers on this device and update _their_ facts with the hostname of this device.

        This is used later in eos_designs_structured_config to quickly identify relevant peers, instead of walking through all devices.

        Invoked by the cross_polinate method.
        """
        for uplink_peer in self.uplink_peers:
            peer_facts = self.get_peer_facts_generator(uplink_peer)
            peer_facts._downlink_switches.append_unique(self.shared_utils.hostname)

    def _populate_evpn_route_server_clients_on_peers(self) -> None:
        """
        Walk through evpn_route_servers on this device and update _their_ facts with the hostname of this device.

        This is used later in eos_designs_structured_config to quickly identify relevant peers, instead of walking through all devices.

        Invoked by the cross_polinate method.
        """
        for uplink_peer in self.evpn_route_servers:
            peer_facts = self.get_peer_facts_generator(uplink_peer)
            if peer_facts.evpn_role == "server":
                peer_facts._evpn_route_server_clients.append_unique(self.shared_utils.hostname)

    def _populate_mpls_route_reflector_clients_on_peers(self) -> None:
        """
        Walk through mpls_route_reflectors on this device and update _their_ facts with the hostname of this device.

        This is used later in eos_designs_structured_config to quickly identify relevant peers, instead of walking through all devices.

        Invoked by the cross_polinate method.
        """
        for uplink_peer in self.mpls_route_reflectors:
            peer_facts = self.get_peer_facts_generator(uplink_peer)
            if peer_facts.mpls_overlay_role == "server":
                peer_facts._mpls_route_reflector_clients.append_unique(self.shared_utils.hostname)

    @remove_cached_property_type
    @cached_property
    def downlink_switches(self) -> EosDesignsFactsProtocol.DownlinkSwitches:
        """
        Exposed in avd_switch_facts.

        Used for fabric docs
        """
        return self._downlink_switches

    @remove_cached_property_type
    @cached_property
    def evpn_route_server_clients(self) -> EosDesignsFactsProtocol.EvpnRouteServerClients:
        return self._evpn_route_server_clients

    @remove_cached_property_type
    @cached_property
    def mpls_route_reflector_clients(self) -> EosDesignsFactsProtocol.MplsRouteReflectorClients:
        return self._mpls_route_reflector_clients


class EosDesignsFactsGenerator(AvdFacts, EosDesignsFactsGeneratorProtocol, EosDesignsFactsProtocol):
    """
    `EosDesignsFactsGenerator` is used to generate facts according to the EosDesignsFactsProtocol.

    The class inherits from `AvdFacts`, to get the render() method, so make sure to read the description there as well.

    The generator's properties can also be accessed directly, to allow computation of facts based on other facts.

    The class is instantiated once per device. Methods may use references to other device instances using `self.peer_generators`,
    which is a dict of `EosDesignsfactsGenerator` instances covering all devices.
    """

    def __init__(self, hostvars: Mapping, inputs: EosDesigns, peer_generators: dict[str, EosDesignsFactsGenerator], shared_utils: SharedUtilsProtocol) -> None:
        super().__init__(hostvars, inputs, shared_utils)
        self.peer_generators = peer_generators

        # Initialize placeholders that are filled out by the peers' generators.
        self._downlink_switches = EosDesignsFactsProtocol.DownlinkSwitches()
        self._evpn_route_server_clients = EosDesignsFactsProtocol.EvpnRouteServerClients()
        self._mpls_route_reflector_clients = EosDesignsFactsProtocol.MplsRouteReflectorClients()

    def cross_pollinate(self) -> None:
        """
        Call helper functions which will register this device in the peers' facts.

        This is used later in eos_designs_structured_config to quickly identify relevant peers, instead of walking through all devices.
        """
        self._populate_downlink_switches_on_peers()
        self._populate_evpn_route_server_clients_on_peers()
        self._populate_mpls_route_reflector_clients_on_peers()
