# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from ansible_collections.arista.avd.plugins.filter.range_expand import range_expand
from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError, AristaAvdMissingVariableError
from ansible_collections.arista.avd.plugins.plugin_utils.utils import default, get, get_item

if TYPE_CHECKING:
    from ansible_collections.arista.avd.plugins.plugin_utils.eos_designs_facts import EosDesignsFacts

    from .shared_utils import EosDesignsFacts


class WanMixin:
    """
    Mixin Class providing a subset of EosDesignsFacts
    Class should only be used as Mixin to the EosDesignsFacts class
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def wan_path_groups(self: EosDesignsFacts) -> list | None:
        """
        Return the list of WAN path_groups directly connected to this router
        """
        # TODO check if needed
        if not self.shared_utils.wan_mode:
            return None
        return [path_group.get("name") for path_group in self.shared_utils.wan_local_path_groups]
