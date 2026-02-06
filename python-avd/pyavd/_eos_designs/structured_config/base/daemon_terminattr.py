# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import ipaddress
from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.schema import EosDesigns
from pyavd._eos_designs.structured_config.constants import CV_REGION_TO_SERVER_MAP
from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor
from pyavd._errors import AristaAvdInvalidInputsError

if TYPE_CHECKING:
    from . import AvdStructuredConfigBaseProtocol


class DaemonTerminattrMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @structured_config_contributor
    def daemon_terminattr(self: AvdStructuredConfigBaseProtocol) -> None:
        """Configures daemon_terminattr settings based on cv_settings."""
        sflow_settings = self.inputs.sflow_settings
        flow_tracking_settings = self.inputs.flow_tracking_settings
        first_tracker_exported_to_cloudvision = next((tracker.name for tracker in flow_tracking_settings.trackers if tracker.export_to_cloudvision), None)

        if not (cv_settings := self.inputs.cv_settings):
            self._validate_missing_cv_settings(first_tracker_exported_to_cloudvision)
            return

        clusters: list[EosDesigns.CvSettings.Cvaas.ClustersItem | EosDesigns.CvSettings.OnpremClustersItem] = (
            list(cv_settings.cvaas.clusters) if cv_settings.cvaas.enabled else []
        )
        clusters.extend(cv_settings.onprem_clusters)

        if not clusters:
            # Do not add any config when we have no clusters configured.
            return

        self._validate_onprem_or_cvaas_clusters_dependencies(clusters)
        self.structured_config.daemon_terminattr._update(
            ingestexclude=cv_settings.terminattr.ingestexclude,
            smashexcludes=cv_settings.terminattr.smashexcludes,
            disable_aaa=cv_settings.terminattr.disable_aaa,
        )

        if first_tracker_exported_to_cloudvision is not None:
            flow_tracking_vrf = self.shared_utils.get_vrf(
                flow_tracking_settings.cloudvision_exporter.vrf, context="flow_tracking_settings.export_to_cloudvision.vrf"
            )
            self.structured_config.daemon_terminattr.ipfixaddr = f"{flow_tracking_vrf}/127.0.0.1:4739"

        if sflow_settings.export_to_cloudvision.enabled:
            sflow_vrf = self.shared_utils.get_vrf(sflow_settings.export_to_cloudvision.vrf, context="sflow_settings.export_to_cloudvision.vrf")
            self.structured_config.daemon_terminattr.sflowaddr = f"{sflow_vrf}/127.0.0.1:6343"

        if len(clusters) == 1:
            # Only one cluster so we add it with general terminattr config.
            cluster = clusters[0]
            self.structured_config.daemon_terminattr._update(
                cvaddrs=self.get_cv_addrs(cluster),
                cvauth=self.get_cv_auth(cluster),
                cvvrf=self.shared_utils.get_vrf(
                    cluster.vrf,
                    self.get_cv_cluster_vrf_context(cluster),
                ),
                cvsourceintf=self.shared_utils.get_source_interface(cluster.vrf, cluster.source_interface) if cv_settings.set_source_interfaces else None,
            )
            return

        # Multiple clusters
        for cluster in clusters:
            self.structured_config.daemon_terminattr.clusters.append_new(
                name=cluster.name,
                cvaddrs=self.get_cv_addrs(cluster)._cast_as(EosCliConfigGen.DaemonTerminattr.ClustersItem.Cvaddrs),
                cvauth=self.get_cv_auth(cluster)._cast_as(EosCliConfigGen.DaemonTerminattr.ClustersItem.Cvauth),
                cvvrf=self.shared_utils.get_vrf(
                    cluster.vrf,
                    self.get_cv_cluster_vrf_context(cluster),
                ),
                cvsourceintf=self.shared_utils.get_source_interface(cluster.vrf, cluster.source_interface) if cv_settings.set_source_interfaces else None,
            )

    @staticmethod
    def get_cv_cluster_vrf_context(cluster: EosDesigns.CvSettings.Cvaas.ClustersItem | EosDesigns.CvSettings.OnpremClustersItem) -> str:
        match cluster:
            case EosDesigns.CvSettings.Cvaas.ClustersItem():
                return f"cv_settings.cvaas[name={cluster.name}].vrf"
            case EosDesigns.CvSettings.OnpremClustersItem():
                return f"cv_settings.onprem_clusters[name={cluster.name}].vrf"

    @staticmethod
    def get_cv_addrs(cluster: EosDesigns.CvSettings.Cvaas.ClustersItem | EosDesigns.CvSettings.OnpremClustersItem) -> EosCliConfigGen.DaemonTerminattr.Cvaddrs:
        match cluster:
            case EosDesigns.CvSettings.Cvaas.ClustersItem():
                fqdn = CV_REGION_TO_SERVER_MAP[cluster.region]
                return EosCliConfigGen.DaemonTerminattr.Cvaddrs([f"{fqdn}:443"])
            case EosDesigns.CvSettings.OnpremClustersItem():
                return EosCliConfigGen.DaemonTerminattr.Cvaddrs(f"{server.name}:{server.port}" for server in cluster.servers)

    @staticmethod
    def get_cv_auth(cluster: EosDesigns.CvSettings.Cvaas.ClustersItem | EosDesigns.CvSettings.OnpremClustersItem) -> EosCliConfigGen.DaemonTerminattr.Cvauth:
        match cluster:
            case EosDesigns.CvSettings.Cvaas.ClustersItem():
                return EosCliConfigGen.DaemonTerminattr.Cvauth(method="token-secure", token_file=cluster.token_file)
            case EosDesigns.CvSettings.OnpremClustersItem():
                return EosCliConfigGen.DaemonTerminattr.Cvauth(method="token", token_file=cluster.token_file)

    def _validate_missing_cv_settings(self: AvdStructuredConfigBaseProtocol, first_tracker_exporting_to_cloudvision: str | None) -> None:
        """
        Verifies that when cv_settings is **not** configured no Sflow or flow tracking configuration expects export to CloudVision.

        Expected to be called when self.inputs.cv_settings is not set.
        """
        if first_tracker_exporting_to_cloudvision is not None:
            msg = (
                "CloudVision export is enabled for flow_tracking_settings, but 'cv_settings' is not defined. Please configure"
                f" 'cv_settings' when enabling 'flow_tracking_settings.trackers[name={first_tracker_exporting_to_cloudvision}].export_to_cloudvision'."
            )
            raise AristaAvdInvalidInputsError(msg)

        if self.inputs.sflow_settings.export_to_cloudvision.enabled:
            msg = (
                "CloudVision export is enabled for sFlow, but 'cv_settings' is not defined."
                " Please configure 'cv_settings' when enabling 'sflow_settings.export_to_cloudvision.enabled'."
            )
            raise AristaAvdInvalidInputsError(msg)

    def _validate_onprem_or_cvaas_clusters_dependencies(
        self: AvdStructuredConfigBaseProtocol,
        clusters: list[EosDesigns.CvSettings.Cvaas.ClustersItem | EosDesigns.CvSettings.OnpremClustersItem],
    ) -> None:
        """
        Validate infrastructure dependencies required when CloudVision clusters are configured.

        This validation applies to both CloudVision on-prem and CVaaS clusters and enforces the following requirements:

        - NTP must be configured when any CloudVision cluster is defined.
        - DNS must be configured for CVaaS clusters.
        - DNS must be configured for on-prem clusters if any server is specified using a DNS name instead of an IP address.

        Raises:
            AristaAvdInvalidInputsError: If required NTP or DNS settings are missing.
        """
        # NTP is always required
        if not self.inputs.ntp_settings.servers:
            msg = (
                "'ntp_settings.servers' must be configured when CloudVision "
                "clusters 'cv_settings.onprem_clusters[].servers[]' or 'cv_settings.cvaas.clusters[]' are defined."
            )
            raise AristaAvdInvalidInputsError(msg)

        # If DNS is already configured, no further DNS validation is needed
        if self.inputs.dns_settings.servers:
            return
        for cluster in clusters:
            match cluster:
                # DNS is always required for CVaaS
                case EosDesigns.CvSettings.Cvaas.ClustersItem():
                    msg = "'dns_settings' must be configured when 'cv_settings.cvaas.clusters[]' are defined with 'cv_settings.cvaas.enabled: true'."
                    raise AristaAvdInvalidInputsError(msg)
                # DNS is required for on-prem clusters using DNS names
                case EosDesigns.CvSettings.OnpremClustersItem():
                    if any(self._is_dns_name(server.name) for server in cluster.servers):
                        msg = "'dns_settings' must be configured when 'cv_settings.onprem_clusters[].servers[].name' is set to a DNS name."
                        raise AristaAvdInvalidInputsError(msg)

    @staticmethod
    def _is_dns_name(value: str) -> bool:
        """
        Determine whether a value represents a DNS name.

        The value is considered a DNS name if it cannot be parsed as a valid IPv4 or IPv6 address.

        Args:
            value: The string value to evaluate.

        Returns:
            True if the value is not a valid IP address, otherwise False.
        """
        try:
            ipaddress.ip_address(value)
        except ValueError:
            return True
        return False
