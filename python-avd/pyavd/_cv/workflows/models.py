# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import TYPE_CHECKING, Any, Literal
from uuid import NAMESPACE_DNS, uuid4, uuid5

from pyavd._cv.client.configlet import ASSIGNMENT_MATCH_POLICY_MAP
from pyavd._cv.client.exceptions import CVManifestError

AVD_NAMESPACE = uuid5(NAMESPACE_DNS, "avd.arista.com")
AVD_ENTITY_PREFIX = "avd_"

if TYPE_CHECKING:
    from pyavd._cv.api.arista.configlet.v1 import ConfigletAssignment


@dataclass
class CloudVision:
    servers: str | list[str]
    token: str | None
    username: str | None
    password: str | None
    verify_certs: bool = True


@dataclass
class CVChangeControl:
    name: str | None = None
    description: str | None = None
    id: str | None = None
    """ `id` should not be set on the request. It will be updated with the ID of the created Change Control. """
    change_control_template: CVChangeControlTemplate | None = None
    requested_state: Literal["pending approval", "approved", "running", "completed", "deleted"] = "pending approval"
    """
    The requested state for the Change Control.

    - `"pending approval"` (default): Leave the Change Control in "pending approval" state.
    - `"approved"`: Approve the Change Control but do not start.
    - `"running"`: Approve and start the Change Control. Do not wait for the Change Control to be completed or failed.
    - `"completed"`: Approve and start the Change Control. Wait for the Change Control to be completed.
    - `"deleted"`: Create and delete the Change Control. Used for dry-run where no changes will be committed to the network.
    """
    state: Literal["pending approval", "approved", "running", "completed", "deleted", "failed"] | None = None


@dataclass
class CVChangeControlTemplate:
    name: str
    id: str | None = None


@dataclass
class CVDeviceTag:
    label: str
    value: str
    device: CVDevice | None = None


@dataclass
class CVInterfaceTag:
    label: str
    value: str
    device: CVDevice | None = None
    interface: str | None = None
    """Must be set if device is set"""


@dataclass
class CVStudioInputs:
    studio_id: str
    inputs: Any
    """Data to set at the given path."""
    input_path: list[str] = field(default_factory=list)
    """Data path elements for setting specific inputs. If not given, inputs are set at the root, replacing all existing inputs."""


@dataclass
class CVPathfinderMetadata:
    metadata: dict
    device: CVDevice | None = None


@dataclass
class CVWorkspace:
    name: str = field(default_factory=lambda: f"AVD {datetime.now()}")
    description: str | None = None
    id: str = field(default_factory=lambda: f"ws-{uuid4()}")
    requested_state: Literal["pending", "built", "submitted", "abandoned", "deleted"] = "submitted"
    """
    The requested state for the Workspace.

    - `"pending"`: Leave the Workspace in pending state.
    - `"built"`: Build the Workspace but do not submit.
    - `"submitted"` (default): Build and submit the Workspace.
    - `"abandoned"`: Build and then abandon the Workspace. \
        Used for dry-run where no changes will be committed to CloudVision.
    - `"deleted"`: Build, abort and then delete the Workspace. \
        Used for dry-run where no changes will be committed to CloudVision and the temporary Workspace will be removed to avoid "clutter".
    """
    force: bool = False
    """ Force submit the workspace even if some devices are not actively streaming to CloudVision."""
    state: Literal["pending", "built", "submitted", "build failed", "submit failed", "abandoned", "deleted"] | None = None
    """The final state of the Workspace. Do not set this manually."""
    change_control_id: str | None = None
    """Do not set this manually."""


@dataclass
class DeployChangeControlResult:
    failed: bool = False
    errors: list = field(default_factory=list)
    warnings: list = field(default_factory=list)
    change_control: CVChangeControl | None = None
    deployed_devices: list[CVDevice] = field(default_factory=list)
    skipped_devices: list[CVDevice] = field(default_factory=list)


@dataclass
class DeployToCvResult:
    failed: bool = False
    errors: list = field(default_factory=list)
    warnings: list = field(default_factory=list)
    workspace: CVWorkspace | None = field(default_factory=CVWorkspace)
    change_control: CVChangeControl | None = None
    deployed_configs: list[CVEosConfig] = field(default_factory=list)
    deployed_static_config_containers: list[AvdContainer] = field(default_factory=list)
    deployed_static_config_configlets: list[AvdConfiglet] = field(default_factory=list)
    deployed_device_tags: list[CVDeviceTag] = field(default_factory=list)
    deployed_interface_tags: list[CVInterfaceTag] = field(default_factory=list)
    deployed_studio_inputs: list[CVStudioInputs] = field(default_factory=list)
    deployed_cv_pathfinder_metadata: list[CVPathfinderMetadata] = field(default_factory=list)
    skipped_configs: list[CVEosConfig] = field(default_factory=list)
    skipped_static_config_containers: list[AvdContainer] = field(default_factory=list)
    skipped_device_tags: list[CVDeviceTag] = field(default_factory=list)
    skipped_interface_tags: list[CVInterfaceTag] = field(default_factory=list)
    skipped_cv_pathfinder_metadata: list[CVPathfinderMetadata] = field(default_factory=list)
    removed_configs: list[str] = field(default_factory=list)
    removed_static_config_root_containers: list[str] = field(default_factory=list)
    removed_static_config_configlets: list[str] = field(default_factory=list)
    removed_device_tags: list[CVDeviceTag] = field(default_factory=list)
    removed_interface_tags: list[CVInterfaceTag] = field(default_factory=list)


