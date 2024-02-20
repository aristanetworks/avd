# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
#
# snmp_hash filter
#
from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible.errors import AnsibleFilterError

try:
    from pyavd.j2filters.snmp_hash import snmp_hash

    HAS_PYAVD = True
except ImportError:
    HAS_PYAVD = False

DOCUMENTATION = r"""
---
name: snmp_hash
collection: arista.avd
author: Arista Ansible Team (@aristanetworks)
version_added: "3.6.0"
short_description: Compute localized SNMP passphrases
description:
  - Key localization as described in [RFC 2574 section 2.6](https://www.rfc-editor.org/rfc/rfc2574.html#section-2.6)
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
          - This is the "auth" passphrase when the `priv` argument is not set.
          - If `priv` is set, it is the "priv" passphrase.
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
    - The localized key generated from the passphrase using `auth` type.
    - If required the key is truncated to match the appropriate keylength for the `priv` type.
  type: string
"""


class FilterModule(object):
    def filters(self):
        if not HAS_PYAVD:
            raise AnsibleFilterError("The Python library 'pyavd' cound not be found. Please install using 'pip3 install'")
        return {
            "snmp_hash": snmp_hash,
        }
