// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.

use std::{
    collections::HashMap,
    fmt::{Debug, Display},
};

use serde::Serialize;

/// Value Wrapper of serde_json::Value to allow us to apply conversion traits on these.
#[derive(Clone, Debug, PartialEq, Serialize, derive_more::From, derive_more::Display)]
pub enum Value {
    #[display("null")]
    Null(),
    Bool(bool),
    #[display("{_0:?}")]
    Dict(HashMap<String, Value>),
    Float(f64),
    Int(i64),
    #[display("{_0:?}")]
    List(Vec<Value>),
    #[display("\"{_0}\"")]
    Str(String),
}
impl From<serde_json::Value> for Value {
    fn from(value: serde_json::Value) -> Self {
        match value {
            serde_json::Value::Array(value) => {
                Self::List(value.into_iter().map(Value::from).collect::<Vec<_>>())
            }
            serde_json::Value::Null => Self::Null(),
            serde_json::Value::Bool(value) => Self::Bool(value),
            serde_json::Value::Number(number) => {
                if let Some(value) = number.as_i64() {
                    Self::Int(value)
                } else if let Some(value) = number.as_f64() {
                    Self::Float(value)
                } else {
                    // Falling back to str
                    Self::Str(number.as_str().to_string())
                }
            }
            serde_json::Value::Object(value) => Self::Dict(
                // By using hashmap we accept that keys may be reordered here.
                value
                    .into_iter()
                    .map(|(k, v)| (k, Value::from(v)))
                    .collect::<std::collections::HashMap<_, _>>(),
            ),
            serde_json::Value::String(value) => Self::Str(value),
        }
    }
}
impl From<&str> for Value {
    fn from(value: &str) -> Self {
        Self::Str(value.to_string())
    }
}

#[derive(Clone, Debug, Default, PartialEq, Serialize, derive_more::From)]
pub struct Path(Vec<String>);
impl Path {
    pub(crate) fn push(&mut self, step: String) {
        self.0.push(step)
    }
    pub(crate) fn pop(&mut self) -> Option<String> {
        self.0.pop()
    }
    pub(crate) fn is_empty(&self) -> bool {
        self.0.is_empty()
    }
    pub(crate) fn clone_with_slice(&self, slice: &[String]) -> Self {
        let mut new = self.clone();
        new.0.extend_from_slice(slice);
        new
    }
}
impl From<&str> for Path {
    fn from(value: &str) -> Self {
        Self(value.split(".").map(|step| step.to_string()).collect())
    }
}

/// Display the path as a json path string like outer[1].inner.lst[23]
impl std::fmt::Display for Path {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        let mut string = String::default();
        for (index, element) in self.0.iter().enumerate() {
            if element.parse::<u64>().is_ok() {
                string.push('[');
                string.push_str(element);
                string.push(']');
            } else {
                if index > 0 {
                    string.push('.');
                }
                string.push_str(element);
            }
        }
        f.write_str(&string)
    }
}
impl From<Path> for Vec<String> {
    fn from(value: Path) -> Self {
        value.0
    }
}
impl<'a> FromIterator<&'a str> for Path {
    fn from_iter<T: IntoIterator<Item = &'a str>>(iter: T) -> Self {
        Self(Vec::from_iter(
            iter.into_iter().map(|item| item.to_string()),
        ))
    }
}

/// Feedback item carried in the Context under either `coercions` or `violations`
#[derive(Clone, Debug, PartialEq, Serialize, derive_more::Display)]
#[display("Feedback for path {path:?}: {issue}.")]
pub struct Feedback<T: Clone + Debug + PartialEq + Serialize + Display> {
    /// Data path which the feedback concerns.
    pub path: Path,
    pub issue: T,
}

/// Error issue is wrapped in Feedback and added to the Context during coercion and validation.
#[derive(Clone, Debug, PartialEq, Serialize, derive_more::From, derive_more::Display)]
pub enum ErrorIssue {
    /// Violation found during validation.
    Violation(Violation),
    /// Some internal error occurred.
    #[display("An internal error occurred: {message}.")]
    InternalError { message: String },
}

