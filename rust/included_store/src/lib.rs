// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.
#![deny(unused_crate_dependencies)]

// Added here to avoid being detected as unused during testing and linting.
use avdschema_macros as _;

use std::sync::LazyLock;

use avdschema::{Load as _, Store};

// Avoid triggering the expensive macro during testing and linting.
#[cfg(not(test))]
const INCLUDED_STORE_XZ2_BYTES: &[u8] = include_bytes!(avdschema_macros::include_avd_schemas!());

#[cfg(test)]
const INCLUDED_STORE_XZ2_BYTES: &[u8] = &[];

pub fn get_store() -> Store {
    Store::from_xz2_bytes(INCLUDED_STORE_XZ2_BYTES).unwrap()
}

pub static STORE: LazyLock<Store> = LazyLock::new(get_store);
