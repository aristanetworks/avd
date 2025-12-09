# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.


HASH_INPUT_TYPE = ["sha512_password"]


def sha512_password(clear_password: str, salt: str) -> str:
    """
    Generate a SHA-512 password hash from a cleartext password for a local user.

    Args:
        clear_password: The cleartext password provided by the user that will be hashed.
        salt: Salt value to be used when creating password hash. A randomly generated salt will be used unless the user specifies one.

    Returns:
        The SHA-512 password hash.

    Raises:
        TypeError: If the password is not of type 'str'.
        ValueError: If sha512_crypt fails for any reason.
    """
    # Importing inside the function to avoid neeedind pyavd-utils in the build dependencies.
    from pyavd_utils.passwords import sha512_crypt  # noqa: PLC0415

    try:
        # setting the rounds parameter to 5000 to omit rounds from the hash string, similar to EOS implementation
        return sha512_crypt(clear_password, salt)
    except Exception as exc:
        msg = f"SHA-512 password hashing failed - check the input parameters of arista.avd.secure_hash: {exc}"
        raise type(exc)(msg) from exc


def secure_hash(user_input: str, salt: str, hash_type: str = "sha512_password") -> str:
    """
    Returns a hash for a given input.

    Args:
        user_input: the user input cleartext that will be hashed.
        salt: Salt value to be used when creating password hash. It must be between 1 and 16 characters.
        hash_type: the use case for the cleartext provided by the user.

    Returns:
        The hash digest.

    Raises:
        ValueError: if the hash_type value provided by the user is not supported.
    """
    if hash_type not in HASH_INPUT_TYPE:
        msg = f"The hash_type key does not support the value '{hash_type}'. The value used with hash_type must be one of {HASH_INPUT_TYPE}"
        raise ValueError(msg)

    return sha512_password(user_input, salt)
