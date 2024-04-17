# Copyright (c) 2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import absolute_import, annotations, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
name: cv_zscaler_endpoints
author: Arista Ansible Team (@aristanetworks)
version_added: "4.8.0"
requirements:
  - md_toc
short_description: PREVIEW - Fetch Zscaler endpoints used for CV Pathfinder internet-exit integration.
description:
  - Use this to autofill the `zscaler_endpoints` data model.
  - The arguments are optional. If not set the same vars must be set.
options:
  cv_server:
    type: str
    description: CV server.
    required: true
  cv_token:
    type: str
    description: CV token.
    required: true
  cv_verify_certs:
    type: bool
    description: Verify SSL certificates.
    default: true
  serial_number:
    type: str
    description: Device serial number.
    required: true
  inventory_hostname:
    type: str
    description: Device inventory hostname.
    required: true
"""

EXAMPLES = r"""
---
zscaler_endpoints: "{{ lookup('arista.avd.cv_zscaler_endpoints') }}"
"""

RETURN = r"""
---
_value:
  description: Dict according to the `zscaler_endpoints` data model.
  type: dict
"""

import logging
from asyncio import run
from typing import TYPE_CHECKING

from ansible.errors import AnsibleLookupError
from ansible.plugins.lookup import LookupBase, display

from ansible_collections.arista.avd.plugins.plugin_utils.cv_client.client import CVClient
from ansible_collections.arista.avd.plugins.plugin_utils.eos_designs_shared_utils import SharedUtils
from ansible_collections.arista.avd.plugins.plugin_utils.schema.avdschematools import AvdSchemaTools
from ansible_collections.arista.avd.plugins.plugin_utils.utils import PythonToAnsibleHandler, get, get_templar

if TYPE_CHECKING:
    from ansible_collections.arista.avd.plugins.plugin_utils.cv_client.api.arista.swg.v1 import VpnEndpoint

LOGGER = logging.getLogger("ansible_collections.arista.avd")
LOGGING_LEVELS = ["DEBUG", "INFO", "ERROR", "WARNING", "CRITICAL"]


class LookupModule(LookupBase):
    def run(self, variables=None, **kwargs):

        # Setup module logging - we don't return 'result' to just giving a dummy dict.
        setup_module_logging({})

        self.set_options(var_options=variables, direct=kwargs)

        self.shared_utils = self.get_avd_shared_utils(variables)

        # Running asyncio coroutine to deploy everything.
        return run(self.get_zscaler_endpoints())

    def get_avd_shared_utils(self, variables) -> SharedUtils:
        # TODO: Figure out what to do with templating of vars, mapping switch.*

        # Ensuring we don't evaluate the inline jinja.
        variables["zscaler_endpoints"] = None

        # Load schema tools and perform conversion and validation
        avdschematools = AvdSchemaTools(
            hostname=self.get_option("inventory_hostname"),
            ansible_display=display,
            schema_id="eos_designs",
            conversion_mode="debug",
            validation_mode="error",
            plugin_name="arista.avd.cv_zscaler_endpoints",
        )
        result = avdschematools.convert_and_validate_data(variables)
        if result.get("failed"):
            raise AnsibleLookupError(result["msg"])

        # Get updated templar instance to be passed along to our simplified "templater"
        templar = get_templar(self, variables)

        return SharedUtils(variables, templar)

    async def get_zscaler_endpoints(self):
        serial_number = self.shared_utils.serial_number
        location = get(self.shared_utils.wan_site or {}, "location")
        if location is None:
            raise AnsibleLookupError("Unable to determine the WAN Site location.")

        cv_server = self.get_option("cv_server")
        cv_token = self.get_option("cv_token")
        cv_verify_certs = self.get_option("cv_verify_certs")

        async with CVClient(servers=[cv_server], token=cv_token, verify_certs=cv_verify_certs) as cv_client:
            await cv_client.set_swg_device(device_id=serial_number, service="zscaler", location=location)
            cv_endpoint_status = await cv_client.wait_for_swg_endpoint_status(device_id=serial_number, service="zscaler")

        zscaler_endpoints = {}
        if not getattr(cv_endpoint_status.vpn_endpoint_map, "values", None):
            return zscaler_endpoints

        for key in ("primary", "secondary", "tertiary"):
            if key in cv_endpoint_status.vpn_endpoint_map.values:
                vpn_endpoint: VpnEndpoint = cv_endpoint_status.vpn_endpoint_map.values[key]
                zscaler_endpoints[key] = {
                    "ip_address": vpn_endpoint.ip_address,
                    "datacenter": vpn_endpoint.datacenter,
                    "city": vpn_endpoint.city,
                    "country": vpn_endpoint.country,
                    "latitude": vpn_endpoint.latitude,
                    "longitude": vpn_endpoint.longitude,
                }

        return zscaler_endpoints


def setup_module_logging(result: dict) -> None:
    """
    Add a Handler to copy the logs from the plugin into Ansible output based on their level

    Parameters:
        result: The dictionary used for the ansible module results
    """
    python_to_ansible_handler = PythonToAnsibleHandler(result, display)
    LOGGER.addHandler(python_to_ansible_handler)
    # TODO mechanism to manipulate the logger globally for pyavd
    # Keep debug to be able to see logs with `-v` and `-vvv`
    LOGGER.setLevel(logging.DEBUG)
