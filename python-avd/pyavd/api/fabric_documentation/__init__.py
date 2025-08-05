# Copyright (c) 2024-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

from dataclasses import dataclass


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
    # internet_access attribute is only applicable to cloudeos and veos node types and is ignored by ACT for all other node types
    internet_access: bool | None


@dataclass(frozen=True)
class ACTDigitalTwin:
    """ACT Digital Twin fabric documentation dataclass."""

    nodes: tuple[dict[str, ActNodeSettings], ...]
    cloudeos: ActNodeTypeSettings | None = None
    cvp: ActNodeTypeSettings | None = None
    generic: ActNodeTypeSettings | None = None
    third_party: ActNodeTypeSettings | None = None
    tools_server: ActNodeTypeSettings | None = None
    veos: ActNodeTypeSettings | None = None
    links: tuple[ActLinkSettings, ...] | None = None


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
