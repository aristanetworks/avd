# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

import pytest

from pyavd import get_fabric_documentation


def test_get_fabric_documentation_with_no_connected_endpoints(monkeypatch: pytest.MonkeyPatch) -> None:
    """Test connected endpoints documentation empty state."""

    class FabricDocumentationFacts:
        def __init__(self, *args: object, **kwargs: object) -> None:
            pass

        def render(self) -> dict[str, object]:
            return {
                "fabric_name": "EMPTY_FABRIC",
                "toc": False,
                "fabric_switches": [],
                "topology_links": [],
                "uplink_ipv4_networks": [],
                "loopback_ipv4_networks": [],
                "vtep_loopback_ipv4_networks": [],
                "has_isis": False,
                "all_connected_endpoints": {},
                "all_connected_endpoints_keys": [],
                "all_port_profiles": [],
            }

    monkeypatch.setattr("pyavd._eos_designs.fabric_documentation_facts.FabricDocumentationFacts", FabricDocumentationFacts)

    fabric_documentation_obj = get_fabric_documentation(
        avd_facts={},
        structured_configs={},
        fabric_name="EMPTY_FABRIC",
        include_connected_endpoints=True,
        toc=False,
    )

    assert "## Connected Endpoints\n\nNo connected endpoint configured!" in fabric_documentation_obj.fabric_documentation
