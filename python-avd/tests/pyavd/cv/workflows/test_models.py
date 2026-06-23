# Copyright (c) 2025-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
# pylint: disable=too-many-lines

from contextlib import AbstractContextManager
from contextlib import nullcontext as does_not_raise
from dataclasses import dataclass, field
from logging import DEBUG
from pathlib import Path
from typing import Any
from unittest.mock import patch

import pytest
from grpclib.config import Configuration

from pyavd._cv.client.exceptions import CVManifestError
from pyavd._cv.workflows.models import (
    AVD_ENTITY_PREFIX,
    AvdChangeControl,
    AvdChangeControlTemplate,
    AvdConfiglet,
    AvdContainer,
    AvdDevice,
    AvdManifest,
    AvdWorkspace,
    AvdWorkspaceBuildWarningsConfig,
    CVChangeControl,
    CVDeployFuture,
    CVDevice,
    CVDeviceTag,
    CVEosConfig,
    CVGRPCChannelConfiguration,
    CVGRPCKeepalives,
    CVInterfaceTag,
    CVManifest,
    CVPathfinderMetadata,
    CVStudioInputs,
    CVWorkspace,
    CVWorkspaceBuildConfigValidationError,
    CVWorkspaceBuildConfigValidationResult,
    CVWorkspaceBuildConfigValidationWarning,
    CVWorkspaceDeviceBuildResult,
    DeployToCvResult,
)
from pyavd._cv.workflows.utils import reset_mutable_fields

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
        assert cv_manifest.preserve_existing_containers is False

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
        assert manifest.preserve_existing_containers is False
        assert manifest.configlets[0].name == "global_cfg"
        assert manifest.containers[0].name == "ROOT"
        assert len(manifest.containers[0].sub_containers) == 1
        assert manifest.containers[0].sub_containers[0].name == "LEAVES"

    def test_success_with_preserve_existing_containers(self, full_manifest_dict: dict[str, Any]) -> None:
        """Tests successful creation of AvdManifest with root-level preservation enabled."""
        full_manifest_dict["preserve_existing_containers"] = True
        manifest = AvdManifest.from_dict(full_manifest_dict)
        assert manifest.preserve_existing_containers is True

        cv_manifest = CVManifest.from_avd_manifest(manifest)
        assert cv_manifest.preserve_existing_containers is True

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
        assert manifest_empty_dict.preserve_existing_containers is False

        manifest_empty_lists = AvdManifest.from_dict({"configlets": [], "containers": []})
        assert not manifest_empty_lists.configlets
        assert not manifest_empty_lists.containers
        assert manifest_empty_lists.preserve_existing_containers is False

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


class TestAvdWorkspaceBuildWarningsConfigFromDict:
    def test_success_defaults(self) -> None:
        """Tests that from_dict with an empty dict produces default values."""
        config = AvdWorkspaceBuildWarningsConfig.from_dict({})
        assert config.enabled is True
        assert isinstance(config.suppress_patterns, tuple)
        assert not config.suppress_patterns
        assert config.suppress_portfast is False

    def test_success_list_to_tuple(self) -> None:
        """Tests that a list passed for suppress_patterns is converted to a tuple."""
        config = AvdWorkspaceBuildWarningsConfig.from_dict({"suppress_patterns": ["pattern1", "pattern2"]})
        assert config.suppress_patterns == ("pattern1", "pattern2")

    def test_success_full(self) -> None:
        """Tests successful creation with all fields specified."""
        config = AvdWorkspaceBuildWarningsConfig.from_dict({"enabled": False, "suppress_patterns": ["p1"], "suppress_portfast": True})
        assert config.enabled is False
        assert config.suppress_patterns == ("p1",)
        assert config.suppress_portfast is True

    @pytest.mark.parametrize(
        ("invalid_data", "match_str"),
        [
            pytest.param(None, "Invalid AvdWorkspaceBuildWarningsConfig definition", id="none_input"),
            pytest.param("string", "Invalid AvdWorkspaceBuildWarningsConfig definition", id="string_input"),
            pytest.param({"suppress_patterns": 42}, "Invalid AvdWorkspaceBuildWarningsConfig definition", id="non_iterable_suppress_patterns"),
            pytest.param({"unknown_key": True}, "Invalid AvdWorkspaceBuildWarningsConfig definition", id="unknown_key"),
        ],
    )
    def test_invalid_data_failure(self, invalid_data: Any, match_str: str) -> None:
        """Tests that ValueError is raised for invalid input data."""
        with pytest.raises(ValueError, match=match_str):
            AvdWorkspaceBuildWarningsConfig.from_dict(invalid_data)


