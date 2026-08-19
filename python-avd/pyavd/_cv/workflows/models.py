# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from dataclasses import dataclass, field, fields
from datetime import datetime
from logging import getLogger
from pathlib import Path
from typing import Any, Literal
from uuid import NAMESPACE_DNS, uuid4, uuid5

from grpclib.config import Configuration

from pyavd._cv.client.exceptions import CVManifestError
from pyavd._cv.client.models import CVTag, CVTagAssignment

from .utils import get_result

AVD_NAMESPACE = uuid5(NAMESPACE_DNS, "avd.arista.com")
AVD_ENTITY_PREFIX = "avd_"

LOGGER = getLogger(__name__)


@dataclass
class CVGRPCKeepalives:
    enabled: bool = False
    keepalive_time: int = 60
    keepalive_timeout: int = 20
    permit_without_calls: bool = False

    def __post_init__(self) -> None:
        if self.enabled and self.keepalive_time < 30:
            msg = f"Invalid CVGRPCKeepalives settings. keepalive_time must be >= 30s, got {self.keepalive_time}."
            raise ValueError(msg)


@dataclass
class CVGRPCChannelConfiguration:
    """Advanced configuration settings of the gRPC channel."""

    grpc_keepalives: CVGRPCKeepalives = field(default_factory=CVGRPCKeepalives)
    """Keepalive settings of the gRPC channel."""

    def as_grpclib_configuration(self) -> Configuration:
        if not self.grpc_keepalives.enabled:
            return Configuration()
        try:
            return Configuration(
                _keepalive_time=self.grpc_keepalives.keepalive_time,
                _keepalive_timeout=self.grpc_keepalives.keepalive_timeout,
                _keepalive_permit_without_calls=self.grpc_keepalives.permit_without_calls,
                # Disable the grpclib default cap of 2 pings without data so keepalives
                # continue for the duration of the deployment.
                _http2_max_pings_without_data=0,
                # Override grpclib's 300s rate-limit so pings fire at the configured interval.
                _http2_min_sent_ping_interval_without_data=self.grpc_keepalives.keepalive_time,
            )
        except TypeError:
            LOGGER.warning("deploy_to_cv: grpclib Configuration does not support the expected keepalive fields. gRPC keepalives will not be enabled.")
            return Configuration()


@dataclass
class CVDeployFuture:
    """Opt-in to future cv_deploy behaviors which will become defaults in a future major version."""

    use_system_certs: bool = False
    """Use system certificates and honor overrides with SSL_CERT_FILE and SSL_CERT_DIR. Will become the default in AVD 7.0."""


@dataclass
class CloudVision:
    servers: str | list[str]
    token: str | None
    username: str | None
    password: str | None
    verify_certs: bool
    proxy_host: str | None
    proxy_port: int | None
    proxy_username: str | None
    proxy_password: str | None
    grpc_channel_configuration: CVGRPCChannelConfiguration = field(default_factory=CVGRPCChannelConfiguration)
    deploy_future: CVDeployFuture = field(default_factory=CVDeployFuture)


@dataclass(frozen=True)
class AvdChangeControl:
    id: str | None = None
    """ID of an existing Change Control to manage."""
    name: str | None = None
    description: str | None = None
    change_control_template: AvdChangeControlTemplate | None = None
    requested_state: Literal["pending approval", "approved", "running", "completed", "deleted"] = "pending approval"
    """
    The requested state for the Change Control.

    - `"pending approval"` (default): Leave the Change Control in "pending approval" state.
    - `"approved"`: Approve the Change Control but do not start.
    - `"running"`: Approve and start the Change Control. Do not wait for the Change Control to be completed or failed.
    - `"completed"`: Approve and start the Change Control. Wait for the Change Control to be completed.
    - `"deleted"`: Create and delete the Change Control. Used for dry-run where no changes will be committed to the network.
    """
    approval_note: str = "Automatic approval by AVD"
    """Note used when approving the Change Control."""
    start_note: str = "Automatically started by AVD"
    """Note used when starting the Change Control."""


