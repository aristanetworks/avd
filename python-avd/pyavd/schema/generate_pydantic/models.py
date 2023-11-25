# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from abc import ABC, abstractmethod
from textwrap import indent, wrap

import isort
from pydantic import BaseModel

PYDANTIC_SRC_HEADER = """\
# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

"""
BASE_IMPORTS = """\
from __future__ import annotations
from pydantic import BaseModel, ConfigDict, Field
"""
BASE_MODEL_NAME = "BaseModel"


class PydanticFieldSrc(BaseModel):
    """
    Dataclass containing the elements to generate Python source code for one Pydantic field.

    Use str() on the instance to render the source code.
    """

    name: str
    type_hints: list[FieldTypeHintSrc]
    description: str | None = None
    optional: bool = True
    default_value: str | None = None

    def __str__(self) -> str:
        """
        Render source code for one field like:
        myfield: str | None = Field(None, pattern="^[a-z]+")
        """

        # Build union of multiple type hints
        type_hints = " | ".join(str(type_hint) for type_hint in self.type_hints)
        if self.optional and "None" not in self.type_hints:
            type_hints += " | None"
        field_src = f"{self.name}: {type_hints}"

        if self.optional or self.default_value is not None:
            field_src += f" = {self.default_value}"

        if self.description:
            # Build docstring styled description
            description = "\n".join(wrap(self.description, width=120, replace_whitespace=False))
            field_src += f'\n"""\n{description}\n"""'

        return field_src

    def get_imports(self) -> set:
        imports = set()
        for type_hint in self.type_hints:
            imports.update(type_hint.get_imports())
        return imports


class PydanticModelSrc(BaseModel):
    """
    Dataclass containing the elements to generate Python source code for this class including any nested classes and fields.
    Can have nested classes and fields.

    Use str() on the instance to render the source code.
    """

    name: str
    classes: list[PydanticModelSrc]
    fields: list[PydanticFieldSrc]
    imports: set[str] | None = None
    base_classes: list[str] | None = None
    description: str | None = None
    allow_extra: bool = False

    def __str__(self) -> str:
        """
        Renders the Python source code for this class including any nested classes and fields.
        """
        base_classes = ", ".join(self.base_classes or [BASE_MODEL_NAME])
        if BASE_MODEL_NAME not in base_classes:
            base_classes += f", {BASE_MODEL_NAME}"

        classsrc = f"class {self.name}({base_classes}):\n"

        if self.description:
            # Build docstring styled description
            description = "\n".join(wrap(self.description, width=120, replace_whitespace=False))
            classsrc += indent(f'"""\n{description}\n"""\n', "    ")

        # Pydantic config option to forbid keys in the inputs that are not covered by the model
        model_config_args = ["defer_build=True"]
        if not self.allow_extra:
            model_config_args.append('extra="forbid"')
        if model_config_args:
            classsrc += indent(f"model_config = ConfigDict({', '.join(model_config_args)})\n\n", "    ")

        if classes := self._render_classes():
            classsrc += f"{classes}\n"

        if fields := self._render_fields():
            classsrc += f"{fields}\n"

        if not classes and not fields:
            classsrc += "    pass\n"

        return classsrc

    def _render_classes(self) -> str:
        return indent("\n".join(str(cls) for cls in self.classes), "    ")

    def _render_fields(self) -> str:
        return indent("\n".join(str(field) for field in self.fields), "    ")

    def get_imports(self) -> set:
        """
        Returns Python import statements required for this class including any nested classes and fields.
        """
        imports = self.imports or set()
        for cls in self.classes:
            imports.update(cls.get_imports())
        for field in self.fields:
            imports.update(field.get_imports())
        return imports


class PydanticSrcData(BaseModel):
    """
    Dataclass contaning a field and an associated class for one schema field including child fields.
    """

    field: PydanticFieldSrc | None = None
    """
    field should be set on all instanced except for the root model
    """

    cls: PydanticModelSrc | None = None
    """
    cls is a full BaseModel for a 'dict' field.
    """


class PydanticFileSrc(BaseModel):
    """
    Dataclass containing the elements to generate Python source code for this file.

    Use str() on the instance to render the source code.
    """

    classes: list[PydanticModelSrc]

    def __str__(self) -> str:
        """
        Returns Python source code for this file.
        """
        src = f"{PYDANTIC_SRC_HEADER}"
        src += f"{isort.code(BASE_IMPORTS + self._render_imports())}\n\n"
        src += self._render_classes()
        return src

    def _render_classes(self) -> str:
        return "\n\n".join(str(cls) for cls in self.classes)

    def _render_imports(self) -> set:
        imports = set()
        for cls in self.classes:
            imports.update(cls.get_imports())

        return "\n".join(str(imp) for imp in imports)
        # return "\n".join(set().union(cls.get_imports() for cls in self.classes))