class TestAvdWorkspace:
    @pytest.mark.parametrize(
        ("max_sync_retries", "expected_exception"),
        [
            pytest.param(0, does_not_raise(), id="ZERO_ALLOWED"),
            pytest.param(1, does_not_raise(), id="ONE_ALLOWED"),
            pytest.param(5, does_not_raise(), id="DEFAULT_ALLOWED"),
            pytest.param(-1, pytest.raises(ValueError, match="max_sync_retries must be a non-negative integer, got -1"), id="NEGATIVE_ONE_REJECTED"),
            pytest.param(-100, pytest.raises(ValueError, match="max_sync_retries must be a non-negative integer, got -100"), id="LARGE_NEGATIVE_REJECTED"),
        ],
    )
    def test_max_sync_retries_validation(self, max_sync_retries: int, expected_exception: AbstractContextManager) -> None:
        """Tests that max_sync_retries >= 0 is enforced at construction time."""
        with expected_exception:
            AvdWorkspace(max_sync_retries=max_sync_retries)


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


# === CVDeployFuture Tests ===


class TestCVDeployFuture:
    def test_defaults(self) -> None:
        """Tests that CVDeployFuture is created with expected default values."""
        future = CVDeployFuture()
        assert future.use_system_certs is False

    def test_custom_values(self) -> None:
        """Tests that CVDeployFuture accepts explicit values for all fields."""
        future = CVDeployFuture(use_system_certs=True)
        assert future.use_system_certs is True


# === CVChangeControl Tests ===


class TestCVChangeControl:
    def test_get_result(self) -> None:
        template = AvdChangeControlTemplate(name="template-name", id="template-id")
        cc = CVChangeControl(
            avd_change_control=AvdChangeControl(name="avd-cc-name", description="avd-cc-desc", requested_state="approved", change_control_template=template),
            id="cc-id",
            state="approved",
            name="cc-name",
            description="cc-desc",
        )
        result = cc.get_result()
        assert "avd_change_control" not in result
        assert result["id"] == "cc-id"
        assert result["state"] == "approved"
        assert result["name"] == "cc-name"
        assert result["description"] == "cc-desc"
        assert result["requested_state"] == "approved"
        assert result["change_control_template"] == {"name": "template-name", "id": "template-id"}

    def test_reset_runtime_fields_cleared(self) -> None:
        """Tests that id and state (populated from CV) are reset to None."""
        cc = CVChangeControl(id="cc-id", state="approved")

        cc.reset_mutable_fields()

        assert cc.id is None
        assert cc.state is None

    @pytest.mark.parametrize(
        ("avd_name", "avd_desc", "expected_name", "expected_desc"),
        [
            pytest.param("avd-cc-name", "avd-cc-desc", "avd-cc-name", "avd-cc-desc", id="both_provided_in_avd_change_control"),
            pytest.param("avd-cc-name", None, "avd-cc-name", None, id="name_only_in_avd_change_control"),
            pytest.param(None, "avd-cc-desc", None, "avd-cc-desc", id="desc_only_in_avd_change_control"),
            pytest.param(None, None, None, None, id="neither_in_avd_change_control"),
        ],
    )
    def test_reset_name_and_description_restored_from_avd_change_control(
        self,
        avd_name: str | None,
        avd_desc: str | None,
        expected_name: str | None,
        expected_desc: str | None,
    ) -> None:
        """Tests that name and description are restored from the frozen avd_change_control after reset."""
        avd_cc = AvdChangeControl(name=avd_name, description=avd_desc)
        cc = CVChangeControl(avd_change_control=avd_cc)

        cc.reset_mutable_fields()

        assert cc.name == expected_name
        assert cc.description == expected_desc

    def test_reset_avd_change_control_object_is_preserved(self) -> None:
        """Tests that the frozen avd_change_control intent object is the same instance after reset."""
        template = AvdChangeControlTemplate(name="template-name", id="template-id")
        avd_cc = AvdChangeControl(name="avd-cc-name", description="avd-cc-desc", requested_state="approved", change_control_template=template)
        cc = CVChangeControl(avd_change_control=avd_cc)

        cc.reset_mutable_fields()

        assert cc.avd_change_control is avd_cc


