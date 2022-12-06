from __future__ import annotations

from functools import cached_property

from .utils import UtilsMixin


class RouterBfdMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    @cached_property
    def router_bfd(self) -> dict | None:
        """
        return structured config for router_bfd
        """
        if self._configure_overlay is False:
            return None

        if self._bfd_multihop is None:
            return None

        return {
            "multihop": {
                "interval": self._bfd_multihop.get("interval"),
                "min_rx": self._bfd_multihop.get("min_rx"),
                "multiplier": self._bfd_multihop.get("multiplier"),
            }
        }
