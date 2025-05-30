// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.

use std::collections::HashMap;

use serde::Serialize;

/// Value Wrapper of serde_json::Value to allow us to apply conversion traits on these.
#[cfg_attr(
    feature = "python_bindings",
    pyo3::pyclass(frozen, module = "validation")
)]
#[derive(Clone, Debug, PartialEq, Serialize, derive_more::From)]
pub enum Value {
    Null(),
    Bool(bool),
    Dict(HashMap<String, Value>),
    Float(f64),
    Int(i64),
    List(Vec<Value>),
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
#[cfg_attr(
    feature = "python_bindings",
    pyo3::pyclass(frozen, get_all, module = "validation")
)]
#[derive(Clone, Debug, PartialEq, Serialize)]
pub struct Feedback {
    /// Data path which the feedback concerns.
    pub path: Vec<String>,
    pub issue: Issue,
}

/// Issue is wrapped in Feedback and added to the Context during coercion and validation.
#[cfg_attr(
    feature = "python_bindings",
    pyo3::pyclass(frozen, module = "validation")
)]
#[derive(Clone, Debug, PartialEq, Serialize, derive_more::From)]
pub enum Issue {
    /// Violation found during validation.
    Validation(Violation),
    /// Coercion performed during coercion.
    Coercion(CoercionNote),
    /// Default value as specified in the schema was inserted into the data.
    DefaultValueInserted(),
    /// Some internal error occurred.
    InternalError { message: String },
}

/// One coercion performed during recursive coercion.
#[cfg_attr(
    feature = "python_bindings",
    pyo3::pyclass(frozen, get_all, module = "validation")
)]
#[derive(Clone, Debug, PartialEq, Serialize)]
pub struct CoercionNote {
    pub found: Value,
    pub made: Value,
}

/// One violation found during recursive validation.
#[cfg_attr(
    feature = "python_bindings",
    pyo3::pyclass(frozen, module = "validation")
)]
#[derive(Clone, Debug, PartialEq, Serialize)]
pub enum Violation {
    /// The length is above the maximum allowed.
    LengthAboveMaximum { maximum: u64, found: u64 },
    /// The length is below the minimum allowed.
    LengthBelowMinimum { minimum: u64, found: u64 },
    /// The dictionary key is required, but was not set.
    MissingRequiredKey { key: String },
    /// The given schema name was not found in the schema store.
    InvalidSchema { schema: String },
    /// The value is not of the expected type.
    InvalidType { expected: Type, found: Type },
    /// The value is not among the valid values.
    InvalidValue {
        expected: ViolationValidValues,
        found: Value,
    },
    /// The value is not matching the allowed pattern.
    NotMatchingPattern { pattern: String, found: String },
    /// The dictionary key is not allowed by the schema.
    UnexpectedKey(),
    /// The value is above the maximum allowed.
    ValueAboveMaximum { maximum: i64, found: i64 },
    /// The value is below the minimum allowed.
    ValueBelowMinimum { minimum: i64, found: i64 },
    /// The value is not unique as required.
    ValueNotUnique { other_path: Vec<String> },
}

/// Data Type used in Violation.
#[cfg_attr(
    feature = "python_bindings",
    pyo3::pyclass(frozen, module = "validation")
)]
#[derive(Clone, Debug, PartialEq, Serialize)]
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
#[cfg_attr(
    feature = "python_bindings",
    pyo3::pyclass(frozen, module = "validation")
)]
#[derive(Clone, Debug, PartialEq, Serialize, derive_more::From)]
pub enum ViolationValidValues {
    Bool(Vec<bool>),
    Int(Vec<i64>),
    Str(Vec<String>),
}
