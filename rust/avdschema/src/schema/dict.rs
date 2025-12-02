// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.

use std::sync::OnceLock;

use ordermap::OrderMap;
use serde::{Deserialize, Serialize};
use serde_json::{Map, Value};
use serde_with::skip_serializing_none;

use crate::{Walker as _, any::Shortcuts, base::Deprecation};

use super::{
    any::AnySchema,
    base::{Base, documentation_options::DocumentationOptionsDict},
};

type DefaultDynamicKeys = Option<Box<OrderMap<String, Vec<String>>>>;

/// AVD Schema for dictionary data.
#[skip_serializing_none]
#[derive(Debug, Clone, Default, PartialEq, Serialize, Deserialize)]
#[serde(deny_unknown_fields)]
pub struct Dict {
    /// Dictionary of dictionary-keys in the format `{<keyname>: {<schema>}}`.
    /// `keyname` must use snake_case.
    /// `schema` is the schema for each key. This is a recursive schema, so the value must conform to AVD Schema
    pub keys: Option<OrderMap<String, AnySchema>>,
    /// Dictionary of dynamic dictionary-keys in the format `{<variable.path>: {<schema>}}`.
    /// `variable.path` is a variable path using dot-notation and pointing to a variable under the parent dictionary containing dictionary-keys.
    /// If an element of the variable path is a list, every list item will unpacked.
    /// `schema` is the schema for each key. This is a recursive schema, so the value must conform to AVD Schema
    /// Note that this is building the schema from values in the _data_ being validated!
    pub dynamic_keys: Option<OrderMap<String, AnySchema>>,
    pub allow_other_keys: Option<bool>,
    pub relaxed_validation: Option<bool>,
    #[serde(rename = "$id")]
    pub schema_id: Option<String>,
    #[serde(rename = "$schema")]
    pub schema_schema: Option<String>,
    #[serde(rename = "$defs")]
    pub schema_defs: Option<OrderMap<String, AnySchema>>,
    #[serde(flatten)]
    pub base: Base<OrderMap<String, Value>>,
    pub documentation_options: Option<DocumentationOptionsDict>,
    #[serde(skip)]
    pub default_dynamic_keys: OnceLock<DefaultDynamicKeys>,
}
impl<'a> Dict {
    /// Get map of dynamic keys and their corresponding schema.
    /// Reads the dynamic_keys definition in the schema, resolves the pointers in the given inputs (or use the default values for the schema).
    pub fn get_dynamic_keys(
        &'a self,
        dict: &Map<String, Value>,
    ) -> Option<OrderMap<String, DynamicKeyInfo<'a>>> {
        self.dynamic_keys.as_ref().map(|dynamic_keys| {
            let default_dynamic_keys = self
                .default_dynamic_keys
                .get_or_init(|| self.init_default_dynamic_keys())
                .as_ref();
            dynamic_keys
                .iter()
                .filter(|(_, dynamic_key_schema)| {
                    dynamic_key_schema
                        .deprecation()
                        .as_ref()
                        .and_then(|deprecation| {
                            deprecation.removed.unwrap_or_default().then_some(())
                        })
                        .is_none()
                })
                .flat_map(|(dynamic_key_path, _)| {
                    Dict::get_all(dynamic_key_path, dict)
                        .or_else(|| {
                            default_dynamic_keys.and_then(|default_dynamic_keys| {
                                default_dynamic_keys.get(dynamic_key_path).cloned()
                            })
                        })
                        .map(|keys| {
                            keys.into_iter().map(|key| {
                                (
                                    key.clone(),
                                    DynamicKeyInfo {
                                        dynamic_key_path: dynamic_key_path.clone(),
                                        schema: dynamic_keys.get(dynamic_key_path).unwrap(),
                                    },
                                )
                            })
                        })
                        .into_iter()
                        .flatten()
                })
                .collect()
        })
    }

    pub(self) fn init_default_dynamic_keys(&self) -> DefaultDynamicKeys {
        self.dynamic_keys.as_ref().map(|dynamic_keys| {
            dynamic_keys
                .iter()
                .filter(|(_, dynamic_key_schema)| {
                    dynamic_key_schema
                        .deprecation()
                        .as_ref()
                        .and_then(|deprecation| {
                            deprecation.removed.unwrap_or_default().then_some(())
                        })
                        .is_none()
                })
                .flat_map(|(dynamic_key_path, _)| {
                    dynamic_key_path
                        .split('.')
                        .next()
                        .and_then(|root_key| {
                            Some(self.get_default_for_key(root_key).map(|default_value| {
                                let default_as_input_map =
                                    Map::from_iter([(root_key.to_string(), default_value)]);
                                Dict::get_all(dynamic_key_path, &default_as_input_map).map(
                                    |default_dynamic_keys| {
                                        (dynamic_key_path.clone(), default_dynamic_keys)
                                    },
                                )
                            }))
                            .flatten()
                        })
                        .flatten()
                        .into_iter()
                })
                .collect::<OrderMap<String, Vec<String>>>()
                .into()
        })
    }

    pub(self) fn get_default_for_key(&self, key: &str) -> Option<Value> {
        self.keys.as_ref().and_then(|keys| {
            keys.get(key).and_then(|key_schema| match key_schema {
                crate::any::AnySchema::Bool(inner_schema) => inner_schema
                    .base
                    .default
                    .as_ref()
                    .map(|value| Value::Bool(*value)),
                crate::any::AnySchema::Int(inner_schema) => inner_schema
                    .base
                    .default
                    .as_ref()
                    .map(|value| Value::Number((*value).into())),
                crate::any::AnySchema::Str(inner_schema) => inner_schema
                    .base
                    .default
                    .as_ref()
                    .map(|value| Value::String(value.clone())),
                crate::any::AnySchema::List(inner_schema) => inner_schema
                    .base
                    .default
                    .as_ref()
                    .map(|value| Value::Array(value.clone())),
                crate::any::AnySchema::Dict(inner_schema) => inner_schema
                    .base
                    .default
                    .as_ref()
                    .map(|value| Value::Object(Map::from_iter(value.clone()))),
            })
        })
    }

    // Get all string values from the given key_path. Non-string values are ignored.
    // Returns None if the first key was missing. That will tell us if we need to look at the default value instead.
    pub(self) fn get_all(key_path: &str, dict: &Map<String, Value>) -> Option<Vec<String>> {
        let mut path = key_path.split('.');
        path.next()
            .and_then(|root_key| dict.get_key_value(root_key))
            .map(|(key, value)| {
                Some(value.walk(path, Some(&mut vec![key.to_string()])))
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
            })
    }
}

