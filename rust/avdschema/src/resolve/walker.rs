// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.

use std::iter::Peekable;

use ordermap::OrderMap;

use crate::{any::AnySchema, dict::Dict, list::List};

pub(crate) trait Walker {
    fn walk<'a, I>(&self, path: Peekable<I>) -> Result<&AnySchema, Box<dyn std::error::Error>>
    where
        I: Iterator<Item = &'a str> + std::fmt::Debug;
}
impl Walker for List {
    fn walk<'a, I>(&self, mut path: Peekable<I>) -> Result<&AnySchema, Box<dyn std::error::Error>>
    where
        I: Iterator<Item = &'a str> + std::fmt::Debug,
    {
        match path.next() {
            Some("items") => match &self.items {
                Some(schema) => schema.walk(path),
                None => Err("Invalid path 'items'".into()),
            },
            Some(value) => Err(format!("Invalid path {value:?}").into()),
            None => Err("Internal error. AnySchema should have returned the schema.".into()),
        }
    }
}
impl Walker for OrderMap<String, AnySchema> {
    fn walk<'a, I>(&self, mut path: Peekable<I>) -> Result<&AnySchema, Box<dyn std::error::Error>>
    where
        I: Iterator<Item = &'a str> + std::fmt::Debug,
    {
        match path.next() {
            Some(key) => match self.get(key) {
                Some(value) => value.walk(path),
                None => Err(format!("Invalid path '{key}'").into()),
            },
            None => Err("Schema ref cannot point to 'keys'.".into()),
        }
    }
}
impl Walker for Dict {
    fn walk<'a, I>(&self, mut path: Peekable<I>) -> Result<&AnySchema, Box<dyn std::error::Error>>
    where
        I: Iterator<Item = &'a str> + std::fmt::Debug,
    {
        match path.next() {
            Some("keys") => {
                if let Some(ref keys) = self.keys {
                    keys.walk(path)
                } else {
                    Err("Invalid path 'keys'".into())
                }
            }
            Some("dynamic_keys") => {
                if let Some(ref dynamic_keys) = self.dynamic_keys {
                    dynamic_keys.walk(path)
                } else {
                    Err("Invalid path 'dynamic_keys'".into())
                }
            }
            Some("$defs") => {
                if let Some(ref schema_defs) = self.schema_defs {
                    schema_defs.walk(path)
                } else {
                    Err("Invalid path '$defs'".into())
                }
            }
            Some(value) => Err(format!("Invalid path {value:?}").into()),
            None => Err("Internal error. AnySchema should have returned the schema.".into()),
        }
    }
}
impl Walker for AnySchema {
    fn walk<'a, I>(&self, mut path: Peekable<I>) -> Result<&AnySchema, Box<dyn std::error::Error>>
    where
        I: Iterator<Item = &'a str> + std::fmt::Debug,
    {
        if path.peek().is_none() {
            return Ok(self);
        }
        match self {
            AnySchema::List(schema) => schema.walk(path),
            AnySchema::Dict(schema) => schema.walk(path),
            _ => Err(format!("Invalid path {path:?}").into()),
        }
    }
}
