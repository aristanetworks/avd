# Copyright (c) 2023-2026 Arista Networks, Inc.
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
        if ssh_settings := self.inputs.ssh_settings:
            if ssh_settings.idle_timeout is not None:
                self.structured_config.management_ssh.idle_timeout = ssh_settings.idle_timeout

            if ssh_settings.enabled is not None:
                self.structured_config.management_ssh.enable = ssh_settings.enabled

            self._set_vrfs_and_acls(ssh_settings)

        # Enforce SSH management access in default VRF for ACT Digital Twin if required
        if self._act_ensure_ssh_access:
            self.structured_config.management_ssh.vrfs.obtain("default").enable = True
            self.structured_config.management_ssh.ip_access_group_in = None

    def _set_vrfs_and_acls(self: AvdStructuredConfigBaseProtocol, ssh_settings: EosDesigns.SshSettings) -> None:
        """SSH IPv4/IPv6 ACLs with VRFs. Resolves VRF from management VRFs."""
        for vrf in ssh_settings.vrfs._natural_sorted():
            vrf_name = self.shared_utils.get_vrf(vrf.name, context=f"ssh_settings.vrfs[name={vrf.name}]")

            if vrf_name == "default":
                self.structured_config.management_ssh.vrfs.append_new(name=vrf_name, enable=vrf.enabled)
                if vrf.enabled:
                    if vrf.ipv4_acl:
                        self.structured_config_utils._validate_ipv4_acl_exclusion(vrf.ipv4_acl, vrf.ipv4_standard_acl, context=f"ssh_settings.vrfs[name={vrf.name}]", direction=None)
                        self.structured_config.management_ssh._update(ip_access_group_in=vrf.ipv4_acl, ipv6_access_group_in=vrf.ipv6_acl)
                    elif vrf.ipv4_standard_acl:
                        self.structured_config_utils._set_ipv4_standard_acl(vrf.ipv4_standard_acl)
                        self.structured_config.management_ssh._update(ip_access_group_in=vrf.ipv4_standard_acl, ipv6_access_group_in=vrf.ipv6_acl)
            else:
                management_ssh_vrf = EosCliConfigGen.ManagementSsh.VrfsItem(name=vrf_name, enable=vrf.enabled, ipv6_access_group_in=vrf.ipv6_acl if vrf.enabled else None)
                if vrf.enabled:
                    if vrf.ipv4_acl:
                        self.structured_config_utils._validate_ipv4_acl_exclusion(vrf.ipv4_acl, vrf.ipv4_standard_acl, context=f"ssh_settings.vrfs[name={vrf.name}]", direction=None)
                        management_ssh_vrf.ip_access_group_in=vrf.ipv4_acl
                    elif vrf.ipv4_standard_acl:
                        self.structured_config_utils._set_ipv4_standard_acl(vrf.ipv4_standard_acl)
                        management_ssh_vrf.ip_access_group_in = vrf.ipv4_standard_acl
                self.structured_config.management_ssh.vrfs.append(management_ssh_vrf)
