// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.
#![deny(unused_crate_dependencies)]

mod inherit;
mod resolve;
mod schema;
mod store;
mod utils;

#[cfg(feature = "dump_load_files")]
pub use self::utils::load::LoadFromFragments;
pub use self::{
    inherit::Inherit, resolve::resolve_ref::resolve_ref, resolve::resolve_schema, schema::any,
    schema::base, schema::boolean, schema::dict, schema::int, schema::list, schema::str,
    store::Schema, store::Store, utils::dump::Dump,
    utils::load::Load, utils::schema_from_path::SchemaKeys,
    utils::schema_from_path::get_schema_from_path, utils::walker::Walker,
};
