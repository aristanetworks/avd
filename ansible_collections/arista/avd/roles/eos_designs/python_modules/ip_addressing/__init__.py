# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from ansible.errors import AnsibleActionFail

from ansible_collections.arista.avd.plugins.plugin_utils.pyavd_wrappers import RaiseOnUse

try:
    from pyavd._eos_designs.ip_addressing import AvdIpAddressing
except ImportError as e:
    AvdIpAddressing = RaiseOnUse(
        AnsibleActionFail(
            "The 'arista.avd.eos_designs' collection requires the 'pyavd' Python library. Got import error",
            orig_exc=e,
        )
    )


__all__ = ["AvdIpAddressing"]
