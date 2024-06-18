# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..shared_utils import SharedUtils


class InterfaceDescriptionData:
    """
    This class is used as transport of data between AVD code and
    instances of AvdInterfaceDescriptions class or subclasses hereof.

    Attributes starting with _ are internal and may change at any time.

    Other attributes are "stable" and changes follow semver practices:
    - Existing attributes will not be changed in terms of type and value, but the underlying code for cached_properties may change.
    - New attributes may be added in minor releases.
    - The __init__ method may change between minor versions as the data may need to be consumed from other sources.
    - Breaking changes may happen between major releases.
    """

    _shared_utils: SharedUtils
    description: str | None
    """Set description for interface"""
    interface: str | None
    """Local interface"""
    link_type: str | None
    """Type of connection. Like 'underlay_p2p' or 'underlay_l2'"""
    peer: str | None
    """Hostname of peer"""
    peer_interface: str | None
    """Interface of peer"""
    peer_channel_group_id: int | None
    """Port channel ID of peer"""
    port_channel_description: str | None
    """Set description for port-channel"""
    vrf: str | None
    """Interface VRF"""
    wan_carrier: str | None
    """The WAN Carrier this interface is connected to"""
    wan_circuit_id: str | None
    """The WAN Circuit ID for this interface."""

    def __init__(
        self,
        shared_utils: SharedUtils,
        description: str | None = None,
        interface: str | None = None,
        link_type: str | None = None,
        peer: str | None = None,
        peer_interface: str | None = None,
        peer_channel_group_id: int | None = None,
        port_channel_description: str | None = None,
        vrf: str | None = None,
        wan_carrier: str | None = None,
        wan_circuit_id: str | None = None,
    ):
        self._shared_utils = shared_utils
        self.description = description
        self.interface = interface
        self.link_type = link_type
        self.peer = peer
        self.peer_interface = peer_interface
        self.peer_channel_group_id = peer_channel_group_id
        self.port_channel_description = port_channel_description
        self.vrf = vrf
        self.wan_carrier = wan_carrier
        self.wan_circuit_id = wan_circuit_id

    @cached_property
    def mpls_overlay_role(self) -> str:
        return self._shared_utils.mpls_overlay_role

    @cached_property
    def overlay_routing_protocol(self) -> str:
        return self._shared_utils.overlay_routing_protocol

    @cached_property
    def mlag_peer(self) -> str:
        return self._shared_utils.mlag_peer

    @cached_property
    def mlag_port_channel_id(self) -> str:
        return self._shared_utils.mlag_port_channel_id

    @cached_property
    def mpls_lsr(self) -> str:
        return self._shared_utils.mpls_lsr

    @cached_property
    def type(self) -> str:
        return self._shared_utils.type
