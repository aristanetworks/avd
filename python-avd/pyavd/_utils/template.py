# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections import ChainMap
    from typing import Any

    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar


def template(template_file: str, template_vars: dict[str, Any] | ChainMap[str, Any], templar: Templar | None) -> Any:
    """
    Run Ansible Templar with template file.

    This function does not support the following Ansible features:
    - No template_* vars (rarely used)
    - The template file path is not inserted into searchpath, so "include" must be absolute from searchpath.
    - No configurable convert_data (we set it to True to match Ansible 2.19+)
    - Maybe something else we have not discovered yet...

    Parameters
    ----------
    template_file : str
        Path to Jinja2 template file
    template_vars : any
        Variables to use when rendering template
    templar : func
        Instance of Ansible Templar class
    searchpath : list of str
        List of Paths

    Returns:
    -------
    Any
        The rendered template result. Can be of any type depending on the template.
    """
    if templar is None:
        msg = "Jinja Templating is not implemented in pyavd"
        raise NotImplementedError(msg)

    # We only get here when running from Ansible, so it is safe to import from ansible and jinja2.
    from ansible_collections.arista.avd.plugins.plugin_utils.utils import ANSIBLE_ABOVE_2_19  # noqa: PLC0415
    from jinja2.loaders import FileSystemLoader  # noqa: PLC0415

    dataloader: DataLoader = templar._loader
    jinjaloader = templar.environment.loader
    searchpath = jinjaloader.searchpath if isinstance(jinjaloader, FileSystemLoader) else []
    template_file_path = dataloader.path_dwim_relative_stack(searchpath, "templates", template_file)

    if ANSIBLE_ABOVE_2_19:
        # New templar from ansible-core 2.19 and above
        from ansible.template import trust_as_template  # noqa: PLC0415 # pyright: ignore reportAttributeAccessIssue

        j2template = trust_as_template(dataloader.get_text_file_contents(template_file_path))  # pyright: ignore [reportAttributeAccessIssue]
        tmp_templar = templar.copy_with_new_env(available_variables=template_vars)
        output = tmp_templar.template(j2template, escape_backslashes=False)

    else:
        # Legacy templar
        # TODO: Remove this once 2.19 is our minimal supported ansible-core version.
        from ansible.module_utils._text import to_text  # noqa: PLC0415

        j2template, _ = dataloader._get_file_contents(template_file_path)
        j2template = to_text(j2template)

        with templar.set_temporary_context(available_variables=template_vars):
            output = templar.template(j2template, convert_data=True, escape_backslashes=False)

    return output
