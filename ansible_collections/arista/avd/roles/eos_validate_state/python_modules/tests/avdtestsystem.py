# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.plugin_utils.eos_validate_state_utils.avdtestbase import AvdTestBase


class AvdTestNTP(AvdTestBase):
    """
    AvdTestNTP class for NTP tests.
    """

    anta_module = "anta.tests.system"
    categories = ["NTP"]
    description = "Synchronised with NTP server"

    @cached_property
    def test_definition(self) -> dict:
        """
        Generates the proper ANTA test definition for all NTP tests.

        Returns:
            test_definition (dict): ANTA test definition.
        """

        anta_tests = [
            {"VerifyNTP": {"result_overwrite": {"categories": self.categories, "description": self.description, "custom_field": "NTP"}}},
        ]

        return {self.anta_module: anta_tests}


class AvdTestReloadCause(AvdTestBase):
    """
    AvdTestReloadCause class for the reload cause of the device.
    """

    anta_module = "anta.tests.system"
    categories = ["Reload Cause"]
    description = "Reload Cause - Reload requested by the user"

    @cached_property
    def test_definition(self) -> dict:
        """
        Generates the proper ANTA test definition for the reload cause test.

        Returns:
            test_definition (dict): ANTA test definition.
        """

        anta_tests = [
            {"VerifyReloadCause": {"result_overwrite": {"categories": self.categories, "description": self.description, "custom_field": "Reload Cause"}}},
        ]

        return {self.anta_module: anta_tests}
