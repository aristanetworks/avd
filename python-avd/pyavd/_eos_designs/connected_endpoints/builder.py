# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Orchestration for building connected-endpoint interfaces."""

from __future__ import annotations

from typing import TYPE_CHECKING

from .ethernet_interfaces import EthernetInterfacesMixin
from .port_channel_interfaces import PortChannelInterfacesMixin
from .utils import UtilsMixin

if TYPE_CHECKING:
    from .context import ConnectedEndpointsBuildContext
    from .target import ConnectedEndpointsBuildTarget


class ConnectedEndpointsBuilder(EthernetInterfacesMixin, PortChannelInterfacesMixin, UtilsMixin):
    """Stateful implementation behind :func:`build_connected_endpoints`."""

    def __init__(self, context: ConnectedEndpointsBuildContext, target: ConnectedEndpointsBuildTarget) -> None:
        self.context = context
        self.target = target

    def build(self) -> None:
        """Build Ethernet interfaces first, then Port-Channel interfaces."""
        self.ethernet_interfaces()
        self.port_channel_interfaces()


def build_connected_endpoints(context: ConnectedEndpointsBuildContext, target: ConnectedEndpointsBuildTarget) -> None:
    """
    Build connected-endpoint and network-port interfaces in place.

    Regular builds construct ``context`` from full eos-designs inputs and pass
    their existing interface collections in ``target``. An isolated consumer can
    construct the same context and choose empty or pre-populated target lists.
    Only interface collections, interface custom-config overlays, the parent
    tracker, and declared non-interface requirements are changed.
    """
    ConnectedEndpointsBuilder(context, target).build()
