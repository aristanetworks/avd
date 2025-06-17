// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.

use serde::Serialize;

#[cfg(feature = "dump_load_files")]
use std::{
    ffi::OsStr,
    fs::File,
    io::{self, BufWriter},
    path::PathBuf,
};

pub trait Dump
where
    Self: Serialize,
{
    fn to_json(&self) -> Result<String, DumpError> {
        Ok(serde_json::to_string(self)?)
    }

    #[cfg(feature = "dump_load_files")]
    fn to_file(&self, output: Option<PathBuf>) -> Result<(), DumpError> {
        // Output result to file / stdout
        match output {
            Some(path) => match path.extension().and_then(OsStr::to_str) {
                Some("yml" | "yaml") => self.to_yaml_file(path),
                Some("json") => self.to_json_file(path),
                #[cfg(feature = "xz2")]
                Some("xz2") => self.to_xz2_file(path),
                Some("gz") => self.to_gz_file(path),
                _ => Err(DumpError::InvalidExtension {}),
            },
            None => self.to_stdout(),
        }
    }
    #[cfg(feature = "dump_load_files")]
    fn to_stdout(&self) -> Result<(), DumpError> {
        let writer = io::stdout();
        Ok(serde_json::to_writer(writer, self)?)
    }
    #[cfg(feature = "dump_load_files")]
    fn to_yaml_file(&self, path: PathBuf) -> Result<(), DumpError> {
        let file = File::create(path)?;
        let writer = BufWriter::new(file);
        Ok(serde_yaml::to_writer(writer, self)?)
    }
    #[cfg(feature = "xz2")]
    fn to_xz2_file(&self, path: PathBuf) -> Result<(), DumpError> {
        let file = File::create(path)?;
        let compressor = xz2::write::XzEncoder::new(file, 1);
        let writer = BufWriter::new(compressor);
        Ok(serde_json::to_writer(writer, self)?)
    }
    #[cfg(feature = "dump_load_files")]
    fn to_json_file(&self, path: PathBuf) -> Result<(), DumpError> {
        let file = File::create(path)?;
        let writer = BufWriter::new(file);
        Ok(serde_json::to_writer(writer, self)?)
    }
    #[cfg(feature = "dump_load_files")]
    fn to_gz_file(&self, path: PathBuf) -> Result<(), DumpError> {
        let file = File::create(path)?;
        let compressor = flate2::write::GzEncoder::new(file, flate2::Compression::fast());
        let writer = BufWriter::new(compressor);
        Ok(serde_json::to_writer(writer, self)?)
    }
}

#[derive(Debug, derive_more::Display, derive_more::From)]
pub enum DumpError {
    JsonError(serde_json::Error),
    YamlError(serde_yaml::Error),
    #[cfg(feature = "dump_load_files")]
    IoError(std::io::Error),
    #[cfg(feature = "dump_load_files")]
    #[display("Invalid extension for output file.")]
    InvalidExtension {},
}

// These tests are also called from the load tests.
#[cfg(test)]
pub(crate) mod tests {
    use super::Dump;
    use crate::utils::test_utils::{get_test_dict_schema, get_test_store, get_tmp_file};

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
    #[cfg(feature = "xz2")]
    #[test]
    pub(crate) fn dump_xz2() {
        let file_path = get_tmp_file("test_dump.xz2");
        let schema = get_test_dict_schema();
        let result = schema.to_file(Some(file_path));
        assert!(result.is_ok())
    }
    #[test]
    pub(crate) fn dump_gz() {
        let file_path = get_tmp_file("test_dump.gz");
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
}
