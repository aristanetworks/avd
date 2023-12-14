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
    interface_types = [
        ("ethernet_interfaces", "Ethernet Interface & Line Protocol == '{state}'"),
        ("port_channel_interfaces", "Port-Channel Interface & Line Protocol == '{state}'"),
        ("vlan_interfaces", "Vlan Interface & Line Protocol == '{state}'"),
        ("loopback_interfaces", "Loopback Interface Status & Line Protocol == 'up'"),
    ]

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
            if interface["shutdown"]:
                return "adminDown", "down", description_template.format(state="adminDown")
            return "up", "up", description_template.format(state="up")

        required_keys = ["name", "shutdown", "description"]

        for interface_key, description_template in self.interface_types:
            interfaces = get(self.structured_config, interface_key, [])

            for idx, interface in enumerate(interfaces):
                self.update_interface_shutdown(interface=interface)
                if not self.validate_data(data=interface, data_path=f"{interface_key}.[{idx}]", required_keys=required_keys):
                    continue
                state, proto, description = generate_test_details(interface, description_template)
                custom_field = f"{interface['name']} - {interface['description']}"

                add_test(str(interface["name"]), state, proto, description, custom_field)

        if get(self.hostvars[self.device_name], "vxlan_interface.Vxlan1") is not None:
            add_test("Vxlan1", "up", "up", "Vxlan Interface Status & Line Protocol == 'up'", "Vxlan1")

        return {self.anta_module: anta_tests} if anta_tests else None
