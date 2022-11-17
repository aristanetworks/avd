from __future__ import annotations

from functools import cached_property

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
        """
        if self._underlay_router is not True:
            return None

        if self._underlay_routing_protocol not in ["ospf", "ospf-ldp"]:
            return None

        ospf_processes = {}

        process_id = self._underlay_ospf_process_id

        no_passive_interfaces = []

        for link in self._underlay_links:
            if link["type"] != "underlay_p2p":
                continue

            no_passive_interfaces.append(link["interface"])

        if self._mlag_l3 is True:
            mlag_l3_vlan = default(get(self._hostvars, "switch.mlag_peer_l3_vlan"), get(self._hostvars, "switch.mlag_peer_vlan"))
            no_passive_interfaces.append(f"Vlan{mlag_l3_vlan}")

        process = {
            "passive_interface_default": True,
            "router_id": self._router_id,
            "max_lsa": get(self._hostvars, "underlay_ospf_max_lsa"),
            "no_passive_interfaces": no_passive_interfaces,
        }

        # TODO - setting this because the default value is false and it would show up in structured_config otherwise
        if get(self._hostvars, "underlay_ospf_bfd_enable") is True:
            process["bfd_enable"] = True

        if self._overlay_routing_protocol is None:
            process["redistribute"] = {
                "connected": {},
            }

        # Strip None values from process before adding to list
        process = {key: value for key, value in process.items() if value is not None}

        ospf_processes[process_id] = process

        if ospf_processes:
            return {"process_ids": ospf_processes}

        return None
