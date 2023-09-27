# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.plugin_utils.strip_empties import strip_empties_from_dict

from .utils import UtilsMixin


class RouterBfdMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    @cached_property
    def router_bfd(self) -> dict | None:
        """
        return structured config for router_bfd
        """
        if self.shared_utils.bfd_multihop is None:
            return None

        if self.shared_utils.overlay_cvx:
            return None

        return strip_empties_from_dict({"multihop": self.shared_utils.bfd_multihop})
