from __future__ import annotations

from functools import cached_property
from ipaddress import ip_interface

from ansible_collections.arista.avd.plugins.plugin_utils.utils import get

from .utils import UtilsMixin


class ManagementCvxMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    @cached_property
    def management_cvx(self) -> dict | None:
        if not (self._overlay_cvx and self._overlay_vtep):
            return None

        server_hosts = []
        overlay_cvx_servers = get(self._hostvars, "overlay_cvx_servers", required=True)
        for overlay_cvx_server in overlay_cvx_servers:
            peer_switch_facts = self._get_peer_facts(overlay_cvx_server, True)
            cvx_server_ip = get(peer_switch_facts, "mgmt_ip", required=True, org_key=f"'mgmt_ip' for CVX Server {overlay_cvx_server}")
            server_hosts.append(str(ip_interface(cvx_server_ip).ip))

        return {
            "shutdown": False,
            "source_interface": "Loopback0",
            "server_hosts": server_hosts,
        }
