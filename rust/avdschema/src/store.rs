// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.

use serde::{Deserialize, Serialize};
use strum_macros::AsRefStr;

use crate::{
    schema::any::AnySchema,
    utils::{dump::Dump, load::Load},
};

#[derive(Debug, Clone, PartialEq, Serialize, Deserialize)]
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

#[cfg(test)]
mod tests {
    use super::Load;
    use crate::any::AnySchema;
    use crate::utils::test_utils::{
        EOS_CLI_CONFIG_GEN_FRAGMENTS, EOS_DESIGNS_FRAGMENTS, get_tmp_file,
    };
    use crate::{Dump as _, LoadFromFragments as _, Store, resolve_schema};

    #[test]
    fn dump_avd_store() {
        // Dumping each stage of resolving a full store, to make it easier to track the behavior in the generated artifacts.

        // First load schemas from fragments and dump the store with raw schemas containing refs etc.
        let mut eos_cli_config_gen_schema =
            AnySchema::from_fragments(EOS_CLI_CONFIG_GEN_FRAGMENTS.into()).unwrap();
        let mut eos_designs_schema =
            AnySchema::from_fragments(EOS_DESIGNS_FRAGMENTS.into()).unwrap();
        let mut store = Store {
            eos_cli_config_gen: eos_cli_config_gen_schema.to_owned(),
            eos_designs: eos_designs_schema.to_owned(),
        };
        let file_path = get_tmp_file("test_dump_avd_store_with_refs.yml");
        let result = store.to_file(Some(file_path));
        assert!(result.is_ok());

        // Next in-place resolve each schema and replace in the store and dump the fully resolved store.
        resolve_schema(&mut eos_cli_config_gen_schema, &store).unwrap();
        store.eos_cli_config_gen = eos_cli_config_gen_schema;
        resolve_schema(&mut eos_designs_schema, &store).unwrap();
        store.eos_designs = eos_designs_schema;
        let file_path = get_tmp_file("test_dump_avd_store_resolved.yml");
        let result = store.to_file(Some(file_path));
        assert!(result.is_ok());

        // Now dump as compressed file to see the size difference
        let file_path = get_tmp_file("test_dump_avd_store_resolved.xz2");
        let result = store.to_file(Some(file_path));
        assert!(result.is_ok());
    }

    #[test]
    fn load_avd_store() {
        dump_avd_store();

        // Load schemas from fragments, resolve all $ref and save in a store we can compare the loaded store with.
        let mut eos_cli_config_gen_schema =
            AnySchema::from_fragments(EOS_CLI_CONFIG_GEN_FRAGMENTS.into()).unwrap();
        let mut eos_designs_schema =
            AnySchema::from_fragments(EOS_DESIGNS_FRAGMENTS.into()).unwrap();
        let mut store = Store {
            eos_cli_config_gen: eos_cli_config_gen_schema.to_owned(),
            eos_designs: eos_designs_schema.to_owned(),
        };
        resolve_schema(&mut eos_cli_config_gen_schema, &store).unwrap();
        store.eos_cli_config_gen = eos_cli_config_gen_schema;
        resolve_schema(&mut eos_designs_schema, &store).unwrap();
        store.eos_designs = eos_designs_schema;

        // Now load the previously dumped files and compare
        let file_path = get_tmp_file("test_dump_avd_store_resolved.yml");
        let result = Store::from_file(Some(file_path));
        assert!(result.is_ok());
        assert_eq!(result.unwrap(), store);

        let file_path = get_tmp_file("test_dump_avd_store_resolved.xz2");
        let result = Store::from_file(Some(file_path));
        assert!(result.is_ok());
        assert_eq!(result.unwrap(), store);
    }
}
