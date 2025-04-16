// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.
#![deny(unused_crate_dependencies)]

//! The full AVD schema is pre-compiled into this crate as a bytestream of GZ compressed JSON.
//! Include it from various bindings and cache it with OnceLock like:
//!
//! This is kept as a separate crate, to avoid bloating the validation crate with the full builtin schema in case that is not needed.
//! TODO: Consider moving this into the validation crate behind a feature toggle.
//!
//! ```
//! use std::sync::OnceLock;
//! use included_store::get_store as get_included_store;
//! use avdschema::Store;
//!
//! static STORE: OnceLock<Store> = OnceLock::new();
//!
//! fn get_store() -> &'static Store {
//!     STORE.get_or_init(get_included_store)
//! }
//! ```

use log::info;

use avdschema::{Load as _, Store};
use avdschema_macros as _;

// Avoid triggering the expensive macro during testing and linting.
// This also means that tests cannot rely on the included_store.
#[cfg(not(test))]
const INCLUDED_STORE_GZ: &[u8] = include_bytes!(avdschema_macros::include_avd_schemas!());

#[cfg(test)]
const INCLUDED_STORE_GZ: &[u8] = &[];

pub fn get_store() -> Store {
    Store::from_gz_bytes(INCLUDED_STORE_GZ)
        .inspect(|_| info!("Initialized the schema store from builtin schemas."))
        .unwrap()
}
