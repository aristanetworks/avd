# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.schema import EosDesigns
from pyavd._eos_designs.structured_config.constants import CV_REGION_TO_SERVER_MAP
from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor

if TYPE_CHECKING:
    from . import AvdStructuredConfigBaseProtocol


class DaemonTerminattrMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @structured_config_contributor
    def daemon_terminattr(self: AvdStructuredConfigBaseProtocol) -> None:
        """
        Configures daemon_terminattr settings based on cv_settings and calls _legacy_daemon_terminattr for the legacy cv_* and terminattr_* models.

        The schema will enforce that we only use either new or old models.
        """
        if not self.inputs.cv_settings:
            self._legacy_daemon_terminattr()
            return

        cv_settings = self.inputs.cv_settings

        clusters: list[EosDesigns.CvSettings.Cvaas.ClustersItem | EosDesigns.CvSettings.OnpremClustersItem] = (
            list(cv_settings.cvaas.clusters) if cv_settings.cvaas.enabled else []
        )
        clusters.extend(cv_settings.onprem_clusters)

        if not clusters:
            # Do not add any config when we have no clusters configured.
            return

        self.structured_config.daemon_terminattr._update(
            ingestexclude=cv_settings.terminattr.ingestexclude,
            smashexcludes=cv_settings.terminattr.smashexcludes,
            disable_aaa=cv_settings.terminattr.disable_aaa,
        )

        if len(clusters) == 1:
            # Only one cluster so we add it with general terminattr config.
            cluster = clusters[0]
            self.structured_config.daemon_terminattr._update(
                cvaddrs=self.get_cv_addrs(cluster),
                cvauth=self.get_cv_auth(cluster),
                cvvrf=self.get_vrf(
                    cluster.vrf,
                    self.get_cv_cluster_vrf_context(cluster),
                ),
                cvsourceintf=self.get_source_interface(cluster.vrf, cluster.source_interface) if cv_settings.set_source_interfaces else None,
            )
            return

        # Multiple clusters
        for cluster in clusters:
            self.structured_config.daemon_terminattr.clusters.append_new(
                name=cluster.name,
                cvaddrs=self.get_cv_addrs(cluster)._cast_as(EosCliConfigGen.DaemonTerminattr.ClustersItem.Cvaddrs),
                cvauth=self.get_cv_auth(cluster)._cast_as(EosCliConfigGen.DaemonTerminattr.ClustersItem.Cvauth),
                cvvrf=self.get_vrf(
                    cluster.vrf,
                    self.get_cv_cluster_vrf_context(cluster),
                ),
                cvsourceintf=self.get_source_interface(cluster.vrf, cluster.source_interface) if cv_settings.set_source_interfaces else None,
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

    def _legacy_daemon_terminattr(self: AvdStructuredConfigBaseProtocol) -> None:
        """
        daemon_terminattr set based on cvp_instance_ips.

        Updating cvaddrs and cvauth considering conditions for cvaas and cvp_on_prem IPs

            if 'arista.io' in cvp_instance_ips:
                 <updating as cvaas_ip>
            else:
                 <updating as cvp_on_prem ip>
        """
        cvp_instance_ip_list = self.inputs.cvp_instance_ips
        if not cvp_instance_ip_list:
            return

        for cvp_instance_ip in cvp_instance_ip_list:
            if "arista.io" in cvp_instance_ip:
                # updating for cvaas_ips
                self.structured_config.daemon_terminattr.cvaddrs.append(f"{cvp_instance_ip}:443")
                self.structured_config.daemon_terminattr.cvauth._update(
                    method="token-secure",
                    # Ignoring sonar-lint false positive for tmp path since this is config for EOS
                    token_file=self.inputs.cvp_token_file or "/tmp/cv-onboarding-token",  # NOSONAR # noqa: S108
                )
            else:
                # updating for cvp_on_prem_ips
                cv_address = f"{cvp_instance_ip}:{self.inputs.terminattr_ingestgrpcurl_port}"
                self.structured_config.daemon_terminattr.cvaddrs.append(cv_address)
                if (cvp_ingestauth_key := self.inputs.cvp_ingestauth_key) is not None:
                    self.structured_config.daemon_terminattr.cvauth._update(method="key", key=cvp_ingestauth_key)
                else:
                    self.structured_config.daemon_terminattr.cvauth._update(
                        method="token",
                        # Ignoring sonar-lint false positive for tmp path since this is config for EOS
                        token_file=self.inputs.cvp_token_file or "/tmp/token",  # NOSONAR # noqa: S108
                    )

        self.structured_config.daemon_terminattr._update(
            cvvrf=self.inputs.mgmt_interface_vrf,
            smashexcludes=self.inputs.terminattr_smashexcludes,
            ingestexclude=self.inputs.terminattr_ingestexclude,
            disable_aaa=self.inputs.terminattr_disable_aaa,
        )