@dataclass
class CVChangeControl:
    avd_change_control: AvdChangeControl = field(default_factory=AvdChangeControl)
    id: str | None = None
    state: Literal["pending approval", "approved", "scheduled", "running", "completed", "deleted", "failed"] | None = None
    name: str | None = None
    description: str | None = None
    changed: bool = False
    """Set to `True` when the workflow modifies the Change Control."""

    def __post_init__(self) -> None:
        """
        Use intended ID, name and/or description as initial state.

        Replacing empty strings with None.
        """
        if not self.id:
            self.id = self.avd_change_control.id or None
        if not self.name:
            self.name = self.avd_change_control.name or None
        if not self.description:
            self.description = self.avd_change_control.description or None

    @property
    def change_control_template(self) -> AvdChangeControlTemplate | None:
        return self.avd_change_control.change_control_template

    @property
    def requested_state(self) -> Literal["pending approval", "approved", "running", "completed", "deleted"]:
        return self.avd_change_control.requested_state

    def get_result(self) -> dict[str, Any]:
        """Return a representation of this object for the Ansible module result."""
        return {
            "name": self.name,
            "description": self.description,
            "id": self.id,
            "change_control_template": get_result(self.change_control_template),
            "requested_state": self.requested_state,
            "state": self.state,
        }


@dataclass(frozen=True)
class AvdChangeControlTemplate:
    name: str
    id: str | None = None


@dataclass
class CVDeviceTag:
    label: str
    value: str
    device: CVDevice | None = None

    def as_cv_tag(self) -> CVTag:
        """Return the CVTag model for this tag."""
        return CVTag(
            element_type="device",
            label=self.label,
            value=self.value,
        )

    def as_cv_tag_assignment(self) -> CVTagAssignment | None:
        """Return the CVTagAssignment model for this tag."""
        if self.device is None or self.device.serial_number is None:
            return None

        return CVTagAssignment(
            element_type="device",
            label=self.label,
            value=self.value,
            device_id=self.device.serial_number,
            interface_id=None,
        )


@dataclass
class CVInterfaceTag:
    label: str
    value: str
    device: CVDevice | None = None
    interface: str | None = None
    """Must be set if device is set"""

    def as_cv_tag(self) -> CVTag:
        """Return the CVTag model for this tag."""
        return CVTag(
            element_type="interface",
            label=self.label,
            value=self.value,
        )

    def as_cv_tag_assignment(self) -> CVTagAssignment | None:
        """Return the CVTagAssignment model for this tag."""
        if self.device is None or self.device.serial_number is None or self.interface is None:
            return None

        return CVTagAssignment(
            element_type="interface",
            label=self.label,
            value=self.value,
            device_id=self.device.serial_number,
            interface_id=self.interface,
        )


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
class CVWorkspaceBuildConfigValidationError:
    error_msg: str | None = None
    """EOS-returned error message."""
    line_num: int | None = None
    """Line number of the violating configuration line within the configlet."""
    configlet_name: str | None = None
    """Name of the configlet which raised validation error."""


@dataclass
class CVWorkspaceBuildConfigValidationWarning:
    warning_msg: str | None = None
    """EOS-returned warning message."""
    line_num: int | None = None
    """Line number of the violating configuration line within the configlet."""
    configlet_name: str | None = None
    """Name of the configlet which returned validation warning."""


@dataclass
class CVWorkspaceBuildConfigValidationResult:
    errors: list[CVWorkspaceBuildConfigValidationError] = field(default_factory=list)
    warnings: list[CVWorkspaceBuildConfigValidationWarning] = field(default_factory=list)


@dataclass
class CVWorkspaceDeviceBuildResult:
    device: CVDevice
    config_validation: CVWorkspaceBuildConfigValidationResult
    """Configuration validation results."""


