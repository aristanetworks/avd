# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Input factories for the ANTA tests."""

from __future__ import annotations

from .avt import VerifyAVTRoleInputFactory, VerifyAVTSpecificPathInputFactory
from .connectivity import VerifyLLDPNeighborsInputFactory, VerifyReachabilityInputFactory
from .hardware import VerifyEnvironmentCoolingInputFactory, VerifyEnvironmentPowerInputFactory
from .interfaces import VerifyInterfacesStatusInputFactory, VerifyPortChannelsInputFactory
from .mlag import VerifyMlagDualPrimaryInputFactory, VerifyMlagReloadDelayInputFactory
from .router_path_selection import VerifySpecificPathInputFactory
from .routing_bgp import VerifyBGPPeerSessionInputFactory
from .routing_generic import VerifyRoutingProtocolModelInputFactory
from .security import VerifyAPIHttpsSSLInputFactory, VerifySpecificIPSecConnInputFactory
from .services import VerifyDNSServersInputFactory
from .stun import VerifyStunClientTranslationInputFactory
from .system import VerifyReloadCauseInputFactory

__all__ = [
    "VerifyAPIHttpsSSLInputFactory",
    "VerifyAVTRoleInputFactory",
    "VerifyAVTSpecificPathInputFactory",
    "VerifyBGPPeerSessionInputFactory",
    "VerifyDNSServersInputFactory",
    "VerifyEnvironmentCoolingInputFactory",
    "VerifyEnvironmentPowerInputFactory",
    "VerifyInterfacesStatusInputFactory",
    "VerifyLLDPNeighborsInputFactory",
    "VerifyMlagDualPrimaryInputFactory",
    "VerifyMlagReloadDelayInputFactory",
    "VerifyPortChannelsInputFactory",
    "VerifyReachabilityInputFactory",
    "VerifyReloadCauseInputFactory",
    "VerifyRoutingProtocolModelInputFactory",
    "VerifySpecificIPSecConnInputFactory",
    "VerifySpecificPathInputFactory",
    "VerifyStunClientTranslationInputFactory",
]
