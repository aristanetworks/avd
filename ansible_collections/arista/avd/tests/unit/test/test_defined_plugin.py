from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible_collections.arista.avd.plugins.test.defined import defined, TestModule
from jinja2.runtime import Undefined
from ansible.errors import AnsibleError
import pytest

VALUE_LIST = ['ab', None, 1, True, {"key": "value"}]
TEST_VALUE_LIST = [None, 'ab', True, 1, True]
FAIL_ACTION_LIST = ['warning', 'error']
VAR_NAME_LIST = ['ab', None, 1]
VAR_TYPE_LIST = ['int', 'str', 'integer', 'aaa', None, dict]
INVALID_FAIL_ACTION_LIST = [None, 'aaaa']

f = TestModule()


class TestDefinedPlugin():

    def defined_function(self, value, test_value=None, var_type=None, fail_action=None, var_name=None, err_msg=None, warn_msg=None):
        if str(fail_action).lower() == 'warning':
            resp, warning = defined(value, test_value=test_value, var_type=var_type, fail_action=fail_action,
                                    var_name=var_name, run_tests=True)
            if warn_msg:
                assert warning is not None
                warn = str(list(warning.keys())[0]).replace(
                    '[WARNING]: ', '').strip().replace('\n', ' ')
                assert warn == warn_msg
                assert resp is False
        elif str(fail_action).lower() == 'error':
            with pytest.raises(AnsibleError) as e:
                resp, warning = defined(value, test_value=test_value, var_type=var_type, fail_action=fail_action,
                                        var_name=var_name, run_tests=True)
            assert str(e.value) == err_msg

    @pytest.mark.parametrize("VALUE", VALUE_LIST)
    @pytest.mark.parametrize("FAIL_ACTION", FAIL_ACTION_LIST)
    @pytest.mark.parametrize("VAR_NAME", VAR_NAME_LIST)
    def test_defined_plugin_value_undefined_or_none(self, VALUE, FAIL_ACTION, VAR_NAME):
        if isinstance(VALUE, Undefined) or VALUE is None:
            if str(FAIL_ACTION).lower() == 'warning':
                if VAR_NAME is not None:
                    warn_msg = f"{VAR_NAME} was expected but not set. Output may be incorrect or incomplete!"
                else:
                    warn_msg = "A variable was expected but not set. Output may be incorrect or incomplete!"

                self.defined_function(
                    VALUE, fail_action=FAIL_ACTION, var_name=VAR_NAME, warn_msg=warn_msg)
            elif str(FAIL_ACTION).lower() == 'error':
                if VAR_NAME is not None:
                    err_msg = f"{VAR_NAME} was expected but not set!"
                else:
                    err_msg = "A variable was expected but not set!"

                self.defined_function(
                    VALUE, fail_action=FAIL_ACTION, var_name=VAR_NAME, err_msg=err_msg)

    @pytest.mark.parametrize("VALUE", VALUE_LIST)
    def test_defined_plugin_value_not_none_and_define(self, VALUE):
        if not isinstance(VALUE, Undefined) and VALUE is not None:
            resp = defined(VALUE)
            assert resp is True

    @pytest.mark.parametrize("VALUE", VALUE_LIST)
    @pytest.mark.parametrize("FAIL_ACTION", FAIL_ACTION_LIST)
    @pytest.mark.parametrize("VAR_NAME", VAR_NAME_LIST)
    @pytest.mark.parametrize("TEST_VALUE", TEST_VALUE_LIST)
    def test_defined_plugin_test_value_not_none(self, VALUE, FAIL_ACTION, VAR_NAME, TEST_VALUE):
        if (not isinstance(VALUE, Undefined) and VALUE is not None) and TEST_VALUE is not None and VALUE != TEST_VALUE:
            if str(FAIL_ACTION).lower() == 'warning':
                if VAR_NAME is not None:
                    warn_msg = f"{VAR_NAME} was set to {VALUE} but we expected {TEST_VALUE}. Output may be incorrect or incomplete!"
                else:
                    warn_msg = f"A variable was set to {VALUE} but we expected {TEST_VALUE}. Output may be incorrect or incomplete!"
                self.defined_function(VALUE, fail_action=FAIL_ACTION,
                                      var_name=VAR_NAME, test_value=TEST_VALUE, warn_msg=warn_msg)
            elif str(FAIL_ACTION).lower() == 'error':
                if VAR_NAME is not None:
                    err_msg = f"{VAR_NAME} was set to {VALUE} but we expected {TEST_VALUE}!"
                else:
                    err_msg = f"A variable was set to {VALUE} but we expected {TEST_VALUE}!"
                self.defined_function(VALUE, fail_action=FAIL_ACTION,
                                      var_name=VAR_NAME, test_value=TEST_VALUE, err_msg=err_msg)

    @pytest.mark.parametrize("VALUE", VALUE_LIST)
    @pytest.mark.parametrize("FAIL_ACTION", FAIL_ACTION_LIST)
    @pytest.mark.parametrize("VAR_NAME", VAR_NAME_LIST)
    @pytest.mark.parametrize("VAR_TYPE", VAR_TYPE_LIST)
    def test_defined_plugin_var_type(self, VALUE, FAIL_ACTION, VAR_NAME, VAR_TYPE):
        type_list = ['float', 'int', 'str', 'list', 'dict', 'tuple', 'bool']
        if not isinstance(VALUE, Undefined) and VALUE is not None:
            if str(VAR_TYPE).lower() in type_list and str(VAR_TYPE).lower() != type(VALUE).__name__:
                if str(FAIL_ACTION).lower() == 'warning':
                    if VAR_NAME is not None:
                        warn_msg = f"{VAR_NAME} was a {type(VALUE).__name__} but we expected a {str(VAR_TYPE).lower()}. Output may be incorrect or incomplete!"
                    else:
                        warn_msg = f"A variable was a {type(VALUE).__name__} but we expected a {str(VAR_TYPE).lower()}. Output may be incorrect or incomplete!"
                    self.defined_function(
                        VALUE, fail_action=FAIL_ACTION, var_name=VAR_NAME, var_type=VAR_TYPE, warn_msg=warn_msg)
                elif str(FAIL_ACTION).lower() == 'error':
                    if VAR_NAME is not None:
                        err_msg = f"{VAR_NAME} was a {type(VALUE).__name__} but we expected a {str(VAR_TYPE).lower()}!"
                    else:
                        err_msg = f"A variable was a {type(VALUE).__name__} but we expected a {str(VAR_TYPE).lower()}!"
                    self.defined_function(
                        VALUE, fail_action=FAIL_ACTION, var_name=VAR_NAME, var_type=VAR_TYPE, err_msg=err_msg)

    @pytest.mark.parametrize("VALUE", VALUE_LIST)
    @pytest.mark.parametrize("TEST_VALUE", TEST_VALUE_LIST)
    @pytest.mark.parametrize("INVALID_FAIL_ACTION", INVALID_FAIL_ACTION_LIST)
    def test_defined_plugin_fail_action_None(self, VALUE, TEST_VALUE, INVALID_FAIL_ACTION):
        resp = defined(VALUE, test_value=TEST_VALUE, fail_action=INVALID_FAIL_ACTION)
        if not isinstance(VALUE, Undefined) and VALUE is not None:
            if TEST_VALUE is not None and VALUE != TEST_VALUE:
                assert resp is False
            else:
                assert resp is True
        else:
            assert resp is False

    @pytest.mark.parametrize("VALUE", VALUE_LIST)
    @pytest.mark.parametrize("VAR_TYPE", VAR_TYPE_LIST)
    def test_defined_plugin_var_type_fail_action_None(self, VALUE, VAR_TYPE):
        type_list = ['float', 'int', 'str', 'list', 'dict', 'tuple', 'bool']
        if not isinstance(VALUE, Undefined) and VALUE is not None:
            resp = defined(VALUE, var_type=VAR_TYPE)
            if str(VAR_TYPE).lower() in type_list and type(VALUE).__name__ != str(VAR_TYPE).lower():
                assert resp is False
            else:
                assert resp is True