impl Shortcuts for Dict {
    fn is_required(&self) -> bool {
        self.base.required.unwrap_or_default()
    }

    fn deprecation(&self) -> &Option<Deprecation> {
        &self.base.deprecation
    }
}
impl<'x> TryFrom<&'x AnySchema> for &'x Dict {
    type Error = &'static str;

    fn try_from(value: &'x AnySchema) -> Result<Self, Self::Error> {
        match value {
            AnySchema::Dict(dict) => Ok(dict),
            _ => Err("Unable to convert from AnySchema to Dict. Invalid Schema type."),
        }
    }
}

#[derive(Debug, PartialEq)]
pub struct DynamicKeyInfo<'a> {
    /// The dynamic key path defined in the schema that led to this dynamic key.
    pub dynamic_key_path: String,
    /// The schema for this dynamic key.
    pub schema: &'a AnySchema,
}

#[cfg(test)]
mod tests {
    use ordermap::OrderMap;
    use serde_json::{Value, json};

    use crate::{
        any::AnySchema, boolean::Bool, dict::DynamicKeyInfo,
        utils::test_utils::get_test_dict_schema,
    };

    use super::Dict;

    #[test]
    fn try_from_anyschema_ok() {
        let anyschema = &AnySchema::Dict(Dict::default());
        let result: Result<&Dict, _> = anyschema.try_into();
        assert!(result.is_ok());
    }
    #[test]
    fn try_from_anyschema_err() {
        let anyschema = &AnySchema::Bool(Bool::default());
        let result: Result<&Dict, _> = anyschema.try_into();
        assert!(result.is_err());
    }

