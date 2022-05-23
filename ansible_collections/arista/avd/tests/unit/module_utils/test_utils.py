from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible_collections.arista.avd.plugins.module_utils.utils import get, AristaAvdError
from contextlib import contextmanager
import pytest
import logging
import re


@contextmanager
def does_not_raise():
    yield


GET_DATA = [
    {  # normal case
        "dictionary": {"avd_switch_facts": {"host1": {"id": 42}}},
        "key": "avd_switch_facts.host1.id",
        "default": None,
        "required": False,
        "org_key": None,
        "separator": ".",
        "expected_result": 42,
        "expected_exception": does_not_raise()
    },
    {  # not required and no default - return None
        "dictionary": {"avd_switch_facts": {"host1": {"id": 42}}},
        "key": "avd_switch_facts.host1.missing",
        "default": None,
        "required": False,
        "org_key": None,
        "separator": ".",
        "expected_result": None,
        "expected_exception": does_not_raise()
    },
    {  # default value
        "dictionary": {"avd_switch_facts": {"host1": {"id": 42}}},
        "key": "avd_switch_facts.host1.missing_default",
        "default": 666,
        "required": False,
        "org_key": None,
        "separator": ".",
        "expected_result": 666,
        "expected_exception": does_not_raise()
    },
    {  # default value - present
        "dictionary": {"avd_switch_facts": {"host1": {"id": 42, "present_default": 1000}}},
        "key": "avd_switch_facts.host1.present_default",
        "default": 666,
        "required": False,
        "org_key": None,
        "separator": ".",
        "expected_result": 1000,
        "expected_exception": does_not_raise()
    },
    {  # required - missing
        "dictionary": {"avd_switch_facts": {"host1": {"id": 42}}},
        "key": "avd_switch_facts.host1.missing_required",
        "default": None,
        "required": True,
        "org_key": None,
        "separator": ".",
        "expected_result": None,
        "expected_exception": pytest.raises(AristaAvdError, match="avd_switch_facts.host1.missing_required")
    },
    {  # custom separator - hostname with a "."
        "dictionary": {"avd_switch_facts": {"host1.test": {"id": 42}}},
        "key": "avd_switch_facts..host1.test..id",
        "default": None,
        "required": False,
        "org_key": None,
        "separator": "..",
        "expected_result": 42,
        "expected_exception": does_not_raise()
    },
    {  # org_key as exception message
        "dictionary": {"avd_switch_facts": {"host1.test": {"id": 42}}},
        "key": "avd_switch_facts..host1.test..missing_required",
        "default": None,
        "required": True,
        "org_key": "avd_switch_facts.(host1.test).missing_required",
        "separator": "..",
        "expected_result": None,
        "expected_exception": pytest.raises(AristaAvdError, match=re.escape("avd_switch_facts.(host1.test).missing_required"))
    },
]


class TestUtils():

    @pytest.mark.parametrize("DATA", GET_DATA)
    def test_get(self, DATA):
        with DATA["expected_exception"]:
            res = get(DATA["dictionary"],
                      DATA["key"],
                      DATA["default"],
                      DATA["required"],
                      DATA["org_key"],
                      DATA["separator"])
            assert res == DATA["expected_result"]
