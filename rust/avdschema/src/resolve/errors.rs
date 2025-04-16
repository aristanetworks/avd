// Copyright (c) 2025 Arista Networks, Inc.
// Use of this source code is governed by the Apache License 2.0
// that can be found in the LICENSE file.

use crate::store::SchemaStoreError;

use super::walker::SchemaWalkError;

// Errors in this file are returned by SchemaResolve.
// Other utilities using SchemaResolve may also return these wrapped in their own Enums.

#[derive(Debug, derive_more::Display, derive_more::From)]
pub enum SchemaResolverError {
    SchemaType(SchemaType),
    RefSyntax(RefSyntax),
    SchemaPath(SchemaPath),
    SchemaStoreError(SchemaStoreError),
    SchemaWalkError(SchemaWalkError),
}

#[derive(Debug, derive_more::Constructor)]
pub struct SchemaType {
    pub schema_ref: String,
    pub expected: String,
    pub found: String,
}
impl std::fmt::Display for SchemaType {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(
            f,
            "Invalid schema type '{}' found in $ref '{}'. Expected '{}'.",
            self.found, self.schema_ref, self.expected
        )
    }
}

#[derive(Debug, derive_more::Constructor)]
pub struct RefSyntax {
    pub schema_ref: String,
}
impl std::fmt::Display for RefSyntax {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "Invalid syntax for schema $ref '{}'.", self.schema_ref)
    }
}

#[derive(Debug, derive_more::Constructor)]
pub struct SchemaPath {
    pub path: String,
}
impl std::fmt::Display for SchemaPath {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "Schema $ref path '{}' was not found.", self.path)
    }
}
