# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
# Including docstrings since that is why we want this. Also allowing bad name style to match pyo3 output.
# ruff: noqa: PYI021, N801
from pathlib import Path
from typing import Literal

class Feedback:
    """Feedback item carried in the Context under either `coercions` or `violations`."""

    path: list[str]
    """Data path which the feedback concerns."""

    issue: Issue_Validation | Issue_Coercion | Issue_DefaultValueInserted | Issue_InternalError

class Value_Bool(Value):
    _0: bool

class Value_Dict(Value):
    _0: dict[str, Value_Bool | Value_Dict | Value_Float | Value_Int | Value_List | Value_None | Value_Str]

class Value_Float(Value):
    _0: float

class Value_Int(Value):
    _0: int

class Value_List(Value):
    _0: list[Value_Bool | Value_Dict | Value_Float | Value_Int | Value_List | Value_None | Value_Str]

class Value_None(Value): ...

class Value_Str(Value):
    _0: str

class Value:
    """Data value reported in coercion or violation."""

    Bool = Value_Bool
    Dict = Value_Dict
    Float = Value_Float
    Int = Value_Int
    List = Value_List
    None_ = Value_None
    Str = Value_Str

class CoercionNote:
    """One coercion performed during recursive coercion."""

    found: Value_Bool | Value_Dict | Value_Float | Value_Int | Value_List | Value_None | Value_Str
    made: Value_Bool | Value_Dict | Value_Float | Value_Int | Value_List | Value_None | Value_Str

class Type_Null(Type): ...
class Type_Bool(Type): ...
class Type_Int(Type): ...
class Type_Str(Type): ...
class Type_List(Type): ...
class Type_Dict(Type): ...

class Type:
    """Type of value reported in violation."""

    Null = Type_Null
    Bool = Type_Bool
    Int = Type_Int
    Str = Type_Str
    List = Type_List
    Dict = Type_Dict

class ViolationValidValues_Bool(ViolationValidValues):
    _0: list[bool]

class ViolationValidValues_Int(ViolationValidValues):
    _0: list[int]

class ViolationValidValues_Str(ViolationValidValues):
    _0: list[str]

class ViolationValidValues:
    """List of valid values used in Violation."""

    Bool = ViolationValidValues_Bool
    Int = ViolationValidValues_Int
    Str = ViolationValidValues_Str

class Violation_LengthAboveMaximum(Violation):
    """The length is above the maximum allowed."""

    maximum: int
    found: int

class Violation_LengthBelowMinimum(Violation):
    """The length is below the minimum allowed."""

    minimum: int
    found: int

class Violation_MissingRequiredKey(Violation):
    """The dictionary key is required, but was not set."""

    key: str

class Violation_InvalidSchema(Violation):
    """The given schema name was not found in the schema store."""

    schema: str

class Violation_InvalidType(Violation):
    """The value is not of the expected type."""

    expected: Type_Null | Type_Bool | Type_Int | Type_Str | Type_List | Type_Dict
    found: Type_Null | Type_Bool | Type_Int | Type_Str | Type_List | Type_Dict

class Violation_InvalidValue(Violation):
    """The value is not among the valid values."""

    expected: ViolationValidValues_Bool | ViolationValidValues_Int | ViolationValidValues_Str
    found: Value_Bool | Value_Dict | Value_Float | Value_Int | Value_List | Value_None | Value_Str

class Violation_NotMatchingPattern(Violation):
    """The value is not matching the allowed pattern."""

    pattern: str
    found: str

class Violation_UnexpectedKey(Violation):
    """The dictionary key is not allowed by the schema."""

class Violation_ValueAboveMaximum(Violation):
    """The value is above the maximum allowed."""

    maximum: int
    found: int

class Violation_ValueBelowMinimum(Violation):
    """The value is below the minimum allowed."""

    minimum: int
    found: int

class Violation_ValueNotUnique(Violation):
    """The value is not unique as required."""

    other_path: list[str]

class Violation:
    """One violation found during recursive validation."""

    LengthAboveMaximum = Violation_LengthAboveMaximum
    LengthBelowMinimum = Violation_LengthBelowMinimum
    MissingRequiredKey = Violation_MissingRequiredKey
    InvalidSchema = Violation_InvalidSchema
    InvalidType = Violation_InvalidType
    InvalidValue = Violation_InvalidValue
    NotMatchingPattern = Violation_NotMatchingPattern
    UnexpectedKey = Violation_UnexpectedKey
    ValueAboveMaximum = Violation_ValueAboveMaximum
    ValueBelowMinimum = Violation_ValueBelowMinimum
    ValueNotUnique = Violation_ValueNotUnique

class Issue_Validation(Issue):
    """Violation found during validation."""

    _0: (
        Violation_LengthAboveMaximum
        | Violation_LengthBelowMinimum
        | Violation_MissingRequiredKey
        | Violation_InvalidSchema
        | Violation_InvalidType
        | Violation_InvalidValue
        | Violation_NotMatchingPattern
        | Violation_UnexpectedKey
        | Violation_ValueAboveMaximum
        | Violation_ValueBelowMinimum
        | Violation_ValueNotUnique
    )

class Issue_Coercion(Issue):
    """Coercion performed during coercion."""

    _0: CoercionNote

class Issue_DefaultValueInserted(Issue):
    """Default value as specified in the schema was inserted into the data."""

class Issue_InternalError(Issue):
    message: str

class Issue:
    """Issue is wrapped in Feedback and added to the Context during coercion and validation."""

    Validation = Issue_Validation
    Coercion = Issue_Coercion
    DefaultValueInserted = Issue_DefaultValueInserted
    InternalError = Issue_InternalError

class ValidationResult:
    """Result of data validation."""

    violations: list[Feedback]
    coercions: list[Feedback]

def init_store_from_fragments(eos_cli_config_gen: Path, eos_designs: Path) -> None:
    """
    Re-initialize the Schema store from Schema YAML fragments.

    This will overwrite the builtin-schema that was included in the Rust code during compilation.
    This must be called before running any validations, since the store is a write-once static.

    Args:
        eos_cli_config_gen: Path to the directory holding the schema fragments for `eos_cli_config_gen`.
        eos_designs: Path to the directory holding the schema fragments for `eos_designs`.

    Raises:
        RuntimeError: For any issue hit during loading, deserializing, combining and resolving schemas.
    """

def validate_json(data_as_json: str, schema_name: Literal["eos_cli_config_gen", "eos_designs"]) -> ValidationResult:
    """
    Validate data against a schema specified by name.

    Args:
        data_as_json: Structured data dumped as JSON.
        schema_name: The name of the schema to validate against.

    Returns:
        ValidationResult holding lists of violations and coercions as Feedback objects.
    """

def validate_json_with_adhoc_schema(data_as_json: str, schema_as_json: str) -> ValidationResult:
    """
    Validate data against the given schema.

    Args:
        data_as_json: Structured data dumped as JSON.
        schema_as_json: A fully resolved schema dumped as JSON.

    Returns:
        ValidationResult holding lists of violations and coercions as Feedback objects.
    """
