# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor

if TYPE_CHECKING:
    from pyavd._eos_cli_config_gen.schema import EosCliConfigGen

    from . import AvdStructuredConfigBaseProtocol


class _ErrdisableDetectCause(Protocol):
    """Protocol for errdisable causes that support detection."""

    detection: bool | None


class _PlatformDetectCause(Protocol):
    """Protocol for platform errdisable causes that support detection."""

    detection: bool | None


class _ErrdisableRecoveryCause(Protocol):
    """Protocol for errdisable causes that support recovery."""

    recovery: bool | None
    recovery_interval: int | None


class _PlatformRecoveryCause(Protocol):
    """Protocol for platform errdisable causes that support recovery."""

    recovery: bool | None


class ErrDisableMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @structured_config_contributor
    def errdisable(self: AvdStructuredConfigBaseProtocol) -> None:
        """Set errdisable configuration."""
        if not self.inputs.errdisable_settings:
            return

        if self.inputs.errdisable_settings.recovery_interval is not None:
            self.structured_config.errdisable.recovery.interval = self.inputs.errdisable_settings.recovery_interval

        errdisable_causes = self.inputs.errdisable_settings.causes
        if not errdisable_causes:
            return

        platform_errdisable_causes = self.shared_utils.platform_settings.feature_support.errdisable_causes

        detect_causes: list[tuple[str, _ErrdisableDetectCause, _PlatformDetectCause]] = [
            ("link-change", errdisable_causes.link_change, platform_errdisable_causes.link_change),
            ("acl", errdisable_causes.acl, platform_errdisable_causes.acl),
            ("arp-inspection", errdisable_causes.arp_inspection, platform_errdisable_causes.arp_inspection),
            ("dot1x", errdisable_causes.dot1x, platform_errdisable_causes.dot1x),
            ("dot1x-coa", errdisable_causes.dot1x_coa, platform_errdisable_causes.dot1x_coa),
            ("dot1x-phone-classification", errdisable_causes.dot1x_phone_classification, platform_errdisable_causes.dot1x_phone_classification),
            ("dot1x-session-replace", errdisable_causes.dot1x_session_replace, platform_errdisable_causes.dot1x_session_replace),
            ("error-correction-encoding", errdisable_causes.error_correction_encoding, platform_errdisable_causes.error_correction_encoding),
            ("hardware-speed-group", errdisable_causes.hardware_speed_group, platform_errdisable_causes.hardware_speed_group),
            ("interface-speed", errdisable_causes.interface_speed, platform_errdisable_causes.interface_speed),
            ("internal-error", errdisable_causes.internal_error, platform_errdisable_causes.internal_error),
            ("port-breakout", errdisable_causes.port_breakout, platform_errdisable_causes.port_breakout),
            ("storm-control", errdisable_causes.storm_control, platform_errdisable_causes.storm_control),
            ("switchcard-unreachable", errdisable_causes.switchcard_unreachable, platform_errdisable_causes.switchcard_unreachable),
            ("tapagg", errdisable_causes.tapagg, platform_errdisable_causes.tapagg),
            ("transceiver-adapter", errdisable_causes.transceiver_adapter, platform_errdisable_causes.transceiver_adapter),
            ("xcvr-misconfigured", errdisable_causes.xcvr_misconfigured, platform_errdisable_causes.xcvr_misconfigured),
            ("xcvr-overheat", errdisable_causes.xcvr_overheat, platform_errdisable_causes.xcvr_overheat),
            ("xcvr-power-unsupported", errdisable_causes.xcvr_power_unsupported, platform_errdisable_causes.xcvr_power_unsupported),
        ]
        recovery_causes: list[tuple[EosCliConfigGen.Errdisable.Recovery.CausesItem.Name, _ErrdisableRecoveryCause, _PlatformRecoveryCause]] = [
            ("acl", errdisable_causes.acl, platform_errdisable_causes.acl),
            ("arp-inspection", errdisable_causes.arp_inspection, platform_errdisable_causes.arp_inspection),
            ("bpduguard", errdisable_causes.bpduguard, platform_errdisable_causes.bpduguard),
            ("dot1x", errdisable_causes.dot1x, platform_errdisable_causes.dot1x),
            ("dot1x-coa", errdisable_causes.dot1x_coa, platform_errdisable_causes.dot1x_coa),
            ("dot1x-phone-classification", errdisable_causes.dot1x_phone_classification, platform_errdisable_causes.dot1x_phone_classification),
            ("dot1x-session-replace", errdisable_causes.dot1x_session_replace, platform_errdisable_causes.dot1x_session_replace),
            ("error-correction-encoding", errdisable_causes.error_correction_encoding, platform_errdisable_causes.error_correction_encoding),
            ("hardware-speed-group", errdisable_causes.hardware_speed_group, platform_errdisable_causes.hardware_speed_group),
            ("hitless-reload-down", errdisable_causes.hitless_reload_down, platform_errdisable_causes.hitless_reload_down),
            ("interface-speed", errdisable_causes.interface_speed, platform_errdisable_causes.interface_speed),
            ("internal-error", errdisable_causes.internal_error, platform_errdisable_causes.internal_error),
            ("lacp-rate-limit", errdisable_causes.lacp_rate_limit, platform_errdisable_causes.lacp_rate_limit),
            ("link-flap", errdisable_causes.link_flap, platform_errdisable_causes.link_flap),
            ("no-internal-vlan", errdisable_causes.no_internal_vlan, platform_errdisable_causes.no_internal_vlan),
            ("port-breakout", errdisable_causes.port_breakout, platform_errdisable_causes.port_breakout),
            ("portchannelguard", errdisable_causes.portchannelguard, platform_errdisable_causes.portchannelguard),
            ("portsec", errdisable_causes.portsec, platform_errdisable_causes.portsec),
            ("speed-misconfigured", errdisable_causes.speed_misconfigured, platform_errdisable_causes.speed_misconfigured),
            ("storm-control", errdisable_causes.storm_control, platform_errdisable_causes.storm_control),
            ("stuck-queue", errdisable_causes.stuck_queue, platform_errdisable_causes.stuck_queue),
            ("switchcard-unreachable", errdisable_causes.switchcard_unreachable, platform_errdisable_causes.switchcard_unreachable),
            ("tap-port-init", errdisable_causes.tap_port_init, platform_errdisable_causes.tap_port_init),
            ("tapagg", errdisable_causes.tapagg, platform_errdisable_causes.tapagg),
            ("transceiver-adapter", errdisable_causes.transceiver_adapter, platform_errdisable_causes.transceiver_adapter),
            ("uplink-failure-detection", errdisable_causes.uplink_failure_detection, platform_errdisable_causes.uplink_failure_detection),
            ("xcvr-misconfigured", errdisable_causes.xcvr_misconfigured, platform_errdisable_causes.xcvr_misconfigured),
            ("xcvr-overheat", errdisable_causes.xcvr_overheat, platform_errdisable_causes.xcvr_overheat),
            ("xcvr-power-unsupported", errdisable_causes.xcvr_power_unsupported, platform_errdisable_causes.xcvr_power_unsupported),
            ("xcvr-unsupported", errdisable_causes.xcvr_unsupported, platform_errdisable_causes.xcvr_unsupported),
        ]

        for eos_cause_name, errdisable_cause, platform_cause in detect_causes:
            if errdisable_cause.detection is True and platform_cause.detection is not False:
                self.structured_config.errdisable.detect.causes.append(eos_cause_name)

        for eos_cause_name, errdisable_cause, platform_cause in recovery_causes:
            if errdisable_cause.recovery is True and platform_cause.recovery is not False:
                self.structured_config.errdisable.recovery.causes.append_new(name=eos_cause_name, interval=errdisable_cause.recovery_interval)
