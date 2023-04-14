from __future__ import annotations

from typing import TYPE_CHECKING

from ansible_collections.arista.avd.plugins.plugin_utils.utils import get

if TYPE_CHECKING:
    from ansible_collections.arista.avd.plugins.plugin_utils.eos_designs_facts import EosDesignsFacts


class UtilsMixin:
    """
    Mixin Class providing a subset of SharedUtils
    Class should only be used as Mixin to the SharedUtils class
    """

    hostvars: dict

    def get_peer_facts(self, peer_name: str, required: bool = True) -> EosDesignsFacts | dict | None:
        """
        util function to retrieve peer_facts for peer_name

        returns avd_switch_facts.{peer_name}.switch

        by default required is True and so the function will raise is peer_facts cannot be found
        using the separator `..` to be able to handle hostnames with `.` inside
        """
        return get(
            self.hostvars,
            f"avd_switch_facts..{peer_name}..switch",
            separator="..",
            required=required,
            org_key=f"avd_switch_facts.{peer_name}.switch",
        )
