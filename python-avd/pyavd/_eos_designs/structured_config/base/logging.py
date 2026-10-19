# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor

if TYPE_CHECKING:
    from . import AvdStructuredConfigBaseProtocol


class LoggingMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @structured_config_contributor
    def logging(self: AvdStructuredConfigBaseProtocol) -> None:
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

        # Apply monitor_layer1 settings
        if settings.monitor_layer1.enabled:
            self.structured_config.monitor_layer1 = settings.monitor_layer1._cast_as(EosCliConfigGen.MonitorLayer1)

        # Temporary structure to detect source interface conflicts
        vrf_logging_config = EosCliConfigGen.Logging.Vrfs()

        for host in settings.hosts:
            # Determine the correct VRF and source interface for the host
            host_vrf, source_interface = self.shared_utils.get_vrf_and_source_interface(
                vrf_input=host.vrf,
                vrfs=settings.vrfs,
                set_source_interfaces=True,
                context=f"logging_settings.hosts[name={host.name}].vrf",
            )

            logging_vrf = self.structured_config.logging.vrfs.obtain(host_vrf)
            if source_interface:
                # Add to local tmp object to detect conflicts.
                vrf_logging_config.append_new(name=host_vrf, source_interface=source_interface)
                # Set either local_interface or source_interface based on use_local_interface_cli
                if settings.use_local_interface_cli:
                    logging_vrf.local_interface = source_interface
                else:
                    logging_vrf.source_interface = source_interface

            # Add host entry under the correct VRF
            logging_vrf.hosts.append_new(
                name=host.name,
                protocol=host.protocol,
                ssl_profile=host.ssl_profile,
                ports=EosCliConfigGen.Logging.VrfsItem.HostsItem.Ports(items=host.ports),
            )
