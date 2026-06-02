# Copyright (c) 2025-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

from contextlib import AbstractContextManager
from contextlib import nullcontext as does_not_raise
from logging import DEBUG
from pathlib import Path
from typing import Any
from unittest.mock import patch

import pytest
from grpclib.config import Configuration

from pyavd._cv.client.exceptions import CVManifestError
from pyavd._cv.workflows.models import (
    AVD_ENTITY_PREFIX,
    AvdConfiglet,
    AvdContainer,
    AvdManifest,
    CVGRPCChannelConfiguration,
    CVGRPCKeepalives,
    CVManifest,
)

from .helpers import generate_id

# === Test Fixtures ===


@pytest.fixture
def complex_avd_manifest() -> AvdManifest:
    """Provides a complex, valid AVD manifest with nested containers and configlets."""
    # Configlets definition.
    configlet1 = AvdConfiglet(name="configlet_global", file=Path("path/to/global.cfg"))
    configlet2 = AvdConfiglet(name="configlet_leaf", file=Path("path/to/leaf.cfg"))
    configlet3 = AvdConfiglet(name="configlet_extra", file=Path("path/to/extra.cfg"))

    # Container hierarchy definition.
    container_leaf_1a = AvdContainer(
        name="LEAF_GROUP_A",
        tag_query="rack:1a AND role:leaf",
        description="Leaves in Rack 1A",
        configlets=("configlet_leaf",),
    )
    container_leaf_1b = AvdContainer(
        name="LEAF_GROUP_B",
        tag_query="rack:1b AND role:leaf",
        description="Leaves in Rack 1B",
        match_policy="match_first",  # Test non-default match policy
    )
    container_rack1 = AvdContainer(
        name="RACK_1",
        tag_query="rack:1",
        description="All devices in Rack 1",
        configlets=("configlet_global",),
        sub_containers=(container_leaf_1a, container_leaf_1b),
    )
    container_rack2 = AvdContainer(
        name="RACK_2",
        tag_query="rack:2",
        description="All devices in Rack 2",
        configlets=(),  # Test empty configlet list
    )

    return AvdManifest(
        configlets=(configlet1, configlet2, configlet3),
        containers=(container_rack1, container_rack2),
    )


# === Test Cases ===


