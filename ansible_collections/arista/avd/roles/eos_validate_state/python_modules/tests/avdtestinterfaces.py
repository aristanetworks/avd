# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.plugin_utils.eos_validate_state_utils.avdtestbase import AvdTestBase
from ansible_collections.arista.avd.plugins.plugin_utils.utils.get import get


class AvdTestInterfacesState(AvdTestBase):
    """
    AvdTestInterfacesState class for interfaces state tests.
    """

    anta_module = "anta.tests.interfaces"
    categories = ["Interface State"]

    @cached_property
    def test_definition(self) -> dict | None:
        """
        Generates the proper ANTA test definition for all interfaces state tests.

        Returns:
            test_definition (dict): ANTA test definition.
        """

        anta_tests = []

        def add_test(interface_name: str, state: str, proto: str, description: str, custom_field: str) -> None:
            """
            Add a test with the proper parameters to the anta_tests list.
            """
            anta_tests.append(
                {
                    "VerifyInterfacesStatus": {
                        "interfaces": [
                            {
                                "interface": interface_name,
                                "state": state,
                                "protocol_status": proto,
                            }
                        ],
                        "result_overwrite": {"categories": self.categories, "description": description, "custom_field": custom_field},
                    }
                }
            )

        def generate_test_details(interface: dict, description_template: str) -> tuple(str, str, str):
            """
            Generates the state, protocol status, and description for a given interface.

            Args:
                interface (dict): A dictionary containing information about the interface.
                description_template (str): A template string for generating the test description.

            Returns:
                tuple[str, str, str]: A tuple containing the state, protocol status and description.
            """
            if "Loopback" in description_template:
                return "up", "up", description_template
            elif interface["shutdown"]:
                return "adminDown", "down", description_template.format(state="adminDown")
            else:
                return "up", "up", description_template.format(state="up")

        interface_types = [
            ("ethernet_interfaces", r"Ethernet Interface & Line Protocol == \"{state}\""),
            ("port_channel_interfaces", r"Port-Channel Interface & Line Protocol == \"{state}\""),
            ("vlan_interfaces", r"Vlan Interface & Line Protocol == \"{state}\""),
            ("loopback_interfaces", r"Loopback Interface Status & Line Protocol == \"up\""),
        ]

        for interface_key, description_template in interface_types:
            interfaces = get(self.hostvars[self.device_name], interface_key, [])

            for interface in interfaces:
                state, proto, description = generate_test_details(interface, description_template)
                custom_field = f"{interface['name']} - {interface['description']}"

                add_test(str(interface["name"]), state, proto, description, custom_field)

        if get(self.hostvars[self.device_name], "vxlan_interface.Vxlan1") is not None:
            add_test("Vxlan1", "up", "up", r"Vxlan Interface Status & Line Protocol == \"up\"", "Vxlan1")

        return {self.anta_module: anta_tests} if anta_tests else None
