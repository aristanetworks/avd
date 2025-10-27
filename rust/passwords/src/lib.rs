// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.

mod errors;
mod sha512crypt;

pub use sha512crypt::sha512_crypt;
pub use errors::{InvalidSaltError, Sha512CryptError};
