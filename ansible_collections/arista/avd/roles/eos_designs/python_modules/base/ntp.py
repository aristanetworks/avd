# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get

from .utils import UtilsMixin


class NtpMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    @cached_property
    def ntp(self) -> dict | None:
        """
        ntp set based on "ntp_settings" data-model.
        """
        ntp_settings = get(self._hostvars, "ntp_settings")

        if not ntp_settings:
            return None

        # Since the eos_cli_config_gen data model almost matches, we can copy most data directly.
        # Below we pop the server_vrf option and insert local_interface and vrf for each server
        ntp = {**ntp_settings}
        ntp.pop("server_vrf", None)

        if "servers" not in ntp:
            # Quick return if we have no servers.
            return ntp or None

        # Get server_vrf from the original settings and replace with relevant VRF.
        # Notice "server_vrf" is only required if "servers" is set.
        # Also set relevant local interface.
        server_vrf = get(ntp_settings, "server_vrf", required=True)
        if server_vrf == "use_mgmt_interface_vrf":
            has_mgmt_ip = (self.shared_utils.mgmt_ip is not None) or (self.shared_utils.ipv6_mgmt_ip is not None)
            if not has_mgmt_ip:
                raise AristaAvdError("'ntp_settings.server_vrf' is set to 'use_mgmt_interface_vrf' but this node is missing an 'mgmt_ip'")
            # Replacing server_vrf with mgmt_interface_vrf
            server_vrf = self.shared_utils.mgmt_interface_vrf
            ntp["local_interface"] = {
                "name": self.shared_utils.mgmt_interface,
                "vrf": self.shared_utils.mgmt_interface_vrf,
            }
        elif server_vrf == "use_inband_mgmt_vrf":
            if self.shared_utils.inband_mgmt_interface is None:
                raise AristaAvdError("'ntp_settings.server_vrf' is set to 'use_inband_mgmt_vrf' but this node is missing configuration for inband management")
            # self.shared_utils.inband_mgmt_vrf returns None for the default VRF.
            # Replacing server_vrf with inband_mgmt_vrf or "default"
            server_vrf = self.shared_utils.inband_mgmt_vrf or "default"
            ntp["local_interface"] = {
                "name": self.shared_utils.inband_mgmt_interface,
                "vrf": self.shared_utils.inband_mgmt_vrf or "default",
            }

        # First server is set with preferred
        first = True
        for server in ntp["servers"]:
            server["vrf"] = server_vrf
            if first:
                server["preferred"] = True
                first = False

        return ntp or None
