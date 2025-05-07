// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.

use ordermap::OrderMap;
use serde::{Deserialize, Serialize};
use serde_json::Value;
use serde_with::skip_serializing_none;

use super::{
    any::AnySchema,
    base::{Base, documentation_options::DocumentationOptionsDict},
};

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

#[cfg(test)]
mod tests {
    use crate::{any::AnySchema, boolean::Bool};

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
}
