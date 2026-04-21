# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
#
# secure_hash filter
#


from ansible.errors import AnsibleFilterError

from ansible_collections.arista.avd.plugins.plugin_utils.pyavd_wrappers import RaiseOnUse, wrap_filter

PLUGIN_NAME = "arista.avd.secure_hash"

try:
    from pyavd.j2filters import secure_hash
except ImportError as e:
    secure_hash = RaiseOnUse(
        AnsibleFilterError(
            f"The '{PLUGIN_NAME}' plugin requires the 'pyavd' Python library. Got import error",
            orig_exc=e,
        ),
    )


DOCUMENTATION = r"""
---
name: secure_hash
collection: arista.avd
author: Arista Ansible Team (@aristanetworks)
version_added: "5.2.0"
short_description: Generate an EOS supported hash digest.
description: |-
  This filter generates an EOS supported hash digest. The algorithm for the hash is defined with the `hash_type` key. `sha512_password` can be
  used with the `hash_type` key to create a SHA-512 password hash from a cleartext password for a local user. By default, the secure_hash filter will use
  `hash_type="sha512_password"`.

  Each user should use a unique salt value to ensure that even if multiple users share the same password, their hashes will be unique.
positional: _input
options:
  _input:
    description: The cleartext input to be hashed.
    type: string
    required: true
  salt:
    description: |-
      The salt value to be used when creating a password hash.
      The salt value can only contain the characters `./`, digits `0-9`, and uppercase or lowercase letters `A-Z a-z`.
      The salt value should not be greater than 16 characters long.
    type: string
  hash_type:
    description: |-
      The hashing algorithm used will be based on the value of the `hash_type` key.
      Currently, only `sha512_password` is supported with hash_type and is set by default. `sha512_password` will generate a SHA-512 password hash from
      a cleartext password for a local user.
    choices: ["sha512_password"]
    type: string
"""


EXAMPLES = r"""
---
local_users:
  # Create a sha512 password hash with a user defined salt value (recommended). The hash_type will default to sha512_password.
  - name: cvpadmin
    sha512_password: "{{ 'securepassword' | arista.avd.secure_hash(salt='Yar49ahkzKddRVYS')}}"

    # Create a sha512 password hash with a user defined salt value and specifying the hash_type as a sha512_password.
  - name: cvpuser
    sha512_password: "{{ 'newpassword' | arista.avd.secure_hash(salt='Kte5paJ3czRQczbk', hash_type='sha512_password')}}"
"""


RETURN = r"""
---
_value:
  description:
    - The hash digest
  type: string
"""


class FilterModule:
    def filters(self) -> dict:
        return {"secure_hash": wrap_filter(PLUGIN_NAME)(secure_hash)}
