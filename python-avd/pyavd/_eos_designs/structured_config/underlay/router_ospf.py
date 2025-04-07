# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor
from pyavd._utils import default

if TYPE_CHECKING:
    from . import AvdStructuredConfigUnderlayProtocol


class RouterOspfMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @structured_config_contributor
    def router_ospf(self: AvdStructuredConfigUnderlayProtocol) -> None:
        """Set the structured config for router_ospf."""
        if self.shared_utils.underlay_ospf is not True:
            return

        process = EosCliConfigGen.RouterOspf.ProcessIdsItem(
            id=self.inputs.underlay_ospf_process_id,
            passive_interface_default=True,
            router_id=self.shared_utils.router_id if not self.inputs.use_router_general_for_router_id else None,
            max_lsa=self.inputs.underlay_ospf_max_lsa,
            bfd_enable=self.inputs.underlay_ospf_bfd_enable,
        )
        for link in self._underlay_links:
            if link.type == "underlay_p2p":
                process.no_passive_interfaces.append(link.interface)

        if self.shared_utils.mlag_l3 is True:
            mlag_l3_vlan = default(self.shared_utils.mlag_peer_l3_vlan, self.shared_utils.node_config.mlag_peer_vlan)
            process.no_passive_interfaces.append(f"Vlan{mlag_l3_vlan}")

        if self.shared_utils.overlay_routing_protocol == "none":
            process.redistribute.connected.enabled = True

        if self.inputs.underlay_ospf_graceful_restart:
            process.graceful_restart.enabled = True

        self.structured_config.router_ospf.process_ids.append(process)
