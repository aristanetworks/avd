// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.

use ordermap::OrderMap;

use serde_json::Value;

use crate::resolve::{errors::SchemaResolverError, resolve_ref::resolve_ref};
use crate::{Schema, Store, any::AnySchema, dict::Dict, get_dynamic_keys};

// Keys that are accepted by the schema from either keys or dynamic keys.
#[derive(Debug)]
struct SchemaKeys {
    keys: Vec<String>,
    key_to_dynamic_key_path: OrderMap<String, String>,
}
impl SchemaKeys {
    fn try_from_schema_with_value(
        schema: &AnySchema,
        value: &Value,
    ) -> Result<Self, SchemaKeysError> {
        let dict_schema: &Dict = schema
            .try_into()
            .map_err(|_err| SchemaKeysError::SchemaNotDict)?;
        let dict = value.as_object().ok_or(SchemaKeysError::ValueNotADict)?;
        Ok(SchemaKeys {
            keys: dict_schema
                .keys
                .as_ref()
                .map(|keys| Vec::from_iter(keys.keys().map(|key| key.to_owned())))
                .unwrap_or_default(),
            key_to_dynamic_key_path: dict_schema
                .dynamic_keys
                .as_ref()
                .map(|dynamic_keys| {
                    OrderMap::from_iter(dynamic_keys.keys().flat_map(|key_path| {
                        get_dynamic_keys(key_path, dict)
                            .iter()
                            .map(|dynamic_key| (dynamic_key.to_owned(), key_path.to_owned()))
                            .collect::<Vec<_>>()
                    }))
                })
                .unwrap_or_default(),
        })
    }
}

#[derive(Debug)]
pub enum SchemaKeysError {
    ValueNotADict,
    SchemaNotDict,
}

#[derive(Debug)]
pub enum GetSchemaFromPathError {
    SchemaKeys(SchemaKeysError),
    SchemaResolve(SchemaResolverError),
}
impl From<SchemaKeysError> for GetSchemaFromPathError {
    fn from(value: SchemaKeysError) -> Self {
        GetSchemaFromPathError::SchemaKeys(value)
    }
}
impl From<SchemaResolverError> for GetSchemaFromPathError {
    fn from(value: SchemaResolverError) -> Self {
        GetSchemaFromPathError::SchemaResolve(value)
    }
}
// Given a data path return the schema covering this.
// Assumes that dynamic keys can only exist at the root level.
// Assumes that the root level is a dict.
pub fn get_schema_from_path<'a>(
    schema_id: Schema,
    store: &'a Store,
    data_path: &'_ [String],
    data_value: &'_ Value,
) -> Result<Option<&'a AnySchema>, GetSchemaFromPathError> {
    let mut path = data_path.iter();
    let schema = store.get(schema_id);
    match path.next() {
        None => Ok(Some(schema)),
        Some(root_key) => {
            let schema_keys = SchemaKeys::try_from_schema_with_value(schema, data_value)?;
            if schema_keys.keys.contains(root_key) {
                // Regular key so we can just build a regular ref and get the schema.
                let schema_ref = get_schema_ref_from_path(&schema_id, data_path);
                Ok(Some(resolve_ref(&schema_ref, store)?))
            } else if let Some(dynamic_key_path) = schema_keys.key_to_dynamic_key_path.get(root_key)
            {
                // Dynamic key so we build a special ref and get the schema.
                let schema_ref = get_dynamic_key_schema_ref_from_path(
                    &schema_id,
                    dynamic_key_path,
                    path.as_slice(),
                );
                Ok(Some(resolve_ref(&schema_ref, store)?))
            } else {
                Ok(None)
            }
        }
    }
}

pub fn get_schema_ref_from_path(schema: &Schema, path: &[String]) -> String {
    let schema_name: String = (*schema).into();
    let mut schema_ref = format!("{schema_name}#");
    for step in path {
        if step.parse::<usize>().is_ok() {
            schema_ref.push_str("/items");
        } else {
            schema_ref.push_str("/keys/");
            schema_ref.push_str(step);
        }
    }
    schema_ref
}

pub fn get_dynamic_key_schema_ref_from_path(
    schema: &Schema,
    dynamic_key_path: &String,
    rest_of_path: &[String],
) -> String {
    let schema_name: String = (*schema).into();
    let mut schema_ref = format!("{schema_name}#/dynamic_keys/{dynamic_key_path}");
    for step in rest_of_path {
        if step.parse::<usize>().is_ok() {
            schema_ref.push_str("/items");
        } else {
            schema_ref.push_str("/keys/");
            schema_ref.push_str(step);
        }
    }
    schema_ref
}

