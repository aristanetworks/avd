// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.

use serde::de::DeserializeOwned;
use std::io::BufReader;

#[cfg(feature = "dump_load_files")]
use std::{ffi::OsStr, fs::File, io, path::PathBuf};

#[cfg(feature = "dump_load_files")]
use walkdir::WalkDir;

#[cfg(feature = "dump_load_files")]
use crate::Inherit;

pub trait Load
where
    Self: DeserializeOwned,
{
    fn from_json(json: &str) -> Result<Self, LoadError> {
        Ok(serde_json::from_str(json)?)
    }

    #[cfg(feature = "dump_load_files")]
    fn from_file(input: Option<PathBuf>) -> Result<Self, LoadError> {
        // Read input from file / stdin
        match input {
            Some(path) => match path.extension().and_then(OsStr::to_str) {
                Some("yml" | "yaml") => Self::from_yaml_file(path),
                Some("json") => Self::from_json_file(path),
                #[cfg(feature = "xz2")]
                Some("xz2") => Self::from_xz2_file(path),
                Some("gz") => Self::from_gz_file(path),
                _ => Err(LoadError::InvalidExtension {}),
            },
            None => Self::from_stdin(),
        }
    }
    #[cfg(feature = "dump_load_files")]
    fn from_stdin() -> Result<Self, LoadError> {
        let reader = io::stdin();
        Ok(serde_yaml::from_reader(reader)?)
    }
    #[cfg(feature = "dump_load_files")]
    fn from_yaml_file(path: PathBuf) -> Result<Self, LoadError> {
        let file = File::open(path)?;
        let reader = BufReader::new(file);
        Ok(serde_yaml::from_reader(reader)?)
    }
    #[cfg(feature = "xz2")]
    fn from_xz2_file(path: PathBuf) -> Result<Self, LoadError> {
        let file = File::open(path)?;
        let decompressor = xz2::read::XzDecoder::new(file);
        let reader = BufReader::new(decompressor);
        Ok(serde_json::from_reader(reader)?)
    }
    #[cfg(feature = "dump_load_files")]
    fn from_json_file(path: PathBuf) -> Result<Self, LoadError> {
        let file = File::open(path)?;
        let reader = BufReader::new(file);
        Ok(serde_json::from_reader(reader)?)
    }
    #[cfg(feature = "xz2")]
    fn from_xz2_bytes(bytes: &[u8]) -> Result<Self, LoadError> {
        let decompressor = xz2::read::XzDecoder::new(bytes);
        let reader = BufReader::new(decompressor);
        Ok(serde_json::from_reader(reader)?)
    }
    #[cfg(feature = "dump_load_files")]
    fn from_gz_file(path: PathBuf) -> Result<Self, LoadError> {
        let file = File::open(path)?;
        let decompressor = flate2::read::GzDecoder::new(file);
        let reader = BufReader::new(decompressor);
        Ok(serde_json::from_reader(reader)?)
    }
    fn from_gz_bytes(bytes: &[u8]) -> Result<Self, LoadError> {
        let decompressor = flate2::read::GzDecoder::new(bytes);
        let reader = BufReader::new(decompressor);
        Ok(serde_json::from_reader(reader)?)
    }
}

#[cfg(feature = "dump_load_files")]
pub trait LoadFromFragments
where
    Self: Load + Inherit + DeserializeOwned,
{
    fn from_fragments(glob: PathBuf) -> Result<Self, LoadError> {
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
        let first_file = glob_iter.next().ok_or(LoadError::NoFilesFound {})?;
        let mut combined_data = Self::from_file(Some(first_file.path().to_path_buf()))?;
        for file in glob_iter {
            let file_data = Self::from_file(Some(file.path().to_path_buf()))?;
            combined_data.inherit(&file_data);
        }
        Ok(combined_data)
    }
}

#[derive(Debug, derive_more::Display, derive_more::From)]
pub enum LoadError {
    JsonError(serde_json::Error),
    YamlError(serde_yaml::Error),
    #[cfg(feature = "dump_load_files")]
    IoError(std::io::Error),
    #[cfg(feature = "dump_load_files")]
    #[display("Invalid extension for input file.")]
    InvalidExtension {},
    #[cfg(feature = "dump_load_files")]
    #[display("No files found.")]
    NoFilesFound {},
}

#[cfg(test)]
mod tests {
    use super::Load;
    use crate::Store;
    use crate::any::AnySchema;
    use crate::utils::test_utils::{get_test_dict_schema, get_test_store, get_tmp_file};

    #[test]
    fn load_yaml() {
        crate::utils::dump::tests::dump_yaml();
        let file_path = get_tmp_file("test_dump.yml");
        let schema = get_test_dict_schema();
        let result = AnySchema::from_file(Some(file_path));
        assert!(result.is_ok());
        assert_eq!(result.unwrap(), schema);
    }
    #[test]
    fn load_json() {
        crate::utils::dump::tests::dump_json();
        let file_path = get_tmp_file("test_dump.json");
        let schema = get_test_dict_schema();
        let result = AnySchema::from_file(Some(file_path));
        assert!(result.is_ok());
        assert_eq!(result.unwrap(), schema);
    }
    #[cfg(feature = "xz2")]
    #[test]
    fn load_xz2() {
        crate::utils::dump::tests::dump_xz2();
        let file_path = get_tmp_file("test_dump.xz2");
        let schema = get_test_dict_schema();
        let result = AnySchema::from_file(Some(file_path));
        assert!(result.is_ok());
        assert_eq!(result.unwrap(), schema);
    }
    #[test]
    fn load_gz() {
        crate::utils::dump::tests::dump_gz();
        let file_path = get_tmp_file("test_dump.gz");
        let schema = get_test_dict_schema();
        let result = AnySchema::from_file(Some(file_path));
        assert!(result.is_ok());
        assert_eq!(result.unwrap(), schema);
    }
    #[test]
    fn load_store_yaml() {
        crate::utils::dump::tests::dump_store_yaml();
        let file_path = get_tmp_file("test_dump_store.yml");
        let store = get_test_store();
        let result = Store::from_file(Some(file_path));
        assert!(result.is_ok());
        assert_eq!(result.unwrap(), store);
    }
}
