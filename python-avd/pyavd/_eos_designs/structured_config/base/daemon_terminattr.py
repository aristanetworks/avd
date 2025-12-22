# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

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
        """
        Configures daemon_terminattr settings based on cv_settings and calls _legacy_daemon_terminattr for the legacy cv_* and terminattr_* models.

        The schema will enforce that we only use either new or old models.
        """
        cv_settings = self.inputs.cv_settings
        sflow_settings = self.inputs.sflow_settings

        if not cv_settings:
            if sflow_settings.export_to_cloudvision.enabled:
                msg = (
                    "CloudVision export is enabled for sFlow, but 'cv_settings' is not defined."
                    " Please configure 'cv_settings' when enabling 'sflow_settings.export_to_cloudvision.enabled'."
                )
                raise AristaAvdInvalidInputsError(msg)
            return

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