class TestCVManifestGeneration:
    def test_successful_conversion(self, complex_avd_manifest: AvdManifest) -> None:
        """Tests successful conversion of a complex manifest to a CVManifest."""
        cv_manifest = CVManifest.from_avd_manifest(complex_avd_manifest)

        # Verify counts.
        assert len(cv_manifest.configlets) == 3
        assert len(cv_manifest.containers) == 4  # 2 roots + 2 children

        # Organize results for easier lookup.
        container_map = {c.name: c for c in cv_manifest.containers}
        configlet_map = {c.name: c for c in cv_manifest.configlets}

        # Verify configlet properties (CVConfiglet).
        assert "configlet_leaf" in configlet_map
        cv_cfg = configlet_map["configlet_leaf"]
        assert cv_cfg.name == "configlet_leaf"
        assert str(cv_cfg.file) == "path/to/leaf.cfg"
        assert cv_cfg.id == generate_id("configlet_leaf")

        # Verify root container properties (CVContainer).
        assert "RACK_1" in container_map
        root1 = container_map["RACK_1"]
        assert root1.is_root is True
        assert root1.name == "RACK_1"
        assert root1.tag_query == "rack:1"
        assert root1.description == "All devices in Rack 1"
        assert root1.match_policy == "match_all"  # Default value

        # Check expected child IDs in root container.
        expected_child_ids = {generate_id("RACK_1/LEAF_GROUP_A"), generate_id("RACK_1/LEAF_GROUP_B")}
        assert set(root1.child_ids) == expected_child_ids

        # Check expected configlet IDs in root container.
        expected_configlet_ids = {configlet_map["configlet_global"].id}
        assert set(root1.configlet_ids) == expected_configlet_ids

        # Verify nested container properties (CVContainer).
        assert "LEAF_GROUP_A" in container_map
        leaf1a = container_map["LEAF_GROUP_A"]
        assert leaf1a.is_root is False
        assert leaf1a.id == generate_id("RACK_1/LEAF_GROUP_A")
        assert len(leaf1a.child_ids) == 0
        assert leaf1a.configlet_ids == (configlet_map["configlet_leaf"].id,)

        # Verify non-default match policy propagation.
        assert "LEAF_GROUP_B" in container_map
        leaf1b = container_map["LEAF_GROUP_B"]
        assert leaf1b.match_policy == "match_first"

    def test_duplicate_configlet_name_error(self) -> None:
        """Tests that a CVManifestError is raised for duplicate configlet names."""
        configlet1 = AvdConfiglet(name="duplicate_name", file=Path("file1.conf"))
        configlet2 = AvdConfiglet(name="duplicate_name", file=Path("file2.conf"))
        avd_manifest = AvdManifest(configlets=(configlet1, configlet2), containers=())

        with pytest.raises(CVManifestError, match="Duplicate configlet name found: 'duplicate_name'"):
            CVManifest.from_avd_manifest(avd_manifest)

    def test_duplicate_container_name_error(self) -> None:
        """Tests that a CVManifestError is raised for duplicate sibling container names."""
        child1 = AvdContainer(name="CHILD_A", tag_query="q1")
        child2 = AvdContainer(name="CHILD_A", tag_query="q2")  # Duplicate name
        root = AvdContainer(name="ROOT", tag_query="q_root", sub_containers=(child1, child2))
        avd_manifest = AvdManifest(configlets=(), containers=(root,))

        with pytest.raises(CVManifestError, match="Duplicate container name found: 'ROOT/CHILD_A'"):
            CVManifest.from_avd_manifest(avd_manifest)

    def test_duplicate_root_container_name_error(self) -> None:
        """Tests that a CVManifestError is raised for duplicate root container names."""
        root1 = AvdContainer(name="ROOT_DUP", tag_query="q1")
        root2 = AvdContainer(name="ROOT_DUP", tag_query="q2")  # Duplicate name
        avd_manifest = AvdManifest(configlets=(), containers=(root1, root2))

        with pytest.raises(CVManifestError, match="Duplicate container name found: 'ROOT_DUP'"):
            CVManifest.from_avd_manifest(avd_manifest)

    def test_invalid_configlet_reference_error(self) -> None:
        """Tests that an error is raised when a container references a non-existent configlet."""
        container = AvdContainer(name="C1", tag_query="q1", configlets=("missing_configlet",))
        avd_manifest = AvdManifest(configlets=(), containers=(container,))

        with pytest.raises(CVManifestError, match=r"Configlet 'missing_configlet' is assigned to a container but is not found in the input definition."):
            CVManifest.from_avd_manifest(avd_manifest)

    def test_manifest_with_configlets_only(self) -> None:
        """Tests a manifest that has configlets but no container definitions."""
        configlet = AvdConfiglet(name="cfg1", file=Path("file1.cfg"))
        avd_manifest = AvdManifest(configlets=(configlet,), containers=())

        cv_manifest = CVManifest.from_avd_manifest(avd_manifest)

        assert len(cv_manifest.configlets) == 1
        assert len(cv_manifest.containers) == 0

    def test_manifest_with_containers_only(self) -> None:
        """Tests a manifest that has containers but no configlets defined globally."""
        # Note: This test will fail if the container references a configlet,
        # so the container's configlet list must be empty.
        container = AvdContainer(name="ROOT", tag_query="all", configlets=())
        avd_manifest = AvdManifest(configlets=(), containers=(container,))

        cv_manifest = CVManifest.from_avd_manifest(avd_manifest)
        container_map = {c.name: c for c in cv_manifest.containers}

        assert len(cv_manifest.configlets) == 0
        assert len(cv_manifest.containers) == 1
        assert container_map["ROOT"].name == "ROOT"

    def test_empty_manifest(self) -> None:
        """Tests an entirely empty manifest."""
        avd_manifest = AvdManifest(configlets=(), containers=())
        cv_manifest = CVManifest.from_avd_manifest(avd_manifest)
        assert len(cv_manifest.configlets) == 0
        assert len(cv_manifest.containers) == 0

    def test_deterministic_id_generation(self) -> None:
        """Ensures the ID generation function is deterministic and consistent."""
        id1 = CVManifest._generate_deterministic_id("my_key")
        id2 = CVManifest._generate_deterministic_id("my_key")
        id3 = CVManifest._generate_deterministic_id("another_key")

        assert id1 == id2
        assert id1 != id3
        assert id1.startswith(AVD_ENTITY_PREFIX)


