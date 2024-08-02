# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from pyavd._utils import append_if_not_duplicate, get, get_item, strip_empties_from_dict

from .utils import UtilsMixin

if TYPE_CHECKING:
    from . import AvdStructuredConfigNetworkServices


class ApplicationTrafficRecognitionMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def application_traffic_recognition(self: AvdStructuredConfigNetworkServices) -> dict | None:
        """Return structured config for application_traffic_recognition if wan router."""
        if not self.shared_utils.is_wan_router:
            return None

        filtered_application_classification = self._filtered_application_classification()

        self._generate_control_plane_application_profile(filtered_application_classification)

        return strip_empties_from_dict(filtered_application_classification)

    #  self._wan_control_plane_application_profile is defined in utils.py
    @cached_property
    def _wan_control_plane_application(self: AvdStructuredConfigNetworkServices) -> str:
        return "APP-CONTROL-PLANE"

    @cached_property
    def _wan_cp_app_dst_prefix(self: AvdStructuredConfigNetworkServices) -> str:
        return "PFX-PATHFINDERS"

    @cached_property
    def _wan_cp_app_src_prefix(self: AvdStructuredConfigNetworkServices) -> str:
        return "PFX-LOCAL-VTEP-IP"

    def _generate_control_plane_application_profile(self: AvdStructuredConfigNetworkServices, app_dict: dict) -> None:
        """
        Generate an application profile using a single application matching.

        * the device Pathfinders vtep_ips as destination for non Pathfinders.
        * the device Pathfinder vtep_ip as source.

        Create a structure as follow. If any object already exist, it is kept as defined by user and override the defaults.

        Edge and Transit:

            application_traffic_recognition:
              application_profiles:
                - name: APP-PROFILE-CONTROL-PLANE
                  applications:
                    - name: APP-CONTROL-PLANE
              applications:
                ipv4_applications:
                  - name: APP-CONTROL-PLANE
                    dest_prefix_set_name: PFX-PATHFINDERS
              field_sets:
                ipv4_prefixes:
                  - name: PFX-PATHFINDERS
                    prefix_values: [Pathfinder to which the router is connected vtep_ips]

        Pathfinder:

            application_traffic_recognition:
              application_profiles:
                - name: APP-PROFILE-CONTROL-PLANE
                  applications:
                    - name: APP-CONTROL-PLANE
              applications:
                ipv4_applications:
                  - name: APP-CONTROL-PLANE
                    src_prefix_set_name: PFX-LOCAL-VTEP-IP
              field_sets:
                ipv4_prefixes:
                  - name: PFX-LOCAL-VTEP-IP
                    prefix_values: [Pathfinder vtep_ip]
        """
        # Adding the application-profile
        application_profiles = get(app_dict, "application_profiles", [])
        if get_item(application_profiles, "name", self._wan_control_plane_application_profile_name) is not None:
            return
        app_dict.setdefault("application_profiles", []).append(
            {
                "name": self._wan_control_plane_application_profile_name,
                "applications": [
                    {
                        "name": self._wan_control_plane_application,
                    },
                ],
            },
        )
        # Adding the application
        ipv4_applications = get(app_dict, "applications.ipv4_applications", [])
        if get_item(ipv4_applications, "name", self._wan_control_plane_application) is not None:
            return
        if self.shared_utils.is_wan_client:
            app_dict.setdefault("applications", {}).setdefault("ipv4_applications", []).append(
                {
                    "name": self._wan_control_plane_application,
                    "dest_prefix_set_name": self._wan_cp_app_dst_prefix,
                },
            )
            # Adding the field-set based on the connected Pathfinder router-ids
            ipv4_prefixes_field_sets = get(app_dict, "field_sets.ipv4_prefixes", [])
            if get_item(ipv4_prefixes_field_sets, "name", self._wan_cp_app_dst_prefix) is not None:
                return
            pathfinder_vtep_ips = [f"{wan_rs_data.get('vtep_ip')}/32" for wan_rs, wan_rs_data in self.shared_utils.filtered_wan_route_servers.items()]
            app_dict.setdefault("field_sets", {}).setdefault("ipv4_prefixes", []).append(
                {
                    "name": self._wan_cp_app_dst_prefix,
                    "prefix_values": pathfinder_vtep_ips,
                },
            )
        elif self.shared_utils.is_wan_server:
            app_dict.setdefault("applications", {}).setdefault("ipv4_applications", []).append(
                {
                    "name": self._wan_control_plane_application,
                    "src_prefix_set_name": self._wan_cp_app_src_prefix,
                },
            )
            app_dict.setdefault("field_sets", {}).setdefault("ipv4_prefixes", []).append(
                {"name": self._wan_cp_app_src_prefix, "prefix_values": [f"{self.shared_utils.vtep_ip}/32"]},
            )

    def _filtered_application_classification(self: AvdStructuredConfigNetworkServices) -> dict:
        """
        Based on the filtered policies local to the device, filter which application profiles should be configured on the device.

        Supports only `application_classification.applications.ipv4_applications` for now.

        For applications - the existence cannot be verified as there are 4000+ applications built-in in the DPI engine used by EOS.
        """
        input_application_classification = get(self._hostvars, "application_classification", {})
        # Application profiles first
        application_profiles = []

        def _append_object_to_list_of_dicts(path: str, obj_name: str, list_of_dicts: list, message: str | None = None, *, required: bool = True) -> None:
            """
            Helper function.

            Technically impossible to get a duplicate, just reusing the method when the same application is used in multiple places.
            """
            if (
                obj := get_item(
                    get(input_application_classification, path, default=[]),
                    "name",
                    obj_name,
                    required=required,
                    custom_error_msg=message,
                )
            ) is None:
                return

            append_if_not_duplicate(
                list_of_dicts=list_of_dicts,
                primary_key="name",
                new_dict=obj,
                context="Application traffic recognition",
                context_keys=["name"],
            )

        for policy in self._filtered_wan_policies:
            if policy.get("is_default"):
                _append_object_to_list_of_dicts(
                    path="application_profiles",
                    obj_name=self._wan_control_plane_application_profile_name,
                    list_of_dicts=application_profiles,
                    required=False,
                )

            for match in get(policy, "matches", []):
                application_profile = get(match, "application_profile", required=True)
                if application_profile == self._wan_control_plane_application_profile_name:
                    # Special handling for control plane as it could be injected later.
                    _append_object_to_list_of_dicts(
                        path="application_profiles",
                        obj_name=application_profile,
                        list_of_dicts=application_profiles,
                        required=False,
                    )
                else:
                    _append_object_to_list_of_dicts(
                        path="application_profiles",
                        obj_name=application_profile,
                        list_of_dicts=application_profiles,
                        message=(
                            f"The application profile {application_profile} used in policy {policy['name']} "
                            "is not defined in 'application_classification.application_profiles'."
                        ),
                    )
            if (default_match := policy.get("default_match")) is not None:
                application_profile = get(default_match, "application_profile", default="default")
                if application_profile != "default":
                    _append_object_to_list_of_dicts(
                        path="application_profiles",
                        obj_name=application_profile,
                        list_of_dicts=application_profiles,
                        message=(
                            f"The application profile {application_profile} used in policy {policy['name']} "
                            "is not defined in 'application_classification.application_profiles'."
                        ),
                    )
        output = {"application_profiles": application_profiles}
        # Now handle categories, applicaations
        categories = []
        applications = []
        for application_profile in application_profiles:
            for category in get(application_profile, "categories", default=[]):
                _append_object_to_list_of_dicts(
                    path="categories",
                    obj_name=category["name"],
                    list_of_dicts=categories,
                    message=(
                        f"The application profile {application_profile['name']} uses the category {category['name']} "
                        "undefined in 'application_classification.categories'."
                    ),
                )
            # Applications in application profiles
            for application in get(application_profile, "applications", default=[]):
                _append_object_to_list_of_dicts(
                    path="applications.ipv4_applications",
                    obj_name=application["name"],
                    list_of_dicts=applications,
                    required=False,
                )
        # Applications in categories
        for category in categories:
            for application in get(category, "applications", default=[]):
                _append_object_to_list_of_dicts(
                    path="applications.ipv4_applications",
                    obj_name=application["name"],
                    list_of_dicts=applications,
                    required=False,
                )
        output["categories"] = categories
        # IPv4 only for now
        output["applications"] = {"ipv4_applications": applications}
        # Now filtering port sets and ipv4 sets
        l4_ports = []
        ipv4_prefixes = []
        for application in applications:
            if (src_prefix_set_name := get(application, "src_prefix_set_name")) is not None:
                _append_object_to_list_of_dicts(
                    path="field_sets.ipv4_prefixes",
                    obj_name=src_prefix_set_name,
                    list_of_dicts=ipv4_prefixes,
                    message=(
                        f"The IPv4 prefix field set {src_prefix_set_name} used in the application {application} "
                        "is undefined in 'application_classification.fields_sets.ipv4_prefixes'."
                    ),
                )
            if (dest_prefix_set_name := get(application, "dest_prefix_set_name")) is not None:
                _append_object_to_list_of_dicts(
                    path="field_sets.ipv4_prefixes",
                    obj_name=dest_prefix_set_name,
                    list_of_dicts=ipv4_prefixes,
                    message=(
                        f"The IPv4 prefix field set {dest_prefix_set_name} used in the application {application} "
                        "is undefined in 'application_classification.fields_sets.ipv4_prefixes'."
                    ),
                )
            if (udp_src_port_set_name := get(application, "udp_src_port_set_name")) is not None:
                _append_object_to_list_of_dicts(
                    path="field_sets.l4_ports",
                    obj_name=udp_src_port_set_name,
                    list_of_dicts=l4_ports,
                    message=(
                        f"The L4 Ports field set {udp_src_port_set_name} used in the application {application} "
                        "is undefined in 'application_classification.fields_sets.l4_ports'."
                    ),
                )
            if (udp_dest_port_set_name := get(application, "udp_dest_port_set_name")) is not None:
                _append_object_to_list_of_dicts(
                    path="field_sets.l4_ports",
                    obj_name=udp_dest_port_set_name,
                    list_of_dicts=l4_ports,
                    message=(
                        f"The L4 Ports field set {udp_dest_port_set_name} used in the application {application} "
                        "is undefined in 'application_classification.fields_sets.l4_ports'."
                    ),
                )
            if (tcp_src_port_set_name := get(application, "tcp_src_port_set_name")) is not None:
                _append_object_to_list_of_dicts(
                    path="field_sets.l4_ports",
                    obj_name=tcp_src_port_set_name,
                    list_of_dicts=l4_ports,
                    message=(
                        f"The L4 Ports field set {tcp_src_port_set_name} used in the application {application} "
                        "is undefined in 'application_classification.fields_sets.l4_ports'."
                    ),
                )
            if (tcp_dest_port_set_name := get(application, "tcp_dest_port_set_name")) is not None:
                _append_object_to_list_of_dicts(
                    path="field_sets.l4_ports",
                    obj_name=tcp_dest_port_set_name,
                    list_of_dicts=l4_ports,
                    message=(
                        f"The L4 Ports field set {tcp_dest_port_set_name} used in the application {application} "
                        "is undefined in 'application_classification.fields_sets.l4_ports'."
                    ),
                )

        output["field_sets"] = {
            "l4_ports": l4_ports,
            "ipv4_prefixes": ipv4_prefixes,
        }

        return output
