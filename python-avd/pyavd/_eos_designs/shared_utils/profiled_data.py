# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING, Protocol

from pyavd._errors import AristaAvdInvalidInputsError
from pyavd._utils.profiles import resolve_profile

if TYPE_CHECKING:
    from pyavd._eos_designs.schema import EosDesigns

    from . import SharedUtilsProtocol


class ProfiledDataMixin(Protocol):
    """
    Mixin Class providing a subset of SharedUtils.

    Class should only be used as Mixin to the SharedUtils class.
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def dns_settings(self: SharedUtilsProtocol) -> EosDesigns.DnsSettings:
        """
        DNS settings with the node's `dns_settings_profile` resolved and merged in.

        If `dns_settings_profile` is not defined, the root-level `dns_settings` is returned.
        """
        if not self.node_config.dns_settings_profile:
            return self.inputs.dns_settings
        return resolve_profile(
            self.inputs.dns_settings,
            self.inputs.dns_settings_profiles,
            self.node_config.dns_settings_profile,
            target_name="dns_settings",
        )

    @cached_property
    def dns_settings_servers(self: SharedUtilsProtocol) -> EosDesigns.DnsSettings.Servers | None:
        """
        Return resolved DNS servers, or None if no servers are configured.

        Read without inserting a default empty list into the resolved DNS settings.
        """
        return self.dns_settings._get("servers") or None

    @cached_property
    def ntp_settings(self: SharedUtilsProtocol) -> EosDesigns.NtpSettings:
        """
        NTP settings with the node's `ntp_settings_profile` resolved and merged in.

        If `ntp_settings_profile` is not defined, the root-level `ntp_settings` is returned.
        """
        if not self.node_config.ntp_settings_profile:
            return self.inputs.ntp_settings

        return resolve_profile(
            self.inputs.ntp_settings,
            self.inputs.ntp_settings_profiles,
            self.node_config.ntp_settings_profile,
            target_name="ntp_settings",
        )

    @cached_property
    def cv_settings(self: SharedUtilsProtocol) -> EosDesigns.CvSettings:
        """
        CloudVision settings with the node's `cv_settings_profile` resolved and merged in.

        If `cv_settings_profile` is not defined, the root-level `cv_settings` is returned.
        """
        cv_settings = self.inputs.cv_settings
        if self.node_config.cv_settings_profile:
            cv_settings = resolve_profile(
                self.inputs.cv_settings,
                self.inputs.cv_settings_profiles,
                self.node_config.cv_settings_profile,
                target_name="cv_settings",
            )

        # The global schema requires `cvaas.enabled`; profiles may omit it while being defined.
        cvaas = cv_settings._get("cvaas")
        if cvaas is not None and cvaas._get("enabled") is None:
            msg = "The 'enabled' setting must be configured when CVaaS settings are provided."
            raise AristaAvdInvalidInputsError(msg)

        self._validate_cv_onprem_clusters(cv_settings)

        return cv_settings

    def _validate_cv_onprem_clusters(self, cv_settings: EosDesigns.CvSettings) -> None:
        """
        Validates if profile resolution does not produce an invalid `EosDesigns.CvSettings` object.

        Some of the schema validations had to be relaxed in order to support profiles. To keep the
        existing behaviours, the error paths should now be validated in the runtime.
        """
        onprem_clusters = cv_settings._get("onprem_clusters")
        if not onprem_clusters:
            return

        server_names = set()
        for cluster in onprem_clusters:
            servers = [server.name for server in cluster.servers]
            # The global schema requires at least one server after profile inheritance is resolved.
            if not servers:
                msg = f"At least 1 server must be provided for on-prem CVP cluster {cluster.name}"
                raise AristaAvdInvalidInputsError(msg)
            # The global schema caps each resolved cluster's server list at three.
            if len(servers) > 3:
                msg = f"Max 3 servers allowed for on-prem CVP cluster {cluster.name}, provided: {sorted(servers)}"
                raise AristaAvdInvalidInputsError(msg)
            for server_name in servers:
                # Mirrors `onprem_clusters.unique_keys: [servers.name]` across cluster entries.
                if server_name in server_names:
                    msg = f"Duplicate on-prem CVP server name '{server_name}'. Server names must be unique across clusters."
                    raise AristaAvdInvalidInputsError(msg)
                server_names.add(server_name)
