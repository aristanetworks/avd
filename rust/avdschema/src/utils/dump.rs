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
                Some("snappy") => self.to_snappy_file(path),
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
    fn to_snappy_file(&self, path: PathBuf) -> Result<(), Box<dyn std::error::Error>> {
        let file = File::create(path)?;
        let snapped = snap::write::FrameEncoder::new(file);
        let writer = BufWriter::new(snapped);
        Ok(serde_json::to_writer(writer, self)?)
    }
    fn to_json_file(&self, path: PathBuf) -> Result<(), Box<dyn std::error::Error>> {
        let file = File::create(path)?;
        let writer = BufWriter::new(file);
        Ok(serde_json::to_writer(writer, self)?)
    }
}
