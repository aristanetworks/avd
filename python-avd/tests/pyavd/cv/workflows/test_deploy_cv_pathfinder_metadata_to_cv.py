# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from pyavd._cv.api.arista.studio.v1 import InputSchema
from pyavd._cv.workflows.deploy_cv_pathfinder_metadata_to_cv import generate_internet_exit_metadata
from pyavd._cv.workflows.models import AvdDevice, CVDevice


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