class TestCVWorkspace:
    def test_get_result(self) -> None:
        ws = CVWorkspace(
            avd_workspace=AvdWorkspace(name="workspace-name", description="workspace-description", requested_state="submitted"),
            state="submitted",
            change_control_id="cc-id",
            build_id="build-id",
        )
        result = ws.get_result()
        assert "avd_workspace" not in result
        assert result["name"] == "workspace-name"
        assert result["description"] == "workspace-description"
        assert result["requested_state"] == "submitted"
        assert result["state"] == "submitted"
        assert result["change_control_id"] == "cc-id"
        assert result["build_id"] == "build-id"
        assert result["device_build_results"] == []

    def test_reset_runtime_fields_cleared(self) -> None:
        """Tests that state, change_control_id, build_id, device_build_results and synchronization_required are reset."""
        avd_ws = AvdWorkspace(name="workspace-name")
        device = CVDevice(avd_device=AvdDevice(hostname="avd-leaf1"))
        ws = CVWorkspace(
            avd_workspace=avd_ws,
            state="built",
            change_control_id="cc-id",
            build_id="build-id",
            device_build_results=[CVWorkspaceDeviceBuildResult(device=device, config_validation=CVWorkspaceBuildConfigValidationResult())],
            synchronization_required=True,
        )

        ws.reset_mutable_fields()

        assert ws.state is None
        assert ws.change_control_id is None
        assert ws.build_id is None
        assert not ws.device_build_results
        assert ws.synchronization_required is False

    def test_reset_avd_workspace_object_is_preserved(self) -> None:
        """Tests that the frozen avd_workspace intent object is the same instance after reset."""
        avd_ws = AvdWorkspace(name="workspace-name", id="ws-id", description="workspace-description", requested_state="submitted", force=True)
        ws = CVWorkspace(avd_workspace=avd_ws)

        ws.reset_mutable_fields()

        assert ws.avd_workspace is avd_ws


