# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from pyavd._errors import AristaAvdError
from pyavd._utils import get, strip_null_from_data

from .utils import UtilsMixin

if TYPE_CHECKING:
    from . import AvdStructuredConfigBase


class NtpMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def ntp(self: AvdStructuredConfigBase) -> dict | None:
        """Ntp set based on "ntp_settings" data-model."""
        ntp_settings = get(self._hostvars, "ntp_settings")
        if not ntp_settings:
            return None

        # Since the eos_cli_config_gen data model almost matches, we can copy most data directly.
        ntp = strip_null_from_data(
            {
                "authenticate": ntp_settings.get("authenticate"),
                "authenticate_servers_only": ntp_settings.get("authenticate_servers_only"),
                "authentication_keys": ntp_settings.get("authentication_keys"),
                "trusted_keys": ntp_settings.get("trusted_keys"),
            },
        )

        if "servers" not in ntp_settings:
            # Quick return if we have no servers.
            return ntp or None

        # Get server_vrf from ntp_settings and configure with the relevant VRF.
        # Also set relevant local interface.
        server_vrf = get(ntp_settings, "server_vrf")
        if server_vrf is None:
            server_vrf = self.shared_utils.default_mgmt_protocol_vrf
            ntp["local_interface"] = {
                "name": self.shared_utils.default_mgmt_protocol_interface,
                "vrf": server_vrf,
            }

        if server_vrf == "use_mgmt_interface_vrf":
            has_mgmt_ip = (self.shared_utils.mgmt_ip is not None) or (self.shared_utils.ipv6_mgmt_ip is not None)
            if not has_mgmt_ip:
                msg = "'ntp_settings.server_vrf' is set to 'use_mgmt_interface_vrf' but this node is missing an 'mgmt_ip'"
                raise AristaAvdError(msg)
            # Replacing server_vrf with mgmt_interface_vrf
            server_vrf = self.shared_utils.mgmt_interface_vrf
            ntp["local_interface"] = {
                "name": self.shared_utils.mgmt_interface,
                "vrf": server_vrf,
            }
        elif server_vrf == "use_inband_mgmt_vrf":
            if self.shared_utils.inband_mgmt_interface is None:
                msg = "'ntp_settings.server_vrf' is set to 'use_inband_mgmt_vrf' but this node is missing configuration for inband management"
                raise AristaAvdError(msg)
            # self.shared_utils.inband_mgmt_vrf returns None for the default VRF.
            # Replacing server_vrf with inband_mgmt_vrf or "default"
            server_vrf = self.shared_utils.inband_mgmt_vrf or "default"
            ntp["local_interface"] = {
                "name": self.shared_utils.inband_mgmt_interface,
                "vrf": server_vrf,
            }

        ntp["servers"] = []
        # First server is set with preferred
        first = True
        for server in ntp_settings["servers"]:
            ntp["servers"].append({**server, "vrf": server_vrf})
            if first:
                ntp["servers"][-1]["preferred"] = True
                first = False

        return ntp
