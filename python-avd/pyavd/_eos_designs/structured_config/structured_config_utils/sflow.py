# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_designs.schema import EosDesigns
from pyavd._errors import AristaAvdInvalidInputsError
from pyavd._utils.run_once import run_once_method

if TYPE_CHECKING:
    from . import StructuredConfigUtilsProtocol


class SflowMixin(Protocol):
    @run_once_method
    def set_once_sflow(self: StructuredConfigUtilsProtocol) -> None:
        """Structured config for sFlow based on sflow_settings."""
        sflow_settings = self.inputs.sflow_settings
        destinations = sflow_settings.destinations._natural_sorted(sort_key="destination")
        if sflow_settings.export_to_cloudvision.enabled:
            destinations.append(EosDesigns.SflowSettings.DestinationsItem(destination="127.0.0.1", port=6343, vrf=sflow_settings.export_to_cloudvision.vrf))

        if not destinations:
            msg = "Either `sflow_settings.destinations` or `sflow_settings.export_to_cloudvision.enabled: true` is required to configure `sflow`."
            raise AristaAvdInvalidInputsError(msg)

        # At this point we have at least one interface with sFlow enabled
        # and at least one destination.
        self.structured_config.sflow._update(run=True, polling_interval=sflow_settings.polling_interval, sample=sflow_settings.sample.rate)

        for destination in destinations:
            destination: EosDesigns.SflowSettings.DestinationsItem
            sflow_vrf, source_interface = self.shared_utils.get_vrf_and_source_interface(
                vrf_input=destination.vrf,
                vrfs=sflow_settings.vrfs,
                set_source_interfaces=True,
                context=f"sflow_settings.destinations[destination={destination.destination}].vrf",
            )
            if sflow_vrf == "default":
                # Add destination without VRF field
                self.structured_config.sflow.destinations.append_new(destination=destination.destination, port=destination.port)
                self.structured_config.sflow.source_interface = source_interface
            else:
                # Add destination with VRF field.
                vrf_item = self.structured_config.sflow.vrfs.obtain(sflow_vrf)
                vrf_item.destinations.append_new(destination=destination.destination, port=destination.port)
                vrf_item.source_interface = source_interface
                self.structured_config.sflow.vrfs.append(vrf_item)

    def get_interface_sflow(self: StructuredConfigUtilsProtocol, interface: str, configured_sflow: bool | None) -> bool | None:
        """
        Get the configured sFlow state if the interface supports it based on platform settings.

        Considers global sFlow support and specific support for subinterfaces.

        Also calls set_once_sflow if configured_sflow is True or not None.

        Returns:
            The configured_sflow value if supported, otherwise None.
        """
        if self.shared_utils.platform_settings.feature_support.sflow and (
            "." not in interface or self.shared_utils.platform_settings.feature_support.sflow_subinterfaces
        ):
            if configured_sflow:
                self.set_once_sflow()
            return configured_sflow
        return None
