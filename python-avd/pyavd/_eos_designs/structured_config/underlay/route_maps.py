# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen

if TYPE_CHECKING:
    from . import AvdStructuredConfigUnderlayProtocol


class RouteMapsMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    def set_route_map_underlay_filter_peer_as(self: AvdStructuredConfigUnderlayProtocol, asn: str) -> None:
        """Set route-map RM-BGP-AS{{ asn }}-OUT."""
        route_map_name = f"RM-BGP-AS{asn}-OUT"
        sequence_numbers = EosCliConfigGen.RouteMapsItem.SequenceNumbers()
        sequence_numbers.append_new(sequence=10, type="deny", match=EosCliConfigGen.RouteMapsItem.SequenceNumbersItem.Match([f"as {asn}"]))
        sequence_numbers.append_new(sequence=20, type="permit")
        self.structured_config.route_maps.append_new(name=route_map_name, sequence_numbers=sequence_numbers)
