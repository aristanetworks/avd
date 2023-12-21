# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import absolute_import, annotations, division, print_function

__metaclass__ = type

import logging
from asyncio import gather, run
from dataclasses import asdict
from pathlib import Path
from string import Template

from ansible.errors import AnsibleActionFail
from ansible.plugins.action import ActionBase, display
from yaml import CLoader, load

from ansible_collections.arista.avd.plugins.plugin_utils.cv_client import deploy_to_cv
from ansible_collections.arista.avd.plugins.plugin_utils.cv_client.deploy_to_cv.models import (
    CloudVision,
    CVChangeControl,
    CVDevice,
    CVDeviceTag,
    CVEosConfig,
    CVInterfaceTag,
    CVTimeOuts,
    CVWorkspace,
)
from ansible_collections.arista.avd.plugins.plugin_utils.strip_empties import strip_null_from_data
from ansible_collections.arista.avd.plugins.plugin_utils.utils import PythonToAnsibleHandler, get

LOGGER = logging.getLogger("ansible_collections.arista.avd")
LOGGING_LEVELS = ["DEBUG", "INFO", "ERROR", "WARNING", "CRITICAL"]


ARGUMENT_SPEC = dict(
    configuration_dir=dict(type="str", required=True),
    structured_config_dir=dict(type="str", required=True),
    structured_config_suffix=dict(type="str", default="yml"),
    device_list=dict(type="list", elements="str", required=True),
    strict_tags=dict(type="bool", required=False, default=False),
    skip_missing_devices=dict(type="bool", required=False, default=False),
    configlet_name_template=dict(type="str", default="AVD-${hostname}"),
    cloudvision=dict(
        type="dict",
        required=True,
        options=dict(
            servers=dict(type="list", elements="str", required=True),
            token=dict(type="str", secret=True, required=True),
            verify_certs=dict(type="bool", default=True),
        ),
    ),
    workspace=dict(
        type="dict",
        options=dict(
            name=dict(type="str", required=False),
            description=dict(type="str", required=False),
            id=dict(type="str", required=False),
            # TODO: Change default to submitted
            requested_state=dict(type="str", default="built", choices=["pending", "built", "submitted", "abandoned", "deleted"]),
        ),
    ),
    change_control=dict(
        type="dict",
        options=dict(
            name=dict(type="str", required=False),
            description=dict(type="str", required=False),
            # TODO: Add deleted once it is supported.
            requested_state=dict(type="str", default="pending approval", choices=["pending approval", "approved", "running", "completed"]),
        ),
    ),
    timeouts=dict(
        type="dict",
        options=dict(
            workspace_build_timeout=dict(type="float", default=CVTimeOuts.workspace_build_timeout),
            change_control_creation_timeout=dict(type="float", default=CVTimeOuts.change_control_creation_timeout),
        ),
    ),
)


