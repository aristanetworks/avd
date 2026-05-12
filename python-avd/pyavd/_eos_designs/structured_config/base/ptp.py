# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from ipaddress import AddressValueError, IPv4Address
from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor
from pyavd._errors import AristaAvdInvalidInputsError
from pyavd._utils import default

if TYPE_CHECKING:
    from . import AvdStructuredConfigBaseProtocol


class PtpMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @structured_config_contributor
    def ptp(self: AvdStructuredConfigBaseProtocol) -> None:
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

        self.structured_config.ptp.free_running.enabled = default(
            self.shared_utils.node_config.ptp.free_running.enabled, self.inputs.ptp_settings.free_running.enabled
        )
        self.structured_config.ptp.free_running.source_clock_hardware = default(
            self.shared_utils.node_config.ptp.free_running.source_clock_hardware, self.inputs.ptp_settings.free_running.source_clock_hardware
        )
        source_ip = self.shared_utils.node_config.ptp.source_ip

        if source_ip == "router_id":
            if self.shared_utils.router_id is None:
                msg = "PTP source IP is set to 'ptp.source_ip: router_id' but no router ID is configured for this device."
                raise AristaAvdInvalidInputsError(msg)
            self.structured_config.ptp.source.ip = self.shared_utils.router_id
        elif source_ip is not None:
            try:
                IPv4Address(source_ip)
                self.structured_config.ptp.source.ip = source_ip
            except AddressValueError:
                msg = f"Invalid PTP source IP 'ptp.source_ip: {source_ip}'. The value must be either 'router_id' or a valid IPv4 address."
                raise AristaAvdInvalidInputsError(msg) from None

        self.structured_config.ptp.message_type.general.dscp = self.shared_utils.node_config.ptp.dscp.general_messages
        self.structured_config.ptp.message_type.event.dscp = self.shared_utils.node_config.ptp.dscp.event_messages

    def get_ptp_monitor(self: AvdStructuredConfigBaseProtocol) -> EosCliConfigGen.Ptp.Monitor:
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
