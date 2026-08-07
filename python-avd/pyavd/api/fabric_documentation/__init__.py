# Copyright (c) 2024-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

from dataclasses import dataclass, field


@dataclass(frozen=True)
class ActLinkSettings:
    connection: tuple[str, str]


@dataclass(frozen=True)
class ContainerlabLinkSettings:
    endpoints: tuple[str, str]


@dataclass(frozen=True)
class ContainerlabNode:
    mgmt_ipv4: str = field(metadata={"yaml_key": "mgmt-ipv4"})


@dataclass(frozen=True)
class ContainerlabDefaults:
    kind: str


@dataclass(frozen=True)
class ContainerlabKind:
    enforce_startup_config: bool = field(metadata={"yaml_key": "enforce-startup-config"})
    image: str
    binds: tuple[str, ...] | None = None


@dataclass(frozen=True)
class ContainerlabMgmt:
    network: str
    ipv4_subnet: str = field(metadata={"yaml_key": "ipv4-subnet"})


@dataclass(frozen=True)
class ContainerlabTopology:
    defaults: ContainerlabDefaults
    kinds: dict[str, ContainerlabKind]
    nodes: dict[str, ContainerlabNode]
    links: tuple[ContainerlabLinkSettings, ...]


@dataclass(frozen=True)
class ActNodeTypeSettings:
    username: str
    password: str


@dataclass(frozen=True)
class ActNodeSettings:
    node_type: str
    ip_addr: str | None
    version: str
    # internet_access attribute is only applicable to cloudeos and veos node types and is ignored by ACT for all other node types
    internet_access: bool | None
    ports: tuple[str, ...] | None


@dataclass(frozen=True)
class ACTDigitalTwin:
    """ACT Digital Twin fabric documentation dataclass."""

    nodes: tuple[dict[str, ActNodeSettings], ...]
    cloudeos: ActNodeTypeSettings | None = None
    cvp: ActNodeTypeSettings | None = None
    generic: ActNodeTypeSettings | None = None
    third_party: ActNodeTypeSettings | None = field(default=None, metadata={"yaml_key": "third-party"})
    tools_server: ActNodeTypeSettings | None = field(default=None, metadata={"yaml_key": "tools-server"})
    veos: ActNodeTypeSettings | None = None
    links: tuple[ActLinkSettings, ...] | None = None


@dataclass(frozen=True)
class ContainerlabDigitalTwin:
    """Containerlab Digital Twin fabric documentation dataclass."""

    name: str
    prefix: str
    mgmt: ContainerlabMgmt
    topology: ContainerlabTopology
    interface_mapping: dict[str, dict[str, str]] | None = None


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
    digital_twin: ACTDigitalTwin | ContainerlabDigitalTwin | None = None
