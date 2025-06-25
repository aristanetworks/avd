# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor

if TYPE_CHECKING:
    from pyavd._eos_designs.schema import EosDesigns

    from . import AvdStructuredConfigBaseProtocol


class ManagementSshMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @structured_config_contributor
    def management_ssh(self: AvdStructuredConfigBaseProtocol) -> None:
        """management_ssh set based on "ssh_settings" data-model."""
        if not (ssh_settings := self.inputs.ssh_settings):
            return

        if ssh_settings.idle_timeout:
            self.structured_config.management_ssh.idle_timeout = ssh_settings.idle_timeout

        self._ssh_vrfs_acls(ssh_settings)

    def _ssh_vrfs(self: AvdStructuredConfigBaseProtocol, ssh_settings: EosDesigns.SshSettings) -> None:
        """SSH IPv4/IPv6 ACLs with VRFs. Resolves VRF from management VRFs."""
        vrfs = EosCliConfigGen.ManagementSsh.Vrfs()
        for vrf in ssh_settings.vrfs:
            vrf_name = self.get_vrf(vrf.name, context=f"ssh_settings.vrfs[name={vrf.name}]")
            vrfs.append_new(name=vrf_name, enable=vrf.enabled)
            self.structured_config.management_ssh.vrfs = vrfs._natural_sorted()

            if vrf.ipv4_acl:
                self.structured_config.management_ssh.access_groups.append_new(name=vrf.ipv4_acl, vrf=vrf.name if vrf.name != "default" else None)

            if vrf.ipv6_acl:
                self.structured_config.management_ssh.ipv6_access_groups.append_new(name=vrf.ipv6_acl, vrf=vrf.name if vrf.name != "default" else None)