class TestAvdConfigletFromDict:
    def test_success(self) -> None:
        """Tests successful creation of AvdConfiglet from a valid dictionary."""
        data = {"name": "TestConfiglet", "file": "/path/to/file.cfg"}
        configlet = AvdConfiglet.from_dict(data)
        assert configlet.name == "TestConfiglet"
        assert str(configlet.file) == "/path/to/file.cfg"

    @pytest.mark.parametrize(
        ("invalid_data", "match_str"),
        [
            pytest.param({"name": "Test"}, "Invalid configlet definition", id="missing_file"),
            pytest.param({"file": "path.cfg"}, "Invalid configlet definition", id="missing_name"),
            pytest.param({}, "Invalid configlet definition", id="empty_dict"),
        ],
    )
    def test_missing_keys_failure(self, invalid_data: dict[str, Any], match_str: str) -> None:
        """Tests that ValueError is raised for various invalid data structures in AvdConfiglet."""
        with pytest.raises(ValueError, match=match_str):
            AvdConfiglet.from_dict(invalid_data)


class TestAvdContainerFromDict:
    def test_success_minimal(self) -> None:
        """Tests successful creation of AvdContainer with only required fields."""
        data = {"name": "MinimalContainer", "tag_query": "role:minimal"}
        container = AvdContainer.from_dict(data)
        assert container.name == "MinimalContainer"
        assert container.tag_query == "role:minimal"
        assert container.description is None
        assert container.match_policy == "match_all"
        assert container.preserve_existing_sub_containers is False
        assert not container.configlets
        assert not container.sub_containers

    def test_success_full_and_nested(self) -> None:
        """Tests successful creation of AvdContainer with all fields, including nested containers."""
        data = {
            "name": "Root",
            "tag_query": "all",
            "description": "Root container",
            "match_policy": "match_first",
            "preserve_existing_sub_containers": True,
            "configlets": [{"name": "cfg1"}, {"name": "cfg2"}],
            "sub_containers": [
                {
                    "name": "Child1",
                    "tag_query": "rack:1",
                    "preserve_existing_sub_containers": True,
                    "configlets": [{"name": "cfg_child"}],
                }
            ],
        }
        container = AvdContainer.from_dict(data)
        assert container.name == "Root"
        assert container.description == "Root container"
        assert container.match_policy == "match_first"
        assert container.preserve_existing_sub_containers is True
        assert container.configlets == ("cfg1", "cfg2")
        assert len(container.sub_containers) == 1

        child = container.sub_containers[0]
        assert isinstance(child, AvdContainer)
        assert child.name == "Child1"
        assert child.tag_query == "rack:1"
        assert child.preserve_existing_sub_containers is True
        assert child.configlets == ("cfg_child",)

    @pytest.mark.parametrize(
        ("invalid_data", "match_str"),
        [
            pytest.param({"name": "Test"}, "Invalid container definition", id="missing_tag_query"),
            pytest.param({"tag_query": "q1"}, "Invalid container definition", id="missing_name"),
            pytest.param({"name": "Test", "tag_query": "q1", "configlets": "not-a-list"}, "Invalid container definition", id="invalid_configlet_type"),
            pytest.param(
                {"name": "Test", "tag_query": "q1", "sub_containers": {"is_dict": True}}, "Invalid container definition", id="invalid_subcontainer_type"
            ),
            pytest.param(
                {"name": "Test", "tag_query": "q1", "configlets": ["string_item"]}, "Invalid container definition", id="invalid_configlet_item_format"
            ),
        ],
    )
    def test_invalid_data_failure(self, invalid_data: dict[str, Any], match_str: str) -> None:
        """Tests that ValueError is raised for various invalid data structures in AvdContainer."""
        with pytest.raises(ValueError, match=match_str):
            AvdContainer.from_dict(invalid_data)


