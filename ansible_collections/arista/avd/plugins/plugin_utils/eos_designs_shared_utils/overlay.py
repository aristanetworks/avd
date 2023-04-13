from __future__ import annotations

from functools import cached_property
from ipaddress import ip_address
from re import fullmatch

from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdMissingVariableError
from ansible_collections.arista.avd.plugins.plugin_utils.utils import default, get


class OverlayMixin:
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to the SharedUtils class
    """

    hostname: str
    hostvars: dict
    id: int
    node_type_key_data: dict
    router_id: str
    switch_data_combined: dict

    @cached_property
    def overlay_rd_type_admin_subfield(self):
        tmp_overlay_rd_type_admin_subfield = get(self.hostvars, "overlay_rd_type.admin_subfield")
        tmp_overlay_rd_type_admin_subfield_offset = int(default(get(self.hostvars, "overlay_rd_type.admin_subfield_offset"), 0))
        if tmp_overlay_rd_type_admin_subfield is None:
            return self.router_id

        if tmp_overlay_rd_type_admin_subfield == "vtep_loopback":
            return get(self.hostvars, "switch.vtep_ip")

        if tmp_overlay_rd_type_admin_subfield == "bgp_as":
            return get(self.hostvars, "switch.bgp_as")

        if tmp_overlay_rd_type_admin_subfield == "switch_id":
            if self.id is None:
                raise AristaAvdMissingVariableError(f"'id' is not set on '{self.hostname}' and 'overlay_rd_type_admin_subfield' is set to 'switch_id'")
            return self.id + tmp_overlay_rd_type_admin_subfield_offset

        if fullmatch(r"[0-9]+", str(tmp_overlay_rd_type_admin_subfield)):
            return str(int(tmp_overlay_rd_type_admin_subfield) + tmp_overlay_rd_type_admin_subfield_offset)

        try:
            ip_address(tmp_overlay_rd_type_admin_subfield)
            return tmp_overlay_rd_type_admin_subfield
        except ValueError:
            pass

        return self.router_id

    @cached_property
    def evpn_gateway_vxlan_l2(self) -> bool:
        return get(self.switch_data_combined, "evpn_gateway.evpn_l2.enabled", default=False)

    @cached_property
    def evpn_gateway_vxlan_l3(self) -> bool:
        return get(self.switch_data_combined, "evpn_gateway.evpn_l3.enabled", default=False)

    @cached_property
    def evpn_gateway_vxlan_l3_inter_domain(self) -> bool:
        return get(self.switch_data_combined, "evpn_gateway.evpn_l3.inter_domain", default=True)
