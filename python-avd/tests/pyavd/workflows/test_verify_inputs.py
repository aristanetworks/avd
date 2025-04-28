# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.


import cProfile
import logging
import re
from collections.abc import Callable
from contextlib import nullcontext as does_not_raise

import pytest
from _pytest.python_api import RaisesContext

from pyavd._cv.client.exceptions import CVDuplicatedDevices
from pyavd._cv.workflows.models import CVDevice
from pyavd._cv.workflows.verify_inputs import identify_duplicated_devices, verify_device_inputs

TWO_DUPED_SERIAL_PATTERNS = [
    "\\('Duplicated devices found in inventory.*\\{"
    "'serial1': \\["
    "CVDevice\\(hostname='switch1'.*serial_number='serial1'.*"
    "CVDevice\\(hostname='switch2'.*serial_number='serial1'.*"
    "'serial3': \\["
    "CVDevice\\(hostname='switch3'.*serial_number='serial3'.*"
    "CVDevice\\(hostname='switch4', serial_number='serial3'.*",
]

NO_DUPS_DEVICES = [
    CVDevice(hostname="switch1", serial_number="serial1", system_mac_address="aa:bb:cc:dd:ee:f1"),
    CVDevice(hostname="switch2", serial_number="serial2", system_mac_address="aa:bb:cc:dd:ee:f2"),
    CVDevice(hostname="switch3", serial_number="serial3", system_mac_address="aa:bb:cc:dd:ee:f3"),
    CVDevice(hostname="switch4", serial_number="serial4", system_mac_address="aa:bb:cc:dd:ee:f4"),
    CVDevice(hostname="switch5", serial_number="serial5", system_mac_address="aa:bb:cc:dd:ee:f5"),
    CVDevice(hostname="switch6", serial_number="serial6", system_mac_address="aa:bb:cc:dd:ee:f6"),
    CVDevice(hostname="switch7", serial_number="serial7"),
    CVDevice(hostname="switch8", serial_number="serial8"),
    CVDevice(hostname="switch9", system_mac_address="aa:bb:cc:dd:ee:f9"),
    CVDevice(hostname="switch10", system_mac_address="aa:bb:cc:dd:ee:f0"),
    CVDevice(hostname="switch11"),
    CVDevice(hostname="switch12"),
]

TWO_DUPED_SERIAL_DEVICES = [
    CVDevice(hostname="switch1", serial_number="serial1", system_mac_address="aa:bb:cc:dd:ee:f1"),
    CVDevice(hostname="switch2", serial_number="serial1", system_mac_address="aa:bb:cc:dd:ee:f2"),
    CVDevice(hostname="switch3", serial_number="serial3"),
    CVDevice(hostname="switch4", serial_number="serial3"),
    CVDevice(hostname="switch5", serial_number="serial5", system_mac_address="aa:bb:cc:dd:ee:f5"),
    CVDevice(hostname="switch6", serial_number="serial6", system_mac_address="aa:bb:cc:dd:ee:f6"),
    CVDevice(hostname="switch7", serial_number="serial7"),
    CVDevice(hostname="switch8", serial_number="serial8"),
    CVDevice(hostname="switch9", system_mac_address="aa:bb:cc:dd:ee:f9"),
    CVDevice(hostname="switch10", system_mac_address="aa:bb:cc:dd:ee:f0"),
    CVDevice(hostname="switch11"),
    CVDevice(hostname="switch12"),
]

TWO_DUPED_SYS_MAC_DEVICES = [
    CVDevice(hostname="switch1", system_mac_address="aa:bb:cc:dd:ee:f1"),
    CVDevice(hostname="switch2", system_mac_address="aa:bb:cc:dd:ee:f1"),
    CVDevice(hostname="switch3", serial_number="serial3", system_mac_address="aa:bb:cc:dd:ee:f3"),
    CVDevice(hostname="switch4", serial_number="serial4", system_mac_address="aa:bb:cc:dd:ee:f3"),
    CVDevice(hostname="switch5", serial_number="serial5", system_mac_address="aa:bb:cc:dd:ee:f5"),
    CVDevice(hostname="switch6", serial_number="serial6", system_mac_address="aa:bb:cc:dd:ee:f6"),
    CVDevice(hostname="switch7", serial_number="serial7"),
    CVDevice(hostname="switch8", serial_number="serial8"),
    CVDevice(hostname="switch9", system_mac_address="aa:bb:cc:dd:ee:f9"),
    CVDevice(hostname="switch10", system_mac_address="aa:bb:cc:dd:ee:f0"),
    CVDevice(hostname="switch11"),
    CVDevice(hostname="switch12"),
]

