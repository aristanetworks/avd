# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from copy import deepcopy
from enum import Enum
from logging import getLogger
from typing import Literal

from ...password_utils.password import simple_7_decrypt
from ...utils import get
from ..client import CVClient
from .models import CVDevice, CVPathfinderMetadata, DeployToCvResult

LOGGER = getLogger(__name__)

CV_PATHFINDER_METADATA_STUDIO_ID = "studio-avd-pathfinder-metadata"
CV_PATHFINDER_DEFAULT_STUDIO_INPUTS = {
    "pathfinders": [],
    "pathgroups": [],
    "regions": [],
    "routers": [],
    "vrfs": [],
}


class StudioVersion(Enum):
    """Supported cv-pathfinder metadata studio versions"""

    v3_2 = 3.2
    v3_3 = 3.3
    v3_4 = 3.4


FEATURE_MIN_VERSION = {
    "pathfinder_location": StudioVersion.v3_4,
    "internet_exit_zscaler": StudioVersion.v3_4,
}
FEATURE = Literal["pathfinder_location"]


async def get_metadata_studio_version(result: DeployToCvResult, cv_client: CVClient) -> StudioVersion | None:
    """
    Extract the version from the metadata studio.
    This is stored as a default value on the studioVersion field.
    """
    studio = await cv_client.get_studio(CV_PATHFINDER_METADATA_STUDIO_ID, result.workspace.id)
    studio_version_field = get(studio.input_schema.fields.values, "studioVersion")
    version = studio_version_field.string_props.default_value
    LOGGER.info("deploy_cv_pathfinder_metadata_to_cv: Found metadata studio version: %s", version)
    try:
        return StudioVersion(float(version))
    except ValueError:
        accepted_versions = [str(v.value) for v in StudioVersion]
        warning = (
            f"deploy_cv_pathfinder_metadata_to_cv: Got invalid metadata studio version '{version}'."
            f"This plugin only accepts versions '{accepted_versions}'. Skipping upload of metadata."
        )
        LOGGER.info(warning)
        result.warnings.append(warning)
        return None


def is_feature_supported(feature: FEATURE, studio_version: StudioVersion) -> bool:
    return studio_version.value >= FEATURE_MIN_VERSION.get(feature, 0).value


def update_general_metadata(metadata: dict, studio_inputs: dict) -> None:
    """
    In-place update general metadata in studio_inputs.
    """
    # Temporary fix for default values in metadata studio
    for vrf in get(metadata, "vrfs", default=[]):
        for avt in get(vrf, "avts", default=[]):
            constraints: dict = avt.setdefault("constraints", {})
            constraints.setdefault("latency", 4294967295)
            constraints.setdefault("jitter", 4294967295)
            constraints.setdefault("lossrate", 99.0)

    studio_inputs.update(
        {
            "pathgroups": [
                {
                    "carriers": get(pathgroup, "carriers", default=[]),
                    "importedCarriers": get(pathgroup, "imported_carriers", default=[]),
                    "name": get(pathgroup, "name", required=True),
                }
                for pathgroup in get(metadata, "pathgroups", default=[])
            ],
            "regions": get(metadata, "regions", default=[]),
            "vrfs": get(metadata, "vrfs", default=[]),
        }
    )


def upsert_pathfinder(metadata: dict, device: CVDevice, studio_inputs: dict, studio_version: StudioVersion) -> None:
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

    if is_feature_supported("pathfinder_location", studio_version):
        pathfinder_metadata.update(
            {
                "region": metadata.get("region", ""),
                "site": metadata.get("site", ""),
                "address": metadata.get("address", ""),
            }
        )
    else:
        LOGGER.info(
            "deploy_cv_pathfinder_metadata_to_cv: Ignoring Pathfinder location information since it is not supported by metadata studio version %s.",
            studio_version,
        )

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


