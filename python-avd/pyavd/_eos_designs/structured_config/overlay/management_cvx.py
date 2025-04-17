# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor
from pyavd._errors import AristaAvdInvalidInputsError, AristaAvdMissingVariableError
from pyavd._utils import get_ip_from_ip_prefix

if TYPE_CHECKING:
    from . import AvdStructuredConfigOverlayProtocol


class ManagementCvxMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @structured_config_contributor
    def management_cvx(self: AvdStructuredConfigOverlayProtocol) -> None:
        if not (self.shared_utils.overlay_cvx and self.shared_utils.overlay_vtep):
            return

        if not self.inputs.overlay_cvx_servers:
            msg = "overlay_cvx_servers"
            raise AristaAvdMissingVariableError(msg)

        for overlay_cvx_server in self.inputs.overlay_cvx_servers:
            peer_switch_facts = self.shared_utils.get_peer_facts(overlay_cvx_server)
            if not peer_switch_facts.mgmt_ip:
                msg = f"'mgmt_ip' for CVX Server {overlay_cvx_server} is required."
                raise AristaAvdInvalidInputsError(msg)
            cvx_server_ip = peer_switch_facts.mgmt_ip
            self.structured_config.management_cvx.server_hosts.append(get_ip_from_ip_prefix(cvx_server_ip))

        self.structured_config.management_cvx._update(shutdown=False, source_interface="Loopback0")
