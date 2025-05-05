# Copyright (c) 2024-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen

if TYPE_CHECKING:
    from pyavd._eos_designs.schema import EosDesigns

    from . import AvdStructuredConfigNetworkServicesProtocol


class MetadataMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    def set_cv_pathfinder_metadata_zscaler_internet_exit_policy(
        self: AvdStructuredConfigNetworkServicesProtocol,
        internet_exit_policy: EosDesigns.CvPathfinderInternetExitPoliciesItem,
        tunnels_metadata: EosCliConfigGen.Metadata.CvPathfinder.InternetExitPoliciesItem.Tunnels,
    ) -> None:
        """
        Set the metadata.cv_pathfinder.internet_exit_policies for the Zscaler policies if available.

        Args:
            internet_exit_policy: The Zscaler internet exit policy to set metadata for.
            tunnels_metadata: the list of per-tunnel metadata pre-computed by the caller.
        """
        ufqdn, ipsec_key = self._get_ipsec_credentials(internet_exit_policy)
        exit_policy = EosCliConfigGen.Metadata.CvPathfinder.InternetExitPoliciesItem(
            name=internet_exit_policy.name,
            type=internet_exit_policy.type,
            city=self._zscaler_endpoints.device_location.city,
            country=self._zscaler_endpoints.device_location.country,
            upload_bandwidth=internet_exit_policy.zscaler.upload_bandwidth,
            download_bandwidth=internet_exit_policy.zscaler.download_bandwidth,
            firewall=internet_exit_policy.zscaler.firewall.enabled,
            ips_control=internet_exit_policy.zscaler.firewall.ips,
            acceptable_use_policy=internet_exit_policy.zscaler.acceptable_use_policy,
            tunnels=tunnels_metadata,
        )
        exit_policy.vpn_credentials.append_new(fqdn=ufqdn, vpn_type="UFQDN", pre_shared_key=ipsec_key)

        self.structured_config.metadata.cv_pathfinder.internet_exit_policies.append(exit_policy)

    def set_cv_pathfinder_metadata_applications(self: AvdStructuredConfigNetworkServicesProtocol) -> None:
        """
        Set the metadata.cv_pathfinder.applications if available.

        This is called after the structured_config has been populated.
        """
        if not self.shared_utils.is_cv_pathfinder_server or (atr := self.structured_config.application_traffic_recognition) is None:
            return

        applications = atr.applications
        user_defined_app_names = set(applications.ipv4_applications.keys())
        categories = atr.categories
        for profile in atr.application_profiles:
            application_profile = EosCliConfigGen.Metadata.CvPathfinder.Applications.ProfilesItem(name=profile.name)
            application_profile.transport_protocols.extend(profile.application_transports)
            for application in profile.applications:
                if application.name not in user_defined_app_names:
                    services = EosCliConfigGen.Metadata.CvPathfinder.Applications.ProfilesItem.BuiltinApplicationsItem.Services()
                    if application.service is not None:
                        services.append_new(application.service)
                    application_profile.builtin_applications.append_new(name=application.name, services=services)
                else:
                    application_profile.user_defined_applications.append_new(name=application.name)
            for category in profile.categories:
                services = EosCliConfigGen.Metadata.CvPathfinder.Applications.ProfilesItem.CategoriesItem.Services()
                if category.service is not None:
                    services.append_new(category.service)
                application_profile.categories.append_new(category=category.name, services=services)
            self.structured_config.metadata.cv_pathfinder.applications.profiles.append(application_profile)
        for category in categories:
            for application in category.applications:
                if application.name not in user_defined_app_names:
                    services = EosCliConfigGen.Metadata.CvPathfinder.Applications.Categories.BuiltinApplicationsItem.Services()
                    if application.service is not None:
                        services.append_new(application.service)
                    self.structured_config.metadata.cv_pathfinder.applications.categories.builtin_applications.append_new(
                        name=application.name, category=category.name, services=services
                    )

                if application.name in user_defined_app_names:
                    self.structured_config.metadata.cv_pathfinder.applications.categories.user_defined_applications.append_new(
                        name=application.name, category=category.name
                    )
