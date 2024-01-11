# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.plugin_utils.utils import get

from .utils import UtilsMixin


class ApplicationTrafficRecognitionMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    @cached_property
    def application_traffic_recognition(self) -> dict | None:
        """
        Return structured config for application_traffic_recognition if `wan_role` is not None

        Covers EVPN services in VRF "default" and redistribution of connected to BGP
        """
        if not self.shared_utils.wan_role:
            return None

        return get(self._hostvars, "application_traffic_recognition", {}) or None
