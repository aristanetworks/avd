# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from ansible.errors import AnsibleFilterError

from ansible_collections.arista.avd.plugins.plugin_utils.pyavd_wrappers import RaiseOnUse, wrap_filter

PLUGIN_NAME = "arista.avd.decrypt"

try:
    from pyavd.j2filters import decrypt
except ImportError as e:
    decrypt = RaiseOnUse(
        AnsibleFilterError(
            f"The '{PLUGIN_NAME}' plugin requires the 'pyavd' Python library. Got import error",
            orig_exc=e,
        ),
    )

DOCUMENTATION = r"""
---
name: decrypt
collection: arista.avd
author: Arista Ansible Team (@aristanetworks)
version_added: "3.8.0"
short_description: Decrypt supported EOS passwords.
description: |-
  - The filter is used to decrypt supported EOS passwords into clear text.
  - The filter only supports decryption from type `7` and not type `8a` for BGP, ISIS, NTP, OSPF, and TACACS+ passwords.
positional: _input
options:
  _input:
    type: string
    description: Encrypted EOS password.
    required: true
  passwd_type:
    type: string
    description: |-
      Type of password to decrypt.
      `bgp` and `ospf_simple` requires the `password` and `key` inputs.
      `ospf_message_digest` requires the `password`, `key`, `hash_algorithm`, `key_id` inputs.
      `isis` requires the `password`, `key` and `mode` inputs.
      `ntp` requires the `password` input.
      `tacacs` requires the `password` input.
    choices: ["bgp", "ospf_simple", "ospf_message_digest", "isis", "ntp", "tacacs"]
    required: true
  key:
    type: string
    description: |-
      Encryption key. The value depends on the type of password.
      For BGP passwords the key is the Neighbor IP or the BGP Peer Group Name in EOS.
      For OSPF passwords the key is the interface name (e.g., `Ethernet1`).
      For ISIS passwords the key is the ISIS instance name (from `router isis <instance name>` or `isis enable <instance name>`).
  hash_algorithm:
    type: string
    description: Hash algorithm to use with `passwd_type=ospf_message_digest`.
    choices: ["md5", "sha1", "sha256", "sha384", "sha512"]
  key_id:
    type: integer
    description: Key ID to use with `passwd_type=ospf_message_digest`.
    min: 1
    max: 255
  mode:
    type: string
    description: ISIS encryption mode (`none`, `text`, `md5`, `sha`) or shared-secret algorithm (`sha-1`, `sha-224`, `sha-256`, `sha-384`, `sha1-512`).
    choices: ["none", "text", "md5", "sha", "sha-1", "sha-224", "sha-256", "sha-384", "sha1-512"]
"""

EXAMPLES = r"""
---
- # Decrypt BGP password for peer group "IPv4-UNDERLAY-PEERS"
  cleartext: "{{ encrypted_password | arista.avd.decrypt(passwd_type='bgp', key='IPv4-UNDERLAY-PEERS') }}"

- # Decrypt OSPF simple password for interface "Ethernet1"
  cleartext: "{{ encrypted_password | arista.avd.decrypt(passwd_type='ospf_simple', key='Ethernet1') }}"

- # Decrypt OSPF message digest password for Ethernet1, MD5 and key id 1
  cleartext: "{{ encrypted_password | arista.avd.decrypt(passwd_type='ospf_message_digest', key='Ethernet1', hash_algorithm='md5', key_id='1') }}"

- # Decrypt ISIS password for instance EVPN-UNDERLAY using sha-512
  cleartext: "{{ encrypted_password | arista.avd.decrypt(passwd_type='isis', key='EVPN_UNDERLAY', mode='sha-512') }}"

- # Decrypt NTP password for NTP authentication key
  cleartext: "{{ encrypted_password | arista.avd.decrypt(passwd_type='ntp') }}"

- # Decrypt TACACS+ password
  cleartext: "{{ encrypted_password | arista.avd.decrypt(passwd_type='tacacs') }}"
"""

RETURN = r"""
---
_value:
  description: Decrypted cleartext password.
  type: string
"""


class FilterModule:
    def filters(self) -> dict:
        return {
            "decrypt": wrap_filter(PLUGIN_NAME)(decrypt),
        }
