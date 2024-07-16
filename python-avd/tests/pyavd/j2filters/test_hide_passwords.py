# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import absolute_import, division, print_function

__metaclass__ = type

import pytest
from pyavd.j2filters import hide_passwords

VALID_INPUT_HIDE_PASSWORDS = [
    ("dummy", False, "dummy"),
    ("dummy", True, "<removed>"),
    (None, True, "<removed>"),
]

INVALID_INPUT_HIDE_PASSWORDS = [("password", "wrong_type_flag", "wrong_type_flag in hide_passwords filter is not of type bool")]


class TestHidePasswordsFilter:
    @pytest.mark.parametrize("value, hide_passwords_flag, hidden_password", VALID_INPUT_HIDE_PASSWORDS)
    def test_hide_passwords_valid(self, value, hide_passwords_flag, hidden_password):
        """
        Test hide_passwords
        """
        assert hide_passwords(value, hide_passwords_flag) == hidden_password

    @pytest.mark.parametrize("value, hide_passwords_flag, error_msg", INVALID_INPUT_HIDE_PASSWORDS)
    def test_hide_passwords_invalid(self, value, hide_passwords_flag, error_msg):
        with pytest.raises(TypeError) as exc_info:
            hide_passwords(value, hide_passwords_flag)
        assert str(exc_info.value) == error_msg