/// WarningIssue is wrapped in Feedback and added to the Context during coercion and validation.
#[derive(Clone, Debug, PartialEq, Serialize, derive_more::From, derive_more::Display)]
pub enum WarningIssue {
    /// Deprecation of data model.
    Deprecated(Deprecated),
}

/// InfoIssue is wrapped in Feedback and added to the Context during coercion and validation.
#[derive(Clone, Debug, PartialEq, Serialize, derive_more::From, derive_more::Display)]
pub enum InfoIssue {
    /// Coercion performed during coercion.
    Coercion(CoercionNote),
    /// Default value as specified in the schema was inserted into the data.
    #[display("Inserted default value.")]
    DefaultValueInserted(),
}

/// One coercion performed during recursive coercion.
#[derive(Clone, Debug, PartialEq, Serialize, derive_more::Display)]
#[display("Coerced value from {found} to {made}.")]
pub struct CoercionNote {
    pub found: Value,
    pub made: Value,
}

/// One violation found during recursive validation.
#[derive(Clone, Debug, PartialEq, Serialize, derive_more::Display)]
pub enum Violation {
    /// The length is above the maximum allowed.
    #[display("The length ({found}) is above the maximum allowed ({maximum}).")]
    LengthAboveMaximum { maximum: u64, found: u64 },
    /// The length is below the minimum allowed.
    #[display("The length ({found}) is below the minimum allowed ({minimum}).")]
    LengthBelowMinimum { minimum: u64, found: u64 },
    /// The dictionary key is required, but was not set.
    #[display("Missing the required key '{key}'.")]
    MissingRequiredKey { key: String },
    /// The given schema name was not found in the schema store.
    #[display("Invalid Schema name '{schema}'.")]
    InvalidSchema { schema: String },
    /// The value is not of the expected type.
    #[display("Invalid type '{found}'. Expected '{expected}'.")]
    InvalidType { expected: Type, found: Type },
    /// The value is not among the valid values.
    #[display("The value '{found}' is not among the valid values {expected}.")]
    InvalidValue {
        expected: ViolationValidValues,
        found: Value,
    },
    /// The value is not matching the allowed pattern.
    #[display("The value '{found}' does not match the allowed pattern '{pattern}'.")]
    NotMatchingPattern { pattern: String, found: String },
    /// The dictionary key is not allowed by the schema.
    #[display("Invalid key.")]
    UnexpectedKey(),
    /// The value is above the maximum allowed.
    #[display("The value '{found}' is above the maximum allowed '{maximum}'.")]
    ValueAboveMaximum { maximum: i64, found: i64 },
    /// The value is below the minimum allowed.
    #[display("The value '{found}' is below the minimum allowed '{minimum}'.")]
    ValueBelowMinimum { minimum: i64, found: i64 },
    /// The value is not unique as required.
    #[display("The value is not unique among similar items. Conflicting item: {other_path}")]
    ValueNotUnique { other_path: Path },
    /// The input data model is deprecated and cannot be used in conjunction with the new data model.
    #[display(
        "The input data model is deprecated and cannot be used in conjunction with the new data model '{other_path}'.{url}"
    )]
    DeprecatedConflict { other_path: Path, url: UrlField },
    /// Removed after deprecation of data model.
    Removed(Removed),
}

/// Data Type used in Violation.
#[derive(Clone, Debug, PartialEq, Serialize, derive_more::Display)]
pub enum Type {
    Null,
    Bool,
    Int,
    Str,
    List,
    Dict,
}
impl From<&serde_json::Value> for Type {
    fn from(value: &serde_json::Value) -> Self {
        match value {
            serde_json::Value::Null => Self::Null,
            serde_json::Value::Bool(_) => Self::Bool,
            serde_json::Value::Number(_) => Self::Int,
            serde_json::Value::String(_) => Self::Str,
            serde_json::Value::Array(_) => Self::List,
            serde_json::Value::Object(_) => Self::Dict,
        }
    }
}

