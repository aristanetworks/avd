// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.

use pyo3::pymodule;

#[pymodule]
#[pyo3(name = "passwords")]
mod passwords {

    use pyo3::{PyResult, pyfunction};

    #[pyfunction]
    /// Computes the SHA512 crypt value for the password given the salt
    pub fn sha512_crypt(password: String, salt: String) -> PyResult<String> {
        passwords::sha512_crypt(&password, &salt).map_err(|err| {
            // Mapping our crates error to Python errors.
            match err {
                passwords::Sha512CryptError::InvalidSalt(_) => {
                    pyo3::exceptions::PyValueError::new_err(format!("{err}"))
                }
                passwords::Sha512CryptError::ShaCrypt(_) => {
                    pyo3::exceptions::PyRuntimeError::new_err(format!("{err}"))
                }
            }
        })
    }
}