    #[test]
    fn get_dynamic_keys_list_of_dicts() {
        let dynamic_key_schema: AnySchema = Bool::default().into();
        let dict_schema = Dict {
            dynamic_keys: Some(OrderMap::from_iter([(
                "outer.inner".to_string(),
                dynamic_key_schema.clone(),
            )])),
            ..Default::default()
        };
        let value: Value =
            json!({"outer": [ {"inner": "one"}, {"inner": "two"}, {"inner": "three"}]});
        let dict = value.as_object().unwrap();
        let result = dict_schema.get_dynamic_keys(dict);
        assert_eq!(
            result,
            Some(OrderMap::from_iter([
                (
                    "one".to_string(),
                    DynamicKeyInfo {
                        dynamic_key_path: "outer.inner".to_string(),
                        schema: &dynamic_key_schema,
                    }
                ),
                (
                    "two".to_string(),
                    DynamicKeyInfo {
                        dynamic_key_path: "outer.inner".to_string(),
                        schema: &dynamic_key_schema,
                    }
                ),
                (
                    "three".to_string(),
                    DynamicKeyInfo {
                        dynamic_key_path: "outer.inner".to_string(),
                        schema: &dynamic_key_schema,
                    }
                ),
            ]))
        );
    }
    #[test]
    fn get_dynamic_keys_list_of_strings() {
        let dynamic_key_schema: AnySchema = Bool::default().into();
        let dict_schema = Dict {
            dynamic_keys: Some(OrderMap::from_iter([(
                "list".to_string(),
                dynamic_key_schema.clone(),
            )])),
            ..Default::default()
        };
        let value: Value = json!({"list": ["one", "two", "three"]});
        let dict = value.as_object().unwrap();
        let result = dict_schema.get_dynamic_keys(dict);
        assert_eq!(
            result,
            Some(OrderMap::from_iter([
                (
                    "one".to_string(),
                    DynamicKeyInfo {
                        dynamic_key_path: "list".to_string(),
                        schema: &dynamic_key_schema,
                    }
                ),
                (
                    "two".to_string(),
                    DynamicKeyInfo {
                        dynamic_key_path: "list".to_string(),
                        schema: &dynamic_key_schema,
                    }
                ),
                (
                    "three".to_string(),
                    DynamicKeyInfo {
                        dynamic_key_path: "list".to_string(),
                        schema: &dynamic_key_schema,
                    }
                ),
            ]))
        );
    }
    #[test]
    fn get_dynamic_keys_from_schema_with_default_and_override() {
        let test_dict_schema = get_test_dict_schema();
        let dict_schema: &Dict = (&test_dict_schema).try_into().unwrap();
        let dynamic_key_schema = dict_schema
            .dynamic_keys
            .as_ref()
            .unwrap()
            .get("outer.inner")
            .unwrap();
        let value: Value = json!({"outer": [{"inner": "one"}, {"inner": "two"}]});
        let dict = value.as_object().unwrap();
        let result = dict_schema.get_dynamic_keys(dict);
        assert_eq!(
            result,
            Some(OrderMap::from_iter([
                (
                    "one".to_string(),
                    DynamicKeyInfo {
                        dynamic_key_path: "outer.inner".to_string(),
                        schema: dynamic_key_schema,
                    }
                ),
                (
                    "two".to_string(),
                    DynamicKeyInfo {
                        dynamic_key_path: "outer.inner".to_string(),
                        schema: dynamic_key_schema,
                    }
                ),
            ]))
        );
    }

    #[test]
    fn get_dynamic_keys_from_schema_with_default_only() {
        let test_dict_schema = get_test_dict_schema();
        let dict_schema: &Dict = (&test_dict_schema).try_into().unwrap();
        let dynamic_key_schema = dict_schema
            .dynamic_keys
            .as_ref()
            .unwrap()
            .get("outer.inner")
            .unwrap();
        let value: Value = json!({"bool_key": true});
        let dict = value.as_object().unwrap();
        let result = dict_schema.get_dynamic_keys(dict);
        assert_eq!(
            result,
            Some(OrderMap::from_iter([(
                "dyn_key1_int".to_string(),
                DynamicKeyInfo {
                    dynamic_key_path: "outer.inner".to_string(),
                    schema: dynamic_key_schema,
                }
            ),]))
        );
    }

    #[test]
    fn get_all_some() {
        let value: Value = json!({"outer": [{"inner": "one"}, {"inner": "two"}]});
        let dict = value.as_object().unwrap();
        let result = Dict::get_all("outer.inner", dict);
        assert_eq!(result, Some(vec!["one".to_string(), "two".to_string()]));
    }

    #[test]
    fn get_all_none() {
        let value: Value = json!({"outer": [{"inner": "one"}, {"inner": "two"}]});
        let dict = value.as_object().unwrap();
        let result = Dict::get_all("non_existing.inner", dict);
        assert!(result.is_none());
    }

    #[test]
    fn get_default_for_key_some() {
        let test_dict_schema = get_test_dict_schema();
        let dict_schema: &Dict = (&test_dict_schema).try_into().unwrap();
        let result = dict_schema.get_default_for_key("outer");
        assert_eq!(result, Some(json!([{"inner": "dyn_key1_int"}])))
    }

    #[test]
    fn get_default_for_key_none() {
        let test_dict_schema = get_test_dict_schema();
        let dict_schema: &Dict = (&test_dict_schema).try_into().unwrap();
        let result = dict_schema.get_default_for_key("str_key");
        assert!(result.is_none())
    }

    #[test]
    fn init_default_dynamic_keys_some() {
        let test_dict_schema = get_test_dict_schema();
        let dict_schema: &Dict = (&test_dict_schema).try_into().unwrap();
        let expected_result: OrderMap<String, Vec<String>> =
            OrderMap::from_iter([("outer.inner".to_string(), vec!["dyn_key1_int".to_string()])]);
        let result = dict_schema.init_default_dynamic_keys();
        assert!(result.is_some());
        let unboxed_result = result.unwrap().as_ref().clone();
        assert_eq!(unboxed_result, expected_result);
    }

    #[test]
    fn init_default_dynamic_keys_none() {
        let dict_schema = Dict::default();
        let result = dict_schema.init_default_dynamic_keys();
        assert!(result.is_none());
    }
}