class AnnotationSrc(BaseModel, ABC):
    """
    Base class for generating python source code for one annotation.
    Subclasses must implement __str__() and get_imports().
    """

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def get_imports(self) -> set:
        pass


class FieldTypeHintSrc(AnnotationSrc):
    """
    Dataclass containing the type and any annotations for one dataclass field.
    The annotations can either be a string, a subclass of AnnotationSrc or another FieldAnnotationSrc.
    For field_type=="list" there list_item_type can be a string or another FieldTypeHintSrc.
    """

    field_type: str
    list_item_type: str | FieldTypeHintSrc | None = None
    annotations: list[str | AnnotationSrc] | None = None

    def __str__(self) -> str:
        """
        Returns Python source code for type hint and optional annotation for one dataclass field

        If there are types but no annotations given it will render "<type1> | <type2>"
        If there are annotations as well as types it will render "Annotated[<type1> | <type2>, <annotation1>, <annotation2>]"
        If there are nested annotations it could look like "Annotated[<type>, Annotated[<nested_type>, <nested_annotation>]]"
        """
        if self.field_type == "list":
            field_type = f"list[{self.list_item_type}]"
        else:
            field_type = self.field_type

        if not self.annotations:
            return field_type

        return f"Annotated[{field_type}, {', '.join(str(annotation) for annotation in self.annotations)}]"

    def get_imports(self) -> set:
        """
        Returns Python import statements required for this type hints and annotations.
        """
        imports = set()
        if self.field_type == "list" and self.list_item_type in [None, "Any"]:
            imports.add("from typing import Any")

        if "Literal[" in self.field_type:
            imports.add("from typing import Literal")

        if not self.annotations:
            return imports

        imports.add("from typing_extensions import Annotated")
        for annotation in self.annotations:
            if isinstance(annotation, AnnotationSrc):
                imports.update(annotation.get_imports())

        return imports


class StrConvertSrc(AnnotationSrc):
    """
    Dataclass containing the inputs for generating python source code for one "StrConvert" annotation.
    """

    convert_types: list[str] | None = None
    to_lower: bool = False

    def __str__(self) -> str:
        """
        Returns python source code for one StrConverter annotation
        Like "StrConvert(convert_types=(int), to_lower=True)"
        """
        args = []
        if self.convert_types:
            # Building argument like "convert_type=(float, int)"
            args.append(f"convert_types=({', '.join(self.convert_types)})")
        if self.to_lower:
            args.append("to_lower=True")

        return f"StrConvert({', '.join(args)})"

    def __bool__(self) -> bool:
        return bool(self.convert_types or self.to_lower)

    def get_imports(self) -> set:
        return {"from .types import StrConvert"}


class IntConvertSrc(AnnotationSrc):
    """
    Dataclass containing the inputs for generating python source code for one "IntConvert" annotation.
    """

    convert_types: list[str] | None = None

    def __str__(self) -> str:
        """
        Returns python source code for one IntConverter annotation
        Like "IntConvert(convert_types=(int))"
        """
        args = []
        if self.convert_types:
            # Building argument like "convert_type=(float, str)"
            args.append(f"convert_types=({', '.join(self.convert_types)})")

        return f"IntConvert({', '.join(args)})"

    def __bool__(self) -> bool:
        return bool(self.convert_types)

    def get_imports(self) -> set:
        return {"from .types import IntConvert"}


class BoolConvertSrc(AnnotationSrc):
    """
    Dataclass containing the inputs for generating python source code for one "BoolConvert" annotation.
    """

    convert_types: list[str] | None = None

    def __str__(self) -> str:
        """
        Returns python source code for one BoolConverter annotation
        Like "BoolConvert(convert_types=(int))"
        """
        args = []
        if self.convert_types:
            # Building argument like "convert_type=(int, str)"
            args.append(f"convert_types=({', '.join(self.convert_types)})")

        return f"BoolConvert({', '.join(args)})"

    def __bool__(self) -> bool:
        return bool(self.convert_types)

    def get_imports(self) -> set:
        return {"from .types import BoolConvert"}
