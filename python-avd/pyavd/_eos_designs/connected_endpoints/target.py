# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Live mutable objects updated by the connected-endpoints builder."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
    from pyavd._eos_designs.structured_config.parent_interfaces import ParentInterfacesTracker


@dataclass(slots=True)
class ConnectedEndpointsBuildTarget:
    """
    Interface-only destination for a connected-endpoints build.

    All interface collections and the parent tracker are live objects owned by
    the caller. They are mutated in place and are never copied. A regular build
    passes the same objects already used by earlier generators, preserving
    collision handling and Python object identity. Isolated callers decide
    whether to start with empty or pre-populated collections.

    ACL and global sFlow fields are requirements discovered while interfaces are
    built. The core builder deliberately does not mutate non-interface structured
    config. The regular-build adapter consumes these requirements afterwards.
    """

    ethernet_interfaces: EosCliConfigGen.EthernetInterfaces
    """Live Ethernet interface list to update in place."""

    port_channel_interfaces: EosCliConfigGen.PortChannelInterfaces
    """Live Port-Channel interface list to update in place."""

    custom_ethernet_interfaces: EosCliConfigGen.EthernetInterfaces
    """Live custom structured-config overlays keyed by Ethernet interface name."""

    custom_port_channel_interfaces: EosCliConfigGen.PortChannelInterfaces
    """Live custom structured-config overlays keyed by Port-Channel interface name."""

    parent_interfaces_tracker: ParentInterfacesTracker
    """Live tracker receiving existing parents and parents required by generated subinterfaces."""

    referenced_mac_acls: list[str] = field(default_factory=list)
    """MAC ACL names referenced by generated interfaces, in first-encounter order."""

    referenced_ipv4_acls: list[str] = field(default_factory=list)
    """IPv4 ACL names referenced by generated 802.1X interface configuration, in first-encounter order."""

    referenced_ipv6_acls: list[str] = field(default_factory=list)
    """IPv6 ACL names referenced by generated 802.1X interface configuration, in first-encounter order."""

    sflow_required: bool = False
    """Whether at least one generated interface requires global sFlow configuration."""
