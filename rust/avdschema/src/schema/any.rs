// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.

use crate::delegate_anyshcema_method;

use serde::{Deserialize, Serialize};

use crate::{
    base::Deprecation,
    utils::{dump::Dump, load::Load},
};

#[cfg(feature = "dump_load_files")]
use crate::utils::load::LoadFromFragments;

use super::{boolean::Bool, dict::Dict, int::Int, list::List, str::Str};

/// Enum covering all AVD Schema types.
#[derive(Debug, Clone, PartialEq, Serialize, Deserialize, derive_more::From)]
#[serde(tag = "type", rename_all = "lowercase")]
pub enum AnySchema {
    Bool(Bool),
    Int(Int),
    Str(Str),
    List(List),
    Dict(Dict),
}

impl Dump for AnySchema {}
impl Load for AnySchema {}
#[cfg(feature = "dump_load_files")]
impl LoadFromFragments for AnySchema {}

impl From<&AnySchema> for String {
    /// Get schema type as Python-like type string
    fn from(value: &AnySchema) -> Self {
        match value {
            AnySchema::Bool(_) => "bool".to_string(),
            AnySchema::Dict(_) => "dict".to_string(),
            AnySchema::Int(_) => "int".to_string(),
            AnySchema::List(_) => "list".to_string(),
            AnySchema::Str(_) => "str".to_string(),
        }
    }
}

impl From<&mut AnySchema> for String {
    /// Get schema type as Python-like type string
    fn from(value: &mut AnySchema) -> Self {
        match value {
            AnySchema::Bool(_) => "bool".to_string(),
            AnySchema::Dict(_) => "dict".to_string(),
            AnySchema::Int(_) => "int".to_string(),
            AnySchema::List(_) => "list".to_string(),
            AnySchema::Str(_) => "str".to_string(),
        }
    }
}

pub trait Shortcuts {
    /// Returns a boolean indicating if the schema field is required.
    fn is_required(&self) -> bool;

    /// Returns the deprecation information from the schema if set.
    fn deprecation(&self) -> &Option<Deprecation>;
}

impl Shortcuts for AnySchema {
    fn is_required(&self) -> bool {
        delegate_anyshcema_method!(self, is_required,)
    }

    fn deprecation(&self) -> &Option<Deprecation> {
        delegate_anyshcema_method!(self, deprecation,)
    }
}
