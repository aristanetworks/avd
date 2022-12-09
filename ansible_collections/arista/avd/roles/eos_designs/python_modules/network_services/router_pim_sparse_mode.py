from __future__ import annotations

from functools import cached_property

import q

from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdMissingVariableError
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get
from ansible_collections.arista.avd.roles.eos_designs.python_modules.network_services.utils import UtilsMixin


class RouterPimSparseModeMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    @cached_property
    def router_pim_sparse_mode(self) -> dict | None:
        """
        return structured config for router_pim

        Used for to configure RPs on the VRF
        """

        if not self._network_services_l3:
            return None

        vrfs = []
        for tenant in self._filtered_tenants:
            for vrf in tenant["vrfs"]:
                rps = []
                for node_item in (mc_node_settings := get(vrf, "_l3_multicast_node_settings")):
                    if not (mc_nodes := get(node_item, "nodes", default=[])) and len(mc_node_settings) > 1:
                        raise AristaAvdMissingVariableError(
                            f"l3_multicast.node_settings in Tenant '{tenant['name']}' or VRF '{vrf['name']}': only one entry with no 'nodes' or multiple"
                            " entries with 'nodes' can be defined."
                        )

                    if self._hostname in mc_nodes or "nodes" not in node_item:
                        q(self._hostname)
                        for rp_item in get(node_item, "rp_addresses"):
                            for rp_address in get(
                                rp_item,
                                "rps",
                                required=True,
                                org_key=f"l3_multicast.node_settings.rp_addresses.rps under VRF '{vrf['name']}' in tenant '{tenant['name']}'",
                            ):
                                if rp_groups := get(rp_item, "groups", default=[]):
                                    rps.append({"address": rp_address, "groups": rp_groups})
                                else:
                                    rps.append({"address": rp_address})

                if rps:
                    vrfs.append({"name": vrf["name"], "ipv4": {"rp_addresses": rps}})

        if vrfs:
            return {"vrfs": vrfs}

        return None
