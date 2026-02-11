# Copyright (c) 2025-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import pytest
from anta.tests.hardware import VerifyInventory
from anta.tests.security import VerifyAPIHttpsSSL
from anta.tests.system import VerifyFileSystemUtilization

from pyavd._anta.input_factories import VerifyAPIHttpsSSLInputFactory
from pyavd.api.anta import AVDTestSpec


def test_avd_test_spec_no_input_model() -> None:
    """Init passes when the ANTA test has no Input model and no factory is provided."""
    test_spec = AVDTestSpec(test_class=VerifyFileSystemUtilization)
    assert test_spec.input_factory is None


def test_avd_test_spec_required_input_no_factory() -> None:
    """Init fails when ANTA test has required inputs but no factory is provided."""
    with pytest.raises(ValueError, match="AVDTestSpec for VerifyAPIHttpsSSL must have `input_factory`"):
        AVDTestSpec(test_class=VerifyAPIHttpsSSL)


def test_avd_test_spec_required_input_with_factory() -> None:
    """Init passes when ANTA test has required inputs and a factory is provided."""
    test_spec = AVDTestSpec(test_class=VerifyAPIHttpsSSL, input_factory=VerifyAPIHttpsSSLInputFactory)
    assert test_spec.input_factory == VerifyAPIHttpsSSLInputFactory


def test_avd_test_spec_optional_input_no_factory() -> None:
    """Init passes when ANTA test has inputs, but they are all optional."""
    test_spec = AVDTestSpec(test_class=VerifyInventory)
    assert test_spec.input_factory is None
