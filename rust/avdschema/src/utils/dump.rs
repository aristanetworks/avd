// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.

use serde::Serialize;
use std::ffi::OsStr;
use std::fs::File;
use std::io::{self, BufWriter};
use std::path::PathBuf;

pub trait Dump
where
    Self: Serialize,
{
    fn to_json(&self) -> Result<String, Box<dyn std::error::Error>> {
        Ok(serde_json::to_string(self)?)
    }
    fn to_file(&self, output: Option<PathBuf>) -> Result<(), Box<dyn std::error::Error>> {
        // Output result to file / stdout
        match output {
            Some(path) => match path.extension().and_then(OsStr::to_str) {
                Some("yml" | "yaml") => self.to_yaml_file(path),
                Some("json") => self.to_json_file(path),
                Some("xz2") => self.to_xz2_file(path),
                _ => Err("Invalid extension for output file".into()),
            },
            None => self.to_stdout(),
        }
    }
    fn to_stdout(&self) -> Result<(), Box<dyn std::error::Error>> {
        let writer = io::stdout();
        Ok(serde_json::to_writer(writer, self)?)
    }
    fn to_yaml_file(&self, path: PathBuf) -> Result<(), Box<dyn std::error::Error>> {
        let file = File::create(path)?;
        let writer = BufWriter::new(file);
        Ok(serde_yaml::to_writer(writer, self)?)
    }
    fn to_xz2_file(&self, path: PathBuf) -> Result<(), Box<dyn std::error::Error>> {
        let file = File::create(path)?;
        let compressor = xz2::write::XzEncoder::new(file, 6);
        let writer = BufWriter::new(compressor);
        Ok(serde_json::to_writer(writer, self)?)
    }
    fn to_json_file(&self, path: PathBuf) -> Result<(), Box<dyn std::error::Error>> {
        let file = File::create(path)?;
        let writer = BufWriter::new(file);
        Ok(serde_json::to_writer(writer, self)?)
    }
}

// These tests are also called from the load tests.
#[cfg(test)]
pub(crate) mod tests {
    use super::Dump;
    use crate::{
        LoadFromFragments as _, Store,
        any::AnySchema,
        resolve_schema,
        utils::test_utils::{
            EOS_CLI_CONFIG_GEN_FRAGMENTS, EOS_DESIGNS_FRAGMENTS, get_test_dict_schema,
            get_test_store, get_tmp_file,
        },
    };

    #[test]
    pub(crate) fn dump_yaml() {
        let file_path = get_tmp_file("test_dump.yml");
        let schema = get_test_dict_schema();
        let result = schema.to_file(Some(file_path));
        assert!(result.is_ok())
    }
    #[test]
    pub(crate) fn dump_json() {
        let file_path = get_tmp_file("test_dump.json");
        let schema = get_test_dict_schema();
        let result = schema.to_file(Some(file_path));
        assert!(result.is_ok())
    }
    #[test]
    pub(crate) fn dump_xz2() {
        let file_path = get_tmp_file("test_dump.xz2");
        let schema = get_test_dict_schema();
        let result = schema.to_file(Some(file_path));
        assert!(result.is_ok())
    }
    #[test]
    pub(crate) fn dump_store_yaml() {
        let file_path = get_tmp_file("test_dump_store.yml");
        let store = get_test_store();
        let result = store.to_file(Some(file_path));
        assert!(result.is_ok())
    }

    #[test]
    pub(crate) fn dump_avd_store() {
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
}
