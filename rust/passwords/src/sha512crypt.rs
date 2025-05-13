// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.

use sha_crypt::{CryptError, Sha512Params, sha512_crypt_b64};

pub fn sha512_crypt(password: String, salt: String) -> Result<String, CryptError> {
    // Setting rounds to 5000 which is the default for sha512crypt
    let params = Sha512Params::new(5_000).expect("Could not instantiate Sha512Params.");

    // Hash the password
    let hashed_password = sha512_crypt_b64(password.as_bytes(), salt.as_bytes(), &params)
        .expect("Failed to compute sha512 password.");

    let mut result = format!("$6${salt}${hashed_password}");
    Ok(result)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn custom_salt_ok() {
        let salt = "1234567890ABCDEF";
        let password = "LittleDropBobbyTable";

        let hash = sha512_crypt(password.to_string(), salt.to_string()).unwrap();
        assert_eq!(
            hash,
            "$6$1234567890ABCDEF$Em9R7hgj77mOWT2JjGxPzUQEXpe0HmEpcxlhR5W.cMjg48.AJ1L3qFxTKuvXdmsiisbVh04tvKKH1ab.15PaD1"
        );
    }
}