TWO_DUPED_SYS_MAC_UNIQ_SER_DEVICES = [
    CVDevice(hostname="switch1", system_mac_address="aa:bb:cc:dd:ee:f1"),
    CVDevice(hostname="switch2", system_mac_address="aa:bb:cc:dd:ee:f2"),
    CVDevice(hostname="switch3", serial_number="serial3", system_mac_address="aa:bb:cc:dd:ee:f3"),
    CVDevice(hostname="switch4", serial_number="serial4", system_mac_address="aa:bb:cc:dd:ee:f3"),
    CVDevice(hostname="switch5", serial_number="serial5", system_mac_address="aa:bb:cc:dd:ee:f5"),
    CVDevice(hostname="switch6", serial_number="serial6", system_mac_address="aa:bb:cc:dd:ee:f5"),
    CVDevice(hostname="switch7", serial_number="serial7"),
    CVDevice(hostname="switch8", serial_number="serial8"),
    CVDevice(hostname="switch9", system_mac_address="aa:bb:cc:dd:ee:f9"),
    CVDevice(hostname="switch10", system_mac_address="aa:bb:cc:dd:ee:f0"),
    CVDevice(hostname="switch11"),
    CVDevice(hostname="switch12"),
]

ONE_DUPED_SERIAL_ONE_DUPED_SYS_MAC_DEVICES = [
    CVDevice(hostname="switch1", serial_number="serial1", system_mac_address="aa:bb:cc:dd:ee:f1"),
    CVDevice(hostname="switch2", serial_number="serial1", system_mac_address="aa:bb:cc:dd:ee:f2"),
    CVDevice(hostname="switch3", serial_number="serial3", system_mac_address="aa:bb:cc:dd:ee:f3"),
    CVDevice(hostname="switch4", serial_number="serial4", system_mac_address="aa:bb:cc:dd:ee:f3"),
    CVDevice(hostname="switch5", serial_number="serial5", system_mac_address="aa:bb:cc:dd:ee:f5"),
    CVDevice(hostname="switch6", serial_number="serial6", system_mac_address="aa:bb:cc:dd:ee:f6"),
    CVDevice(hostname="switch7", serial_number="serial7"),
    CVDevice(hostname="switch8", serial_number="serial8"),
    CVDevice(hostname="switch9", system_mac_address="aa:bb:cc:dd:ee:f9"),
    CVDevice(hostname="switch10", system_mac_address="aa:bb:cc:dd:ee:f0"),
    CVDevice(hostname="switch11"),
    CVDevice(hostname="switch12"),
]

ONE_DUPED_SERIAL_ONE_DUPED_SYS_MAC_SAME_DEVICES_DEVICES = [
    CVDevice(hostname="switch1", serial_number="serial1", system_mac_address="aa:bb:cc:dd:ee:f1"),
    CVDevice(hostname="switch2", serial_number="serial1", system_mac_address="aa:bb:cc:dd:ee:f1"),
    CVDevice(hostname="switch3", serial_number="serial3", system_mac_address="aa:bb:cc:dd:ee:f3"),
    CVDevice(hostname="switch4", serial_number="serial4", system_mac_address="aa:bb:cc:dd:ee:f4"),
    CVDevice(hostname="switch5", serial_number="serial5", system_mac_address="aa:bb:cc:dd:ee:f5"),
    CVDevice(hostname="switch6", serial_number="serial6", system_mac_address="aa:bb:cc:dd:ee:f6"),
    CVDevice(hostname="switch7", serial_number="serial7"),
    CVDevice(hostname="switch8", serial_number="serial8"),
    CVDevice(hostname="switch9", system_mac_address="aa:bb:cc:dd:ee:f9"),
    CVDevice(hostname="switch10", system_mac_address="aa:bb:cc:dd:ee:f0"),
    CVDevice(hostname="switch11"),
    CVDevice(hostname="switch12"),
]