@dataclass(frozen=True)
class AvdWorkspaceBuildWarningsConfig:
    enabled: bool = True
    """Fetch and expose Workspace build warnings."""
    suppress_patterns: tuple[str, ...] = field(default_factory=tuple)
    """Arbitrary tuple of the EOS CLI warning string patterns to suppress."""
    suppress_portfast: bool = False
    """Suppress Workspace build warnings related to the usage of the `portfast` feature on switchports."""

    @classmethod
    def from_dict(cls, data: dict) -> AvdWorkspaceBuildWarningsConfig:
        """Build an AvdWorkspaceBuildWarningsConfig instance from an input dictionary."""
        try:
            copied_data = data.copy()
            suppress_patterns = tuple(copied_data.pop("suppress_patterns", ()))
            return cls(suppress_patterns=suppress_patterns, **copied_data)
        except (AttributeError, TypeError) as e:
            msg = f"Invalid AvdWorkspaceBuildWarningsConfig definition: {data}. Error: {e}"
            raise ValueError(msg) from e


@dataclass(frozen=True)
class AvdWorkspace:
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
    build_warnings: AvdWorkspaceBuildWarningsConfig = field(default_factory=AvdWorkspaceBuildWarningsConfig)
    """Configuration settings to control fetching and exposing Workspace build warnings."""


@dataclass
class CVWorkspace:
    avd_workspace: AvdWorkspace = field(default_factory=AvdWorkspace)
    state: Literal["pending", "built", "submitted", "build failed", "submit failed", "abandoned", "deleted"] | None = None
    """The current state of the Workspace."""
    change_control_id: str | None = None
    build_id: str | None = None
    """last_build_id of the Workspace. Used to fetch build details related to the last Workspace build attempt."""
    device_build_results: list[CVWorkspaceDeviceBuildResult] = field(default_factory=list)
    """Details of per-device Workspace build results."""

    @property
    def name(self) -> str:
        return self.avd_workspace.name

    @property
    def description(self) -> str | None:
        return self.avd_workspace.description

    @property
    def id(self) -> str:
        return self.avd_workspace.id

    @property
    def requested_state(self) -> Literal["pending", "built", "submitted", "abandoned", "deleted"]:
        return self.avd_workspace.requested_state

    @property
    def force(self) -> bool:
        return self.avd_workspace.force

    @property
    def build_warnings(self) -> AvdWorkspaceBuildWarningsConfig:
        return self.avd_workspace.build_warnings

    def get_result(self) -> dict[str, Any]:
        """Return a representation of this object for the Ansible module result."""
        return {
            "name": self.name,
            "description": self.description,
            "id": self.id,
            "requested_state": self.requested_state,
            "force": self.force,
            "state": self.state,
            "change_control_id": self.change_control_id,
            "build_id": self.build_id,
            "build_warnings": get_result(self.build_warnings),
            "device_build_results": get_result(self.device_build_results),
        }


@dataclass
class DeployToCvResult:
    failed: bool = False
    errors: list = field(default_factory=list)
    warnings: list = field(default_factory=list)
    workspace: CVWorkspace | None = None
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
    removed_static_config_containers: list[str] = field(default_factory=list)
    removed_static_config_configlets: list[str] = field(default_factory=list)
    removed_device_tags: list[CVDeviceTag] = field(default_factory=list)
    removed_interface_tags: list[CVInterfaceTag] = field(default_factory=list)

    def get_result(self) -> dict[str, Any]:
        """Return a representation of this object for the Ansible module result."""
        return {f.name: get_result(getattr(self, f.name)) for f in fields(self)}


@dataclass(frozen=True)
class AvdDevice:
    hostname: str
    """
    Device hostname or intended hostname.
    `serial_number` or `system_mac_address` must be set if the hostname is not already configured on the device or
    if the hostname is not unique.
    """
    serial_number: str | None = None
    system_mac_address: str | None = None


