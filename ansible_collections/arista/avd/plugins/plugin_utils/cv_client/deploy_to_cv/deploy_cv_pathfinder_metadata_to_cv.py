# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from copy import deepcopy
from logging import getLogger

from ...utils import get
from ..client import CVClient
from .models import CVDevice, CVPathfinderMetadata, DeployToCvResult

LOGGER = getLogger(__name__)

CV_PATHFINDER_METADATA_STUDIO_ID = "studio-caravan"
CV_PATHFINDER_DEFAULT_STUDIO_INPUTS = {"pathfinders": [], "pathgroups": [], "regions": [], "routers": [], "vrfs": [], "version": "3"}


def update_general_metadata(metadata: dict, studio_inputs: dict) -> None:
    """
    In-place update general metadata in studio_inputs.
    """
    studio_inputs.update(
        {
            "pathgroups": [
                {
                    "carriers": get(pathgroup, "carriers", required=True),
                    "importedCarriers": get(pathgroup, "imported_carriers", default=[]),
                    "name": get(pathgroup, "name", required=True),
                }
                for pathgroup in get(metadata, "pathgroups", required=True)
            ],
            "regions": get(metadata, "regions", required=True),
            "vrfs": get(metadata, "vrfs", default=[]),
        }
    )


def upsert_pathfinder(metadata: dict, device: CVDevice, studio_inputs: dict) -> None:
    """
    In-place insert / update metadata for one pathfinder device in studio_inputs.
    """
    LOGGER.info("deploy_cv_pathfinder_metadata_to_cv: upsert_pathfinder %s", device.hostname)

    pathfinder_metadata = {
        "inputs": {
            "value": {
                "sslProfileName": metadata.get("ssl_profile", ""),
                "vtepIp": metadata.get("vtep_ip", ""),
                "wanInterfaces": [
                    {
                        "inputs": {
                            "details": {
                                "carrier": interface.get("carrier", ""),
                                "circuitId": interface.get("circuit_id", ""),
                                "pathgroup": interface.get("pathgroup", ""),
                                "publicIp": interface.get("public_ip", ""),
                            }
                        },
                        "tags": {"query": f"interface:{interface.get('name', '')}@{device.serial_number}"},
                    }
                    for interface in metadata.get("interfaces", [])
                ],
            },
        },
        "tags": {"query": f"device:{device.serial_number}"},
    }

    found_index = None
    for index, router in enumerate(studio_inputs.get("pathfinders", [])):
        if get(router, "tags.query") == f"device:{device.serial_number}":
            found_index = index
            break

    if found_index is None:
        LOGGER.info("deploy_cv_pathfinder_metadata_to_cv: New pathfinder device, adding %s", device.hostname)
        studio_inputs.setdefault("pathfinders", []).append(pathfinder_metadata)
    else:
        LOGGER.info("deploy_cv_pathfinder_metadata_to_cv: Existing pathfinder device, updating %s", device.hostname)
        studio_inputs["pathfinders"][found_index] = pathfinder_metadata


def upsert_edge(metadata: dict, device: CVDevice, studio_inputs: dict) -> None:
    """
    In-place insert / update metadata for one edge device in studio_inputs.
    """
    LOGGER.info("deploy_cv_pathfinder_metadata_to_cv: upsert_edge %s", device.hostname)
    role = metadata.get("role", "")
    role = "transit" if "transit" in role else role
    edge_metadata = {
        "inputs": {
            "router": {
                "pathfinders": [{"vtepIp": pathfinder["vtep_ip"]} for pathfinder in metadata.get("pathfinders", [])],
                "region": metadata.get("region", ""),
                "role": role,
                "site": metadata.get("site", ""),
                "vtepIp": metadata.get("vtep_ip", ""),
                "wanInterfaces": [
                    {
                        "inputs": {
                            "details": {
                                "carrier": interface.get("carrier", ""),
                                "circuitId": interface.get("circuit_id", ""),
                                "pathgroup": interface.get("pathgroup", ""),
                            }
                        },
                        "tags": {"query": f"interface:{interface.get('name', '')}@{device.serial_number}"},
                    }
                    for interface in metadata.get("interfaces", [])
                ],
                "zone": metadata.get("zone", ""),
            },
        },
        "tags": {"query": f"device:{device.serial_number}"},
    }

    found_index = None
    for index, router in enumerate(studio_inputs.get("routers", [])):
        if get(router, "tags.query") == f"device:{device.serial_number}":
            found_index = index
            break

    if found_index is None:
        LOGGER.info("deploy_cv_pathfinder_metadata_to_cv: New edge/transit device, adding %s", device.hostname)
        studio_inputs.setdefault("routers", []).append(edge_metadata)
    else:
        LOGGER.info("deploy_cv_pathfinder_metadata_to_cv: Existing edge/transit device, updating %s", device.hostname)
        studio_inputs["routers"][found_index] = edge_metadata


