# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

import pytest

from pyavd._cv.api.arista.configlet.v1 import ConfigletAssignment, ConfigletAssignmentKey, MatchPolicy
from pyavd._cv.api.fmp import RepeatedString
from pyavd._cv.client.exceptions import CVManifestError
from pyavd._cv.workflows.models import AVD_ENTITY_PREFIX, AvdConfiglet, AvdContainer, AvdManifest, CVContainer, CVManifest

from .helpers import generate_id

# === Test Fixtures ===


@pytest.fixture
def complex_avd_manifest() -> AvdManifest:
    """Provides a complex, valid AVD manifest with nested containers and configlets."""
    # Configlets definition.
    configlet1 = AvdConfiglet(name="configlet_global", file="path/to/global.cfg")
    configlet2 = AvdConfiglet(name="configlet_leaf", file="path/to/leaf.cfg")
    configlet3 = AvdConfiglet(name="configlet_extra", file="path/to/extra.cfg")

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
        assert cv_cfg.file == "path/to/leaf.cfg"
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
        configlet1 = AvdConfiglet(name="duplicate_name", file="file1.conf")
        configlet2 = AvdConfiglet(name="duplicate_name", file="file2.conf")
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

        with pytest.raises(CVManifestError, match="Configlet 'missing_configlet' is assigned to a container but is not found in the input definition."):
            CVManifest.from_avd_manifest(avd_manifest)

    def test_manifest_with_configlets_only(self) -> None:
        """Tests a manifest that has configlets but no container definitions."""
        configlet = AvdConfiglet(name="cfg1", file="file1.cfg")
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


class TestCVContainerMatching:
    @pytest.fixture
    def test_cv_container(self) -> CVContainer:
        """Creates a single CVContainer instance for matching tests."""
        # Setup data to create one container instance.
        avd_cfg = AvdConfiglet(name="test_cfg", file="test.cfg")
        avd_container = AvdContainer(
            name="TEST_CONTAINER", description="Test Description", tag_query="app:test", match_policy="match_all", configlets=("test_cfg",)
        )

        # Manually create dependent objects for CVContainer constructor.
        # In a real scenario, we'd run CVManifest.from_avd_manifest, but here we can isolate CVContainer.
        configlet_id = generate_id(avd_cfg.name)
        container_id = generate_id(avd_container.name)

        return CVContainer(
            avd_container=avd_container,
            id=container_id,
            is_root=True,
            configlet_ids=(configlet_id,),
            child_ids=(),
        )

    def test_matches_configlet_assignment_success(self, test_cv_container: CVContainer) -> None:
        """Tests successful match between local CVContainer and remote ConfigletAssignment."""
        # Create an API object that perfectly matches test_cv_container.
        api_assignment = ConfigletAssignment(
            key=ConfigletAssignmentKey(configlet_assignment_id=test_cv_container.id),
            display_name=test_cv_container.name,
            description=test_cv_container.description,
            configlet_ids=RepeatedString(values=list(test_cv_container.configlet_ids)),
            query=test_cv_container.tag_query,
            child_assignment_ids=RepeatedString(values=list(test_cv_container.child_ids)),
            match_policy=MatchPolicy.MATCH_ALL,
        )

        assert test_cv_container.matches_configlet_assignment(api_assignment) is True

    @pytest.mark.parametrize(
        "mismatch_field",
        [
            pytest.param("id", id="mismatch on id field"),
            pytest.param("name", id="mismatch on name field"),
            pytest.param("description", id="mismatch on description field"),
            pytest.param("configlet_ids", id="mismatch on configlet_ids field"),
            pytest.param("tag_query", id="mismatch on tag_query field"),
            pytest.param("child_ids", id="mismatch on child_ids field"),
            pytest.param("match_policy", id="mismatch on match_policy field"),
        ],
    )
    def test_matches_configlet_assignment_mismatch(self, test_cv_container: CVContainer, mismatch_field: str) -> None:
        """Tests mismatch detection for each field individually."""
        # Create a mock remote object that perfectly matches test_cv_container.
        mock_assignment = ConfigletAssignment(
            key=ConfigletAssignmentKey(configlet_assignment_id=test_cv_container.id),
            display_name=test_cv_container.name,
            description=test_cv_container.description,
            configlet_ids=RepeatedString(values=list(test_cv_container.configlet_ids)),
            query=test_cv_container.tag_query,
            child_assignment_ids=RepeatedString(values=list(test_cv_container.child_ids)),
            match_policy=MatchPolicy.MATCH_ALL,
        )

        # Introduce a mismatch based on the test parameter using match case.
        match mismatch_field:
            case "id":
                mock_assignment.key.configlet_assignment_id = "wrong-id"
            case "name":
                mock_assignment.display_name = "Wrong Name"
            case "description":
                mock_assignment.description = "Wrong Description"
            case "configlet_ids":
                mock_assignment.configlet_ids.values = ["wrong-configlet-id"]
            case "tag_query":
                mock_assignment.query = "wrong-query"
            case "child_ids":
                mock_assignment.child_assignment_ids.values = ["wrong-child-id"]
            case "match_policy":
                mock_assignment.match_policy = MatchPolicy.MATCH_FIRST  # Change to match_first

        # Assert failure.
        assert test_cv_container.matches_configlet_assignment(mock_assignment) is False

    def test_description_none_matches_empty_string(self) -> None:
        """Tests that a local container with description=None matches a remote with description=''."""
        # Create container with description=None.
        avd_container = AvdContainer(name="NO_DESC_CONTAINER", tag_query="q1", description=None)
        cv_container = CVContainer(
            avd_container=avd_container,
            id=generate_id(avd_container.name),
            is_root=True,
        )

        # Create mock assignment with description="".
        mock_assignment = ConfigletAssignment(
            key=ConfigletAssignmentKey(configlet_assignment_id=cv_container.id),
            display_name=cv_container.name,
            description="",  # Remote side has empty string
            configlet_ids=RepeatedString(values=[]),
            query=cv_container.tag_query,
            child_assignment_ids=RepeatedString(values=[]),
            match_policy=MatchPolicy.MATCH_ALL,
        )

        # Verify api_tuple logic (self.description or "") works.
        assert cv_container.matches_configlet_assignment(mock_assignment) is True
