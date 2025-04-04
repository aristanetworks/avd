# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import re
from ipaddress import AddressValueError, IPv4Address, ip_network
from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from . import AvdStructuredConfigUnderlayProtocol

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
        self._update_subnets(dhcp_server)
        if len(dhcp_server.subnets) == 0:
            return
        dhcp_server.vrf = "default"
        # Set ZTP bootfile
        self._update_ipv4_ztp_boot_file(dhcp_server)
        # Set DNS servers
        if dns_servers := self.inputs.name_servers:
            dhcp_server.dns_servers_ipv4 = dns_servers._cast_as(EosCliConfigGen.DhcpServersItem.DnsServersIpv4)
        # Set NTP servers
        self._update_ntp_servers(dhcp_server)

        self.structured_config.dhcp_servers.append(dhcp_server)

    def _update_subnets(self: AvdStructuredConfigUnderlayProtocol, dhcp_server: EosCliConfigGen.DhcpServersItem) -> None:
        """
        Update dhcp_server with a list of dhcp subnets for downstream p2p interfaces.

        Used for l3 inband ztp/ztr.
        """
        for peer in self._avd_peers:
            peer_facts = self.shared_utils.get_peer_facts(peer)
            for uplink in peer_facts.uplinks:
                if (
                    uplink.peer == self.shared_utils.hostname
                    and uplink.type == "underlay_p2p"
                    and uplink.ip_address
                    and "unnumbered" not in uplink.ip_address
                    and peer_facts.inband_ztp
                ):
                    subnet_item = EosCliConfigGen.DhcpServersItem.SubnetsItem(
                        subnet=str(ip_network(f"{uplink.peer_ip_address}/{uplink.prefix_length}", strict=False)),
                        name=f"inband ztp for {peer}-{uplink.interface}",
                        default_gateway=f"{uplink.peer_ip_address}",
                    )
                    subnet_item.ranges.append_new(start=str(uplink.ip_address), end=str(uplink.ip_address))
                    dhcp_server.subnets.append(subnet_item)

    def _update_ipv4_ztp_boot_file(self: AvdStructuredConfigUnderlayProtocol, dhcp_server: EosCliConfigGen.DhcpServersItem) -> None:
        """Update the file name to allow for ZTP to CV."""
        if self.inputs.inband_ztp_bootstrap_file:
            dhcp_server.tftp_server.file_ipv4 = self.inputs.inband_ztp_bootstrap_file
            return
        if not (cvp_instance_ips := self.inputs.cvp_instance_ips):
            return

        if "arista.io" in cvp_instance_ips[0]:
            clean_cvaas_fqdn = re.sub(r"https:\/\/|www\.|apiserver\.", "", cvp_instance_ips[0])
            cvp_instance_ips[0] = f"www.{clean_cvaas_fqdn}"

        dhcp_server.tftp_server.file_ipv4 = f"https://{cvp_instance_ips[0]}/ztp/bootstrap"

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
