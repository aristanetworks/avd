# Copyright (c) 2024-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

from pyavd._utils import default, get
from pyavd.api.fabric_documentation import (
    ACTDigitalTwin,
    ActLinkSettings,
    ActNodeSettings,
    ActNodeTypeSettings,
    FabricDocumentation,
)

if TYPE_CHECKING:
    from pyavd._eos_designs.eos_designs_facts.schema import EosDesignsFacts
    from pyavd._eos_designs.fabric_documentation_facts import FabricDocumentationFacts
    from pyavd._eos_designs.schema import EosDesigns


def get_fabric_documentation(
    avd_facts: dict[str, EosDesignsFacts],
    structured_configs: dict[str, dict],
    fabric_name: str,
    fabric_documentation: bool = True,
    include_connected_endpoints: bool = False,
    topology_csv: bool = False,
    p2p_links_csv: bool = False,
    toc: bool = True,
    digital_twin: tuple[bool, EosDesigns.DigitalTwin | None] = (False, None),
) -> FabricDocumentation:
    """
    Build and return the AVD fabric documentation.

    The returned object will contain the content of the requested documentation areas:
    - Fabric documentation as Markdown, optionally including connected endpoints.
    - Topology CSV containing the physical interface connections for every device.
    - P2P links CSV containing the Routed point-to-point links.

    Args:
        avd_facts: Dictionary of avd_facts as returned from `pyavd.get_avd_facts`.
        structured_configs: Dictionary of structured configurations for all devices, keyed by hostname.
        fabric_name: Name of the fabric. Only used for the main heading in the Markdown documentation.
        fabric_documentation: Returns fabric documentation when set to True.
        include_connected_endpoints: Includes connected endpoints in the fabric documentation when set to True.
        topology_csv: Returns topology CSV when set to True.
        p2p_links_csv: Returns P2P links CSV when set to True.
        toc: Skip TOC when set to False.
        digital_twin: PREVIEW: Returns Digital Twin topology when set to True.

    Returns:
        FabricDocumentation object containing the requested documentation areas.
    """
    from pyavd._eos_designs.fabric_documentation_facts import FabricDocumentationFacts  # noqa: PLC0415
    from pyavd.j2filters import add_md_toc  # noqa: PLC0415

    from .constants import EOS_DESIGNS_JINJA2_PRECOMPILED_TEMPLATE_PATH  # noqa: PLC0415
    from .templater import Templar  # noqa: PLC0415

    fabric_documentation_facts = FabricDocumentationFacts(avd_facts, structured_configs, fabric_name, include_connected_endpoints, toc)
    result = FabricDocumentation()
    doc_templar = Templar(precompiled_templates_path=EOS_DESIGNS_JINJA2_PRECOMPILED_TEMPLATE_PATH)
    if fabric_documentation:
        fabric_documentation_facts_dict = fabric_documentation_facts.render()
        result.fabric_documentation = doc_templar.render_template_from_file("fabric_documentation.j2", fabric_documentation_facts_dict)
        if include_connected_endpoints:
            result.fabric_documentation += "\n" + doc_templar.render_template_from_file("connected_endpoints_documentation.j2", fabric_documentation_facts_dict)
        if toc:
            result.fabric_documentation = add_md_toc(result.fabric_documentation, skip_lines=3)

    if topology_csv:
        result.topology_csv = _get_topology_csv(fabric_documentation_facts)
    if p2p_links_csv:
        result.p2p_links_csv = _get_p2p_links_csv(fabric_documentation_facts)
    if digital_twin[0] and digital_twin[1] is not None:
        result.digital_twin = _get_digital_twin(fabric_documentation_facts, digital_twin[1])

    return result


def _get_topology_csv(fabric_documentation_facts: FabricDocumentationFacts) -> str:
    from csv import writer  # noqa: PLC0415
    from io import StringIO  # noqa: PLC0415

    csv_content = StringIO()
    csv_writer = writer(csv_content, lineterminator="\n")
    csv_writer.writerow(("Node Type", "Node", "Node Interface", "Peer Type", "Peer Node", "Peer Interface", "Node Interface Enabled"))
    csv_writer.writerows(fabric_documentation_facts.get_physical_links())
    csv_content.seek(0)
    return csv_content.read()


def _get_p2p_links_csv(fabric_documentation_facts: FabricDocumentationFacts) -> str:
    from csv import writer  # noqa: PLC0415
    from io import StringIO  # noqa: PLC0415

    csv_content = StringIO()
    csv_writer = writer(csv_content, lineterminator="\n")
    csv_writer.writerow(("Type", "Node", "Node Interface", "Leaf IP Address", "Peer Type", "Peer Node", "Peer Interface", "Peer IP Address"))
    csv_writer.writerows(
        (
            topology_link["type"],
            topology_link["node"],
            topology_link["node_interface"],
            topology_link["node_ip_address"],
            topology_link["peer_type"],
            topology_link["peer"],
            topology_link["peer_interface"],
            topology_link["peer_ip_address"],
        )
        for topology_link in fabric_documentation_facts.topology_links
        if topology_link["routed"]
    )
    csv_content.seek(0)
    return csv_content.read()