IDENTIFY_DUPLICATED_DEVICES_FULL_INVENTORY = [
    # Unique devices with fully-set attributes
    CVDevice(hostname="switch01", serial_number="serial01", system_mac_address="aa:bb:cc:dd:ee:01"),
    CVDevice(hostname="switch02", serial_number="serial02", system_mac_address="aa:bb:cc:dd:ee:02"),
    CVDevice(hostname="switch03", serial_number="serial03", system_mac_address="aa:bb:cc:dd:ee:03"),
    CVDevice(hostname="switch04", serial_number="serial04", system_mac_address="aa:bb:cc:dd:ee:04"),
    CVDevice(hostname="switch05", serial_number="serial05", system_mac_address="aa:bb:cc:dd:ee:05"),
    # Duplicated serial_number unique system_mac_address
    ## Use case A
    CVDevice(hostname="switch06", serial_number="serial06", system_mac_address="aa:bb:cc:dd:ee:06"),
    CVDevice(hostname="switch07", serial_number="serial06", system_mac_address="aa:bb:cc:dd:ee:07"),
    ## Use case B
    CVDevice(hostname="switch08", serial_number="serial08", system_mac_address="aa:bb:cc:dd:ee:08"),
    CVDevice(hostname="switch09", serial_number="serial08", system_mac_address="aa:bb:cc:dd:ee:09"),
    CVDevice(hostname="switch10", serial_number="serial08", system_mac_address="aa:bb:cc:dd:ee:10"),
    # Duplicated serial_number with unset system_mac_address
    ## Use case A
    CVDevice(hostname="switch11", serial_number="serial11"),
    CVDevice(hostname="switch12", serial_number="serial11"),
    ## Use case B
    CVDevice(hostname="switch13", serial_number="serial13"),
    CVDevice(hostname="switch14", serial_number="serial13"),
    CVDevice(hostname="switch15", serial_number="serial13"),
    # Duplicated serial_number with mix of set and unset system_mac_address
    ## Use case A
    CVDevice(hostname="switch16", serial_number="serial16", system_mac_address="aa:bb:cc:dd:ee:16"),
    CVDevice(hostname="switch17", serial_number="serial16"),
    ## Use case B
    CVDevice(hostname="switch18", serial_number="serial18", system_mac_address="aa:bb:cc:dd:ee:18"),
    CVDevice(hostname="switch19", serial_number="serial18", system_mac_address="aa:bb:cc:dd:ee:19"),
    CVDevice(hostname="switch20", serial_number="serial18"),
    ## Use case C
    CVDevice(hostname="switch21", serial_number="serial21", system_mac_address="aa:bb:cc:dd:ee:21"),
    CVDevice(hostname="switch22", serial_number="serial21"),
    CVDevice(hostname="switch23", serial_number="serial21"),
    ## Use case D
    CVDevice(hostname="switch24", serial_number="serial24", system_mac_address="aa:bb:cc:dd:ee:24"),
    CVDevice(hostname="switch25", serial_number="serial24", system_mac_address="aa:bb:cc:dd:ee:24"),
    CVDevice(hostname="switch26", serial_number="serial24", system_mac_address="aa:bb:cc:dd:ee:26"),
    CVDevice(hostname="switch27", serial_number="serial24", system_mac_address="aa:bb:cc:dd:ee:26"),
    CVDevice(hostname="switch28", serial_number="serial24", system_mac_address="aa:bb:cc:dd:ee:28"),
    CVDevice(hostname="switch29", serial_number="serial24", system_mac_address="aa:bb:cc:dd:ee:29"),
    CVDevice(hostname="switch30", serial_number="serial24"),
    CVDevice(hostname="switch31", serial_number="serial24"),
    # Duplicated system_mac_address with set serial_number
    ## Use case A
    CVDevice(hostname="switch32", serial_number="serial32", system_mac_address="aa:bb:cc:dd:ee:32"),
    CVDevice(hostname="switch33", serial_number="serial33", system_mac_address="aa:bb:cc:dd:ee:32"),
    ## Use case B
    CVDevice(hostname="switch34", serial_number="serial34", system_mac_address="aa:bb:cc:dd:ee:34"),
    CVDevice(hostname="switch35", serial_number="serial35", system_mac_address="aa:bb:cc:dd:ee:34"),
    CVDevice(hostname="switch36", serial_number="serial36", system_mac_address="aa:bb:cc:dd:ee:34"),
    # Duplicated system_mac_address with unset serial_number
    ## Use case A
    CVDevice(hostname="switch37", system_mac_address="aa:bb:cc:dd:ee:37"),
    CVDevice(hostname="switch38", system_mac_address="aa:bb:cc:dd:ee:37"),
    ## Use case B
    CVDevice(hostname="switch39", system_mac_address="aa:bb:cc:dd:ee:39"),
    CVDevice(hostname="switch40", system_mac_address="aa:bb:cc:dd:ee:39"),
    CVDevice(hostname="switch41", system_mac_address="aa:bb:cc:dd:ee:39"),
    # Duplicated system_mac_address with mix or serial_number cases
    ## Use case A
    CVDevice(hostname="switch42", serial_number="serial42", system_mac_address="aa:bb:cc:dd:ee:42"),
    CVDevice(hostname="switch43", serial_number="serial43", system_mac_address="aa:bb:cc:dd:ee:42"),
    CVDevice(hostname="switch44", system_mac_address="aa:bb:cc:dd:ee:42"),
    CVDevice(hostname="switch45", system_mac_address="aa:bb:cc:dd:ee:42"),
    CVDevice(hostname="switch46", system_mac_address="aa:bb:cc:dd:ee:42"),
    ## Use case B
    CVDevice(hostname="switch47", serial_number="serial47", system_mac_address="aa:bb:cc:dd:ee:47"),
    CVDevice(hostname="switch48", system_mac_address="aa:bb:cc:dd:ee:47"),
    ## Use case C
    CVDevice(hostname="switch49", serial_number="serial49", system_mac_address="aa:bb:cc:dd:ee:49"),
    CVDevice(hostname="switch50", system_mac_address="aa:bb:cc:dd:ee:49"),
    CVDevice(hostname="switch51", system_mac_address="aa:bb:cc:dd:ee:49"),
    ## Use case D
    CVDevice(hostname="switch52", serial_number="serial52", system_mac_address="aa:bb:cc:dd:ee:52"),
    CVDevice(hostname="switch53", serial_number="serial53", system_mac_address="aa:bb:cc:dd:ee:52"),
    CVDevice(hostname="switch54", system_mac_address="aa:bb:cc:dd:ee:52"),
    CVDevice(hostname="switch55", system_mac_address="aa:bb:cc:dd:ee:52"),
]

