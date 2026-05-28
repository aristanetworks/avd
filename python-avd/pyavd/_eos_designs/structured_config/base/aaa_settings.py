# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Any, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor
from pyavd._errors import AristaAvdInvalidInputsError
from pyavd.j2filters import secure_hash

if TYPE_CHECKING:
    from pyavd._eos_designs.schema import EosDesigns

    from . import AvdStructuredConfigBaseProtocol


class AaaSettingsMixin(Protocol):
    """
    Mixin Class used to generate structured config.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @structured_config_contributor
    def enable_password(self: AvdStructuredConfigBaseProtocol) -> None:
        """enable_password.disable is set to match EOS default config and historic configs if aaa_settings.enable_password.password is not defined."""
        if self.inputs.aaa_settings.enable_password.password:
            self.structured_config.enable_password._update(hash_algorithm="sha512", key=self.inputs.aaa_settings.enable_password.password)
        elif self.inputs.aaa_settings.enable_password.cleartext_password:
            salt = self.get_salt(self.shared_utils.hostname)
            secure_hash_password = secure_hash(self.inputs.aaa_settings.enable_password.cleartext_password, salt)
            self.structured_config.enable_password._update(hash_algorithm="sha512", key=secure_hash_password)
        else:
            self.structured_config.enable_password.disabled = True

    @structured_config_contributor
    def local_users(self: AvdStructuredConfigBaseProtocol) -> None:
        """local_users set based on global aaa_settings.local_users data model."""
        # Exit early if no local users are defined in inputs
        if not (local_users := self.inputs.aaa_settings.local_users):
            return

        for local_user in local_users._natural_sorted():
            local_user_data = EosCliConfigGen.LocalUsersItem(name=local_user.name, disabled=local_user.disabled)

            # If the user is disabled, append it as-is and skip further processing
            if local_user_data.disabled is True:
                self.structured_config.local_users.append(local_user_data)
                continue
            local_user_data._update(
                privilege=local_user.privilege,
                role=local_user.role,
                ssh_key=local_user.ssh_key,
                secondary_ssh_key=local_user.secondary_ssh_key,
                shell=local_user.shell,
            )

            # Pre-hashed SHA-512 password
            if local_user.sha512_password:
                local_user_data.sha512_password = local_user.sha512_password
            # Cleartext password (hashed using a deterministic salt)
            elif local_user.cleartext_password:
                salt = self.get_salt(f"{self.shared_utils.hostname}-{local_user.name}")
                password = secure_hash(local_user.cleartext_password, salt)
                local_user_data.sha512_password = password
            # Explicitly configure user with no password
            elif local_user.no_password:
                local_user_data.no_password = True
                # EOS requires either no_password: true or a secret to be set.
            else:
                msg = f"Either 'sha512_password', 'cleartext_password' or 'no_password: true' must be set for username '{local_user.name}'."
                raise AristaAvdInvalidInputsError(msg)
            self.structured_config.local_users.append(local_user_data)

    def _add_radius_server_config(self: AvdStructuredConfigBaseProtocol, server: EosDesigns.AaaSettings.Radius.ServersItem, server_vrf: str) -> None:
        """
        Add radius server configuration to the appropriate VRF.

        Args:
            server: The RADIUS server configuration from EOS Designs inputs.
            server_vrf: The VRF name where the server should be configured.
        """
        server_kwargs: dict[str, Any] = {"host": server.host}
        if server.tls.enabled:
            server_kwargs["tls"] = server.tls
        else:
            server_kwargs["key"] = self._get_tacacs_or_radius_server_password(server)

        server_kwargs["timeout"] = server.timeout
        server_kwargs["retransmit"] = server.retransmit

        if server_vrf == "default":
            self.structured_config.radius_server.servers.append_new(**server_kwargs)
        else:
            radius_server_vrf = self.structured_config.radius_server.vrfs.obtain(server_vrf)
            if server.tls.enabled:
                server_kwargs["tls"] = server.tls._cast_as(EosCliConfigGen.RadiusServer.VrfsItem.ServersItem.Tls)
            radius_server_vrf.servers.append_new(**server_kwargs)

    @structured_config_contributor
    def radius_servers(self: AvdStructuredConfigBaseProtocol) -> None:
        """Parse AAA radius server configurations and update structured config with server and source interface details."""
        if not self.inputs.aaa_settings.radius:
            return

        for server in self.inputs.aaa_settings.radius.servers:
            server_vrf, source_interface = self.shared_utils.get_vrf_and_source_interface(
                vrf_input=server.vrf,
                vrfs=self.inputs.aaa_settings.radius.vrfs,
                set_source_interfaces=True,
                context=f"aaa_settings.radius.servers[host={server.host}].vrf",
            )
            if source_interface:
                if server_vrf == "default":
                    self.structured_config.ip_radius.source_interface = source_interface
                else:
                    self.structured_config.ip_radius.vrfs.append_new(name=server_vrf, source_interface=source_interface)

            self._add_radius_server_config(server, server_vrf)

            for group in server.groups:
                radius_group = self.structured_config.aaa_server_groups.obtain(group)
                radius_group.type = "radius"
                group_server = EosCliConfigGen.AaaServerGroupsItem.ServersItem(server=server.host, vrf=server_vrf)
                if self.inputs.avd_design_future.include_tls_on_radius_server_group_members and server.tls.enabled:
                    group_server.tls._update(enabled=server.tls.enabled, port=server.tls.port)
                radius_group.servers.append(group_server)

    @structured_config_contributor
    def tacacs_servers(self: AvdStructuredConfigBaseProtocol) -> None:
        """Parse AAA tacacs server configurations and update structured config with server and source interface details."""
        if not self.inputs.aaa_settings.tacacs:
            return

        all_tacacs_servers = EosCliConfigGen.TacacsServers.Hosts()
        for server in self.inputs.aaa_settings.tacacs.servers:
            server_vrf, source_interface = self.shared_utils.get_vrf_and_source_interface(
                vrf_input=server.vrf,
                vrfs=self.inputs.aaa_settings.tacacs.vrfs,
                set_source_interfaces=True,
                context=f"aaa_settings.tacacs.servers[host={server.host}].vrf",
            )

            if source_interface:
                if server_vrf == "default":
                    self.structured_config.ip_tacacs.source_interface = source_interface
                else:
                    self.structured_config.ip_tacacs.vrfs.append_new(name=server_vrf, source_interface=source_interface)

            tacacs_server = EosCliConfigGen.TacacsServers.HostsItem(host=server.host, vrf=server_vrf)
            if not all_tacacs_servers.__contains__(tacacs_server):
                all_tacacs_servers.append(tacacs_server)
                server_key = self._get_tacacs_or_radius_server_password(server)
                self.structured_config.tacacs_servers.hosts.append_new(host=server.host, vrf=server_vrf, key=server_key, timeout=server.timeout)

                for group in server.groups:
                    tacacs_group = self.structured_config.aaa_server_groups.obtain(group)
                    tacacs_group.type = "tacacs+"
                    tacacs_group.servers.append_new(server=server.host, vrf=server_vrf)

        self.structured_config.tacacs_servers.policy_unknown_mandatory_attribute_ignore = (
            self.inputs.aaa_settings.tacacs.policy.ignore_unknown_mandatory_attribute
        )

    @structured_config_contributor
    def aaa_authentication(self: AvdStructuredConfigBaseProtocol) -> None:
        """Assign AAA authentication configuration from inputs to structured config."""
        if not self.inputs.aaa_settings.authentication:
            return

        self.structured_config.aaa_authentication = self.inputs.aaa_settings.authentication._cast_as(new_type=EosCliConfigGen.AaaAuthentication)

    @structured_config_contributor
    def aaa_authorization(self: AvdStructuredConfigBaseProtocol) -> None:
        """Assign AAA authorization configuration from inputs to structured config."""
        if not self.inputs.aaa_settings.authorization:
            return

        self.structured_config.aaa_authorization = self.inputs.aaa_settings.authorization._cast_as(new_type=EosCliConfigGen.AaaAuthorization)

    @structured_config_contributor
    def aaa_accounting(self: AvdStructuredConfigBaseProtocol) -> None:
        """Assign AAA accounting configuration from inputs to structured config."""
        if not self.inputs.aaa_settings.accounting:
            return

        self.structured_config.aaa_accounting = self.inputs.aaa_settings.accounting._cast_as(new_type=EosCliConfigGen.AaaAccounting)

    @structured_config_contributor
    def aaa_root_login(self: AvdStructuredConfigBaseProtocol) -> None:
        """Assign AAA root login configuration from inputs to structured config."""
        aaa_root_login = self.inputs.aaa_settings.root_login
        self.structured_config.aaa_root.disabled = not aaa_root_login.enabled
        self.structured_config.aaa_root.secret.sha512_password = aaa_root_login.sha512_password
