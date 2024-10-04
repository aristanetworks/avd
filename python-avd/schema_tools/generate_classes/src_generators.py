# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from textwrap import indent, wrap
from typing import Any

from schema_tools.constants import LICENSE_HEADER

SRC_HEADER = indent(LICENSE_HEADER + "\n\n", "# ")

BASE_IMPORTS = """\
from pyavd._schema.models import AvdBase
"""
BASE_MODEL_NAME = "AvdBase"


@dataclass
class FieldSrc:
    """
    Dataclass containing the elements to generate Python source code for one field.

    Use str() on the instance to render the source code.
    """

    name: str
    type_hints: list[FieldTypeHintSrc]
    description: str | None = None
    optional: bool = True
    default_value: str | None = None

    def __str__(self) -> str:
        """
        Render source code for one field.

        myfield: str | None = field(None, pattern="^[a-z]+")
        """
        # Build union of multiple type hints
        type_hints = " | ".join(str(type_hint) for type_hint in self.type_hints)
        if self.optional and "None" not in self.type_hints:
            type_hints += " | None"
        field_src = f"{self.name}: {type_hints}"

        if self.optional or self.default_value is not None:
            field_src += f" = {self.default_value}"

        return field_src

    def _docstring(self) -> str:
        if not self.description:
            return ""

        docstring = "\n".join(wrap(self.description, width=100, replace_whitespace=False))
        return f"{docstring}\n"

    def get_imports(self) -> set:
        imports = set()
        for type_hint in self.type_hints:
            imports.update(type_hint.get_imports())
        return imports


@dataclass
class ModelSrc:
    """
    Dataclass containing the elements to generate Python source code for this class including any nested classes and fields.

    Can have nested classes and fields.

    Use str() on the instance to render the source code.
    """

    name: str
    classes: list[ModelSrc]
    fields: list[FieldSrc]
    imports: set[str] | None = None
    base_classes: list[str] | None = None
    description: str | None = None
    allow_extra: bool = False

    def __str__(self) -> str:
        """Renders the Python source code for this class including any nested classes and fields."""
        base_classes = ", ".join(self.base_classes) if self.base_classes else BASE_MODEL_NAME

        classsrc = f"class {self.name}({base_classes}):\n" if base_classes else f"class {self.name}:\n"

        if self.description:
            description = "\n".join(wrap(self.description, width=100, replace_whitespace=False))
            if "\n" in description:
                classsrc += indent(f'"""\n{description.strip()}\n"""\n', "    ")
            else:
                classsrc += indent(f'"""{description}"""\n', "    ")

        if classes := self._render_classes():
            classsrc += f"{classes}\n"

        if fields := self._render_fields():
            classsrc += f"{fields}\n"

        if not classes and not fields:
            classsrc += "    pass\n"

        return classsrc

    def _init_docstring(self) -> str:
        docstring_elements = [f"{self.name}.\n"]
        if self.description:
            # Build docstring styled description
            docstring_elements.append("\n".join(wrap(self.description, width=100, replace_whitespace=False)))

        if self.fields:
            args = "Args:\n-----\n"
            for field in self.fields:
                field_arg = f"{field.name}"
                if field.description:
                    description = "\n".join(wrap(field.description, width=100, replace_whitespace=False))
                    if "\n" in description:
                        field_arg += f":\n{indent(description, '   ')}"
                    else:
                        field_arg += f": {description}"
                else:
                    field_arg += f": {field.name}"
                args += indent(field_arg, "    ")
                args += "\n"

            docstring_elements.append(args)

        if docstring_elements:
            docstring_content = "\n\n".join(docstring_elements)
            return indent(f'"""\n{docstring_content}\n"""\n', "    ")
        return ""

    def _render_classes(self) -> str:
        if not self.classes:
            return ""

        return indent("\n".join(str(cls) for cls in self.classes), "    ")

    def _render_fields(self) -> str:
        if not self.fields:
            return ""

        field_names_as_strings = tuple(f'"{field.name}"' for field in self.fields)

        extra_comma = "," if len(field_names_as_strings) == 1 else ""
        src = f"    _fields = ({', '.join(field_names_as_strings)}{extra_comma})\n"
        required_field_names_as_strings = tuple(f'"{field.name}"' for field in self.fields if not field.optional and field.default_value is None)

        extra_comma = "," if len(required_field_names_as_strings) == 1 else ""
        src += f"    _required_fields = ({', '.join(required_field_names_as_strings)}{extra_comma})\n"

        if self.allow_extra:
            src += "    _allow_other_keys = True\n"
        if not self.fields:
            return src

        for field in self.fields:
            src += indent(f"{field!s}\n", "    ")
            if docstring := field._docstring().strip():
                multiline = ""
                if "\n" in docstring:
                    multiline = "\n"
                src += indent(f'"""{multiline}{docstring}{multiline}"""\n', "    ")

        if self.base_classes == ["object"]:
            # This is some internal class so we don't need __init__
            return src

        field_as_args = ["self", "*", *(str(field).split("\n", maxsplit=1)[0] for field in self.fields)]
        if self.allow_extra:
            field_as_args.append("**kwargs: Any")
        src += indent(f"\n\ndef __init__({', '.join(field_as_args)}) -> None:\n", "    ")
        src += indent(self._init_docstring(), "    ")
        src += "        for arg, arg_value in locals().items():\n"
        src += '            if arg in ("self", "kwargs"):\n'
        src += "                continue\n"
        src += "            setattr(self, arg, arg_value)\n"
        return src

    def get_imports(self) -> set:
        """Returns Python import statements required for this class including any nested classes and fields."""
        imports = self.imports or set()
        if self.allow_extra:
            imports.add("from typing import Any")
        for cls in self.classes:
            imports.update(cls.get_imports())
        for field in self.fields:
            imports.update(field.get_imports())
        return imports


