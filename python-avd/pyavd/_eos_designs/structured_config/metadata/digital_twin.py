# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar, Protocol

from pyavd._errors import AristaAvdError
from pyavd._utils.default import default
from pyavd._utils.get import get

if TYPE_CHECKING:
    from . import AvdStructuredConfigMetadataProtocol

# Node types for which ip_addr ACT attribute is optional. For all other node types it is mandatory
_ACT_NODE_TYPES_OPTIONAL_MGMT_IP: frozenset[str] = frozenset({"cloudeos", "veos"})


class DigitalTwinMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    DEFAULT_OS_VERSION_MAP: ClassVar[dict[str, dict[str, str]]] = {
        "act": {
            "cloudeos": "4.33.2F",
            "cvp": "2024.3.2",
            "generic": "ubuntu-2204-lts",
            "third-party": "byod",
            "tools-server": "ubuntu-2204-lts",
            "veos": "4.33.1.1F",
        },
    }

    def _set_digital_twin(self: AvdStructuredConfigMetadataProtocol) -> None:
        """
        Set the metadata for Digital Twin feature.

        Only relevant to the use cases where generation of the Digital Twin infrastructure is globally enabled.
        """
        environment = self.inputs.digital_twin.environment
        match environment:
            case "act":
                digital_twin_node_type = self.shared_utils.platform_settings.digital_twin.act_node_type
                node_config_digital_twin = self.shared_utils.node_config.digital_twin
                if not (isinstance(digital_twin_node_type, str) and digital_twin_node_type):
                    msg = (
                        f"Failed to generate ACT Digital Twin metadata for device '{self.shared_utils.hostname}' using platform '{self.shared_utils.platform}'."
                        f" 'digital_twin.{environment}_node_type' key is missing in platform settings."
                    )
                    raise AristaAvdError(msg)
                ip_addr = default(node_config_digital_twin.mgmt_ip, self.shared_utils.node_config.mgmt_ip)
                if not ip_addr and digital_twin_node_type not in _ACT_NODE_TYPES_OPTIONAL_MGMT_IP:
                    msg = (
                        f"Failed to generate ACT Digital Twin metadata for device '{self.shared_utils.hostname}'."
                        " 'mgmt_ip' attribute must be set in the node configuration settings using either the 'digital_twin.mgmt_ip' or 'mgmt_ip' key."
                    )
                    raise AristaAvdError(msg)
                if ip_addr == "dhcp":
                    msg = (
                        f"'mgmt_ip: dhcp' is not supported for Digital Twin. "
                        f"A static management IP address is required for host '{self.shared_utils.hostname}'."
                    )
                    raise AristaAvdError(msg)
                version = default(
                    node_config_digital_twin.act_os_version,
                    self.inputs.digital_twin.fabric.act_os_version,
                    get(self.DEFAULT_OS_VERSION_MAP, f"act..{digital_twin_node_type}", separator=".."),
                )
                username = self.inputs.digital_twin.fabric.act_username
                password = self.inputs.digital_twin.fabric.act_password
                self.structured_config.metadata.digital_twin._update(
                    environment=environment,
                    node_type=digital_twin_node_type,
                    ip_addr=ip_addr,
                    version=version,
                    username=username,
                    password=password,
                )
                if self.structured_config_utils.current_act_node_supports_feature("internet_access") and (
                    act_internet_access := default(
                        self.shared_utils.node_config.digital_twin.act_internet_access,
                        self.inputs.digital_twin.fabric.act_internet_access,
                    )
                ):
                    self.structured_config.metadata.digital_twin._update(internet_access=act_internet_access)

                # ACT treats an omitted ztp key as disabled, so only write the key when ZTP is enabled
                if self.structured_config_utils.current_act_node_supports_feature("ztp") and (
                    ztp := default(node_config_digital_twin.ztp, self.inputs.digital_twin.fabric.ztp)
                ):
                    self.structured_config.metadata.digital_twin._update(ztp=ztp)
                return
            case "containerlab":
                self.structured_config.metadata.digital_twin._update(environment=environment)