@dataclass
class CVDevice:
    avd_device: AvdDevice
    serial_number: str | None = None
    system_mac_address: str | None = None
    exists_on_cv: bool | None = None
    streaming: bool | None = None
    """Device's streaming status."""

    def __post_init__(self) -> None:
        """
        Use intended serial_number and/or system_mac_address as initial state.

        Replacing empty strings with None.
        """
        if not self.serial_number:
            self.serial_number = self.avd_device.serial_number or None
        if not self.system_mac_address:
            self.system_mac_address = self.avd_device.system_mac_address or None

    @property
    def hostname(self) -> str:
        return self.avd_device.hostname

    def get_result(self) -> dict[str, Any]:
        """Return a representation of this object for the Ansible module result."""
        return {
            "hostname": self.hostname,
            "serial_number": self.serial_number,
            "system_mac_address": self.system_mac_address,
            "exists_on_cv": self.exists_on_cv,
            "streaming": self.streaming,
        }


@dataclass
class CVEosConfig:
    file: str
    """Path to file containing EOS Config"""
    device: CVDevice
    configlet_name: str | None = None
    """By default "AVD_<hostname>"""


@dataclass
class CVDeviceDeployment:
    """All deployment objects for a single device."""

    device: CVDevice
    use_static_config_manifest: bool = False
    """When `True`, the device configuration is expected to be deployed via the static config manifest hierarchy
    instead of the flat "AVD Configurations" layout."""
    eos_config: CVEosConfig | None = None
    device_tags: list[CVDeviceTag] = field(default_factory=list)
    interface_tags: list[CVInterfaceTag] = field(default_factory=list)
    cv_pathfinder_metadata: CVPathfinderMetadata | None = None


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
    Input configlet from the static configuration manifest.

    Can be assigned to one or more containers.
    """

    name: str
    file: str

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> AvdConfiglet:
        """Build an AvdConfiglet instance from an input dictionary."""
        try:
            return cls(name=data["name"], file=str(Path(data["file"]).resolve()))
        except (KeyError, TypeError) as e:
            msg = f"Invalid configlet definition: {data}. Error: {e}"
            raise ValueError(msg) from e


@dataclass(frozen=True)
class AvdContainer:
    """
    Input container from the static configuration manifest.

    Containers are recursive, allowing for a nested hierarchy.
    """

    name: str
    tag_query: str
    description: str | None = None
    match_policy: Literal["match_all", "match_first"] = field(default="match_all")
    configlets: tuple[str, ...] = field(default_factory=tuple)
    sub_containers: tuple[AvdContainer, ...] = field(default_factory=tuple)
    preserve_existing_sub_containers: bool = False

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
    Input static configuration manifest.

    This model defines the desired state for containers and configlets in the "Static Configuration" Studio.

    It can contain a full container hierarchy, only configlets, or both.
    """

    configlets: tuple[AvdConfiglet, ...] = field(default_factory=tuple)
    containers: tuple[AvdContainer, ...] = field(default_factory=tuple)
    preserve_existing_containers: bool = False

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> AvdManifest:
        """Build an AvdManifest instance from an input dictionary."""
        try:
            configlets_data = data.get("configlets", [])
            containers_data = data.get("containers", [])
            preserve_existing_containers = data.get("preserve_existing_containers", False)

            configlets = tuple(AvdConfiglet.from_dict(configlet_data) for configlet_data in configlets_data)
            containers = tuple(AvdContainer.from_dict(container_data) for container_data in containers_data)

            return cls(configlets=configlets, containers=containers, preserve_existing_containers=preserve_existing_containers)
        except (KeyError, TypeError, ValueError) as e:
            msg = f"Failed to build the static configuration manifest. Please check your input data. Original error: {e}"
            raise ValueError(msg) from e


@dataclass(frozen=True)
class CVManifest:
    """CloudVision manifest to be created/updated to the "Static Configuration" Studio."""

    configlets: tuple[CVConfiglet, ...]
    containers: tuple[CVContainer, ...]
    preserve_existing_containers: bool = False

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
        return cls(
            configlets=tuple(cv_configlet_map.values()),
            containers=tuple(cv_container_map.values()),
            preserve_existing_containers=avd_manifest.preserve_existing_containers,
        )

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
    def file(self) -> str:
        return self.avd_configlet.file

    @property
    def api_tuple(self) -> tuple[str, str, str, str]:
        """Return a tuple representation of the configlet compatible with the CVClient APIs."""
        return (self.id, self.name, self.description, self.file)


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
