#!/usr/bin/env python
"""
"""

import yaml

SCOPES = [
    "eos_config_deploy_cvp",
    "eos_config_deploy_eapi",
    "eos_designs",
    "eos_designs_to_containerlab",
    "eos_l3ls_evpn",
    "eos_snapshot",
    "eos_validate_state",
    "build_output_folders",
    "cvp_configlet_upload",
    "dhcp_provisioner",
    "eos_cli_config_gen",
    "plugins",
    "mkdoc",
    "contribution",
    "how-to",
    "actions",
    "molecule",
    "ansible",
    "github",
    "requirements",
    "",  # empty scope
]

CATEGORIES = {
    "Feat": "Features ✨",
    "Fix": "Bug Fixes 🐛",
    "Cut": "Cut ✂️",
    "Doc": "Documentation 📚",
    "CI": "CI 👷",
    "Bump": "Bump ☝️",
    "Test": "Test 🚨",
    "Revert": "Revert ⏪ ",
    "Refactor": "Refactoring 🔨",
}


class Dumper(yaml.Dumper):
    """
    Make yamllint happy
    https://github.com/yaml/pyyaml/issues/234#issuecomment-765894586
    """

    def increase_indent(self, flow=False, *args, **kwargs):
        return super().increase_indent(flow=flow, indentless=False)


if __name__ == "__main__":
    result_list = []
    for scope in SCOPES:
        if scope != "":
            # First add Breaking Changes
            result_list.append(
                {
                    "title": f"`{scope}` Breaking Changes 🛠",
                    "labels": [f"rn: Feat({scope})!", f"rn: Fix({scope})!"],
                }
            )
            if scope in ["eos_designs", "eos_cli_config_gen"]:
                result_list[-1]["labels"].extend(
                    [
                        "rn: Feat(eos_designs-eos_cli_config_gen)!",
                        "rn: Feat(eos_cli_config_gen-eos_designs)!",
                    ]
                )
            # Then add the rest of the changes for each scope
            for cc_type, rn_title in CATEGORIES.items():
                result_list.append(
                    {
                        "title": f"`{scope}` {rn_title}",
                        "labels": [f"rn: {cc_type}({scope})"],
                    }
                )
                if scope in ["eos_designs", "eos_cli_config_gen"]:
                    result_list[-1]["labels"].extend(
                        [
                            "rn: Feat(eos_designs-eos_cli_config_gen)",
                            "rn: Feat(eos_cli_config_gen-eos_designs)",
                        ]
                    )
        else:  # scope == ""
            result_list.append(
                {
                    "title": "Other Breaking Changes 🛠",
                    "labels": ["rn: Feat!", "rn: Fix!"],
                }
            )
            for cc_type, rn_title in CATEGORIES.items():
                result_list.append(
                    {
                        "title": f"Other {rn_title}",
                        "labels": [f"rn: {cc_type}"],
                    }
                )

    # Add the catch all
    result_list.append(
        {
            "title": "Other Changes 🔀",
            "labels": ["*"],
        }
    )
    with open(r"release.yml", "w") as release_file:
        yaml.dump(
            {"changelog": {"categories": result_list}},
            release_file,
            Dumper=Dumper,
            sort_keys=False,
        )
