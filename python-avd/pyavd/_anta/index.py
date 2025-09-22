# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Test index for PyAVD ANTA tests."""

from __future__ import annotations

from pyavd._anta.input_factories import *
from pyavd._anta.lib.tests import *
from pyavd.api._anta import TestSpec

from .constants import StructuredConfigKey

AVD_TEST_INDEX: list[TestSpec] = [
    TestSpec(
        test_class=VerifyAgentLogs,
    ),
    TestSpec(
        test_class=VerifyAPIHttpsSSL,
        conditional_keys=[StructuredConfigKey.HTTPS_SSL_PROFILE],
        input_factory=VerifyAPIHttpsSSLInputFactory,
    ),
    TestSpec(
        test_class=VerifyAVTSpecificPath,
        conditional_keys=[StructuredConfigKey.ROUTER_AVT, StructuredConfigKey.ROUTER_PATH_SELECTION],
        input_factory=VerifyAVTSpecificPathInputFactory,
    ),
    TestSpec(
        test_class=VerifyBGPPeerSession,
        conditional_keys=[StructuredConfigKey.ROUTER_BGP],
        input_factory=VerifyBGPPeerSessionInputFactory,
    ),
    TestSpec(
        test_class=VerifyCoredump,
    ),
    TestSpec(
        test_class=VerifyEnvironmentCooling,
        input_factory=VerifyEnvironmentCoolingInputFactory,
    ),
    TestSpec(
        test_class=VerifyEnvironmentPower,
        input_factory=VerifyEnvironmentPowerInputFactory,
    ),
    TestSpec(
        test_class=VerifyEnvironmentSystemCooling,
    ),
    TestSpec(
        test_class=VerifyFileSystemUtilization,
    ),
    TestSpec(
        test_class=VerifyIllegalLACP,
        conditional_keys=[StructuredConfigKey.PORT_CHANNEL_INTERFACES],
    ),
    TestSpec(
        test_class=VerifyInterfaceDiscards,
    ),
    TestSpec(
        test_class=VerifyInterfaceErrDisabled,
    ),
    TestSpec(
        test_class=VerifyInterfaceErrors,
    ),
    TestSpec(
        test_class=VerifyInterfaceUtilization,
    ),
    TestSpec(
        test_class=VerifyInterfacesStatus,
        input_factory=VerifyInterfacesStatusInputFactory,
    ),
    TestSpec(
        test_class=VerifyPortChannels,
        conditional_keys=[StructuredConfigKey.PORT_CHANNEL_INTERFACES],
        input_factory=VerifyPortChannelsInputFactory,
    ),
    TestSpec(
        test_class=VerifyRunningConfigDiffs,
    ),
    TestSpec(
        test_class=VerifyStormControlDrops,
    ),
    TestSpec(
        test_class=VerifyLLDPNeighbors,
        conditional_keys=[StructuredConfigKey.ETHERNET_INTERFACES],
        input_factory=VerifyLLDPNeighborsInputFactory,
    ),
    TestSpec(
        test_class=VerifyLoggingErrors,
    ),
    TestSpec(
        test_class=VerifyMaintenance,
    ),
    TestSpec(
        test_class=VerifyMemoryUtilization,
    ),
    TestSpec(
        test_class=VerifyMlagConfigSanity,
        conditional_keys=[StructuredConfigKey.MLAG_CONFIGURATION],
    ),
    TestSpec(
        test_class=VerifyMlagInterfaces,
        conditional_keys=[StructuredConfigKey.MLAG_CONFIGURATION],
    ),
    TestSpec(
        test_class=VerifyMlagStatus,
        conditional_keys=[StructuredConfigKey.MLAG_CONFIGURATION],
    ),
    TestSpec(
        test_class=VerifyNTP,
    ),
    TestSpec(
        test_class=VerifySpecificPath,
        conditional_keys=[StructuredConfigKey.ROUTER_PATH_SELECTION],
        input_factory=VerifySpecificPathInputFactory,
    ),
    TestSpec(
        test_class=VerifyReachability,
        input_factory=VerifyReachabilityInputFactory,
    ),
    TestSpec(
        test_class=VerifyReloadCause,
        input_factory=VerifyReloadCauseInputFactory,
    ),
    TestSpec(
        test_class=VerifyRoutingProtocolModel,
        conditional_keys=[StructuredConfigKey.SERVICE_ROUTING_PROTOCOLS_MODEL],
        input_factory=VerifyRoutingProtocolModelInputFactory,
    ),
    TestSpec(
        test_class=VerifySpecificIPSecConn,
        conditional_keys=[StructuredConfigKey.ROUTER_PATH_SELECTION],
        input_factory=VerifySpecificIPSecConnInputFactory,
    ),
    TestSpec(
        test_class=VerifySTPCounters,
    ),
    TestSpec(
        test_class=VerifyTemperature,
    ),
    TestSpec(
        test_class=VerifyTransceiversTemperature,
    ),
    TestSpec(test_class=VerifyVxlanConfigSanity, conditional_keys=[StructuredConfigKey.VXLAN1_INTERFACE]),
    TestSpec(
        test_class=VerifyZeroTouch,
    ),
]
"""List of all ANTA tests with their specifications that AVD will run by default."""

AVD_TEST_INDEX.sort(key=lambda x: x.test_class.name)
"""Sort the test index by the test class name."""

AVD_TEST_NAMES: list[str] = [test.test_class.name for test in AVD_TEST_INDEX]
"""List of all available ANTA test names that AVD will run by default."""
