# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor

if TYPE_CHECKING:
    from . import AvdStructuredConfigBaseProtocol


class ErrDisableMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @structured_config_contributor
    def errdisable(self: AvdStructuredConfigBaseProtocol) -> None:
        """
        Set errdisable configuration.

        Only emit per-cause structured config when the user has explicitly set `detection`
        or `recovery` in `errdisable_settings.causes.<cause>`. Anything left unset falls
        back to the EOS default. A cause is skipped when the platform does not support that
        capability (`platform_settings.feature_support.errdisable_causes.<cause>.<field>: false`).
        """
        if not self.inputs.errdisable_settings:
            return

        if self.inputs.errdisable_settings.recovery_interval is not None:
            self.structured_config.errdisable.recovery_interval = self.inputs.errdisable_settings.recovery_interval

        errdisable_causes = self.inputs.errdisable_settings.causes
        if not errdisable_causes:
            return

        platform_errdisable_causes = self.shared_utils.platform_settings.feature_support.errdisable_causes

        for cause_field, errdisable_cause in errdisable_causes.items():
            platform_cause = getattr(platform_errdisable_causes, cause_field)
            detection_supported = "detection" in errdisable_cause._fields
            if detection_supported and (detect := errdisable_cause.detection if platform_cause.detection else None) is not None:
                setattr(self.structured_config.errdisable.detect_cause, cause_field, detect)

            recovery_supported = "recovery" in errdisable_cause._fields
            if recovery_supported and (recovery := errdisable_cause.recovery if platform_cause.recovery else None) is not None:
                structured_config_recovery_cause = getattr(self.structured_config.errdisable.recovery_cause, cause_field)
                structured_config_recovery_cause.enabled = recovery
                if recovery and (recovery_interval := errdisable_cause.recovery_interval) is not None:
                    structured_config_recovery_cause.interval = recovery_interval
