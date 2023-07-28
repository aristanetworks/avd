# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
#
# snmp_hash filter
#

__metaclass__ = type

import hashlib

from ansible.errors import AnsibleFilterError

DOCUMENTATION = r"""
---
name: snmp_hash
collection: arista.avd
author: Arista Ansible Team (@aristanetworks)
version_added: "3.6.0"
short_description: Compute localized SNMP passphrases
description:
  - Key localization as described in L(RFC 2574 section 2.6,https://www.rfc-editor.org/rfc/rfc2574.html#section-2.6)
positional: _input
options:
  _input:
    description: Dictionary with SNMP passphrase details.
    type: dictionary
    required: true
    suboptions:
      passphrase:
        type: string
        required: true
        description:
          - The passphrase to localize.
          - This is the "auth" passphrase when the I(priv) argument is not set.
          - If I(priv) is set, it is the "priv" passphrase.
      auth:
        type: string
        description: Auth type
        choices: ["md5", "sha", "sha224", "sha256", "sha384", "sha512"]
        required: true
      engine_id:
        type: string
        description: A hexadecimal string containing the engine_id to be used to localize the passphrase
        required: true
      priv:
        type: string
        description: Priv type
        choices: ["des", "aes", "aes192", "aes256"]
"""


RETURN = r"""
---
_value:
  description:
    - The localized key generated from the passphrase using I(auth) type.
    - If required the key is truncated to match the appropriate keylength for the I(priv) type.
  type: string
"""

PRIV_KEY_LENGTH = {"des": 128, "aes": 128, "aes192": 192, "aes256": 256}


def get_hash_object(auth_type: str) -> hashlib._hashlib.HASH:
    """
    :param auth_type: a string in [md5|sha|sha224|sha256|sha384|sha512]

    :return: an instance of hashlib._hashlib.HASH corresponding to the
             auth_type

    :raises: AnsibleFilterError, when the auth_type is not valid
    """
    auth = "sha1" if auth_type == "sha" else auth_type
    try:
        return hashlib.new(auth)
    except ValueError:
        raise AnsibleFilterError(f"{auth_type} is not a valid Auth algorithm for SNMPv3") from ValueError


def key_from_passphrase(passphrase: str, auth_type: str) -> str:
    """
    RFC 2574 section A.2 algorithm
    https://www.rfc-editor.org/rfc/rfc2574.html#appendix-A2

    :param passphrase: the passphrase to use to generate the key
    :param auth_type: a string in [md5|sha|sha224|sha256|sha384|sha512]

    :return: the key generated from the passphrase using auth_type as per
             the algorithm described in the RFC.

    :raises: AnsibleFilterError, when the auth_type is not valid
    """
    b_passphrase = passphrase
    if isinstance(passphrase, str):
        b_passphrase = passphrase.encode("UTF-8", errors="strict")
    hash_object = get_hash_object(auth_type)
    count = 0
    password_index = 0
    password_length = len(b_passphrase)
    while count < 1048576:
        cp = bytearray()
        for index in range(0, 64):
            cp.append(b_passphrase[password_index % password_length])
            password_index += 1
        hash_object.update(cp)
        count += 64
    return hash_object.hexdigest()


def localize_passphrase(passphrase: str, auth_type: str, engine_id: str, priv_type: str = None) -> str:
    """
    Key localization as described in RFC 2574, section 2.6
    https://www.rfc-editor.org/rfc/rfc2574.html#section-2.6

    :param passphrase: the passphrase to localize, if priv_type is None
                       it is the auth passphrase else it is the priv
                       passphrase
    :param auth_type: a string in [md5|sha|sha224|sha256|sha384|sha512]
    :param engine_id: an hexadecimal string containing the engine_id to be
                      used to localize the key
    :param auth_type: an optional argument indicating the priv algorithm
                    in [des|aes|aes192|aes256]

    :return: the localized key generated from the passphrase using auth_type
             and if required truncated to match the appropriate keylength for
             the priv_type.

    :raises: AnsibleFilterError, when the auth_type or priv_type is not valid
             or if the engined_id is not a proper hexadecimal string
    """

    key = bytes.fromhex(key_from_passphrase(passphrase, auth_type))
    hash_object = get_hash_object(auth_type)
    try:
        hash_object.update(key + bytes.fromhex(engine_id) + key)
    except ValueError as error:
        raise AnsibleFilterError(f"engine ID {engine_id} is not an hexadecimal string") from error
    localized_key = hash_object.hexdigest()
    if priv_type is not None:
        try:
            while len(localized_key) * 4 < PRIV_KEY_LENGTH[priv_type]:
                hash_object = get_hash_object(auth_type)
                hash_object.update(bytes.fromhex(localized_key))
                localized_key = localized_key + hash_object.hexdigest()
            # Truncate ithe key if required
            localized_key = localized_key[: PRIV_KEY_LENGTH[priv_type] // 4]
        except KeyError as error:
            raise AnsibleFilterError(f"{priv_type} is not a valid Priv algorithm for SNMPv3") from error
    return localized_key


def hash_passphrase(input_dict):
    try:
        passphrase = input_dict["passphrase"]
        auth_type = input_dict["auth"]
        engine_id = input_dict["engine_id"]
    except KeyError as exc:
        raise AnsibleFilterError() from exc
    try:
        priv_type = input_dict["priv"]
    except KeyError:
        priv_type = None

    return localize_passphrase(passphrase, auth_type, engine_id, priv_type)


class FilterModule(object):
    def filters(self):
        return {
            "hash_passphrase": hash_passphrase,
        }
