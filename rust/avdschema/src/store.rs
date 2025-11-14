// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.
use serde::{Deserialize, Serialize};

use crate::{
    schema::any::AnySchema,
    utils::{dump::Dump, load::Load},
};

/// Schema store containing the AVD schemas.
/// The store is used as entrypoint for validation and when resolving a $ref pointing to a specific schema.
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
impl Dump for Store {}
impl Load for Store {}

#[derive(Debug, Clone, Copy)]
pub enum Schema {
    EosDesigns,
    EosCliConfigGen,
}

impl TryFrom<&str> for Schema {
    type Error = SchemaStoreError;

    /// Try to get the Schema Enum variant for the string.
    fn try_from(value: &str) -> Result<Self, Self::Error> {
        match value {
            "eos_designs" => Ok(Self::EosDesigns),
            "eos_cli_config_gen" => Ok(Self::EosCliConfigGen),
            _ => Err(SchemaName::new(value.into()).into()),
        }
    }
}
impl From<Schema> for String {
    /// Get the schema name as string.
    fn from(value: Schema) -> Self {
        match value {
            Schema::EosDesigns => "eos_designs".to_string(),
            Schema::EosCliConfigGen => "eos_cli_config_gen".to_string(),
        }
    }
}

#[derive(Debug, derive_more::Display, derive_more::From)]
pub enum SchemaStoreError {
    SchemaName(SchemaName),
}

#[derive(Debug, derive_more::Constructor, derive_more::Display)]
#[display("Schema name '{name}' not found in the schema store.")]
pub struct SchemaName {
    pub name: String,
}

#[cfg(test)]
mod tests {

    use super::Load;

    use crate::utils::test_utils::{get_avd_store, get_tmp_file};
    use crate::{Dump as _, Store};

    #[test]
    fn dump_avd_store() {
        // Dumping uncompressed and compressed schema.
        let store = get_avd_store();

        let file_path = get_tmp_file("test_dump_avd_store_resolved.json");
        let result = store.to_file(Some(file_path));
        assert!(result.is_ok());

        // Now dump as compressed file to see the size difference
        let file_path = get_tmp_file("test_dump_avd_store_resolved.gz");
        let result = store.to_file(Some(file_path));
        assert!(result.is_ok());

        #[cfg(feature = "xz2")]
        {
            let file_path = get_tmp_file("test_dump_avd_store_resolved.xz2");
            let result = store.to_file(Some(file_path));
            assert!(result.is_ok());
        }
    }

    #[test]
    fn load_avd_store() {
        dump_avd_store();
        let store = get_avd_store();

        // Now load the previously dumped files and compare
        let file_path = get_tmp_file("test_dump_avd_store_resolved.json");
        let result = Store::from_file(Some(file_path));
        assert!(result.is_ok());
        assert_eq!(result.unwrap(), *store);

        let file_path = get_tmp_file("test_dump_avd_store_resolved.gz");
        let result = Store::from_file(Some(file_path));
        assert!(result.is_ok());
        assert_eq!(result.unwrap(), *store);

        #[cfg(feature = "xz2")]
        {
            let file_path = get_tmp_file("test_dump_avd_store_resolved.xz2");
            let result = Store::from_file(Some(file_path));
            assert!(result.is_ok());
            assert_eq!(result.unwrap(), *store);
        }
    }

    #[test]
    #[ignore = "Test only used for manual performance testing"]
    fn quick_load_avd_store_json() {
        //Depends on dump to be done before. This is just here to test the speed of loading from the file.
        let file_path = get_tmp_file("test_dump_avd_store_resolved.json");
        let result = Store::from_file(Some(file_path));
        assert!(result.is_ok());
    }

    #[test]
    #[ignore = "Test only used for manual performance testing"]
    fn quick_load_avd_store_gz() {
        //Depends on dump to be done before. This is just here to test the speed of loading from the file.
        let file_path = get_tmp_file("test_dump_avd_store_resolved.gz");
        let result = Store::from_file(Some(file_path));
        assert!(result.is_ok());
    }

    #[test]
    #[ignore = "Test only used for manual performance testing"]
    fn quick_load_avd_store_xz2() {
        //Depends on dump to be done before. This is just here to test the speed of loading from the file.
        let file_path = get_tmp_file("test_dump_avd_store_resolved.xz2");
        let result = Store::from_file(Some(file_path));
        assert!(result.is_ok());
    }
}
