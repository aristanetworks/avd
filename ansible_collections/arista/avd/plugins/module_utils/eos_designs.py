from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from functools import cached_property
from ansible_collections.arista.avd.plugins.module_utils.utils import AristaAvdError, compile_searchpath, get, template_var
from ansible_collections.arista.avd.plugins.filter.convert_dicts import convert_dicts
from ansible_collections.arista.avd.plugins.filter.list_compress import list_compress
from ansible_collections.arista.avd.plugins.filter.range_expand import range_expand
from ansible_collections.arista.avd.plugins.filter.natural_sort import natural_sort
try:
    from ansible.plugins.filter.core import combine
except ImportError as imp_exc:
    FILTER_IMPORT_ERROR = imp_exc
else:
    FILTER_IMPORT_ERROR = None


class AvdFacts:

    def __init__(self, hostvars, templar):
        self._hostvars = hostvars
        self._templar = templar
        self._list_compress = list_compress
        self._range_expand = range_expand
        self._convert_dicts = convert_dicts
        self._natural_sort = natural_sort
        self._combine = combine

    @classmethod
    def keys(cls):
        '''
        Return the list of "keys"

        Actually the returned list are the names of attributes not starting with "_" and using cached_property class.
        The "_" check is added to allow support for "internal" cached_properties storing temporary values.
        '''

        return [key for key in cls.__dict__ if not key.startswith('_') and isinstance(getattr(cls, key), cached_property)]

    @classmethod
    def internal_keys(cls):
        '''
        Return a list containing the names of attributes starting with "_" and using cached_property class.
        '''

        return [key for key in cls.__dict__ if key.startswith('_') and isinstance(getattr(cls, key), cached_property)]

    def get(self, key, default_value=None):
        '''
        Emulate the builtin dict .get method
        '''

        if key in self.keys():
            return getattr(self, key)
        return default_value

    def render(self):
        '''
        Return a dictionary of all @cached_property values.

        If the value is cached, it will automatically get returned from cache
        If the value is not cached, it will be resolved by the attribute function first.
        Empty values are removed from the returned data.
        '''
        return {key: getattr(self, key) for key in self.keys() if getattr(self, key) is not None}

    @cached_property
    def _searchpath(self):
        '''
        Add a '<>/templates' entry for every entry in "ansible_search_path"
        similar to is done in the Ansible "template" lookup module.
        '''
        ansible_search_path = get(self._hostvars, "ansible_search_path", required=True)
        return compile_searchpath(ansible_search_path)

    def template_var(self, template_file, template_vars):
        '''
        Run the simplified templater using the passed Ansible "templar" engine.

        Note that the "templar" was initialized in the calling action module with
        the following variables per device:
        - Ansible hostvars for that device
        - "avd_switch_facts" pointer to dictionary containing instances of this
           class for every device
        - "switch" pointer to this instance of this class
        The pointers mean that templates can leverage any fact method on any device
        during templating, even if those facts have not yet been calculated.
        '''
        try:
            return template_var(template_file, template_vars, self._templar, self._searchpath)
        except Exception as e:
            raise AristaAvdError(f"[{self.hostname}] Error during templating of template: {template_file} with data: {template_vars}") from e
