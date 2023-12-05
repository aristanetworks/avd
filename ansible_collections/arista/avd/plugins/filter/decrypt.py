# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError, AristaAvdMissingVariableError
from ansible_collections.arista.avd.plugins.plugin_utils.password_utils import METHODS_DIR

DOCUMENTATION = r"""
---
name: decrypt
collection: arista.avd
author: Arista Ansible Team (@aristanetworks)
version_added: "3.8.0"
short_description: Decrypt supported EOS passwords.
description:
  - The filter is used to decrypt supported EOS passwords into clear text.
  - Note - For now this filter only supports decryption from type C(7) and not type C(8a) for OSPF and BGP passwords.
positional: _input
options:
  _input:
    type: string
    description: Encrypted EOS password.
    required: true
  passwd_type:
    type: string
    description:
      - Type of password to decrypt.
      - C(bgp) and C(ospf_simple) requires the I(password) and I(key) inputs.
      - C(ospf_message_digest) requires the I(password), I(key), I(hash_algorithm), I(key_id) inputs.
    choices: ["bgp", "ospf_simple", "ospf_message_digest"]
    required: true
  key:
    type: string
    description:
      - Encryption key. The value depends on the type of password.
      - For BGP passwords the key is the Neighbor IP or the BGP Peer Group Name in EOS.
      - For OSPF passwords the key is the interface name (e.g., C(Ethernet1)).
    required: true
  hash_algorithm:
    type: string
    description:
      - Hash algorithm to use with I(passwd_type="ospf_message_digest").
    choices: ["md5", "sha1", "sha256", "sha384", "sha512"]
  key_id:
    type: integer
    description:
      - Key ID to use with I(passwd_type="ospf_message_digest").
    min: 1
    max: 255
"""

EXAMPLES = r"""
---
- # Decrypt BGP password for peer group "IPv4-UNDERLAY-PEERS"
  cleartext: "{{ encrypted_password | arista.avd.decrypt(passwd_type='bgp', key='IPv4-UNDERLAY-PEERS') }}"

- # Decrypt OSPF simple password for interface "Ethernet1"
  cleartext: "{{ encrypted_password | arista.avd.decrypt(passwd_type='ospf_simple', key='Ethernet1') }}"

- # Decrypt OSPF message digest password for Ethernet1, MD5 and key id 1
  cleartext: "{{ encrypted_password | arista.avd.decrypt(passwd_type='ospf_message_digest', key='Ethernet1', hash_algorithm='md5', key_id='1') }}"
"""

RETURN = r"""
---
_value:
  description: Decrypted cleartext password.
  type: string
"""


def decrypt(value, passwd_type=None, key=None, **kwargs) -> str:
    """
    Umbrella function to execute the correct decrypt method based on the input type
    """
    if not passwd_type:
        raise AristaAvdMissingVariableError("type keyword must be present to use this test")
    try:
        decrypt_method = METHODS_DIR[passwd_type][1]
    except KeyError as exc:
        raise AristaAvdError(f"Type {passwd_type} is not supported for the decrypt filter") from exc
    return decrypt_method(str(value), key=key, **kwargs)


class FilterModule(object):
    def filters(self):
        return {
            "decrypt": decrypt,
        }
