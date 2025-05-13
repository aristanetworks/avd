// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.

mod sha512crypt;

use pyo3::pymodule;

#[pymodule]
#[pyo3(name = "passwords")]
mod passwords {

    use crate::sha512crypt;
    use pyo3::{
        PyResult,
        exceptions::{PyRuntimeError, PyValueError},
        pyfunction,
    };
    use sha_crypt::CryptError;

    #[pyfunction]
    /// Computes the SHA512 crypt value for the password given the salt
    pub fn sha512_crypt(password: String, salt: String) -> PyResult<String> {
        sha512crypt::sha512_crypt(password, salt).map_err(|err: CryptError| match err {
            CryptError::RoundsError => {
                PyValueError::new_err("Invalid number of rounds specified for SHA512 crypt.")
            }
            CryptError::StringError(utf8_err) => PyValueError::new_err(format!(
                "String encoding error during SHA512 crypt (UTF-8 conversion failed): {}",
                utf8_err
            )),
            CryptError::RandomError => PyRuntimeError::new_err(
                "A random number generation error occurred during SHA512 crypt.",
            ),
        })
    }
}