@dataclass
class SrcData:
    """Dataclass containing a field and an associated class for one schema field including child fields."""

    field: FieldSrc | None = None
    """
    field should be set on all instanced except for the root model
    """

    cls: ModelSrc | None = None
    """
    cls is a full Model for a 'dict' field.
    """


@dataclass
class FileSrc:
    """
    Dataclass containing the elements to generate Python source code for this file.

    Use str() on the instance to render the source code.
    """

    classes: list[ModelSrc]

    def __str__(self) -> str:
        """Returns Python source code for this file."""
        src = f"{SRC_HEADER}"
        src += f"{BASE_IMPORTS + self._render_imports()}\n\n"
        src += self._render_classes()
        return src.rstrip() + "\n"

    def _render_classes(self) -> str:
        return "\n\n".join(str(cls) for cls in self.classes)

    def _render_imports(self) -> set:
        imports = set()
        for cls in self.classes:
            imports.update(cls.get_imports())
        return "\n".join(str(imp) for imp in imports)


@dataclass
class AnnotationSrc(ABC):
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


@dataclass
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
        Returns Python source code for type hint and optional annotation for one dataclass field.

        If there are types but no annotations given it will render "<type1> | <type2>"
        If there are annotations as well as types it will render "Annotated[<type1> | <type2>, <annotation1>, <annotation2>]"
        If there are nested annotations it could look like "Annotated[<type>, Annotated[<nested_type>, <nested_annotation>]]"
        """
        field_type = f"{self.field_type}[{self.list_item_type}]" if self.field_type in ("list", "tuple") else self.field_type

        if not self.annotations:
            return field_type

        return f"Annotated[{field_type}, {', '.join(str(annotation) for annotation in self.annotations)}]"

    def get_imports(self) -> set:
        """Returns Python import statements required for this type hints and annotations."""
        imports = set()
        if self.field_type == "list" and self.list_item_type in [None, "Any"]:
            imports.add("from typing import Any")

        if "Literal[" in self.field_type:
            imports.add("from typing import Literal")

        if not self.annotations:
            return imports

        imports.add("from typing import Annotated")
        for annotation in self.annotations:
            if isinstance(annotation, AnnotationSrc):
                imports.update(annotation.get_imports())

        return imports


@dataclass
class FormatSrc(AnnotationSrc):
    format: str

    def __str__(self) -> str:
        return f"Format['{self.format}']"

    def get_imports(self) -> set:
        return {"from pyavd._schema.types import Format"}


@dataclass
class MinLenSrc(AnnotationSrc):
    min_len: int

    def __str__(self) -> str:
        return f"MinLen[{self.min_len}]"

    def get_imports(self) -> set:
        return {"from pyavd._schema.types import MinLen"}


@dataclass
class MaxLenSrc(AnnotationSrc):
    max_len: int

    def __str__(self) -> str:
        return f"MaxLen[{self.max_len}]"

    def get_imports(self) -> set:
        return {"from pyavd._schema.types import MaxLen"}


@dataclass
class MinSrc(AnnotationSrc):
    min_value: int

    def __str__(self) -> str:
        return f"Min[{self.min_value}]"

    def get_imports(self) -> set:
        return {"from pyavd._schema.types import Min"}


@dataclass
class MaxSrc(AnnotationSrc):
    max_value: int

    def __str__(self) -> str:
        return f"Max[{self.max_value}]"

    def get_imports(self) -> set:
        return {"from pyavd._schema.types import Max"}


@dataclass
class PatternSrc(AnnotationSrc):
    pattern: str

    def __str__(self) -> str:
        return f'Pattern[r"{self.pattern}"]'

    def get_imports(self) -> set:
        return {"from pyavd._schema.types import Pattern"}


@dataclass
class LowerSrc(AnnotationSrc):
    def __str__(self) -> str:
        return "Lower"

    def get_imports(self) -> set:
        return {"from pyavd._schema.types import Lower"}


@dataclass
class ValidValuesSrc(AnnotationSrc):
    valid_values: list[Any]

    def __str__(self) -> str:
        valid_values = [self.quote_string(valid_value) for valid_value in self.valid_values]
        return f"ValidValues[{', '.join(valid_values)}]"

    @staticmethod
    def quote_string(value: Any) -> Any:
        if isinstance(value, str):
            value = f"'{value}'"
        return str(value)

    def get_imports(self) -> set:
        return {"from pyavd._schema.types import ValidValues"}
