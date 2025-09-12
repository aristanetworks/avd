# Copyright (c) 2023-2025 Arista Networks, Inc.
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
from pyavd._utils import Undefined, default, get_v2
from pyavd.j2filters import natural_sort

from .address_locking import AddressLockingMixin
from .daemon_terminattr import DaemonTerminattrMixin
from .management_ssh import ManagementSshMixin
from .monitor_sessions import MonitorSessionsMixin
from .ntp import NtpMixin
from .platform_mixin import PlatformMixin
from .router_general import RouterGeneralMixin
from .snmp_server import SnmpServerMixin
from .utils import UtilsMixin


class AvdStructuredConfigBaseProtocol(
    AddressLockingMixin,
    DaemonTerminattrMixin,
    ManagementSshMixin,
    NtpMixin,
    SnmpServerMixin,
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
    def serial_number(self) -> None:
        """serial_number variable set based on serial_number fact."""
        self.structured_config.serial_number = self.shared_utils.serial_number

    @structured_config_contributor
    def router_bgp(self) -> None:
        """
        Set the structured config for router_bgp.

        router_bgp set based on switch.bgp_as, switch.bgp_defaults, router_id facts and aggregating the values of bgp_maximum_paths and bgp_ecmp variables.
        """
        if self.shared_utils.bgp_as is None:
            return

        platform_bgp_update_wait_for_convergence = self.shared_utils.platform_settings.feature_support.bgp_update_wait_for_convergence
        platform_bgp_update_wait_install = self.shared_utils.platform_settings.feature_support.bgp_update_wait_install

        if self.shared_utils.is_wan_router:
            # Special defaults for WAN routers
            default_maximum_paths = 16
            default_ecmp = None
        else:
            default_maximum_paths = 4
            default_ecmp = 4

        self.structured_config.router_bgp._update(
            router_id=self.shared_utils.router_id if not self.inputs.use_router_general_for_router_id else None, field_as=self.shared_utils.bgp_as
        )
        if bgp_defaults := self.shared_utils.node_config.bgp_defaults:
            self.structured_config.router_bgp.bgp_defaults = bgp_defaults._cast_as(EosCliConfigGen.RouterBgp.BgpDefaults)

        if bgp_distance := self.inputs.bgp_distance:
            self.structured_config.router_bgp.distance = bgp_distance

        self.structured_config.router_bgp.bgp.default.ipv4_unicast = self.inputs.bgp_default_ipv4_unicast
        self.structured_config.router_bgp.maximum_paths._update(
            paths=self.inputs.bgp_maximum_paths or default_maximum_paths, ecmp=self.inputs.bgp_ecmp or default_ecmp
        )

        if self.shared_utils.underlay_bgp or self.shared_utils.is_wan_router or self.shared_utils.l3_bgp_neighbors:
            self.structured_config.router_bgp.redistribute.connected.enabled = True
            if (self.shared_utils.overlay_routing_protocol != "none" or self.shared_utils.is_wan_router) and self.inputs.underlay_filter_redistribute_connected:
                # Use route-map for redistribution
                self.structured_config.router_bgp.redistribute.connected.route_map = "RM-CONN-2-BGP"

        if self.inputs.bgp_update_wait_for_convergence and platform_bgp_update_wait_for_convergence:
            self.structured_config.router_bgp.updates.wait_for_convergence = True

        if self.inputs.bgp_update_wait_install and platform_bgp_update_wait_install:
            self.structured_config.router_bgp.updates.wait_install = True

        if self.inputs.bgp_graceful_restart.enabled:
            self.structured_config.router_bgp.graceful_restart._update(enabled=True, restart_time=self.inputs.bgp_graceful_restart.restart_time)

        # Add neighbors
        self.structured_config.router_bgp.neighbors.extend(self.shared_utils.l3_bgp_neighbors)
        for neighbor in self.shared_utils.l3_bgp_neighbors:
            self.structured_config.router_bgp.address_family_ipv4.neighbors.append_new(ip_address=neighbor.ip_address, activate=True)

    @structured_config_contributor
    def static_routes(self) -> None:
        """static_routes set based on mgmt_gateway, mgmt_destination_networks and mgmt_interface_vrf."""
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
        """router_multicast set based on underlay_multicast, underlay_router and switch.evpn_multicast facts."""
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
    def enable_password(self) -> None:
        """enable_password.disable is set to match EOS default config and historic configs if aaa_settings.enable_password.password is not defined."""
        if self.inputs.aaa_settings.enable_password.password:
            self.structured_config.enable_password._update(hash_algorithm="sha512", key=self.inputs.aaa_settings.enable_password.password)
        else:
            self.structured_config.enable_password.disabled = True

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
    def ip_name_servers(self) -> None:
        """Set ip name servers using old name_servers model and new dns_settings model. Results will be combined."""
        for name_server in self.inputs.name_servers:
            self.structured_config.ip_name_servers.append_new(ip_address=name_server, vrf=self.inputs.mgmt_interface_vrf)

        if not self.inputs.dns_settings:
            return

        if self.inputs.dns_settings.domain:
            self.structured_config.dns_domain = self.inputs.dns_settings.domain

        vrfs = self.inputs.dns_settings.vrfs
        for server in self.inputs.dns_settings.servers:
            server_vrf, source_interface = self._get_vrf_and_source_interface(
                vrf_input=server.vrf,
                vrfs=vrfs,
                set_source_interfaces=self.inputs.dns_settings.set_source_interfaces,
                context=f"dns_settings.servers[ip_address={server.ip_address}].vrf",
            )
            if source_interface:
                self.structured_config.ip_domain_lookup.source_interfaces.append_new(name=source_interface, vrf=server_vrf if server_vrf != "default" else None)

            self.structured_config.ip_name_servers.append_new(ip_address=server.ip_address, vrf=server_vrf, priority=server.priority)

    @structured_config_contributor
    def logging(self) -> None:
        """
        Configures logging settings based on the input data model.

        Applies global logging parameters and per-VRF host logging configuration,
        including source interfaces, protocols, ports, and SSL profiles.
        Ensures that each VRF has a unique and consistent source interface.
        """
        if not self.inputs.logging_settings:
            return

        settings = self.inputs.logging_settings

        # Apply global logging parameters
        self.structured_config.logging._update(
            console=settings.console,
            monitor=settings.monitor,
            repeat_messages=settings.repeat_messages,
            trap=settings.trap,
            facility=settings.facility,
            buffered=settings.buffered,
            synchronous=settings.synchronous,
            format=settings.format,
            policy=settings.policy,
            event=settings.event,
            level=settings.level,
        )

        # Temporary structure to detect source interface conflicts
        vrf_logging_config = EosCliConfigGen.Logging.Vrfs()

        for host in settings.hosts:
            # Determine the correct VRF and source interface for the host
            host_vrf, source_interface = self._get_vrf_and_source_interface(
                vrf_input=host.vrf,
                vrfs=settings.vrfs,
                set_source_interfaces=True,
                context=f"logging_settings.hosts[name={host.name}].vrf",
            )

            logging_vrf = self.structured_config.logging.vrfs.obtain(host_vrf)
            if source_interface:
                # Add to local tmp object to detect conflicts.
                vrf_logging_config.append_new(name=host_vrf, source_interface=source_interface)
                logging_vrf.source_interface = source_interface

            # Add host entry under the correct VRF
            logging_vrf.hosts.append_new(
                name=host.name,
                protocol=host.protocol,
                ssl_profile=host.ssl_profile,
                ports=EosCliConfigGen.Logging.VrfsItem.HostsItem.Ports(items=host.ports),
            )

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
    def local_users(self) -> None:
        """local_users set based on global local_users data model or aaa_settings.local_users data model."""
        local_users = self.inputs.aaa_settings.local_users or self.inputs.local_users
        if not local_users:
            return

        self.structured_config.local_users = local_users._natural_sorted()

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
            interface_settings = EosCliConfigGen.ManagementInterfacesItem(
                name=self.shared_utils.mgmt_interface,
                description=self.inputs.mgmt_interface_description,
                shutdown=False,
                vrf=self.inputs.mgmt_interface_vrf,
                ip_address=self.shared_utils.node_config.mgmt_ip,
                gateway=self.shared_utils.mgmt_gateway,
                type="oob",
            )
            """
            inserting ipv6 variables if ipv6_mgmt_ip is set
            """
            if self.shared_utils.node_config.ipv6_mgmt_ip:
                interface_settings._update(
                    ipv6_enable=True, ipv6_address=self.shared_utils.node_config.ipv6_mgmt_ip, ipv6_gateway=self.shared_utils.ipv6_mgmt_gateway
                )
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

            # TODO: For backward compatibility, checking in advance if we are using the default value
            # remove in AVD 6.0 as well as the try/except below
            using_default_vrfs = self.inputs.management_eapi._get_defined_attr("vrfs") == Undefined

            for vrf in self.inputs.management_eapi.vrfs:
                if vrf.enabled:
                    try:
                        vrf_name = self.get_vrf(vrf.name, context=f"self.inputs.management_eapi.vrfs[name={vrf.name}]")
                    except AristaAvdInvalidInputsError:
                        if not using_default_vrfs:
                            raise
                        vrf_name = self.inputs.mgmt_interface_vrf
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
    def ptp(self) -> None:
        """
        Set PTP config on node level as well as for interfaces, using various defaults.

        - The following are set in default node_type_keys for design "l3ls-evpn":
                spine:
                  default_ptp_priority1: 20
                l3leaf:
                  default_ptp_priority1: 30
        PTP priority2 is set in the code below, calculated based on the node id:
            default_priority2 = self.id % 256.
        """
        if not self.shared_utils.ptp_enabled:
            return
        default_ptp_domain = self.inputs.ptp_settings.domain
        default_ptp_priority1 = self.shared_utils.node_type_key_data.default_ptp_priority1
        default_clock_identity = None

        priority1 = default(self.shared_utils.node_config.ptp.priority1, default_ptp_priority1)
        priority2 = self.shared_utils.node_config.ptp.priority2
        if priority2 is None:
            if self.shared_utils.id is None:
                msg = f"'id' must be set on '{self.shared_utils.hostname}' to set ptp priority2"
                raise AristaAvdInvalidInputsError(msg)

            priority2 = self.shared_utils.id % 256
        if default(self.shared_utils.node_config.ptp.auto_clock_identity, self.inputs.ptp_settings.auto_clock_identity):
            clock_identity_prefix = self.shared_utils.node_config.ptp.clock_identity_prefix
            default_clock_identity = f"{clock_identity_prefix}:{priority1:02x}:00:{priority2:02x}"

        self.structured_config.ptp._update(
            mode=self.shared_utils.node_config.ptp.mode,
            mode_one_step=self.shared_utils.node_config.ptp.mode_one_step or None,  # Historic output is without false
            forward_unicast=self.shared_utils.node_config.ptp.forward_unicast or None,  # Historic output is without false
            clock_identity=default(self.shared_utils.node_config.ptp.clock_identity, default_clock_identity),
            priority1=priority1,
            priority2=priority2,
            ttl=self.shared_utils.node_config.ptp.ttl,
            domain=default(self.shared_utils.node_config.ptp.domain, default_ptp_domain),
            monitor=self.get_ptp_monitor(),
            forward_v1=default(self.shared_utils.node_config.ptp.forward_v1, self.inputs.ptp_settings.forward_v1) or None,
        )

        self.structured_config.ptp.source.ip = self.shared_utils.node_config.ptp.source_ip
        self.structured_config.ptp.message_type.general.dscp = self.shared_utils.node_config.ptp.dscp.general_messages
        self.structured_config.ptp.message_type.event.dscp = self.shared_utils.node_config.ptp.dscp.event_messages

    def get_ptp_monitor(self) -> EosCliConfigGen.Ptp.Monitor:
        """
        Return the Ptp Monitor configuration based on the NodeConfig.

        Cannot use global _case_as because of the default values in EosDesigns.
        """
        node_config_ptp_monitor = self.shared_utils.node_config.ptp.monitor

        # Here _cast_as is not possible because there are default
        ptp_monitor = EosCliConfigGen.Ptp.Monitor(enabled=node_config_ptp_monitor.enabled)
        # Threshold
        ptp_monitor.threshold._update(
            offset_from_master=node_config_ptp_monitor.threshold.offset_from_master,
            mean_path_delay=node_config_ptp_monitor.threshold.mean_path_delay,
        )
        ptp_monitor.threshold.drop._update(
            offset_from_master=node_config_ptp_monitor.threshold.drop.offset_from_master,
            mean_path_delay=node_config_ptp_monitor.threshold.drop.mean_path_delay,
        )
        # Missing message
        ptp_monitor.missing_message.intervals = EosCliConfigGen.Ptp.Monitor.MissingMessage.Intervals(
            announce=node_config_ptp_monitor.missing_message.intervals.announce,
            follow_up=node_config_ptp_monitor.missing_message.intervals.follow_up,
            sync=node_config_ptp_monitor.missing_message.intervals.sync,
        )
        ptp_monitor.missing_message.sequence_ids = EosCliConfigGen.Ptp.Monitor.MissingMessage.SequenceIds(
            enabled=node_config_ptp_monitor.missing_message.sequence_ids.enabled,
            announce=node_config_ptp_monitor.missing_message.sequence_ids.announce,
            delay_resp=node_config_ptp_monitor.missing_message.sequence_ids.delay_resp,
            follow_up=node_config_ptp_monitor.missing_message.sequence_ids.follow_up,
            sync=node_config_ptp_monitor.missing_message.sequence_ids.sync,
        )

        return ptp_monitor

    @structured_config_contributor
    def eos_cli(self) -> None:
        """Aggregate the values of raw_eos_cli and platform_settings.platform_raw_eos_cli facts."""
        eos_cli = "\n".join(filter(None, [self.shared_utils.node_config.raw_eos_cli, self.shared_utils.platform_settings.raw_eos_cli]))
        if eos_cli:
            self.structured_config.eos_cli = eos_cli

    # need to update return type in self._build_source_interfaces() method, then update the below cached_property where this method is used
    @structured_config_contributor
    def ip_radius_source_interfaces(self) -> None:
        """Parse source_interfaces.radius and return list of source_interfaces."""
        if not (inputs := self.inputs.source_interfaces.radius):
            return

        if source_interfaces := self._build_source_interfaces(
            inputs.mgmt_interface, inputs.inband_mgmt_interface, "IP Radius", output_type=EosCliConfigGen.IpRadiusSourceInterfaces
        ):
            self.structured_config.ip_radius_source_interfaces.extend(source_interfaces)

    @structured_config_contributor
    def radius_servers(self) -> None:
        """Parse AAA radius server configurations and update structured config with server and source interface details."""
        if not self.inputs.aaa_settings.radius:
            return

        for server in self.inputs.aaa_settings.radius.servers:
            server_vrf, source_interface = self._get_vrf_and_source_interface(
                vrf_input=server.vrf,
                vrfs=self.inputs.aaa_settings.radius.vrfs,
                set_source_interfaces=True,
                context=f"aaa_settings.radius.servers[host={server.host}].vrf",
            )
            if source_interface:
                self.structured_config.ip_radius_source_interfaces.append_unique(
                    EosCliConfigGen.IpRadiusSourceInterfacesItem(name=source_interface, vrf=server_vrf)
                )

            server_key = self._get_tacacs_or_radius_server_password(server)
            self.structured_config.radius_server.hosts.append_new(host=server.host, vrf=server_vrf, key=server_key)

            for group in server.groups:
                radius_group = self.structured_config.aaa_server_groups.obtain(group)
                radius_group.type = "radius"
                radius_group.servers.append_new(server=server.host, vrf=server_vrf)

    @structured_config_contributor
    def ip_tacacs_source_interfaces(self) -> None:
        """Parse source_interfaces.tacacs and return list of source_interfaces."""
        if not (inputs := self.inputs.source_interfaces.tacacs):
            return

        if source_interfaces := self._build_source_interfaces(
            inputs.mgmt_interface, inputs.inband_mgmt_interface, "IP Tacacs", output_type=EosCliConfigGen.IpTacacsSourceInterfaces
        ):
            self.structured_config.ip_tacacs_source_interfaces.extend(source_interfaces)

    @structured_config_contributor
    def tacacs_servers(self) -> None:
        """Parse AAA tacacs server configurations and update structured config with server and source interface details."""
        if not self.inputs.aaa_settings.tacacs:
            return
        all_tacacs_servers = EosCliConfigGen.TacacsServers.Hosts()
        for server in self.inputs.aaa_settings.tacacs.servers:
            server_vrf, source_interface = self._get_vrf_and_source_interface(
                vrf_input=server.vrf,
                vrfs=self.inputs.aaa_settings.tacacs.vrfs,
                set_source_interfaces=True,
                context=f"aaa_settings.tacacs.servers[host={server.host}].vrf",
            )

            if source_interface:
                self.structured_config.ip_tacacs_source_interfaces.append_unique(
                    EosCliConfigGen.IpTacacsSourceInterfacesItem(name=source_interface, vrf=server_vrf)
                )
            tacacs_server = EosCliConfigGen.TacacsServers.HostsItem(host=server.host, vrf=server_vrf)
            if not all_tacacs_servers.__contains__(tacacs_server):
                all_tacacs_servers.append(tacacs_server)
                server_key = self._get_tacacs_or_radius_server_password(server)
                self.structured_config.tacacs_servers.hosts.append_new(host=server.host, vrf=server_vrf, key=server_key)

                for group in server.groups:
                    tacacs_group = self.structured_config.aaa_server_groups.obtain(group)
                    tacacs_group.type = "tacacs+"
                    tacacs_group.servers.append_new(server=server.host, vrf=server_vrf)

        self.structured_config.tacacs_servers.policy_unknown_mandatory_attribute_ignore = (
            self.inputs.aaa_settings.tacacs.policy.ignore_unknown_mandatory_attribute
        )

    @structured_config_contributor
    def aaa_authentication(self) -> None:
        """Assign AAA authentication configuration from inputs to structured config."""
        if not (aaa_authentication := self.inputs.aaa_settings.authentication):
            return
        self.structured_config.aaa_authentication = aaa_authentication

    @structured_config_contributor
    def aaa_authorization(self) -> None:
        """Assign AAA authorization configuration from inputs to structured config."""
        if not (aaa_authorization := self.inputs.aaa_settings.authorization):
            return
        self.structured_config.aaa_authorization = aaa_authorization

    @structured_config_contributor
    def aaa_accounting(self) -> None:
        """Assign AAA accounting configuration from inputs to structured config."""
        if not (aaa_accounting := self.inputs.aaa_settings.accounting):
            return
        self.structured_config.aaa_accounting = aaa_accounting

    @structured_config_contributor
    def aaa_root_login(self) -> None:
        """Assign AAA root login configuration from inputs to structured config."""
        aaa_root_login = self.inputs.aaa_settings.root_login
        self.structured_config.aaa_root.disabled = not aaa_root_login.enabled
        self.structured_config.aaa_root.secret.sha512_password = aaa_root_login.sha512_password

    @structured_config_contributor
    def ip_ssh_client_source_interfaces(self) -> None:
        """Parse source_interfaces.ssh_client and return list of source_interfaces."""
        if not (inputs := self.inputs.source_interfaces.ssh_client):
            return

        if source_interfaces := self._build_source_interfaces(
            inputs.mgmt_interface, inputs.inband_mgmt_interface, "IP SSH Client", output_type=EosCliConfigGen.IpSshClientSourceInterfaces
        ):
            self.structured_config.ip_ssh_client_source_interfaces = source_interfaces

    @structured_config_contributor
    def ip_domain_lookup(self) -> None:
        """Parse source_interfaces.domain_lookup and return dict with nested source_interfaces list."""
        if not (inputs := self.inputs.source_interfaces.domain_lookup):
            return

        if source_interfaces := self._build_source_interfaces(
            inputs.mgmt_interface, inputs.inband_mgmt_interface, "IP Domain Lookup", output_type=EosCliConfigGen.IpDomainLookup.SourceInterfaces
        ):
            self.structured_config.ip_domain_lookup.source_interfaces = source_interfaces

    @structured_config_contributor
    def ip_http_client_source_interfaces(self) -> None:
        """Parse source_interfaces.http_client and set list of source_interfaces."""
        if not (inputs := self.inputs.source_interfaces.http_client):
            return

        if source_interfaces := self._build_source_interfaces(
            inputs.mgmt_interface, inputs.inband_mgmt_interface, "IP HTTP Client", output_type=EosCliConfigGen.IpHttpClientSourceInterfaces
        ):
            self.structured_config.ip_http_client_source_interfaces = source_interfaces

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
