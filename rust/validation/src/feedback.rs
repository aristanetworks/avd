// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.
use serde::Serialize;
use serde_json::Value;

#[derive(Debug, PartialEq, Serialize)]
pub struct Feedback {
    pub path: Vec<String>,
    pub issue: Issue,
}

#[derive(Debug, PartialEq, Serialize)]
pub enum Issue {
    Validation(Violation),
    Coercion(CoercionNote),
    InternalError { message: String },
}

impl From<CoercionNote> for Issue {
    fn from(value: CoercionNote) -> Self {
        Self::Coercion(value)
    }
}

impl From<Violation> for Issue {
    fn from(value: Violation) -> Self {
        Self::Validation(value)
    }
}

#[derive(Debug, PartialEq, Eq, Serialize)]
pub struct CoercionNote {
    pub found: Value,
    pub made: Value,
}

#[derive(Debug, PartialEq, Serialize)]
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
    /// The value is not conforming to the pattern allowed.
    InvalidValuePattern { pattern: String, found: String },
    /// The dictionary key is not allowed by the schema.
    UnexpectedKey { key: String },
    /// The value is above the maximum allowed.
    ValueAboveMaximum { maximum: i64, found: i64 },
    /// The value is below the minimum allowed.
    ValueBelowMinimum { minimum: i64, found: i64 },
    /// The value is not unique as required.
    ValueNotUnique { other_path: Vec<String> },
}

#[derive(Debug, PartialEq, Serialize)]
pub enum Type {
    Null,
    Bool,
    Int,
    Str,
    List,
    Dict,
}

impl From<&Value> for Type {
    fn from(value: &Value) -> Self {
        match value {
            Value::Null => Self::Null,
            Value::Bool(_) => Self::Bool,
            Value::Number(_) => Self::Int,
            Value::String(_) => Self::Str,
            Value::Array(_) => Self::List,
            Value::Object(_) => Self::Dict,
        }
    }
}

#[derive(Debug, PartialEq, Serialize)]
pub enum ViolationValidValues {
    Bool(Vec<bool>),
    Int(Vec<i64>),
    Str(Vec<String>),
}

impl From<Vec<bool>> for ViolationValidValues {
    fn from(value: Vec<bool>) -> Self {
        ViolationValidValues::Bool(value)
    }
}

impl From<Vec<i64>> for ViolationValidValues {
    fn from(value: Vec<i64>) -> Self {
        ViolationValidValues::Int(value)
    }
}

impl From<Vec<String>> for ViolationValidValues {
    fn from(value: Vec<String>) -> Self {
        ViolationValidValues::Str(value)
    }
}