def _get_digital_twin(fabric_documentation_facts: FabricDocumentationFacts, digital_twin: EosDesigns.DigitalTwin) -> ACTDigitalTwin | None:
    match digital_twin.environment:
        case "act":
            return _get_digital_twin_act(fabric_documentation_facts, digital_twin)
        case _:
            return None


def _get_digital_twin_act(fabric_documentation_facts: FabricDocumentationFacts, digital_twin: EosDesigns.DigitalTwin) -> ACTDigitalTwin:
    """
    Build and return the ACT topology data.

    The returned object will contain information required to render ACT topology file:
    - ACT global node definitions.
    - ACT individual node definitions.
    - ACT node links.

    Args:
        fabric_documentation_facts: FabricDocumentationFacts object holding facts used for generating Fabric Documentation.
        digital_twin: EosDesigns.DigitalTwin object holding facts used to generate Digital Twin artifacts.

    Returns:
        ACTDigitalTwin object containing information to render ACT topology file.
    """
    digital_twin_node_types: dict[str, ActNodeTypeSettings | None] = {
        "cloudeos": None,
        "cvp": None,
        "generic": None,
        "third-party": None,
        "tools-server": None,
        "veos": None,
    }
    digital_twin_devices: list[dict[str, ActNodeSettings]] = []
    device_list: list[str] = list(fabric_documentation_facts.avd_facts)
    for device in sorted(device_list):
        if (
            digital_twin_node_type := get(fabric_documentation_facts.structured_configs, f"{device}..metadata..digital_twin..node_type", separator="..")
        ) in digital_twin_node_types and not digital_twin_node_types[digital_twin_node_type]:
            match digital_twin_node_type:
                case "cloudeos":
                    username = digital_twin.act_cloudeos_username
                    password = digital_twin.act_cloudeos_password
                case "third-party":
                    username = digital_twin.act_third_party_username
                    password = digital_twin.act_third_party_password
                case "veos":
                    username = digital_twin.act_veos_username
                    password = digital_twin.act_veos_password
                case _:
                    # TODO: Raise
                    raise ValueError
            digital_twin_node_types[digital_twin_node_type] = ActNodeTypeSettings(username=username, password=password)

        digital_twin_devices.append(
            {
                device: ActNodeSettings(
                    # All three values are enforced as non-empty strings during the generation of the metadata part of the structured_config
                    node_type=digital_twin_node_type,
                    ip_addr=get(fabric_documentation_facts.structured_configs, f"{device}..metadata..digital_twin..ip_addr", separator=".."),
                    version=get(fabric_documentation_facts.structured_configs, f"{device}..metadata..digital_twin..version", separator=".."),
                )
            }
        )

    # Process auxiliary_systems
    if auxiliary_systems := digital_twin.auxiliary_systems:
        for auxiliary_system in auxiliary_systems:
            node_name = auxiliary_system.node_name
            node_type = auxiliary_system.node_type
            match node_type:
                case "act-tools-server":
                    matched_node_type = "tools-server"
                    username = digital_twin.act_tools_server_username
                    password = digital_twin.act_tools_server_password
                    if not (mgmt_ip := auxiliary_system.act_mgmt_ip):
                        # TODO: Raise as IP is mandatory
                        raise ValueError
                    os_version = default(auxiliary_system.act_os_version, digital_twin.act_tools_server_os_version)
                case _:
                    continue
            # Update digital_twin_node_types if matching node type has not been defined yet
            if not digital_twin_node_types[matched_node_type]:
                digital_twin_node_types[matched_node_type] = ActNodeTypeSettings(username=username, password=password)
            # Check for overlapping names between fabric and auxiliary nodes
            if node_name in digital_twin_devices:
                # TODO: Raise, name of the auxiliary node matches the name of one of the fabrci devices
                pass
            # Append auxiliary node to the list of ACT nodes
            digital_twin_devices.append({node_name: ActNodeSettings(node_type=matched_node_type, ip_addr=mgmt_ip, version=os_version)})

    return ACTDigitalTwin(
        nodes=tuple(digital_twin_devices),
        links=tuple(
            ActLinkSettings(
                connection=(f"{topology_link['node']}:{topology_link['node_interface']}", f"{topology_link['peer']}:{topology_link['peer_interface']}")
            )
            for topology_link in fabric_documentation_facts.topology_links
            # Skip connections where at least one of the contributing sources is not a non-empty string
            if (
                isinstance(topology_link["node"], str)
                and topology_link["node"]
                and isinstance(topology_link["node_interface"], str)
                and topology_link["node_interface"]
                and isinstance(topology_link["peer"], str)
                and topology_link["peer"]
                and isinstance(topology_link["peer_interface"], str)
                and topology_link["peer_interface"]
            )
        ),
        cloudeos=digital_twin_node_types["cloudeos"],
        cvp=digital_twin_node_types["cvp"],
        generic=digital_twin_node_types["generic"],
        third_party=digital_twin_node_types["third-party"],
        tools_server=digital_twin_node_types["tools-server"],
        veos=digital_twin_node_types["veos"],
    )
