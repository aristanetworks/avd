// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.

use ordermap::OrderMap;

use serde_json::Value;

use crate::dict::DynamicKeyInfo;
use crate::resolve::{errors::SchemaResolverError, resolve_ref::resolve_ref};
use crate::{Schema, Store, any::AnySchema, dict::Dict};

// Keys that are accepted by the schema from either keys or dynamic keys.
#[derive(Debug, PartialEq)]
pub enum SchemaKey {
    StaticKey,
    DynamicKey { dynamic_key_path: String },
}
impl SchemaKey {
    /// Return a schema $ref like
    /// "eos_cli_config_gen#/keys/somekey/items/" or
    /// "eos_designs#/dynamic_keys/connected_endpoint_keys.key"
    /// For dynamic keys the first item of the path is replaced with with dynamic key path.
    pub fn get_schema_ref_from_path(&self, schema: &Schema, data_path: &[String]) -> String {
        let schema_name: String = (*schema).into();
        let mut path = data_path.iter();
        let mut schema_ref = format!("{schema_name}#");
        match path.next() {
            Some(root_key) => match self {
                SchemaKey::DynamicKey { dynamic_key_path } => {
                    schema_ref.push_str(format!("/dynamic_keys/{dynamic_key_path}").as_str())
                }
                SchemaKey::StaticKey => schema_ref.push_str(format!("/keys/{root_key}").as_str()),
            },
            None => return schema_ref,
        }
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
}

#[derive(Debug, PartialEq)]
pub struct SchemaKeys {
    pub keys: OrderMap<String, SchemaKey>,
}
impl SchemaKeys {
    pub fn try_from_schema_with_value(
        schema: &AnySchema,
        value: &Value,
    ) -> Result<Self, SchemaKeysError> {
        let dict_schema: &Dict = schema
            .try_into()
            .map_err(|_err| SchemaKeysError::SchemaNotDict)?;
        let dict = value.as_object().ok_or(SchemaKeysError::ValueNotADict)?;
        let mut schema_keys = SchemaKeys {
            keys: OrderMap::from_iter(dict_schema.keys.as_ref().into_iter().flat_map(|keys| {
                keys.keys()
                    .map(|key| (key.to_owned(), SchemaKey::StaticKey))
            })),
        };

        schema_keys.keys.extend(
            dict_schema
                .get_dynamic_keys(dict)
                .unwrap_or_default()
                .into_iter()
                .map(|(key, dynamic_key_info)| {
                    (key.to_owned(), SchemaKey::from(&dynamic_key_info))
                }),
        );
        Ok(schema_keys)
    }
}
impl From<&DynamicKeyInfo<'_>> for SchemaKey {
    fn from(value: &DynamicKeyInfo) -> Self {
        Self::DynamicKey {
            dynamic_key_path: value.dynamic_key_path.to_owned(),
        }
    }
}

#[derive(Debug)]
pub enum SchemaKeysError {
    ValueNotADict,
    SchemaNotDict,
}

#[derive(Debug, derive_more::From)]
pub enum GetSchemaFromPathError {
    SchemaKeys(SchemaKeysError),
    SchemaResolve(SchemaResolverError),
}
/// Given a data path return the schema covering this.
/// Assumes that dynamic keys can only exist at the root level.
/// Assumes that the root level is a dict.
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
            match schema_keys.keys.get(root_key) {
                None => Ok(None),
                Some(schema_key) => {
                    let schema_ref = schema_key.get_schema_ref_from_path(&schema_id, data_path);
                    Ok(Some(resolve_ref(&schema_ref, store)?))
                }
            }
        }
    }
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
        assert_eq!(
            schema_keys.keys,
            OrderMap::from([
                ("outer".into(), SchemaKey::StaticKey),
                ("another_key".into(), SchemaKey::StaticKey),
                (
                    "one".into(),
                    SchemaKey::DynamicKey {
                        dynamic_key_path: "outer.inner".into()
                    }
                ),
                (
                    "two".into(),
                    SchemaKey::DynamicKey {
                        dynamic_key_path: "outer.inner".into()
                    }
                ),
                (
                    "three".into(),
                    SchemaKey::DynamicKey {
                        dynamic_key_path: "outer.inner".into()
                    }
                ),
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
        assert_eq!(schema, &store.eos_cli_config_gen);
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