class TestAvdManifestFromDict:
    @pytest.fixture
    def full_manifest_dict(self) -> dict[str, Any]:
        """Provides a complex, valid manifest as a dictionary."""
        return {
            "configlets": [
                {"name": "global_cfg", "file": "global.cfg"},
                {"name": "leaf_cfg", "file": "leaf.cfg"},
            ],
            "containers": [
                {
                    "name": "ROOT",
                    "tag_query": "all",
                    "configlets": [{"name": "global_cfg"}],
                    "sub_containers": [{"name": "LEAVES", "tag_query": "role:leaf", "configlets": [{"name": "leaf_cfg"}]}],
                }
            ],
        }

    def test_success_full(self, full_manifest_dict: dict[str, Any]) -> None:
        """Tests successful creation of AvdManifest from a full dictionary."""
        manifest = AvdManifest.from_dict(full_manifest_dict)
        assert len(manifest.configlets) == 2
        assert len(manifest.containers) == 1
        assert manifest.configlets[0].name == "global_cfg"
        assert manifest.containers[0].name == "ROOT"
        assert len(manifest.containers[0].sub_containers) == 1
        assert manifest.containers[0].sub_containers[0].name == "LEAVES"

    def test_success_configlets_only(self) -> None:
        """Tests successful creation of AvdManifest with only configlets defined."""
        data = {"configlets": [{"name": "cfg1", "file": "f1.cfg"}]}
        manifest = AvdManifest.from_dict(data)
        assert len(manifest.configlets) == 1
        assert len(manifest.containers) == 0
        assert manifest.configlets[0].name == "cfg1"

    def test_success_containers_only(self) -> None:
        """Tests successful creation of AvdManifest with only containers defined."""
        data = {"containers": [{"name": "c1", "tag_query": "q1"}]}
        manifest = AvdManifest.from_dict(data)
        assert len(manifest.configlets) == 0
        assert len(manifest.containers) == 1
        assert manifest.containers[0].name == "c1"

    def test_success_empty_manifest(self) -> None:
        """Tests successful creation of AvdManifest from an empty dictionary or with empty lists."""
        manifest_empty_dict = AvdManifest.from_dict({})
        assert not manifest_empty_dict.configlets
        assert not manifest_empty_dict.containers

        manifest_empty_lists = AvdManifest.from_dict({"configlets": [], "containers": []})
        assert not manifest_empty_lists.configlets
        assert not manifest_empty_lists.containers

    @pytest.mark.parametrize(
        ("invalid_data", "match_str"),
        [
            pytest.param({"configlets": {"is_dict": True}}, "Failed to build", id="invalid_configlets_type"),
            pytest.param({"containers": {"is_dict": True}}, "Failed to build", id="invalid_containers_type"),
            pytest.param({"configlets": [{"name_only": True}]}, "Failed to build", id="invalid_item_in_configlets"),
            pytest.param({"containers": [{"name_only": True}]}, "Failed to build", id="invalid_item_in_containers"),
        ],
    )
    def test_invalid_data_failure(self, invalid_data: dict[str, Any], match_str: str) -> None:
        """Tests that ValueError is raised for invalid AvdManifest data."""
        with pytest.raises(ValueError, match=match_str):
            AvdManifest.from_dict(invalid_data)


# === CVGRPCKeepalives Tests ===


