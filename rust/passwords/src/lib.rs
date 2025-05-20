// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.

mod errors;
mod sha512crypt;

use pyo3::pymodule;

#[pymodule]
#[pyo3(name = "passwords")]
mod passwords {

    use crate::sha512crypt;
    use pyo3::{PyResult, pyfunction};

    #[pyfunction]
    /// Computes the SHA512 crypt value for the password given the salt
    pub fn sha512_crypt(password: String, salt: String) -> PyResult<String> {
        Ok(sha512crypt::sha512_crypt(&password, &salt)?)
    }
}
