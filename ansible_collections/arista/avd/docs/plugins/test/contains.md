# arista.avd.contains

Test if a list contains one or more of the supplied values\.

## Synopsis

The arista\.avd\.contains test will test if the passed list contains one or more of the supplied test\_values\.

The test accepts either a single test\_value or a list of test\_values\.

## Parameters

  _input (True, list, None)
    List of items to test\.

  test_value (optional, any, None)
    Single item or list of items to test for in value\.

## Examples

```yaml
vars:
  mylist: ["test", "test2"]
  item_is_in_my_list: "{{ mylist is arista.avd.contains("test") }}"
  any_item_is_in_my_list: "{{ mylist is arista.avd.contains(["test2", "test3"]) }}"
  platform_settings: {{ platform_settings | selectattr("platforms", "arista.avd.contains", switch_platform) }}
```

## Return Values

  _value (, boolean, )
    Returns <code>False</code> if either the passed value or the test\_values are <code>Undefined</code> or <code>none</code>\.
    Returns <code>True</code> if the passed list contains one or more of the supplied test\_values\. <code>False</code> otherwise\.

## Status

## Authors

- Arista Ansible Team (@aristanetworks)
