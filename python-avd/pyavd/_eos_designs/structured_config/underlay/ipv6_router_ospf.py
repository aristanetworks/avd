# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor
from pyavd._utils import default

if TYPE_CHECKING:
    from . import AvdStructuredConfigUnderlayProtocol


class Ipv6RouterOspfMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @structured_config_contributor
    def ipv6_router_ospf(self: AvdStructuredConfigUnderlayProtocol) -> None:
        """Set the structured config for ipv6_router_ospf."""
        if self.shared_utils.underlay_ospf is not True:
            return

        process = EosCliConfigGen.Ipv6RouterOspf.ProcessIdsItem(
            id=self.inputs.underlay_ospf_process_id,
            router_id=self.shared_utils.router_id if not self.inputs.use_router_general_for_router_id else None,
        )

        if self.shared_utils.overlay_routing_protocol == "none":
            process.redistribute.connected.enabled = True

        self.structured_config.router_ospf.process_ids.append(process)
