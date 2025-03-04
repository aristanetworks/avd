// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.

use serde::{Deserialize, Serialize};
use strum_macros::AsRefStr;

use crate::{
    schema::any::AnySchema,
    utils::{dump::Dump, load::Load},
};

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct Store {
    pub eos_cli_config_gen: AnySchema,
    pub eos_designs: AnySchema,
}
impl Store {
    pub fn get(&self, schema: Schema) -> &AnySchema {
        match schema {
            Schema::EosDesigns => &self.eos_designs,
            Schema::EosCliConfigGen => &self.eos_cli_config_gen,
        }
    }
}

#[derive(Debug, Clone, Copy, AsRefStr)]
pub enum Schema {
    EosDesigns,
    EosCliConfigGen,
}

impl TryFrom<&str> for Schema {
    type Error = &'static str;

    fn try_from(value: &str) -> Result<Self, Self::Error> {
        match value {
            "eos_designs" => Ok(Self::EosDesigns),
            "eos_cli_config_gen" => Ok(Self::EosCliConfigGen),
            _ => Err("Invalid schema name"),
        }
    }
}

impl Dump for Store {}
impl Load for Store {}
