// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.

use crate::{Schema, Store, any::AnySchema, resolve_ref};

// Given a data path return the schema covering this.
pub fn get_schema_from_path<'a>(
    schema: Schema,
    store: &'a Store,
    path: &'_ [String],
) -> Option<&'a AnySchema> {
    let schema_ref = get_schema_ref_from_path(schema, path);
    resolve_ref(&schema_ref, store).ok()
}

pub fn get_schema_ref_from_path(schema: Schema, path: &[String]) -> String {
    let schema_name: String = schema.into();
    let mut schema_ref = format!("{schema_name}#");
    for step in path {
        if step.parse::<usize>().is_ok() {
            schema_ref.push_str("/items");
        } else {
            schema_ref.push_str("/keys/");
            schema_ref.push_str(step);
        }
    }
    schema_ref
}
