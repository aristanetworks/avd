# Copyright (c) 2024-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class ActLinkSettings:
    connection: tuple[str, str]


@dataclass(frozen=True)
class ActNodeTypeSettings:
    username: str
    password: str


@dataclass(frozen=True)
class ActNodeSettings:
    node_type: str
    ip_addr: str
    version: str


class ACTDigitalTwin(Protocol):
    """Protocol describing the structure of the dynamically generated ACT Digital Twin fabric documentation dataclass."""

    # Always present attributes
    nodes: tuple[dict[str, ActNodeSettings], ...]
    # Dynamically-added attributes
    # links attribute may be missing if fabric has no links defined
    links: tuple[ActLinkSettings, ...] | None
    cloudeos: ActNodeTypeSettings | None
    cvp: ActNodeTypeSettings | None
    generic: ActNodeTypeSettings | None
    third_party: ActNodeTypeSettings | None
    tools_server: ActNodeTypeSettings | None
    veos: ActNodeTypeSettings | None


class FabricDocumentation:
    """
    Object containing the requested documentation.

    Attributes:
        fabric_documentation: Fabric Documentation as Markdown.
        topology_csv: Topology CSV containing the physical interface connections for every device.
        p2p_links_csv: P2P links CSV containing the Routed point-to-point links.
        digital_twin: Immutable dataclass instance containing Digital Twin topology information.
    """

    fabric_documentation: str = ""
    topology_csv: str = ""
    p2p_links_csv: str = ""
    digital_twin: ACTDigitalTwin | None = None
