# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from ipaddress import ip_address
from typing import TYPE_CHECKING, Literal, Protocol, cast

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor
from pyavd._errors import AristaAvdInvalidInputsError, AristaAvdMissingVariableError
from pyavd._utils import get_ip_from_ip_prefix
from pyavd._utils.password_utils import ntp_encrypt

if TYPE_CHECKING:
    from . import AvdStructuredConfigBaseProtocol


class NtpMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @structured_config_contributor
    def ntp(self: AvdStructuredConfigBaseProtocol) -> None:
        """Ntp set based on "ntp_settings" data-model."""
        if not (ntp_settings := self.inputs.ntp_settings):
            return

        # Since the EOS Config data model almost matches, we can copy most data directly.
        self.structured_config.ntp._update(
            authenticate=ntp_settings.authenticate,
            authenticate_servers_only=ntp_settings.authenticate_servers_only,
            trusted_keys=ntp_settings.trusted_keys,
        )
        for authentication_key in ntp_settings.authentication_keys:
            # `key` takes precedence over `cleartext_key`
            if authentication_key.key is not None:
                self.structured_config.ntp.authentication_keys.append(
                    authentication_key._cast_as(EosCliConfigGen.Ntp.AuthenticationKeysItem, ignore_extra_keys=True)
                )
            elif authentication_key.cleartext_key is not None:
                # always type 7
                # deterministic salt based on the key ID
                salt = cast("Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]", authentication_key.id % 16)
                output_key = ntp_encrypt(authentication_key.cleartext_key, salt=salt)
                self.structured_config.ntp.authentication_keys.append_new(
                    id=authentication_key.id, key_type="7", key=output_key, hash_algorithm=authentication_key.hash_algorithm
                )
            else:
                path_prefix = f"ntp_settings.authentication_keys[id={authentication_key.id}]"
                msg = f"`{path_prefix}.key` or `{path_prefix}.cleartext_key`"
                raise AristaAvdMissingVariableError(msg)

        if not ntp_settings.servers:
            # Quick return if we have no servers.
            return

        # Get server_vrf from ntp_settings and configure with the relevant VRF.
        # Also set relevant local interface.
        server_vrf = self.shared_utils.get_vrf(ntp_settings.server_vrf, context="ntp_settings.server_vrf")
        self.structured_config.ntp.vrf = server_vrf
        # Reusing get_source_interface for local-interface settings.
        if local_interface := self.shared_utils.get_source_interface(ntp_settings.server_vrf, source_interface_override=None):
            self.structured_config.ntp.local_interface.name = local_interface
            self.structured_config.ntp.local_interface.vrf = server_vrf

        # First server is set as preferred if ntp_settings.set_first_ntp_server_as_preferred set to true
        first = self.inputs.ntp_settings.set_first_ntp_server_as_preferred
        for server in ntp_settings.servers:
            ntp_server = server._cast_as(EosCliConfigGen.Ntp.ServersItem)
            if server.source_address is not None:
                ntp_server.source_address = self._get_ntp_server_source_address(server.name, server.source_address, server_vrf)
            if first:
                ntp_server.preferred = True
                first = False

            self.structured_config.ntp.servers.append(ntp_server)

    def _get_ntp_server_source_address(
        self: AvdStructuredConfigBaseProtocol,
        server_name: str | None,
        source_address: str,
        server_vrf: str,
    ) -> str:
        """Resolve the source address for an NTP server."""
        if not source_address.startswith("use_"):
            self._validate_ntp_server_source_address_type(server_name, source_address)
            return source_address

        context = f"ntp_settings.servers[name={server_name}].source_address"

        match source_address:
            case "use_mgmt_interface_ipv4":
                required_vrf = self.shared_utils.mgmt_interface_vrf
                ip_prefix = self.shared_utils.node_config.mgmt_ip
                missing_variable = "mgmt_ip"
            case "use_mgmt_interface_ipv6":
                required_vrf = self.shared_utils.mgmt_interface_vrf
                ip_prefix = self.shared_utils.node_config.ipv6_mgmt_ip
                missing_variable = "ipv6_mgmt_ip"
            case "use_inband_mgmt_interface_ipv4":
                required_vrf = self.shared_utils.inband_mgmt_vrf
                ip_prefix = self.shared_utils.inband_mgmt_ip
                missing_variable = "inband_mgmt_ip"
            case "use_inband_mgmt_interface_ipv6":
                required_vrf = self.shared_utils.inband_mgmt_vrf
                ip_prefix = self.shared_utils.inband_mgmt_ipv6_address
                missing_variable = "inband_mgmt_ipv6_address"
            case _:
                msg = (
                    f"'{context}' is set to '{source_address}', which is not supported. "
                    "Supported values are 'use_mgmt_interface_ipv4', 'use_mgmt_interface_ipv6', "
                    "'use_inband_mgmt_interface_ipv4', and 'use_inband_mgmt_interface_ipv6'."
                )
                raise AristaAvdInvalidInputsError(msg, host=self.shared_utils.hostname)

        if ip_prefix is None:
            msg = f"'{context}' is set to '{source_address}' but this node is missing '{missing_variable}'."
            raise AristaAvdInvalidInputsError(msg, host=self.shared_utils.hostname)

        if ip_prefix in {"dhcp", "auto-config"}:
            msg = (
                f"'{context}' is set to '{source_address}' but {missing_variable} is set to '{ip_prefix}'. "
                "A static IP is required to resolve this source_address keyword."
            )
            raise AristaAvdInvalidInputsError(msg, host=self.shared_utils.hostname)

        if required_vrf is not None and server_vrf != required_vrf:
            msg = (
                f"'{context}' is set to '{source_address}', but 'ntp_settings.server_vrf' resolves to '{server_vrf}'. "
                f"This source_address keyword requires VRF '{required_vrf}'."
            )
            raise AristaAvdInvalidInputsError(msg, host=self.shared_utils.hostname)

        resolved_source_address = get_ip_from_ip_prefix(ip_prefix)
        self._validate_ntp_server_source_address_type(server_name, resolved_source_address)
        return resolved_source_address

    def _validate_ntp_server_source_address_type(self: AvdStructuredConfigBaseProtocol, server_name: str | None, source_address: str) -> None:
        """Validate that source address type matches server address type for IP-address-based servers."""
        if server_name is None:
            # TODO: 7.0 Clean up when `server.name` becomes primary key in the data model.
            msg = "'ntp_settings.servers[].name' is required and cannot be null/none."
            raise AristaAvdInvalidInputsError(msg, host=self.shared_utils.hostname)

        try:
            server_ip = ip_address(server_name)
        except ValueError:
            # `server_name` may be an FQDN/DNS name instead of a literal IP.
            # In that case we cannot determine the server IP version at build time,
            # so this IP-version consistency check is intentionally skipped.
            return

        try:
            source_ip = ip_address(source_address)
        except ValueError as err:
            msg = f"'ntp_settings.servers[name={server_name}].source_address' resolves to '{source_address}', which is not a valid IP address."
            raise AristaAvdInvalidInputsError(msg, host=self.shared_utils.hostname) from err

        if server_ip.version == source_ip.version:
            return

        msg = (
            f"'ntp_settings.servers[name={server_name}].source_address' resolves to '{source_address}', "
            f"but NTP server '{server_name}' is IPv{server_ip.version}. "
            f"Set a matching IPv{server_ip.version} source address or use an FQDN server name."
        )
        raise AristaAvdInvalidInputsError(msg, host=self.shared_utils.hostname)
