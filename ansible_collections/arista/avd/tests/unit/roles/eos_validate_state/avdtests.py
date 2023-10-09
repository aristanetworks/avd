# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from ansible_collections.arista.avd.plugins.plugin_utils.eos_validate_state_utils import AvdTestBase
from ansible_collections.arista.avd.plugins.plugin_utils.utils import load_python_class

if TYPE_CHECKING:
    from pytest import LogCaptureFixture


def test_avd_tests(caplog: LogCaptureFixture, data: dict) -> None:
    """
    Generic function for all AvdTestBase subclasses unit tests.
    """
    caplog.set_level(logging.INFO)
    avd_test_class = load_python_class("ansible_collections.arista.avd.roles.eos_validate_state.python_modules.tests", data["test_module"], AvdTestBase)
    avd_test_bgp = avd_test_class(device_name="DC1-SPINE1", hostvars=data["hostvars"])
    result = avd_test_bgp.render()
    assert result == data["expected_result"]

    if data["expected_log"] and data["expected_log_level"]:
        found_expected_log = any(record.message == data["expected_log"] and record.levelname == data["expected_log_level"] for record in caplog.records)
        assert found_expected_log, f"Expected log message not found: {data['expected_log']}"
