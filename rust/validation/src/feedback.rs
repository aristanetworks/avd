// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.

use std::collections::HashMap;

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

/// Feedback item carried in the Context under either `coercions` or `violations`
#[derive(Clone, Debug, PartialEq, Serialize, derive_more::Display)]
#[display("Feedback for path {path:?}: {issue}.")]
pub struct Feedback {
    /// Data path which the feedback concerns.
    pub path: Vec<String>,
    pub issue: Issue,
}

/// Issue is wrapped in Feedback and added to the Context during coercion and validation.
#[derive(Clone, Debug, PartialEq, Serialize, derive_more::From, derive_more::Display)]
pub enum Issue {
    /// Violation found during validation.
    Validation(Violation),
    /// Coercion performed during coercion.
    Coercion(CoercionNote),
    /// Default value as specified in the schema was inserted into the data.
    #[display("Inserted default value.")]
    DefaultValueInserted(),
    /// Some internal error occurred.
    #[display("An internal error occurred: {message}.")]
    InternalError { message: String },
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
    #[display("The value is not unique among similar items. Conflicting items: {other_path:?}")]
    ValueNotUnique { other_path: Vec<String> },
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
