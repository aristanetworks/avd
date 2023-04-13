from __future__ import annotations

from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError
from ansible_collections.arista.avd.plugins.plugin_utils.utils import template_var


class TemplateMixin:
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to the SharedUtils class
    """

    def template_var(self, template_file, template_vars):
        """
        Run the simplified templater using the passed Ansible "templar" engine.
        """
        try:
            return template_var(template_file, template_vars, self.templar)
        except Exception as e:
            raise AristaAvdError(f"Error during templating of template: {template_file}") from e