@dataclass
class CVDevice:
    hostname: str
    """
    Device hostname or intended hostname.
    `serial_number` or `system_mac_address` must be set if the hostname is not already configured on the device or
    if the hostname is not unique.
    """
    serial_number: str | None = None
    system_mac_address: str | None = None
    _exists_on_cv: bool | None = None
    """ Do not set this manually. """


@dataclass
class CVEosConfig:
    file: str
    """Path to file containing EOS Config"""
    device: CVDevice
    configlet_name: str | None = None
    """By default "AVD_<hostname>"""


@dataclass
class CVTimeOuts:
    """Timeouts in seconds."""

    workspace_build_timeout: float = 300.0
    change_control_creation_timeout: float = 300.0


@dataclass
class DuplicatedSystemMacAddress:
    unset_or_mixed_serial_number: dict[str, list[CVDevice]] = field(default_factory=dict)
    """Dictionary holding CVDevices with duplicated system_mac_address and at least one device with unset serial_number."""
    set_serial_number: dict[str, list[CVDevice]] = field(default_factory=dict)
    """Dictionary holding CVDevices with duplicated system_mac_address and set serial_number."""


@dataclass
class DuplicatedDevices:
    system_mac_address: DuplicatedSystemMacAddress = field(default_factory=DuplicatedSystemMacAddress)
    """Object holding CVDevices with duplicated system_mac_address."""
    serial_number: dict[str, list[CVDevice]] = field(default_factory=dict)
    """Dictionary holding CVDevices with duplicated serial_number."""

    def detected(self) -> bool:
        return any([self.serial_number, self.system_mac_address.unset_or_mixed_serial_number, self.system_mac_address.set_serial_number])


@dataclass(frozen=True)
class AvdConfiglet:
    """
    Input configlet generated by AVD.

    Can be assigned to one or more containers.
    """

    name: str
    file: Path

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> AvdConfiglet:
        """Build an AvdConfiglet instance from an input dictionary."""
        try:
            return cls(name=data["name"], file=Path(data["file"]).resolve())
        except (KeyError, TypeError) as e:
            msg = f"Invalid configlet definition: {data}. Error: {e}"
            raise ValueError(msg) from e


@dataclass(frozen=True)
class AvdContainer:
    """
    Input container generated by AVD.

    Containers are recursive, allowing for a nested hierarchy.
    """

    name: str
    tag_query: str
    description: str | None = None
    match_policy: Literal["match_all", "match_first"] = field(default="match_all")
    configlets: tuple[str, ...] = field(default_factory=tuple)
    sub_containers: tuple[AvdContainer, ...] = field(default_factory=tuple)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> AvdContainer:
        """Recursively build an AvdContainer instance from an input dictionary."""
        try:
            copied_data = data.copy()
            sub_containers_data = copied_data.pop("sub_containers", [])
            sub_containers = tuple(cls.from_dict(sub_container_data) for sub_container_data in sub_containers_data)

            configlets_data = copied_data.pop("configlets", [])
            configlets = tuple(item["name"] for item in configlets_data)

            return cls(sub_containers=sub_containers, configlets=configlets, **copied_data)
        except (AttributeError, KeyError, TypeError) as e:
            msg = f"Invalid container definition: {data}. Error: {e}"
            raise ValueError(msg) from e


@dataclass(frozen=True)
class AvdManifest:
    """
    Input manifest generated by AVD.

    This model defines the desired state for containers and configlets in the "Static Configuration" Studio.

    It can contain a full container hierarchy, only configlets, or both.
    """

    configlets: tuple[AvdConfiglet, ...] = field(default_factory=tuple)
    containers: tuple[AvdContainer, ...] = field(default_factory=tuple)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> AvdManifest:
        """Build an AvdManifest instance from an input dictionary."""
        try:
            configlets_data = data.get("configlets", [])
            containers_data = data.get("containers", [])

            configlets = tuple(AvdConfiglet.from_dict(configlet_data) for configlet_data in configlets_data)
            containers = tuple(AvdContainer.from_dict(container_data) for container_data in containers_data)

            return cls(configlets=configlets, containers=containers)
        except (KeyError, TypeError, ValueError) as e:
            msg = f"Failed to build the static configuration manifest. Please check your input data. Original error: {e}"
            raise ValueError(msg) from e


