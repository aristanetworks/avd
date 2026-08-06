# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import json
import logging
from asyncio import gather, run
from pathlib import Path
from string import Template
from typing import Any, Literal

from ansible.errors import AnsibleActionFail
from ansible.plugins.action import ActionBase, display
from yaml import load

from ansible_collections.arista.avd.plugins.plugin_utils.utils import (
    AVDFileHandler,
    AVDVaultHandler,
    PythonToAnsibleHandler,
    YamlLoader,
    get_tmp_paths,
    raise_action_fail,
)

PLUGIN_NAME = "arista.avd.cv_workflow"

try:
    from pyavd._cv.workflows.deploy_to_cv import deploy_to_cv
    from pyavd._cv.workflows.models import (
        AvdChangeControl,
        AvdDevice,
        AvdManifest,
        AvdWorkspace,
        AvdWorkspaceBuildWarningsConfig,
        CloudVision,
        CVChangeControl,
        CVDeployFuture,
        CVDevice,
        CVDeviceDeployment,
        CVDeviceTag,
        CVEosConfig,
        CVGRPCChannelConfiguration,
        CVGRPCKeepalives,
        CVInterfaceTag,
        CVPathfinderMetadata,
        CVTimeOuts,
        CVWorkspace,
        DeployToCvResult,
    )
    from pyavd._cv.workflows.utils import extract_from_device_deployments, get_result
    from pyavd._utils import default, get, strip_empties_from_dict

    HAS_PYAVD = True
except ImportError:
    HAS_PYAVD = False


LOGGER = logging.getLogger("ansible_collections.arista.avd")
LOGGING_LEVELS = ["DEBUG", "INFO", "ERROR", "WARNING", "CRITICAL"]

ARGUMENT_SPEC = {
    "tmp_dir": {"type": "str", "required": False},
    "preview_features": {
        "type": "dict",
        "options": {
            "read_from_validated_inputs": {"type": "bool", "default": False},
        },
    },
    "grpc_keepalives": {
        "type": "dict",
        "required": False,
        "options": {
            "enabled": {"type": "bool", "required": False, "default": False},
            "keepalive_time": {"type": "int", "required": False, "default": 60},
            "keepalive_timeout": {"type": "int", "required": False, "default": 20},
            "permit_without_calls": {"type": "bool", "required": False, "default": False},
        },
    },
    # TODO: Make configuration_dir optional for users using the manifest to push device configs.
    "configuration_dir": {"type": "str", "required": True},
    "structured_config_dir": {"type": "str", "required": False},
    "structured_config_suffix": {"type": "str", "default": "yml"},
    "device_list": {"type": "list", "elements": "str", "required": False},
    "strict_tags": {"type": "bool", "required": False, "default": False},
    "skip_missing_devices": {"type": "bool", "required": False, "default": False},
    "strict_system_mac_address": {"type": "bool", "required": False, "default": False},
    "inventory_mode": {"type": "str", "required": False, "default": "loose", "choices": ["loose", "controlled"]},
    "configlet_name_template": {"type": "str", "default": "AVD-${hostname}"},
    "cv_servers": {"type": "list", "elements": "str", "required": True},
    "cv_token": {"type": "str", "secret": True, "required": False},
    "cv_username": {"type": "str", "required": False},
    "cv_password": {"type": "str", "secret": True, "required": False},
    "cv_verify_certs": {"type": "bool", "default": True},
    "cv_deploy_future": {
        "type": "dict",
        "options": {
            "use_system_certs": {"type": "bool", "default": False},
        },
    },
    "proxy_host": {"type": "str", "required": False},
    "proxy_port": {"type": "int", "required": False, "default": 8080},
    "proxy_username": {"type": "str", "required": False},
    "proxy_password": {"type": "str", "secret": True, "required": False},
    "workspace": {
        "type": "dict",
        "options": {
            "name": {"type": "str", "required": False},
            "description": {"type": "str", "required": False},
            "id": {"type": "str", "required": False},
            "requested_state": {"type": "str", "default": "built", "choices": ["pending", "built", "submitted", "abandoned", "deleted"]},
            "force": {"type": "bool", "default": False},
            "build_warnings": {
                "type": "dict",
                "options": {
                    "enabled": {"type": "bool", "required": False, "default": True},
                    "suppress_patterns": {"type": "list", "elements": "str", "required": False, "default": []},
                    "suppress_portfast": {"type": "bool", "required": False, "default": False},
                },
            },
        },
    },
    "change_control": {
        "type": "dict",
        "options": {
            "name": {"type": "str", "required": False},
            "description": {"type": "str", "required": False},
            "requested_state": {"type": "str", "default": "pending approval", "choices": ["pending approval", "approved", "running", "completed"]},
        },
    },
    "timeouts": {
        "type": "dict",
        "options": {
            "workspace_build_timeout": {"type": "float", "default": CVTimeOuts.workspace_build_timeout if HAS_PYAVD else 300.0},
            "change_control_creation_timeout": {"type": "float", "default": CVTimeOuts.change_control_creation_timeout if HAS_PYAVD else 300.0},
        },
    },
    "static_config_manifest": {
        "type": "dict",
        "options": {
            "preserve_existing_containers": {"type": "bool", "default": False},
            "containers": {"type": "list", "elements": "dict", "required": False},
            "configlets": {"type": "list", "elements": "dict", "required": False},
        },
    },
    "return_details": {"type": "bool", "required": False, "default": False},
}


