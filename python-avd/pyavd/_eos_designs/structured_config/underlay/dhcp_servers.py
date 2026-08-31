# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import re
from ipaddress import AddressValueError, IPv4Address
from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from . import AvdStructuredConfigUnderlayProtocol

from pyavd._cv.constants import CV_REGION_TO_SERVER_MAP, CVAAS_API_PREFIX
from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor
from pyavd._errors import AristaAvdInvalidInputsError


class DhcpServersMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @structured_config_contributor
    def dhcp_servers(self: AvdStructuredConfigUnderlayProtocol) -> None:
        """Set structured config for dhcp_server."""
        dhcp_server = EosCliConfigGen.DhcpServersItem()
        # Set subnets for DHCP server
        dhcp_server.ipv4_subnets = self._underlay_subnets[1]
        if len(dhcp_server.ipv4_subnets) == 0:
            return
        dhcp_server.vrf = "default"
        # Set ZTP bootfile
        self._update_ipv4_ztp_boot_file(dhcp_server)
        # Set DNS servers
        # TODO: Figure out if / how we should filter on VRFs. Currently just adding all servers.
        if dns_servers := self.inputs.dns_settings.servers:
            for dns_server in dns_servers:
                dhcp_server.dns_servers_ipv4.append(dns_server.ip_address)
        # Set NTP servers
        self._update_ntp_servers(dhcp_server)

        self.structured_config.dhcp_servers.append(dhcp_server)

    def _get_cvp_server_for_dhcp(self: AvdStructuredConfigUnderlayProtocol) -> str | None:
        """Return the first CVP server using either new or old data models."""
        if self.inputs.cv_settings.cvaas.enabled:
            region = next(iter(self.inputs.cv_settings.cvaas.clusters)).region
            return f"{CVAAS_API_PREFIX}.{CV_REGION_TO_SERVER_MAP[region]}"

        if self.inputs.cv_settings.onprem_clusters:
            return next(iter(next(iter(self.inputs.cv_settings.onprem_clusters)).servers)).name

        return None

    def _update_ipv4_ztp_boot_file(self: AvdStructuredConfigUnderlayProtocol, dhcp_server: EosCliConfigGen.DhcpServersItem) -> None:
        """Update the file name to allow for ZTP to CV."""
        if self.inputs.inband_ztp_bootstrap_file:
            dhcp_server.tftp_server.file_ipv4 = self.inputs.inband_ztp_bootstrap_file
            return
        if not (cvp_server := self._get_cvp_server_for_dhcp()):
            return

        if "arista.io" in cvp_server:
            # Change apiserver.<...>arista.io to www.<...>arista.io
            domain = re.sub(r"https:\/\/|www\.|apiserver\.", "", cvp_server)
            cvp_server = f"www.{domain}"

        dhcp_server.tftp_server.file_ipv4 = f"https://{cvp_server}/ztp/bootstrap"

    def _update_ntp_servers(self: AvdStructuredConfigUnderlayProtocol, dhcp_server: EosCliConfigGen.DhcpServersItem) -> None:
        """Set list of NTP servers."""
        ntp_servers_settings = self.inputs.ntp_settings.servers
        if not ntp_servers_settings:
            return

        ntp_servers = EosCliConfigGen.DhcpServersItem.Ipv4VendorOptionsItem.SubOptionsItem.ArrayIpv4Address()
        for ntp_server in ntp_servers_settings:
            # Check and validate NTP server IP address
            try:
                ntp_server_ip = IPv4Address(ntp_server.name)
            except AddressValueError:
                continue
            ntp_servers.append(str(ntp_server_ip))

        if not ntp_servers:
            msg = "When in-band ZTP is enabled, at least one NTP server's `name` field provided under `ntp_settings.servers` must be a valid IPv4 address."
            raise AristaAvdInvalidInputsError(msg)

        suboptions = EosCliConfigGen.DhcpServersItem.Ipv4VendorOptionsItem.SubOptions()
        suboptions.append_new(code=42, array_ipv4_address=ntp_servers)
        dhcp_server.ipv4_vendor_options.append_new(
            vendor_id="NTP",
            sub_options=suboptions,
        )
