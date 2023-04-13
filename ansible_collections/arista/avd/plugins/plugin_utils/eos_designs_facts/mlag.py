from __future__ import annotations

import re
from functools import cached_property
from typing import TYPE_CHECKING

from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdMissingVariableError
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get

if TYPE_CHECKING:
    from ansible_collections.arista.avd.plugins.plugin_utils.eos_designs_shared_utils import SharedUtils


class MlagMixin:
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to the EosDesignsFacts class
    """

    _hostvars: dict
    shared_utils: SharedUtils

    @cached_property
    def mlag_peer(self):
        """REQUIRED in avd_switch_facts"""
        if self.shared_utils.mlag is True:
            return self.shared_utils.mlag_peer
        return None

    @cached_property
    def mlag_port_channel_id(self):
        """REQUIRED in avd_switch_facts"""
        if self.shared_utils.mlag is True:
            default_mlag_port_channel_id = "".join(re.findall(r"\d", self.shared_utils.mlag_interfaces[0]))
            return get(self.shared_utils.switch_data_combined, "mlag_port_channel_id", default_mlag_port_channel_id)
        return None

    @cached_property
    def mlag_interfaces(self):
        """REQUIRED in avd_switch_facts"""
        if self.shared_utils.mlag is True:
            return self.shared_utils.mlag_interfaces
        return None

    @cached_property
    def mlag_ip(self):
        """
        REQUIRED in avd_switch_facts

        Render ipv4 address for mlag_ip using dynamically loaded python module.
        """
        if self.shared_utils.mlag is True:
            if self.shared_utils.mlag_role == "primary":
                return self.shared_utils.ip_addressing.mlag_ip_primary()
            elif self.shared_utils.mlag_role == "secondary":
                return self.shared_utils.ip_addressing.mlag_ip_secondary()
        return None

    @cached_property
    def mlag_l3_ip(self):
        """
        REQUIRED in avd_switch_facts

        Render ipv4 address for mlag_l3_ip using dynamically loaded python module.
        """
        if self.shared_utils.mlag_l3 is True and self.shared_utils.mlag_peer_l3_vlan is not None:
            if self.shared_utils.mlag_role == "primary":
                return self.shared_utils.ip_addressing.mlag_l3_ip_primary()
            elif self.shared_utils.mlag_role == "secondary":
                return self.shared_utils.ip_addressing.mlag_l3_ip_secondary()
        return None

    @cached_property
    def mlag_switch_ids(self):
        """
        REQUIRED in avd_switch_facts

        Returns the switch id's of both primary and secondary switches for a given node group
        {"primary": int, "secondary": int}
        """
        if self.shared_utils.mlag_role == "primary":
            if self.shared_utils.id is None:
                raise AristaAvdMissingVariableError(f"'id' is not set on '{self.shared_utils.hostname}' and is required to compute MLAG ids")
            return {"primary": self.shared_utils.id, "secondary": self._mlag_peer_id}
        elif self.shared_utils.mlag_role == "secondary":
            if self.shared_utils.id is None:
                raise AristaAvdMissingVariableError(f"'id' is not set on '{self.shared_utils.hostname}' and is required to compute MLAG ids")
            return {"primary": self._mlag_peer_id, "secondary": self.shared_utils.id}

    @cached_property
    def _mlag_peer_id(self):
        if self.shared_utils.mlag is True:
            return get(
                self._hostvars,
                f"avd_switch_facts..{self.shared_utils.mlag_peer}..switch..id",
                required=True,
                org_key=f"avd_switch_facts.({self.shared_utils.mlag_peer}).switch.id",
                separator="..",
            )
