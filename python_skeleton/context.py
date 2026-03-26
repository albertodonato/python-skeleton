from pathlib import Path
import re
import tomllib
from typing import Any, Self

from packaging.version import Version
from pydantic import BaseModel, ConfigDict, model_validator
import yaml

JSONDict = dict[str, Any]


class ContextError(Exception):
    """Error in context configuration."""


class HyphenModel(BaseModel):
    """Pydantic model using dashes in keys."""

    model_config = ConfigDict(
        populate_by_name=True, alias_generator=lambda s: s.replace("_", "-")
    )


class PythonVersions(HyphenModel):
    """Python versions supported by the project."""

    min: str
    max: str

    @model_validator(mode="after")
    def validate_range(self) -> Self:
        if Version(self.min) > Version(self.max):
            raise ValueError(
                f"min version {self.min} must be <= max version {self.max}"
            )
        return self

    @property
    def supported_versions(self) -> list[str]:
        min_v = Version(self.min)
        max_v = Version(self.max)
        versions = []
        major, minor = min_v.major, min_v.minor
        while (v := Version(f"{major}.{minor}")) <= max_v:
            versions.append(str(v))
            minor += 1
        return versions


class Project(HyphenModel):
    """Project details."""

    name: str
    version: str = "0.0.1"
    package: str = ""
    title: str
    license: str = "Apache-2.0"
    urls: dict[str, str]
    python_versions: PythonVersions

    @model_validator(mode="after")
    def _default_package(self) -> Self:
        if not self.package:
            self.package = self.name.lower().replace("-", "_")
        return self


class Author(HyphenModel):
    """Project author details."""

    name: str
    email: str


class Config(HyphenModel):
    """Configuration for the generated project."""

    use_uv_lock: bool = True


class Context(BaseModel):
    """Top-level context object passed to templates."""

    project: Project
    author: Author
    config: Config


def get_context(
    project_dir: Path, project_details: Path | None = None
) -> Context:
    """Return the template context from either project details or the existing project dir."""

    if project_details:
        return _get_yaml_context(project_details)

    return _get_project_context(project_dir)


def _get_yaml_context(config_file: Path) -> Context:
    """Return the context from the YAML config file."""
    return Context.model_validate(yaml.safe_load(config_file.read_text()))


def _get_project_context(project_dir: Path) -> Context:
    """Return the context from an existing project."""

    pyproject_conf = _get_pyproject_config(project_dir / "pyproject.toml")
    project = pyproject_conf["project"]
    package = _get_pyproject_package(pyproject_conf)

    return Context(
        project=Project(
            name=project["name"],
            version=_get_project_version(project_dir, package),
            title=project["description"],
            license=project["license"],
            package=package,
            urls=project["urls"],
            python_versions=PythonVersions(
                min=project["requires-python"].lstrip(">="),
                max=_get_pyproject_max_python_version(project),
            ),
        ),
        author=Author.model_validate(project["authors"][0]),
        config=Config(
            use_uv_lock=(project_dir / "uv.lock").exists(),
        ),
    )


def _get_pyproject_config(config_file: Path) -> JSONDict:
    with config_file.open("rb") as fd:
        return tomllib.load(fd)


def _get_pyproject_package(data: JSONDict) -> str:
    package_data = _get_nested_option(
        data, "tool", "setuptools", "package-data"
    )
    if not package_data:
        raise ContextError("No package-data entry found")

    # use the first key found in the list
    return next(iter(package_data))


def _get_pyproject_max_python_version(project_data: JSONDict) -> str:
    """Return maximum Python version from classifiers."""
    entries = [
        entry
        for entry in project_data["classifiers"]
        if entry.startswith("Programming Language :: Python ::")
        and not entry.endswith(":: Only")
    ]
    if not entries:
        raise ContextError("No maximum Python version found")
    return entries[-1].rsplit(" ")[-1]


def _get_project_version(project_dir: Path, package_name: str) -> str:
    init_file = project_dir / package_name / "__init__.py"
    if not init_file.exists():
        raise ContextError(f"File not found: {init_file}")

    if m := re.search(r'__version__ = "(.*)"', init_file.read_text()):
        return m.groups()[0]

    raise ContextError(f"Version not found in {init_file}")


def _get_nested_option(data: JSONDict, *keys: str) -> Any:
    """Return a value from a nested dict, if found."""
    for key in keys:
        if key not in data:
            return None
        data = data[key]
    return data
