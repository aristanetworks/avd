from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.plugin_utils.utils import get

from .utils import UtilsMixin


class ManagementCvxMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    @cached_property
    def management_cvx(self) -> dict | None:
        if not self._overlay_cvx:
            return None

        return {
            "source_interface": "Loopback0",
            "server_hosts": get(self._hostvars, "overlay_cvx_servers", required=True),
        }
