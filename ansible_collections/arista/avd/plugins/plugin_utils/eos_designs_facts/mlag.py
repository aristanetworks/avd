from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ansible_collections.arista.avd.plugins.plugin_utils.eos_designs_shared_utils import SharedUtils


class MlagMixin:
    """
    Mixin Class used to generate some of the EosDesignsFacts.
    Class should only be used as Mixin to the EosDesignsFacts class
    """

    _hostvars: dict
    shared_utils: SharedUtils

    @cached_property
    def mlag_peer(self) -> str | None:
        """
        Exposed in avd_switch_facts
        """
        if self.shared_utils.mlag is True:
            return self.shared_utils.mlag_peer
        return None

    @cached_property
    def mlag_port_channel_id(self) -> int | None:
        """
        Exposed in avd_switch_facts
        """
        if self.shared_utils.mlag is True:
            return self.shared_utils.mlag_port_channel_id
        return None

    @cached_property
    def mlag_interfaces(self) -> list | None:
        """
        Exposed in avd_switch_facts
        """
        if self.shared_utils.mlag is True:
            return self.shared_utils.mlag_interfaces
        return None

    @cached_property
    def mlag_ip(self) -> str | None:
        """
        Exposed in avd_switch_facts
        """
        if self.shared_utils.mlag is True:
            return self.shared_utils.mlag_ip
        return None

    @cached_property
    def mlag_l3_ip(self) -> str | None:
        """
        Exposed in avd_switch_facts
        """
        if self.shared_utils.mlag_l3 is True and self.shared_utils.mlag_peer_l3_vlan is not None:
            return self.shared_utils.mlag_l3_ip
        return None

    @cached_property
    def mlag_switch_ids(self) -> dict | None:
        """
        Exposed in avd_switch_facts

        Returns the switch id's of both primary and secondary switches for a given node group
        {"primary": int, "secondary": int}
        """
        return self.shared_utils.mlag_switch_ids
