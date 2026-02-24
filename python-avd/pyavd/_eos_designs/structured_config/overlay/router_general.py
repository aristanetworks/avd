# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._utils.run_once import run_once_method

if TYPE_CHECKING:
    from . import AvdStructuredConfigOverlayProtocol


class RouterGeneralMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @run_once_method
    def set_once_rcf_evpn_filter_as(self: AvdStructuredConfigOverlayProtocol) -> None:
        """Set argument-based RCF RCF_EVPN_FILTER_AS to filter out EVPN routes containing BGP AS of the remote peer in the AS path."""
        self.structured_config.router_general.control_functions.code_units.append_new(
            name="CU_EVPN_FILTER_AS",
            content="""function RCF_EVPN_FILTER_AS( as_number_type $PEER_ASN ) {\n    return as_path has_none { $PEER_ASN };\n}\nEOF""",
        )
