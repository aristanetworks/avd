# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from jinja2 import ChoiceLoader, Environment, FileSystemLoader, ModuleLoader, StrictUndefined

from .constants import JINJA2_EXTENSIONS, JINJA2_PRECOMPILED_TEMPLATE_PATH
from .vendor.j2.filter.convert_dicts import convert_dicts
from .vendor.j2.filter.decrypt import decrypt
from .vendor.j2.filter.default import default
from .vendor.j2.filter.encrypt import encrypt
from .vendor.j2.filter.hide_passwords import hide_passwords
from .vendor.j2.filter.list_compress import list_compress
from .vendor.j2.filter.natural_sort import natural_sort
from .vendor.j2.filter.range_expand import range_expand
from .vendor.j2.test.contains import contains
from .vendor.j2.test.defined import defined

JINJA2_CUSTOM_FILTERS = {
    "arista.avd.default": default,
    "arista.avd.convert_dicts": convert_dicts,
    "arista.avd.decrypt": decrypt,
    "arista.avd.encrypt": encrypt,
    "arista.avd.hide_passwords": hide_passwords,
    "arista.avd.list_compress": list_compress,
    "arista.avd.natural_sort": natural_sort,
    "arista.avd.range_expand": range_expand,
}
JINJA2_CUSTOM_TESTS = {
    "arista.avd.defined": defined,
    "arista.avd.contains": contains,
}


class Undefined(StrictUndefined):
    """
    Allow nested checks for undefined instead of having to check on every level.
    Example "{% if var.key.subkey is arista.avd.undefined %}" is ok.

    Without this it we would have to test every level, like
    "{% if var is arista.avd.undefined or var.key is arista.avd.undefined or var.key.subkey is arista.avd.undefined %}"
    """

    def __getattr__(self, name):
        # Return original Undefined object to preserve the first failure context
        return self

    def __getitem__(self, key):
        # Return original Undefined object to preserve the first failure context
        return self

    def __repr__(self):
        return f"Undefined(hint={self._undefined_hint}, obj={self._undefined_obj}, name={self._undefined_name})"

    def __contains__(self, item):
        # Return original Undefined object to preserve the first failure context
        return self


class Templar:
    def __init__(self, searchpaths: list[str] = None):
        self.loader = ChoiceLoader(
            [
                ModuleLoader(JINJA2_PRECOMPILED_TEMPLATE_PATH),
                FileSystemLoader(searchpaths or []),
            ]
        )

        self.environment = Environment(
            extensions=JINJA2_EXTENSIONS,
            loader=self.loader,
            undefined=Undefined,
            trim_blocks=True,
        )
        self.environment.filters.update(JINJA2_CUSTOM_FILTERS)
        self.environment.tests.update(JINJA2_CUSTOM_TESTS)

    def render_template_from_file(self, template_file: str, template_vars: dict) -> str:
        return self.environment.get_template(template_file).render(template_vars)

    def compile_templates_in_paths(self, searchpaths: list[str]) -> None:
        print(JINJA2_PRECOMPILED_TEMPLATE_PATH)
        self.environment.loader = FileSystemLoader(searchpaths)
        self.environment.compile_templates(
            zip=None,
            log_function=print,
            target=JINJA2_PRECOMPILED_TEMPLATE_PATH,
            ignore_errors=False,
        )
        self.environment.loader = self.loader