class TestCVDevice:
    def test_get_result(self) -> None:
        device = CVDevice(
            avd_device=AvdDevice(hostname="avd-leaf1", serial_number="sn54321", system_mac_address="55:44:33:22:11:00"),
            serial_number="sn12345",
            system_mac_address="00:11:22:33:44:55",
            exists_on_cv=True,
            streaming=True,
        )
        result = device.get_result()
        assert result["hostname"] == "avd-leaf1"
        assert result["serial_number"] == "sn12345"
        assert result["system_mac_address"] == "00:11:22:33:44:55"
        assert result["exists_on_cv"] is True
        assert result["streaming"] is True

    @pytest.mark.parametrize(
        ("intended_serial", "intended_mac", "expected_serial_after_reset", "expected_mac_after_reset"),
        [
            pytest.param(None, None, None, None, id="no_intent_values_reset_to_none"),
            pytest.param("sn-intended", None, "sn-intended", None, id="intended_serial_restored"),
            pytest.param(None, "aa:bb:cc:dd:ee:ff", None, "aa:bb:cc:dd:ee:ff", id="intended_mac_restored"),
            pytest.param("sn-intended", "aa:bb:cc:dd:ee:ff", "sn-intended", "aa:bb:cc:dd:ee:ff", id="both_intent_values_restored"),
        ],
    )
    def test_reset_cv_state_cleared_and_intent_values_restored(
        self,
        intended_serial: str | None,
        intended_mac: str | None,
        expected_serial_after_reset: str | None,
        expected_mac_after_reset: str | None,
    ) -> None:
        """Tests that CV-discovered serial/mac/exists_on_cv/streaming are cleared and avd_device intent values are restored."""
        avd_device = AvdDevice(hostname="avd-leaf1", serial_number=intended_serial, system_mac_address=intended_mac)
        device = CVDevice(avd_device=avd_device)
        # Simulate values written by verify_devices_on_cv.
        device.serial_number = "cv-discovered-serial"
        device.system_mac_address = "cv-discovered-mac"
        device.exists_on_cv = True
        device.streaming = True

        device.reset_mutable_fields()

        assert device.serial_number == expected_serial_after_reset
        assert device.system_mac_address == expected_mac_after_reset
        assert device.exists_on_cv is None
        assert device.streaming is None

    def test_reset_avd_device_object_is_preserved(self) -> None:
        """Tests that the frozen avd_device intent object is the same instance after reset."""
        avd_device = AvdDevice(hostname="avd-leaf1", serial_number="sn54321", system_mac_address="55:44:33:22:11:00")
        device = CVDevice(avd_device=avd_device)
        device.exists_on_cv = True

        device.reset_mutable_fields()

        assert device.avd_device is avd_device


