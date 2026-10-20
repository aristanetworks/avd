# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING, Protocol

from pyavd._eos_designs.digital_twin import ActNodeTypeFeature, act_node_type_supports_feature
from pyavd._errors import AristaAvdInvalidInputsError
from pyavd._utils.default import default
from pyavd._utils.format_string import AvdStringFormatter
from pyavd._utils.strip_empties import strip_null_from_data

if TYPE_CHECKING:
    from . import StructuredConfigUtilsProtocol

_SUPPORTED_DIGITAL_TWIN_HARDWARE_IDENTITY_TEMPLATE_FIELDS = ("serial_number", "system_mac_address", "hostname", "device_id", "fabric_name")


class DigitalTwinMixin(Protocol):
    """Utilities shared by Digital Twin structured-config contributors."""

    def current_act_node_supports_feature(self: StructuredConfigUtilsProtocol, feature: ActNodeTypeFeature) -> bool:
        """Return whether the selected ACT node type supports the feature."""
        if not self.shared_utils.is_act_digital_twin:
            return False
        return act_node_type_supports_feature(self.shared_utils.platform_settings.digital_twin.act_node_type, feature)

    @cached_property
    def digital_twin_hardware_identity_template_vars(self: StructuredConfigUtilsProtocol) -> dict:
        """Return the production identity and device attributes available to Digital Twin identity templates."""
        return strip_null_from_data(
            {
                "serial_number": self.shared_utils.serial_number,
                "system_mac_address": self.production_system_mac_address,
                "hostname": self.shared_utils.hostname,
                "device_id": self.shared_utils.id,
                "fabric_name": self.shared_utils.fabric_name,
            }
        )

    def render_digital_twin_hardware_identity_template(self: StructuredConfigUtilsProtocol, template: str, setting_path: str) -> str:
        """Render AVD string formatter Digital Twin identity templates."""
        try:
            return AvdStringFormatter().format(template, **self.digital_twin_hardware_identity_template_vars)
        except KeyError as error:
            field_name = error.args[0]
            if field_name in _SUPPORTED_DIGITAL_TWIN_HARDWARE_IDENTITY_TEMPLATE_FIELDS:
                msg = (
                    f"'{setting_path}' uses template variable '{field_name}' which is not configured for device '{self.shared_utils.hostname}'. "
                    "Ensure the device has this value set."
                )
            else:
                supported_fields = ", ".join(repr(field) for field in _SUPPORTED_DIGITAL_TWIN_HARDWARE_IDENTITY_TEMPLATE_FIELDS)
                msg = f"'{setting_path}' uses unsupported template variable '{field_name}'. Supported template variables are: {supported_fields}."
            raise AristaAvdInvalidInputsError(msg, host=self.shared_utils.hostname) from error

    @cached_property
    def digital_twin_serial_number(self: StructuredConfigUtilsProtocol) -> str | None:
        """Return the rendered Digital Twin serial number, or None if not configured."""
        node_serial_number = self.shared_utils.node_config.digital_twin.serial_number
        fabric_serial_number = self.inputs.digital_twin.fabric.serial_number
        serial_number_template = default(node_serial_number, fabric_serial_number)
        if serial_number_template is None:
            return None

        setting_path = "node_config.digital_twin.serial_number" if node_serial_number is not None else "digital_twin.fabric.serial_number"
        serial_number = self.render_digital_twin_hardware_identity_template(serial_number_template, setting_path)
        if not serial_number:
            msg = f"'{setting_path}' rendered an empty serial number for device '{self.shared_utils.hostname}'."
            raise AristaAvdInvalidInputsError(msg, host=self.shared_utils.hostname)
        return serial_number

    @cached_property
    def act_digital_twin_serial_number(self: StructuredConfigUtilsProtocol) -> str | None:
        """Return the Digital Twin serial number when supported by the selected ACT node type."""
        if not self.current_act_node_supports_feature("serial_number"):
            return None
        return self.digital_twin_serial_number

    @cached_property
    def metadata_serial_number(self: StructuredConfigUtilsProtocol) -> str | None:
        """Return the serial number appropriate for metadata in the current Digital Twin environment."""
        if not self.shared_utils.digital_twin:
            return self.shared_utils.serial_number

        match self.inputs.digital_twin.environment:
            case "act":
                return self.act_digital_twin_serial_number
            case _:
                # Containerlab currently retains the production serial number.
                return self.shared_utils.serial_number

    @cached_property
    def metadata_system_mac_address(self: StructuredConfigUtilsProtocol) -> str | None:
        """Return the system MAC appropriate for metadata in the current Digital Twin environment."""
        if not self.shared_utils.digital_twin:
            return self.system_mac_address

        match self.inputs.digital_twin.environment:
            case "act":
                return self.act_digital_twin_system_mac_address
            case _:
                # Containerlab currently retains the production system MAC.
                return self.system_mac_address
