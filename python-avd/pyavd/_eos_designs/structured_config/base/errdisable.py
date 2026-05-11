# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol, cast

from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor

if TYPE_CHECKING:
    from pyavd._eos_cli_config_gen.schema import EosCliConfigGen

    from . import AvdStructuredConfigBaseProtocol


def _evaluate_errdisable_cause(
    cause_field: str,
    errdisable_cause: object,
    platform_cause: object,
) -> tuple[str, bool, bool, int | None]:
    """
    Return (cause_name, detection_enabled, recovery_enabled, recovery_interval) for a single cause.

    The schema field name (snake_case) is translated to the EOS cause name.
    A cause is enabled only when both the user input and the platform support evaluate to True.
    `getattr` defaults to None to handle causes whose class doesn't define detection or recovery
    (e.g. recovery-only causes have no `detection` field).
    """
    cause_name = cause_field.replace("_", "-")
    detection_enabled = bool(getattr(errdisable_cause, "detection", None) and getattr(platform_cause, "detection", None))
    recovery_enabled = bool(getattr(errdisable_cause, "recovery", None) and getattr(platform_cause, "recovery", None))
    recovery_interval = getattr(errdisable_cause, "recovery_interval", None)
    return cause_name, detection_enabled, recovery_enabled, recovery_interval


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

        for cause_field, errdisable_cause in errdisable_causes.items():
            platform_cause = getattr(platform_errdisable_causes, cause_field)
            cause_name, detection_enabled, recovery_enabled, recovery_interval = _evaluate_errdisable_cause(cause_field, errdisable_cause, platform_cause)
            if detection_enabled:
                self.structured_config.errdisable.detect.causes.append(cause_name)
            if recovery_enabled:
                self.structured_config.errdisable.recovery.causes.append_new(
                    name=cast("EosCliConfigGen.Errdisable.Recovery.CausesItem.Name", cause_name),
                    interval=recovery_interval,
                )