class TestCVGRPCKeepalives:
    def test_defaults(self) -> None:
        """Tests that CVGRPCKeepalives is created with expected default values."""
        keepalives = CVGRPCKeepalives()
        assert keepalives.enabled is False
        assert keepalives.keepalive_time == 60
        assert keepalives.keepalive_timeout == 20
        assert keepalives.permit_without_calls is False

    def test_custom_values(self) -> None:
        """Tests that CVGRPCKeepalives accepts custom values including explicit enable."""
        keepalives = CVGRPCKeepalives(enabled=True, keepalive_time=30, keepalive_timeout=10, permit_without_calls=True)
        assert keepalives.enabled is True
        assert keepalives.keepalive_time == 30
        assert keepalives.keepalive_timeout == 10
        assert keepalives.permit_without_calls is True

    @pytest.mark.parametrize(
        ("enabled", "keepalive_time", "expected_exception"),
        [
            pytest.param(True, 29, pytest.raises(ValueError, match="keepalive_time must be >= 30s, got 29"), id="ENABLED_TIME_29_BELOW_MIN"),
            pytest.param(True, 1, pytest.raises(ValueError, match="keepalive_time must be >= 30s, got 1"), id="ENABLED_TIME_1_BELOW_MIN"),
            pytest.param(True, 30, does_not_raise(), id="ENABLED_TIME_AT_MIN"),
            pytest.param(True, 60, does_not_raise(), id="ENABLED_TIME_DEFAULT"),
            pytest.param(False, 29, does_not_raise(), id="DISABLED_TIME_BELOW_MIN_OK"),
        ],
    )
    def test_keepalive_time_validation(self, enabled: bool, keepalive_time: int, expected_exception: AbstractContextManager) -> None:
        """Tests that keepalive_time >= 30 is enforced only when enabled=True."""
        with expected_exception:
            CVGRPCKeepalives(enabled=enabled, keepalive_time=keepalive_time)


# === CVGRPCChannelConfiguration Tests ===


class TestCVGRPCChannelConfiguration:
    def test_as_grpclib_configuration_disabled_returns_default_configuration(self) -> None:
        """Tests that as_grpclib_configuration returns a default Configuration when keepalives are disabled."""
        channel_config = CVGRPCChannelConfiguration(grpc_keepalives=CVGRPCKeepalives(enabled=False))
        config = channel_config.as_grpclib_configuration()
        assert isinstance(config, Configuration)
        # _http2_max_pings_without_data is only set to 0 when keepalives are enabled
        assert config._http2_max_pings_without_data != 0

    def test_as_grpclib_configuration_enabled_returns_configuration(self) -> None:
        """Tests that as_grpclib_configuration builds a grpclib Configuration from the keepalive fields."""
        channel_config = CVGRPCChannelConfiguration(
            grpc_keepalives=CVGRPCKeepalives(enabled=True, keepalive_time=45, keepalive_timeout=15, permit_without_calls=True),
        )
        config = channel_config.as_grpclib_configuration()
        assert isinstance(config, Configuration)
        assert config._keepalive_time == 45
        assert config._keepalive_timeout == 15
        assert config._keepalive_permit_without_calls is True
        assert config._http2_max_pings_without_data == 0
        assert config._http2_min_sent_ping_interval_without_data == 45

    def test_as_grpclib_configuration_type_error_falls_back_to_default_configuration(self, caplog: pytest.LogCaptureFixture) -> None:
        """Tests that a TypeError from grpclib Configuration falls back to a default Configuration and logs a warning."""
        channel_config = CVGRPCChannelConfiguration(grpc_keepalives=CVGRPCKeepalives(enabled=True))
        # Raise on first Configuration() call. Succeed on second
        with (
            caplog.at_level(DEBUG),
            patch(
                "pyavd._cv.workflows.models.Configuration",
                side_effect=[TypeError("unexpected keyword argument"), Configuration()],
            ),
        ):
            config = channel_config.as_grpclib_configuration()
        assert isinstance(config, Configuration)
        assert "gRPC keepalives will not be enabled" in caplog.text
