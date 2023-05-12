from __future__ import annotations

from functools import cached_property
from hashlib import sha1

from ansible_collections.arista.avd.plugins.filter.convert_dicts import convert_dicts
from ansible_collections.arista.avd.plugins.filter.natural_sort import natural_sort
from ansible_collections.arista.avd.plugins.filter.snmp_hash import hash_passphrase
from ansible_collections.arista.avd.plugins.plugin_utils.avdfacts import AvdFacts
from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError, AristaAvdMissingVariableError
from ansible_collections.arista.avd.plugins.plugin_utils.strip_empties import strip_null_from_data
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get


class AvdStructuredConfig(AvdFacts):
    """
    This would return facts to ansible set at the rool-level of the host vars for the host calling this:
    {
        "cvp_tags": {
            "topology_hint_type": <topology_hint_type taken from node_type_keys.[].cvp_tags.topology_hint_type>,
        },
        "key2": "bar"
    }

    Missing fabric_name from shared_utils
    """

    @cached_property
    def cvp_tags(self) -> str:
        """
        Insert all the logic to deduct cvp tags here.
        User helper functions to larger code blocks
        Helper functions should be regular methods on the class (start with underscore)
        and if you need @cached_properties make sure to start the name with underscore.
        """
        interface_peer_name = self._interface_peer_name

        return {"topology_hint_type": self.shared_utils.cvp_tag_topology_hint_type}

    @cached_property
    def key2(self) -> str:
        self.shared_utils.all_fabric_devices
        return "bar"

    @cached_property
    def _interface_peer_name(self) -> str:
        """The leading underscore signals that this key is not included in the output facts"""
        return get(self._hostvars, "cvp_tags.interface_peer.name", default="peer")
