#!/usr/bin/env python
"""
generate_release.py

This script is used to generate the release.yml file as per
https://docs.github.com/en/repositories/releasing-projects-on-github/automatically-generated-release-notes
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
]

# CI and Test are excluded from Release Notes
CATEGORIES = {
    "Feat": "Features",
    "Fix": "Bug Fixes",
    "Cut": "Cut",
    "Doc": "Documentation",
    # "CI": "CI",
    "Bump": "Bump",
    # "Test": "Test",
    "Revert": "Revert",
    "Refactor": "Refactoring",
}


class SafeDumper(yaml.SafeDumper):
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
        exclude_list.append(f"rn: Test({scope})")
        exclude_list.append(f"rn: CI({scope})")
    exclude_list.extend(["rn: Test", "rn: CI"])

    # Then add the categories
    # First add Breaking Changes
    breaking_label_categories = ["Feat", "Fix", "Cut", "Revert", "Refactor", "Bump"]
    breaking_labels = [f"rn: {cc_type}({scope})!" for cc_type in breaking_label_categories for scope in SCOPES]
    breaking_labels.extend([f"rn: {cc_type}!" for cc_type in breaking_label_categories])

    categories_list.append(
        {
            "title": "Breaking Changes",
            "labels": breaking_labels,
        }
    )
    # Add fixes in eos_cli_config_gen
    categories_list.append(
        {
            "title": "Fixed issues in eos_cli_config_gen",
            "labels": ["rn: Fix(eos_cli_config_gen)"],
        }
    )

    # Add fixes in eos_designs
    categories_list.append(
        {
            "title": "Fixed issues in eos_designs",
            "labels": ["rn: Fix(eos_designs)"],
        }
    )

    # Add other fixes
    other_fixes_labels = [f"rn: Fix({scope})" for scope in SCOPES if scope not in ["eos_cli_config_gen", "eos_designs"]]
    other_fixes_labels.append("rn: Fix")

    categories_list.append(
        {
            "title": "Other Fixed issues",
            "labels": other_fixes_labels,
        }
    )

    # Add Documentation
    doc_labels = [f"rn: Doc({scope})" for scope in SCOPES]
    doc_labels.append("rn: Doc")

    categories_list.append(
        {
            "title": "Documentation",
            "labels": doc_labels,
        }
    )

    # Add new features in eos_cli_config_gen
    categories_list.append(
        {
            "title": "New features and enhancements in eos_cli_config_gen",
            "labels": ["rn: Feat(eos_cli_config_gen)"],
        }
    )

    # Add new features in eos_designs
    categories_list.append(
        {
            "title": "New features and enhancements in eos_designs",
            "labels": ["rn: Feat(eos_designs)"],
        }
    )

    # Add other new features
    other_feat_labels = [f"rn: Feat({scope})" for scope in SCOPES if scope not in ["eos_cli_config_gen", "eos_designs"]]
    other_feat_labels.append("rn: Feat")

    categories_list.append(
        {
            "title": "Other new features and enhancements",
            "labels": other_feat_labels,
        }
    )

    # Add the catch all
    categories_list.append(
        {
            "title": "Other Changes",
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
            Dumper=SafeDumper,
            sort_keys=False,
        )
