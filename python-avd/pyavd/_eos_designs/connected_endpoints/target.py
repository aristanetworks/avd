# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Live mutable objects updated by the connected-endpoints builder."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
    from pyavd._eos_designs.structured_config.parent_interfaces import ParentInterfacesTracker
    from pyavd._schema.models.avd_base import AvdListMergeStrategy


class ConnectedEndpointsStructuredConfigProtocol(Protocol):
    """Interface collections the builder may access on a structured-config model."""

    @property
    def ethernet_interfaces(self) -> EosCliConfigGen.EthernetInterfaces:
        """Live Ethernet interface list."""
        ...  # pylint: disable=unnecessary-ellipsis

    @property
    def port_channel_interfaces(self) -> EosCliConfigGen.PortChannelInterfaces:
        """Live Port-Channel interface list."""
        ...  # pylint: disable=unnecessary-ellipsis


class ConnectedEndpointsCustomStructuredConfigsProtocol(Protocol):
    """Custom structured-config state used by the connected-endpoints builder."""

    @property
    def nested(self) -> ConnectedEndpointsStructuredConfigProtocol:
        """Structured-config model receiving custom interface overlays."""
        ...  # pylint: disable=unnecessary-ellipsis

    @property
    def list_merge_strategy(self) -> AvdListMergeStrategy:
        """Normalized strategy used to merge custom interface configuration."""
        ...  # pylint: disable=unnecessary-ellipsis


@dataclass(slots=True)
class ConnectedEndpointsBuildTarget:
    """
    Interface-only destination for a connected-endpoints build.

    The structured-config models and parent tracker are live objects owned by
    the caller. Their interface collections are mutated in place and are never
    copied. A regular build passes the same models already used by earlier
    generators, preserving collision handling and Python object identity.
    Isolated callers decide whether to start with empty or pre-populated models.

    The structured-config protocol deliberately exposes only Ethernet and
    Port-Channel interface collections. Passing the parent models instead of
    their collections also avoids creating empty lists unless the builder
    actually accesses them.

    ACL and global sFlow fields are requirements discovered while interfaces are
    built. The core builder deliberately does not mutate non-interface structured
    config. The regular-build adapter consumes these requirements afterwards.
    """

    structured_config: ConnectedEndpointsStructuredConfigProtocol
    """Live structured-config model receiving generated interface configuration."""

    custom_structured_configs: ConnectedEndpointsCustomStructuredConfigsProtocol
    """Live custom structured-config state receiving interface overlays."""

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