/// List of valid values used in Violation
#[derive(Clone, Debug, PartialEq, Serialize, derive_more::From, derive_more::Display)]
pub enum ViolationValidValues {
    #[display("{_0:?}")]
    Bool(Vec<bool>),
    #[display("{_0:?}")]
    Int(Vec<i64>),
    #[display("{_0:?}")]
    Str(Vec<String>),
}

#[derive(Clone, Debug, PartialEq, Serialize, derive_more::From)]
pub struct ReplacementField(Option<String>);
impl Display for ReplacementField {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        if let Some(replacement) = &self.0 {
            write!(f, " Use '{replacement}' instead.")
        } else {
            Ok(())
        }
    }
}
impl From<ReplacementField> for Option<String> {
    fn from(value: ReplacementField) -> Self {
        value.0
    }
}

#[derive(Clone, Debug, PartialEq, Serialize, derive_more::From)]
pub struct VersionField(Option<String>);
impl Display for VersionField {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        if let Some(version) = &self.0 {
            write!(f, " in AVD version {version}")
        } else {
            Ok(())
        }
    }
}
impl From<VersionField> for Option<String> {
    fn from(value: VersionField) -> Self {
        value.0
    }
}

#[derive(Clone, Debug, PartialEq, Serialize, derive_more::From)]
pub struct UrlField(Option<String>);
impl Display for UrlField {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        if let Some(url) = &self.0 {
            write!(f, " See '{url}' for details.")
        } else {
            Ok(())
        }
    }
}
impl From<UrlField> for Option<String> {
    fn from(value: UrlField) -> Self {
        value.0
    }
}

#[derive(Clone, Debug, PartialEq, Serialize, derive_more::Display)]
#[display(
    "The input data model '{path}' is deprecated and will be removed{version}.{replacement}{url}"
)]
pub struct Deprecated {
    pub path: Path,
    pub replacement: ReplacementField,
    pub version: VersionField,
    pub url: UrlField,
}
impl Deprecated {
    pub(crate) fn from_schema(path: &Path, deprecation: &avdschema::base::Deprecation) -> Self {
        Self {
            path: path.to_owned(),
            replacement: deprecation.new_key.to_owned().into(),
            version: deprecation.remove_in_version.to_owned().into(),
            url: deprecation.url.to_owned().into(),
        }
    }
}

