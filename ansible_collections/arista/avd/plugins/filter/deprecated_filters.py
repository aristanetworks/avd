# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
#
# deprecated filters - grouped together to avoid Ansible to generate warning on loading the module name...
#

__metaclass__ = type

from ansible.errors import AnsibleFilterError

from ansible_collections.arista.avd.plugins.plugin_utils.pyavd_wrappers import RaiseOnUse, wrap_filter

PLUGIN_NAME_1 = "arista.avd.generate_lacp_id"
PLUGIN_NAME_2 = "arista.avd.generate_esi"
PLUGIN_NAME_3 = "arista.avd.generate_route_target"

try:
    from pyavd.j2filters import generate_esi, generate_lacp_id, generate_route_target
except ImportError as e:
    generate_lacp_id = RaiseOnUse(
        AnsibleFilterError(
            f"The '{PLUGIN_NAME_1}' plugin requires the 'pyavd' Python library. Got import error",
            orig_exc=e,
        )
    )
    generate_generate_esi = RaiseOnUse(
        AnsibleFilterError(
            f"The '{PLUGIN_NAME_2}' plugin requires the 'pyavd' Python library. Got import error",
            orig_exc=e,
        )
    )
    generate_route_target = RaiseOnUse(
        AnsibleFilterError(
            f"The '{PLUGIN_NAME_3}' plugin requires the 'pyavd' Python library. Got import error",
            orig_exc=e,
        )
    )


class FilterModule(object):
    def filters(self):
        return {
            "generate_lacp_id": wrap_filter(PLUGIN_NAME_1)(generate_lacp_id),
            "generate_esi": wrap_filter(PLUGIN_NAME_2)(generate_esi),
            "generate_route_target": wrap_filter(PLUGIN_NAME_3)(generate_route_target),
        }
