# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.plugin_utils.utils import append_if_not_duplicate, get, get_item

from .utils import UtilsMixin


class ApplicationTrafficRecognitionMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    @cached_property
    def application_traffic_recognition(self) -> dict | None:
        """
        Return structured config for application_traffic_recognition if `wan_role` is not None
        """
        if not self.shared_utils.wan_role:
            return None

        return self._filtered_application_traffic_recognition or None

    @cached_property
    def _filtered_application_traffic_recognition(self) -> dict:
        """
        Based on the filtered policies local to the device, filter which application profiles should be configured on the device.

        Supports only `application_traffic_recognition.applications.ipv4_applications` for now.

        For applications - the existence cannot be verified as there are 4000+ applications built-in in the DPI engine used by EOS.
        """
        input_application_traffic_recognition = get(self._hostvars, "application_traffic_recognition", {})
        # Application profiles first
        application_profiles = []
        # TODO inject "application_profile": "CONTROL-PLANE-APPLICATION-PROFILE",

        def _append_object_to_list_of_dicts(path: str, obj_name: str, list_of_dicts: list, message: str | None = None, required=True) -> None:
            """
            Helper function
            Technically impossible to get a duplicate, just reusing the methode when the same applicaiton is used in multiple places
            """
            if (
                obj := get_item(
                    get(input_application_traffic_recognition, path, default=[]),
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
            for application_virtual_topology in get(policy, "application_virtual_topologies", []):
                application_profile = get(application_virtual_topology, "application_profile", required=True)
                _append_object_to_list_of_dicts(
                    path="application_profiles",
                    obj_name=application_profile,
                    list_of_dicts=application_profiles,
                    message=(
                        f"The application profile {application_profile} used in one of the policies "
                        "is not defined in 'application_traffic_recognition.application_profiles'."
                    ),
                )
            default_virtual_topology = get(policy, "default_virtual_topology", required=True)
            if not get(default_virtual_topology, "drop_unmatched", default=False):
                application_profile = get(default_virtual_topology, "application_profile", default="default")
                if application_profile != "default":
                    _append_object_to_list_of_dicts(
                        path="application_profiles",
                        obj_name=application_profile,
                        list_of_dicts=application_profiles,
                        message=(
                            f"The application profile {application_profile} used in one of the policies "
                            "is not defined in 'application_traffic_recognition.application_profiles'."
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
                        "undefined in 'application_traffic_recognition.categories'."
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
                        "is undefined in 'application_traffic_recognition.fields_sets.ipv4_prefixes'."
                    ),
                )
            if (dest_prefix_set_name := get(application, "dest_prefix_set_name")) is not None:
                _append_object_to_list_of_dicts(
                    path="field_sets.ipv4_prefixes",
                    obj_name=dest_prefix_set_name,
                    list_of_dicts=ipv4_prefixes,
                    message=(
                        f"The IPv4 prefix field set {dest_prefix_set_name} used in the application {application} "
                        "is undefined in 'application_traffic_recognition.fields_sets.ipv4_prefixes'."
                    ),
                )
            if (udp_src_port_set_name := get(application, "udp_src_port_set_name")) is not None:
                _append_object_to_list_of_dicts(
                    path="field_sets.l4_ports",
                    obj_name=udp_src_port_set_name,
                    list_of_dicts=l4_ports,
                    message=(
                        f"The L4 Ports field set {udp_src_port_set_name} used in the application {application} "
                        "is undefined in 'application_traffic_recognition.fields_sets.l4_ports'."
                    ),
                )
            if (udp_dest_port_set_name := get(application, "udp_dest_port_set_name")) is not None:
                _append_object_to_list_of_dicts(
                    path="field_sets.l4_ports",
                    obj_name=udp_dest_port_set_name,
                    list_of_dicts=l4_ports,
                    message=(
                        f"The L4 Ports field set {udp_dest_port_set_name} used in the application {application} "
                        "is undefined in 'application_traffic_recognition.fields_sets.l4_ports'."
                    ),
                )
            if (tcp_src_port_set_name := get(application, "tcp_src_port_set_name")) is not None:
                _append_object_to_list_of_dicts(
                    path="field_sets.l4_ports",
                    obj_name=tcp_src_port_set_name,
                    list_of_dicts=l4_ports,
                    message=(
                        f"The L4 Ports field set {tcp_src_port_set_name} used in the application {application} "
                        "is undefined in 'application_traffic_recognition.fields_sets.l4_ports'."
                    ),
                )
            if (tcp_dest_port_set_name := get(application, "tcp_dest_port_set_name")) is not None:
                _append_object_to_list_of_dicts(
                    path="field_sets.l4_ports",
                    obj_name=tcp_dest_port_set_name,
                    list_of_dicts=l4_ports,
                    message=(
                        f"The L4 Ports field set {tcp_dest_port_set_name} used in the application {application} "
                        "is undefined in 'application_traffic_recognition.fields_sets.l4_ports'."
                    ),
                )

        output["field_sets"] = {
            "l4_ports": l4_ports,
            "ipv4_prefixes": ipv4_prefixes,
        }

        return output
