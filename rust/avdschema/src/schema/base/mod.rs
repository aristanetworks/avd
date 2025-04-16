// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.

pub mod convert_types;
pub mod documentation_options;
pub mod valid_values;

use ordermap::OrderMap;
use serde::{Deserialize, Serialize};
use serde_json::Value;
use serde_with::skip_serializing_none;

/// DataValue marks the allowed types to be used as generics in Base, ValidValues and default values.
pub trait DataValue {}
impl DataValue for bool {}
impl DataValue for i64 {}
impl DataValue for String {}
// OrderMap<String, Value> corresponds to a dict
impl DataValue for OrderMap<String, Value> {}
// Vec<Value> corresponds to a list
impl DataValue for Vec<Value> {}

/// Schema properties shared by all schema types.
#[skip_serializing_none]
#[derive(Debug, Default, Clone, PartialEq, Serialize, Deserialize)]
#[serde(deny_unknown_fields)]
pub struct Base<T>
where
    T: DataValue,
{
    /// Default value
    pub default: Option<T>,
    /// Free text display name for forms and documentation (single line)
    pub display_name: Option<String>,
    /// Free text description for forms and documentation (multi line)
    pub description: Option<String>,
    /// Key is required
    pub required: Option<bool>,
    pub deprecation: Option<Deprecation>,
    #[serde(rename = "$ref")]
    pub schema_ref: Option<String>,
}

/// Deprecation settings
#[skip_serializing_none]
#[derive(Debug, Default, Clone, PartialEq, Serialize, Deserialize)]
#[serde(deny_unknown_fields)]
pub struct Deprecation {
    /// Emit deprecation warning if key is set
    pub warning: bool,
    /// Relative path to new key
    pub new_key: Option<String>,
    /// Support for this key has been removed
    pub removed: Option<bool>,
    /// Version in which the key will be removed
    pub remove_in_version: Option<String>,
    /// Date after which the key will be removed in the next major version
    pub remove_after_date: Option<String>,
    /// URL detailing the deprecation and migration guidelines
    pub url: Option<String>,
}
