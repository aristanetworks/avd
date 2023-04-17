from __future__ import annotations

from typing import TYPE_CHECKING

from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get, template_var

if TYPE_CHECKING:
    from ansible_collections.arista.avd.plugins.plugin_utils.eos_designs_facts import EosDesignsFacts

    from .shared_utils import SharedUtils


class UtilsMixin:
    """
    Mixin Class providing a subset of SharedUtils
    Class should only be used as Mixin to the SharedUtils class
    Using quoted type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    def get_peer_facts(self: "SharedUtils", peer_name: str, required: bool = True) -> EosDesignsFacts | dict | None:
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

    def template_var(self: "SharedUtils", template_file, template_vars) -> str:
        """
        Run the simplified templater using the passed Ansible "templar" engine.
        """
        try:
            return template_var(template_file, template_vars, self.templar)
        except Exception as e:
            raise AristaAvdError(f"Error during templating of template: {template_file}") from e
