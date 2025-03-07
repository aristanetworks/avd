// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.

use serde::de::DeserializeOwned;
use std::ffi::OsStr;
use std::fs::File;
use std::io::{self, BufReader};
use std::path::PathBuf;
use walkdir::WalkDir;

use crate::Inherit;

pub trait Load
where
    Self: DeserializeOwned,
{
    fn from_json(json: &str) -> Result<Self, Box<dyn std::error::Error>> {
        Ok(serde_json::from_str(json)?)
    }
    fn from_file(input: Option<PathBuf>) -> Result<Self, Box<dyn std::error::Error>> {
        // Read input from file / stdin
        match input {
            Some(path) => match path.extension().and_then(OsStr::to_str) {
                Some("yml" | "yaml") => Self::from_yaml_file(path),
                Some("json") => Self::from_json_file(path),
                Some("xz2") => Self::from_xz2_file(path),
                _ => Err("Invalid extension for input file".into()),
            },
            None => Self::from_stdin(),
        }
    }
    fn from_stdin() -> Result<Self, Box<dyn std::error::Error>> {
        let reader = io::stdin();
        Ok(serde_yaml::from_reader(reader)?)
    }
    fn from_yaml_file(path: PathBuf) -> Result<Self, Box<dyn std::error::Error>> {
        let file = File::open(path)?;
        let reader = BufReader::new(file);
        Ok(serde_yaml::from_reader(reader)?)
    }
    fn from_xz2_file(path: PathBuf) -> Result<Self, Box<dyn std::error::Error>> {
        let file = File::open(path)?;
        let decompressor = xz2::read::XzDecoder::new(file);
        let reader = BufReader::new(decompressor);
        Ok(serde_json::from_reader(reader)?)
    }
    fn from_json_file(path: PathBuf) -> Result<Self, Box<dyn std::error::Error>> {
        let file = File::open(path)?;
        let reader = BufReader::new(file);
        Ok(serde_json::from_reader(reader)?)
    }
}

pub trait LoadFromFragments
where
    Self: Load + Inherit + DeserializeOwned,
{
    fn from_fragments(glob: PathBuf) -> Result<Self, Box<dyn std::error::Error>> {
        let mut glob_iter = WalkDir::new(glob)
            .max_depth(1)
            .sort_by_file_name()
            .into_iter()
            .filter_map(Result::ok)
            .filter_map(|entry| {
                std::path::Path::new(entry.file_name().to_str()?)
                    .extension()
                    .is_some_and(|ext| ext.eq_ignore_ascii_case("yml"))
                    .then_some(entry)
            });
        let first_file = glob_iter
            .next()
            .ok_or_else(|| Box::<dyn std::error::Error>::from("No files found"))?;
        let mut combined_data = Self::from_file(Some(first_file.path().to_path_buf()))?;
        for file in glob_iter {
            let file_data = Self::from_file(Some(file.path().to_path_buf()))?;
            combined_data.inherit(&file_data);
        }
        Ok(combined_data)
    }
}

#[cfg(test)]
mod tests {
    use super::Load;
    use crate::any::AnySchema;
    use crate::utils::dump::tests::{
        dump_avd_store, dump_json, dump_store_yaml, dump_xz2, dump_yaml,
    };
    use crate::utils::test_utils::{
        EOS_CLI_CONFIG_GEN_FRAGMENTS, EOS_DESIGNS_FRAGMENTS, get_test_dict_schema, get_test_store,
        get_tmp_file,
    };
    use crate::{LoadFromFragments as _, Store, resolve_schema};

    #[test]
    fn load_yaml() {
        dump_yaml();
        let file_path = get_tmp_file("test_dump.yml");
        let schema = get_test_dict_schema();
        let result = AnySchema::from_file(Some(file_path));
        assert!(result.is_ok());
        assert_eq!(result.unwrap(), schema);
    }
    #[test]
    fn load_json() {
        dump_json();
        let file_path = get_tmp_file("test_dump.json");
        let schema = get_test_dict_schema();
        let result = AnySchema::from_file(Some(file_path));
        assert!(result.is_ok());
        assert_eq!(result.unwrap(), schema);
    }
    #[test]
    fn load_xz2() {
        dump_xz2();
        let file_path = get_tmp_file("test_dump.xz2");
        let schema = get_test_dict_schema();
        let result = AnySchema::from_file(Some(file_path));
        assert!(result.is_ok());
        assert_eq!(result.unwrap(), schema);
    }
    #[test]
    fn load_store_yaml() {
        dump_store_yaml();
        let file_path = get_tmp_file("test_dump_store.yml");
        let store = get_test_store();
        let result = Store::from_file(Some(file_path));
        assert!(result.is_ok());
        assert_eq!(result.unwrap(), store);
    }
    #[test]
    pub(crate) fn load_avd_store() {
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
