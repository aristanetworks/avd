# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from pathlib import Path
from typing import Any

import pytest

from pyavd._cv.client import CVClient, CvVersion
from pyavd._cv.workflows.deploy_static_config_studio_manifest_to_cv import deploy_static_config_studio_manifest_to_cv
from pyavd._cv.workflows.models import AvdConfiglet, AvdContainer, AvdManifest, CVWorkspace, DeployToCvResult


# Test Data Fixtures
@pytest.fixture(scope="module")
def initial_manifest_data() -> dict[str, Any]:
    """Return the raw data for building the initial AvdManifest."""
    configlets = [
        {"name": "DC1-SPINES-BASE-CONFIG", "file_content": "hostname spine\n!"},
        {"name": "LEAFS-BASE-CONFIG", "file_content": "hostname leaf\n!"},
    ]
    containers = [
        AvdContainer(
            name="DC1_SPINES",
            tag_query="topology_hint_type:spine AND topology_hint_datacenter:DC1",
            description="Base configuration for DC1 Spines",
            configlets=("DC1-SPINES-BASE-CONFIG",),
        ),
        AvdContainer(
            name="DC1_LEAFS",
            tag_query="topology_hint_type:leaf AND topology_hint_datacenter:DC1",
            description="Base configuration for DC1 Leafs",
            configlets=("LEAFS-BASE-CONFIG",),
            sub_containers=(
                AvdContainer(
                    name="RACK1_LEAFS",
                    tag_query="topology_hint_rack:RACK1",
                    description="Rack 1 specific configuration",
                ),
            ),
        ),
    ]
    return {"configlets": configlets, "containers": containers}


@pytest.fixture
def avd_manifest_initial(tmp_path: Path, initial_manifest_data: dict[str, Any]) -> AvdManifest:
    """Create an AvdManifest instance for initial deployment and writes dummy configlet files."""
    configlet_objects = []
    for configlet_data in initial_manifest_data["configlets"]:
        config_file = tmp_path / f"{configlet_data['name']}.cfg"
        config_file.write_text(configlet_data["file_content"])
        configlet_objects.append(AvdConfiglet(name=configlet_data["name"], file=str(config_file)))

    return AvdManifest(
        configlets=tuple(configlet_objects),
        containers=tuple(initial_manifest_data["containers"]),
    )


@pytest.fixture
def avd_manifest_update(tmp_path: Path, initial_manifest_data: dict[str, Any]) -> AvdManifest:
    """Create an updated AvdManifest instance to test changes and deletion."""
    # New/Updated configlet definitions.
    configlet_list = initial_manifest_data["configlets"].copy()
    configlet_list.append({"name": "GLOBAL-BANNER", "file_content": "banner motd\nDual-DC\nEOF\n!"})

    configlet_objects = []
    for configlet_data in configlet_list:
        config_file = tmp_path / f"{configlet_data['name']}.cfg"
        config_file.write_text(configlet_data["file_content"])
        configlet_objects.append(AvdConfiglet(name=configlet_data["name"], file=str(config_file)))

    # Container definitions.
    container_spines = AvdContainer(
        name="DC1_SPINES",
        tag_query="topology_hint_type:spine AND topology_hint_datacenter:DC1",
        description="UPDATED description for DC1 Spines",  # CHANGED
        configlets=("DC1-SPINES-BASE-CONFIG",),
    )
    container_leafs = AvdContainer(
        name="DC1_LEAFS",
        tag_query="topology_hint_type:leaf AND topology_hint_datacenter:DC1",
        description="Base configuration for DC1 Leafs",
        configlets=("LEAFS-BASE-CONFIG", "GLOBAL-BANNER"),  # ADDED configlet
        # sub_containers field omitted, effectively removing RACK1_LEAFS
    )

    return AvdManifest(
        configlets=tuple(configlet_objects),
        containers=(container_spines, container_leafs),
    )


# Test Cases
@pytest.mark.asyncio
class TestDeployStaticConfigStudioManifest:
    """
    Test various scenarios of `deploy_static_config_studio_manifest_to_cv`.

    # TODO: Test deleting unused configlets.
    # TODO: Test changing AVD-managed root containers order.
    # TODO: Test stale AVD-managed root containers.
    """

    async def test_initial_deployment(self, cv_client: CVClient, avd_manifest_initial: AvdManifest) -> None:
        """
        Test case for the initial deployment.

        Expects all configlets and containers to be created.
        """
        cv_client._cv_version = CvVersion("2025.1.1")
        workspace = CVWorkspace(name="test_initial_deployment", id="test_initial_deployment")
        deployment_result = DeployToCvResult(workspace=workspace)

        await deploy_static_config_studio_manifest_to_cv(
            manifest=avd_manifest_initial,
            deployment_result=deployment_result,
            cv_client=cv_client,
        )

        # Check configlets: 2 created.
        assert len(deployment_result.deployed_static_config_configlets) == 2
        assert {cfg.name for cfg in deployment_result.deployed_static_config_configlets} == {
            "DC1-SPINES-BASE-CONFIG",
            "LEAFS-BASE-CONFIG",
        }

        # Check containers: 3 created (DC1_SPINES, DC1_LEAFS, RACK1_LEAFS).
        assert len(deployment_result.deployed_static_config_containers) == 3
        assert {cont.name for cont in deployment_result.deployed_static_config_containers} == {
            "DC1_SPINES",
            "DC1_LEAFS",
            "RACK1_LEAFS",
        }
        assert len(deployment_result.skipped_static_config_containers) == 0

    async def test_no_change_deployment(self, cv_client: CVClient, avd_manifest_initial: AvdManifest) -> None:
        """
        Test case for a subsequent run where the manifest has not changed.

        Expects all items to be skipped except configlets that are always pushed for now.
        """
        cv_client._cv_version = CvVersion("2025.1.1")
        workspace = CVWorkspace(name="test_no_change_deployment", id="test_no_change_deployment")
        deployment_result = DeployToCvResult(workspace=workspace)

        await deploy_static_config_studio_manifest_to_cv(
            manifest=avd_manifest_initial,
            deployment_result=deployment_result,
            cv_client=cv_client,
        )

        assert len(deployment_result.deployed_static_config_configlets) == 2
        assert len(deployment_result.deployed_static_config_containers) == 0
        assert len(deployment_result.skipped_static_config_containers) == 3

    async def test_update_and_prune_deployment(self, cv_client: CVClient, avd_manifest_update: AvdManifest) -> None:
        """
        Test case for an update run: modifies one container, adds a configlet, removes a container.

        Expects creations, updates, skips, and deletions to occur.
        """
        cv_client._cv_version = CvVersion("2025.1.1")
        workspace = CVWorkspace(name="test_update_and_prune_deployment", id="test_update_and_prune_deployment")
        deployment_result = DeployToCvResult(workspace=workspace)

        await deploy_static_config_studio_manifest_to_cv(
            manifest=avd_manifest_update,
            deployment_result=deployment_result,
            cv_client=cv_client,
        )

        # Check configlets: 3 total configlets should be pushed (2 existing + 1 new).
        assert len(deployment_result.deployed_static_config_configlets) == 3
        assert "GLOBAL-BANNER" in {cfg.name for cfg in deployment_result.deployed_static_config_configlets}

        # Check containers: 2 containers updated/deployed, 0 skipped.
        # DC1_SPINES is updated due to description change.
        # DC1_LEAFS is updated due to configlet list change and child removal.
        # RACK1_LEAFS deletion happens via API call, not tracked in deployment_result directly.
        assert len(deployment_result.deployed_static_config_containers) == 2
        assert len(deployment_result.skipped_static_config_containers) == 0
