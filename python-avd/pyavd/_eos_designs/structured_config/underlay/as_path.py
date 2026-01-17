# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._utils import as_path_list_match_from_bgp_asns
from pyavd._utils.run_once import run_once_method

if TYPE_CHECKING:
    from . import AvdStructuredConfigUnderlayProtocol


class AsPathMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @run_once_method
    def set_once_as_path_acl_aspath_wan(self: AvdStructuredConfigUnderlayProtocol) -> None:
        """Set as-path access-list ASPATH-WAN."""
        entries = EosCliConfigGen.AsPath.AccessListsItem.Entries()
        entries.append_new(type="permit", match=as_path_list_match_from_bgp_asns((self.shared_utils.bgp_as,)))  # pyright: ignore[reportArgumentType]
        self.structured_config.as_path.access_lists.append_new(name="ASPATH-WAN", entries=entries)
