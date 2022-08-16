#!/usr/bin/env python
"""
generate_release.py
"""

import yaml

SCOPES = [
    "build_output_folders",
    "cvp_configlet_upload",
    "dhcp_provisioner",
    "eos_cli_config_gen",
    "eos_config_deploy_cvp",
    "eos_config_deploy_eapi",
    "eos_designs",
    "eos_snapshot",
    "eos_validate_state",
    "plugins",
    "requirements",
    "",  # empty scope
]

# CI and Test are excluded from Release Notes
CATEGORIES = {
    "Feat": "Features ✨",
    "Fix": "Bug Fixes 🐛",
    "Cut": "Cut ✂️",
    "Doc": "Documentation 📚",
    # "CI": "CI 👷",
    "Bump": "Bump ☝️",
    # "Test": "Test 🚨",
    "Revert": "Revert ⏪ ",
    "Refactor": "Refactoring 🔨",
}


class Dumper(yaml.Dumper):
    """
    Make yamllint happy
    https://github.com/yaml/pyyaml/issues/234#issuecomment-765894586
    """

    # pylint: disable=R0901,W0613,W1113

    def increase_indent(self, flow=False, *args, **kwargs):
        return super().increase_indent(flow=flow, indentless=False)


if __name__ == "__main__":
    exclude_list = []
    categories_list = []
    # First add exclude labels
    for scope in SCOPES:
        if scope != "":
            exclude_list.append(f"rn: Test({scope})")
            exclude_list.append(f"rn: CI({scope})")
        else:
            exclude_list.append("rn: Test")
            exclude_list.append("rn: CI")
    # Then add the categories
    # First add Breaking Changes
    breaking_labels = []
    for scope in SCOPES:
        for cc_type, rn_title in CATEGORIES.items():
            # This assumes that Doc and Bump cannot be breaking
            if cc_type in ["Feat", "Fix", "Cut", "Revert", "Refactor"]:
                if scope != "":
                    breaking_labels.append(f"rn: {cc_type}({scope})!")
                else:
                    breaking_labels.append(f"rn: {cc_type}!")
    categories_list.append(
        {
            "title": "Breaking Changes 🛠",
            "labels": breaking_labels,
        }
    )
    # Add fixes in eos_cli_config_gen
    categories_list.append(
        {
            "title": "Fixed issues in eos_cli_config_gen 🐛",
            "labels": "rn: Fix(eos_cli_config_gen)",
        }
    )
    # Add fixes in eos_designs
    categories_list.append(
        {
            "title": "Fixed issues in eos_designs 🐛",
            "labels": "rn: Fix(eos_designs)",
        }
    )
    # Add other fixes
    other_fixes_labels = []
    for scope in SCOPES:
        if scope not in ["eos_cli_config_gen", "eos_designs", ""]:
            other_fixes_labels.append(f"rn: Fix({scope})")
        elif scope == "":
            other_fixes_labels.append("rn: Fix")
    categories_list.append(
        {
            "title": "Other Fixed issues 🐛",
            "labels": other_fixes_labels,
        }
    )
    # Add Documentation
    doc_labels = []
    for scope in SCOPES:
        if scope != "":
            doc_labels.append(f"rn: Doc({scope})")
        elif scope == "":
            doc_labels.append("rn: Doc")
    categories_list.append(
        {
            "title": "Documentation 📚",
            "labels": doc_labels,
        }
    )
    # Add new features in eos_cli_config_gen
    categories_list.append(
        {
            "title": "New features and enhancements in eos_cli_config_gen ✨",
            "labels": "rn: Feat(eos_cli_config_gen)",
        }
    )
    # Add new features in eos_designs
    categories_list.append(
        {
            "title": "New features and enhancements in eos_designs ✨",
            "labels": "rn: Feat(eos_designs)",
        }
    )
    # Add other new features
    other_feat_labels = []
    for scope in SCOPES:
        if scope not in ["eos_cli_config_gen", "eos_designs", ""]:
            other_feat_labels.append(f"rn: Feat({scope})")
        elif scope == "":
            other_feat_labels.append("rn: Feat")
    categories_list.append(
        {
            "title": "Other new features and enhancements ✨",
            "labels": other_feat_labels,
        }
    )

    # Add the catch all
    categories_list.append(
        {
            "title": "Other Changes 🔀",
            "labels": ["*"],
        }
    )
    with open(r"release.yml", "w", encoding="utf-8") as release_file:
        yaml.dump(
            {
                "changelog": {
                    "exclude": {"labels": exclude_list},
                    "categories": categories_list,
                }
            },
            release_file,
            Dumper=Dumper,
            sort_keys=False,
        )
