// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.

use std::sync::OnceLock;

use regex::Regex;
use serde::{Deserialize, Serialize};
use serde_with::skip_serializing_none;

use crate::{any::Shortcuts, base::Deprecation};

use super::{
    any::AnySchema,
    base::{
        Base, convert_types::ConvertTypes, documentation_options::DocumentationOptions,
        valid_values::ValidValues,
    },
};

/// Enum for string formats allowed by the Str schema.
#[derive(Debug, Clone, Copy, PartialEq, Serialize, Deserialize)]
#[serde(rename_all = "snake_case")]
pub enum Format {
    Cidr,
    Ip,
    IpPool,
    Ipv4,
    Ipv4Cidr,
    Ipv4Pool,
    Ipv6,
    Ipv6Cidr,
    Ipv6Pool,
    Mac,
}

/// AVD Schema for string data.
#[skip_serializing_none]
#[derive(Debug, Clone, Default, PartialEq, Serialize, Deserialize)]
#[serde(deny_unknown_fields)]
pub struct Str {
    /// Convert string value to lower case before performing validation
    pub convert_to_lower_case: Option<bool>,
    pub format: Option<Format>,
    pub max_length: Option<u64>,
    pub min_length: Option<u64>,
    /// A regular expression which will be matched on the variable value.
    /// The regular expression should be valid according to the ECMA 262 dialect
    /// Remember to use double escapes
    pub pattern: Option<Pattern>,
    #[serde(flatten)]
    pub base: Base<String>,
    #[serde(flatten)]
    pub convert_types: ConvertTypes,
    #[serde(flatten)]
    pub valid_values: ValidValues<String>,
    pub documentation_options: Option<DocumentationOptions>,
}

impl Shortcuts for Str {
    fn is_required(&self) -> bool {
        self.base.required.unwrap_or_default()
    }

    fn deprecation(&self) -> &Option<Deprecation> {
        &self.base.deprecation
    }
}

impl<'x> TryFrom<&'x AnySchema> for &'x Str {
    type Error = &'static str;

    fn try_from(value: &'x AnySchema) -> Result<Self, Self::Error> {
        match value {
            AnySchema::Str(str) => Ok(str),
            _ => Err("Unable to convert from AnySchema to Str. Invalid Schema type."),
        }
    }
}

#[derive(Debug, Clone, Serialize, Deserialize, derive_more::Display)]
#[display("{pattern}")]
#[serde(transparent)]
pub struct Pattern {
    pub pattern: String,
    #[serde(skip)]
    compiled_pattern: OnceLock<Regex>,
}
impl Pattern {
    fn new(pattern: String) -> Self {
        Self {
            pattern,
            compiled_pattern: Default::default(),
        }
    }
    pub fn get_compiled_pattern(&self) -> &Regex {
        self.compiled_pattern
            .get_or_init(|| Regex::new(format!("^{}$",&self.pattern).as_str()).unwrap())
    }
}
impl PartialEq for Pattern {
    fn eq(&self, other: &Self) -> bool {
        self.pattern == other.pattern
    }
}
impl From<&str> for Pattern {
    fn from(value: &str) -> Self {
        Self::new(value.to_string())
    }
}

#[cfg(test)]
mod tests {
    use crate::{any::AnySchema, boolean::Bool};

    use super::Str;

    #[test]
    fn try_from_anyschema_ok() {
        let anyschema = &AnySchema::Str(Str::default());
        let result: Result<&Str, _> = anyschema.try_into();
        assert!(result.is_ok());
    }
    #[test]
    fn try_from_anyschema_err() {
        let anyschema = &AnySchema::Bool(Bool::default());
        let result: Result<&Str, _> = anyschema.try_into();
        assert!(result.is_err());
    }
}
