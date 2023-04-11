from __future__ import annotations

import pathlib
import sys

import yaml

from ansible_collections.arista.avd.plugins.plugin_utils.schema.avdschema import AvdSchema
from ansible_collections.arista.avd.plugins.plugin_utils.schema.avdtocoverageschemaconverter import AvdToCoverageSchemaConverter

MOLECULE_PATH = pathlib.Path(__file__).parent.parent / "ansible_collections" / "arista" / "avd" / "molecule"
CURRENT_COVERAGE_FILE = pathlib.Path(__file__).parent / "current_coverage.yml"

WARNING = "\033[93m"
FAIL = "\033[91m"


def _load_current_coverage() -> dict:
    """
    Load current values for schema coverage
    """
    with open(CURRENT_COVERAGE_FILE, "r", encoding="utf-8") as f:
        try:
            return yaml.safe_load(f.read())
        except Exception as e:
            print(e)
            raise


def _update_current_coverage():
    file_data = _load_current_coverage()
    for key, value in file_data.items():
        if CURRENT_COVERAGE[key] != value:
            print(f"{WARNING}Warning: Molecule Schema Coverage increased - please commit the updated value")
    with open(CURRENT_COVERAGE_FILE, "w", encoding="utf-8") as f:
        yaml.safe_dump(CURRENT_COVERAGE, f)


CURRENT_COVERAGE = _load_current_coverage()


def _run_schema_molecule_coverage(schema_id: str, data_paths: list[pathlib.Path]) -> None:
    avdschema = AvdSchema(schema_id=schema_id)
    converter = AvdToCoverageSchemaConverter(avdschema)
    coverage_tree = converter.convert_schema()

    for file in data_paths:
        with open(file, "r", encoding="utf-8") as f:
            data = ""
            try:
                data = yaml.safe_load(f.read())
            except Exception as e:
                print(e)
        # Empty list for root node
        coverage_tree.get_coverage(data, [])

    percentage = coverage_tree.get_coverage_percentage()
    if percentage >= CURRENT_COVERAGE[schema_id]:
        CURRENT_COVERAGE[schema_id] = percentage
    else:
        raise ValueError(f"Molecule coverage for `{schema_id}` decreased from {CURRENT_COVERAGE[schema_id]} to {percentage}!")


def eos_cli_config_gen_schema_molecule_coverage():
    """
    Runs schema coverage for eos_cli_config_gen schema
    """
    schema_id = "eos_cli_config_gen"
    # Maybe make a function to generate data_paths
    scenarios = ["eos_cli_config_gen"]
    data_paths = []
    for scenario in scenarios:
        path = MOLECULE_PATH / scenario / "inventory"
        data_paths.extend(path.glob("*_vars/**/*.yml"))

    _run_schema_molecule_coverage(schema_id, data_paths)


def eos_designs_schema_molecule_coverage():
    """
    Runs schema coverage for eos_designs schema
    """
    schema_id = "eos_designs"
    scenarios = [
        "eos_designs-l2ls",
        "eos_designs-mpls-isis-sr-ldp",
        "eos_designs-twodc-5stage-clos",
        "eos_designs_negative_unit_tests",
        "eos_designs_unit_tests",
        "eos_designs_unit_tests_v4.0",
        "evpn_underlay_ebgp_overlay_ebgp",
        "evpn_underlay_isis_overlay_ibgp",
        "evpn_underlay_ospf_overlay_ebgp",
        "evpn_underlay_rfc5549_overlay_ebgp",
        "example-campus-fabric",
        "example-dual-dc-l3ls",
        "example-l2ls-fabric",
        "example-single-dc-l3ls",
    ]
    data_paths = []
    for scenario in scenarios:
        path = MOLECULE_PATH / scenario / "inventory"
        data_paths.extend(path.glob("*_vars/**/*.yml"))
        # try:
        #     path = MOLECULE_PATH / scenario / "inventory" / "host_vars"
        #     data_paths.extend(path.iterdir())
        # except FileNotFoundError:
        #     # No host_vars
        #     pass
        # try:
        #     path = MOLECULE_PATH / scenario / "inventory" / "group_vars"
        #     data_paths.extend(path.iterdir())
        # except FileNotFoundError:
        #     # No group_vars
        #     pass

    _run_schema_molecule_coverage(schema_id, data_paths)


if __name__ == "__main__":
    print("Running schema coverage for molecule...\n")
    print(
        f"Current coverage values are:\n  * eos_cli_config_gen: {CURRENT_COVERAGE['eos_cli_config_gen']}\n  * eos_designs: {CURRENT_COVERAGE['eos_designs']}\n"
    )

    exceptions = []

    print("### eos_cli_config_gen ...")
    try:
        eos_cli_config_gen_schema_molecule_coverage()
    except ValueError as e:
        exceptions.append(e)
    print("### eos_cli_config_gen - [done]")

    print("### eos_designs ...")
    eos_designs_schema_molecule_coverage()
    print("### eos_designs - [done]")

    if exceptions:
        print("\n#############################################\n")
        sys.exit("\n".join(str(e) for e in exceptions))
    # Update saved coverage
    _update_current_coverage()
    sys.exit()
