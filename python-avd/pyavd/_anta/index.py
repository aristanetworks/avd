# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Test index for PyAVD ANTA tests."""

from __future__ import annotations

from pyavd._anta.input_factories import *
from pyavd._anta.lib.tests import *
from pyavd.api._anta.avd_test_spec import AvdTestSpec

AVD_TEST_INDEX: list[AvdTestSpec] = [
    AvdTestSpec(test_class=VerifyAgentLogs),
    AvdTestSpec(test_class=VerifyAPIHttpsSSL, input_factory=VerifyAPIHttpsSSLInputFactory),
    AvdTestSpec(test_class=VerifyAVTSpecificPath, input_factory=VerifyAVTSpecificPathInputFactory),
    AvdTestSpec(test_class=VerifyBGPPeerSession, input_factory=VerifyBGPPeerSessionInputFactory),
    AvdTestSpec(test_class=VerifyCoredump),
    AvdTestSpec(test_class=VerifyEnvironmentCooling, input_factory=VerifyEnvironmentCoolingInputFactory),
    AvdTestSpec(test_class=VerifyEnvironmentPower, input_factory=VerifyEnvironmentPowerInputFactory),
    AvdTestSpec(test_class=VerifyEnvironmentSystemCooling, input_factory=VerifyEnvironmentSystemCoolingInputFactory),
    AvdTestSpec(test_class=VerifyFileSystemUtilization),
    AvdTestSpec(test_class=VerifyIllegalLACP, input_factory=VerifyIllegalLACPInputFactory),
    AvdTestSpec(test_class=VerifyInterfaceDiscards),
    AvdTestSpec(test_class=VerifyInterfaceErrDisabled),
    AvdTestSpec(test_class=VerifyInterfaceErrors),
    AvdTestSpec(test_class=VerifyInterfaceUtilization),
    AvdTestSpec(test_class=VerifyInterfacesStatus, input_factory=VerifyInterfacesStatusInputFactory),
    AvdTestSpec(test_class=VerifyInventory, input_factory=VerifyInventoryInputFactory),
    AvdTestSpec(test_class=VerifyPortChannels, input_factory=VerifyPortChannelsInputFactory),
    AvdTestSpec(test_class=VerifyRunningConfigDiffs),
    AvdTestSpec(test_class=VerifyStormControlDrops, input_factory=VerifyStormControlDropsInputFactory),
    AvdTestSpec(test_class=VerifyLLDPNeighbors, input_factory=VerifyLLDPNeighborsInputFactory),
    AvdTestSpec(test_class=VerifyLoggingErrors, input_factory=VerifyLoggingErrorsInputFactory),
    AvdTestSpec(test_class=VerifyMaintenance),
    AvdTestSpec(test_class=VerifyMemoryUtilization),
    AvdTestSpec(test_class=VerifyMlagConfigSanity, input_factory=VerifyMlagConfigSanityInputFactory),
    AvdTestSpec(test_class=VerifyMlagInterfaces, input_factory=VerifyMlagInterfacesInputFactory),
    AvdTestSpec(test_class=VerifyMlagStatus, input_factory=VerifyMlagStatusInputFactory),
    AvdTestSpec(test_class=VerifyNTP),
    AvdTestSpec(test_class=VerifyOSPFNeighborState, input_factory=VerifyOSPFNeighborStateInputFactory),
    AvdTestSpec(test_class=VerifyOSPFMaxLSA, input_factory=VerifyOSPFMaxLSAInputFactory),
    AvdTestSpec(test_class=VerifySpecificPath, input_factory=VerifySpecificPathInputFactory),
    AvdTestSpec(test_class=VerifyReachability, input_factory=VerifyReachabilityInputFactory),
    AvdTestSpec(test_class=VerifyReloadCause, input_factory=VerifyReloadCauseInputFactory),
    AvdTestSpec(test_class=VerifyRoutingProtocolModel, input_factory=VerifyRoutingProtocolModelInputFactory),
    AvdTestSpec(test_class=VerifyRoutingTableEntry, input_factory=VerifyRoutingTableEntryInputFactory),
    AvdTestSpec(test_class=VerifySpecificIPSecConn, input_factory=VerifySpecificIPSecConnInputFactory),
    AvdTestSpec(test_class=VerifySTPCounters),
    AvdTestSpec(test_class=VerifyTemperature, input_factory=VerifyTemperatureInputFactory),
    AvdTestSpec(test_class=VerifyTransceiversManufacturers, input_factory=VerifyTransceiversManufacturersInputFactory),
    AvdTestSpec(test_class=VerifyTransceiversTemperature, input_factory=VerifyTransceiversTemperatureInputFactory),
    AvdTestSpec(test_class=VerifyVxlanConfigSanity, input_factory=VerifyVxlanConfigSanityInputFactory),
    AvdTestSpec(test_class=VerifyZeroTouch),
]
"""List of all ANTA tests with their specifications that AVD will run by default."""

AVD_TEST_INDEX.sort(key=lambda x: x.test_class.name)
"""Sort the test index by the test class name."""
