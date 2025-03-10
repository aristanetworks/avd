// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.
#![deny(unused_crate_dependencies)]

/// The full AVD schema is pre-compiled into this crate as a bytestream of XZ2 compressed JSON.
/// Include it from various bindings and cache it with OnceLock like:
/// ```
/// use included_store::get_store as get_included_store;
///
/// static STORE: OnceLock<Store> = OnceLock::new();
///
/// fn get_store() -> &'static Store {
///     STORE.get_or_init(get_included_store)
/// }
/// ```
// Added here to avoid it being deemed unused during testing and linting.
use log::info;

use avdschema::{Load as _, Store};
use avdschema_macros as _;

// Avoid triggering the expensive macro during testing and linting.
#[cfg(not(test))]
const INCLUDED_STORE_XZ2_BYTES: &[u8] = include_bytes!(avdschema_macros::include_avd_schemas!());

#[cfg(test)]
const INCLUDED_STORE_XZ2_BYTES: &[u8] = &[];

pub fn get_store() -> Store {
    Store::from_xz2_bytes(INCLUDED_STORE_XZ2_BYTES)
        .inspect(|_| info!("Initialized the schema store from builtin schemas."))
        .unwrap()
}
