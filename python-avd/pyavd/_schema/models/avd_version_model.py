# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import Any

from pyavd._schema.avd_version import FUTURE_SETTINGS, get_future_defaults
from pyavd._utils.undefined import Undefined

from .avd_model import AvdModel


class AvdVersionModel(AvdModel):
    """Root model applying versioned defaults while preserving explicit future flags."""

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        if (version := kwargs.get("avd_version")) is None or version is Undefined:
            return
        for future_key in FUTURE_SETTINGS:
            if future_key not in self._fields:
                continue
            defaults = get_future_defaults(version, future_key)
            if not defaults:
                continue
            future_settings = getattr(self, future_key)
            if future_settings._created_from_null:
                continue
            # A caller may have passed an existing model into the constructor.
            future_settings = future_settings._deepcopy()
            for flag, value in defaults.items():
                if future_settings._get_defined_attr(flag) is Undefined:
                    setattr(future_settings, flag, value)
            setattr(self, future_key, future_settings)
