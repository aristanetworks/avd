# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from copy import deepcopy
from functools import lru_cache
from logging import getLogger

from ...utils import get
from ..client import CVClient
from .models import CVDevice, CVPathfinderMetadata, DeployToCvResult

LOGGER = getLogger(__name__)

CV_PATHFINDER_METADATA_STUDIO_ID = "cv-pathfinder-metadata"
CV_PATHFINDER_DEFAULT_STUDIO_INPUTS = {"pathfinders": [], "pathgroups": [], "regions": [], "routers": [], "vrfs": [], "version": 3}


@lru_cache
def get_pathfinder_serial_number_from_public_ip(public_ip: str, studio_inputs: dict) -> str:
    """
    Look for the public IP across all pathfinders and their WAN interfaces.
    Return the serial number if a match is found. Otherwise raise LookupError.
    """
    LOGGER.info("deploy_cv_pathfinder_metadata_to_cv: get_pathfinder_serial_number_from_public_ip %s", public_ip)

    for pathfinder in studio_inputs["pathfinders"]:
        for interface in get(pathfinder, "inputs.router.wanInterfaces", required=True):
            if get(interface, "inputs.details.publicIP", required=True) == public_ip:
                return str(get(pathfinder, "tags.query", required=True)).removeprefix("device:")

    raise LookupError(f"Unable to find serial number for pathfinder with public IP {public_ip}.")


def update_general_metadata(metadata: dict, studio_inputs: dict) -> None:
    """
    In-place update general metadata in studio_inputs.
    """
    studio_inputs.update()


def upsert_pathfinder(metadata: dict, device: CVDevice, studio_inputs: dict) -> None:
    """
    In-place insert / update metadata for one pathfinder device in studio_inputs.
    """
    LOGGER.info("deploy_cv_pathfinder_metadata_to_cv: upsert_pathfinder %s", device.hostname)

    pathfinder_metadata = {
        "inputs": {
            "router": {
                "sslProfileName": metadata.get("ssl_profile", ""),
                "vtepIP": metadata.get("vtep_ip", ""),
                "wanInterfaces": [
                    {
                        "inputs": {
                            "details": {
                                "carrier": interface.get("carrier", ""),
                                "circuitId": interface.get("circuit_id", ""),
                                "pathgroup": interface.get("pathgroup", ""),
                                "publicIP": interface.get("public_ip", ""),
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
    for index, router in enumerate(studio_inputs["routers"]):
        if get(router, "tags.query") == f"device:{device.serial_number}":
            found_index = index
            break

    if found_index is None:
        LOGGER.info("deploy_cv_pathfinder_metadata_to_cv: New pathfinder device, adding %s", device.hostname)
        studio_inputs["routers"].append(pathfinder_metadata)
    else:
        LOGGER.info("deploy_cv_pathfinder_metadata_to_cv: Existing pathfinder device, updating %s", device.hostname)
        studio_inputs["routers"][found_index] = pathfinder_metadata


def upsert_edge(metadata: dict, device: CVDevice, studio_inputs: dict) -> None:
    """
    In-place insert / update metadata for one edge device in studio_inputs.
    """
    LOGGER.info("deploy_cv_pathfinder_metadata_to_cv: upsert_edge %s", device.hostname)

    edge_metadata = {
        "inputs": {
            "router": {
                "pathfinders": [
                    {
                        "pathfinder": {
                            "tags": {
                                "query": f"device:{get_pathfinder_serial_number_from_public_ip(public_ip, studio_inputs)}",
                            }
                        },
                    }
                    for public_ip in metadata.get("pathfinder_public_ips", [])
                ],
                "region": metadata.get("region", ""),
                "role": metadata.get("role", ""),
                "site": metadata.get("site", ""),
                "vtepIP": metadata.get("vtep_ip", ""),
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
    for index, router in enumerate(studio_inputs["routers"]):
        if get(router, "tags.query") == f"device:{device.serial_number}":
            found_index = index
            break

    if found_index is None:
        LOGGER.info("deploy_cv_pathfinder_metadata_to_cv: New edge/transit device, adding %s", device.hostname)
        studio_inputs["routers"].append(edge_metadata)
    else:
        LOGGER.info("deploy_cv_pathfinder_metadata_to_cv: Existing edge/transit device, updating %s", device.hostname)
        studio_inputs["routers"][found_index] = edge_metadata


async def deploy_cv_pathfinder_metadata_to_cv(cv_pathfinder_metadata: list[CVPathfinderMetadata], result: DeployToCvResult, cv_client: CVClient) -> None:
    """
    Deploy given CV Pathfinder metadata.

    The given metadata is parsed and updated onto the existing metadata studio inputs.

    TODO: Remove stale metadata - not sure how to deduct this.
    """

    LOGGER.info("deploy_cv_pathfinder_metadata_to_cv: %s", len(cv_pathfinder_metadata))

    if not cv_pathfinder_metadata:
        return

    # Get existing studio inputs
    existing_studio_inputs = await cv_client.get_studio_inputs(
        studio_id=CV_PATHFINDER_METADATA_STUDIO_ID, workspace_id=result.workspace.id, default=CV_PATHFINDER_DEFAULT_STUDIO_INPUTS
    )
    studio_inputs = deepcopy(existing_studio_inputs)

    # Walk through given metadata, skip missing devices or invalid roles.
    # Sort between edges (including transit) and pathfinders
    edges: list[CVPathfinderMetadata] = []
    pathfinders: list[CVPathfinderMetadata] = []
    for device_metadata in cv_pathfinder_metadata:
        if not device_metadata.device._exists_on_cv:
            result.skipped_cv_pathfinder_metadata.append(device_metadata)
            continue

        device_role = get(device_metadata.metadata, "role")

        if device_role in ["edge", "transit region"]:
            edges.append(device_metadata)
        elif device_role == "pathfinder":
            pathfinders.append(device_metadata)
        else:
            result.skipped_cv_pathfinder_metadata.append(device_metadata)
            continue

    if pathfinders:
        # All pathfinders must have the same be general metadata, so we just set it in the studio based on the first one.
        update_general_metadata(metadata=pathfinders[0], studio_inputs=studio_inputs)

    for pathfinder in pathfinders:
        upsert_pathfinder(metadata=pathfinder.metadata, device=pathfinder.device, studio_inputs=studio_inputs)

    for edge in edges:
        upsert_edge(metadata=edge.metadata, device=edge.device, studio_inputs=studio_inputs)

    if studio_inputs != existing_studio_inputs:
        await cv_client.set_studio_inputs(studio_id=CV_PATHFINDER_METADATA_STUDIO_ID, workspace_id=result.workspace.id, inputs=studio_inputs)

    result.deployed_cv_pathfinder_metadata.extend(pathfinders + edges)
