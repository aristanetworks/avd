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
        input_dict={"profile": StructuredConfigKey.HTTPS_SSL_PROFILE},
    ),
    TestSpec(
        test_class=VerifyAVTPathHealth,
        conditional_keys=[StructuredConfigKey.ROUTER_AVT],
    ),
    TestSpec(
        test_class=VerifyAVTRole,
        conditional_keys=[StructuredConfigKey.ROUTER_AVT],
        input_factory=VerifyAVTRoleInputFactory,
    ),
    TestSpec(
        test_class=VerifyBFDPeersHealth,
        conditional_keys=[StructuredConfigKey.ROUTER_BFD],
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
        test_class=VerifyMemoryUtilization,
    ),
    TestSpec(
        test_class=VerifyMlagConfigSanity,
        conditional_keys=[StructuredConfigKey.MLAG_CONFIGURATION],
    ),
    TestSpec(
        test_class=VerifyMlagDualPrimary,
        conditional_keys=[StructuredConfigKey.MLAG_DUAL_PRIMARY_DETECTION_DELAY],
        input_factory=VerifyMlagDualPrimaryInputFactory,
    ),
    TestSpec(
        test_class=VerifyMlagInterfaces,
        conditional_keys=[StructuredConfigKey.MLAG_CONFIGURATION],
    ),
    TestSpec(
        test_class=VerifyMlagReloadDelay,
        conditional_keys=[StructuredConfigKey.RELOAD_DELAY_MLAG, StructuredConfigKey.RELOAD_DELAY_NON_MLAG],
        input_dict={
            "reload_delay": StructuredConfigKey.RELOAD_DELAY_MLAG,
            "reload_delay_non_mlag": StructuredConfigKey.RELOAD_DELAY_NON_MLAG,
        },
    ),
    TestSpec(
        test_class=VerifyMlagStatus,
        conditional_keys=[StructuredConfigKey.MLAG_CONFIGURATION],
    ),
    TestSpec(
        test_class=VerifyNTP,
    ),
    TestSpec(
        test_class=VerifyPathsHealth,
        conditional_keys=[StructuredConfigKey.ROUTER_PATH_SELECTION],
    ),
    TestSpec(
        test_class=VerifyReachability,
        input_factory=VerifyReachabilityInputFactory,
    ),
    TestSpec(
        test_class=VerifyReloadCause,
    ),
    TestSpec(
        test_class=VerifyRoutingProtocolModel,
        conditional_keys=[StructuredConfigKey.SERVICE_ROUTING_PROTOCOLS_MODEL],
        input_dict={"model": StructuredConfigKey.SERVICE_ROUTING_PROTOCOLS_MODEL},
    ),
    TestSpec(
        test_class=VerifySpecificIPSecConn,
        conditional_keys=[StructuredConfigKey.ROUTER_PATH_SELECTION],
        input_factory=VerifySpecificIPSecConnInputFactory,
    ),
    TestSpec(
        test_class=VerifySTPBlockedPorts,
    ),
    TestSpec(
        test_class=VerifySTPCounters,
    ),
    TestSpec(
        test_class=VerifyStunClientTranslation,
        conditional_keys=[StructuredConfigKey.ROUTER_PATH_SELECTION],
        input_factory=VerifyStunClientTranslationInputFactory,
    ),
    TestSpec(
        test_class=VerifyTelnetStatus,
    ),
    TestSpec(
        test_class=VerifyTemperature,
    ),
    TestSpec(
        test_class=VerifyTransceiversTemperature,
    ),
    TestSpec(
        test_class=VerifyZeroTouch,
    ),
]
"""List of all ANTA tests with their specifications that AVD will run by default."""

AVD_TEST_INDEX.sort(key=lambda x: x.test_class.name)
"""Sort the test index by the test class name."""

AVD_TEST_NAMES: list[str] = [test.test_class.name for test in AVD_TEST_INDEX]
"""List of all available ANTA test names that AVD will run by default."""
