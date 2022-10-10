from __future__ import absolute_import, division, print_function

__metaclass__ = type

import pytest
from jinja2.runtime import Undefined

from ansible_collections.arista.avd.plugins.test.bgp_valid_password import TestModule, bgp_valid_password
from ansible_collections.arista.avd.plugins.plugin_utils.utils import AristaAvdError

MISSING_VALUES = [(Undefined, "blah"), (None, "blah"), (42, "blah"), ("blah", Undefined), ("blah", None), ("blah", 42)]
# password used is "arista"
VALID_PASSWORD_KEY_PAIRS = [("42.42.42.42", "3QGcqpU2YTwKh2jVQ4Vj/A=="), ("AVD-TEST", "bM7t58t04qSqLHAfZR/Szg==")]
INVALID_PASSWORD_KEY_PAIRS = [("10.42.42.43", "3QGcqpU2YTwKh2jVQ4Vj/A=="), ("AVD-TEST-DUMMY", "bM7t58t04qSqLHAfZR/Szg==")]


f = TestModule()


@pytest.mark.parametrize("key, password", MISSING_VALUES)
def test_bgp_valid_password_missing_arg(key, password):
    """
    Missing values - expect False
    """
    assert bgp_valid_password(password, key) is False


@pytest.mark.parametrize("key, password", VALID_PASSWORD_KEY_PAIRS)
def test_bgp_valid_password_success(key, password):
    """
    Valid cases for both neighbor IP and peer group name
    """
    assert bgp_valid_password(password, key) is True


@pytest.mark.parametrize("key, password", INVALID_PASSWORD_KEY_PAIRS)
def test_bgp_valid_password_failure(key, password):
    """
    Invalid cases for both neighbor IP and peer group name
    """
    with pytest.raises(AristaAvdError):
        bgp_valid_password(password, key)


def test_bgp_valid_password_module():
    """
    Assert the bgp_valid_password test is part of the module
    """
    resp = f.tests()
    assert isinstance(resp, dict)
    assert "bgp_valid_password" in resp.keys()
