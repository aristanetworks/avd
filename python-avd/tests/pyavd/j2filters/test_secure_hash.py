# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

from __future__ import annotations

import re
from unittest.mock import patch

import pytest

from pyavd.j2filters import secure_hash

sha512_regex = r"^\$6\$[A-Za-z0-9\.\/]{1,16}\$[A-Za-z0-9\.\/]{86}"


INVALID_PASSWORDS = [
    pytest.param(True, "sha512_password", TypeError, "Password MUST be of type 'str' but is of type <class 'bool'>"),
    pytest.param([], "sha512_password", TypeError, "Password MUST be of type 'str' but is of type <class 'list'>"),
    pytest.param({}, "sha512_password", TypeError, "Password MUST be of type 'str' but is of type <class 'dict'>"),
]

INVALID_SALTS = [
    pytest.param("password", "DxaFhA,rzqgZV", "sha512_password", ValueError, "Salt value MUST only contain the characters ./0-9A-Za-z"),
    pytest.param("password", "abcdefghijklmnopqrs", "sha512_password", ValueError, "Salt value length MUST not be greater than 16 characters but is 19"),
    pytest.param("password", [], "sha512_password", TypeError, "Salt value MUST be of type 'str' but is of type <class 'list'>"),
]

VALID_PASSWORD_FORMAT = [
    pytest.param("rAnDoM123456789", "sha512_password", sha512_regex),
    pytest.param("ar!st@Us95r", "sha512_password", sha512_regex),
]

VALID_PASSWORDS = [
    pytest.param(
        "pass",
        "DxaFhAPPrrOzqgZV",
        "sha512_password",
        "$6$DxaFhAPPrrOzqgZV$pdiZUeB6SRwVsiTzW1jPQvBy3eP5DqJWjZ1Fd3mpO8E9tjJ/ntaiZx7CaIIkfYyOnzgV92AW7fFSWnQzzowzP.",
    ),
    pytest.param(
        "pass123",
        "LYP1.qA2GBfCkgjG",
        "sha512_password",
        "$6$LYP1.qA2GBfCkgjG$fKJUO/Rd0WoedrBv1ZQRHJgXAQVto7FiRB7qftH5ojHhhazwjG8r.J54ekLskS6M7ET/jDwhttxub1k4Af.Re1",
    ),
    pytest.param(
        "987pass",
        "L6FWaPqBAGw9cchr",
        "sha512_password",
        "$6$L6FWaPqBAGw9cchr$72Aw0G3LEmjzR2JFaC4vKzuB8Y1QhSQWoNAvFeCT0/i1td7LVxcGu/d3C9zBGOufbE.fQa/dRpQVLoFuaM4GH0",
    ),
    pytest.param(
        "@rista",
        "md1wAfP0nC2/4M8d",
        "sha512_password",
        "$6$md1wAfP0nC2/4M8d$qlQTd/ShOtMBImVvdXxVo.4MqLFI6BUQHoAqqyUUyKWTdtGi7wMQBqkDCRJ.ZLvotQtOyzYXQGuvc8SsAGyFM1",
    ),
]

INVALID_HASH_HASH_TYPES = [
    pytest.param(
        "pass",
        "",
        ValueError,
        "The hash_type key does not support the value ''. The value used with hash_type must be in \\['sha512_password'\\]",
    ),
    pytest.param(
        "pass",
        "user_p",
        ValueError,
        "The hash_type key does not support the value 'user_p'. The value used with hash_type must be in \\['sha512_password'\\]",
    ),
]


class TestSecureHashFilter:
    @pytest.mark.parametrize(("cleartext_password", "hash_type", "expected_raise", "expected_raise_message"), INVALID_PASSWORDS)
    def test_secure_hash_invalid_password(self, cleartext_password: str, hash_type: str, expected_raise: type[Exception], expected_raise_message: str) -> None:
        """Test secure_hash for invalid password types (non-string)."""
        with pytest.raises(expected_raise, match=expected_raise_message):
            secure_hash(cleartext_password, hash_type)

    @pytest.mark.parametrize(("cleartext_password", "salt", "hash_type", "expected_raise", "expected_raise_message"), INVALID_SALTS)
    def test_secure_hash_invalid_salt(
        self, cleartext_password: str, salt: str, hash_type: str, expected_raise: type[Exception], expected_raise_message: str
    ) -> None:
        """Test secure_hash for invalid salt values."""
        with pytest.raises(expected_raise, match=expected_raise_message):
            secure_hash(cleartext_password, salt, hash_type)

    @pytest.mark.parametrize(("cleartext_password", "hash_type", "expected_raise", "expected_raise_message"), INVALID_HASH_HASH_TYPES)
    def test_secure_hash_invalid_type(self, cleartext_password: str, hash_type: str, expected_raise: type[Exception], expected_raise_message: str) -> None:
        """Test secure_hash for invalid hash_type."""
        with pytest.raises(expected_raise, match=expected_raise_message):
            secure_hash(cleartext_password, salt="AAAAAAAAA", hash_type=hash_type)

    @pytest.mark.parametrize(("cleartext_password", "hash_type", "regex_of_hashed_password"), VALID_PASSWORD_FORMAT)
    def test_secure_hash_password_format(self, cleartext_password: str, hash_type: str, regex_of_hashed_password: str) -> None:
        """Test the format of the hash output from secure_hash i.e. $6$<salt-value>$<hashed-password>."""
        hashed_password = secure_hash(cleartext_password, salt="AAAAAAAAAAAA", hash_type=hash_type)
        assert re.fullmatch(regex_of_hashed_password, hashed_password)

    def test_secure_hash_uncaught_execption(self) -> None:
        """Test when an uncaught exception is returned by pyavd-utils."""
        with (
            patch("pyavd_utils.passwords.sha512_crypt", side_effect=Exception("foo")),
            pytest.raises(Exception, match=r"SHA-512 password hashing failed - check the input parameters of arista.avd.secure_hash"),
        ):
            secure_hash("aaaaaa", salt="AAAAAAAAAAAA")
