// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.

use std::collections::HashMap;

use serde_json::Value;

use crate::resolve::resolve_ref::resolve_ref;
use crate::{Schema, Store, any::AnySchema, dict::Dict, get_dynamic_keys};

// Keys that are accepted by the schema from either keys or dynamic keys.
struct SchemaKeys {
    keys: Vec<String>,
    key_to_dynamic_key_path: HashMap<String, String>,
}
impl SchemaKeys {
    fn try_from_schema_with_value(schema: &AnySchema, value: &Value) -> Result<Self, &'static str> {
        let dict_schema: &Dict = schema.try_into()?;
        let dict = value
            .as_object()
            .ok_or("The given value is not a dictionary")?;
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
                    HashMap::from_iter(dynamic_keys.keys().flat_map(|key_path| {
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

// Given a data path return the schema covering this.
// Assumes that dynamic keys can only exist at the root level.
// Assumes that the root level is a dict.
pub fn get_schema_from_path<'a>(
    schema_id: Schema,
    store: &'a Store,
    data_path: &'_ [String],
    data_value: &'_ Value,
) -> Option<&'a AnySchema> {
    let mut path = data_path.iter();
    let schema = store.get(schema_id);
    match path.next() {
        None => Some(schema),
        Some(root_key) => {
            SchemaKeys::try_from_schema_with_value(schema, data_value)
                .ok()
                .and_then(|schema_keys| {
                    if schema_keys.keys.contains(root_key) {
                        // Regular key so we can just build a regular ref and get the schema.
                        let schema_ref = get_schema_ref_from_path(&schema_id, data_path);
                        resolve_ref(&schema_ref, store).ok()
                    } else if let Some(dynamic_key_path) =
                        schema_keys.key_to_dynamic_key_path.get(root_key)
                    {
                        // Dynamic key so we build a special ref and get the schema.
                        let schema_ref = get_dynamic_key_schema_ref_from_path(
                            &schema_id,
                            dynamic_key_path,
                            path.as_slice(),
                        );
                        resolve_ref(&schema_ref, store).ok()
                    } else {
                        None
                    }
                })
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