#[cfg(test)]
mod tests {
    use crate::{int::Int, list::List, str::Str, utils::test_utils::get_test_store};

    use super::*;
    use ordermap::OrderMap;
    use serde_json::json;

    #[test]
    fn schema_keys_try_from_schema_with_value_ok() {
        let schema = AnySchema::Dict(Dict {
            keys: Some(OrderMap::from_iter([
                (
                    "outer".into(),
                    List {
                        items: Some(Box::new(
                            Dict {
                                keys: Some(OrderMap::from_iter([(
                                    "inner".into(),
                                    Str::default().into(),
                                )])),
                                ..Default::default()
                            }
                            .into(),
                        )),
                        ..Default::default()
                    }
                    .into(),
                ),
                (
                    "another_key".into(),
                    Str {
                        ..Default::default()
                    }
                    .into(),
                ),
            ])),
            dynamic_keys: Some(OrderMap::from_iter([(
                "outer.inner".into(),
                Int {
                    max: Some(10),
                    ..Default::default()
                }
                .into(),
            )])),
            allow_other_keys: Some(true),
            ..Default::default()
        });
        let value = json!({"outer": [ {"inner": "one"}, {"inner": "two"}, {"inner": "three"}]});
        let result = SchemaKeys::try_from_schema_with_value(&schema, &value);
        assert!(result.is_ok());
        let schema_keys = result.unwrap();
        assert_eq!(schema_keys.keys, vec!["outer", "another_key"]);
        assert_eq!(
            schema_keys.key_to_dynamic_key_path,
            OrderMap::<String, String>::from_iter(vec![
                ("one".into(), "outer.inner".into()),
                ("two".into(), "outer.inner".into()),
                ("three".into(), "outer.inner".into()),
            ])
        );
    }

    #[test]
    fn schema_keys_try_from_schema_with_value_wrong_schema_err() {
        let schema = AnySchema::Str(Str {
            ..Default::default()
        });
        let value = json!({});
        let result = SchemaKeys::try_from_schema_with_value(&schema, &value);
        assert!(result.is_err());
        let err = result.unwrap_err();
        assert!(matches!(err, SchemaKeysError::SchemaNotDict));
    }
    #[test]
    fn schema_keys_try_from_schema_with_value_wrong_value_err() {
        let schema = AnySchema::Dict(Dict {
            ..Default::default()
        });
        let value = json!([]);
        let result = SchemaKeys::try_from_schema_with_value(&schema, &value);
        assert!(result.is_err());
        let err = result.unwrap_err();
        assert!(matches!(err, SchemaKeysError::ValueNotADict));
    }

    #[test]
    fn get_schema_from_path_empty_path_some_ok() {
        let value = json!(
            {"dynamic": [ {"key": "one"}, {"key": "two"}, {"key": "three"}]});
        let store = get_test_store();
        let result = get_schema_from_path(Schema::EosCliConfigGen, &store, &[], &value);
        assert!(result.is_ok());
        let opt = result.unwrap();
        assert!(opt.is_some());
        let schema = opt.unwrap();
        assert_eq!(schema, &store.eos_designs);
    }

    #[test]
    fn get_schema_from_path_regular_key_some_ok() {
        let value = json!(
            {"dynamic": [ {"key": "one"}, {"key": "two"}, {"key": "three"}]});
        let store = get_test_store();
        let result =
            get_schema_from_path(Schema::EosCliConfigGen, &store, &["key2".into()], &value);
        assert!(result.is_ok());
        let opt = result.unwrap();
        assert!(opt.is_some());
        let schema = opt.unwrap();
        let expected_schema: AnySchema = serde_json::from_value(json!({
            "type": "str",
            "description": "this is from key2",
        }))
        .unwrap();
        assert_eq!(schema, &expected_schema);
    }

    #[test]
    fn get_schema_from_path_dynamic_key_some_ok() {
        let value = json!(
            {"dynamic": [ {"key": "one"}, {"key": "two"}, {"key": "three"}]});
        let store = get_test_store();
        let result = get_schema_from_path(Schema::EosCliConfigGen, &store, &["two".into()], &value);
        assert!(result.is_ok());
        let opt = result.unwrap();
        assert!(opt.is_some());
        let schema = opt.unwrap();
        let expected_schema: AnySchema = serde_json::from_value(json!({
            "type": "int",
            "max": 10,
        }))
        .unwrap();
        assert_eq!(schema, &expected_schema);
    }
}
