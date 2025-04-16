// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.

use super::{
    any::AnySchema,
    base::{Base, documentation_options::DocumentationOptions},
};
use serde::{Deserialize, Serialize};
use serde_with::skip_serializing_none;

/// AVD Schema for boolean data.
#[skip_serializing_none]
#[derive(Debug, Clone, Default, PartialEq, Serialize, Deserialize)]
#[serde(deny_unknown_fields)]
pub struct Bool {
    #[serde(flatten)]
    pub base: Base<bool>,
    pub documentation_options: Option<DocumentationOptions>,
}

impl<'x> TryFrom<&'x AnySchema> for &'x Bool {
    type Error = &'static str;

    fn try_from(value: &'x AnySchema) -> Result<Self, Self::Error> {
        match value {
            AnySchema::Bool(bool) => Ok(bool),
            _ => Err("Unable to convert from AnySchema to Bool. Invalid Schema type."),
        }
    }
}

#[cfg(test)]
mod tests {
    use crate::{any::AnySchema, str::Str};

    use super::Bool;

    #[test]
    fn try_from_anyschema_ok() {
        let anyschema = &AnySchema::Bool(Bool::default());
        let result: Result<&Bool, _> = anyschema.try_into();
        assert!(result.is_ok());
    }
    #[test]
    fn try_from_anyschema_err() {
        let anyschema = &AnySchema::Str(Str::default());
        let result: Result<&Bool, _> = anyschema.try_into();
        assert!(result.is_err());
    }
}
