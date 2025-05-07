// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.

use serde_json::{Map, Value};

use super::walker::Walker;

pub fn get_dynamic_keys(key_path: &str, dict: &Map<String, Value>) -> Vec<String> {
    let mut path = key_path.split('.');
    path.next()
        .and_then(|component| dict.get_key_value(component))
        .map(|(key, value)| value.walk(path, Some(&mut vec![key.to_string()])))
        .into_iter()
        .flatten()
        .flat_map(|(_, value)| match value {
            Value::String(string) => vec![string.to_owned()],
            Value::Array(array) => array
                .iter()
                .filter_map(|item| item.as_str().map(|str| str.to_string()))
                .collect(),
            _ => {
                // Ignore an incorrect type targeted by the key_path.
                // The validation will report this during validation of that model.
                vec![]
            }
        })
        .collect::<Vec<_>>()
}

#[cfg(test)]
mod tests {
    use super::*;
    use serde_json::{Value, json};

    #[test]
    fn get_dynamic_keys_list_of_dicts() {
        let value: Value =
            json!({"outer": [ {"inner": "one"}, {"inner": "two"}, {"inner": "three"}]});
        let dict = value.as_object().unwrap();
        let result = get_dynamic_keys("outer.inner", dict);
        assert_eq!(result, vec!["one", "two", "three"]);
    }
    #[test]
    fn get_dynamic_keys_list_of_strings() {
        let value: Value = json!({"list": ["one", "two", "three"]});
        let dict = value.as_object().unwrap();
        let result = get_dynamic_keys("list", dict);
        assert_eq!(result, vec!["one", "two", "three"]);
    }
}
