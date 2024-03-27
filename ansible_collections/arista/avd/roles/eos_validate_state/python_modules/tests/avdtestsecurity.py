# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import logging
from functools import cached_property

from ansible_collections.arista.avd.plugins.plugin_utils.eos_validate_state_utils.avdtestbase import AvdTestBase
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get

LOGGER = logging.getLogger(__name__)


class AvdTestAPIHttpsSSL(AvdTestBase):
    """
    AvdTestAPIHttpsSSL class for eAPI HTTPS SSL tests.
    """

    anta_module = "anta.tests.security"

    @cached_property
    def test_definition(self) -> dict | None:
        """
        Generates the proper ANTA test definition for all eAPI HTTPS SSL tests.

        Returns:
            test_definition (dict): ANTA test definition.
        """
        anta_tests = []

        if (profile := get(self.structured_config, "management_api_http.https_ssl_profile")) is None:
            LOGGER.info("No https ssl profile found. %s is skipped.", self.__class__.__name__)
            return None

        anta_tests.append({"VerifyAPIHttpsSSL": {"profile": profile, "result_overwrite": {"custom_field": f"eAPI HTTPS SSL Profile: {profile}"}}})

        return {self.anta_module: anta_tests}
