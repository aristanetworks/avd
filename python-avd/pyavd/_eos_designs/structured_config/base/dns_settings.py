# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor

if TYPE_CHECKING:
    from . import AvdStructuredConfigBaseProtocol


class DnsSettingsMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @structured_config_contributor
    def dns_settings(self: AvdStructuredConfigBaseProtocol) -> None:
        """
        Configure DNS settings from the dns_settings input model.

        Sets IP name servers (with VRF and priority), IP hosts, DNS domain, domain list, and domain-lookup source interfaces per VRF.
        """
        if not self.inputs.dns_settings:
            return

        if self.inputs.dns_settings.ip_hosts:
            self.structured_config.ip_hosts = self.inputs.dns_settings.ip_hosts

        if self.inputs.dns_settings.domain:
            self.structured_config.dns_domain = self.inputs.dns_settings.domain

        self.structured_config.domain_list = EosCliConfigGen.DomainList(self.inputs.dns_settings.domain_list)

        vrfs = self.inputs.dns_settings.vrfs
        for server in self.inputs.dns_settings.servers:
            server_vrf, source_interface = self.shared_utils.get_vrf_and_source_interface(
                vrf_input=server.vrf,
                vrfs=vrfs,
                set_source_interfaces=self.inputs.dns_settings.set_source_interfaces,
                context=f"dns_settings.servers[ip_address={server.ip_address}].vrf",
            )
            if source_interface:
                self.structured_config.ip_domain_lookup.source_interfaces.append_new(name=source_interface, vrf=server_vrf if server_vrf != "default" else None)

            ip_name_server_vrf = self.structured_config.ip_name_server.vrfs.obtain(server_vrf)
            ip_name_server_vrf.servers.append_new(ip_address=server.ip_address, priority=server.priority)
