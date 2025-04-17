# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor
from pyavd._errors import AristaAvdInvalidInputsError
from pyavd.j2filters import list_compress, range_expand

if TYPE_CHECKING:
    from pyavd._eos_designs.schema import EosDesigns

    from . import AvdStructuredConfigBaseProtocol


class PlatformMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class or other Mixins.
    """

    @structured_config_contributor
    def platform(self: AvdStructuredConfigBaseProtocol) -> None:
        """
        Set platform keys in structured config based on platform data-model, using various platform-related information.

        The following settings are used:

        * platform_settings.lag_hardware_only,
        * platform_settings.trident_forwarding_table_partition and switch.evpn_multicast facts
        * data_plane_cpu_allocation_max,
        * platform_settings.feature_support.platform_sfe_interface_profile.supported
        """
        if (lag_hardware_only := self.shared_utils.platform_settings.lag_hardware_only) is not None:
            self.structured_config.platform.sand.lag.hardware_only = lag_hardware_only

        trident_forwarding_table_partition = self.shared_utils.platform_settings.trident_forwarding_table_partition
        if trident_forwarding_table_partition and self.shared_utils.evpn_multicast:
            self.structured_config.platform.trident.forwarding_table_partition = trident_forwarding_table_partition

        if (cpu_max_allocation := self.shared_utils.node_config.data_plane_cpu_allocation_max) is not None:
            self.structured_config.platform.sfe.data_plane_cpu_allocation_max = cpu_max_allocation
        elif self.shared_utils.is_wan_server:
            # For AutoVPN Route Reflectors and Pathfinders, running on CloudEOS, setting
            # this value is required for the solution to work.
            msg = "For AutoVPN RRs and Pathfinders, 'data_plane_cpu_allocation_max' must be set"
            raise AristaAvdInvalidInputsError(msg)

        # populate interface profile for SFE platform (if supported)
        if self.shared_utils.is_sfe_interface_profile_supported and (sfe_member_interfaces_for_profile := self._get_sfe_interface_profile_member_interfaces):
            # build single ProfilesItem and append to Profiles
            default_sfe_interface_profile_name = "SFE-INTERFACE-PROFILE"
            self.structured_config.platform.sfe.interface.profiles.append_new(
                name=default_sfe_interface_profile_name,
                interfaces=sfe_member_interfaces_for_profile,
            )
            # indicate above profile as the one to apply for the device
            self.structured_config.platform.sfe.interface.interface_profile = default_sfe_interface_profile_name

    @cached_property
    def _get_sfe_interface_profile_member_interfaces(
        self: AvdStructuredConfigBaseProtocol,
    ) -> EosCliConfigGen.Platform.Sfe.Interface.ProfilesItem.Interfaces:
        """
        Returns list of eligible SFE interfaces with profile settings for structured config.

        Caller needs to check if `shared_utils.is_sfe_interface_profile_supported` is true
        and then call this method.
        """
        # Iterate through all L3 interfaces checking for those with 'rx_queue' config
        # Also iterate through member interfaces of all L3 Port-Channels with 'rx_queue' config
        sfe_profile_member_interfaces = EosCliConfigGen.Platform.Sfe.Interface.ProfilesItem.Interfaces()
        # iterate through each L3 interface
        for interface in self.shared_utils.l3_interfaces:
            intf_profile_settings = self._build_interface_with_rx_queue_settings(interface)
            if intf_profile_settings is not None:
                sfe_profile_member_interfaces.append(intf_profile_settings)

        # iterate through member interfaces of each L3 Port-Channel
        for interface in self.shared_utils.node_config.l3_port_channels:
            for member_intf in interface.member_interfaces:
                intf_profile_settings = self._build_interface_with_rx_queue_settings(member_intf)
                if intf_profile_settings is not None:
                    sfe_profile_member_interfaces.append(intf_profile_settings)

        if sfe_profile_member_interfaces:
            return sfe_profile_member_interfaces._natural_sorted()
        # return empty list if no candidate interfaces found
        return sfe_profile_member_interfaces

    def _build_interface_with_rx_queue_settings(
        self: AvdStructuredConfigBaseProtocol,
        l3_ethernet_interface: EosDesigns._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodesItem.L3InterfacesItem
        | EosDesigns._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodesItem.L3PortChannelsItem.MemberInterfacesItem,
    ) -> EosCliConfigGen.Platform.Sfe.Interface.ProfilesItem.InterfacesItem | None:
        """Returns one SFE interface with profile settings for structured config."""
        if not l3_ethernet_interface.rx_queue:
            # specified interface does not have explicit "rx_queue" key or sub-keys specified
            # exclude such interface from profile being built
            return None
        # validate rx_queue 'count' when specified
        self._validate_rx_queue_count(l3_ethernet_interface.rx_queue.count, l3_ethernet_interface.name)

        # build a set of worker_ids with each value as int and then validate
        if rx_queue_workers := set(map(int, range_expand(l3_ethernet_interface.rx_queue.workers))):
            self._validate_rx_queue_worker(max(rx_queue_workers), l3_ethernet_interface.name)
        rx_queue_workers_range = list_compress(list(rx_queue_workers))

        return EosCliConfigGen.Platform.Sfe.Interface.ProfilesItem.InterfacesItem(
            name=l3_ethernet_interface.name,
            rx_queue=EosCliConfigGen.Platform.Sfe.Interface.ProfilesItem.InterfacesItem.RxQueue(
                count=l3_ethernet_interface.rx_queue.count,
                worker=rx_queue_workers_range if rx_queue_workers_range else None,
                mode=l3_ethernet_interface.rx_queue.mode,
            ),
        )

    def _validate_rx_queue_count(self: AvdStructuredConfigBaseProtocol, rx_queue_count: int, l3_ethernet_interface_name: str) -> None:
        if rx_queue_count and rx_queue_count > self.shared_utils.max_rx_queues:
            msg = (
                f"'rx_queue.count' for interface '{l3_ethernet_interface_name}' exceeds maximum supported "
                f"'{self.shared_utils.max_rx_queues}' for this platform."
            )
            raise AristaAvdInvalidInputsError(msg)

    def _validate_rx_queue_worker(self: AvdStructuredConfigBaseProtocol, worker_id: int, l3_ethernet_interface_name: str) -> None:
        if worker_id >= self.shared_utils.max_rx_queues:
            msg = (
                f"Worker id '{worker_id}' specified under 'rx_queue.workers' for interface '{l3_ethernet_interface_name}' "
                f"equals or exceeds maximum supported '{self.shared_utils.max_rx_queues}' for this platform."
            )
            raise AristaAvdInvalidInputsError(msg)
