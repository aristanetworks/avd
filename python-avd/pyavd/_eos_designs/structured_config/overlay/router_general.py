# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor
from pyavd.j2filters import natural_sort

if TYPE_CHECKING:
    from . import AvdStructuredConfigOverlayProtocol


class RouterGeneralMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @structured_config_contributor
    def router_general(self: AvdStructuredConfigOverlayProtocol) -> None:
        """Set the structured config for router_general."""
        if self.shared_utils.overlay_routing_protocol != "ebgp":
            return

        if self.inputs.evpn_prevent_readvertise_to_server and self.inputs.evpn_prevent_readvertise_to_server_mode == "rcf":
            remote_asns = natural_sort({bgp_as for rs_dict in self._evpn_route_servers.values() if (bgp_as := rs_dict.get("bgp_as")) is not None})
            for remote_asn in remote_asns:
                self.structured_config.router_general.control_functions.code_units.append_new(
                    name=f"CU-EVPN-FILTER-AS{remote_asn}",
                    content=f"""function EVPN-FILTER-AS{remote_asn}() {{
    if as_path has_any {{ {remote_asn} }} {{
        return false;
    }}
    return true;
}}
EOF""",
                )
