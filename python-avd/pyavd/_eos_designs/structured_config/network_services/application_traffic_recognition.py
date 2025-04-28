# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Final, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.schema import EosDesigns
from pyavd._errors import AristaAvdInvalidInputsError

if TYPE_CHECKING:
    from . import AvdStructuredConfigNetworkServicesProtocol


class ApplicationTrafficRecognitionMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    DEFAULT_WAN_CONTROL_PLANE_APPLICATION_NAME: Final[str] = "APP-CONTROL-PLANE"
    DEFAULT_WAN_CONTROL_PLANE_APP_DST_PREFIX_NAME: Final[str] = "PFX-PATHFINDERS"
    DEFAULT_WAN_CONTROL_PLANE_APP_SRC_PREFIX_NAME: Final[str] = "PFX-LOCAL-VTEP-IP"

    def _set_virtual_topology_application_classification(
        self: AvdStructuredConfigNetworkServicesProtocol,
        virtual_topology: EosDesigns.WanVirtualTopologies.PoliciesItem.ApplicationVirtualTopologiesItem
        | EosDesigns.WanVirtualTopologies.PoliciesItem.DefaultVirtualTopology
        | EosDesigns.WanVirtualTopologies.ControlPlaneVirtualTopology,
        policy_name: str,
    ) -> None:
        """
        Set the application-profiles, applications, categories and field sets relevant to the virtual topology in structured config.

        Supports only `application_classification.applications.ipv4_applications` for now.

        For applications - the existence cannot be verified as there are 4000+ applications built-in in the DPI engine used by EOS.
        """
        atr = EosCliConfigGen.ApplicationTrafficRecognition()
        """Keeping a local version used to store the local object as we traverse them."""
        is_control_plane_vt = isinstance(virtual_topology, EosDesigns.WanVirtualTopologies.ControlPlaneVirtualTopology)
        """Boolean to track if we are dealing with the Control-Plane Virtual Topology to inject defaults object where required."""

        if virtual_topology.application_profile not in self.inputs.application_classification.application_profiles:
            if is_control_plane_vt:
                # use default application profile
                atr.application_profiles.append(self.get_default_control_plane_application_profile())
            else:
                msg = (
                    f"Application Profile '{virtual_topology.application_profile}' referenced in policy '{policy_name}' "
                    "is not defined in 'application_classification.application_profiles'."
                )
                raise AristaAvdInvalidInputsError(msg)

        else:
            atr.application_profiles.append(self.inputs.application_classification.application_profiles[virtual_topology.application_profile])

        # set the applications and categories in the atr object.
        self._update_applications_and_categories(atr, is_control_plane_vt=is_control_plane_vt)
        # Set categories and applications in structured config

        # Update the field sets from applications in the atr object
        self._update_field_sets(atr, is_control_plane_vt=is_control_plane_vt)

        # deepmerge the atr object in the structured_config
        self.structured_config.application_traffic_recognition._deepmerge(atr)

    def _update_applications_and_categories(
        self: AvdStructuredConfigNetworkServicesProtocol, atr: EosCliConfigGen.ApplicationTrafficRecognition, *, is_control_plane_vt: bool
    ) -> None:
        """
        Update the IPv4 applications and categories in the atr based on the Application Profile in atr.

        The way the module is build, there is only one Application-profile in the atr object.

        Args:
            atr: The ApplicationTrafficRecognition object local to the module to track the set objects
            is_control_plane_vt: Indicates if we are setting up the ApplicationTrafficRecognition for Control-Plane Virtual Topology
        """
        application_profile = next(iter(atr.application_profiles))

        # Categories in application profile
        for category in application_profile.categories:
            if category.name not in self.inputs.application_classification.categories:
                msg = (
                    f"Category '{category.name}' referenced in the Application Profile '{application_profile.name}' "
                    "is not defined in 'application_classification.categories'."
                )
                raise AristaAvdInvalidInputsError(msg)

            atr.categories.append(self.inputs.application_classification.categories[category.name])

        # Applications in application profiles
        for application in application_profile.applications:
            if application.name in self.inputs.application_classification.applications.ipv4_applications:
                atr.applications.ipv4_applications.append(self.inputs.application_classification.applications.ipv4_applications[application.name])

            elif is_control_plane_vt and application.name == self.DEFAULT_WAN_CONTROL_PLANE_APPLICATION_NAME:
                # the default Control Plane application profile has one application.
                atr.applications.ipv4_applications.append(self.get_default_control_plane_application())

        # Applications in categories
        for category in atr.categories:
            for application in category.applications:
                if application.name in self.inputs.application_classification.applications.ipv4_applications:
                    atr.applications.ipv4_applications.append(self.inputs.application_classification.applications.ipv4_applications[application.name])

    def _update_field_sets(
        self: AvdStructuredConfigNetworkServicesProtocol, atr: EosCliConfigGen.ApplicationTrafficRecognition, *, is_control_plane_vt: bool
    ) -> None:
        """
        Update the IPv4 prefix and port field sets in the atr object base on the IPv4 Applications in atr.

        Args:
            atr: The ApplicationTrafficRecognition object local to the module to track the set objects
            is_control_plane_vt: Indicates if we are setting up the ApplicationTrafficRecognition for Control-Plane Virtual Topology
        """
        for application in atr.applications.ipv4_applications:
            # prefix sets
            if application.src_prefix_set_name:
                self._update_prefix_set(atr, application.src_prefix_set_name, application.name, is_control_plane_vt=is_control_plane_vt)
            if application.dest_prefix_set_name:
                self._update_prefix_set(atr, application.dest_prefix_set_name, application.name, is_control_plane_vt=is_control_plane_vt)

            # port sets
            for port_set_name in (
                application.udp_src_port_set_name,
                application.udp_dest_port_set_name,
                application.tcp_src_port_set_name,
                application.tcp_dest_port_set_name,
            ):
                if not port_set_name:
                    continue
                self._update_port_set(atr, port_set_name, application.name)

    def _update_prefix_set(
        self: AvdStructuredConfigNetworkServicesProtocol,
        atr: EosCliConfigGen.ApplicationTrafficRecognition,
        prefix_set_name: str,
        application_name: str,
        *,
        is_control_plane_vt: bool,
    ) -> None:
        """
        Update atr with the prefix set.

        Default Application Profile for control plane uses prefix sets.

        Args:
            atr: The ApplicationTrafficRecognition object local to the module to track the set objects
            prefix_set_name: Name of the prefix set to configure
            application_name: Name of the application to use in error message
            is_control_plane_vt: Indicates if we are setting up the ApplicationTrafficRecognition for Control-Plane Virtual Topology

        Raises:
            AristaAvdInvalidInputsError: if the prefix-set name is not the appropriate control-plane one and is not present in the inputs.
        """
        if prefix_set_name in self.inputs.application_classification.field_sets.ipv4_prefixes:
            atr.field_sets.ipv4_prefixes.append(self.inputs.application_classification.field_sets.ipv4_prefixes[prefix_set_name])
        elif is_control_plane_vt and (
            (self.shared_utils.is_wan_client and prefix_set_name == self.DEFAULT_WAN_CONTROL_PLANE_APP_DST_PREFIX_NAME)
            or (self.shared_utils.is_wan_server and prefix_set_name == self.DEFAULT_WAN_CONTROL_PLANE_APP_SRC_PREFIX_NAME)
        ):
            # use default prefix-set
            atr.field_sets.ipv4_prefixes.append(self.get_default_control_plane_prefix_set())
        else:
            msg = (
                f"IPv4 prefix field set '{prefix_set_name}' referenced in the application '{application_name}' "
                "is not defined in 'application_classification.fields_sets.ipv4_prefixes'."
            )
            raise AristaAvdInvalidInputsError(msg)

    def _update_port_set(
        self: AvdStructuredConfigNetworkServicesProtocol, atr: EosCliConfigGen.ApplicationTrafficRecognition, port_set_name: str, application_name: str
    ) -> None:
        """
        Update atr with the port set.

        Args:
            atr: The ApplicationTrafficRecognition object local to the module to track the set objects
            port_set_name: Name of the port set to configure
            application_name: Name of the application to use in error message

        Raises:
            AristaAvdInvalidInputsError: if the port-set name is not present in the inputs.
        """
        if port_set_name not in self.inputs.application_classification.field_sets.l4_ports:
            msg = (
                f"L4 Ports field set '{port_set_name}' referenced in the application '{application_name}' "
                "is not defined in 'application_classification.fields_sets.l4_ports'."
            )
            raise AristaAvdInvalidInputsError(msg)

        atr.field_sets.l4_ports.append(self.inputs.application_classification.field_sets.l4_ports[port_set_name])

    def get_default_control_plane_application_profile(
        self: AvdStructuredConfigNetworkServicesProtocol,
    ) -> EosCliConfigGen.ApplicationTrafficRecognition.ApplicationProfilesItem:
        """
        Return the default application profile for control-plane.

        The default name is defined in the schema.

        This is the same for all WAN routers:

        application_traffic_recognition:
          application_profiles:
            - name: APP-PROFILE-CONTROL-PLANE
              applications:
                - name: APP-CONTROL-PLANE
        """
        application_profile = EosCliConfigGen.ApplicationTrafficRecognition.ApplicationProfilesItem(
            name=self.inputs.wan_virtual_topologies.control_plane_virtual_topology.application_profile
        )
        application_profile.applications.append_new(name=self.DEFAULT_WAN_CONTROL_PLANE_APPLICATION_NAME)
        return application_profile

    def get_default_control_plane_application(
        self: AvdStructuredConfigNetworkServicesProtocol,
    ) -> EosCliConfigGen.ApplicationTrafficRecognition.Applications.Ipv4ApplicationsItem:
        """
        Return the default application for control-plane.

        Edge and Transit

            application_traffic_recognition:
              applications:
                ipv4_applications:
                  - name: APP-CONTROL-PLANE
                    dest_prefix_set_name: PFX-PATHFINDERS

        Pathfinder:

            application_traffic_recognition:
              applications:
                ipv4_applications:
                  - name: APP-CONTROL-PLANE
                    src_prefix_set_name: PFX-LOCAL-VTEP-IP

        """
        application = EosCliConfigGen.ApplicationTrafficRecognition.Applications.Ipv4ApplicationsItem(name=self.DEFAULT_WAN_CONTROL_PLANE_APPLICATION_NAME)
        if self.shared_utils.is_wan_client:
            application.dest_prefix_set_name = self.DEFAULT_WAN_CONTROL_PLANE_APP_DST_PREFIX_NAME
        else:  # self.shared_utils.is_wan_server
            application.src_prefix_set_name = self.DEFAULT_WAN_CONTROL_PLANE_APP_SRC_PREFIX_NAME

        return application

    def get_default_control_plane_prefix_set(
        self: AvdStructuredConfigNetworkServicesProtocol,
    ) -> EosCliConfigGen.ApplicationTrafficRecognition.FieldSets.Ipv4PrefixesItem:
        """
        Return the default prefix-set for control-plane.

        * the device Pathfinders vtep_ips as destination for non Pathfinders.
        * the device Pathfinder vtep_ip as source.

        Edge and Transit:

            application_traffic_recognition:
              field_sets:
                ipv4_prefixes:
                  - name: PFX-PATHFINDERS
                    prefix_values: [Pathfinder to which the router is connected vtep_ips]

        Pathfinder:

            application_traffic_recognition:
              field_sets:
                ipv4_prefixes:
                  - name: PFX-LOCAL-VTEP-IP
                    prefix_values: [Pathfinder vtep_ip]

        """
        if self.shared_utils.is_wan_client:
            name = self.DEFAULT_WAN_CONTROL_PLANE_APP_DST_PREFIX_NAME
            prefix_set_values = [f"{wan_rs.vtep_ip}/32" for wan_rs in self.shared_utils.filtered_wan_route_servers]
        else:  # self.shared_utils.is_wan_server:
            name = self.DEFAULT_WAN_CONTROL_PLANE_APP_SRC_PREFIX_NAME
            prefix_set_values = [f"{self.shared_utils.vtep_ip}/32"]

        return EosCliConfigGen.ApplicationTrafficRecognition.FieldSets.Ipv4PrefixesItem(
            name=name, prefix_values=EosCliConfigGen.ApplicationTrafficRecognition.FieldSets.Ipv4PrefixesItem.PrefixValues(prefix_set_values)
        )
