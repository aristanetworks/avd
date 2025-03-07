// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.

use serde::{Deserialize, Serialize};

use crate::utils::{
    dump::Dump,
    load::{Load, LoadFromFragments},
};

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
impl LoadFromFragments for AnySchema {}