class TestDeployToCvResult:
    def test_get_result(self) -> None:
        cv_device_1 = CVDevice(avd_device=AvdDevice(hostname="leaf1", serial_number="snleaf1"), serial_number="snleaf1", system_mac_address="00:11:22:33:44:55")
        cv_device_2 = CVDevice(avd_device=AvdDevice(hostname="leaf2"), serial_number="snleaf2", system_mac_address=None)

        validation_result = CVWorkspaceBuildConfigValidationResult(
            errors=[CVWorkspaceBuildConfigValidationError(error_msg="syntax error", line_num=5, configlet_name="AVD_leaf1")],
            warnings=[CVWorkspaceBuildConfigValidationWarning(warning_msg="portfast warning", line_num=3, configlet_name="AVD_leaf1")],
        )

        child_container = AvdContainer(name="CHILD", tag_query="role:leaf", description="child desc", configlets=("cfg1",))
        root_container = AvdContainer(name="ROOT", tag_query="all", description="root desc", configlets=("cfg2",), sub_containers=(child_container,))

        result_obj = DeployToCvResult(
            failed=True,
            errors=["error1"],
            warnings=["warning1"],
            workspace=CVWorkspace(
                avd_workspace=AvdWorkspace(id="ws-id", name="workspace-name", description="workspace-description", requested_state="submitted", force=True),
                state="submitted",
                change_control_id="cc-id",
                build_id="build-id",
                device_build_results=[CVWorkspaceDeviceBuildResult(device=cv_device_1, config_validation=validation_result)],
            ),
            change_control=CVChangeControl(
                avd_change_control=AvdChangeControl(
                    name="avd-cc-name",
                    description="avd-cc-desc",
                    requested_state="approved",
                    change_control_template=AvdChangeControlTemplate(name="template-name", id="template-id"),
                ),
                id="cc-id",
                state="approved",
                name="cc-name",
                description="cc-desc",
            ),
            deployed_configs=[CVEosConfig(file="intended/leaf1.cfg", device=cv_device_1, configlet_name="AVD_leaf1")],
            deployed_static_config_containers=[root_container],
            deployed_static_config_configlets=[AvdConfiglet(name="cfg1", file="path/cfg1.cfg")],
            deployed_device_tags=[CVDeviceTag(label="dc", value="DC1", device=cv_device_1)],
            deployed_interface_tags=[CVInterfaceTag(label="speed", value="100G", device=cv_device_1, interface="Ethernet1")],
            deployed_studio_inputs=[CVStudioInputs(studio_id="studio-1", inputs={"key": "val"}, input_path=["root", "sub"])],
            deployed_cv_pathfinder_metadata=[CVPathfinderMetadata(metadata={"role": "transit"}, device=cv_device_2)],
            skipped_configs=[CVEosConfig(file="intended/leaf2.cfg", device=cv_device_2)],
            skipped_static_config_containers=[child_container],
            skipped_device_tags=[CVDeviceTag(label="dc", value="DC2")],
            skipped_interface_tags=[CVInterfaceTag(label="speed", value="10G")],
            skipped_cv_pathfinder_metadata=[CVPathfinderMetadata(metadata={"role": "edge"})],
            removed_configs=["removed/leaf1.cfg"],
            removed_static_config_containers=["OLD_CONTAINER"],
            removed_static_config_configlets=["OLD_CONFIGLET"],
            removed_device_tags=[CVDeviceTag(label="old_dc", value="old_val")],
            removed_interface_tags=[CVInterfaceTag(label="old_speed", value="old_val")],
        )

        result = result_obj.get_result()

        assert result["failed"] is True
        assert result["errors"] == ["error1"]
        assert result["warnings"] == ["warning1"]

        # workspace
        result_workspace = result["workspace"]
        assert "avd_workspace" not in result_workspace
        assert result_workspace["name"] == "workspace-name"
        assert result_workspace["description"] == "workspace-description"
        assert result_workspace["id"] == "ws-id"
        assert result_workspace["requested_state"] == "submitted"
        assert result_workspace["force"] is True
        assert result_workspace["state"] == "submitted"
        assert result_workspace["change_control_id"] == "cc-id"
        assert result_workspace["build_id"] == "build-id"
        assert result_workspace["build_warnings"] == {"enabled": True, "suppress_patterns": (), "suppress_portfast": False}

        result_workspace_device_duild_results = result_workspace["device_build_results"][0]
        assert "avd_device" not in result_workspace_device_duild_results["device"]
        assert result_workspace_device_duild_results["device"]["hostname"] == "leaf1"
        assert result_workspace_device_duild_results["device"]["serial_number"] == "snleaf1"
        assert result_workspace_device_duild_results["device"]["system_mac_address"] == "00:11:22:33:44:55"
        assert result_workspace_device_duild_results["device"]["exists_on_cv"] is None
        assert result_workspace_device_duild_results["device"]["streaming"] is None
        assert result_workspace_device_duild_results["config_validation"]["errors"][0]["error_msg"] == "syntax error"
        assert result_workspace_device_duild_results["config_validation"]["errors"][0]["line_num"] == 5
        assert result_workspace_device_duild_results["config_validation"]["errors"][0]["configlet_name"] == "AVD_leaf1"
        assert result_workspace_device_duild_results["config_validation"]["warnings"][0]["warning_msg"] == "portfast warning"
        assert result_workspace_device_duild_results["config_validation"]["warnings"][0]["line_num"] == 3
        assert result_workspace_device_duild_results["config_validation"]["warnings"][0]["configlet_name"] == "AVD_leaf1"

        # change_control
        result_change_control = result["change_control"]
        assert "avd_change_control" not in result_change_control
        assert result_change_control["name"] == "cc-name"
        assert result_change_control["description"] == "cc-desc"
        assert result_change_control["id"] == "cc-id"
        assert result_change_control["change_control_template"] == {"name": "template-name", "id": "template-id"}
        assert result_change_control["requested_state"] == "approved"
        assert result_change_control["state"] == "approved"

        # deployed_configs
        result_deployed_configs = result["deployed_configs"][0]
        assert result_deployed_configs["file"] == "intended/leaf1.cfg"
        assert result_deployed_configs["configlet_name"] == "AVD_leaf1"
        assert "avd_device" not in result_deployed_configs["device"]
        assert result_deployed_configs["device"]["hostname"] == "leaf1"
        assert result_deployed_configs["device"]["serial_number"] == "snleaf1"
        assert result_deployed_configs["device"]["system_mac_address"] == "00:11:22:33:44:55"
        assert result_deployed_configs["device"]["exists_on_cv"] is None
        assert result_deployed_configs["device"]["streaming"] is None

        # deployed_static_config_containers
        result_deployed_static_config_containers = result["deployed_static_config_containers"][0]
        assert result_deployed_static_config_containers["name"] == "ROOT"
        assert result_deployed_static_config_containers["tag_query"] == "all"
        assert result_deployed_static_config_containers["description"] == "root desc"
        assert result_deployed_static_config_containers["match_policy"] == "match_all"
        assert result_deployed_static_config_containers["configlets"] == ("cfg2",)
        result_deployed_static_config_subcontainers = result_deployed_static_config_containers["sub_containers"][0]
        assert result_deployed_static_config_subcontainers["name"] == "CHILD"
        assert result_deployed_static_config_subcontainers["tag_query"] == "role:leaf"
        assert result_deployed_static_config_subcontainers["description"] == "child desc"
        assert result_deployed_static_config_subcontainers["configlets"] == ("cfg1",)

        # deployed_static_config_configlets
        result_deployed_static_config_configlets = result["deployed_static_config_configlets"][0]
        assert result_deployed_static_config_configlets["name"] == "cfg1"
        assert result_deployed_static_config_configlets["file"] == "path/cfg1.cfg"

        # deployed_device_tags
        result_deployed_device_tags = result["deployed_device_tags"][0]
        assert result_deployed_device_tags["label"] == "dc"
        assert result_deployed_device_tags["value"] == "DC1"
        assert "avd_device" not in result_deployed_device_tags["device"]
        assert result_deployed_device_tags["device"]["hostname"] == "leaf1"

        # deployed_interface_tags
        result_deployed_interface_tags = result["deployed_interface_tags"][0]
        assert result_deployed_interface_tags["label"] == "speed"
        assert result_deployed_interface_tags["value"] == "100G"
        assert result_deployed_interface_tags["interface"] == "Ethernet1"
        assert result_deployed_interface_tags["device"]["hostname"] == "leaf1"

        # deployed_studio_inputs
        result_deployed_studio_inputs = result["deployed_studio_inputs"][0]
        assert result_deployed_studio_inputs["studio_id"] == "studio-1"
        assert result_deployed_studio_inputs["inputs"] == {"key": "val"}
        assert result_deployed_studio_inputs["input_path"] == ["root", "sub"]

        # deployed_cv_pathfinder_metadata
        result_deployed_cv_pathfinder_metadata = result["deployed_cv_pathfinder_metadata"][0]
        assert result_deployed_cv_pathfinder_metadata["metadata"] == {"role": "transit"}
        assert "avd_device" not in result_deployed_cv_pathfinder_metadata["device"]
        assert result_deployed_cv_pathfinder_metadata["device"]["hostname"] == "leaf2"
        assert result_deployed_cv_pathfinder_metadata["device"]["serial_number"] == "snleaf2"
        assert result_deployed_cv_pathfinder_metadata["device"]["system_mac_address"] is None

        # skipped_configs
        skipped_result_deployed_configs = result["skipped_configs"][0]
        assert skipped_result_deployed_configs["file"] == "intended/leaf2.cfg"
        assert skipped_result_deployed_configs["configlet_name"] is None
        assert skipped_result_deployed_configs["device"]["hostname"] == "leaf2"

        # skipped_static_config_containers
        assert result["skipped_static_config_containers"][0]["name"] == "CHILD"

        # skipped_device_tags — device is None
        skipped_result_deployed_device_tags = result["skipped_device_tags"][0]
        assert skipped_result_deployed_device_tags["label"] == "dc"
        assert skipped_result_deployed_device_tags["value"] == "DC2"
        assert skipped_result_deployed_device_tags["device"] is None

        # skipped_interface_tags — device and interface are None
        skipped_result_deployed_interface_tags = result["skipped_interface_tags"][0]
        assert skipped_result_deployed_interface_tags["label"] == "speed"
        assert skipped_result_deployed_interface_tags["value"] == "10G"
        assert skipped_result_deployed_interface_tags["device"] is None
        assert skipped_result_deployed_interface_tags["interface"] is None

        # skipped_cv_pathfinder_metadata — device is None
        skipped_result_deployed_cv_pathfinder_metadata = result["skipped_cv_pathfinder_metadata"][0]
        assert skipped_result_deployed_cv_pathfinder_metadata["metadata"] == {"role": "edge"}
        assert skipped_result_deployed_cv_pathfinder_metadata["device"] is None

        assert result["removed_configs"] == ["removed/leaf1.cfg"]
        assert result["removed_static_config_containers"] == ["OLD_CONTAINER"]
        assert result["removed_static_config_configlets"] == ["OLD_CONFIGLET"]

        # removed_device_tags
        assert result["removed_device_tags"][0]["label"] == "old_dc"
        assert result["removed_device_tags"][0]["value"] == "old_val"
        assert result["removed_device_tags"][0]["device"] is None

        # removed_interface_tags
        assert result["removed_interface_tags"][0]["label"] == "old_speed"
        assert result["removed_interface_tags"][0]["value"] == "old_val"
        assert result["removed_interface_tags"][0]["device"] is None

    def _make_populated_result(self) -> DeployToCvResult:
        """Return a DeployToCvResult with every field populated to verify complete resetting."""
        avd_ws = AvdWorkspace(name="workspace-name")
        avd_cc = AvdChangeControl(name="avd-cc-name", description="avd-cc-desc")
        device = CVDevice(avd_device=AvdDevice(hostname="leaf1", serial_number="snleaf1"))
        device.exists_on_cv = True
        device.streaming = False
        return DeployToCvResult(
            failed=True,
            errors=["err"],
            warnings=["warn"],
            workspace=CVWorkspace(avd_workspace=avd_ws, state="built", build_id="build-id", change_control_id="cc-id"),
            change_control=CVChangeControl(avd_change_control=avd_cc, id="cc-id", state="approved"),
            deployed_configs=[CVEosConfig(file="f.cfg", device=device)],
            deployed_static_config_containers=[AvdContainer(name="C", tag_query="all")],
            deployed_static_config_configlets=[AvdConfiglet(name="cfg1", file="f.cfg")],
            deployed_device_tags=[CVDeviceTag(label="dc", value="DC1", device=device)],
            deployed_interface_tags=[CVInterfaceTag(label="speed", value="100G", device=device, interface="Eth1")],
            deployed_studio_inputs=[CVStudioInputs(studio_id="s1", inputs={})],
            deployed_cv_pathfinder_metadata=[CVPathfinderMetadata(metadata={})],
            skipped_configs=[CVEosConfig(file="g.cfg", device=device)],
            skipped_static_config_containers=[AvdContainer(name="D", tag_query="role:leaf")],
            skipped_device_tags=[CVDeviceTag(label="rack", value="R1")],
            skipped_interface_tags=[CVInterfaceTag(label="mtu", value="9214")],
            skipped_cv_pathfinder_metadata=[CVPathfinderMetadata(metadata={})],
            removed_configs=["old.cfg"],
            removed_static_config_containers=["OLD"],
            removed_static_config_configlets=["OLD_CFG"],
            removed_device_tags=[CVDeviceTag(label="old", value="v")],
            removed_interface_tags=[CVInterfaceTag(label="old", value="v")],
        )

    def test_reset_runtime_fields_cleared(self) -> None:
        """Tests that failed, errors, warnings, and all deployed/skipped/removed list fields are cleared after reset."""
        result = self._make_populated_result()

        result.reset_mutable_fields()

        assert result.failed is False
        for dataclass_field in (
            "errors",
            "warnings",
            "deployed_configs",
            "deployed_static_config_containers",
            "deployed_static_config_configlets",
            "deployed_device_tags",
            "deployed_interface_tags",
            "deployed_studio_inputs",
            "deployed_cv_pathfinder_metadata",
            "skipped_configs",
            "skipped_static_config_containers",
            "skipped_device_tags",
            "skipped_interface_tags",
            "skipped_cv_pathfinder_metadata",
            "removed_configs",
            "removed_static_config_containers",
            "removed_static_config_configlets",
            "removed_device_tags",
            "removed_interface_tags",
        ):
            assert not getattr(result, dataclass_field)

    def test_reset_workspace_in_place(self) -> None:
        """Tests that the workspace object is reset in-place (its runtime fields are cleared)."""
        result = self._make_populated_result()
        original_ws = result.workspace

        result.reset_mutable_fields()

        assert result.workspace is original_ws
        assert result.workspace is not None
        assert result.workspace.state is None
        assert result.workspace.build_id is None
        assert result.workspace.change_control_id is None
        assert result.workspace.name == "workspace-name"

    def test_reset_change_control_in_place(self) -> None:
        """Tests that the change_control object is reset in-place (id/state cleared, name/description restored)."""
        result = self._make_populated_result()
        original_cc = result.change_control

        result.reset_mutable_fields()

        assert result.change_control is original_cc
        assert result.change_control is not None
        assert result.change_control.id is None
        assert result.change_control.state is None
        assert result.change_control.name == "avd-cc-name"
        assert result.change_control.description == "avd-cc-desc"

    def test_reset_none_workspace_and_change_control_remain_none(self) -> None:
        """Tests that when workspace and change_control start as None they remain None after reset."""
        result = DeployToCvResult()

        result.reset_mutable_fields()

        assert result.workspace is None
        assert result.change_control is None


