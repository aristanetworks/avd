# Copyright (c) 2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.


class FabricDocumentation:
    fabric_documentation: str = ""


def get_fabric_documentation(
    avd_facts: dict[str, dict],
    structured_configs: dict[str, dict],
    fabric_name: str,
    fabric_documentation: bool = True,
    include_connected_endpoints: bool = False,
) -> FabricDocumentation:
    # pylint: disable=import-outside-toplevel
    from pyavd._eos_designs.fabric_documentation_facts import FabricDocumentationFacts
    from pyavd.j2filters import add_md_toc

    from .constants import EOS_DESIGNS_JINJA2_PRECOMPILED_TEMPLATE_PATH
    from .templater import Templar

    # pylint: enable=import-outside-toplevel

    result = FabricDocumentation()
    doc_templar = Templar(precompiled_templates_path=EOS_DESIGNS_JINJA2_PRECOMPILED_TEMPLATE_PATH)
    if fabric_documentation:
        fabric_documentation_facts = FabricDocumentationFacts(avd_facts, structured_configs, fabric_name, include_connected_endpoints).render()
        result.fabric_documentation = doc_templar.render_template_from_file("fabric_documentation.j2", fabric_documentation_facts)
        if include_connected_endpoints:
            result.fabric_documentation += "\n" + doc_templar.render_template_from_file("connected_endpoints_documentation.j2", fabric_documentation_facts)

        result.fabric_documentation = add_md_toc(result.fabric_documentation, skip_lines=3)
    return result