async def deploy_cv_pathfinder_metadata_to_cv(cv_pathfinder_metadata: list[CVPathfinderMetadata], result: DeployToCvResult, cv_client: CVClient) -> None:
    """
    Deploy given CV Pathfinder metadata.

    The given metadata is parsed and updated onto the existing metadata studio inputs.

    TODO: Remove stale metadata - not sure how to deduct this.

    Example of metadata for an edge (below metadata.cv_pathfinder in structured config):
    ```yaml
    ---
    pathfinders:
      - public_ip: 10.2.3.4
    region: EMEA
    role: "transit region"
    site: Paris
    vtep_ip: 10.10.10.10
    interfaces:
      - name: Ethernet1
        carrier: BT
        circuit_id: ABC123
        pathgroup: INET
    zone: EU
    ```

    Example of metadata for a pathfinder (below metadata.cv_pathfinder in structured config):
    ```yaml
    ---
    role: pathfinder
    ssl_profile: VERYSAFE
    vtep_ip: 10.0.1.1
    interfaces:
      - carrier: BT
        circuit_id: XYZ987
        name: Ethernet2
        pathgroup: INET
        public_ip: 10.2.3.4
    pathgroups:
      - carriers:
          - name: BT
        imported_carriers:
          - name: 5GLTE
        name: INET
    regions:
      - id: 1
        name: EMEA
        zones:
          - id: 1
            name: DefaultZone
            sites:
              - id: 1
                name: Paris
                location: 99, rue de Rivoli, 75001 Paris
    vrfs:
      - avts:
          - constraints:
              jitter: 50
              latency: 200
              lossrate: 0.1
            description: Voice AVT
            id: 1
            name: Voice
            pathgroups:
              - name: INET
                preference: preferred
              - name: BACKUP
                preference: alternate
        name: HR
        vni: 100
    ```
    """

    LOGGER.info("deploy_cv_pathfinder_metadata_to_cv: Got cv_pathfinder_metadata for %s devices", len(cv_pathfinder_metadata))

    if not cv_pathfinder_metadata:
        return

    # Get existing studio inputs
    existing_studio_inputs = await cv_client.get_studio_inputs(
        studio_id=CV_PATHFINDER_METADATA_STUDIO_ID, workspace_id=result.workspace.id, default_value=CV_PATHFINDER_DEFAULT_STUDIO_INPUTS
    )
    studio_inputs = deepcopy(existing_studio_inputs)

    # Walk through given metadata, skip missing devices or invalid roles.
    # Sort between edges (including transit) and pathfinders
    edges: list[CVPathfinderMetadata] = []
    pathfinders: list[CVPathfinderMetadata] = []
    for device_metadata in cv_pathfinder_metadata:
        if not device_metadata.device._exists_on_cv:
            LOGGER.info(
                "deploy_cv_pathfinder_metadata_to_cv: Skipping metadata for device '%s' since the device is not found on CV.",
                device_metadata.device.serial_number,
            )
            result.skipped_cv_pathfinder_metadata.append(device_metadata)
            continue

        device_role = get(device_metadata.metadata, "role")

        if device_role in ["edge", "transit region"]:
            LOGGER.info(
                "deploy_cv_pathfinder_metadata_to_cv: Adding metadata for device '%s' as role '%s'.",
                device_metadata.device.serial_number,
                device_role,
            )
            edges.append(device_metadata)
        elif device_role == "pathfinder":
            LOGGER.info(
                "deploy_cv_pathfinder_metadata_to_cv: Adding metadata for device '%s' as role '%s'.",
                device_metadata.device.serial_number,
                device_role,
            )
            edges.append(device_metadata)
            pathfinders.append(device_metadata)
        else:
            LOGGER.info(
                "deploy_cv_pathfinder_metadata_to_cv: Skipping metadata for device '%s' since role '%s' is not supported.",
                device_metadata.device.serial_number,
                device_role,
            )
            result.skipped_cv_pathfinder_metadata.append(device_metadata)
            continue

    if pathfinders:
        # All pathfinders must have the same be general metadata, so we just set it in the studio based on the first one.
        update_general_metadata(metadata=pathfinders[0].metadata, studio_inputs=studio_inputs)

    for pathfinder in pathfinders:
        upsert_pathfinder(metadata=pathfinder.metadata, device=pathfinder.device, studio_inputs=studio_inputs)

    for edge in edges:
        upsert_edge(metadata=edge.metadata, device=edge.device, studio_inputs=studio_inputs)

    if studio_inputs != existing_studio_inputs:
        await cv_client.set_studio_inputs(studio_id=CV_PATHFINDER_METADATA_STUDIO_ID, workspace_id=result.workspace.id, inputs=studio_inputs)

    result.deployed_cv_pathfinder_metadata.extend(pathfinders + edges)
