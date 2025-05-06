# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
# For now we allow docstrings in stubs
# ruff: noqa: PYI021

def sha512_crypt(password: str, salt: str) -> str:
    """
    Computes the SHA512 crypt value for the password given the salt.

    The number of rounds is hardcoded to 5000 as expected by EOS.

    Args:
      password: The password.
      salt: The salt to use (should be 16 in length max or will be truncated).

    Returns:
      The sha512 crypt value.
    """
