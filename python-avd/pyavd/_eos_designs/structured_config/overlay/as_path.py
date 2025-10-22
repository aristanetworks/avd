# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor
from pyavd._utils import as_path_list_match_from_bgp_asns
from pyavd.j2filters import natural_sort

if TYPE_CHECKING:
    from . import AvdStructuredConfigOverlayProtocol


class AsPathMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @structured_config_contributor
    def as_path(self: AvdStructuredConfigOverlayProtocol) -> None:
        """Set the structured config for as_path."""
        if self.shared_utils.overlay_routing_protocol != "ebgp":
            return

        if self.inputs.evpn_prevent_readvertise_to_server and self.inputs.evpn_prevent_readvertise_to_server_mode == "as_path_acl":
            remote_asns = natural_sort({bgp_as for rs_dict in self._evpn_route_servers.values() if (bgp_as := rs_dict.get("bgp_as")) is not None})
            for remote_asn in remote_asns:
                entries = EosCliConfigGen.AsPath.AccessListsItem.Entries()
                entries.append_new(type="permit", match=as_path_list_match_from_bgp_asns([remote_asn]))
                self.structured_config.as_path.access_lists.append_new(name=f"AS{remote_asn}", entries=entries)
