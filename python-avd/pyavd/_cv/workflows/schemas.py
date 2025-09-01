# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING, Literal

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator

if TYPE_CHECKING:
    from typing_extensions import Self


class StaticConfigurationBaseModel(BaseModel):
    """Common settings for all StaticConfiguration models."""

    model_config = ConfigDict(extra="forbid", frozen=True)


class StaticConfigurationConfiglet(StaticConfigurationBaseModel):
    """A configlet to be applied to one or many containers."""

    name: str
    file: Path

    @field_validator("file", mode="after")
    @classmethod
    def check_if_file_exists(cls, file: Path) -> Path:
        """Check if the provided file path exists."""
        if not file.is_file():
            msg = f"Configlet {file.resolve()} not found."
            raise ValueError(msg)
        return file


class StaticConfigurationContainer(StaticConfigurationBaseModel):
    """
    A container in the hierarchy, which applies configlets to devices matching a query.

    Containers are recursive, allowing for a nested hierarchy.
    """

    name: str
    description: str | None = None
    device_tag: str
    match_policy: Literal["match_all", "match_first"] = "match_all"
    configlets: tuple[StaticConfigurationConfiglet, ...] = Field(default_factory=tuple)
    sub_containers: tuple[StaticConfigurationContainer, ...] = Field(default_factory=tuple)

    @model_validator(mode="after")
    def check_for_duplicate_sub_container_names(self) -> Self:
        """Validate that all sub-containers have unique names."""
        if self.sub_containers:
            _validate_unique_sibling_names(self.sub_containers, parent_name_for_error=self.name)
        return self


class StaticConfigurationHierarchy(StaticConfigurationBaseModel):
    """
    The root model for defining the static configuration hierarchy.

    This model is the top-level key that must be defined in an input YAML file
    to describe the desired container and configlet structure in CloudVision.

    To promote an unambiguous and maintainable configuration, this model enforces strict uniqueness:
        - Sibling containers (those under the same parent) must have unique names.
        - All configlet names must be unique across the entire hierarchy.

    While CloudVision can handle duplicate names internally (by generating different IDs for each),
    this model treats them as a validation error to prevent user confusion and ensure a declarative structure.

    TODO: Add an example.
    """

    containers: tuple[StaticConfigurationContainer, ...]

    @model_validator(mode="after")
    def check_for_duplicate_container_names(self) -> Self:
        """Validate that all top-level containers have unique names."""
        if self.containers:
            _validate_unique_sibling_names(self.containers, parent_name_for_error="top-level hierarchy")
        return self

    @model_validator(mode="after")
    def check_for_duplicate_configlet_names(self) -> Self:
        """Validate that all configlets defined throughout the hierarchy have unique names."""
        seen_configlets: dict[str, Path] = {}
        duplicated_configlet_names: set[str] = set()

        def traverse(containers_to_scan: tuple[StaticConfigurationContainer, ...]) -> None:
            for container in containers_to_scan:
                for configlet in container.configlets:
                    if configlet.name in seen_configlets:
                        # If the name exists but the file path is different, it's a conflict.
                        if seen_configlets[configlet.name] != configlet.file:
                            duplicated_configlet_names.add(configlet.name)
                    else:
                        # If this is the first time we see this name, record it.
                        seen_configlets[configlet.name] = configlet.file

                # Recurse into sub-containers.
                if container.sub_containers:
                    traverse(container.sub_containers)

        # Start the traversal from the top-level containers.
        traverse(self.containers)

        if duplicated_configlet_names:
            sorted_duplicates = ", ".join(sorted(duplicated_configlet_names))
            name_str = "name" if len(duplicated_configlet_names) == 1 else "names"
            msg = (
                f"Configuration error: The hierarchy contains configlets with the duplicate {name_str}: "
                f"{sorted_duplicates}. All configlet names must be unique throughout the entire hierarchy."
            )
            raise ValueError(msg)

        return self


def _validate_unique_sibling_names(containers: tuple[StaticConfigurationContainer, ...], parent_name_for_error: str) -> None:
    """Check for duplicate names in a list of sibling containers."""
    seen_names: set[str] = set()
    duplicated_container_names: set[str] = set()

    for container in containers:
        if container.name in seen_names:
            duplicated_container_names.add(container.name)
        seen_names.add(container.name)

    if duplicated_container_names:
        sorted_duplicates = ", ".join(sorted(duplicated_container_names))
        name_str = "name" if len(duplicated_container_names) == 1 else "names"
        msg = (
            f"Configuration error in {parent_name_for_error}: "
            f"It contains containers with the duplicate {name_str}: {sorted_duplicates}. "
            "Sibling containers must have unique names."
        )
        raise ValueError(msg)
