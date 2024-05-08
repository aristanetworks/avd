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
    vars:
      - name: cv_server
  cv_token:
    type: str
    description: CV token.
    required: true
    vars:
      - name: cv_token
  cv_verify_certs:
    type: bool
    description: Verify SSL certificates.
    default: true
    vars:
      - name: cv_verify_certs
  serial_number:
    type: str
    description: Device serial number.
    required: true
    vars:
      - name: serial_number
  inventory_hostname:
    type: str
    description: Device inventory hostname.
    required: true
    vars:
      - name: inventory_hostname
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
    from ansible_collections.arista.avd.plugins.plugin_utils.cv_client.api.arista.swg.v1 import Location, VpnEndpoint

LOGGER = logging.getLogger("ansible_collections.arista.avd")
LOGGING_LEVELS = ["DEBUG", "INFO", "ERROR", "WARNING", "CRITICAL"]


class LookupModule(LookupBase):
    def run(self, terms, variables=None, **kwargs):

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

        # Get updated templar instance to be passed along to our simplified "templater"
        templar = get_templar(self, variables)

        # Initialize SharedUtils class to be passed to EosDesignsFacts below.
        shared_utils = SharedUtils(hostvars=variables, templar=templar)

        # Insert dynamic keys into the input data if not set.
        # These keys are required by the schema, but the default values are set inside shared_utils.
        variables.setdefault("node_type_keys", shared_utils.node_type_keys)
        variables.setdefault("connected_endpoints_keys", shared_utils.connected_endpoints_keys)
        variables.setdefault("network_services_keys", shared_utils.network_services_keys)

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

        return shared_utils

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
        if not getattr(cv_endpoint_status, "vpn_endpoints", None) or not getattr(cv_endpoint_status.vpn_endpoints, "values", None):
            return zscaler_endpoints

        for key in ("primary", "secondary", "tertiary"):
            if key in cv_endpoint_status.vpn_endpoints.values:
                vpn_endpoint: VpnEndpoint = cv_endpoint_status.vpn_endpoints.values[key]
                location: Location = vpn_endpoint.endpoint_location
                zscaler_endpoints[key] = {
                    "ip_address": vpn_endpoint.ip_address.value,
                    "datacenter": vpn_endpoint.datacenter,
                    "city": location.city,
                    "country": location.country,
                    "latitude": location.latitude,
                    "longitude": location.longitude,
                }

        # Lookup plugins are always expected to return an iterable,
        # but if we only return a single item, it will be unpacked to the value by Ansible.
        return [zscaler_endpoints]


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
