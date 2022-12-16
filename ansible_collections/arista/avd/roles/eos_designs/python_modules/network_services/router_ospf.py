from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdMissingVariableError
from ansible_collections.arista.avd.plugins.plugin_utils.utils import default, get

from .utils import UtilsMixin


class RouterOspfMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    @cached_property
    def router_ospf(self) -> dict | None:
        """
        return structured config for router_ospf

        If we have static_routes in default VRF and not EPVN, and underlay is OSPF
        Then add redistribute static to the underlay OSPF process.
        """

        if not self._network_services_l3:
            return None

        ospf_processes = {}
        for tenant in self._filtered_tenants:
            for vrf in tenant["vrfs"]:
                if get(vrf, "ospf.enabled") is not True:
                    continue

                if self._hostname not in get(vrf, "ospf.nodes", default=[self._hostname]):
                    continue

                ospf_interfaces = []
                for l3_interface in vrf["l3_interfaces"]:
                    if get(l3_interface, "ospf.enabled") is True:
                        for node_index, node in enumerate(l3_interface["nodes"]):
                            if node != self._hostname:
                                continue

                            ospf_interfaces.append(l3_interface["interfaces"][node_index])

                for svi in vrf["svis"]:
                    if get(svi, "ospf.enabled") is True:
                        interface_name = f"Vlan{svi['id']}"
                        ospf_interfaces.append(interface_name)

                process_id = default(get(vrf, "ospf.process_id"), vrf.get("vrf_id"))
                if not process_id:
                    raise AristaAvdMissingVariableError(f"'ospf.process_id' or 'vrf_id' under vrf '{vrf['name']}")

                process = {
                    "vrf": vrf["name"],
                    "passive_interface_default": True,
                    "router_id": default(get(vrf, "ospf.router_id"), self._router_id),
                    "no_passive_interfaces": ospf_interfaces,
                    "bfd_enable": get(vrf, "ospf.bfd"),
                    "max_lsa": get(vrf, "ospf.max_lsa"),
                }

                if get(vrf, "ospf.redistribute_bgp.enabled", default=True) is True:
                    process["redistribute"] = {
                        "bgp": {},
                    }
                    if (route_map := get(vrf, "ospf.redistribute_bgp.route_map")) is not None:
                        process["redistribute"]["bgp"]["route_map"] = route_map

                # Strip None values from process before adding to list
                process = {key: value for key, value in process.items() if value is not None}

                ospf_processes[process_id] = process

        # If we have static_routes in default VRF and not EPVN, and underlay is OSPF
        # Then add redistribute static to the underlay OSPF process.
        if self._vrf_default_ipv4_static_routes["redistribute_in_underlay"] and self._underlay_routing_protocol in ["ospf", "ospf-ldp"]:
            ospf_processes[self._underlay_ospf_process_id] = {"redistribute": {"static": {}}}

        if ospf_processes:
            return {"process_ids": ospf_processes}

        return None