IDENTIFY_DUPLICATED_DEVICES_FULL_INVENTORY_EXPECTED_RETURN = {
    "duplicated_serial_number": {
        "serial06": [
            CVDevice(hostname="switch06", serial_number="serial06", system_mac_address="aa:bb:cc:dd:ee:06", _exists_on_cv=None),
            CVDevice(hostname="switch07", serial_number="serial06", system_mac_address="aa:bb:cc:dd:ee:07", _exists_on_cv=None),
        ],
        "serial08": [
            CVDevice(hostname="switch08", serial_number="serial08", system_mac_address="aa:bb:cc:dd:ee:08", _exists_on_cv=None),
            CVDevice(hostname="switch09", serial_number="serial08", system_mac_address="aa:bb:cc:dd:ee:09", _exists_on_cv=None),
            CVDevice(hostname="switch10", serial_number="serial08", system_mac_address="aa:bb:cc:dd:ee:10", _exists_on_cv=None),
        ],
        "serial11": [
            CVDevice(hostname="switch11", serial_number="serial11", system_mac_address=None, _exists_on_cv=None),
            CVDevice(hostname="switch12", serial_number="serial11", system_mac_address=None, _exists_on_cv=None),
        ],
        "serial13": [
            CVDevice(hostname="switch13", serial_number="serial13", system_mac_address=None, _exists_on_cv=None),
            CVDevice(hostname="switch14", serial_number="serial13", system_mac_address=None, _exists_on_cv=None),
            CVDevice(hostname="switch15", serial_number="serial13", system_mac_address=None, _exists_on_cv=None),
        ],
        "serial16": [
            CVDevice(hostname="switch16", serial_number="serial16", system_mac_address="aa:bb:cc:dd:ee:16", _exists_on_cv=None),
            CVDevice(hostname="switch17", serial_number="serial16", system_mac_address=None, _exists_on_cv=None),
        ],
        "serial18": [
            CVDevice(hostname="switch18", serial_number="serial18", system_mac_address="aa:bb:cc:dd:ee:18", _exists_on_cv=None),
            CVDevice(hostname="switch19", serial_number="serial18", system_mac_address="aa:bb:cc:dd:ee:19", _exists_on_cv=None),
            CVDevice(hostname="switch20", serial_number="serial18", system_mac_address=None, _exists_on_cv=None),
        ],
        "serial21": [
            CVDevice(hostname="switch21", serial_number="serial21", system_mac_address="aa:bb:cc:dd:ee:21", _exists_on_cv=None),
            CVDevice(hostname="switch22", serial_number="serial21", system_mac_address=None, _exists_on_cv=None),
            CVDevice(hostname="switch23", serial_number="serial21", system_mac_address=None, _exists_on_cv=None),
        ],
        "serial24": [
            CVDevice(hostname="switch24", serial_number="serial24", system_mac_address="aa:bb:cc:dd:ee:24", _exists_on_cv=None),
            CVDevice(hostname="switch25", serial_number="serial24", system_mac_address="aa:bb:cc:dd:ee:24", _exists_on_cv=None),
            CVDevice(hostname="switch26", serial_number="serial24", system_mac_address="aa:bb:cc:dd:ee:26", _exists_on_cv=None),
            CVDevice(hostname="switch27", serial_number="serial24", system_mac_address="aa:bb:cc:dd:ee:26", _exists_on_cv=None),
            CVDevice(hostname="switch28", serial_number="serial24", system_mac_address="aa:bb:cc:dd:ee:28", _exists_on_cv=None),
            CVDevice(hostname="switch29", serial_number="serial24", system_mac_address="aa:bb:cc:dd:ee:29", _exists_on_cv=None),
            CVDevice(hostname="switch30", serial_number="serial24", system_mac_address=None, _exists_on_cv=None),
            CVDevice(hostname="switch31", serial_number="serial24", system_mac_address=None, _exists_on_cv=None),
        ],
    },
    "duplicated_system_mac_address_unset_or_mixed_serial_number": {
        "aa:bb:cc:dd:ee:37": [
            CVDevice(hostname="switch37", serial_number=None, system_mac_address="aa:bb:cc:dd:ee:37", _exists_on_cv=None),
            CVDevice(hostname="switch38", serial_number=None, system_mac_address="aa:bb:cc:dd:ee:37", _exists_on_cv=None),
        ],
        "aa:bb:cc:dd:ee:39": [
            CVDevice(hostname="switch39", serial_number=None, system_mac_address="aa:bb:cc:dd:ee:39", _exists_on_cv=None),
            CVDevice(hostname="switch40", serial_number=None, system_mac_address="aa:bb:cc:dd:ee:39", _exists_on_cv=None),
            CVDevice(hostname="switch41", serial_number=None, system_mac_address="aa:bb:cc:dd:ee:39", _exists_on_cv=None),
        ],
        "aa:bb:cc:dd:ee:42": [
            CVDevice(hostname="switch42", serial_number="serial42", system_mac_address="aa:bb:cc:dd:ee:42", _exists_on_cv=None),
            CVDevice(hostname="switch43", serial_number="serial43", system_mac_address="aa:bb:cc:dd:ee:42", _exists_on_cv=None),
            CVDevice(hostname="switch44", serial_number=None, system_mac_address="aa:bb:cc:dd:ee:42", _exists_on_cv=None),
            CVDevice(hostname="switch45", serial_number=None, system_mac_address="aa:bb:cc:dd:ee:42", _exists_on_cv=None),
            CVDevice(hostname="switch46", serial_number=None, system_mac_address="aa:bb:cc:dd:ee:42", _exists_on_cv=None),
        ],
        "aa:bb:cc:dd:ee:47": [
            CVDevice(hostname="switch47", serial_number="serial47", system_mac_address="aa:bb:cc:dd:ee:47", _exists_on_cv=None),
            CVDevice(hostname="switch48", serial_number=None, system_mac_address="aa:bb:cc:dd:ee:47", _exists_on_cv=None),
        ],
        "aa:bb:cc:dd:ee:49": [
            CVDevice(hostname="switch49", serial_number="serial49", system_mac_address="aa:bb:cc:dd:ee:49", _exists_on_cv=None),
            CVDevice(hostname="switch50", serial_number=None, system_mac_address="aa:bb:cc:dd:ee:49", _exists_on_cv=None),
            CVDevice(hostname="switch51", serial_number=None, system_mac_address="aa:bb:cc:dd:ee:49", _exists_on_cv=None),
        ],
        "aa:bb:cc:dd:ee:52": [
            CVDevice(hostname="switch52", serial_number="serial52", system_mac_address="aa:bb:cc:dd:ee:52", _exists_on_cv=None),
            CVDevice(hostname="switch53", serial_number="serial53", system_mac_address="aa:bb:cc:dd:ee:52", _exists_on_cv=None),
            CVDevice(hostname="switch54", serial_number=None, system_mac_address="aa:bb:cc:dd:ee:52", _exists_on_cv=None),
            CVDevice(hostname="switch55", serial_number=None, system_mac_address="aa:bb:cc:dd:ee:52", _exists_on_cv=None),
        ],
    },
    "duplicated_system_mac_address_set_serial_number": {
        "aa:bb:cc:dd:ee:24": [
            CVDevice(hostname="switch24", serial_number="serial24", system_mac_address="aa:bb:cc:dd:ee:24", _exists_on_cv=None),
            CVDevice(hostname="switch25", serial_number="serial24", system_mac_address="aa:bb:cc:dd:ee:24", _exists_on_cv=None),
        ],
        "aa:bb:cc:dd:ee:26": [
            CVDevice(hostname="switch26", serial_number="serial24", system_mac_address="aa:bb:cc:dd:ee:26", _exists_on_cv=None),
            CVDevice(hostname="switch27", serial_number="serial24", system_mac_address="aa:bb:cc:dd:ee:26", _exists_on_cv=None),
        ],
        "aa:bb:cc:dd:ee:32": [
            CVDevice(hostname="switch32", serial_number="serial32", system_mac_address="aa:bb:cc:dd:ee:32", _exists_on_cv=None),
            CVDevice(hostname="switch33", serial_number="serial33", system_mac_address="aa:bb:cc:dd:ee:32", _exists_on_cv=None),
        ],
        "aa:bb:cc:dd:ee:34": [
            CVDevice(hostname="switch34", serial_number="serial34", system_mac_address="aa:bb:cc:dd:ee:34", _exists_on_cv=None),
            CVDevice(hostname="switch35", serial_number="serial35", system_mac_address="aa:bb:cc:dd:ee:34", _exists_on_cv=None),
            CVDevice(hostname="switch36", serial_number="serial36", system_mac_address="aa:bb:cc:dd:ee:34", _exists_on_cv=None),
        ],
    },
}


