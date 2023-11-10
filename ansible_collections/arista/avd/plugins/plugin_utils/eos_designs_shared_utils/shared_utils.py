# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

from .bgp_peer_groups import BgpPeerGroupsMixin
from .connected_endpoints_keys import ConnectedEndpointsKeysMixin
from .cv_topology import CvTopology
from .inband_management import InbandManagementMixin
from .interface_descriptions import InterfaceDescriptionsMixin
from .ip_addressing import IpAddressingMixin
from .link_tracking_groups import LinkTrackingGroupsMixin
from .mgmt import MgmtMixin
from .misc import MiscMixin
from .mlag import MlagMixin
from .node_type import NodeTypeMixin
from .node_type_keys import NodeTypeKeysMixin
from .overlay import OverlayMixin
from .platform import PlatformMixin
from .ptp import PtpMixin
from .routing import RoutingMixin
from .switch_data import SwitchDataMixin
from .underlay import UnderlayMixin
from .utils import UtilsMixin

if TYPE_CHECKING:
    from ansible_collections.arista.avd.roles.eos_designs.python_modules.pool_manager import AvdPoolManager


class SharedUtils(
    BgpPeerGroupsMixin,
    ConnectedEndpointsKeysMixin,
    InbandManagementMixin,
    InterfaceDescriptionsMixin,
    IpAddressingMixin,
    LinkTrackingGroupsMixin,
    CvTopology,
    MgmtMixin,
    MlagMixin,
    MiscMixin,
    NodeTypeMixin,
    NodeTypeKeysMixin,
    OverlayMixin,
    PlatformMixin,
    PtpMixin,
    SwitchDataMixin,
    RoutingMixin,
    UnderlayMixin,
    UtilsMixin,
):
    """
    Class with commonly used methods / cached_properties to be shared between all the python_modules
    loaded in eos_designs.

    This class is instatiated in 'EosDesignsFacts' class and set as 'shared_utils' property.
    This class is also instatiated in 'eos_designs_structured_config' and the instance is given as argument to
    each python module. The base class '__init__' will set the instance as 'shared_utils' property.

    Since these methods / cached_properties will not be rendered automatically, we can avoid some of the
    general conditions and just return the value. We expect the logic that determines the relevancy of the
    value to be handled in calling function.

    The class cannot be overriden.
    """

    def __init__(self, hostvars: dict, templar, pool_manager: AvdPoolManager | None = None) -> None:
        self.hostvars = hostvars
        self.templar = templar
        self.pool_manager = pool_manager