class ActionModule(ActionBase):
    def run(self, tmp=None, task_vars=None):
        self._supports_check_mode = True

        if task_vars is None:
            task_vars = {}

        result = super().run(tmp, task_vars)
        del tmp  # tmp no longer has any effect

        # Setup module logging
        setup_module_logging(result)

        # Get task arguments and validate them
        validation_result, validated_args = self.validate_argument_spec(ARGUMENT_SPEC)
        validated_args = strip_null_from_data(validated_args)
        return run(self.deploy(validated_args, result))

    async def deploy(self, validated_args: dict, result: dict):
        LOGGER.info("deploy: %s", validated_args)
        try:
            cloudvision = CloudVision(**get(validated_args, "cloudvision", default={}))
            eos_config_objects, device_tag_objects, interface_tag_objects = await self.build_objects(
                device_list=get(validated_args, "device_list"),
                structured_config_dir=get(validated_args, "structured_config_dir"),
                structured_config_suffix=get(validated_args, "structured_config_suffix"),
                configuration_dir=get(validated_args, "configuration_dir"),
                configlet_name_template=get(validated_args, "configlet_name_template"),
            )
            result.update(
                cloudvision=dict(asdict(cloudvision), token="<removed>"),
                configs=[asdict(config) for config in eos_config_objects],
                device_tags=[asdict(device_tag) for device_tag in device_tag_objects],
                interface_tags=[asdict(interface_tag) for interface_tag in interface_tag_objects],
            )
            result_object = await deploy_to_cv(
                change_control=CVChangeControl(**get(validated_args, "change_control", default={})),
                cloudvision=cloudvision,
                configs=eos_config_objects,
                device_tags=device_tag_objects,
                interface_tags=interface_tag_objects,
                skip_missing_devices=get(validated_args, "skip_missing_devices"),
                strict_tags=get(validated_args, "strict_tags"),
                timeouts=CVTimeOuts(**get(validated_args, "timeouts", default={})),
                workspace=CVWorkspace(**get(validated_args, "workspace", default={})),
            )

            result_object.errors = [str(error) for error in result_object.errors]
            result_object.warnings = [str(warning) for warning in result_object.warnings]
            result.update(asdict(result_object))
        except Exception as error:
            msg = f"Error during plugin execution: {error}"
            raise AnsibleActionFail(msg) from error

        return result

    async def build_objects(
        self, device_list: list[str], structured_config_dir: str, structured_config_suffix: str, configuration_dir: str, configlet_name_template: str
    ) -> (list[CVEosConfig], list[CVDeviceTag], list[CVInterfaceTag]):
        """
        Parameters:
            device_list: List of device hostnames.
            structured_config_dir: Path to structured config files.
            structured_config_suffix: Suffix for structured config files.
        Return:
            Tuple containing (<EOS Configs to deploy>, <Device Tags to deploy>, <Interface Tags to deploy>)

        Workflow:
            Per device:
              - Read and load structured config
              - If is_deployed is false, skip the device.
              - Read serial_number & system_mac from structured config.
              - Create CVDevice object and add to list of device_objects.
        """
        coroutines = [
            self.build_object_for_device(hostname, structured_config_dir, structured_config_suffix, configuration_dir, configlet_name_template)
            for hostname in device_list
        ]
        tuples = await gather(*coroutines)

        eos_config_objects = []
        device_tag_objects = []
        interface_tag_objects = []
        for device_eos_config_objects, device_device_tag_objects, device_interface_tag_objects in tuples:
            eos_config_objects.extend(device_eos_config_objects)
            device_tag_objects.extend(device_device_tag_objects)
            interface_tag_objects.extend(device_interface_tag_objects)
        return eos_config_objects, device_tag_objects, interface_tag_objects

    async def build_object_for_device(
        self, hostname: str, structured_config_dir: str, structured_config_suffix: str, configuration_dir: str, configlet_name_template: str
    ) -> (list[CVEosConfig], list[CVDeviceTag], list[CVInterfaceTag]):
        """
        Parameters:
            device_list: List of device hostnames.
            structured_config_dir: Path to structured config files.
            structured_config_suffix: Suffix for structured config files.
        Return:
            Tuple containing (<EOS Configs to deploy>, <Device Tags to deploy>, <Interface Tags to deploy>)

        Workflow:
            Per device:
              - Read and load structured config
              - If is_deployed is false, skip the device.
              - Read serial_number & system_mac from structured config.
              - Create CVDevice object and add to list of device_objects.
        """
        LOGGER.info("build_object_for_device: %s", hostname)
        with Path(structured_config_dir, f"{hostname}.{structured_config_suffix}").open(mode="r", encoding="UTF-8") as structured_config_stream:
            interesting_keys = ("is_deployed", "serial_number", "metadata")
            in_interesting_context = False
            structured_config_lines = []
            for line in structured_config_stream.readlines():
                if line.startswith(interesting_keys) or (in_interesting_context and line.startswith(" ")):
                    structured_config_lines.append(line)
                    in_interesting_context = True
                else:
                    in_interesting_context = False

            structured_config = load("".join(structured_config_lines), Loader=CLoader)

        if not get(structured_config, "is_deployed", default=True):
            del structured_config
            return ([], [], [])

        # Build device object to be used in other objects.
        serial_number = get(structured_config, "serial_number")
        system_mac_address = get(structured_config, "metadata.system_mac_address")
        device_object = CVDevice(hostname=hostname, serial_number=serial_number, system_mac_address=system_mac_address)

        # Build device config objects
        configlet_name = Template(configlet_name_template).substitute(hostname=hostname)
        config_file_path = str(Path(configuration_dir, f"{hostname}.cfg"))
        eos_config_objects = [CVEosConfig(file=config_file_path, device=device_object, configlet_name=configlet_name)]

        # Build device tag objects for this device.
        # metadata:
        #   cv_device_tags:
        #   - name: topology_hint_datacenter
        #     value: DC1
        device_tags = get(structured_config, "metadata.cv_device_tags", default=[])
        device_tag_objects = [
            CVDeviceTag(label=device_tag["name"], value=device_tag["value"], device=device_object)
            for device_tag in device_tags
            if "name" in device_tag and "value" in device_tag
        ]

        # Build interface tag objects for this device.
        # metadata:
        #   cv_interface_tags:
        #   - interface: Ethernet3
        #     tags:
        #     - name: peer_device_interface
        #       value: Ethernet3
        all_interface_tags = get(structured_config, "metadata.cv_interface_tags", default=[])
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

        del structured_config
        return eos_config_objects, device_tag_objects, interface_tag_objects


def setup_module_logging(result: dict) -> None:
    """
    Add a Handler to copy the logs from the plugin into Ansible output based on their level

    Parameters:
        result: The dictionary used for the ansible module results
    """
    python_to_ansible_handler = PythonToAnsibleHandler(result, display)
    LOGGER.addHandler(python_to_ansible_handler)
    # TODO mechanism to manipulate the logger globally for pyavd
    # Keep debug to be able to see logs with `-v` and `-vvv`
    LOGGER.setLevel(logging.DEBUG)
