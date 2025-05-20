// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.

use sha_crypt::{Sha512Params, sha512_crypt_b64};

use crate::errors::{InvalidSaltError, Sha512CryptError};

pub fn sha512_crypt(password: &str, salt: &str) -> Result<String, Sha512CryptError> {
    // Setting rounds to 5000 which is the default for sha512crypt
    let params = Sha512Params::new(5_000)?;

    // Validate Salt
    validate_salt_characters(salt)?;

    // Hash the password
    let hashed_password = sha512_crypt_b64(password.as_bytes(), salt.as_bytes(), &params)?;
    Ok(format!("$6${salt}${hashed_password}"))
}

/// Verify that the salt is only composed of valid characters: [a-zA-Z0-9/.]
fn validate_salt_characters(s: &str) -> Result<(), InvalidSaltError> {
    if s.is_empty() {
        return Err(InvalidSaltError::IsEmpty);
    }

    for c in s.chars() {
        if !(c.is_ascii_alphanumeric() || c == '/' || c == '.') {
            return Err(InvalidSaltError::InvalidCharacter(c));
        }
    }

    Ok(())
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn valid_salt() {
        let salt = "1234567890ABCDEF";
        let password = "LittleDropBobbyTable";

        let result = sha512_crypt(password, salt).unwrap();
        assert_eq!(
            result,
            "$6$1234567890ABCDEF$Em9R7hgj77mOWT2JjGxPzUQEXpe0HmEpcxlhR5W.cMjg48.AJ1L3qFxTKuvXdmsiisbVh04tvKKH1ab.15PaD1",
            "Incorrect hash returned."
        );
    }

    #[test]
    fn invalid_salt_bad_characters() {
        // invalid characters
        let salt = "🦀$;";
        let password = "LittleDropBobbyTable";

        let result = sha512_crypt(password, salt).unwrap_err();
        assert!(matches!(
            result,
            Sha512CryptError::InvalidSalt(InvalidSaltError::InvalidCharacter('🦀'))
        ));
    }

    #[test]
    fn invalid_salt_empty() {
        // empty salt
        let salt = "";
        let password = "LittleDropBobbyTable";

        let result = sha512_crypt(password, salt).unwrap_err();

        assert!(matches!(
            result,
            Sha512CryptError::InvalidSalt(InvalidSaltError::IsEmpty)
        ));
    }
}