class TestResetMutableFieldsUtility:
    """Unit tests for the reset_mutable_fields utility."""

    def test_frozen_dataclass_field_with_default_factory_is_preserved(self) -> None:
        """Tests that a frozen dataclass stored in a field that has default_factory is not replaced."""
        avd_ws = AvdWorkspace(name="workspace-name", id="ws-id")
        ws = CVWorkspace(avd_workspace=avd_ws, state="built")

        reset_mutable_fields(ws)

        # Must be the exact same object, not a fresh AvdWorkspace() from calling default_factory.
        assert ws.avd_workspace is avd_ws
        assert ws.name == "workspace-name"
        assert ws.id == "ws-id"

    def test_none_value_field_with_default_none_remains_none(self) -> None:
        """Tests that fields whose current value is None and whose default is None are handled without error."""
        ws = CVWorkspace()
        assert ws.state is None

        reset_mutable_fields(ws)

        assert ws.state is None

    def test_non_dataclass_object(self) -> None:
        """Tests that calling reset_mutable_fields on a non-dataclass does not raise."""
        plain_dict: dict = {"key": "value"}
        reset_mutable_fields(plain_dict)
        assert plain_dict == {"key": "value"}

    def test_frozen_dataclass_is_left_unchanged(self) -> None:
        """Tests that calling reset_mutable_fields on a frozen dataclass leaves all fields intact and does not raise FrozenInstanceError."""
        avd_ws = AvdWorkspace(name="workspace-name", id="ws-id")
        reset_mutable_fields(avd_ws)
        assert avd_ws.name == "workspace-name"
        assert avd_ws.id == "ws-id"

    def test_non_frozen_dataclass_field_without_reset_method(self) -> None:
        """Tests that a non-frozen dataclass stored in a field that has no reset_mutable_fields is reset recursively."""

        @dataclass
        class Inner:
            state: str = "original"

        @dataclass
        class Outer:
            inner: Inner = field(default_factory=Inner)
            state: str | None = None

        outer = Outer(inner=Inner(state="modified"), state="original")
        reset_mutable_fields(outer)

        assert outer.state is None
        assert outer.inner.state == "original"