#[derive(Clone, Debug, PartialEq, Serialize, derive_more::Display)]
#[display("The input data model '{path}' was removed{version}.{replacement}{url}")]
pub struct Removed {
    pub path: Path,
    pub replacement: ReplacementField,
    pub version: VersionField,
    pub url: UrlField,
}
impl Removed {
    pub(crate) fn from_schema(path: &Path, deprecation: &avdschema::base::Deprecation) -> Self {
        Self {
            path: path.to_owned(),
            replacement: deprecation.new_key.to_owned().into(),
            version: deprecation.remove_in_version.to_owned().into(),
            url: deprecation.url.to_owned().into(),
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn value_from_json_value() {
        let value = Value::from(serde_json::json!(true));
        assert_eq!(value, Value::Bool(true));
        let value = Value::from(serde_json::json!(-123));
        assert_eq!(value, Value::Int(-123));
        let value = Value::from(serde_json::json!(123.45));
        assert_eq!(value, Value::Float(123.45));
        let value: Value = Value::from(serde_json::json!(null));
        assert_eq!(value, Value::Null());
        let value = Value::from(serde_json::json!("string"));
        assert_eq!(value, Value::Str("string".to_string()));
        let value = Value::from(serde_json::json!({"key": "value"}));
        assert_eq!(
            value,
            Value::Dict([("key".to_string(), Value::Str("value".to_string()))].into())
        );
        let value = Value::from(serde_json::json!(["item", 123]));
        assert_eq!(
            value,
            Value::List([Value::Str("item".to_string()), Value::Int(123)].into())
        );
    }

    #[test]
    fn type_from_json_value() {
        let type_ = Type::from(&serde_json::json!(null));
        assert_eq!(type_, Type::Null);
        let type_ = Type::from(&serde_json::json!(true));
        assert_eq!(type_, Type::Bool);
        let type_ = Type::from(&serde_json::json!(-123));
        assert_eq!(type_, Type::Int);
        let type_ = Type::from(&serde_json::json!("string"));
        assert_eq!(type_, Type::Str);
        let type_ = Type::from(&serde_json::json!({"key": "value"}));
        assert_eq!(type_, Type::Dict);
        let type_ = Type::from(&serde_json::json!(["item", 123]));
        assert_eq!(type_, Type::List);
    }

    #[test]
    fn value_display() {
        let value = Value::Bool(true);
        assert_eq!(format!("{}", value).as_str(), "true");
        let value = Value::Int(-123);
        assert_eq!(format!("{}", value).as_str(), "-123");
        let value = Value::Float(123.45);
        assert_eq!(format!("{}", value).as_str(), "123.45");
        let value = Value::Null();
        assert_eq!(format!("{}", value).as_str(), "null");
        let value = Value::Str("string".to_string());
        assert_eq!(format!("{}", value).as_str(), "\"string\"");
        let value = Value::Dict([("key".to_string(), Value::Str("value".to_string()))].into());
        // TODO: Improve the output format for dicts. Not really used currently.
        assert_eq!(format!("{}", value).as_str(), "{\"key\": Str(\"value\")}");
        let value = Value::List([Value::Str("item".to_string()), Value::Int(123)].into());
        // TODO: Improve the output format for lists. Not really used currently.
        assert_eq!(format!("{}", value).as_str(), "[Str(\"item\"), Int(123)]");
    }
    #[test]
    fn deprecated_display() {
        let deprecated = Deprecated {
            path: Path::from(vec![
                "key".to_string(),
                "1".to_string(),
                "subkey".to_string(),
            ]),
            replacement: Some("another_key".to_string()).into(),
            version: Some("6.0.0".to_string()).into(),
            url: Some("foo.bar".to_string()).into(),
        };
        assert_eq!(
            format!("{}", deprecated).as_str(),
            "The input data model 'key[1].subkey' is deprecated and will be removed in AVD version 6.0.0. Use 'another_key' instead. See 'foo.bar' for details."
        );
    }

    #[test]
    fn removed_display() {
        let removed = Removed {
            path: Path::from(vec![
                "key".to_string(),
                "1".to_string(),
                "subkey".to_string(),
            ]),
            replacement: Some("another_key".to_string()).into(),
            version: Some("6.0.0".to_string()).into(),
            url: Some("foo.bar".to_string()).into(),
        };
        assert_eq!(
            format!("{}", removed).as_str(),
            "The input data model 'key[1].subkey' was removed in AVD version 6.0.0. Use 'another_key' instead. See 'foo.bar' for details."
        );
    }

    fn get_deprecation_test_schema() -> avdschema::base::Deprecation {
        avdschema::base::Deprecation {
            warning: true,
            new_key: Some("new_key".to_string()),
            removed: Some(true),
            remove_in_version: Some("6.0.0".to_string()),
            url: Some("my.url".to_string()),
            ..Default::default()
        }
    }

    #[test]
    fn deprecated_from_schema() {
        let deprecated =
            Deprecated::from_schema(&Path::from_iter(["foo"]), &get_deprecation_test_schema());
        let expected_deprecated = Deprecated {
            path: Path::from(vec!["foo".to_string()]),
            replacement: Some("new_key".to_string()).into(),
            version: Some("6.0.0".to_string()).into(),
            url: Some("my.url".to_string()).into(),
        };
        assert_eq!(deprecated, expected_deprecated);
    }

    #[test]
    fn removed_from_schema() {
        let removed =
            Removed::from_schema(&Path::from_iter(["foo"]), &get_deprecation_test_schema());
        let expected_removed = Removed {
            path: Path::from(vec!["foo".to_string()]),
            replacement: Some("new_key".to_string()).into(),
            version: Some("6.0.0".to_string()).into(),
            url: Some("my.url".to_string()).into(),
        };
        assert_eq!(removed, expected_removed);
    }
}
