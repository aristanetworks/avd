# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from ipaddress import AddressValueError, IPv4Address, ip_network

from ...._utils import get
from .utils import UtilsMixin


class DhcpServerMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    _hostvars: dict

    @cached_property
    def _subnets(self) -> list:
        """
        Returns a list of dhcp subnets for downstream p2p interfaces

        Used for l3 inband ztp/ztr
        """
        subnets = []
        for peer in self._avd_peers:
            peer_facts = self.shared_utils.get_peer_facts(peer, required=True)
            for uplink in peer_facts["uplinks"]:
                if (
                    uplink["peer"] == self.shared_utils.hostname
                    and uplink["type"] == "underlay_p2p"
                    and uplink.get("ip_address")
                    and "unnumbered" not in uplink["ip_address"]
                    and get(peer_facts, "inband_ztp")
                ):
                    subnet = {
                        "subnet": str(ip_network(f"{uplink['peer_ip_address']}/{uplink['prefix_length']}", strict=False)),
                        "ranges": [{"start": str(uplink["ip_address"]), "end": str(uplink["ip_address"])}],
                        "name": f"p2p to {peer}-{uplink['interface']}",
                        "default_gateway": f"{uplink['peer_ip_address'].split('/')[0]}",
                    }
                    subnets.append(subnet)
        return subnets

    @cached_property
    def _ipv4_ztp_boot_file(self) -> str | None:
        """
        Returns the file name to allow for ZTP to CV
        """
        custom_bootfile = get(self._hostvars, "inband_ztp_bootstrap_file")
        if custom_bootfile:
            return custom_bootfile
        cvp_instance_ips = get(self._hostvars, "cvp_instance_ips")
        if not cvp_instance_ips:
            return
        if "arista.io" in cvp_instance_ips[0]:
            return "https://www.arista.io/ztp/bootstrap"

        return f"https://{cvp_instance_ips[0]}/ztp/bootstrap"

    @cached_property
    def _dns_servers(self) -> list | None:
        """
        Returns the list of name servers
        """
        dns_servers = get(self._hostvars, "name_servers")
        if not dns_servers:
            return
        return dns_servers

    @cached_property
    def _ntp_servers(self) -> list | None:
        """
        Returns the list of name servers
        """
        ntp_servers_settings = get(self._hostvars, "ntp_settings.servers")
        if not ntp_servers_settings:
            return

        ntp_servers = []
        for ntp_server in ntp_servers_settings:
            # Validate NTP server IP address
            try:
                ntp_server_ip = IPv4Address(ntp_server["name"])
            except AddressValueError:
                continue
            ntp_servers.append(str(ntp_server_ip))

        if ntp_servers:
            ntp_dhcp_option = {"vendor_id": "NTP", "sub_options": [{"code": 42, "array_ipv4_address": ntp_servers}]}
            return ntp_dhcp_option

    @cached_property
    def dhcp_servers(self) -> dict | None:
        """
        Return structured config for dhcp_server
        """
        dhcp_servers = []
        # Set subnets for DHCP server
        dhcp_server = {"vrf": "default", "subnets": self._subnets}
        if len(dhcp_server["subnets"]) == 0:
            return
        # Set ZTP bootfile
        if ztp_bootfile := self._ipv4_ztp_boot_file:
            dhcp_server["tftp_server"] = {"file_ipv4": ztp_bootfile}
        # Set DNS servers
        if dns_servers := self._dns_servers:
            dhcp_server["dns_servers_ipv4"] = dns_servers
        # Set NTP servers
        if ntp_servers := self._ntp_servers:
            dhcp_server["ipv4_vendor_options"] = [ntp_servers]
        dhcp_servers.append(dhcp_server)
        return dhcp_servers
