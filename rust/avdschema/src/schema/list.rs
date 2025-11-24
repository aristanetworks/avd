// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.

use serde::{Deserialize, Serialize};
use serde_json::Value;
use serde_with::skip_serializing_none;

use crate::{any::Shortcuts, base::Deprecation, schema::base::Base};

use super::{any::AnySchema, base::documentation_options::DocumentationOptions};

/// AVD Schema for list data.
#[skip_serializing_none]
#[derive(Debug, Clone, Default, PartialEq, Serialize, Deserialize)]
#[serde(deny_unknown_fields)]
pub struct List {
    /// Schema for list items
    pub items: Option<Box<AnySchema>>,
    pub min_length: Option<u64>,
    pub max_length: Option<u64>,
    /// Name of a primary key in a list of dictionaries.
    /// The configured key is implicitly required and must have unique values between the list elements
    pub primary_key: Option<String>,
    /// List of keys or dot-notation path keys that must be unique in addition to primary_key.
    pub unique_keys: Option<Vec<String>>,
    /// Set to True to allow duplicate primary_key values for a list of dicts.
    /// Useful when primary key is only used for triggering documentation.
    /// NOTE! Should only be used in eos_designs inputs since we cannot merge on primary key if there are duplicate entries.
    pub allow_duplicate_primary_key: Option<bool>,
    #[serde(flatten)]
    pub base: Base<Vec<Value>>,
    pub documentation_options: Option<DocumentationOptions>,
}

impl Shortcuts for List {
    fn is_required(&self) -> bool {
        self.base.required.unwrap_or_default()
    }

    fn deprecation(&self) -> &Option<Deprecation> {
        &self.base.deprecation
    }
}

impl<'x> TryFrom<&'x AnySchema> for &'x List {
    type Error = &'static str;

    fn try_from(value: &'x AnySchema) -> Result<Self, Self::Error> {
        match value {
            AnySchema::List(list) => Ok(list),
            _ => Err("Unable to convert from AnySchema to List. Invalid Schema type."),
        }
    }
}

#[cfg(test)]
mod tests {
    use crate::{any::AnySchema, dict::Dict};

    use super::List;

    #[test]
    fn try_from_anyschema_ok() {
        let anyschema = &AnySchema::List(List::default());
        let result: Result<&List, _> = anyschema.try_into();
        assert!(result.is_ok());
    }
    #[test]
    fn try_from_anyschema_err() {
        let anyschema = &AnySchema::Dict(Dict::default());
        let result: Result<&List, _> = anyschema.try_into();
        assert!(result.is_err());
    }
}
