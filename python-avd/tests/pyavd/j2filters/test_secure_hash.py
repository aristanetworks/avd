# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

from __future__ import annotations

from unittest.mock import patch

import pytest

from pyavd.j2filters import secure_hash

INVALID_PASSWORDS = [
    pytest.param(True, "sha512_password", TypeError, "SHA-512 password hashing failed - check the input parameters of arista.avd.secure_hash"),
]

VALID_PASSWORDS = [
    pytest.param(
        "pass",
        "DxaFhAPPrrOzqgZV",
        "sha512_password",
        "$6$DxaFhAPPrrOzqgZV$pdiZUeB6SRwVsiTzW1jPQvBy3eP5DqJWjZ1Fd3mpO8E9tjJ/ntaiZx7CaIIkfYyOnzgV92AW7fFSWnQzzowzP.",
    )
]

INVALID_HASH_HASH_TYPES = [
    pytest.param(
        "pass",
        "",
        ValueError,
        "The hash_type key does not support the value ''. The value used with hash_type must be one of \\['sha512_password'\\]",
    ),
    pytest.param(
        "pass",
        "user_p",
        ValueError,
        "The hash_type key does not support the value 'user_p'. The value used with hash_type must be one of \\['sha512_password'\\]",
    ),
]


class TestSecureHashFilter:
    @pytest.mark.parametrize(("cleartext_password", "hash_type", "expected_raise", "expected_raise_message"), INVALID_PASSWORDS)
    def test_secure_hash_invalid_password(self, cleartext_password: str, hash_type: str, expected_raise: type[Exception], expected_raise_message: str) -> None:
        """Test secure_hash for invalid password types (non-string)."""
        with pytest.raises(expected_raise, match=expected_raise_message):
            secure_hash(cleartext_password, salt="AAAAAAAAA", hash_type=hash_type)

    @pytest.mark.parametrize(("cleartext_password", "salt", "hash_type", "expected_password"), VALID_PASSWORDS)
    def test_secure_hash_valid_password(self, cleartext_password: str, salt: str, hash_type: str, expected_password: str) -> None:
        """Test secure_hash for invalid password types (non-string)."""
        assert secure_hash(cleartext_password, salt=salt, hash_type=hash_type) == expected_password

    @pytest.mark.parametrize(("cleartext_password", "hash_type", "expected_raise", "expected_raise_message"), INVALID_HASH_HASH_TYPES)
    def test_secure_hash_invalid_type(self, cleartext_password: str, hash_type: str, expected_raise: type[Exception], expected_raise_message: str) -> None:
        """Test secure_hash for invalid hash_type."""
        with pytest.raises(expected_raise, match=expected_raise_message):
            secure_hash(cleartext_password, salt="AAAAAAAAA", hash_type=hash_type)

    def test_secure_hash_uncaught_exception(self) -> None:
        """Test when an uncaught exception is returned by pyavd-utils."""
        with (
            patch("pyavd.j2filters.secure_hash.sha512_crypt", side_effect=Exception("foo")),
            pytest.raises(Exception, match=r"SHA-512 password hashing failed - check the input parameters of arista.avd.secure_hash"),
        ):
            secure_hash("aaaaaa", salt="AAAAAAAAAAAA")
