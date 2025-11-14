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

#[derive(Debug, derive_more::Constructor, derive_more::Display)]
#[display("Invalid schema type '{found}' found in $ref '{schema_ref}'. Expected '{expected}'.")]
pub struct SchemaType {
    pub schema_ref: String,
    pub expected: String,
    pub found: String,
}

#[derive(Debug, derive_more::Constructor, derive_more::Display)]
#[display("Invalid syntax for schema $ref '{schema_ref}'.")]
pub struct RefSyntax {
    pub schema_ref: String,
}

#[derive(Debug, derive_more::Constructor, derive_more::Display)]
#[display("Schema $ref path '{path}' was not found.")]
pub struct SchemaPath {
    pub path: String,
}
