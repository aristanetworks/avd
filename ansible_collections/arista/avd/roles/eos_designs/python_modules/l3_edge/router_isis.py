from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.filter.natural_sort import natural_sort

from .utils import UtilsMixin


class RouterIsisMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    @cached_property
    def router_isis(self) -> dict | None:
        """
        Return structured config for router_isis
        """

        if not self._underlay_isis:
            return None

        no_passive_interfaces = [p2p_link["data"]["interface"] for p2p_link in self._filtered_p2p_links if p2p_link.get("include_in_underlay_protocol") is True]
        if no_passive_interfaces:
            return {"no_passive_interfaces": natural_sort(no_passive_interfaces)}

        return None