@dataclass(frozen=True)
class CVManifest:
    """CloudVision manifest to be created/updated to the "Static Configuration" Studio."""

    configlets: tuple[CVConfiglet, ...]
    containers: tuple[CVContainer, ...]

    @classmethod
    def from_avd_manifest(cls, avd_manifest: AvdManifest) -> CVManifest:
        """Build the desired CVManifest from the AVD input manifest."""
        cv_configlet_map: dict[str, CVConfiglet] = {}
        cv_container_map: dict[str, CVContainer] = {}

        # Create all CVConfiglet objects first.
        for avd_configlet in avd_manifest.configlets:
            cv_configlet = CVConfiglet(
                avd_configlet=avd_configlet, id=cls._generate_deterministic_id(avd_configlet.name), description="Configlet created and uploaded by AVD."
            )
            if cv_configlet.name in cv_configlet_map:
                msg = f"Duplicate configlet name found: '{cv_configlet.name}'. All AVD-managed configlet names must be unique."
                raise CVManifestError(msg)
            cv_configlet_map[cv_configlet.name] = cv_configlet

        # Recursively process all containers.
        for root_container in avd_manifest.containers:
            cls._process_container_recursively(container=root_container, parent_path="", cv_configlet_map=cv_configlet_map, cv_container_map=cv_container_map)

        # Return the completed manifest.
        return cls(configlets=tuple(cv_configlet_map.values()), containers=tuple(cv_container_map.values()))

    @classmethod
    def _process_container_recursively(
        cls, container: AvdContainer, parent_path: str, cv_configlet_map: dict[str, CVConfiglet], cv_container_map: dict[str, CVContainer]
    ) -> str:
        """Recursively traverse the container tree, populating the cv_ mappings along the way. Returns the generated ID for the current container."""
        current_path = f"{parent_path}/{container.name}" if parent_path else container.name

        # Process sub-containers.
        child_ids = [
            cls._process_container_recursively(sub_container, current_path, cv_configlet_map, cv_container_map) for sub_container in container.sub_containers
        ]

        # Process configlets attached to this container.
        configlet_ids = []
        for configlet_name in container.configlets:
            if configlet_name not in cv_configlet_map:
                msg = f"Configlet '{configlet_name}' is assigned to a container but is not found in the input definition."
                raise CVManifestError(msg)
            configlet_ids.append(cv_configlet_map[configlet_name].id)

        # Create the parent CVContainer object.
        cv_container = CVContainer(
            avd_container=container,
            id=cls._generate_deterministic_id(current_path),
            is_root=(parent_path == ""),
            configlet_ids=tuple(configlet_ids),
            child_ids=tuple(child_ids),
        )

        # Store it in the main dictionary.
        if current_path in cv_container_map:
            msg = f"Duplicate container name found: '{current_path}'. All AVD-managed sibling containers must have unique names."
            raise CVManifestError(msg)
        cv_container_map[current_path] = cv_container

        return cv_container.id

    @staticmethod
    def _generate_deterministic_id(key: str) -> str:
        """Generate a deterministic ID from AVD_NAMESPACE and the provided key."""
        return f"{AVD_ENTITY_PREFIX}{uuid5(AVD_NAMESPACE, key)}"


@dataclass(frozen=True)
class CVConfiglet:
    """CloudVision configlet to be create/updated to the "Static Configuration" Studio configlet library."""

    avd_configlet: AvdConfiglet
    id: str
    description: str

    @property
    def name(self) -> str:
        return self.avd_configlet.name

    @property
    def file(self) -> Path:
        return self.avd_configlet.file

    @property
    def api_tuple(self) -> tuple[str, str, str, str]:
        """Return a tuple representation of the configlet compatible with the CVClient APIs."""
        return (self.id, self.name, self.description, str(self.file))


@dataclass(frozen=True)
class CVContainer:
    """CloudVision container to be create/updated to the "Static Configuration" Studio hierarchy."""

    avd_container: AvdContainer
    id: str
    is_root: bool
    configlet_ids: tuple[str, ...] = field(default_factory=tuple)
    child_ids: tuple[str, ...] = field(default_factory=tuple)

    @property
    def name(self) -> str:
        return self.avd_container.name

    @property
    def description(self) -> str | None:
        return self.avd_container.description

    @property
    def tag_query(self) -> str:
        return self.avd_container.tag_query

    @property
    def match_policy(self) -> str:
        return self.avd_container.match_policy

    @property
    def api_tuple(self) -> tuple[Any, ...]:
        """Return a tuple representation of the container compatible with the CVClient APIs."""
        return (self.id, self.name, self.description or "", list(self.configlet_ids), self.tag_query, list(self.child_ids), self.match_policy)

    def matches_configlet_assignment(self, configlet_assignment: ConfigletAssignment) -> bool:
        """
        Check if this container state matches a ConfigletAssignment from CVClient APIs.

        This is primarily used to determine if the local configuration has diverged from the
        remote configuration, indicating whether an update is required.
        """
        reversed_match_policy_map = {enum_member.value: str_key for str_key, enum_member in ASSIGNMENT_MATCH_POLICY_MAP.items()}
        return self.api_tuple == (
            configlet_assignment.key.configlet_assignment_id,
            configlet_assignment.display_name,
            configlet_assignment.description,
            configlet_assignment.configlet_ids.values,
            configlet_assignment.query,
            configlet_assignment.child_assignment_ids.values,
            reversed_match_policy_map.get(configlet_assignment.match_policy.value),
        )