@pytest.fixture(scope="module")
def generate_x_mock_cvdevices(num_devices: int = 1000000) -> list[CVDevice]:
    return [CVDevice(str(item), str(item), str(item)) for item in range(num_devices)]


@pytest.mark.parametrize(
    (
        "devices",
        "warnings_qty",
        "expected_warning_patterns",
        "logs_qty",
        "expected_logs_patterns",
        "expected_exception_patterns",
        "expected_exception",
        "strict_system_mac_address",
    ),
    [
        pytest.param(
            NO_DUPS_DEVICES,
            # Warnings
            0,
            [],
            # Logs
            0,
            [],
            # Exceptions
            [],
            does_not_raise(),
            # strict_system_mac_address
            False,
            id="NO_DUPS_STRICT_MAC_FALSE",
        ),
        pytest.param(
            NO_DUPS_DEVICES,
            # Warnings
            0,
            [],
            # Logs
            0,
            [],
            # Exceptions
            [],
            does_not_raise(),
            # strict_system_mac_address
            True,
            id="NO_DUPS_STRICT_MAC_TRUE",
        ),
        pytest.param(
            TWO_DUPED_SERIAL_DEVICES,
            # Warnings
            0,
            [],
            # Logs
            0,
            [],
            # Exceptions
            TWO_DUPED_SERIAL_PATTERNS,
            pytest.raises(CVDuplicatedDevices),
            # strict_system_mac_address
            False,
            id="TWO_DUPED_SERIAL_STRICT_MAC_FALSE",
        ),
        pytest.param(
            TWO_DUPED_SERIAL_DEVICES,
            # Warnings
            0,
            [],
            # Logs
            0,
            [],
            # Exception
            TWO_DUPED_SERIAL_PATTERNS,
            pytest.raises(CVDuplicatedDevices),
            # strict_system_mac_address
            True,
            id="TWO_DUPED_SERIAL_STRICT_MAC_TRUE",
        ),
        pytest.param(
            TWO_DUPED_SYS_MAC_DEVICES,
            # Warnings
            0,
            [],
            # Logs
            0,
            [],
            # Exceptions
            [
                "\\('Duplicated devices found in inventory.*\\{"
                "'aa:bb:cc:dd:ee:f1': \\["
                "CVDevice\\(hostname='switch1'.*system_mac_address='aa:bb:cc:dd:ee:f1'.*"
                "CVDevice\\(hostname='switch2'.*system_mac_address='aa:bb:cc:dd:ee:f1'.*",
            ],
            pytest.raises(CVDuplicatedDevices),
            # strict_system_mac_address
            False,
            id="TWO_DUPED_SYS_MAC_STRICT_MAC_FALSE",
        ),
        pytest.param(
            TWO_DUPED_SYS_MAC_DEVICES,
            # Warnings
            0,
            [],
            # Logs
            0,
            [],
            # Exception
            [
                "\\('Duplicated devices found in inventory.*\\{"
                "'aa:bb:cc:dd:ee:f1': \\["
                "CVDevice\\(hostname='switch1'.*system_mac_address='aa:bb:cc:dd:ee:f1'.*"
                "CVDevice\\(hostname='switch2'.*system_mac_address='aa:bb:cc:dd:ee:f1'.*"
                "'aa:bb:cc:dd:ee:f3': \\["
                "CVDevice\\(hostname='switch3'.*system_mac_address='aa:bb:cc:dd:ee:f3'.*"
                "CVDevice\\(hostname='switch4'.*system_mac_address='aa:bb:cc:dd:ee:f3'.*",
            ],
            pytest.raises(CVDuplicatedDevices),
            # strict_system_mac_address
            True,
            id="TWO_DUPED_SYS_MAC_STRICT_MAC_TRUE",
        ),
        pytest.param(
            TWO_DUPED_SYS_MAC_UNIQ_SER_DEVICES,
            # Warnings
            1,
            [
                "\\('Duplicated devices found in inventory.*\\{"
                "'aa:bb:cc:dd:ee:f3': \\["
                "CVDevice\\(hostname='switch3'.*system_mac_address='aa:bb:cc:dd:ee:f3'.*"
                "CVDevice\\(hostname='switch4'.*system_mac_address='aa:bb:cc:dd:ee:f3'.*"
                "'aa:bb:cc:dd:ee:f5': \\["
                "CVDevice\\(hostname='switch5'.*system_mac_address='aa:bb:cc:dd:ee:f5'.*"
                "CVDevice\\(hostname='switch6'.*system_mac_address='aa:bb:cc:dd:ee:f5'.*",
            ],
            # Logs
            1,
            [
                "verify_inputs: Devices with duplicated system_mac_address and unique serial_number discovered in inventory \\(structured config\\): \\{"
                "'aa:bb:cc:dd:ee:f3': \\["
                "CVDevice\\(hostname='switch3'.*serial_number='serial3'.*system_mac_address='aa:bb:cc:dd:ee:f3'.*"
                "CVDevice\\(hostname='switch4'.*serial_number='serial4'.*system_mac_address='aa:bb:cc:dd:ee:f3'.*"
                "'aa:bb:cc:dd:ee:f5': \\["
                "CVDevice\\(hostname='switch5'.*serial_number='serial5'.*system_mac_address='aa:bb:cc:dd:ee:f5'.*"
                "CVDevice\\(hostname='switch6'.*serial_number='serial6'.*system_mac_address='aa:bb:cc:dd:ee:f5.*",
            ],
            # Exceptions
            [],
            does_not_raise(),
            # strict_system_mac_address
            False,
            id="TWO_DUPED_SYS_MAC_UNIQ_SER_STRICT_MAC_FALSE",
        ),
        pytest.param(
            TWO_DUPED_SYS_MAC_UNIQ_SER_DEVICES,
            # Warnings
            0,
            [],
            # Logs
            0,
            [],
            # Exceptions
            [
                "\\('Duplicated devices found in inventory.*\\{"
                "'aa:bb:cc:dd:ee:f3': \\["
                "CVDevice\\(hostname='switch3'.*system_mac_address='aa:bb:cc:dd:ee:f3'.*"
                "CVDevice\\(hostname='switch4'.*system_mac_address='aa:bb:cc:dd:ee:f3'.*"
                "'aa:bb:cc:dd:ee:f5': \\["
                "CVDevice\\(hostname='switch5'.*system_mac_address='aa:bb:cc:dd:ee:f5'.*"
                "CVDevice\\(hostname='switch6'.*system_mac_address='aa:bb:cc:dd:ee:f5'.*",
            ],
            pytest.raises(CVDuplicatedDevices),
            # strict_system_mac_address
            True,
            id="TWO_DUPED_SYS_MAC_UNIQ_SER_STRICT_MAC_TRUE",
        ),
        pytest.param(
            ONE_DUPED_SERIAL_ONE_DUPED_SYS_MAC_DEVICES,
            # Warnings
            0,
            [],
            # Logs
            0,
            [],
            # Exceptions
            [
                "\\('Duplicated devices found in inventory.*\\{"
                "'serial1':.*\\["
                "CVDevice\\(hostname='switch1'.*serial_number='serial1'.*"
                "CVDevice\\(hostname='switch2'.*serial_number='serial1'.*",
            ],
            pytest.raises(CVDuplicatedDevices),
            # strict_system_mac_address
            False,
            id="ONE_DUPED_SERIAL_ONE_DUPED_SYS_MAC_STRICT_MAC_FALSE",
        ),
        pytest.param(
            ONE_DUPED_SERIAL_ONE_DUPED_SYS_MAC_DEVICES,
            # Warnings
            0,
            [],
            # Logs
            0,
            [],
            # Exceptions
            [
                "\\('Duplicated devices found in inventory.*\\{"
                "'serial1':.*\\["
                "CVDevice\\(hostname='switch1'.*serial_number='serial1'.*"
                "CVDevice\\(hostname='switch2'.*serial_number='serial1'.*"
                "'aa:bb:cc:dd:ee:f3':.*\\["
                "CVDevice\\(hostname='switch3'.*system_mac_address='aa:bb:cc:dd:ee:f3'.*"
                "CVDevice\\(hostname='switch4'.*system_mac_address='aa:bb:cc:dd:ee:f3'.*",
            ],
            pytest.raises(CVDuplicatedDevices),
            # strict_system_mac_address
            True,
            id="ONE_DUPED_SERIAL_ONE_DUPED_SYS_MAC_STRICT_MAC_TRUE",
        ),
        pytest.param(
            ONE_DUPED_SERIAL_ONE_DUPED_SYS_MAC_SAME_DEVICES_DEVICES,
            # Warnings
            0,
            [],
            # Logs
            0,
            [],
            # Exception
            [
                "\\('Duplicated devices found in inventory.*\\{"
                "'serial1':.*\\["
                "CVDevice\\(hostname='switch1'.*serial_number='serial1'.*system_mac_address='aa:bb:cc:dd:ee:f1'.*"
                "CVDevice\\(hostname='switch2'.*serial_number='serial1'.*system_mac_address='aa:bb:cc:dd:ee:f1'.*",
            ],
            pytest.raises(CVDuplicatedDevices),
            # strict_system_mac_address
            False,
            id="ONE_DUPED_SERIAL_ONE_DUPED_SYS_MAC_SAME_DEVICES_STRICT_MAC_FALSE",
        ),
        pytest.param(
            ONE_DUPED_SERIAL_ONE_DUPED_SYS_MAC_SAME_DEVICES_DEVICES,
            # Warnings
            0,
            [],
            # Logs
            0,
            [],
            # Exception
            [
                "\\('Duplicated devices found in inventory.*\\{"
                "'serial1':.*\\["
                "CVDevice\\(hostname='switch1'.*serial_number='serial1'.*system_mac_address='aa:bb:cc:dd:ee:f1'.*"
                "CVDevice\\(hostname='switch2'.*serial_number='serial1'.*system_mac_address='aa:bb:cc:dd:ee:f1'.*"
                "'aa:bb:cc:dd:ee:f1':.*\\["
                "CVDevice\\(hostname='switch1'.*serial_number='serial1'.*system_mac_address='aa:bb:cc:dd:ee:f1'.*"
                "CVDevice\\(hostname='switch2'.*serial_number='serial1'.*system_mac_address='aa:bb:cc:dd:ee:f1'.*",
            ],
            pytest.raises(CVDuplicatedDevices),
            # strict_system_mac_address
            True,
            id="ONE_DUPED_SERIAL_ONE_DUPED_SYS_MAC_SAME_DEVICES_STRICT_MAC_TRUE",
        ),
    ],
)
def test_verify_device_inputs(
    caplog: pytest.LogCaptureFixture,
    devices: list[CVDevice],
    warnings_qty: int,
    expected_warning_patterns: list[str],
    logs_qty: int,
    expected_logs_patterns: list[str],
    expected_exception_patterns: list[str],
    expected_exception: RaisesContext | does_not_raise,
    *,
    strict_system_mac_address: bool,
) -> None:
    # Create an empty list for warnings
    warnings = []
    with caplog.at_level(logging.DEBUG), expected_exception as exc_info:
        # Engage FUT
        verify_device_inputs(devices, warnings, strict_system_mac_address=strict_system_mac_address)
    # Assert number of returned warnings
    assert len(warnings) == warnings_qty
    # Assert that updated warnings match expected warning patterns
    for expected_pattern in expected_warning_patterns:
        assert any(re.search(re.compile(expected_pattern), str(warning_item.args)) for warning_item in warnings)
    # Assert number of log messages
    assert len(caplog.records) == logs_qty
    # Assert that log messages match expected log patterns
    for expected_pattern in expected_logs_patterns:
        assert any(re.search(re.compile(expected_pattern), str(record.message)) for record in caplog.records)
    # If exception is raised, assert that exception value contains all expected exception patterns
    if exc_info and (exception_string := str(exc_info.value)):
        for expected_pattern in expected_exception_patterns:
            assert re.search(re.compile(expected_pattern), exception_string)


