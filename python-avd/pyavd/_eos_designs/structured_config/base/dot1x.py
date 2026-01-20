# Copyright (c) 2025-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor
from pyavd._errors import AristaAvdInvalidInputsError

if TYPE_CHECKING:
    from pyavd._eos_designs.schema import EosDesigns

    from . import AvdStructuredConfigBaseProtocol


class Dot1xMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfigBase class.
    """

    @structured_config_contributor
    def dot1x(self: AvdStructuredConfigBaseProtocol) -> None:
        """Configure dot1x settings based on the `dot1x_settings` data model."""
        dot1x_settings = self.inputs.dot1x_settings
        if not dot1x_settings.enabled:
            return

        self._configure_dot1x_aaa_authentication(dot1x_settings.authentication)
        self._configure_dot1x_dynamic_authorization(dot1x_settings.dynamic_authorization)
        self._configure_dot1x_aaa_accounting(dot1x_settings.accounting)
        self._configure_dot1x_global_settings(dot1x_settings)

    def _configure_dot1x_aaa_authentication(self: AvdStructuredConfigBaseProtocol, authentication_settings: EosDesigns.Dot1xSettings.Authentication) -> None:
        """Configure 802.1X AAA authentication settings."""
        if authentication_settings.radius_groups:
            self._validate_radius_groups(authentication_settings.radius_groups, context_msg="authentication server")
            self.structured_config.aaa_authentication.dot1x.default = " ".join(f"group {group}" for group in authentication_settings.radius_groups)
        else:
            self._validate_radius_servers()
            self.structured_config.aaa_authentication.dot1x.default = "group radius"

    def _configure_dot1x_dynamic_authorization(
        self: AvdStructuredConfigBaseProtocol, dyn_authorization_settings: EosDesigns.Dot1xSettings.DynamicAuthorization
    ) -> None:
        """Configure 802.1X AAA dynamic authorization settings."""
        if not (dyn_authorization_settings.enabled and dyn_authorization_settings.additional_groups):
            return

        self._validate_radius_groups(dyn_authorization_settings.additional_groups, "additional dynamic authorization server")

        self.structured_config.aaa_authorization.dynamic.dot1x_additional_groups = dyn_authorization_settings.additional_groups._cast_as(
            new_type=EosCliConfigGen.AaaAuthorization.Dynamic.Dot1xAdditionalGroups
        )

    def _configure_dot1x_aaa_accounting(self: AvdStructuredConfigBaseProtocol, accounting_settings: EosDesigns.Dot1xSettings.Accounting) -> None:
        """Configure 802.1X AAA accounting settings."""
        if not accounting_settings.enabled:
            return

        if accounting_settings.radius_groups:
            self._validate_radius_groups(accounting_settings.radius_groups, "accounting server")

            # Add RADIUS server groups.
            for group in accounting_settings.radius_groups:
                self.structured_config.aaa_accounting.dot1x.default.methods.append_unique(
                    EosCliConfigGen.AaaAccounting.Dot1x.Default.MethodsItem(method="group", group=group, multicast=accounting_settings.multicast)
                )
        else:
            # Presence of at least one RADIUS server has already been validated in the AAA authentication configuration above.
            self.structured_config.aaa_accounting.dot1x.default.methods.append(
                EosCliConfigGen.AaaAccounting.Dot1x.Default.MethodsItem(method="group", group="radius", multicast=accounting_settings.multicast)
            )

        # Set record mode (start-stop vs stop-only).
        self.structured_config.aaa_accounting.dot1x.default.type = accounting_settings.mode

        # Add Syslog fallback.
        if accounting_settings.syslog:
            self.structured_config.aaa_accounting.dot1x.default.methods.append_new(method="logging")

    def _configure_dot1x_global_settings(self: AvdStructuredConfigBaseProtocol, dot1x_settings: EosDesigns.Dot1xSettings) -> None:
        """Configure 802.1X global settings."""
        self.structured_config.dot1x = EosCliConfigGen.Dot1x(
            system_auth_control=True,
            protocol_bpdu_bypass=dot1x_settings.bypass_bpdu,
            protocol_lldp_bypass=dot1x_settings.bypass_lldp,
            dynamic_authorization=dot1x_settings.dynamic_authorization.enabled,
        )
        if dot1x_settings.radius_av_pairs.service_type is True:
            self.structured_config.dot1x.radius_av_pair.service_type = True
        if dot1x_settings.mac_based_authentication.username_format:
            self.structured_config.dot1x.radius_av_pair_username_format = EosCliConfigGen.Dot1x.RadiusAvPairUsernameFormat(
                delimiter=dot1x_settings.mac_based_authentication.username_format.delimiter,
                mac_string_case=dot1x_settings.mac_based_authentication.username_format.letter_case,
            )

    def _validate_radius_groups(
        self: AvdStructuredConfigBaseProtocol,
        groups: EosDesigns.Dot1xSettings.Authentication.RadiusGroups
        | EosDesigns.Dot1xSettings.DynamicAuthorization.AdditionalGroups
        | EosDesigns.Dot1xSettings.Accounting.RadiusGroups,
        context_msg: str,
    ) -> None:
        """Validate that the provided groups are defined in `aaa_settings.radius.servers`."""
        undefined_groups = set(groups).difference(self._radius_server_groups)

        # "radius" is a special group in EOS for all servers, so we don't need to validate it against defined groups.
        undefined_groups.discard("radius")

        if undefined_groups:
            msg = (
                f"The RADIUS {context_msg} group(s) '{', '.join(sorted(undefined_groups))}' are not defined on any server under 'aaa_settings.radius.servers'."
            )
            raise AristaAvdInvalidInputsError(msg)

    def _validate_radius_servers(self: AvdStructuredConfigBaseProtocol) -> None:
        """Validate that there is at least one RADIUS server defined in `aaa_settings.radius.servers`."""
        if len(self.inputs.aaa_settings.radius.servers) == 0:
            msg = "At least one RADIUS server must be defined under `aaa_settings.radius.servers` for 802.1X authentication."
            raise AristaAvdInvalidInputsError(msg)

    @cached_property
    def _radius_server_groups(self: AvdStructuredConfigBaseProtocol) -> set[str]:
        """Return a set of all RADIUS server group names defined under `aaa_settings.radius.servers`."""
        return {group for server in self.inputs.aaa_settings.radius.servers for group in server.groups}
