# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ansible_collections.arista.avd.plugins.plugin_utils.eos_designs_shared_utils import SharedUtils


class UtilsMixin:
    """
    Mixin Class with internal functions.
    Class should only be used as Mixin to an AvdInterfaceDescriptions class
    """

    _hostvars: dict
    shared_utils: SharedUtils

    @cached_property
    def _mpls_overlay_role(self) -> str:
        """TODO: AVD5.0.0 remove this since it has been replaced by DescriptionData."""
        return self.shared_utils.mpls_overlay_role

    @cached_property
    def _overlay_routing_protocol(self) -> str:
        """TODO: AVD5.0.0 remove this since it has been replaced by DescriptionData."""
        return self.shared_utils.overlay_routing_protocol

    @cached_property
    def _mlag_peer(self) -> str:
        """TODO: AVD5.0.0 remove this since it has been replaced by DescriptionData."""
        return self.shared_utils.mlag_peer

    @cached_property
    def _mlag_port_channel_id(self) -> str:
        """TODO: AVD5.0.0 remove this since it has been replaced by DescriptionData."""
        return self.shared_utils.mlag_port_channel_id

    @cached_property
    def _mpls_lsr(self) -> str:
        """TODO: AVD5.0.0 remove this since it has been replaced by DescriptionData."""
        return self.shared_utils.mpls_lsr
