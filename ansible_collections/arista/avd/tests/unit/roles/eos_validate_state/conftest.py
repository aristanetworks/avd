# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pytest import Metafunc


def build_test_id(val: dict) -> str:
    """
    Build a proper test ID for AvdTestBase subclasses unit tests: `<test_module>-<test_name>`

    Examples output:

    `::test_avd_tests[AvdTestBGP-missing-router-bgp]`

    `::test_avd_tests[AvdTestBGP-missing-service-routing-protocols-model]`
    """
    return f"{val['test_module']}-{val['test_name']}"


def pytest_generate_tests(metafunc: Metafunc) -> None:
    """
    This function is called during test collection.

    It will parametrize test cases based on the `DATA` data structure defined in `tests.unit.roles.eos_validate_state.tests` modules.

    Test IDs are generated using the `build_test_id` function above.
    """
    if "tests.unit.roles.eos_validate_state.tests" in metafunc.module.__package__:
        metafunc.parametrize("data", metafunc.module.DATA, ids=build_test_id)
