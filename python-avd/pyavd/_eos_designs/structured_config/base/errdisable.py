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
            user_detection = errdisable_cause._get("detection")
            user_recovery = errdisable_cause._get("recovery")
            recovery_interval = errdisable_cause._get("recovery_interval")

            if user_detection is not None and getattr(platform_cause, "detection", None):
                setattr(self.structured_config.errdisable.detect_cause, cause_field, user_detection)

            if user_recovery is not None and getattr(platform_cause, "recovery", None):
                recovery_cause = getattr(self.structured_config.errdisable.recovery_cause, cause_field)
                recovery_cause.enabled = user_recovery
                if recovery_interval is not None and user_recovery:
                    recovery_cause.interval = recovery_interval