@pytest.mark.parametrize(
    (
        "devices",
        "expected_return",
        "target_function",
    ),
    [
        pytest.param(
            IDENTIFY_DUPLICATED_DEVICES_FULL_INVENTORY,
            IDENTIFY_DUPLICATED_DEVICES_FULL_INVENTORY_EXPECTED_RETURN,
            identify_duplicated_devices,
            id="IDENTIFY_DUPLICATED_DEVICES_FULL_INVENTORY_ORIGINAL_FUNCTION",
        )
    ],
)
@pytest.mark.usefixtures("generate_x_mock_cvdevices")
def test_identify_duplicated_devices(
    devices: list[CVDevice],
    expected_return: dict[str, list[CVDevice]],
    target_function: Callable,
    generate_x_mock_cvdevices: list[CVDevice],
) -> None:
    # Call tested function to fetch devices with overlapping serial_number or system_mac_address
    duplicated_devices = target_function(
        devices,
    )

    # Validate duplicated_devices.serial_number
    assert len(duplicated_devices.serial_number) == len(expected_return["duplicated_serial_number"])
    for serial_number, matching_cvdevices in duplicated_devices.serial_number.items():
        assert {device.hostname for device in matching_cvdevices} == {device.hostname for device in expected_return["duplicated_serial_number"][serial_number]}

    # Validate duplicated_devices.system_mac_address.unset_or_mixed_serial_number
    assert len(duplicated_devices.system_mac_address.unset_or_mixed_serial_number) == len(
        expected_return["duplicated_system_mac_address_unset_or_mixed_serial_number"]
    )
    for system_mac_address, matching_cvdevices in duplicated_devices.system_mac_address.unset_or_mixed_serial_number.items():
        assert {device.hostname for device in matching_cvdevices} == {
            device.hostname for device in expected_return["duplicated_system_mac_address_unset_or_mixed_serial_number"][system_mac_address]
        }

    # Validate duplicated_devices.system_mac_address.set_serial_number
    assert len(duplicated_devices.system_mac_address.set_serial_number) == len(expected_return["duplicated_system_mac_address_set_serial_number"])
    for system_mac_address, matching_cvdevices in duplicated_devices.system_mac_address.set_serial_number.items():
        assert {device.hostname for device in matching_cvdevices} == {
            device.hostname for device in expected_return["duplicated_system_mac_address_set_serial_number"][system_mac_address]
        }

    # Measure performance of each tested function based on the inventory of 1M mock CVDevices
    profiler = cProfile.Profile()
    profiler.enable()
    _ = target_function(
        generate_x_mock_cvdevices,
    )
    profiler.disable()
    profiler.print_stats()