def upsert_edge(metadata: dict, device: CVDevice, studio_inputs: dict, studio_version: StudioVersion) -> None:
    """
    In-place insert / update metadata for one edge device in studio_inputs.
    """
    LOGGER.info("deploy_cv_pathfinder_metadata_to_cv: upsert_edge %s", device.hostname)
    edge_metadata = {
        "inputs": {
            "router": {
                "sslProfileName": metadata.get("ssl_profile", ""),
                "pathfinders": [{"vtepIp": pathfinder["vtep_ip"]} for pathfinder in metadata.get("pathfinders", [])],
                "region": metadata.get("region", ""),
                "role": metadata.get("role", ""),
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
    if internet_exit_metadata := generate_internet_exit_metadata(metadata, device, studio_version):
        edge_metadata["inputs"]["router"]["services"] = internet_exit_metadata

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
    ssl_profile: VERYSAFE
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

    if (studio_version := await get_metadata_studio_version(result, cv_client)) is None:
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
        upsert_pathfinder(metadata=pathfinder.metadata, device=pathfinder.device, studio_inputs=studio_inputs, studio_version=studio_version)

    for edge in edges:
        upsert_edge(metadata=edge.metadata, device=edge.device, studio_inputs=studio_inputs, studio_version=studio_version)

    if studio_inputs != existing_studio_inputs:
        await cv_client.set_studio_inputs(studio_id=CV_PATHFINDER_METADATA_STUDIO_ID, workspace_id=result.workspace.id, inputs=studio_inputs)

    result.deployed_cv_pathfinder_metadata.extend(pathfinders + edges)


def generate_internet_exit_metadata(metadata: dict, device: CVDevice, studio_version: StudioVersion) -> dict:
    """
    Generate internet-exit related metadata for one device.
    To be inserted into edge router metadata under "services"
    """
    if (internet_exit_policies := get(metadata, "internet_exit_policies")) is None:
        LOGGER.info("deploy_cv_pathfinder_metadata_to_cv: Did not find 'internet_exit_policies' for device: %s", device.hostname)
        return []

    LOGGER.info("deploy_cv_pathfinder_metadata_to_cv: Found %s 'internet_exit_policies' for device: %s", len(internet_exit_policies), device.hostname)

    services_dict = {}
    for internet_exit_policy in internet_exit_policies:
        # We currently only support zscaler
        if internet_exit_policy.get("type") != "zscaler":
            LOGGER.info(
                "deploy_cv_pathfinder_metadata_to_cv: Ignoring unsupported internet exit policy '%s' with type '%s' for device: %s.",
                internet_exit_policies.get("name"),
                internet_exit_policy.get("type"),
                device.hostname,
            )
            continue

        if not is_feature_supported("internet_exit_zscaler", studio_version):
            LOGGER.info(
                "deploy_cv_pathfinder_metadata_to_cv: Ignoring Pathfinder location information since it is not supported by metadata studio version %s.",
                studio_version,
            )
            continue

        policy_name = internet_exit_policy["name"]
        services_dict.setdefault("zscaler", {"locations": [], "tunnels": []})
        services_dict["zscaler"]["locations"].append(
            {
                "name": f"{device.hostname}_{policy_name}",
                "description": f"Location corresponding to {device.hostname} for internet-exit policy {policy_name}.",
                "city": internet_exit_policy["city"],
                "country": internet_exit_policy["country"],
                "uploadBandwidth": internet_exit_policy.get("upload_bandwidth"),
                "downloadBandwidth": internet_exit_policy.get("download_bandwidth"),
                "firewallEnabled": internet_exit_policy["firewall"],
                "ipsControl": internet_exit_policy["ips_control"],
                "aupEnabled": internet_exit_policy["acceptable_use_policy"],
                "vpnCredentials": [
                    {
                        "fqdn": vpn_credential["fqdn"],
                        "comments": f"Credential for {device.hostname} internet-exit policy {policy_name}",
                        "vpnType": vpn_credential["vpn_type"],
                        "presharedKey": simple_7_decrypt(vpn_credential["pre_shared_key"]),
                    }
                    for vpn_credential in internet_exit_policy["vpn_credentials"]
                ],
            }
        )
        services_dict["zscaler"]["tunnels"].extend(
            {
                "name": tunnel["name"],
                "preference": tunnel["preference"],
            }
            for tunnel in internet_exit_policy["tunnels"]
        )

    return services_dict
