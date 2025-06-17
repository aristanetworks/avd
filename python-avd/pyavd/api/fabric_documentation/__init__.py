# Copyright (c) 2024-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

from dataclasses import dataclass


@dataclass(frozen=True)
class DigitalTwinFabricDocumentationActLink:
    connection: tuple[str | None, str | None]


@dataclass(frozen=True)
class DigitalTwinFabricDocumentationActNodeType:
    username: str | None = None
    password: str | None = None


@dataclass(frozen=True)
class DigitalTwinFabricDocumentationActNode:
    node_type: str | None = None
    ip_addr: str | None = None
    version: str | None = None


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
    digital_twin: object | None = None
