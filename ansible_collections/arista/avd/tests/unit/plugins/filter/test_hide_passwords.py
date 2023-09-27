# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import absolute_import, division, print_function

__metaclass__ = type

from contextlib import nullcontext as does_not_raise

import pytest

from ansible_collections.arista.avd.plugins.filter.hide_passwords import FilterModule, hide_passwords
from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError

f = FilterModule()

INPUT_HIDE_PASSWORDS = [
    pytest.param("dummy", False, "dummy", does_not_raise(), id="Not Removed"),
    pytest.param("dummy", True, "<removed>", does_not_raise(), id="Removed"),
    pytest.param("dummy", "wrong-type", None, pytest.raises(AristaAvdError), id="Removed"),
]


@pytest.mark.parametrize("value, hide_passwords_flag, expected, raise_context", INPUT_HIDE_PASSWORDS)
def test_hide_passwords(value, hide_passwords_flag, expected, raise_context):
    """
    Test hide_passwords
    """
    with raise_context:
        assert hide_passwords(value, hide_passwords_flag) == expected


def test_hide_passwords_module():
    """
    Assert:
      * hide_passwords
    filters are part of the module
    """
    resp = f.filters()
    assert isinstance(resp, dict)
    assert "hide_passwords" in resp.keys()
