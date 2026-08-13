# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""
Testing get_avd_facts and get_device_structured_config for the variations of supported inputs.

Only covering variants not already handled in e2e-test-avd,
and just testing that we don't raise.
"""

from pyavd import get_avd_facts, get_device_structured_config
from pyavd.api.schemas import AVDDesign

INPUTS = {
    "testhost1": {"fabric_name": "FABRIC", "devices": [{"name": "testhost1", "type": "l2leaf"}]},
}


def test_get_avd_facts_get_device_structured_config_dicts() -> None:
    avd_facts = get_avd_facts(all_inputs=INPUTS, all_hostvars=None)
    assert len(avd_facts) == len(INPUTS)

    for hostname, hostvars in INPUTS.items():
        structured_config = get_device_structured_config(hostname, hostvars, avd_facts, hostvars=None)
        assert structured_config.hostname == hostname


def test_get_avd_facts_get_device_structured_config_models() -> None:
    models = {name: AVDDesign._load(hostvars) for name, hostvars in INPUTS.items()}
    avd_facts = get_avd_facts(all_inputs=models, all_hostvars=INPUTS)
    assert len(avd_facts) == len(INPUTS)

    for hostname, model in models.items():
        structured_config = get_device_structured_config(hostname, model, avd_facts, hostvars=INPUTS[hostname])
        assert structured_config.hostname == hostname
