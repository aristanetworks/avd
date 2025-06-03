# Copyright (c) 2024-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Centralized package to import all the tests of the ANTA framework."""

from anta.tests.avt import VerifyAVTRole, VerifyAVTSpecificPath
from anta.tests.configuration import VerifyRunningConfigDiffs, VerifyZeroTouch
from anta.tests.connectivity import VerifyLLDPNeighbors, VerifyReachability
from anta.tests.hardware import (
    VerifyEnvironmentCooling,
    VerifyEnvironmentPower,
    VerifyEnvironmentSystemCooling,
    VerifyTemperature,
    VerifyTransceiversTemperature,
)
from anta.tests.interfaces import (
    VerifyIllegalLACP,
    VerifyInterfaceDiscards,
    VerifyInterfaceErrDisabled,
    VerifyInterfaceErrors,
    VerifyInterfacesStatus,
    VerifyInterfaceUtilization,
    VerifyPortChannels,
    VerifyStormControlDrops,
)
from anta.tests.logging import VerifyLoggingErrors
from anta.tests.mlag import (
    VerifyMlagConfigSanity,
    VerifyMlagDualPrimary,
    VerifyMlagInterfaces,
    VerifyMlagReloadDelay,
    VerifyMlagStatus,
)
from anta.tests.path_selection import VerifySpecificPath
from anta.tests.routing.bgp import VerifyBGPPeerSession
from anta.tests.routing.generic import VerifyRoutingProtocolModel
from anta.tests.security import VerifyAPIHttpsSSL, VerifySpecificIPSecConn, VerifyTelnetStatus
from anta.tests.services import VerifyDNSServers
from anta.tests.stp import VerifySTPBlockedPorts, VerifySTPCounters
from anta.tests.stun import VerifyStunClientTranslation
from anta.tests.system import (
    VerifyAgentLogs,
    VerifyCoredump,
    VerifyFileSystemUtilization,
    VerifyMemoryUtilization,
    VerifyNTP,
    VerifyReloadCause,
)

__all__ = [
    "VerifyAPIHttpsSSL",
    "VerifyAVTRole",
    "VerifyAVTSpecificPath",
    "VerifyAgentLogs",
    "VerifyBGPPeerSession",
    "VerifyCoredump",
    "VerifyDNSServers",
    "VerifyEnvironmentCooling",
    "VerifyEnvironmentPower",
    "VerifyEnvironmentSystemCooling",
    "VerifyFileSystemUtilization",
    "VerifyIllegalLACP",
    "VerifyInterfaceDiscards",
    "VerifyInterfaceErrDisabled",
    "VerifyInterfaceErrors",
    "VerifyInterfaceUtilization",
    "VerifyInterfacesStatus",
    "VerifyLLDPNeighbors",
    "VerifyLoggingErrors",
    "VerifyMemoryUtilization",
    "VerifyMlagConfigSanity",
    "VerifyMlagDualPrimary",
    "VerifyMlagInterfaces",
    "VerifyMlagReloadDelay",
    "VerifyMlagStatus",
    "VerifyNTP",
    "VerifyPortChannels",
    "VerifyReachability",
    "VerifyReloadCause",
    "VerifyRoutingProtocolModel",
    "VerifyRunningConfigDiffs",
    "VerifySTPBlockedPorts",
    "VerifySTPCounters",
    "VerifySpecificIPSecConn",
    "VerifySpecificPath",
    "VerifyStormControlDrops",
    "VerifyStunClientTranslation",
    "VerifyTelnetStatus",
    "VerifyTemperature",
    "VerifyTransceiversTemperature",
    "VerifyZeroTouch",
]
