# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.plugin_utils.eos_validate_state_utils.avdtestbase import AvdTestBase


class AvdTestMLAG(AvdTestBase):
    """
    AvdTestMLAG class for MLAG tests.
    """

    anta_module = "anta.tests.mlag"
    categories = ["MLAG"]

    @cached_property
    def test_definition(self) -> dict:
        """
        Generates the proper ANTA test definition for all MLAG tests.

        Returns:
            test_definition (dict): ANTA test definition.
        """
        if self.logged_get(key="mlag_configuration", logging_level="INFO") is None:
            return None

        anta_tests = [
            {
                "VerifyMlagStatus": {
                    "result_overwrite": {"categories": self.categories, "description": "MLAG State active & Status connected", "custom_field": "MLAG"}
                }
            },
        ]

        return {self.anta_module: anta_tests}