class ActionModule(ActionBase):
    def run(self, tmp: Any = None, task_vars: dict | None = None) -> dict:
        self._supports_check_mode = False

        if task_vars is None:
            task_vars = {}

        result = super().run(tmp, task_vars)
        del tmp  # tmp no longer has any effect

        if not HAS_PYAVD:
            msg = "The 'arista.avd.cv_workflow' plugin requires the 'pyavd' Python library. Got import error"
            raise AnsibleActionFail(msg)

        # Setup module logging
        setup_module_logging(result)

        # Get task arguments and validate them
        _validation_result, validated_args = self.validate_argument_spec(ARGUMENT_SPEC)
        validated_args = strip_empties_from_dict(validated_args)

        # Converting to json and back to remove any AnsibeUnsafe types
        validated_args = json.loads(json.dumps(validated_args))

        # Running asyncio coroutine to deploy everything.
        return run(self.deploy(validated_args, result))

    async def deploy(self, validated_args: dict, result: dict) -> dict:
        """Prepare data, perform deployment and convert result data."""
        logged_args = validated_args.copy()
        # Excempting the lines below from Ruff and Sonar since they think we are hardcoding a password,
        # when we are actually just being conscious about not printing passwords.
        if "cv_token" in logged_args:
            logged_args["cv_token"] = "<removed>"  # noqa: S105
        if "cv_password" in logged_args:
            logged_args["cv_password"] = "<removed>"  # NOSONAR # noqa: S105
        if "proxy_password" in logged_args:
            logged_args["proxy_password"] = "<removed>"  # NOSONAR # noqa: S105
        LOGGER.info("deploy: %s", logged_args)

        # Validate preview_features requirements before starting deployment.
        read_from_validated_inputs = get(validated_args, "preview_features.read_from_validated_inputs", False)
        tmp_dir = validated_args.get("tmp_dir")
        if read_from_validated_inputs and not tmp_dir:
            msg = "tmp_dir is required when preview_features.read_from_validated_inputs is true"
            raise AnsibleActionFail(msg)

        try:
            # Create CloudVision object
            cloudvision = CloudVision(
                servers=validated_args["cv_servers"],
                token=validated_args.get("cv_token"),
                username=validated_args.get("cv_username"),
                password=validated_args.get("cv_password"),
                verify_certs=validated_args["cv_verify_certs"],
                deploy_future=CVDeployFuture(**get(validated_args, "cv_deploy_future", default={})),
                proxy_host=validated_args.get("proxy_host"),
                proxy_port=validated_args.get("proxy_port"),
                proxy_username=validated_args.get("proxy_username"),
                proxy_password=validated_args.get("proxy_password"),
                grpc_channel_configuration=CVGRPCChannelConfiguration(grpc_keepalives=CVGRPCKeepalives(**validated_args.get("grpc_keepalives", {}))),
            )

            # If read_from_validated_inputs is enabled, we use the tmp_dir which contains validated inputs as JSON for structured_config_dir.
            if read_from_validated_inputs:
                _templated_path, validated_path = get_tmp_paths(tmp_dir)
                structured_config_dir = str(validated_path)
                structured_config_suffix = "json"
            else:
                structured_config_dir = validated_args.get("structured_config_dir")
                structured_config_suffix = validated_args.get("structured_config_suffix")

            inventory_mode = get(validated_args, "inventory_mode", default="loose")

            # Build list of CVDeviceDeployment objects (one per deployed device).
            device_deployments = await self.build_device_deployments(
                device_list=get(validated_args, "device_list", default=[]),
                structured_config_dir=structured_config_dir,
                structured_config_suffix=structured_config_suffix,
                configuration_dir=get(validated_args, "configuration_dir"),
                configlet_name_template=get(validated_args, "configlet_name_template"),
                inventory_mode=inventory_mode,
            )

            # Extract to individual list objects to maintain the same Ansible result.
            eos_config_objects, device_tag_objects, interface_tag_objects, cv_pathfinder_metadata_objects = extract_from_device_deployments(device_deployments)

            # Build Static Config Studio manifest if necessary.
            static_config_manifest = AvdManifest.from_dict(validated_args["static_config_manifest"]) if "static_config_manifest" in validated_args else None

            # Add return data if relevant.
            if validated_args["return_details"]:
                # Objects are converted to JSON compatible dicts.
                result.update(
                    cloudvision={
                        **get_result(cloudvision),
                        "token": "<removed>",
                        **({"proxy_password": "<removed>"} if cloudvision.proxy_password is not None else {}),  # NOSONAR
                    },
                    configs=[get_result(config) for config in eos_config_objects],
                    device_tags=[get_result(device_tag) for device_tag in device_tag_objects],
                    interface_tags=[get_result(interface_tag) for interface_tag in interface_tag_objects],
                    cv_pathfinder_metadata=[get_result(metadata) for metadata in cv_pathfinder_metadata_objects],
                    static_config_manifest=get_result(static_config_manifest) if static_config_manifest else None,
                )

            # Check if there is anything to deploy or decommission.
            work_to_do = any(
                [
                    eos_config_objects,
                    device_tag_objects,
                    interface_tag_objects,
                    cv_pathfinder_metadata_objects,
                    static_config_manifest,
                    # Decommission devices (contribute no configs or tags).
                    any(device_deployment.device.action == "decommission" for device_deployment in device_deployments),
                ]
            )

            if work_to_do:
                # Pre-process workspace args to convert build_warnings to AvdWorkspaceBuildWarningsConfig object.
                workspace_args = get(validated_args, "workspace", default={})
                if "build_warnings" in workspace_args:
                    workspace_args["build_warnings"] = AvdWorkspaceBuildWarningsConfig.from_dict(workspace_args["build_warnings"])

                # Perform deployment of all objects, getting a DeployToCVResult object back.
                result_object = await deploy_to_cv(
                    change_control=CVChangeControl(avd_change_control=AvdChangeControl(**get(validated_args, "change_control", default={}))),
                    cloudvision=cloudvision,
                    device_deployments=device_deployments,
                    static_config_manifest=static_config_manifest,
                    skip_missing_devices=get(validated_args, "skip_missing_devices"),
                    strict_system_mac_address=get(validated_args, "strict_system_mac_address"),
                    strict_tags=get(validated_args, "strict_tags"),
                    timeouts=CVTimeOuts(**get(validated_args, "timeouts", default={})),
                    workspace=CVWorkspace(avd_workspace=AvdWorkspace(**workspace_args)),
                )
                # Errors and warnings are converted to JSON compatible strings.
                result_object.errors = [str(error) for error in result_object.errors]
                result_object.warnings = [str(warning) for warning in result_object.warnings]

                # Add warnings caught by the logger.
                result_object.warnings.extend(result.get("warnings", []))
            else:
                result_object = DeployToCvResult(workspace=None)
                result["notes"] = ["No configurations, tags, or static config manifest found to deploy."]

            # Add either all return data or only warnings, errors, failed.
            if validated_args["return_details"]:
                # Result object is converted to JSON compatible dict.
                result.update(result_object.get_result())
            else:
                result.update(
                    {
                        "warnings": result_object.warnings,
                        "errors": result_object.errors,
                        "failed": result_object.failed,
                    },
                )

            # Set changed if we did anything. TODO: Improve this logic to only set changed if something actually changed.
            change_indicators = [
                result_object.deployed_configs,
                result_object.deployed_static_config_containers,
                result_object.deployed_static_config_configlets,
                result_object.deployed_device_tags,
                result_object.deployed_interface_tags,
                result_object.deployed_cv_pathfinder_metadata,
                result_object.removed_configs,
                result_object.removed_static_config_containers,
                result_object.removed_static_config_configlets,
                result_object.removed_device_tags,
                result_object.removed_interface_tags,
                result_object.removed_devices,
            ]
            result["changed"] = any(change_indicators)

        except Exception as error:
            # Recast errors as AnsibleActionFail
            msg = f"Error during plugin execution: {error}"
            raise_action_fail(msg, error)

        return result

    async def build_device_deployments(
        self,
        device_list: list[str],
        structured_config_dir: str | None,
        structured_config_suffix: str,
        configuration_dir: str,
        configlet_name_template: str,
        inventory_mode: Literal["loose", "controlled"] = "loose",
    ) -> list[CVDeviceDeployment]:
        """
        Build CVDeviceDeployment objects for all devices.

        Parameters:
            device_list: List of device hostnames.
            structured_config_dir: Path to structured config files.
            structured_config_suffix: Suffix for structured config files.
            configuration_dir: Path to EOS config files.
            configlet_name_template: Python string template used for naming configlets. Ex. "AVD-${hostname}"
            inventory_mode: Controls handling of devices with `is_deployed: false`. In loose mode they are silently skipped.
                In controlled mode they are included with `device.action="decommission"`.

        Return:
            List of CVDeviceDeployment objects (one per deployed device, skipping devices where is_deployed is false when inventory_mode is "loose").

        Workflow:
            Per device:
              - Read and load structured config.
              - If is_deployed is false and inventory_mode is loose then skip the device entirely.
              - If is_deployed is false and inventory_mode is controlled then build a CVDeviceDeployment with device.action="decommission".
              - Read serial_number & system_mac from structured config.
              - Create CVDevice object.
              - Read cv_use_static_config_manifest from structured config.
              - If cv_use_static_config_manifest is false, create CVEosConfig object.
              - Create tag and pathfinder metadata objects.
              - Return CVDeviceDeployment object bundling all per-device objects.
        """
        coroutines = [
            self.build_device_deployment(hostname, structured_config_dir, structured_config_suffix, configuration_dir, configlet_name_template, inventory_mode)
            for hostname in device_list
        ]
        results = await gather(*coroutines)
        return [deployment for deployment in results if deployment is not None]

    async def build_device_deployment(
        self,
        hostname: str,
        structured_config_dir: str | None,
        structured_config_suffix: str,
        configuration_dir: str,
        configlet_name_template: str,
        inventory_mode: Literal["loose", "controlled"] = "loose",
    ) -> CVDeviceDeployment | None:
        """
        Build a CVDeviceDeployment object for one device.

        Parameters:
            hostname: Device hostname.
            structured_config_dir: Path to structured config files.
            structured_config_suffix: Suffix for structured config files.
            configuration_dir: Path to EOS config files.
            configlet_name_template: Python string template used for naming configlets. Ex. "AVD-${hostname}"
            inventory_mode: Controls handling of devices with `is_deployed: false`. In loose mode such devices are silently skipped and `None`
                is returned. In controlled mode a CVDeviceDeployment with device.action="decommission" is returned.

        Returns:
            `None` when the device has `is_deployed: false` and inventory_mode is loose.
            A CVDeviceDeployment with device.action="decommission" for devices with `is_deployed: false`
            in controlled mode. A CVDeviceDeployment with device.action="deploy" otherwise.

        TODO: Refactor into smaller functions.
        """
        LOGGER.info("build_device_deployment: %s", hostname)

        structured_config = self.load_structured_config(hostname, structured_config_dir, structured_config_suffix)

        # TODO: Use CVDeploy schema class.
        # metadata.* keys take precedence over global cv_deploy schema keys.
        is_deployed = default(get(structured_config, "metadata.is_deployed"), get(structured_config, "is_deployed", default=True))

        if not is_deployed and inventory_mode == "loose":
            del structured_config
            return None

        # Build device object to be used in other objects.
        serial_number = default(get(structured_config, "metadata.serial_number"), get(structured_config, "serial_number"))
        system_mac_address = default(get(structured_config, "metadata.system_mac_address"), get(structured_config, "system_mac_address"))
        action = "deploy" if is_deployed else "decommission"
        device_object = CVDevice(
            avd_device=AvdDevice(hostname=hostname, serial_number=serial_number, system_mac_address=system_mac_address),
            action=action,
        )

        # Check if the device should use the static config manifest instead of the flat layout.
        use_static_config_manifest = default(
            get(structured_config, "metadata.cv_use_static_config_manifest"),
            get(structured_config, "cv_use_static_config_manifest", default=False),
        )

        # Build device config objects (only for devices being deployed and only if NOT opted into manifest layout).
        eos_config = None
        if is_deployed and not use_static_config_manifest:
            configlet_name = Template(configlet_name_template).substitute(hostname=hostname)
            config_file_path = str(Path(configuration_dir, f"{hostname}.cfg"))
            eos_config = CVEosConfig(file=config_file_path, device=device_object, configlet_name=configlet_name)

        # Build device tag objects for this device (deploy only — CloudVision unassociates tags automatically on decommission).
        # ! metadata:
        # !   cv_tags:
        # !     device_tags:
        # !     - name: topology_hint_datacenter
        # !       value: DC1
        device_tag_objects: list[CVDeviceTag] = []
        interface_tag_objects: list[CVInterfaceTag] = []
        if is_deployed:
            device_tags = default(get(structured_config, "metadata.cv_tags.device_tags"), get(structured_config, "cv_device_tags"), [])
            device_tag_objects = [
                CVDeviceTag(label=device_tag["name"], value=device_tag["value"], device=device_object)
                for device_tag in device_tags
                if "name" in device_tag and "value" in device_tag
            ]

            # Build interface tag objects for this device.
            # ! metadata:
            # !  cv_tags:
            # !    interface_tags:
            # !    - interface: Ethernet3
            # !      tags:
            # !      - name: peer_device_interface
            # !        value: Ethernet3
            all_interface_tags = default(get(structured_config, "metadata.cv_tags.interface_tags"), get(structured_config, "cv_interface_tags"), [])
            interface_tag_objects = [
                CVInterfaceTag(
                    label=interface_tag["name"],
                    value=interface_tag["value"],
                    device=device_object,
                    interface=one_interface_tags["interface"],
                )
                for one_interface_tags in all_interface_tags
                if "interface" in one_interface_tags and "tags" in one_interface_tags
                for interface_tag in one_interface_tags["tags"]
                if "name" in interface_tag and "value" in interface_tag
            ]

        # Build WAN metadata object for this device (only if device is being deployed).
        # TODO: Implement pathfinder metadata cleanup for decommission devices.
        cv_pathfinder_metadata_object = None
        if (
            is_deployed
            and (cv_pathfinder_metadata := default(get(structured_config, "metadata.cv_pathfinder"), get(structured_config, "cv_pathfinder_metadata")))
            is not None
        ):
            cv_pathfinder_metadata_object = CVPathfinderMetadata(metadata=cv_pathfinder_metadata, device=device_object)

        del structured_config
        return CVDeviceDeployment(
            device=device_object,
            use_static_config_manifest=use_static_config_manifest,
            eos_config=eos_config,
            device_tags=device_tag_objects,
            interface_tags=interface_tag_objects,
            cv_pathfinder_metadata=cv_pathfinder_metadata_object,
        )

    def load_structured_config(self, hostname: str, structured_config_dir: str | None, structured_config_suffix: str) -> dict[str, Any]:
        """
        Load the structured config for the host.

        Args:
            hostname: Inventory hostname.
            structured_config_dir: Path to structured config files.
            structured_config_suffix: Suffix for structured config files.

        Returns:
            Dict containing the structured config for the host.
        """
        if not structured_config_dir or not (file_path := Path(structured_config_dir, f"{hostname}.{structured_config_suffix}")).exists():
            LOGGER.info("load_structured_config: No structured config file for %s", hostname)
            return {}

        if structured_config_suffix in ["yml", "yaml"]:
            with file_path.open(mode="r", encoding="UTF-8") as structured_config_stream:
                metadata_lines = []
                in_metadata = False
                for line in structured_config_stream:
                    if line.startswith("metadata"):
                        in_metadata = True
                    elif in_metadata and not line.startswith(" "):
                        break
                    if in_metadata:
                        metadata_lines.append(line)

                return load("".join(metadata_lines), Loader=YamlLoader) or {}  # noqa: S506 TODO: Consider safeload

        # JSON files may be encrypted by the validate_inputs plugin, so we use AVDFileHandler to decrypt if needed.
        vault_handler = AVDVaultHandler(self._loader)
        file_handler = AVDFileHandler(vault_handler)
        return file_handler.load_json(file_path)


def setup_module_logging(result: dict) -> None:
    """
    Add a Handler to copy the logs from the plugin into Ansible output based on their level.

    Parameters:
        result: The dictionary used for the ansible module results
    """
    python_to_ansible_handler = PythonToAnsibleHandler(result, display)

    # Modifying the root logger to also cover pyavd.
    root_logger = logging.getLogger()
    root_logger.addHandler(python_to_ansible_handler)
    if display.verbosity >= 3:
        root_logger.setLevel(logging.DEBUG)
    elif display.verbosity >= 1:
        root_logger.setLevel(logging.INFO)
