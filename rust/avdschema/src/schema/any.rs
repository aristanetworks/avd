// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.

use serde::{Deserialize, Serialize};

use crate::utils::{dump::Dump, load::Load};

#[cfg(feature = "dump_load_files")]
use crate::utils::load::LoadFromFragments;

use super::{boolean::Bool, dict::Dict, int::Int, list::List, str::Str};

#[derive(Debug, Clone, PartialEq, Serialize, Deserialize)]
#[serde(tag = "type", rename_all = "lowercase")]
pub enum AnySchema {
    Bool(Bool),
    Int(Int),
    Str(Str),
    List(List),
    Dict(Dict),
}
impl From<Bool> for AnySchema {
    fn from(value: Bool) -> Self {
        Self::Bool(value)
    }
}
impl From<Int> for AnySchema {
    fn from(value: Int) -> Self {
        Self::Int(value)
    }
}
impl From<Str> for AnySchema {
    fn from(value: Str) -> Self {
        Self::Str(value)
    }
}
impl From<List> for AnySchema {
    fn from(value: List) -> Self {
        Self::List(value)
    }
}
impl From<Dict> for AnySchema {
    fn from(value: Dict) -> Self {
        Self::Dict(value)
    }
}
impl Dump for AnySchema {}
impl Load for AnySchema {}
#[cfg(feature = "dump_load_files")]
impl LoadFromFragments for AnySchema {}

impl From<&AnySchema> for String {
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
