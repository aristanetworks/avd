# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from pyavd import get_avd_facts


def test_get_avd_facts(all_inputs: dict, pool_manager):
    """
    Test get_avd_facts
    """
    avd_facts = get_avd_facts(all_inputs, pool_manager=pool_manager)

    assert isinstance(avd_facts, dict)
    assert "avd_switch_facts" in avd_facts.keys()
    assert isinstance(avd_facts["avd_switch_facts"], dict)
    assert len(avd_facts["avd_switch_facts"]) == len(all_inputs)
    assert "avd_overlay_peers" in avd_facts.keys()
    assert isinstance(avd_facts["avd_overlay_peers"], dict)
    assert "avd_topology_peers" in avd_facts.keys()
    assert isinstance(avd_facts["avd_topology_peers"], dict)

    # Ensure that the we did not change any data from the preloaded id pool data.
    assert len(pool_manager.changed_id_files) == 0
