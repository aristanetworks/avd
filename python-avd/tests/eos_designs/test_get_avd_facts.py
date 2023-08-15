from pyavd import get_avd_facts


def test_get_avd_facts(all_inputs: dict):
    """
    Test get_avd_facts
    """
    avd_facts = get_avd_facts(all_inputs)

    assert isinstance(avd_facts, dict)
    assert "avd_switch_facts" in avd_facts.keys()
    assert isinstance(avd_facts["avd_switch_facts"], dict)
    assert len(avd_facts["avd_switch_facts"]) == len(all_inputs)
    assert "avd_overlay_peers" in avd_facts.keys()
    assert isinstance(avd_facts["avd_overlay_peers"], dict)
    assert "avd_topology_peers" in avd_facts.keys()
    assert isinstance(avd_facts["avd_topology_peers"], dict)
