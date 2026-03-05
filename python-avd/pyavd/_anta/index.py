# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Test index for PyAVD ANTA tests."""

from __future__ import annotations

from pyavd._anta.input_factories import *
from pyavd._anta.lib.tests import *
from pyavd.api.anta.avd_test_spec import AVDTestSpec

AVD_TEST_INDEX: list[AVDTestSpec] = [
    AVDTestSpec(test_class=VerifyAgentLogs),
    AVDTestSpec(test_class=VerifyAPIHttpsSSL, input_factory=VerifyAPIHttpsSSLInputFactory),
    AVDTestSpec(test_class=VerifyAVTSpecificPath, input_factory=VerifyAVTSpecificPathInputFactory),
    AVDTestSpec(test_class=VerifyBGPPeerSession, input_factory=VerifyBGPPeerSessionInputFactory),
    AVDTestSpec(test_class=VerifyCoredump),
    AVDTestSpec(test_class=VerifyEnvironmentCooling, input_factory=VerifyEnvironmentCoolingInputFactory),
    AVDTestSpec(test_class=VerifyEnvironmentPower, input_factory=VerifyEnvironmentPowerInputFactory),
    AVDTestSpec(test_class=VerifyEnvironmentSystemCooling, input_factory=VerifyEnvironmentSystemCoolingInputFactory),
    AVDTestSpec(test_class=VerifyFileSystemUtilization),
    AVDTestSpec(test_class=VerifyIllegalLACP, input_factory=VerifyIllegalLACPInputFactory),
    AVDTestSpec(test_class=VerifyInterfaceDiscards),
    AVDTestSpec(test_class=VerifyInterfaceErrDisabled),
    AVDTestSpec(test_class=VerifyInterfaceErrors),
    AVDTestSpec(test_class=VerifyInterfaceUtilization),
    AVDTestSpec(test_class=VerifyInterfacesStatus, input_factory=VerifyInterfacesStatusInputFactory),
    AVDTestSpec(test_class=VerifyInventory, input_factory=VerifyInventoryInputFactory),
    AVDTestSpec(test_class=VerifyPortChannels, input_factory=VerifyPortChannelsInputFactory),
    AVDTestSpec(test_class=VerifyRunningConfigDiffs),
    AVDTestSpec(test_class=VerifyStormControlDrops, input_factory=VerifyStormControlDropsInputFactory),
    AVDTestSpec(test_class=VerifyLLDPNeighbors, input_factory=VerifyLLDPNeighborsInputFactory),
    AVDTestSpec(test_class=VerifyLoggingErrors, input_factory=VerifyLoggingErrorsInputFactory),
    AVDTestSpec(test_class=VerifyMaintenance),
    AVDTestSpec(test_class=VerifyMemoryUtilization),
    AVDTestSpec(test_class=VerifyMlagConfigSanity, input_factory=VerifyMlagConfigSanityInputFactory),
    AVDTestSpec(test_class=VerifyMlagInterfaces, input_factory=VerifyMlagInterfacesInputFactory),
    AVDTestSpec(test_class=VerifyMlagStatus, input_factory=VerifyMlagStatusInputFactory),
    AVDTestSpec(test_class=VerifyNTP),
    AVDTestSpec(test_class=VerifyOSPFNeighborState, input_factory=VerifyOSPFNeighborStateInputFactory),
    AVDTestSpec(test_class=VerifyOSPFMaxLSA, input_factory=VerifyOSPFMaxLSAInputFactory),
    AVDTestSpec(test_class=VerifySpecificPath, input_factory=VerifySpecificPathInputFactory),
    AVDTestSpec(test_class=VerifyReachability, input_factory=VerifyReachabilityInputFactory),
    AVDTestSpec(test_class=VerifyReloadCause, input_factory=VerifyReloadCauseInputFactory),
    AVDTestSpec(test_class=VerifyRoutingProtocolModel, input_factory=VerifyRoutingProtocolModelInputFactory),
    AVDTestSpec(test_class=VerifyRoutingTableEntry, input_factory=VerifyRoutingTableEntryInputFactory),
    AVDTestSpec(test_class=VerifySpecificIPSecConn, input_factory=VerifySpecificIPSecConnInputFactory),
    AVDTestSpec(test_class=VerifySTPCounters),
    AVDTestSpec(test_class=VerifyTemperature, input_factory=VerifyTemperatureInputFactory),
    AVDTestSpec(test_class=VerifyTransceiversManufacturers, input_factory=VerifyTransceiversManufacturersInputFactory),
    AVDTestSpec(test_class=VerifyTransceiversTemperature, input_factory=VerifyTransceiversTemperatureInputFactory),
    AVDTestSpec(test_class=VerifyVxlanConfigSanity, input_factory=VerifyVxlanConfigSanityInputFactory),
    AVDTestSpec(test_class=VerifyZeroTouch),
]
"""List of all ANTA tests with their specifications that AVD will run by default."""

AVD_TEST_INDEX.sort(key=lambda x: x.test_class.name)
"""Sort the test index by the test class name."""
