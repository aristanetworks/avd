from functools import cached_property

from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError
from ansible_collections.arista.avd.plugins.plugin_utils.utils import template_var


class AvdFacts:
    def __init__(self, hostvars, templar):
        self._hostvars = hostvars
        self._templar = templar

    @classmethod
    def __keys(cls):  # pylint: disable=bad-option-value, unused-private-member # CH Sep-22: Some pylint bug.
        """
        Get all class attributes including those of base Classes and Mixins.
        Using MRO, which is the same way Python resolves attributes.
        """
        keys = []
        for c in cls.mro():
            c_keys = [key for key in c.__dict__ if key not in keys]
            keys.extend(c_keys)

        return keys

    @classmethod
    def keys(cls):
        """
        Return the list of "keys"

        Actually the returned list are the names of attributes not starting with "_" and using cached_property class.
        The "_" check is added to allow support for "internal" cached_properties storing temporary values.
        """

        return [key for key in cls.__keys() if not key.startswith("_") and isinstance(getattr(cls, key), cached_property)]

    @classmethod
    def internal_keys(cls):
        """
        Return a list containing the names of attributes starting with "_" and using cached_property class.
        """

        return [key for key in cls.__keys() if key.startswith("_") and isinstance(getattr(cls, key), cached_property)]

    def get(self, key, default_value=None):
        """
        Emulate the builtin dict .get method
        """

        if key in self.keys():
            return getattr(self, key)
        return default_value

    def render(self):
        """
        Return a dictionary of all @cached_property values.

        If the value is cached, it will automatically get returned from cache
        If the value is not cached, it will be resolved by the attribute function first.
        Empty values are removed from the returned data.
        """
        return {key: getattr(self, key) for key in self.keys() if getattr(self, key) is not None}

    def template_var(self, template_file, template_vars):
        """
        Run the simplified templater using the passed Ansible "templar" engine.
        """
        try:
            return template_var(template_file, template_vars, self._templar)
        except Exception as e:
            raise AristaAvdError(f"Error during templating of template: {template_file}") from e
