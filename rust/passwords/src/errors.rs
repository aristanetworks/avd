// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.

#[derive(Debug, derive_more::Display, derive_more::From)]
pub enum Sha512CryptError {
    // The errors from sha_crypt library should never happen in our case.
    #[display("SHA crypt library error: {_0:?}")]
    ShaCrypt(sha_crypt::CryptError),
    #[display("Invalid Salt: {_0}")]
    InvalidSalt(InvalidSaltError),
}

// Mapping our crates error to Python errors.
impl From<Sha512CryptError> for pyo3::PyErr {
    fn from(value: Sha512CryptError) -> Self {
        match value {
            Sha512CryptError::InvalidSalt(_) => {
                pyo3::exceptions::PyValueError::new_err(format!("{value}"))
            }
            Sha512CryptError::ShaCrypt(_) => {
                pyo3::exceptions::PyRuntimeError::new_err(format!("{value}"))
            }
        }
    }
}

#[derive(Debug, derive_more::Display)]
pub enum InvalidSaltError {
    #[display("Salt cannot be empty.")]
    IsEmpty,
    #[display("Salt contains an invalid character: '{_0}'")]
    InvalidCharacter(char),
}
