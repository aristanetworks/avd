# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor
from pyavd._errors import AristaAvdInvalidInputsError

if TYPE_CHECKING:
    from . import AvdStructuredConfigBaseProtocol


class MonitorConnectivityMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @structured_config_contributor
    def monitor_connectivity(self: AvdStructuredConfigBaseProtocol) -> None:
        """Set monitor_connectivity based on the input data model."""
        if not self.inputs.monitor_connectivity:
            return
        monitor_connectivity = self.structured_config.monitor_connectivity._update(
            shutdown=self.inputs.monitor_connectivity.shutdown,
            interval=self.inputs.monitor_connectivity.interval,
            interface_sets=self.inputs.monitor_connectivity.interface_sets._cast_as(EosCliConfigGen.MonitorConnectivity.InterfaceSets),
            address_only=self.inputs.monitor_connectivity.address_only,
            name_server_group=self.inputs.monitor_connectivity.name_server_group,
        )
        if (local_interfaces := self.inputs.monitor_connectivity.local_interfaces) is not None:
            if local_interfaces in self.inputs.monitor_connectivity.interface_sets:
                monitor_connectivity.local_interfaces = local_interfaces
            else:
                msg = f"monitor_connectivity.local_interfaces '{local_interfaces}' has to be defined in monitor_connectivity.interface_sets."
                raise AristaAvdInvalidInputsError(msg)
        self._set_monitor_connectivity_hosts(
            self.inputs.monitor_connectivity.hosts,
            monitor_connectivity.hosts,
            self.inputs.monitor_connectivity.interface_sets,
            "monitor_connectivity",
        )
        for vrf in self.inputs.monitor_connectivity.vrfs:
            monitor_connectivity_vrf = monitor_connectivity.vrfs.append_new(
                name=vrf.name,
                description=vrf.description,
                single_line_description=vrf.single_line_description,
                interface_sets=vrf.interface_sets._cast_as(EosCliConfigGen.MonitorConnectivity.VrfsItem.InterfaceSets),
                address_only=vrf.address_only,
            )
            if (vrf_local_interfaces := vrf.local_interfaces) is not None:
                if vrf_local_interfaces in vrf.interface_sets:
                    monitor_connectivity_vrf.local_interfaces = vrf_local_interfaces
                else:
                    msg = (
                        f"monitor_connectivity.vrfs[name={vrf.name}].local_interfaces '{vrf_local_interfaces}' "
                        f"has to be defined in monitor_connectivity.vrfs[name={vrf.name}].interface_sets."
                    )
                    raise AristaAvdInvalidInputsError(msg)
            self._set_monitor_connectivity_hosts(
                vrf.hosts,
                monitor_connectivity_vrf.hosts,
                vrf.interface_sets,
                f"monitor_connectivity.vrfs[name={vrf.name}]",
            )
