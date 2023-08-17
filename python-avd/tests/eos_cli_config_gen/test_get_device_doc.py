# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from pyavd import get_device_doc


def test_get_device_doc(hostname: str, all_inputs: dict, device_docs: dict):
    """
    Test get_device_config
    """

    structured_config: dict = all_inputs[hostname]
    if not structured_config.get("generate_device_documentation", True):
        return

    expected_doc: str = device_docs.get(hostname, "")

    device_doc = get_device_doc(structured_config, add_md_toc=True)

    assert isinstance(device_doc, str)
    assert device_doc == expected_doc
