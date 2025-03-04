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
                Some("snappy") => Self::from_snappy_file(path),
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
    fn from_snappy_file(path: PathBuf) -> Result<Self, Box<dyn std::error::Error>> {
        let file = File::open(path)?;
        let snapped = snap::read::FrameDecoder::new(file);
        let reader = BufReader::new(snapped);
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
