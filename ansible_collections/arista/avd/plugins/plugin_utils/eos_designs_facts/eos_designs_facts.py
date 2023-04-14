from __future__ import annotations

import ipaddress
from functools import cached_property

from ansible_collections.arista.avd.plugins.filter.range_expand import range_expand
from ansible_collections.arista.avd.plugins.plugin_utils.avdfacts import AvdFacts
from ansible_collections.arista.avd.plugins.plugin_utils.eos_designs_shared_utils import SharedUtils
from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError, AristaAvdMissingVariableError
from ansible_collections.arista.avd.plugins.plugin_utils.utils import default, get

from .mlag import MlagMixin
from .overlay import OverlayMixin
from .short_esi import ShortEsiMixin
from .uplinks import UplinksMixin
from .vlans import VlansMixin


class EosDesignsFacts(AvdFacts, MlagMixin, ShortEsiMixin, OverlayMixin, UplinksMixin, VlansMixin):
    """
    `EosDesignsFacts` is based on `AvdFacts`, so make sure to read the description there first.

    The class is instantiated once per device. Methods may use references to other device instances using `hostvars.avd_switch_facts`,
    which is a dict of `EosDesignsfacts` instances covering all devices.

    hostvars["switch"] is set to self, to allow `shared_utils` to work the same when they are called from `EosDesignsFacts` or from
    `AvdStructuredConfig`.
    """

    def __init__(self, hostvars, templar):
        # Add reference to this instance of EosDesignsFacts object inside hostvars.
        # This is used to allow templates to access the facts object directly with "switch.*"
        hostvars["switch"] = self

        shared_utils = SharedUtils(hostvars=hostvars, templar=templar)
        super().__init__(hostvars=hostvars, shared_utils=shared_utils)

    @cached_property
    def id(self) -> int | None:
        """
        Exposed in avd_switch_facts
        """
        return self.shared_utils.id

    @cached_property
    def type(self) -> str:
        """
        Exposed in avd_switch_facts

        switch.type fact set based on type variable
        """
        return self.shared_utils.type

    @cached_property
    def platform(self):
        """
        Exposed in avd_switch_facts
        """
        return self.shared_utils.platform

    @cached_property
    def is_deployed(self):
        """
        Exposed in avd_switch_facts
        """
        return get(self._hostvars, "is_deployed", default=True)

    @cached_property
    def serial_number(self):
        """
        Exposed in avd_switch_facts

        serial_number is inherited from
        Fabric Topology data model serial_number ->
            Host variable var serial_number
        """
        return default(get(self.shared_utils.switch_data_combined, "serial_number"), get(self._hostvars, "serial_number"))

    @cached_property
    def mgmt_ip(self) -> str | None:
        """
        Exposed in avd_switch_facts
        """
        return get(self.shared_utils.switch_data_combined, "mgmt_ip")

    @cached_property
    def mpls_lsr(self):
        """
        Exposed in avd_switch_facts
        """
        return self.shared_utils.mpls_lsr

    @cached_property
    def evpn_multicast(self):
        """
        Exposed in avd_switch_facts
        """
        if "evpn" not in self.shared_utils.overlay_address_families:
            return None
        if get(self._hostvars, "evpn_multicast") is True and self.shared_utils.vtep is True:
            if not (self.shared_utils.underlay_multicast is True and self.shared_utils.igmp_snooping_enabled is not False):
                raise AristaAvdError(
                    "'evpn_multicast: True' is only supported in combination with 'underlay_multicast: True' and 'igmp_snooping_enabled : True'"
                )
            elif self.shared_utils.mlag is True:
                peer_eos_designs_facts: EosDesignsFacts = get(
                    self._hostvars,
                    f"avd_switch_facts..{self.mlag_peer}..switch",
                    org_key=f"avd_switch_facts.({self.mlag_peer}).switch",
                    separator="..",
                )
                if self.shared_utils.overlay_rd_type_admin_subfield == peer_eos_designs_facts.shared_utils.overlay_rd_type_admin_subfield:
                    raise AristaAvdError(
                        "For MLAG devices Route Distinguisher must be unique when 'evpn_multicast: True' since it will create a multi-vtep configuration."
                    )
            return True
        return None

    @cached_property
    def loopback_ipv4_pool(self):
        """
        Exposed in avd_switch_facts
        """
        if self.shared_utils.underlay_router is True:
            return get(self.shared_utils.switch_data_combined, "loopback_ipv4_pool", required=True)
        return None

    @cached_property
    def uplink_ipv4_pool(self):
        """
        Exposed in avd_switch_facts
        """
        if self.shared_utils.underlay_router is True:
            return get(self.shared_utils.switch_data_combined, "uplink_ipv4_pool")
        return None

    @cached_property
    def bgp_as(self):
        """
        Exposed in avd_switch_facts

        Get global bgp_as or fabric_topology bgp_as.

        At least one of global bgp_as or fabric_topology bgp_as must be defined.

        AS ranges in fabric_topology bgp_as will be expanded to a list and:
         - For standalone or A/A MH devices, the node id will be used to index into the list to find the ASN.
         - For MLAG devices, the node id of the first node in the node group will be used to index into the ASN list.
         - If a bare ASN is used, that ASN will be used for all relevant devices (depending on whether defined
           at the defaults, node_group or node level).
         - Lower level definitions override higher level definitions as is standard with AVD.
        """
        if self.shared_utils.underlay_router is True:
            if self.shared_utils.underlay_routing_protocol == "ebgp" or self.shared_utils.evpn_role != "none" or self.shared_utils.mpls_overlay_role != "none":
                if get(self._hostvars, "bgp_as") is not None:
                    return str(get(self._hostvars, "bgp_as"))
                else:
                    bgp_as_range_expanded = range_expand(str(get(self.shared_utils.switch_data_combined, "bgp_as", required=True)))
                    try:
                        if len(bgp_as_range_expanded) == 1:
                            return bgp_as_range_expanded[0]
                        elif self.shared_utils.mlag:
                            return bgp_as_range_expanded[self.mlag_switch_ids["primary"] - 1]
                        else:
                            if self.id is None:
                                raise AristaAvdMissingVariableError(
                                    f"'id' is not set on '{self.shared_utils.hostname}' and is required when expanding 'bgp_as'"
                                )
                            return bgp_as_range_expanded[self.id - 1]
                    except IndexError as exc:
                        raise AristaAvdError(
                            f"Unable to allocate BGP AS: bgp_as range is too small ({len(bgp_as_range_expanded)}) for the id of the device"
                        ) from exc

            # Hack to make mpls PR non-breaking, adds empty bgp to igp topology spines
            # TODO: Remove this as part of AVD4.0
            elif self.shared_utils.underlay_routing_protocol in ["isis", "ospf"] and self.shared_utils.evpn_role == "none" and get(self._hostvars, "bgp_as") is not None:
                return str(get(self._hostvars, "bgp_as"))
        return None

    @cached_property
    def underlay_routing_protocol(self):
        """
        Exposed in avd_switch_facts
        """
        return self.shared_utils.underlay_routing_protocol

    @cached_property
    def vtep_loopback_ipv4_pool(self):
        """
        Exposed in avd_switch_facts
        """
        if self.shared_utils.vtep is True:
            return get(self.shared_utils.switch_data_combined, "vtep_loopback_ipv4_pool", required=True)
        return None

    @cached_property
    def inband_management_subnet(self):
        """
        Exposed in avd_switch_facts
        """
        return get(self.shared_utils.switch_data_combined, "inband_management_subnet")

    @cached_property
    def inband_management_role(self):
        if self.inband_management_subnet is not None and self.shared_utils.uplink_type == "port-channel":
            return "child"
        return None

    @cached_property
    def inband_management_parents(self):
        """
        Exposed in avd_switch_facts
        """
        if self.inband_management_role == "child":
            return self.shared_utils.uplink_switches
        return None

    @cached_property
    def inband_management_vlan(self):
        """
        Exposed in avd_switch_facts
        """
        if self.inband_management_role == "child":
            return int(get(self.shared_utils.switch_data_combined, "inband_management_vlan", default=4092))
        return None

    @cached_property
    def inband_management_ip(self):
        """
        Exposed in avd_switch_facts
        """
        if self.inband_management_role == "child":
            if self.id is None:
                raise AristaAvdMissingVariableError(f"'id' is not set on '{self.shared_utils.hostname}' and is required to set inband_management_ip")
            subnet = ipaddress.ip_network(self.inband_management_subnet, strict=False)
            hosts = list(subnet.hosts())
            inband_management_ip = str(hosts[2 + self.id])
            inband_management_prefix = str(subnet.prefixlen)
            return f"{inband_management_ip}/{inband_management_prefix}"
        return None

    @cached_property
    def inband_management_gateway(self):
        """
        Exposed in avd_switch_facts
        """
        if self.inband_management_role == "child":
            subnet = ipaddress.ip_network(self.inband_management_subnet, strict=False)
            hosts = list(subnet.hosts())
            return str(hosts[0])
        return None

    @cached_property
    def inband_management_interface(self):
        """
        Exposed in avd_switch_facts
        """
        if self.inband_management_role == "child":
            return f"Vlan{self.inband_management_vlan}"
        return None

    @cached_property
    def vtep_ip(self):
        """
        Exposed in avd_switch_facts

        Render ipv4 address for vtep_ip using dynamically loaded python module.
        """
        if self.shared_utils.vtep is True:
            if self.shared_utils.mlag is True:
                return self.shared_utils.ip_addressing.vtep_ip_mlag()

            else:
                return self.shared_utils.ip_addressing.vtep_ip()

        return None
