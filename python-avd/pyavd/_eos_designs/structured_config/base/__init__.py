# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.structured_config.structured_config_generator import (
    StructuredConfigGenerator,
    StructuredConfigGeneratorProtocol,
    structured_config_contributor,
)
from pyavd._errors import AristaAvdInvalidInputsError
from pyavd._utils import get_v2
from pyavd.j2filters import natural_sort

from .aaa_settings import AaaSettingsMixin
from .address_locking import AddressLockingMixin
from .daemon_terminattr import DaemonTerminattrMixin
from .dns_settings import DnsSettingsMixin
from .dot1x import Dot1xMixin
from .errdisable import ErrDisableMixin
from .logging import LoggingMixin
from .management_ssh import ManagementSshMixin
from .monitor_connectivity import MonitorConnectivityMixin
from .monitor_sessions import MonitorSessionsMixin
from .ntp import NtpMixin
from .platform_mixin import PlatformMixin
from .ptp import PtpMixin
from .router_bgp import RouterBgpMixin
from .router_general import RouterGeneralMixin
from .snmp_server import SnmpServerMixin
from .utils import UtilsMixin


class AvdStructuredConfigBaseProtocol(
    AaaSettingsMixin,
    AddressLockingMixin,
    DaemonTerminattrMixin,
    DnsSettingsMixin,
    Dot1xMixin,
    ErrDisableMixin,
    LoggingMixin,
    ManagementSshMixin,
    MonitorConnectivityMixin,
    NtpMixin,
    PtpMixin,
    SnmpServerMixin,
    RouterBgpMixin,
    RouterGeneralMixin,
    PlatformMixin,
    MonitorSessionsMixin,
    UtilsMixin,
    StructuredConfigGeneratorProtocol,
    Protocol,
):
    """
    Protocol for the AvdStructuredConfig Class, which is imported by "get_structured_config" to render parts of the structured config.

    "get_structured_config" imports, instantiates and run the .render() method on the class.
    .render() runs all class methods not starting with _ and of type @cached property and inserts the returned data into
    a dict with the name of the method as key. This means that each key in the final dict corresponds to a method.

    The Class uses StructuredConfigGenerator, as the base class, to inherit the _hostvars, keys and other attributes.
    Other methods are included as "Mixins" to make the files more manageable.

    The order of the @cached_properties methods imported from Mixins will also control the order in the output.
    """

    @structured_config_contributor
    def hostname(self) -> None:
        self.structured_config.hostname = self.shared_utils.hostname

    @structured_config_contributor
    def static_routes(self) -> None:
        """static_routes set based on mgmt_gateway, mgmt_destination_networks and mgmt_interface_vrf."""
        # Skip static routes if mgmt_ip is set to "dhcp" and avd_design_future.accept_dhcp_default_route_for_mgmt_ip_dhcp: true,
        # since DHCP will provide the default route
        if self.shared_utils.node_config.mgmt_ip == "dhcp" and self.inputs.avd_design_future.accept_dhcp_default_route_for_mgmt_ip_dhcp:
            return

        if self.shared_utils.mgmt_gateway is None:
            return

        if self.inputs.mgmt_destination_networks:
            for mgmt_destination_network in self.inputs.mgmt_destination_networks:
                self.structured_config.static_routes.append_new(
                    vrf=self.inputs.mgmt_interface_vrf, prefix=mgmt_destination_network, next_hop=self.shared_utils.mgmt_gateway
                )
        else:
            self.structured_config.static_routes.append_new(vrf=self.inputs.mgmt_interface_vrf, prefix="0.0.0.0/0", next_hop=self.shared_utils.mgmt_gateway)

    @structured_config_contributor
    def ipv6_static_routes(self) -> None:
        """ipv6_static_routes set based on ipv6_mgmt_gateway, ipv6_mgmt_destination_networks and mgmt_interface_vrf."""
        if self.shared_utils.ipv6_mgmt_gateway is None or self.shared_utils.node_config.ipv6_mgmt_ip is None:
            return

        if self.inputs.ipv6_mgmt_destination_networks:
            for mgmt_destination_network in self.inputs.ipv6_mgmt_destination_networks:
                self.structured_config.ipv6_static_routes.append_new(
                    vrf=self.inputs.mgmt_interface_vrf, prefix=mgmt_destination_network, next_hop=self.shared_utils.ipv6_mgmt_gateway
                )
            return

        self.structured_config.ipv6_static_routes.append_new(vrf=self.inputs.mgmt_interface_vrf, prefix="::/0", next_hop=self.shared_utils.ipv6_mgmt_gateway)

    @structured_config_contributor
    def service_routing_protocols_model(self) -> None:
        """service_routing_protocols_model set to 'multi-agent'."""
        self.structured_config.service_routing_protocols_model = "multi-agent"

    @structured_config_contributor
    def ip_routing(self) -> None:
        """Set ip_routing, ip_routing_ipv6_interfaces and ipv6_unicast_routing based on underlay_rfc5549 variable."""
        if not self.shared_utils.underlay_router and not self.shared_utils.node_config.always_configure_ip_routing:
            return

        if self.inputs.underlay_rfc5549 or self.shared_utils.underlay_ipv6:
            self.structured_config.ipv6_unicast_routing = True
        if self.inputs.underlay_rfc5549:
            self.structured_config.ip_routing_ipv6_interfaces = True
        else:
            self.structured_config.ip_routing = True

    @structured_config_contributor
    def router_multicast(self) -> None:
        """router_multicast set based on underlay_multicast_<>, underlay_router and switch.evpn_multicast facts."""
        if not self.shared_utils.any_multicast_enabled:
            return

        self.structured_config.router_multicast.ipv4.routing = True
        if self.shared_utils.evpn_multicast:
            self.structured_config.router_multicast.ipv4.software_forwarding = "sfe"

    @structured_config_contributor
    def hardware_counters(self) -> None:
        """
        Set hardware_counters.

        Contributing data sources:
          - hardware_counters.features variable.
          - platform_settings.feature_support.hardware_counters fact.
          - platform_settings.feature_support.hardware_counter_features fact.
        """
        if not self.inputs.hardware_counters:
            return
        if not self.shared_utils.platform_settings.feature_support.hardware_counters:
            # Since we use the same data model in eos_cli_config_gen, it would pick up the input vars unless we explicitly set it to null.
            self.custom_structured_configs.nested.hardware_counters = EosCliConfigGen.HardwareCounters._from_null()
            return
        hardware_counters = self.inputs.hardware_counters._deepcopy()

        # Filter different hardware counter features based on the platform supportability
        hardware_counters.features = hardware_counters.features._filtered(
            lambda feature: get_v2(
                self.shared_utils.platform_settings.feature_support.hardware_counter_features,
                feature.name.replace(" ", "_").replace("-", "_"),
                # Assume all uncovered/new features are supported
                default=True,
            )
        )
        # Use case where all specific features are filtered out leaving an empty list
        if not hardware_counters.features:
            # Since we use the same data model in eos_cli_config_gen, it would pick up the input vars unless we explicitly set it to null.
            self.custom_structured_configs.nested.hardware_counters.features = EosCliConfigGen.HardwareCounters.Features._from_null()
            return

        self.structured_config.hardware_counters = hardware_counters

    @structured_config_contributor
    def hardware(self) -> None:
        """
        Hardware set based on platform_speed_groups variable and switch.platform fact.

        Converting nested dict to list of dict to support avd_v4.0.
        """
        if not self.shared_utils.platform_settings.feature_support.hardware_speed_group:
            return
        platform_speed_groups = self.inputs.platform_speed_groups
        switch_platform = self.shared_utils.platform
        if not platform_speed_groups or switch_platform is None:
            return

        if switch_platform not in platform_speed_groups:
            return

        tmp_speed_groups = {}
        for speed in platform_speed_groups[switch_platform].speeds._natural_sorted():
            for speed_group in speed.speed_groups:
                tmp_speed_groups[speed_group] = speed.speed

        if tmp_speed_groups:
            for speed_group in natural_sort(tmp_speed_groups):
                self.structured_config.hardware.speed_groups.append_new(speed_group=speed_group, serdes=tmp_speed_groups[speed_group])

    @structured_config_contributor
    def vlan_internal_order(self) -> None:
        """
        vlan_internal_order set based on internal_vlan_order data-model.

        TODO: Add platform_setting to control this.
        """
        if self.shared_utils.wan_role:
            return

        self.structured_config.vlan_internal_order = self.inputs.internal_vlan_order._cast_as(EosCliConfigGen.VlanInternalOrder)

    @structured_config_contributor
    def config_end(self) -> None:
        """config_end is always set to match EOS default config and historic configs."""
        self.structured_config.config_end = True

    @structured_config_contributor
    def transceiver_qsfp_default_mode_4x10(self) -> None:
        """
        transceiver_qsfp_default_mode_4x10 is on for all devices except WAN routers.

        TODO: Add platform_setting to control this.
        """
        self.structured_config.transceiver_qsfp_default_mode_4x10 = not self.shared_utils.is_wan_router

    @structured_config_contributor
    def event_monitor(self) -> None:
        """event_monitor set based on event_monitor data-model."""
        self.structured_config.event_monitor = self.inputs.event_monitor

    @structured_config_contributor
    def event_handlers(self) -> None:
        """event_handlers set based on event_handlers data-model."""
        self.structured_config.event_handlers = self.inputs.event_handlers

    @structured_config_contributor
    def load_interval(self) -> None:
        """load_interval set based on load_interval_default variable."""
        self.structured_config.load_interval = self.inputs.load_interval

    @structured_config_contributor
    def queue_monitor_length(self) -> None:
        """
        Set queue_monitor_length.

        Contributing data sources:
          - queue_monitor_length data-model
          - platform_settings.feature_support.queue_monitor fact
          - platform_settings.feature_support.queue_monitor_length_notify fact.
        """
        if not self.inputs.queue_monitor_length:
            return
        if not self.shared_utils.platform_settings.feature_support.queue_monitor:
            # Since we use the same data model in eos_cli_config_gen, it would pick up the input vars unless we explicitly set it to null.
            self.custom_structured_configs.nested.queue_monitor_length = EosCliConfigGen.QueueMonitorLength._from_null()
            return

        # Remove notifying key if not supported by the platform settings.
        queue_monitor_length = self.inputs.queue_monitor_length._cast_as(EosCliConfigGen.QueueMonitorLength)
        if not self.shared_utils.platform_settings.feature_support.queue_monitor_length_notify and queue_monitor_length.notifying:
            del queue_monitor_length.notifying
        self.structured_config.queue_monitor_length = queue_monitor_length

    @structured_config_contributor
    def redundancy(self) -> None:
        """Redundancy set based on redundancy data-model."""
        if self.inputs.redundancy.protocol:
            self.structured_config.redundancy.protocol = self.inputs.redundancy.protocol

    @structured_config_contributor
    def interface_defaults(self) -> None:
        """interface_defaults set based on default_interface_mtu."""
        if self.shared_utils.default_interface_mtu is not None:
            self.structured_config.interface_defaults.mtu = self.shared_utils.default_interface_mtu
        if self.inputs.general_settings.interface_defaults.ethernet_shutdown:
            self.structured_config.interface_defaults.ethernet.shutdown = True

    @structured_config_contributor
    def spanning_tree(self) -> None:
        """spanning_tree set based on spanning_tree_root_super, spanning_tree_mode and spanning_tree_priority."""
        if not self.shared_utils.network_services_l2:
            self.structured_config.spanning_tree.mode = "none"
            return

        spanning_tree_mode = self.shared_utils.node_config.spanning_tree_mode

        if self.shared_utils.node_config.spanning_tree_root_super is True:
            self.structured_config.spanning_tree.root_super = True

        if self.shared_utils.node_config.spanning_tree_mst_pvst_boundary:
            self.structured_config.spanning_tree.mst.pvst_border = True

        if stp_po_range := self.shared_utils.node_config.spanning_tree_port_id_allocation_port_channel_range:
            self.structured_config.spanning_tree.port_id_allocation_port_channel_range = stp_po_range

        if spanning_tree_mode is not None:
            self.structured_config.spanning_tree.mode = spanning_tree_mode
            priority = self.shared_utils.node_config.spanning_tree_priority
            # "rapid-pvst" is not included below. Per vlan spanning-tree priorities are set under network-services.
            if spanning_tree_mode == "mstp":
                self.structured_config.spanning_tree.mst_instances.append_new(id="0", priority=priority)
            elif spanning_tree_mode == "rstp":
                self.structured_config.spanning_tree.rstp_priority = priority

    @structured_config_contributor
    def service_unsupported_transceiver(self) -> None:
        """service_unsupported_transceiver based on unsupported_transceiver data-model."""
        self.structured_config.service_unsupported_transceiver = self.inputs.unsupported_transceiver

    @structured_config_contributor
    def clock(self) -> None:
        """Clock set based on timezone variable."""
        if self.inputs.timezone:
            self.structured_config.clock.timezone = self.inputs.timezone

    @structured_config_contributor
    def vrfs(self) -> None:
        """Vrfs set based on mgmt_interface_vrf variable."""
        vrf_settings = EosCliConfigGen.VrfsItem(name=self.inputs.mgmt_interface_vrf, ip_routing=self.inputs.mgmt_vrf_routing)

        if self.shared_utils.node_config.ipv6_mgmt_ip is not None:
            vrf_settings.ipv6_routing = self.inputs.mgmt_vrf_routing
        self.structured_config.vrfs.append(vrf_settings)

    @structured_config_contributor
    def management_interfaces(self) -> None:
        """management_interfaces set based on mgmt_interface, mgmt_ip, ipv6_mgmt_ip facts, mgmt_gateway, ipv6_mgmt_gateway and mgmt_interface_vrf variables."""
        if self.shared_utils.node_config.mgmt_ip or self.shared_utils.node_config.ipv6_mgmt_ip:
            # Check if mgmt_ip is set to "dhcp"
            is_dhcp = self.shared_utils.node_config.mgmt_ip == "dhcp"

            interface_settings = EosCliConfigGen.ManagementInterfacesItem(
                name=self.shared_utils.mgmt_interface,
                description=self.inputs.mgmt_interface_description,
                shutdown=False,
                vrf=self.inputs.mgmt_interface_vrf,
                ip_address=self.shared_utils.node_config.mgmt_ip,
                type="oob",
            )

            # For DHCP, automatically accept default route instead of using gateway
            if is_dhcp and self.inputs.avd_design_future.accept_dhcp_default_route_for_mgmt_ip_dhcp:
                interface_settings.dhcp_client_accept_default_route = True
            else:
                # For static IP, set gateway (metadata field, actual routing done via static_routes)
                interface_settings.gateway = self.shared_utils.mgmt_gateway

            """
            inserting ipv6 variables if ipv6_mgmt_ip is set
            """
            if self.shared_utils.node_config.ipv6_mgmt_ip:
                interface_settings._update(
                    ipv6_enable=True,
                    ipv6_gateway=self.shared_utils.ipv6_mgmt_gateway,
                )
                interface_settings.ipv6_addresses.append(self.shared_utils.node_config.ipv6_mgmt_ip)
            self.structured_config.management_interfaces.append(interface_settings)

    @structured_config_contributor
    def management_security(self) -> None:
        """Set the structured config for management_security."""
        self.structured_config.management_security.entropy_sources = self.shared_utils.platform_settings.security_entropy_sources._cast_as(
            EosCliConfigGen.ManagementSecurity.EntropySources
        )

    @structured_config_contributor
    def tcam_profile(self) -> None:
        """tcam_profile set based on platform_settings.tcam_profile fact."""
        if tcam_profile := self.shared_utils.platform_settings.tcam_profile:
            self.structured_config.tcam_profile.system = tcam_profile

    @structured_config_contributor
    def mac_address_table(self) -> None:
        """mac_address_table set based on mac_address_table data-model."""
        self.structured_config.mac_address_table = self.inputs.mac_address_table

    @structured_config_contributor
    def queue_monitor_streaming(self) -> None:
        """queue_monitor_streaming set based on queue_monitor_streaming data-model and platform_settings.feature_support.queue_monitor fact."""
        if not self.inputs.queue_monitor_streaming:
            return
        if not self.shared_utils.platform_settings.feature_support.queue_monitor:
            # Since we use the same data model in eos_cli_config_gen, it would pick up the input vars unless we explicitly set it to null.
            self.custom_structured_configs.nested.queue_monitor_streaming = EosCliConfigGen.QueueMonitorStreaming._from_null()
            return
        self.structured_config.queue_monitor_streaming = self.inputs.queue_monitor_streaming

    @structured_config_contributor
    def management_api_http(self) -> None:
        """management_api_http set based on management_eapi data-model."""
        if self.inputs.management_eapi.enabled:
            self.structured_config.management_api_http._update(
                enable_http=self.inputs.management_eapi.enable_http,
                enable_https=self.inputs.management_eapi.enable_https,
                default_services=self.inputs.management_eapi.default_services,
            )

            for vrf in self.inputs.management_eapi.vrfs:
                if vrf.enabled:
                    vrf_name = self.shared_utils.get_vrf(vrf.name, context=f"self.inputs.management_eapi.vrfs[name={vrf.name}]")
                    self.structured_config.management_api_http.enable_vrfs.append_new(name=vrf_name, access_group=vrf.ipv4_acl, ipv6_access_group=vrf.ipv6_acl)

        # Enforce eAPI management access in default VRF for ACT Digital Twin if required
        if self._act_ensure_eapi_access:
            self.structured_config.management_api_http.enable_https = True
            # Create item for default VRF if not present. If present, remove IPv4 ACL.
            self.structured_config.management_api_http.enable_vrfs.obtain("default").access_group = None

    @structured_config_contributor
    def link_tracking_groups(self) -> None:
        """Set link_tracking_groups."""
        if link_tracking_groups := self.shared_utils.link_tracking_groups:
            self.structured_config.link_tracking_groups = link_tracking_groups

    @structured_config_contributor
    def lacp(self) -> None:
        """Lacp set based on lacp_port_id_range."""
        lacp_port_id_range = self.shared_utils.node_config.lacp_port_id_range
        if not lacp_port_id_range.enabled:
            return

        if (switch_id := self.shared_utils.id) is None:
            msg = f"'id' is not set on '{self.shared_utils.hostname}' to set LACP port ID ranges"
            raise AristaAvdInvalidInputsError(msg)

        node_group_length = max(len(self.shared_utils.node_group_config.nodes), 1) if self.shared_utils.node_group_config is not None else 1

        begin = 1 + (((switch_id - 1) % node_group_length) * lacp_port_id_range.size) + lacp_port_id_range.offset
        end = (((switch_id - 1) % node_group_length + 1) * lacp_port_id_range.size) + lacp_port_id_range.offset

        self.structured_config.lacp.port_id.range._update(begin=begin, end=end)

    @structured_config_contributor
    def eos_cli(self) -> None:
        """Aggregate the values of raw_eos_cli and platform_settings.platform_raw_eos_cli facts."""
        eos_cli = "\n".join(filter(None, [self.shared_utils.node_config.raw_eos_cli, self.shared_utils.platform_settings.raw_eos_cli]))
        if eos_cli:
            self.structured_config.eos_cli = eos_cli

    @structured_config_contributor
    def ip_ssh_client(self) -> None:
        """Parse source_interfaces.ssh_client and return list of source_interfaces."""
        if not (inputs := self.inputs.source_interfaces.ssh_client):
            return

        if source_interfaces := self._build_source_interfaces(
            inputs.mgmt_interface, inputs.inband_mgmt_interface, "IP SSH Client", output_type=EosCliConfigGen.IpSshClient
        ):
            self.structured_config.ip_ssh_client = source_interfaces

    @structured_config_contributor
    def ip_http_client(self) -> None:
        """Parse source_interfaces.http_client and set list of source_interfaces."""
        if not (inputs := self.inputs.source_interfaces.http_client):
            return

        if source_interfaces := self._build_source_interfaces(
            inputs.mgmt_interface, inputs.inband_mgmt_interface, "IP HTTP Client", output_type=EosCliConfigGen.IpHttpClient
        ):
            self.structured_config.ip_http_client = source_interfaces

    @structured_config_contributor
    def arp(self: AvdStructuredConfigBaseProtocol) -> None:
        """
        Set ARP configuration.

        ARP set based on "general_settings.arp" data-model.
        """
        if not (arp_settings := self.inputs.general_settings.arp):
            return

        self.structured_config.arp.persistent = arp_settings.persistent
        self.structured_config.arp.aging.timeout_default = arp_settings.aging.timeout_default

    @structured_config_contributor
    def ip_icmp_redirect(self: AvdStructuredConfigBaseProtocol) -> None:
        """
        Set IP ICMP redirect.

        IP ICMP redirect set based on "general_settings.ip_icmp_redirect" data-model.
        """
        self.structured_config.ip_icmp_redirect = self.inputs.general_settings.ip_icmp_redirect

    @structured_config_contributor
    def prefix_lists(self) -> None:
        self.structured_config.prefix_lists.extend(self.shared_utils.l3_bgp_prefix_lists)

    @structured_config_contributor
    def route_maps(self) -> None:
        self.structured_config.route_maps.extend(self.shared_utils.l3_bgp_route_maps)

    @structured_config_contributor
    def struct_cfgs(self) -> None:
        if self.shared_utils.platform_settings.structured_config:
            self.custom_structured_configs.root.append(self.shared_utils.platform_settings.structured_config)

    @cached_property
    def _act_ensure_eapi_access(self) -> bool:
        """Flag indicating if we are in ACT Digital Twin mode and if eAPI access in default VRF is enforced."""
        return self.shared_utils.digital_twin and self.inputs.digital_twin.environment == "act" and self.inputs.digital_twin.fabric.act_ensure_eapi_access

    @structured_config_contributor
    def management_settings(self) -> None:
        """Configures management settings based on the input data model."""
        if not (management_settings := self.inputs.management_settings):
            return

        # Apply management console settings
        if management_settings.console:
            self.structured_config.management_console = management_settings.console._cast_as(EosCliConfigGen.ManagementConsole)

        # Apply banner settings
        if management_settings.banners:
            self.structured_config.banners = management_settings.banners._cast_as(EosCliConfigGen.Banners)

    @structured_config_contributor
    def ip_dhcp_relay(self: AvdStructuredConfigBaseProtocol) -> None:
        """Set ip dhcp relay global configurations."""
        if not (relay_settings := self.inputs.general_settings.dhcp_relay):
            return

        if relay_settings.information_option:
            self.structured_config.ip_dhcp_relay.information_option = relay_settings.information_option

    @structured_config_contributor
    def dhcp_relay(self: AvdStructuredConfigBaseProtocol) -> None:
        """Set general relay agent configuration."""
        if not (relay_settings := self.inputs.general_settings.dhcp_relay):
            return

        if self.shared_utils.vtep:
            if relay_settings.tunnel_requests_disabled:
                self.structured_config.dhcp_relay.tunnel_requests_disabled = relay_settings.tunnel_requests_disabled
            if self.shared_utils.mlag and relay_settings.mlag_peerlink_requests_disabled:
                self.structured_config.dhcp_relay.mlag_peerlink_requests_disabled = relay_settings.mlag_peerlink_requests_disabled


class AvdStructuredConfigBase(StructuredConfigGenerator, AvdStructuredConfigBaseProtocol):
    """
    The AvdStructuredConfig Class is imported by "get_structured_config" to render parts of the structured config.

    "get_structured_config" imports, instantiates and run the .render() method on the class.
    .render() runs all class methods not starting with _ and of type @cached property and inserts the returned data into
    a dict with the name of the method as key. This means that each key in the final dict corresponds to a method.

    The Class uses StructuredConfigGenerator, as the base class, to inherit the _hostvars, keys and other attributes.
    Other methods are included as "Mixins" to make the files more manageable.

    The order of the @cached_properties methods imported from Mixins will also control the order in the output.
    """
