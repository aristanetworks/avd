# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import pytest

from pyavd._cv.api.arista.studio.v1 import InputSchema
from pyavd._cv.workflows.deploy_cv_pathfinder_metadata_to_cv import generate_internet_exit_metadata, is_pathfinder_location_supported, upsert_pathfinder
from pyavd._cv.workflows.models import AvdDevice, CVDevice


@pytest.mark.parametrize("location_supported", [False, True], ids=["unsupported-studio", "supported-studio"])
@pytest.mark.parametrize(
    ("location", "has_location"),
    [
        pytest.param({}, False, id="absent"),
        pytest.param({"region": None, "site": None, "address": None}, False, id="none"),
        pytest.param({"region": "", "site": "", "address": ""}, False, id="empty"),
        pytest.param({"region": "REGION1"}, True, id="region-only"),
        pytest.param({"site": "SITE1"}, True, id="site-only"),
        pytest.param({"address": "ADDRESS1"}, True, id="address-only"),
        pytest.param({"region": "REGION1", "site": "SITE1", "address": "ADDRESS1"}, True, id="all-populated"),
    ],
)
def test_upsert_pathfinder_location(location: dict[str, str | None], has_location: bool, location_supported: bool) -> None:
    """Warn only when supplied location values cannot be deployed to the metadata studio."""
    studio_schema = (
        InputSchema.from_dict(
            {
                "fields": {
                    "values": {
                        "pathfinderGroup": {
                            "groupProps": {
                                "members": {"values": ["pathfinderRegion", "pathfinderSite", "pathfinderAddress"]},
                            },
                        },
                    },
                },
            },
        )
        if location_supported
        else InputSchema()
    )
    assert is_pathfinder_location_supported(studio_schema) is location_supported
    device = CVDevice(avd_device=AvdDevice(hostname="pathfinder1", serial_number="SERIAL1"))
    studio_inputs = {}

    warnings = upsert_pathfinder(location, device, studio_inputs, studio_schema)

    expected_warnings = (
        ["deploy_cv_pathfinder_metadata_to_cv: Ignoring Pathfinder location information since it is not supported by the metadata studio."]
        if has_location and not location_supported
        else []
    )
    assert warnings == expected_warnings
    pathfinder_values = studio_inputs["pathfinders"][0]["inputs"]["value"]
    location_keys = ("region", "site", "address")
    deployed_location = {key: pathfinder_values[key] for key in location_keys if key in pathfinder_values}
    expected_location = {key: location.get(key) for key in location_keys} if has_location and location_supported else {}
    assert deployed_location == expected_location


def test_generate_internet_exit_metadata_unsupported_policy() -> None:
    """Unsupported policies produce named warnings and do not prevent processing subsequent policies."""
    device = CVDevice(avd_device=AvdDevice(hostname="wan-edge1"))
    metadata = {
        "internet_exit_policies": [
            {"name": "unsupported-policy1", "type": "unsupported-type1"},
            {"name": "direct-policy", "type": "direct"},
            {"name": "unsupported-policy2", "type": "unsupported-type2"},
        ],
    }

    services, warnings = generate_internet_exit_metadata(metadata, device, InputSchema())

    assert not services
    assert warnings == [
        (
            "deploy_cv_pathfinder_metadata_to_cv: Ignoring unsupported internet exit policy 'unsupported-policy1' "
            "with type 'unsupported-type1' for device: wan-edge1."
        ),
        (
            "deploy_cv_pathfinder_metadata_to_cv: Ignoring unsupported internet exit policy 'unsupported-policy2' "
            "with type 'unsupported-type2' for device: wan-edge1."
        ),
    ]
