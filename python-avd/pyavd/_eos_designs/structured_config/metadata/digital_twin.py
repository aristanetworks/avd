# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._errors import AristaAvdError
from pyavd._utils import default

if TYPE_CHECKING:
    from . import AvdStructuredConfigMetadataProtocol


class DigitalTwinMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    def _set_digital_twin(self: AvdStructuredConfigMetadataProtocol) -> None:
        """
        Set the metadata for Digital Twin feature.

        Only relevant to the use cases where generation of the Digital Twin infrastructure is globally enabled.
        """
        environment = self.inputs.digital_twin.environment
        match environment:
            case "act":
                digital_twin_node_type = self.shared_utils.platform_settings.digital_twin.act_node_type
                if not (isinstance(digital_twin_node_type, str) and digital_twin_node_type):
                    msg = (
                        f"Failed to generate ACT Digital Twin metadata for device '{self.shared_utils.hostname}' using platform '{self.shared_utils.platform}'."
                        f" 'digital_twin.{environment}_node_type' key is missing in platform settings."
                    )
                    raise AristaAvdError(msg)

                ip_addr = default(self.shared_utils.node_config.digital_twin.mgmt_ip, self.shared_utils.node_config.mgmt_ip)
                # TODO: Adjust once dynamic pool-based IP allocation is implemented.
                if not (isinstance(ip_addr, str) and ip_addr):
                    msg = (
                        f"Failed to generate ACT Digital Twin metadata for device '{self.shared_utils.hostname}'."
                        " 'mgmt_ip' attribute must be set in the node configuration settings using either the 'digital_twin.mgmt_ip' or 'mgmt_ip' key."
                    )
                    raise AristaAvdError(msg)

                # Identify default os_version, username and password based on the matched ACT node type
                match digital_twin_node_type:
                    case "cloudeos":
                        default_os_version_for_node_type = self.inputs.digital_twin.act_cloudeos_os_version
                        username = self.inputs.digital_twin.act_cloudeos_username
                        password = self.inputs.digital_twin.act_cloudeos_password
                    case "third-party":
                        default_os_version_for_node_type = self.inputs.digital_twin.act_third_party_os_version
                        username = self.inputs.digital_twin.act_third_party_username
                        password = self.inputs.digital_twin.act_third_party_password
                    case "veos":
                        default_os_version_for_node_type = self.inputs.digital_twin.act_veos_os_version
                        username = self.inputs.digital_twin.act_veos_username
                        password = self.inputs.digital_twin.act_veos_password

                version = default(self.shared_utils.node_config.digital_twin.act_os_version, default_os_version_for_node_type)

                self.structured_config.metadata.digital_twin._update(
                    environment=environment,
                    node_type=digital_twin_node_type,
                    # TODO: How-to guide explaining ip_addr requirements and limitations for each Digital Twin environment.
                    ip_addr=ip_addr,
                    version=version,
                    username=username,
                    password=password,
                )
                # Set internet_access flag if node_type is cloudeos or veos
                if (
                    act_internet_access := default(
                        self.shared_utils.node_config.digital_twin.act_internet_access,
                        self.inputs.digital_twin.act_internet_access,
                    )
                ) and digital_twin_node_type in ["cloudeos", "veos"]:
                    self.structured_config.metadata.digital_twin._update(
                        internet_access=act_internet_access,
                    )
                return
